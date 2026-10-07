from __future__ import annotations

from decimal import Decimal

import streamlit as st

from src.domain.models import PersonStatus, Workspace


def render_air_view(workspace: Workspace) -> None:
    today = st.context.date

    st.header("Air")
    st.subheader("Current people capacity")

    filter_status = st.radio(
        "Filter by status",
        ("All", "Available", "Busy", "Overbooked", "Missing time"),
        index=0,
        horizontal=True,
    )

    filtered_people = [
        person
        for person in workspace.people
        if filter_status == "All"
        or (
            filter_status == "Available"
            and person.status == PersonStatus.AVAILABLE
        )
        or (
            filter_status == "Busy"
            and person.status == PersonStatus.BUSY
        )
        or (
            filter_status == "Overbooked"
            and person.status == PersonStatus.OVERBOOKED
        )
        or (
            filter_status == "Missing time"
            and person.status == PersonStatus.MISSING_TIME
        )
    ]

    for person in filtered_people:
        status = person.status
        status_label = {
            PersonStatus.AVAILABLE: "Available",
            PersonStatus.BUSY: "Busy",
            PersonStatus.OVERBOOKED: "Overbooked",
            PersonStatus.MISSING_TIME: "Missing time",
        }[status]

        with st.container(border=True):
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    label="Name",
                    value=person.name,
                )

            with col2:
                st.metric(
                    label="Role",
                    value=person.role,
                )

            with col3:
                st.metric(
                    label="Logged today",
                    value=f"{person.logged_hours_today:,.1f} h",
                )

            with col4:
                st.metric(
                    label="Status",
                    value=status_label,
                    delta=None,
                )

            st.progress(
                float(min(person.logged_hours_today / person.daily_capacity_hours, Decimal("1"))),
                text="Daily capacity utilisation",
            )

            remaining = person.capacity_remaining
            if remaining > Decimal("0"):
                st.caption(f"Capacity remaining: {remaining:,.1f} hours")
            else:
                st.caption("No capacity remaining today")

            if status == PersonStatus.OVERBOOKED:
                st.error(
                    "This person has exceeded their daily capacity. Review allocation immediately."
                )
            elif status == PersonStatus.MISSING_TIME:
                st.warning(
                    "This person has not logged any time today. Confirm availability."
                )
            elif status == PersonStatus.BUSY:
                st.info(
                    "This person has limited capacity remaining. Plan accordingly."
                )
