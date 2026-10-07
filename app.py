from __future__ import annotations

import streamlit as st

from src.services.workspace_service import WorkspaceService
from src.ui.styles import apply_global_styles
from src.ui.land_view import render_land_view
from src.ui.sea_view import render_sea_view

st.set_page_config(
    page_title="Providence",
    page_icon="P",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_global_styles()

service = WorkspaceService()
workspace = service.load_workspace()

st.title("Providence")
st.caption("Time intelligence for clear management decisions")

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
    st.header("Air")
    st.write("Current people capacity will appear here.")
else:
    st.header("Overview")
    st.write("A concise explanation of Providence will appear here.")

st.divider()
st.caption(
    f"Validated workspace loaded: {workspace.name}. "
    f"{len(workspace.projects)} projects and {len(workspace.people)} people are available."
)
