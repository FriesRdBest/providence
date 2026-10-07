from __future__ import annotations

import streamlit as st

from src.services.workspace_service import WorkspaceService
from src.ui.styles import apply_global_styles

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
    st.header("Land")
    st.write("Weekly organisational health will appear here.")
elif view == "Sea":
    st.header("Sea")
    st.write("Daily project delivery status will appear here.")
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
