from __future__ import annotations

import json
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


def _insight_copy(
    projects_at_risk: int,
    projects_on_watch: int,
    remaining_budget: Decimal,
) -> tuple[str, str]:
    if projects_at_risk > 0:
        project_word = "project" if projects_at_risk == 1 else "projects"
        return (
            f"{projects_at_risk} {project_word} need attention",
            "Current delivery conditions show immediate risk. Review Health to understand "
            "budget pace and delivery pressure before making allocation decisions.",
        )

    if projects_on_watch > 0:
        project_word = "project" if projects_on_watch == 1 else "projects"
        return (
            f"{projects_on_watch} {project_word} are on watch",
            "Delivery remains within current boundaries, but the next allocation decision "
            "should protect remaining budget and delivery time.",
        )

    return (
        "Delivery is within current boundaries",
        f"{_format_hours(remaining_budget)} remains across active project budgets. "
        "Continue to review pace as work moves through the week.",
    )


def _export_document(workspace: Workspace) -> str:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)

    document = {
        "application": "Providence",
        "generated_on": str(today),
        "overview": {
            "team_utilisation": str(health.utilisation_percentage),
            "projects_tracked": len(workspace.projects),
            "people_tracked": len(workspace.people),
            "remaining_budget_hours": str(health.remaining_budget_hours),
            "projects_at_risk": health.projects_at_risk,
            "projects_on_watch": health.projects_on_watch,
        },
        "projects": [
            {
                "name": project.name,
                "client": project.client,
                "budget_hours": str(project.budget_hours),
                "logged_hours": str(project.logged_hours),
                "remaining_hours": str(project.budget_remaining_hours),
                "budget_burn": str(project.budget_burn_percentage),
                "days_until_delivery": project.days_until_delivery(today),
                "status": project.status(today).value,
            }
            for project in workspace.projects
        ],
    }
    return json.dumps(document, indent=2)


