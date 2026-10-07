from __future__ import annotations

from datetime import date
from decimal import Decimal

import streamlit as st

from src.domain.models import Person, PersonStatus, Workspace
from src.ui.components import render_page_header, render_section_heading


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

    control_status, control_sort, control_count = st.columns(
        [1.15, 1.15, 0.7],
        gap="medium",
    )

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

    total_capacity = sum(
        (person.daily_capacity_hours for person in people),
        Decimal("0"),
    )
    total_logged = sum(
        (person.logged_hours_today for person in people),
        Decimal("0"),
    )
    total_remaining = sum(
        (person.capacity_remaining for person in people),
        Decimal("0"),
    )
    attention_count = sum(
        person.status in {PersonStatus.OVERBOOKED, PersonStatus.MISSING_TIME} for person in people
    )
    busy_count = sum(person.status == PersonStatus.BUSY for person in people)
    utilisation = Decimal("0")
    if total_capacity > Decimal("0"):
        utilisation = (total_logged / total_capacity * Decimal("100")).quantize(Decimal("0.1"))
    utilisation_width = min(float(utilisation), 100)

    with control_count:
        st.markdown(
            f"""
            <div class="providence-people-count">
                <span>Showing</span>
                <strong>{len(people)}</strong>
                <small>people</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<section class="providence-people-stage">', unsafe_allow_html=True)

    capacity_column, insight_column = st.columns([1.65, 0.95], gap="large")

    with capacity_column:
        st.markdown(
            f"""
            <article class="providence-people-hero">
                <div class="providence-people-hero-topline">
                    <span class="providence-people-kicker">Capacity pulse</span>
                    <span class="providence-people-live"><i></i> Today's view</span>
                </div>
                <div class="providence-people-hero-grid">
                    <div>
                        <span class="providence-people-hero-label">Team utilisation</span>
                        <strong>{utilisation}%</strong>
                        <p>
                            {_format_hours(total_remaining)} remains from
                            {_format_hours(total_capacity)} daily capacity.
                        </p>
                    </div>
                    <div class="providence-people-orbit">
                        <span>{len(people)}</span>
                        <small>tracked</small>
                    </div>
                </div>
                <div class="providence-people-pace">
                    <div class="providence-people-pace-track">
                        <span style="width: {utilisation_width:.2f}%"></span>
                    </div>
                    <div class="providence-people-pace-labels">
                        <span>Logged {_format_hours(total_logged)}</span>
                        <span>Available {_format_hours(total_remaining)}</span>
                    </div>
                </div>
                <div class="providence-people-hero-stats">
                    <div>
                        <span>Available</span>
                        <strong>
                            {sum(person.status == PersonStatus.AVAILABLE for person in people)}
                        </strong>
                    </div>
                    <div>
                        <span>Busy</span>
                        <strong>{busy_count}</strong>
                    </div>
                    <div>
                        <span>Attention</span>
                        <strong>{attention_count}</strong>
                    </div>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with insight_column:
        insight_title, insight_body = _insight_copy(people)
        st.markdown(
            f"""
            <aside class="providence-people-decision">
                <div class="providence-people-kicker">Allocation signal</div>
                <h2>{insight_title}</h2>
                <p>{insight_body}</p>
                <div class="providence-people-decision-foot">
                    <span>Attention needed</span>
                    <strong>{attention_count}</strong>
                </div>
            </aside>
            """,
            unsafe_allow_html=True,
        )

    summary_available, summary_busy, summary_attention = st.columns(3, gap="medium")

    with summary_available:
        available_count = sum(person.status == PersonStatus.AVAILABLE for person in people)
        st.markdown(
            f"""
            <article class="providence-people-signal providence-people-signal-violet">
                <span>Available</span>
                <strong>{available_count}</strong>
                <p>People with room for assignment</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with summary_busy:
        st.markdown(
            f"""
            <article class="providence-people-signal providence-people-signal-pink">
                <span>Busy</span>
                <strong>{busy_count}</strong>
                <p>People nearing a capacity boundary</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    with summary_attention:
        st.markdown(
            f"""
            <article class="providence-people-signal providence-people-signal-coral">
                <span>Attention</span>
                <strong>{attention_count}</strong>
                <p>Overbooked or missing time records</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

    render_section_heading(
        "Capacity ledger",
        "Current time records and available capacity for the active view",
    )

    if not people:
        st.markdown(
            """
            <article class="providence-people-empty">
                <div class="providence-people-kicker">No matches</div>
                <h3>No people match this view</h3>
                <p>Change the capacity filter to review other people records.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</section>", unsafe_allow_html=True)
        return

    for person in people:
        capacity_ratio = 0.0
        if person.daily_capacity_hours > Decimal("0"):
            capacity_ratio = min(
                float(person.logged_hours_today / person.daily_capacity_hours),
                1.0,
            )
        capacity_width = capacity_ratio * 100
        status_class = _status_style(person.status)
        status_text = _status_label(person.status)

        st.markdown(
            f"""
            <article class="providence-people-card">
                <div class="providence-people-card-person">
                    <div class="providence-people-avatar">{_person_initials(person.name)}</div>
                    <div>
                        <h3>{person.name}</h3>
                        <p>{person.role}</p>
                    </div>
                </div>
                <div class="providence-people-card-capacity">
                    <div class="providence-people-card-progress">
                        <span
                            class="providence-people-progress-{status_class}"
                            style="width: {capacity_width:.2f}%"
                        ></span>
                    </div>
                    <p>{_capacity_message(person)}</p>
                </div>
                <div class="providence-people-card-data">
                    <span>Logged</span>
                    <strong>{_format_hours(person.logged_hours_today)}</strong>
                </div>
                <div class="providence-people-card-data">
                    <span>Capacity</span>
                    <strong>{_format_hours(person.daily_capacity_hours)}</strong>
                </div>
                <div class="providence-people-card-data">
                    <span>Remaining</span>
                    <strong>{_format_hours(person.capacity_remaining)}</strong>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="providence-people-card-status">
                <span class="providence-status providence-status-{status_class}">
                    {status_text}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</section>", unsafe_allow_html=True)
