import streamlit as st
from src.domain.models import Workspace, ProjectStatus


def render(workspace: Workspace, today) -> None:
    st.header("Sea View")

    filter_status = st.selectbox(
        "Filter by status",
        ["All", "Healthy", "Watch", "At risk"],
        key="sea_filter_status",
    )

    projects = [
        project
        for project in workspace.projects
        if filter_status == "All"
        or (filter_status == "Healthy" and project.status(today) == ProjectStatus.HEALTHY)
        or (filter_status == "Watch" and project.status(today) == ProjectStatus.WATCH)
        or (filter_status == "At risk" and project.status(today) == ProjectStatus.AT_RISK)
    ]

    if not projects:
        st.info("No projects match the selected filter.")
        return

    for project in projects:
        with st.container():
            status = project.status(today)
            st.markdown(f"**{project.name}**")
            st.caption(f"Budget: {project.budget_hours:.2f}h | Logged: {project.logged_hours:.2f}h")

            if status == ProjectStatus.HEALTHY:
                st.success("On track")
            elif status == ProjectStatus.WATCH:
                st.info("This project is approaching a threshold. Monitor allocation closely.")
            elif status == ProjectStatus.AT_RISK:
                st.error("At risk of exceeding budget or missing deadline.")
