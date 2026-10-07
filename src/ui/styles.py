from __future__ import annotations

import streamlit as st

from src.ui.tokens import TOKENS


def apply_global_styles() -> None:
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        :root {{
            --page-background: {TOKENS.page_background};
            --surface-background: {TOKENS.surface_background};
            --surface-elevated: {TOKENS.surface_elevated};
            --primary-text: {TOKENS.primary_text};
            --secondary-text: {TOKENS.secondary_text};
            --tertiary-text: {TOKENS.tertiary_text};
            --primary-action: {TOKENS.primary_action};
            --primary-action-hover: {TOKENS.primary_action_hover};
            --focus-ring: {TOKENS.focus_ring};
            --border-subtle: {TOKENS.border_subtle};
            --border-default: {TOKENS.border_default};
            --success: {TOKENS.success};
            --warning: {TOKENS.warning};
            --error: {TOKENS.error};
            --shadow-sm: {TOKENS.shadow_sm};
            --shadow-md: {TOKENS.shadow_md};
            --shadow-lg: {TOKENS.shadow_lg};
            --shadow-xl: {TOKENS.shadow_xl};
            --radius-sm: {TOKENS.radius_small};
            --radius-md: {TOKENS.radius_medium};
            --radius-lg: {TOKENS.radius_large};
        }}
        
        * {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}
        
        .stApp {{
            background: var(--page-background);
            color: var(--primary-text);
        }}
        
        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: var(--primary-text);
            margin-bottom: 0.5rem;
        }}
        
        h2 {{
            font-size: 1.75rem;
            font-weight: 600;
            letter-spacing: -0.01em;
            color: var(--primary-text);
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        
        h3 {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--primary-text);
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}
        
        p, label, .stMarkdown {{
            color: var(--primary-text);
            line-height: 1.6;
        }}
        
        .stCaption {{
            color: var(--secondary-text);
            font-size: 0.875rem;
            font-weight: 400;
        }}
        
        [data-testid="stMetricValue"] {{
            font-size: 1.875rem;
            font-weight: 600;
            color: var(--primary-text);
        }}
        
        [data-testid="stMetricLabel"] {{
            color: var(--secondary-text);
            font-size: 0.875rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        [data-testid="stMetricDelta"] {{
            font-size: 0.875rem;
            font-weight: 500;
        }}
        
        .stButton > button {{
            border-radius: var(--radius-md);
            border: 1px solid transparent;
            background: var(--primary-action);
            color: white;
            font-weight: 600;
            font-size: 0.9375rem;
            padding: 0.625rem 1.25rem;
            transition: all 0.2s ease;
            box-shadow: var(--shadow-sm);
        }}
        
        .stButton > button:hover {{
            background: var(--primary-action-hover);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }}
        
        button:focus-visible, input:focus-visible, [role="radio"]:focus-visible {{
            outline: 3px solid var(--focus-ring) !important;
            outline-offset: 3px !important;
        }}
        
        [data-testid="stSidebar"] {{
            background: var(--surface-background);
            border-right: 1px solid var(--border-subtle);
            box-shadow: var(--shadow-sm);
        }}
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
            font-size: 1.125rem;
            font-weight: 600;
        }}
        
        .stRadio > label {{
            font-weight: 500;
            color: var(--primary-text);
            padding: 0.5rem 0.75rem;
            border-radius: var(--radius-sm);
            transition: background 0.15s ease;
        }}
        
        .stRadio > label:hover {{
            background: var(--surface-elevated);
        }}
        
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: var(--surface-background);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
            padding: 1.5rem;
            transition: box-shadow 0.2s ease, transform 0.2s ease;
        }}
        
        [data-testid="stVerticalBlockBorderWrapper"]:hover {{
            box-shadow: var(--shadow-md);
        }}
        
        .stProgress > div > div > div > div {{
            background-color: var(--primary-action);
            border-radius: var(--radius-sm);
        }}
        
        .stProgress > div > div {{
            background-color: var(--border-subtle);
            border-radius: var(--radius-sm);
            height: 8px;
        }}
        
        .stAlert {{
            border-radius: var(--radius-md);
            border: none;
            box-shadow: var(--shadow-sm);
        }}
        
        .stAlert[data-testid="stAlert"] {{
            background: var(--surface-elevated);
        }}
        
        div[data-testid="stAlert"] p {{
            font-weight: 500;
        }}
        
        .stDivider {{
            border-top: 1px solid var(--border-subtle);
        }}
        
        [data-testid="stJson"] {{
            background: var(--surface-elevated);
            border-radius: var(--radius-md);
            padding: 1rem;
            border: 1px solid var(--border-subtle);
        }}
        
        .element-container {{
            border-radius: var(--radius-md);
        }}
        
        .stTextInput > div > div > input {{
            border-radius: var(--radius-md);
            border: 1px solid var(--border-default);
            padding: 0.625rem 0.875rem;
            font-size: 0.9375rem;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }}
        
        .stTextInput > div > div > input:focus {{
            border-color: var(--focus-ring);
            box-shadow: 0 0 0 3px rgba(47, 111, 143, 0.1);
        }}
        
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
            margin-top: 0;
        }}
        
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}
            h2 {{
                font-size: 1.5rem;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
