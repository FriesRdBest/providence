from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import ProjectStatus, Workspace
from src.services.rule_engine import RuleEngine
from src.ui.components import (
    render_insight,
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

    render_page_header(
        "Health",
        "Weekly view of delivery pace, budget boundaries, and emerging project pressure.",
        today,
    )

    capacity_column, budget_column, exposure_column = st.columns([1, 1.35, 1], gap="medium")

    with capacity_column:
        with st.container(border=True):
            st.metric(
                label="Team utilisation",
                value=f"{health.utilisation_percentage}%",
                delta=(
                    f"{_format_hours(capacity_remaining)} capacity remaining"
                    if total_capacity > 0
                    else "Capacity data is not available"
                ),
                delta_color="off",
            )

    with budget_column:
        with st.container(border=True):
            st.metric(
                label="Budget remaining",
                value=_format_hours(health.remaining_budget_hours),
                delta=f"Of {_format_hours(health.total_budget_hours)} total budget",
                delta_color="off",
            )

    with exposure_column:
        with st.container(border=True):
            exposure_count = health.projects_at_risk + health.projects_on_watch
            st.metric(
                label="Delivery exposure",
                value=exposure_count,
                delta=("Review required" if exposure_count > 0 else "No current exposure"),
                delta_color="inverse" if exposure_count > 0 else "off",
            )

    render_section_heading(
        "Budget pace",
        "Current use against active project budgets",
    )

    pace_column, exposure_detail_column = st.columns([1.65, 1], gap="large")

    with pace_column:
        with st.container(border=True):
            st.markdown(
                """
                <div class="providence-health-hero-label">Overall budget used</div>
                <div class="providence-health-hero-value">"""
                f"{overall_burn}%"
                """</div>
                <div class="providence-health-hero-copy">"""
                f"{
                    _budget_interpretation(
                        overall_burn,
                        health.projects_at_risk,
                        health.projects_on_watch,
                    )
                }"
                """</div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(min(float(overall_burn) / 100, 1.0))
            budget_total, budget_used, budget_remaining = st.columns(3, gap="small")
            with budget_total:
                st.markdown(
                    '<div class="providence-health-stat-label">Budget</div>'
                    f'<div class="providence-health-stat-value">'
                    f"{_format_hours(health.total_budget_hours)}</div>",
                    unsafe_allow_html=True,
                )
            with budget_used:
                st.markdown(
                    '<div class="providence-health-stat-label">Used</div>'
                    f'<div class="providence-health-stat-value">'
                    f"{_format_hours(total_logged)}</div>",
                    unsafe_allow_html=True,
                )
            with budget_remaining:
                st.markdown(
                    '<div class="providence-health-stat-label">Remaining</div>'
                    f'<div class="providence-health-stat-value">'
                    f"{_format_hours(health.remaining_budget_hours)}</div>",
                    unsafe_allow_html=True,
                )

    with exposure_detail_column:
        with st.container(border=True):
            st.markdown(
                '<div class="providence-health-exposure-title">Delivery exposure</div>',
                unsafe_allow_html=True,
            )
            risk_column, watch_column = st.columns(2, gap="small")
            with risk_column:
                st.markdown(
                    '<div class="providence-preview-label">At risk</div>'
                    f'<div class="providence-health-number providence-health-number-risk">'
                    f"{health.projects_at_risk}</div>",
                    unsafe_allow_html=True,
                )
                st.caption("Requires immediate attention")
            with watch_column:
                st.markdown(
                    '<div class="providence-preview-label">On watch</div>'
                    f'<div class="providence-health-number providence-health-number-watch">'
                    f"{health.projects_on_watch}</div>",
                    unsafe_allow_html=True,
                )
                st.caption("Approaching a delivery boundary")

    insight_title, insight_body = _delivery_insight(
        health.projects_at_risk,
        health.projects_on_watch,
        health.remaining_budget_hours,
    )
    render_insight(insight_title, insight_body)

    render_section_heading(
        "Project health",
        "Budget position and delivery timing across active work",
    )

    if not workspace.projects:
        with st.container(border=True):
            st.markdown(
                '<div class="providence-empty-title">No project health data is available</div>'
                '<p class="providence-empty-copy">'
                "Health information will appear here when active project records are available."
                "</p>",
                unsafe_allow_html=True,
            )
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
        with st.container(border=True):
            identity_column, budget_column, delivery_column, status_column = st.columns(
                [2.1, 1.15, 1.15, 0.85],
                gap="medium",
            )
            with identity_column:
                st.markdown(f"### {project.name}")
                st.caption(project.client)
            with budget_column:
                st.markdown(
                    '<div class="providence-preview-label">Budget used</div>'
                    f'<div class="providence-health-row-value">'
                    f"{project.budget_burn_percentage}%</div>",
                    unsafe_allow_html=True,
                )
                st.caption(f"{_format_hours(project.budget_remaining_hours)} remaining")
            with delivery_column:
                st.markdown(
                    '<div class="providence-preview-label">Delivery</div>'
                    f'<div class="providence-health-row-value">'
                    f"{project.days_until_delivery(today)} days</div>",
                    unsafe_allow_html=True,
                )
                st.caption("Time remaining")
            with status_column:
                render_status(project.status(today))

            st.progress(min(float(project.budget_burn_percentage) / 100, 1.0))