def render_overview_view(workspace: Workspace) -> None:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)
    total_budget = health.total_budget_hours
    total_logged = workspace.total_logged_hours
    overall_burn = workspace.overall_burn_percentage
    attention_count = health.projects_at_risk + health.projects_on_watch

    render_page_header(
        "Overview",
        today,
    )

    summary_one, summary_two, summary_three, summary_four = st.columns(4, gap="medium")

    with summary_one:
        with st.container(border=True):
            st.metric(
                label="Team utilisation",
                value=f"{health.utilisation_percentage}%",
                delta="Current capacity use",
                delta_color="off",
            )

    with summary_two:
        with st.container(border=True):
            st.metric(
                label="Active projects",
                value=len(workspace.projects),
                delta="Current delivery work",
                delta_color="off",
            )

    with summary_three:
        with st.container(border=True):
            st.metric(
                label="Budget remaining",
                value=_format_hours(health.remaining_budget_hours),
                delta=f"Of {_format_hours(total_budget)} total",
                delta_color="off",
            )

    with summary_four:
        with st.container(border=True):
            attention_label = (
                "No projects need attention" if attention_count == 0 else "Review today"
            )
            st.metric(
                label="Attention needed",
                value=attention_count,
                delta=attention_label,
                delta_color="inverse" if attention_count > 0 else "off",
            )

    render_section_heading(
        "Delivery pulse",
        "Current budget pace across active work",
    )

    hero_column, insight_column = st.columns([1.7, 1], gap="large")

    with hero_column:
        with st.container(border=True):
            st.markdown(
                """
                <div class="providence-hero-label">Budget position</div>
                <div class="providence-hero-value">"""
                f"{overall_burn}%"
                """</div>
                <div class="providence-hero-copy">
                    of active project budget has been used across the workspace
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(min(float(overall_burn) / 100, 1.0))
            pace_one, pace_two, pace_three = st.columns(3, gap="small")
            with pace_one:
                st.markdown(
                    f'<div class="providence-hero-stat-label">Budget</div>'
                    f'<div class="providence-hero-stat-value">{_format_hours(total_budget)}</div>',
                    unsafe_allow_html=True,
                )
            with pace_two:
                st.markdown(
                    f'<div class="providence-hero-stat-label">Used</div>'
                    f'<div class="providence-hero-stat-value">{_format_hours(total_logged)}</div>',
                    unsafe_allow_html=True,
                )
            with pace_three:
                st.markdown(
                    f'<div class="providence-hero-stat-label">Remaining</div>'
                    f'<div class="providence-hero-stat-value">'
                    f"{_format_hours(health.remaining_budget_hours)}</div>",
                    unsafe_allow_html=True,
                )

    with insight_column:
        insight_title, insight_body = _insight_copy(
            health.projects_at_risk,
            health.projects_on_watch,
            health.remaining_budget_hours,
        )
        render_insight(insight_title, insight_body)

    preview_left, preview_right = st.columns([1.1, 1], gap="large")

    with preview_left:
        render_section_heading("Project focus", "Budget pace and delivery timing")
        if not workspace.projects:
            with st.container(border=True):
                st.caption("No active projects are available in this workspace.")
        else:
            ranked_projects = sorted(
                workspace.projects,
                key=lambda project: (
                    project.status(today) == ProjectStatus.AT_RISK,
                    project.status(today) == ProjectStatus.WATCH,
                    float(project.budget_burn_percentage),
                ),
                reverse=True,
            )

            for project in ranked_projects[:3]:
                with st.container(border=True):
                    top_left, top_right = st.columns([3, 1], gap="small")
                    with top_left:
                        st.markdown(f"### {project.name}")
                        st.caption(project.client)
                    with top_right:
                        render_status(project.status(today))

                    project_meta_left, project_meta_right = st.columns(2, gap="small")
                    with project_meta_left:
                        st.markdown(
                            f'<div class="providence-preview-label">Budget used</div>'
                            f'<div class="providence-preview-value">'
                            f"{project.budget_burn_percentage}%</div>",
                            unsafe_allow_html=True,
                        )
                    with project_meta_right:
                        st.markdown(
                            f'<div class="providence-preview-label">Delivery</div>'
                            f'<div class="providence-preview-value">'
                            f"{project.days_until_delivery(today)} days</div>",
                            unsafe_allow_html=True,
                        )
                    st.progress(min(float(project.budget_burn_percentage) / 100, 1.0))

    with preview_right:
        render_section_heading("Health snapshot", "Current delivery exposure")
        with st.container(border=True):
            health_left, health_right = st.columns(2, gap="medium")
            with health_left:
                st.markdown(
                    '<div class="providence-preview-label">At risk</div>'
                    f'<div class="providence-health-number providence-health-number-risk">'
                    f"{health.projects_at_risk}</div>",
                    unsafe_allow_html=True,
                )
                st.caption("Projects requiring immediate attention")
            with health_right:
                st.markdown(
                    '<div class="providence-preview-label">On watch</div>'
                    f'<div class="providence-health-number providence-health-number-watch">'
                    f"{health.projects_on_watch}</div>",
                    unsafe_allow_html=True,
                )
                st.caption("Projects approaching a delivery boundary")

        render_section_heading("People snapshot", "Current capacity visibility")
        with st.container(border=True):
            people_count = len(workspace.people)
            if people_count == 0:
                st.markdown(
                    '<div class="providence-empty-title">Capacity data is not available yet</div>'
                    '<p class="providence-empty-copy">'
                    "People activity will appear here when workspace capacity records "
                    "are available."
                    "</p>",
                    unsafe_allow_html=True,
                )
            else:
                st.metric(
                    label="People tracked",
                    value=people_count,
                    delta="Current workspace capacity",
                    delta_color="off",
                )

    st.markdown('<div class="providence-export-area">', unsafe_allow_html=True)
    export_left, export_right = st.columns([3, 1], gap="large")
    with export_left:
        st.markdown(
            '<div class="providence-export-title">Workspace summary</div>'
            '<p class="providence-export-copy">'
            "Create a portable record of the current delivery picture "
            "for review outside Providence."
            "</p>",
            unsafe_allow_html=True,
        )
    with export_right:
        st.download_button(
            label="Export summary",
            data=_export_document(workspace),
            file_name="providence_summary.json",
            mime="application/json",
            use_container_width=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
