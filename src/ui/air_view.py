from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import Person, PersonStatus, Workspace
from src.ui.components import (
    render_insight,
    render_page_header,
    render_section_heading,
)


def _format_hours(value: Decimal) -> str:
    return f"{value:,.1f} h"


def _status_label(status: PersonStatus) -> str:
    return {
        PersonStatus.AVAILABLE: "Available",
        PersonStatus.BUSY: "Busy",
        PersonStatus.OVERBOOKED: "Overbooked",
        PersonStatus.MISSING_TIME: "Time missing",
    }[status]


def _status_style(status: PersonStatus) -> str:
    return {
        PersonStatus.AVAILABLE: "healthy",
        PersonStatus.BUSY: "watch",
        PersonStatus.OVERBOOKED: "risk",
        PersonStatus.MISSING_TIME: "neutral",
    }[status]


def _person_initials(name: str) -> str:
    parts = [part for part in name.split() if part]
    return "".join(part[0].upper() for part in parts[:2])


def _capacity_message(person: Person) -> str:
    if person.status == PersonStatus.OVERBOOKED:
        excess = person.logged_hours_today - person.daily_capacity_hours
        return f"{_format_hours(excess)} above daily capacity"

    if person.status == PersonStatus.MISSING_TIME:
        return "No time has been logged today"

    if person.status == PersonStatus.BUSY:
        return f"{_format_hours(person.capacity_remaining)} remains today"

    return f"{_format_hours(person.capacity_remaining)} available today"


def _insight_copy(people: list[Person]) -> tuple[str, str]:
    overbooked = [person for person in people if person.status == PersonStatus.OVERBOOKED]
    if overbooked:
        priority_person = max(
            overbooked,
            key=lambda person: person.logged_hours_today - person.daily_capacity_hours,
        )
        excess = priority_person.logged_hours_today - priority_person.daily_capacity_hours
        return (
            f"{priority_person.name} is overbooked",
            f"Current logged time is {_format_hours(excess)} above daily capacity. "
            "Review current assignment before adding more work.",
        )

    missing_time = [person for person in people if person.status == PersonStatus.MISSING_TIME]
    if missing_time:
        person_word = "person" if len(missing_time) == 1 else "people"
        return (
            f"{len(missing_time)} {person_word} have not logged time",
            "Capacity cannot be fully assessed until current time records are available.",
        )

    busy_people = [person for person in people if person.status == PersonStatus.BUSY]
    if busy_people:
        return (
            "Capacity is approaching a review boundary",
            "Some people have limited availability remaining today. Review new assignments "
            "before they are allocated.",
        )

    return (
        "Team capacity is within current boundaries",
        "All people have recorded time and remain within their daily capacity.",
    )


def _sort_people(people: list[Person], sort_by: str) -> list[Person]:
    status_order = {
        PersonStatus.OVERBOOKED: 0,
        PersonStatus.MISSING_TIME: 1,
        PersonStatus.BUSY: 2,
        PersonStatus.AVAILABLE: 3,
    }

    if sort_by == "Capacity remaining":
        return sorted(people, key=lambda person: float(person.capacity_remaining))

    if sort_by == "Name":
        return sorted(people, key=lambda person: person.name.lower())

    return sorted(
        people,
        key=lambda person: (
            status_order[person.status],
            float(person.capacity_remaining),
        ),
    )


