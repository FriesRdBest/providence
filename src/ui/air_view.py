from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import PersonStatus, Workspace


def render_air_view(workspace: Workspace) -> None:
    today = date.today()

    st.header("People")
    st.caption("Real time capacity monitoring and availability")

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
            col_main, col_status = st.columns([4, 1], gap="large")

            with col_main:
                st.markdown(f"### {person.name}")
                st.caption(f"{person.role}")

                col1, col2, col3 = st.columns(3, gap="large")

                with col1:
                    st.metric(
                        label="Logged today",
                        value=f"{person.logged_hours_today:,.1f} h",
                    )

                with col2:
                    st.metric(
                        label="Capacity",
                        value=f"{person.daily_capacity_hours:,.0f} h",
                    )

                with col3:
                    remaining = person.capacity_remaining
                    st.metric(
                        label="Remaining",
                        value=f"{remaining:,.1f} h",
                    )

            with col_status:
                if status == PersonStatus.OVERBOOKED:
                    st.error(f"**{status_label}**")
                elif status == PersonStatus.MISSING_TIME:
                    st.warning(f"**{status_label}**")
                elif status == PersonStatus.BUSY:
                    st.info(f"**{status_label}**")
                else:
                    st.success(f"**{status_label}**")

            utilisation = float(min(person.logged_hours_today / person.daily_capacity_hours, Decimal("1")))
            st.progress(utilisation)

            if status == PersonStatus.OVERBOOKED:
                st.error(
                    "This person has exceeded their daily capacity. Review allocation immediately."
                )
            elif status == PersonStatus.MISSING_TIME:
                st.info(
                    "This person has not logged any time today. Confirm availability."
                )
