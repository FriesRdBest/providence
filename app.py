from __future__ import annotations

import streamlit as st

from src.services.workspace_service import WorkspaceService
from src.services.ai_insight_service import AIInsightService
from src.ui.styles import apply_global_styles
from src.ui.land_view import render_land_view
from src.ui.sea_view import render_sea_view
from src.ui.air_view import render_air_view
from src.ui.overview_view import render_overview_view

st.set_page_config(
    page_title="Providence",
    page_icon="P",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_global_styles()

try:
    service = WorkspaceService()
    workspace = service.load_workspace()
    ai_service = AIInsightService()
    workspace_loaded = True
except Exception as error:
    workspace_loaded = False
    workspace = None
    ai_service = None
    st.error(f"Failed to load workspace: {error}")
    st.info("Check the Streamlit Cloud deployment logs for details.")

st.title("Providence")
st.caption("Time intelligence for clear management decisions")

if workspace_loaded:
    st.sidebar.title("Providence")
    view = st.sidebar.radio(
        "Choose a view",
        ("Land", "Sea", "Air", "Overview"),
        index=0,
    )

    if view == "Land":
        render_land_view(workspace)
    elif view == "Sea":
        render_sea_view(workspace)
    elif view == "Air":
        render_air_view(workspace)
    else:
        render_overview_view(workspace)

    st.divider()

    with st.container(border=True):
        st.subheader("AI Predictive Insight Box")
        st.caption("Ask a plain language question about your workspace")

        query = st.text_input(
            "Your question",
            placeholder="Which active project faces immediate budget depletion this week?",
            label_visibility="collapsed",
        )

        if query:
            insight = ai_service.answer_query(workspace, query)

            with st.container(border=True):
                st.write(f"**Query:** {insight.query}")
                st.write(f"**Answer:** {insight.answer}")
                st.write(f"**Confidence:** {insight.confidence}")

                if insight.supporting_facts:
                    st.write("**Supporting facts:**")
                    for fact in insight.supporting_facts:
                        st.write(f"- {fact}")

    st.caption(
        f"Validated workspace loaded: {workspace.name}. "
        f"{len(workspace.projects)} projects and {len(workspace.people)} people are available."
    )
