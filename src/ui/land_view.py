from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import ProjectStatus, Workspace
from src.services.rule_engine import RuleEngine
from src.ui.components import (
    render_page_header,
    render_section_heading,
    render_status,
)


def _format_hours(value: Decimal) -> str:
    return f"{value:,.0f} h"


def _delivery_insight(
    projects_at_risk: int,
    projects_on_watch: int,
    remaining_budget: Decimal,
) -> tuple[str, str]:
    if projects_at_risk > 0:
        project_word = "project" if projects_at_risk == 1 else "projects"
        return (
            f"{projects_at_risk} {project_word} require immediate attention",
            "Current budget pace and delivery timing show active exposure. "
            "Protect remaining capacity before the next allocation decision.",
        )

    if projects_on_watch > 0:
        project_word = "project" if projects_on_watch == 1 else "projects"
        return (
            f"{projects_on_watch} {project_word} need close review",
            "No project has crossed a critical boundary, but delivery pace should be "
            "reviewed before work is allocated for the next period.",
        )

    return (
        "Delivery remains within current boundaries",
        f"{_format_hours(remaining_budget)} remains across active budgets. "
        "Maintain the current review cadence as delivery work progresses.",
    )


def _budget_interpretation(
    overall_burn: Decimal,
    projects_at_risk: int,
    projects_on_watch: int,
) -> str:
    if projects_at_risk > 0:
        return "Budget pace requires immediate management attention."
    if projects_on_watch > 0:
        return "Budget pace is stable, with emerging pressure in selected project work."
    if overall_burn >= Decimal("70"):
        return "Budget use is advanced. Keep delivery pace under close review."
    return "Budget use remains within current delivery boundaries."


def render_land_view(workspace: Workspace) -> None:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)
    total_logged = workspace.total_logged_hours
    overall_burn = workspace.overall_burn_percentage
    total_capacity = sum(
        (person.daily_capacity_hours for person in workspace.people),
        Decimal("0"),
    )
    capacity_remaining = max(
        Decimal("0"),
        total_capacity
        - sum(
            (person.logged_hours_today for person in workspace.people),
            Decimal("0"),
        ),
    )
    exposure_count = health.projects_at_risk + health.projects_on_watch
    burn_width = min(float(overall_burn), 100)

    render_page_header(
        "Health",
        "Weekly view of delivery pace, budget boundaries, and emerging project pressure.",
        today,
    )

    st.markdown('<section class="providence-health-stage">', unsafe_allow_html=True)

    triage_column, decision_column = st.columns([1, 1], gap="large")

    with triage_column:
        capacity_note = (
            f"{_format_hours(capacity_remaining)} capacity remaining"
            if total_capacity > 0
            else "Capacity data is not available"
        )
        st.markdown(
            f"""
            <article class="providence-health-hero">
                <div class="providence-health-hero-topline">
                    <span class="providence-health-kicker">Weekly triage</span>
                    <span class="providence-health-live"><i></i> {capacity_note}</span>
                </div>
                <div class="providence-health-hero-grid">
                    <div>
                        <span class="providence-health-hero-label">Overall budget used</span>
                        <strong>{overall_burn}%</strong>
                        <p>{
                _budget_interpretation(
                    overall_burn,
                    health.projects_at_risk,
                    health.projects_on_watch,
                )
            }</p>
                    </div>
                    <div class="providence-health-orbit">
                        <span>{health.utilisation_percentage}%</span>
                        <small>team use</small>
                    </div>
                </div>
                <div class="providence-health-pace">
                    <div class="providence-health-pace-track">
                        <span style="width: {burn_width:.2f}%"></span>
                    </div>
                    <div class="providence-health-pace-labels">
                        <span>Budget pace</span>
                        <span>{_format_hours(health.remaining_budget_hours)} left</span>
                    </div>
                </div>
                <div class="providence-health-hero-stats">
                    <div>
                        <span>Total budget</span>
                        <strong>{_format_hours(health.total_budget_hours)}</strong>
                    </div>
                    <div>
                        <span>Logged</span>
                        <strong>{_format_hours(total_logged)}</strong>
                    </div>
                    <div>
                        <span>Remaining</span>
                        <strong>{_format_hours(health.remaining_budget_hours)}</strong>
                    </div>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with decision_column:
        insight_title, insight_body = _delivery_insight(
            health.projects_at_risk,
            health.projects_on_watch,
            health.remaining_budget_hours,
        )
        st.markdown(
            f"""
            <aside class="providence-health-decision">
                <div class="providence-health-kicker">Triage signal</div>
                <h2>{insight_title}</h2>
                <p>{insight_body}</p>
                <div class="providence-health-decision-foot">
                    <span>Delivery exposure</span>
                    <strong>{exposure_count}</strong>
                </div>
            </aside>
            """,
            unsafe_allow_html=True,
        )

    signal_risk, signal_watch, signal_capacity = st.columns(3, gap="medium")

    with signal_risk:
        st.markdown(
            f"""
            <article class="providence-health-signal providence-health-signal-risk">
                <span>At risk</span>
                <strong>{health.projects_at_risk}</strong>
                <p>Immediate allocation review</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with signal_watch:
        st.markdown(
            f"""
            <article class="providence-health-signal providence-health-signal-watch">
                <span>On watch</span>
                <strong>{health.projects_on_watch}</strong>
                <p>Approaching a boundary</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with signal_capacity:
        st.markdown(
            f"""
            <article class="providence-health-signal providence-health-signal-capacity">
                <span>Capacity</span>
                <strong>{_format_hours(capacity_remaining)}</strong>
                <p>Available across tracked people</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    render_section_heading(
        "Project health",
        "Budget position and delivery timing across active work",
    )

    if not workspace.projects:
        st.markdown(
            """
            <article class="providence-health-empty">
                <div class="providence-health-kicker">No health data</div>
                <h3>Active project records are not available</h3>
                <p>Health information will appear when project records are added.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</section>", unsafe_allow_html=True)
        return

    status_order = {
        ProjectStatus.AT_RISK: 0,
        ProjectStatus.WATCH: 1,
        ProjectStatus.HEALTHY: 2,
    }
    ranked_projects = sorted(
        workspace.projects,
        key=lambda project: (
            status_order[project.status(today)],
            -float(project.budget_burn_percentage),
        ),
    )

    for project in ranked_projects:
        project_burn = min(float(project.budget_burn_percentage), 100)
        st.markdown(
            f"""
            <article class="providence-health-project">
                <div class="providence-health-project-main">
                    <h3>{project.name}</h3>
                    <p>{project.client}</p>
                    <div class="providence-health-project-progress">
                        <span style="width: {project_burn:.2f}%"></span>
                    </div>
                </div>
                <div class="providence-health-project-data">
                    <span>Budget used</span>
                    <strong>{project.budget_burn_percentage}%</strong>
                    <small>{_format_hours(project.budget_remaining_hours)} left</small>
                </div>
                <div class="providence-health-project-data">
                    <span>Delivery</span>
                    <strong>{project.days_until_delivery(today)}d</strong>
                    <small>Time remaining</small>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )
        render_status(project.status(today))

    st.markdown("</section>", unsafe_allow_html=True)
