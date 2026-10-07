import streamlit as st
from decimal import Decimal
from src.domain.models import Workspace, PersonStatus


def render(workspace: Workspace, today) -> None:
    st.header("Air View")

    filter_status = st.selectbox(
        "Filter by status",
        ["All", "Available", "Busy", "Overbooked", "Missing time"],
        key="air_filter_status",
    )

    people = [
        person
        for person in workspace.people
        if filter_status == "All"
        or (filter_status == "Available" and person.status == PersonStatus.AVAILABLE)
        or (filter_status == "Busy" and person.status == PersonStatus.BUSY)
        or (filter_status == "Overbooked" and person.status == PersonStatus.OVERBOOKED)
        or (filter_status == "Missing time" and person.status == PersonStatus.MISSING_TIME)
    ]

    if not people:
        st.info("No people match the selected filter.")
        return

    for person in people:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{person.name}**")
                if person.status == PersonStatus.AVAILABLE:
                    st.success("Available")
                elif person.status == PersonStatus.BUSY:
                    st.warning("Busy")
                elif person.status == PersonStatus.OVERBOOKED:
                    st.error("Overbooked")
                elif person.status == PersonStatus.MISSING_TIME:
                    st.info("This person has not logged any time today. Confirm availability.")
            with col2:
                utilisation = float(
                    min(person.logged_hours_today / person.daily_capacity_hours, Decimal("1"))
                )
                st.progress(utilisation)
                st.caption(f"{person.logged_hours_today:.2f}h / {person.daily_capacity_hours:.2f}h")
