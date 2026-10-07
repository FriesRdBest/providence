from __future__ import annotations

import json
from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import ProjectStatus, Workspace
from src.services.report_service import build_detailed_pdf, build_executive_pdf
from src.services.rule_engine import RuleEngine
from src.ui.components import (
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


def _attention_copy(attention_count: int) -> str:
    if attention_count == 0:
        return "Clear"
    return "Review"


def render_overview_view(workspace: Workspace) -> None:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)
    total_budget = health.total_budget_hours
    total_logged = workspace.total_logged_hours
    overall_burn = workspace.overall_burn_percentage
    attention_count = health.projects_at_risk + health.projects_on_watch
    remaining_budget = health.remaining_budget_hours
    remaining_percent = max(0, min(100, 100 - float(overall_burn)))

    render_page_header(
        "Overview",
        "A clear picture of delivery pace, budget exposure, and current team capacity.",
        today,
    )

    st.markdown('<section class="providence-overview-stage">', unsafe_allow_html=True)

    hero_column, insight_column = st.columns([1, 1], gap="large")

    with hero_column:
        st.markdown(
            f"""
            <article class="providence-overview-hero">
                <div class="providence-overview-hero-topline">
                    <span class="providence-overview-kicker">Delivery pulse</span>
                    <span class="providence-overview-live"><i></i> Live workspace view</span>
                </div>
                <div class="providence-overview-hero-grid">
                    <div>
                        <div class="providence-overview-hero-label">Budget position</div>
                        <div class="providence-overview-burn">{overall_burn}%</div>
                        <p class="providence-overview-hero-copy">
                            of active project budget has been used across the workspace
                        </p>
                    </div>
                    <div class="providence-overview-orbit" aria-label="Budget remaining">
                        <span>{remaining_percent:.0f}%</span>
                        <small>remaining</small>
                    </div>
                </div>
                <div class="providence-overview-pace">
                    <div class="providence-overview-pace-track">
                        <span style="width: {min(float(overall_burn), 100):.2f}%"></span>
                    </div>
                    <div class="providence-overview-pace-labels">
                        <span>Budget pace</span>
                        <span>{_format_hours(remaining_budget)} available</span>
                    </div>
                </div>
                <div class="providence-overview-hero-stats">
                    <div>
                        <span>Total budget</span>
                        <strong>{_format_hours(total_budget)}</strong>
                    </div>
                    <div>
                        <span>Logged</span>
                        <strong>{_format_hours(total_logged)}</strong>
                    </div>
                    <div>
                        <span>Remaining</span>
                        <strong>{_format_hours(remaining_budget)}</strong>
                    </div>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with insight_column:
        insight_title, insight_body = _insight_copy(
            health.projects_at_risk,
            health.projects_on_watch,
            remaining_budget,
        )
        st.markdown(
            f"""
            <aside class="providence-overview-decision">
                <div class="providence-overview-decision-orb"></div>
                <div class="providence-overview-kicker">Decision support</div>
                <h2>{insight_title}</h2>
                <p>{insight_body}</p>
                <div class="providence-overview-decision-foot">
                    <span>Workspace signal</span>
                    <strong>{_attention_copy(attention_count)}</strong>
                </div>
            </aside>
            """,
            unsafe_allow_html=True,
        )

    metric_one, metric_two, metric_three = st.columns([1, 1, 1], gap="medium")

    with metric_one:
        st.markdown(
            f"""
            <article class="providence-overview-metric providence-overview-metric-violet">
                <span class="providence-overview-metric-label">Team utilisation</span>
                <strong>{health.utilisation_percentage}%</strong>
                <p>Current capacity use across the workspace</p>
                <div class="providence-overview-metric-line">
                    <span
                        style="width: {min(float(health.utilisation_percentage), 100):.2f}%"
                    ></span>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with metric_two:
        st.markdown(
            f"""
            <article class="providence-overview-metric providence-overview-metric-pink">
                <span class="providence-overview-metric-label">Active projects</span>
                <strong>{len(workspace.projects)}</strong>
                <p>Delivery commitments in the current view</p>
                <div class="providence-overview-metric-dots">
                    <i></i><i></i><i></i>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with metric_three:
        attention_description = (
            "No projects currently need attention"
            if attention_count == 0
            else "Projects need a closer delivery review"
        )
        st.markdown(
            f"""
            <article class="providence-overview-metric providence-overview-metric-coral">
                <span class="providence-overview-metric-label">Attention needed</span>
                <strong>{attention_count}</strong>
                <p>{attention_description}</p>
                <div class="providence-overview-attention-badge">
                    {_attention_copy(attention_count)}
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    project_column, snapshot_column = st.columns([1.45, 0.85], gap="large")

    with project_column:
        render_section_heading("Project focus", "Budget pace and delivery timing")
        if not workspace.projects:
            st.markdown(
                """
                <article class="providence-overview-empty">
                    <div class="providence-overview-kicker">Portfolio</div>
                    <h3>No active projects are available</h3>
                    <p>Add project records to reveal budget pace and delivery timing.</p>
                </article>
                """,
                unsafe_allow_html=True,
            )
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

            for index, project in enumerate(ranked_projects[:3], start=1):
                burn_width = min(float(project.budget_burn_percentage), 100)
                st.markdown(
                    f"""
                    <article class="providence-overview-project">
                        <div class="providence-overview-project-index">0{index}</div>
                        <div class="providence-overview-project-main">
                            <div class="providence-overview-project-title-row">
                                <div>
                                    <h3>{project.name}</h3>
                                    <p>{project.client}</p>
                                </div>
                            </div>
                            <div class="providence-overview-project-progress">
                                <span style="width: {burn_width:.2f}%"></span>
                            </div>
                        </div>
                        <div class="providence-overview-project-data">
                            <span>Budget used</span>
                            <strong>{project.budget_burn_percentage}%</strong>
                        </div>
                        <div class="providence-overview-project-data">
                            <span>Delivery</span>
                            <strong>{project.days_until_delivery(today)}d</strong>
                        </div>
                    </article>
                    """,
                    unsafe_allow_html=True,
                )
                render_status(project.status(today))

    with snapshot_column:
        render_section_heading("Workspace signals", "What needs attention")

        st.markdown(
            f"""
            <article class="providence-overview-signal-grid">
                <div class="providence-overview-signal providence-overview-signal-risk">
                    <span>At risk</span>
                    <strong>{health.projects_at_risk}</strong>
                    <p>Immediate review</p>
                </div>
                <div class="providence-overview-signal providence-overview-signal-watch">
                    <span>On watch</span>
                    <strong>{health.projects_on_watch}</strong>
                    <p>Monitor pace</p>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

        people_count = len(workspace.people)
        st.markdown(
            f"""
            <article class="providence-overview-people">
                <div>
                    <span class="providence-overview-kicker">Capacity view</span>
                    <h3>{people_count} people tracked</h3>
                    <p>Current workspace capacity is reflected in the utilisation signal.</p>
                </div>
                <div class="providence-overview-people-mark">
                    <span>{health.utilisation_percentage}%</span>
                    <small>used</small>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <section class="providence-overview-export">
            <div>
                <div class="providence-overview-kicker">Workspace record</div>
                <h3>Take the current delivery picture with you</h3>
                <p>Create a portable summary for review outside Providence.</p>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    executive_pdf, detailed_pdf, json_export = st.columns(3, gap="small")

    with executive_pdf:
        st.download_button(
            label="Executive PDF",
            data=build_executive_pdf(workspace, today=today),
            file_name="providence_executive_summary.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    with detailed_pdf:
        st.download_button(
            label="Detailed PDF",
            data=build_detailed_pdf(workspace, today=today),
            file_name="providence_detailed_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    with json_export:
        st.download_button(
            label="JSON data",
            data=_export_document(workspace),
            file_name="providence_workspace_data.json",
            mime="application/json",
            use_container_width=True,
        )

    st.markdown("</section>", unsafe_allow_html=True)
