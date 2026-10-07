from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import Project, ProjectStatus, Workspace
from src.ui.components import (
    render_page_header,
    render_section_heading,
    render_status,
)


def _format_hours(value: Decimal) -> str:
    return f"{value:,.0f} h"


def _status_label(status: ProjectStatus) -> str:
    return {
        ProjectStatus.HEALTHY: "Healthy",
        ProjectStatus.WATCH: "Watch",
        ProjectStatus.AT_RISK: "At risk",
    }[status]


def _delivery_message(project: Project, today: date) -> str:
    status = project.status(today)
    days_remaining = project.days_until_delivery(today)

    if status == ProjectStatus.AT_RISK:
        return (
            f"Budget use has reached {project.budget_burn_percentage}% with "
            f"{days_remaining} days remaining. Review allocation today."
        )

    if status == ProjectStatus.WATCH:
        return f"Delivery is approaching a review boundary with {days_remaining} days remaining."

    return f"Delivery remains within current boundaries with {days_remaining} days remaining."


def _insight_copy(projects: list[Project], today: date) -> tuple[str, str]:
    if not projects:
        return (
            "No project data matches this view",
            "Change the current status filter to review active project delivery work.",
        )

    at_risk = [project for project in projects if project.status(today) == ProjectStatus.AT_RISK]
    if at_risk:
        priority_project = max(
            at_risk,
            key=lambda project: project.budget_burn_percentage,
        )
        return (
            f"{priority_project.name} needs immediate review",
            f"Budget use is {priority_project.budget_burn_percentage}% with "
            f"{priority_project.days_until_delivery(today)} days remaining. "
            "Protect remaining budget before assigning more work.",
        )

    on_watch = [project for project in projects if project.status(today) == ProjectStatus.WATCH]
    if on_watch:
        priority_project = min(
            on_watch,
            key=lambda project: project.days_until_delivery(today),
        )
        return (
            f"{priority_project.name} is nearest to a delivery boundary",
            f"{priority_project.days_until_delivery(today)} days remain until "
            "delivery. Review planned allocation before the next work period.",
        )

    return (
        "Current project pace is within boundaries",
        "No active project has reached a risk or watch threshold in this view.",
    )


def _sort_projects(
    projects: list[Project],
    sort_by: str,
    today: date,
) -> list[Project]:
    status_order = {
        ProjectStatus.AT_RISK: 0,
        ProjectStatus.WATCH: 1,
        ProjectStatus.HEALTHY: 2,
    }

    if sort_by == "Budget used":
        return sorted(
            projects,
            key=lambda project: (
                status_order[project.status(today)],
                -float(project.budget_burn_percentage),
            ),
        )

    if sort_by == "Project name":
        return sorted(projects, key=lambda project: project.name.lower())

    return sorted(
        projects,
        key=lambda project: (
            status_order[project.status(today)],
            project.days_until_delivery(today),
        ),
    )


def render_sea_view(workspace: Workspace) -> None:
    today = date.today()

    render_page_header(
        "Project",
        "Daily view of budget pace, delivery timing, and active work requiring attention.",
        today,
    )

    control_status, control_sort, control_count = st.columns(
        [1.15, 1.15, 0.7],
        gap="medium",
    )

    with control_status:
        filter_status = st.selectbox(
            "Status",
            ["All", "Healthy", "Watch", "At risk"],
            key="project_filter_status",
        )

    with control_sort:
        sort_by = st.selectbox(
            "Sort projects by",
            ["Delivery urgency", "Budget used", "Project name"],
            key="project_sort_by",
        )

    projects = [
        project
        for project in workspace.projects
        if filter_status == "All" or _status_label(project.status(today)) == filter_status
    ]
    projects = _sort_projects(projects, sort_by, today)

    with control_count:
        st.markdown(
            f"""
            <div class="providence-project-count">
                <span>Showing</span>
                <strong>{len(projects)}</strong>
                <small>projects</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    total_remaining = sum(
        (project.budget_remaining_hours for project in projects),
        Decimal("0"),
    )
    at_risk_count = sum(project.status(today) == ProjectStatus.AT_RISK for project in projects)
    watch_count = sum(project.status(today) == ProjectStatus.WATCH for project in projects)
    exposure = at_risk_count + watch_count

    st.markdown('<section class="providence-project-stage">', unsafe_allow_html=True)

    summary_active, summary_budget, summary_pressure = st.columns(3, gap="medium")

    with summary_active:
        st.markdown(
            f"""
            <article class="providence-project-metric providence-project-metric-violet">
                <span>Active projects</span>
                <strong>{len(projects)}</strong>
                <p>Current result set</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with summary_budget:
        st.markdown(
            f"""
            <article class="providence-project-metric providence-project-metric-pink">
                <span>Budget remaining</span>
                <strong>{_format_hours(total_remaining)}</strong>
                <p>Across visible projects</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with summary_pressure:
        pressure_copy = "Review required" if exposure > 0 else "Within current boundaries"
        st.markdown(
            f"""
            <article class="providence-project-metric providence-project-metric-coral">
                <span>Delivery pressure</span>
                <strong>{exposure}</strong>
                <p>{pressure_copy}</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    insight_title, insight_body = _insight_copy(projects, today)
    st.markdown(
        f"""
        <aside class="providence-project-decision">
            <div class="providence-project-kicker">Portfolio signal</div>
            <h2>{insight_title}</h2>
            <p>{insight_body}</p>
        </aside>
        """,
        unsafe_allow_html=True,
    )

    render_section_heading(
        "Active work",
        "Budget position and delivery timing for the current view",
    )

    if not projects:
        st.markdown(
            """
            <article class="providence-project-empty">
                <div class="providence-project-kicker">No matches</div>
                <h3>No projects match this view</h3>
                <p>Change the status filter to review other active project records.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</section>", unsafe_allow_html=True)
        return

    for project in projects:
        project_burn = min(float(project.budget_burn_percentage), 100)
        st.markdown(
            f"""
            <article class="providence-project-card">
                <div class="providence-project-card-main">
                    <h3>{project.name}</h3>
                    <p>{project.client}</p>
                    <div class="providence-project-card-progress">
                        <span style="width: {project_burn:.2f}%"></span>
                    </div>
                    <p class="providence-project-card-message">
                        {_delivery_message(project, today)}
                    </p>
                </div>
                <div class="providence-project-card-data">
                    <span>Budget used</span>
                    <strong>{project.budget_burn_percentage}%</strong>
                </div>
                <div class="providence-project-card-data">
                    <span>Logged</span>
                    <strong>{_format_hours(project.logged_hours)}</strong>
                </div>
                <div class="providence-project-card-data">
                    <span>Remaining</span>
                    <strong>{_format_hours(project.budget_remaining_hours)}</strong>
                </div>
                <div class="providence-project-card-data">
                    <span>Delivery</span>
                    <strong>{project.days_until_delivery(today)}d</strong>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )
        render_status(project.status(today))

    st.markdown("</section>", unsafe_allow_html=True)