def render_air_view(workspace: Workspace) -> None:
    today = date.today()

    render_page_header(
        "People",
        "Current capacity, logged time, and attention needed across the workspace.",
        today,
    )

    control_status, control_sort, control_count = st.columns([1.15, 1.15, 0.7], gap="medium")

    with control_status:
        filter_status = st.selectbox(
            "Capacity status",
            ["All", "Available", "Busy", "Overbooked", "Time missing"],
            key="people_filter_status",
        )

    with control_sort:
        sort_by = st.selectbox(
            "Sort people by",
            ["Attention first", "Capacity remaining", "Name"],
            key="people_sort_by",
        )

    people = [
        person
        for person in workspace.people
        if filter_status == "All" or _status_label(person.status) == filter_status
    ]
    people = _sort_people(people, sort_by)

    with control_count:
        st.markdown(
            '<div class="providence-project-count-label">Showing</div>'
            f'<div class="providence-project-count-value">{len(people)}</div>'
            '<div class="providence-project-count-copy">people</div>',
            unsafe_allow_html=True,
        )

    total_capacity = sum((person.daily_capacity_hours for person in people), Decimal("0"))
    total_remaining = sum((person.capacity_remaining for person in people), Decimal("0"))
    attention_count = sum(
        person.status in {PersonStatus.OVERBOOKED, PersonStatus.MISSING_TIME} for person in people
    )

    summary_one, summary_two, summary_three = st.columns(3, gap="medium")

    with summary_one:
        with st.container(border=True):
            st.metric(
                label="People tracked",
                value=len(people),
                delta="Current result set",
                delta_color="off",
            )

    with summary_two:
        with st.container(border=True):
            st.metric(
                label="Capacity remaining",
                value=_format_hours(total_remaining),
                delta=f"Of {_format_hours(total_capacity)} daily capacity",
                delta_color="off",
            )

    with summary_three:
        with st.container(border=True):
            st.metric(
                label="Attention needed",
                value=attention_count,
                delta=("Review required" if attention_count > 0 else "Within current boundaries"),
                delta_color="inverse" if attention_count > 0 else "off",
            )

    insight_title, insight_body = _insight_copy(people)
    render_insight(insight_title, insight_body)

    render_section_heading(
        "Capacity ledger",
        "Current time records and available capacity for the active view",
    )

    if not people:
        with st.container(border=True):
            st.markdown(
                '<div class="providence-empty-title">No people match this view</div>'
                '<p class="providence-empty-copy">'
                "Change the current capacity filter to review other people records."
                "</p>",
                unsafe_allow_html=True,
            )
        return

    for person in people:
        capacity_ratio = 0.0
        if person.daily_capacity_hours > Decimal("0"):
            capacity_ratio = min(
                float(person.logged_hours_today / person.daily_capacity_hours),
                1.0,
            )

        with st.container(border=True):
            identity_column, logged_column, capacity_column, remaining_column, status_column = (
                st.columns(
                    [2.2, 1, 1, 1.15, 1],
                    gap="medium",
                )
            )

            with identity_column:
                st.markdown(
                    f'<div class="providence-person-identity">'
                    f'<div class="providence-person-mark">{_person_initials(person.name)}</div>'
                    f'<div><div class="providence-person-name">{person.name}</div>'
                    f'<div class="providence-person-role">{person.role}</div></div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )

            with logged_column:
                st.markdown(
                    '<div class="providence-preview-label">Logged today</div>'
                    f'<div class="providence-project-value">'
                    f"{_format_hours(person.logged_hours_today)}</div>",
                    unsafe_allow_html=True,
                )

            with capacity_column:
                st.markdown(
                    '<div class="providence-preview-label">Daily capacity</div>'
                    f'<div class="providence-project-value">'
                    f"{_format_hours(person.daily_capacity_hours)}</div>",
                    unsafe_allow_html=True,
                )

            with remaining_column:
                st.markdown(
                    '<div class="providence-preview-label">Remaining</div>'
                    f'<div class="providence-project-value">'
                    f"{_format_hours(person.capacity_remaining)}</div>",
                    unsafe_allow_html=True,
                )

            with status_column:
                status_class = _status_style(person.status)
                status_text = _status_label(person.status)
                status_markup = (
                    f'<span class="providence-status providence-status-{status_class}">'
                    f"{status_text}</span>"
                )
                st.markdown(status_markup, unsafe_allow_html=True)

            progress_class = f"providence-capacity-progress-{_status_style(person.status)}"
            progress_container = st.container()
            with progress_container:
                st.markdown(
                    f'<div class="{progress_class}"></div>',
                    unsafe_allow_html=True,
                )
                st.progress(capacity_ratio)

            st.markdown(
                f'<p class="providence-project-message">{_capacity_message(person)}</p>',
                unsafe_allow_html=True,
            )
