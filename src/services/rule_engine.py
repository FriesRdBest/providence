from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from src.domain.models import ProjectStatus, Workspace


@dataclass(frozen=True)
class WorkspaceHealth:
    utilisation_percentage: Decimal
    total_budget_hours: Decimal
    remaining_budget_hours: Decimal
    projects_at_risk: int
    projects_on_watch: int


class RuleEngine:
    def assess_workspace(self, workspace: Workspace, today: date | None = None) -> WorkspaceHealth:
        assessment_date = today or date.today()
        total_capacity = sum(
            (person.daily_capacity_hours for person in workspace.people),
            Decimal("0"),
        )
        total_logged = sum(
            (person.logged_hours_today for person in workspace.people),
            Decimal("0"),
        )
        total_budget = sum(
            (project.budget_hours for project in workspace.projects),
            Decimal("0"),
        )
        remaining_budget = sum(
            (project.budget_remaining_hours for project in workspace.projects),
            Decimal("0"),
        )
        statuses = [project.status(assessment_date) for project in workspace.projects]
        utilisation = Decimal("0")
        if total_capacity > Decimal("0"):
            utilisation = (total_logged / total_capacity * Decimal("100")).quantize(Decimal("0.1"))
        return WorkspaceHealth(
            utilisation_percentage=utilisation,
            total_budget_hours=total_budget,
            remaining_budget_hours=remaining_budget,
            projects_at_risk=statuses.count(ProjectStatus.AT_RISK),
            projects_on_watch=statuses.count(ProjectStatus.WATCH),
        )
