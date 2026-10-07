from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import Project, ProjectStatus, Workspace
from src.ui.components import (
    render_insight,
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
        priority_project = max(at_risk, key=lambda project: project.budget_burn_percentage)
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
            f"{priority_project.days_until_delivery(today)} days remain until delivery. "
            "Review planned allocation before the next work period.",
        )

    return (
        "Current project pace is within boundaries",
        "No active project has reached a risk or watch threshold in this view.",
    )


def _sort_projects(projects: list[Project], sort_by: str, today: date) -> list[Project]:
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

    control_status, control_sort, control_count = st.columns([1.15, 1.15, 0.7], gap="medium")

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
            '<div class="providence-project-count-label">Showing</div>'
            f'<div class="providence-project-count-value">{len(projects)}</div>'
            '<div class="providence-project-count-copy">projects</div>',
            unsafe_allow_html=True,
        )

    total_remaining = sum(
        (project.budget_remaining_hours for project in projects),
        Decimal("0"),
    )
    at_risk_count = sum(project.status(today) == ProjectStatus.AT_RISK for project in projects)
    watch_count = sum(project.status(today) == ProjectStatus.WATCH for project in projects)

    summary_one, summary_two, summary_three = st.columns(3, gap="medium")

    with summary_one:
        with st.container(border=True):
            st.metric(
                label="Active projects",
                value=len(projects),
                delta="Current result set",
                delta_color="off",
            )

    with summary_two:
        with st.container(border=True):
            st.metric(
                label="Budget remaining",
                value=_format_hours(total_remaining),
                delta="Across visible projects",
                delta_color="off",
            )

    with summary_three:
        with st.container(border=True):
            exposure = at_risk_count + watch_count
            st.metric(
                label="Delivery pressure",
                value=exposure,
                delta=("Review required" if exposure > 0 else "Within current boundaries"),
                delta_color="inverse" if exposure > 0 else "off",
            )

    insight_title, insight_body = _insight_copy(projects, today)
    render_insight(insight_title, insight_body)

    render_section_heading(
        "Active work",
        "Budget position and delivery timing for the current view",
    )

    if not projects:
        with st.container(border=True):
            st.markdown(
                '<div class="providence-empty-title">No projects match this view</div>'
                '<p class="providence-empty-copy">'
                "Change the current status filter to view other active project records."
                "</p>",
                unsafe_allow_html=True,
            )
        return

    for project in projects:
        with st.container(border=True):
            top_left, top_right = st.columns([3.1, 0.9], gap="medium")
            with top_left:
                st.markdown(f"### {project.name}")
                st.caption(project.client)
            with top_right:
                render_status(project.status(today))

            metric_one, metric_two, metric_three, metric_four = st.columns(
                4,
                gap="small",
            )

            with metric_one:
                st.markdown(
                    '<div class="providence-preview-label">Budget used</div>'
                    f'<div class="providence-project-value">'
                    f"{project.budget_burn_percentage}%</div>",
                    unsafe_allow_html=True,
                )

            with metric_two:
                st.markdown(
                    '<div class="providence-preview-label">Logged</div>'
                    f'<div class="providence-project-value">'
                    f"{_format_hours(project.logged_hours)}</div>",
                    unsafe_allow_html=True,
                )

            with metric_three:
                st.markdown(
                    '<div class="providence-preview-label">Remaining</div>'
                    f'<div class="providence-project-value">'
                    f"{_format_hours(project.budget_remaining_hours)}</div>",
                    unsafe_allow_html=True,
                )

            with metric_four:
                st.markdown(
                    '<div class="providence-preview-label">Delivery</div>'
                    f'<div class="providence-project-value">'
                    f"{project.days_until_delivery(today)} days</div>",
                    unsafe_allow_html=True,
                )

            st.progress(min(float(project.budget_burn_percentage) / 100, 1.0))
            st.markdown(
                f'<p class="providence-project-message">{_delivery_message(project, today)}</p>',
                unsafe_allow_html=True,
            )
