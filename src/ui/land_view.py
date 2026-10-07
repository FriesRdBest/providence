from __future__ import annotations

from datetime import date

import streamlit as st

from src.domain.models import ProjectStatus, Workspace
from src.services.rule_engine import RuleEngine


def render_land_view(workspace: Workspace) -> None:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)

    st.header("Health")
    st.caption("Weekly organisational health and capacity overview")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        with st.container(border=True):
            st.metric(
                label="Team utilisation",
                value=f"{health.utilisation_percentage} %",
                delta=None,
            )

    with col2:
        with st.container(border=True):
            st.metric(
                label="Total budget",
                value=f"{health.total_budget_hours:,.0f} h",
            )
            st.metric(
                label="Remaining",
                value=f"{health.remaining_budget_hours:,.0f} h",
            )

    with col3:
        with st.container(border=True):
            st.metric(
                label="At risk",
                value=health.projects_at_risk,
                delta="Requires attention" if health.projects_at_risk > 0 else "None",
                delta_color="inverse",
            )
            st.metric(
                label="On watch",
                value=health.projects_on_watch,
                delta="Monitor closely" if health.projects_on_watch > 0 else "None",
                delta_color="normal",
            )

    st.subheader("Project health summary")

    for project in workspace.projects:
        status = project.status(today)
        status_label = {
            ProjectStatus.HEALTHY: "Healthy",
            ProjectStatus.WATCH: "Watch",
            ProjectStatus.AT_RISK: "At risk",
        }[status]

        with st.container(border=True):
            col_a, col_b = st.columns([3, 1], gap="large")

            with col_a:
                st.markdown(f"### {project.name}")
                st.caption(f"{project.client}")
                st.write(
                    f"Budget burn **{project.budget_burn_percentage} %** • "
                    f"{project.days_until_delivery(today)} days until delivery"
                )

            with col_b:
                if status == ProjectStatus.AT_RISK:
                    st.error(f"**{status_label}**")
                elif status == ProjectStatus.WATCH:
                    st.warning(f"**{status_label}**")
                else:
                    st.success(f"**{status_label}**")

            st.progress(
                float(project.budget_burn_percentage) / 100,
            )
