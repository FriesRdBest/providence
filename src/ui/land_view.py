from __future__ import annotations

import streamlit as st

from src.domain.models import ProjectStatus, Workspace
from src.services.rule_engine import RuleEngine


def render_land_view(workspace: Workspace) -> None:
    today = st.context.date
    health = RuleEngine().assess_workspace(workspace, today=today)

    st.header("Land")
    st.subheader("Weekly organisational health")

    with st.container(border=True):
        st.metric(
            label="Team utilisation",
            value=f"{health.utilisation_percentage} %",
            delta=None,
        )

    with st.container(border=True):
        st.metric(
            label="Total budget hours",
            value=f"{health.total_budget_hours:,.0f} h",
        )
        st.metric(
            label="Remaining budget hours",
            value=f"{health.remaining_budget_hours:,.0f} h",
        )

    with st.container(border=True):
        st.metric(
            label="Projects at risk",
            value=health.projects_at_risk,
            delta="Requires attention" if health.projects_at_risk > 0 else "None",
            delta_color="inverse",
        )
        st.metric(
            label="Projects on watch",
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

        st.write(
            f"**{project.name}** ({project.client}) — "
            f"Budget burn {project.budget_burn_percentage} %, "
            f"{project.days_until_delivery(today)} days until delivery — "
            f"Status: {status_label}"
        )
