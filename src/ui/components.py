from __future__ import annotations

from datetime import date

import streamlit as st

from src.domain.models import ProjectStatus
from src.ui.tokens import TOKENS


def render_brand() -> None:
    st.markdown(
        """
        <div class="providence-brand">
            <div class="providence-mark">P</div>
            <div>
                <div class="providence-brand-name">Providence</div>
                <div class="providence-brand-detail">Time intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title: str, description: str, today: date) -> None:
    formatted_date = today.strftime("%A, %B %d, %Y")
    st.markdown(
        f"""
        <div class="providence-page-header">
            <div>
                <div class="providence-eyebrow">Workspace intelligence</div>
                <h1>{title}</h1>
                <p class="providence-page-subtitle">{description}</p>
            </div>
            <div class="providence-date-context">{formatted_date}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_heading(title: str, detail: str | None = None) -> None:
    detail_markup = f'<span class="providence-section-detail">{detail}</span>' if detail else ""
    st.markdown(
        f"""
        <div class="providence-section-heading">
            <h2>{title}</h2>
            {detail_markup}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_status(status: ProjectStatus) -> None:
    labels = {
        ProjectStatus.HEALTHY: "Healthy",
        ProjectStatus.WATCH: "Watch",
        ProjectStatus.AT_RISK: "At risk",
    }
    styles = {
        ProjectStatus.HEALTHY: "healthy",
        ProjectStatus.WATCH: "watch",
        ProjectStatus.AT_RISK: "risk",
    }
    status_markup = (
        f'<span class="providence-status providence-status-{styles[status]}">'
        f"{labels[status]}</span>"
    )
    st.markdown(status_markup, unsafe_allow_html=True)


def render_neutral_status(label: str) -> None:
    st.markdown(
        f'<span class="providence-status providence-status-neutral">{label}</span>',
        unsafe_allow_html=True,
    )


def render_insight(title: str, body: str) -> None:
    st.markdown(
        f"""
        <section class="providence-insight">
            <div class="providence-insight-label">Decision support</div>
            <div class="providence-insight-title">{title}</div>
            <p class="providence-insight-body">{body}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def chart_palette() -> dict[str, str]:
    return {
        "primary": TOKENS.action_primary,
        "healthy": TOKENS.status_healthy,
        "watch": TOKENS.status_watch,
        "risk": TOKENS.status_risk,
        "text": TOKENS.text_core,
        "supporting_text": TOKENS.text_supporting,
        "grid": TOKENS.border_subtle,
        "surface": TOKENS.surface_primary,
    }
