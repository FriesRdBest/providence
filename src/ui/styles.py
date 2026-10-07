from __future__ import annotations

import streamlit as st

from src.ui.tokens import TOKENS


def apply_global_styles() -> None:
    st.markdown(
        f"""
        <style>
        :root {{
            --page-background: {TOKENS.page_background};
            --surface-background: {TOKENS.surface_background};
            --primary-text: {TOKENS.primary_text};
            --secondary-text: {TOKENS.secondary_text};
            --primary-action: {TOKENS.primary_action};
            --focus-ring: {TOKENS.focus_ring};
        }}
        .stApp {{
            background: var(--page-background);
            color: var(--primary-text);
        }}
        h1, h2, h3, p, label {{
            color: var(--primary-text);
        }}
        .stButton > button {{
            border-radius: 0.5rem;
            border: 1px solid var(--primary-action);
            background: var(--primary-action);
            color: white;
            font-weight: 650;
        }}
        button:focus-visible, input:focus-visible, [role="radio"]:focus-visible {{
            outline: 3px solid var(--focus-ring) !important;
            outline-offset: 3px !important;
        }}
        [data-testid="stSidebar"] {{
            background: #FFFFFF;
            border-right: 1px solid #D8DDE3;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
