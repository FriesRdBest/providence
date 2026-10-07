from __future__ import annotations

import json
from datetime import date

import streamlit as st

from src.domain.models import Workspace
from src.services.rule_engine import RuleEngine


def render_overview_view(workspace: Workspace) -> None:
    today = date.today()
    health = RuleEngine().assess_workspace(workspace, today=today)

    st.header("Overview")
    st.caption("Understanding Providence and exporting guidance")

    with st.container(border=True):
        st.markdown("### What is Providence")
        st.write(
            "Providence presents time intelligence across three connected views. "
            "**Health** shows weekly organisational health. "
            "**Project** shows daily project delivery status. "
            "**People** shows current people capacity."
        )

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        with st.container(border=True):
            st.metric(
                label="Team utilisation",
                value=f"{health.utilisation_percentage} %",
            )

    with col2:
        with st.container(border=True):
            st.metric(
                label="Projects tracked",
                value=len(workspace.projects),
            )

    with col3:
        with st.container(border=True):
            st.metric(
                label="People tracked",
                value=len(workspace.people),
            )

    with st.container(border=True):
        st.markdown("### Design and technical approach")
        st.write(
            "The interface uses a three layer visual language. "
            "Primitive values define the base palette. "
            "Semantic roles express intent for backgrounds, text, and actions. "
            "Component decisions use semantic roles rather than direct palette values. "
            "This keeps the interface consistent."
        )

        st.write(
            "Every workspace record is validated before use. "
            "Pydantic models enforce data contracts. "
            "The rule engine produces deterministic health signals. "
            "The presentation layer consumes prepared data without changing the ledger."
        )

    with st.container(border=True):
        st.markdown("### Export guidance document")
        st.write(
            "The following document provides a complete overview of the application "
            "for stakeholder review. "
            "You can copy this content or export it as a JSON file for archival purposes."
        )

        overview_document = {
            "application_name": "Providence",
            "description": "Time intelligence for clear management decisions",
            "views": {
                "Health": {
                    "purpose": "Weekly organisational health",
                    "metrics": [
                        "Team utilisation percentage",
                        "Total and remaining budget hours",
                        "Projects at risk and on watch counts",
                        "Project health summary with budget burn and delivery timeline",
                    ],
                },
                "Project": {
                    "purpose": "Daily project delivery status",
                    "metrics": [
                        "Budget burn percentage per project",
                        "Budget remaining hours per project",
                        "Days until delivery per project",
                        "Status classification with contextual alerts",
                    ],
                },
                "People": {
                    "purpose": "Current people capacity",
                    "metrics": [
                        "Name and role per person",
                        "Logged hours today per person",
                        "Status classification with capacity remaining",
                        "Alerts for overbooked and missing time states",
                    ],
                },
            },
            "workspace_summary": {
                "workspace_name": workspace.name,
                "total_projects": len(workspace.projects),
                "total_people": len(workspace.people),
                "team_utilisation": str(health.utilisation_percentage),
                "projects_at_risk": health.projects_at_risk,
                "projects_on_watch": health.projects_on_watch,
                "generated_date": str(date.today()),
            },
        }

        st.json(overview_document, expanded=False)

        export_button = st.button(
            "Download overview document",
            help="Download the overview document as a JSON file for stakeholder review",
        )

        if export_button:
            st.download_button(
                label="Download JSON",
                data=json.dumps(overview_document, indent=2),
                file_name="providence_overview.json",
                mime="application/json",
            )
