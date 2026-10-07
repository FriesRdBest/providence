from __future__ import annotations

import streamlit as st

from src.domain.models import ProjectStatus, Workspace


def render_sea_view(workspace: Workspace) -> None:
    today = st.context.date

    st.header("Sea")
    st.subheader("Daily project delivery status")

    filter_status = st.radio(
        "Filter by status",
        ("All", "Healthy", "Watch", "At risk"),
        index=0,
        horizontal=True,
    )

    filtered_projects = [
        project
        for project in workspace.projects
        if filter_status == "All"
        or (
            filter_status == "Healthy"
            and project.status(today) == ProjectStatus.HEALTHY
        )
        or (
            filter_status == "Watch"
            and project.status(today) == ProjectStatus.WATCH
        )
        or (
            filter_status == "At risk"
            and project.status(today) == ProjectStatus.AT_RISK
        )
    ]

    for project in filtered_projects:
        status = project.status(today)
        status_label = {
            ProjectStatus.HEALTHY: "Healthy",
            ProjectStatus.WATCH: "Watch",
            ProjectStatus.AT_RISK: "At risk",
        }[status]

        with st.container(border=True):
            st.subheader(project.name)
            st.caption(f"Client: {project.client}")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    label="Budget burn",
                    value=f"{project.budget_burn_percentage} %",
                )

            with col2:
                st.metric(
                    label="Budget remaining",
                    value=f"{project.budget_remaining_hours:,.1f} h",
                )

            with col3:
                st.metric(
                    label="Days until delivery",
                    value=project.days_until_delivery(today),
                )

            with col4:
                st.metric(
                    label="Status",
                    value=status_label,
                    delta=None,
                )

            st.progress(
                float(project.budget_burn_percentage) / 100,
                text="Budget utilisation",
            )

            if status == ProjectStatus.AT_RISK:
                st.warning(
                    "This project requires immediate attention due to budget or timeline pressure."
                )
            elif status == ProjectStatus.WATCH:
                st.info(
                    "This project is approaching a threshold. Monitor allocation closely."
                )
            else:
                st.success("This project is tracking within expected boundaries.")
