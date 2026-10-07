from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from src.domain.models import ProjectStatus, Workspace


@dataclass(frozen=True)
class InsightResponse:
    query: str
    answer: str
    confidence: str
    supporting_facts: tuple[str, ...]


class AIInsightService:
    def answer_query(self, workspace: Workspace, query: str, today: date | None = None) -> InsightResponse:
        assessment_date = today or date.today()
        query_lower = query.lower()

        if "budget depletion" in query_lower or "budget" in query_lower and "week" in query_lower:
            return self._budget_depletion_insight(workspace, assessment_date, query)

        if "overbooked" in query_lower or "capacity" in query_lower and "people" in query_lower:
            return self._capacity_insight(workspace, assessment_date, query)

        if "risk" in query_lower or "at risk" in query_lower:
            return self._risk_insight(workspace, assessment_date, query)

        return InsightResponse(
            query=query,
            answer="I cannot answer this query with the current data model. Try asking about budget depletion, overbooked people, or project risk.",
            confidence="low",
            supporting_facts=("Query does not match supported insight patterns",),
        )

    def _budget_depletion_insight(
        self, workspace: Workspace, today: date, query: str
    ) -> InsightResponse:
        at_risk_projects = [
            project for project in workspace.projects if project.status(today) == ProjectStatus.AT_RISK
        ]

        if not at_risk_projects:
            return InsightResponse(
                query=query,
                answer="No active project faces immediate budget depletion this week. All projects are within acceptable burn boundaries.",
                confidence="high",
                supporting_facts=("No projects classified as at risk",),
            )

        most_critical = max(
            at_risk_projects,
            key=lambda p: float(p.budget_burn_percentage),
        )

        facts = (
            f"{most_critical.name} has {most_critical.budget_burn_percentage} % budget burn",
            f"{most_critical.days_until_delivery(today)} days remain until delivery",
            f"{len(at_risk_projects)} project or projects are classified as at risk",
        )

        return InsightResponse(
            query=query,
            answer=(
                f"{most_critical.name} faces immediate budget depletion. "
                f"Budget burn stands at {most_critical.budget_burn_percentage} % with "
                f"{most_critical.days_until_delivery(today)} days until delivery."
            ),
            confidence="high",
            supporting_facts=facts,
        )

    def _capacity_insight(
        self, workspace: Workspace, today: date, query: str
    ) -> InsightResponse:
        from src.domain.models import PersonStatus

        overbooked_people = [
            person for person in workspace.people if person.status == PersonStatus.OVERBOOKED
        ]
        missing_time_people = [
            person for person in workspace.people if person.status == PersonStatus.MISSING_TIME
        ]

        facts: list[str] = []

        if overbooked_people:
            facts.append(f"{len(overbooked_people)} person or people are overbooked today")

        if missing_time_people:
            facts.append(f"{len(missing_time_people)} person or people have not logged time today")

        if not facts:
            return InsightResponse(
                query=query,
                answer="All people are within capacity boundaries and have logged time today.",
                confidence="high",
                supporting_facts=("No capacity alerts detected",),
            )

        return InsightResponse(
            query=query,
            answer="Capacity alerts detected. Review the Air view for detailed person level information.",
            confidence="medium",
            supporting_facts=tuple(facts),
        )

    def _risk_insight(
        self, workspace: Workspace, today: date, query: str
    ) -> InsightResponse:
        at_risk_projects = [
            project for project in workspace.projects if project.status(today) == ProjectStatus.AT_RISK
        ]
        watch_projects = [
            project for project in workspace.projects if project.status(today) == ProjectStatus.WATCH
        ]

        facts: list[str] = []

        if at_risk_projects:
            facts.append(f"{len(at_risk_projects)} project or projects are at risk")

        if watch_projects:
            facts.append(f"{len(watch_projects)} project or projects are on watch")

        if not facts:
            return InsightResponse(
                query=query,
                answer="No projects are currently classified as at risk. All projects are tracking within expected boundaries.",
                confidence="high",
                supporting_facts=("No risk alerts detected",),
            )

        return InsightResponse(
            query=query,
            answer="Project risk alerts detected. Review the Land and Sea views for detailed project level information.",
            confidence="medium",
            supporting_facts=tuple(facts),
        )
