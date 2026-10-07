from __future__ import annotations

import streamlit as st

from src.ui.tokens import TOKENS


def apply_global_styles() -> None:
    st.markdown(
        f"""
        <style>
        :root {{
            --app-surface: {TOKENS.app_surface};
            --surface-primary: {TOKENS.surface_primary};
            --surface-secondary: {TOKENS.surface_secondary};
            --surface-subtle: {TOKENS.surface_subtle};
            --text-core: {TOKENS.text_core};
            --text-supporting: {TOKENS.text_supporting};
            --text-muted: {TOKENS.text_muted};
            --border-subtle: {TOKENS.border_subtle};
            --border-default: {TOKENS.border_default};
            --action-primary: {TOKENS.action_primary};
            --action-primary-hover: {TOKENS.action_primary_hover};
            --status-healthy: {TOKENS.status_healthy};
            --status-healthy-surface: {TOKENS.status_healthy_surface};
            --status-watch: {TOKENS.status_watch};
            --status-watch-surface: {TOKENS.status_watch_surface};
            --status-risk: {TOKENS.status_risk};
            --status-risk-surface: {TOKENS.status_risk_surface};
            --status-neutral: {TOKENS.status_neutral};
            --status-neutral-surface: {TOKENS.status_neutral_surface};
            --focus-ring: {TOKENS.focus_ring};
            --shadow-card: {TOKENS.primitives.shadow_card};
            --shadow-float: {TOKENS.primitives.shadow_float};
            --radius-sm: {TOKENS.primitives.radius_sm};
            --radius-md: {TOKENS.primitives.radius_md};
            --radius-lg: {TOKENS.primitives.radius_lg};
            --radius-xl: {TOKENS.primitives.radius_xl};
        }}

        html, body, [class*="css"] {{
            font-family: Inter, ui-sans-serif, system-ui, -apple-system,
                BlinkMacSystemFont, "Segoe UI", sans-serif;
        }}

        .stApp {{
            background:
                radial-gradient(circle at 80% 0%, rgba(224, 90, 71, 0.07), transparent 26rem),
                var(--app-surface);
            color: var(--text-core);
        }}

        [data-testid="stAppViewContainer"] {{
            background: transparent;
        }}

        [data-testid="stHeader"] {{
            background: rgba(253, 251, 247, 0.92);
            border-bottom: 1px solid rgba(221, 225, 226, 0.72);
        }}

        [data-testid="stToolbar"] {{
            right: 1rem;
        }}

        .block-container {{
            max-width: 1480px;
            padding: 2.25rem 2.25rem 3.5rem;
        }}

        h1, h2, h3, h4, p {{
            color: var(--text-core);
        }}

        h1 {{
            font-size: clamp(2rem, 3vw, 3.15rem);
            font-weight: 650;
            letter-spacing: -0.045em;
            line-height: 1.04;
            margin-bottom: 0.45rem;
        }}

        h2 {{
            font-size: 1.4rem;
            font-weight: 650;
            letter-spacing: -0.025em;
            line-height: 1.2;
            margin-top: 0;
        }}

        h3 {{
            font-size: 1rem;
            font-weight: 650;
            letter-spacing: -0.01em;
            margin-top: 0;
        }}

        p, .stMarkdown {{
            color: var(--text-core);
            line-height: 1.55;
        }}

        [data-testid="stCaptionContainer"] {{
            color: var(--text-supporting);
            font-size: 0.9rem;
            line-height: 1.45;
        }}

        [data-testid="stSidebar"] {{
            min-width: 248px;
            background: var(--surface-primary);
            border-right: 1px solid var(--border-subtle);
        }}

        [data-testid="stSidebar"] > div:first-child {{
            min-height: 100%;
            padding: 1.25rem 0.9rem 7rem;
        }}

        [data-testid="stSidebarNav"] {{
            display: none;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] > div {{
            gap: 0.22rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label {{
            border-radius: var(--radius-md);
            color: var(--text-supporting);
            font-size: 0.92rem;
            font-weight: 650;
            padding: 0.62rem 0.72rem;
            transition: background 150ms ease, color 150ms ease;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
            background: var(--surface-secondary);
            color: var(--text-core);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {{
            background: var(--surface-secondary);
            color: var(--text-core);
            box-shadow: inset 3px 0 0 var(--action-primary);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] input {{
            display: none;
        }}

        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: var(--surface-primary);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-card);
        }}

        [data-testid="stMetric"] {{
            padding: 0;
        }}

        [data-testid="stMetricLabel"] {{
            color: var(--text-supporting);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        [data-testid="stMetricValue"] {{
            color: var(--text-core);
            font-size: clamp(1.8rem, 2.5vw, 2.55rem);
            font-weight: 650;
            letter-spacing: -0.045em;
            line-height: 1.08;
        }}

        [data-testid="stMetricDelta"] {{
            font-size: 0.82rem;
            font-weight: 600;
        }}

        .stButton > button {{
            min-height: 2.7rem;
            border: 1px solid var(--action-primary);
            border-radius: var(--radius-md);
            background: var(--action-primary);
            color: #FFFFFF;
            font-size: 0.92rem;
            font-weight: 650;
            letter-spacing: -0.01em;
            padding: 0.58rem 1rem;
            box-shadow: none;
            transition: background 150ms ease, transform 150ms ease, box-shadow 150ms ease;
        }}

        .stButton > button:hover {{
            background: var(--action-primary-hover);
            border-color: var(--action-primary-hover);
            box-shadow: var(--shadow-card);
            transform: translateY(-1px);
        }}

        .stDownloadButton > button {{
            min-height: 2.7rem;
            border: 1px solid var(--border-default);
            border-radius: var(--radius-md);
            background: var(--surface-primary);
            color: var(--text-core);
            font-size: 0.9rem;
            font-weight: 650;
            letter-spacing: -0.01em;
            padding: 0.58rem 0.9rem;
            transition: background 150ms ease, border-color 150ms ease;
        }}

        .stDownloadButton > button:hover {{
            background: var(--surface-secondary);
            border-color: var(--text-muted);
        }}

        .stButton > button:focus-visible,
        .stDownloadButton > button:focus-visible,
        button:focus-visible,
        input:focus-visible,
        [role="tab"]:focus-visible,
        [role="radio"]:focus-visible {{
            outline: 3px solid var(--focus-ring) !important;
            outline-offset: 3px !important;
        }}

        [data-testid="stTabs"] [data-baseweb="tab-list"] {{
            gap: 0.35rem;
            border-bottom: 1px solid var(--border-subtle);
        }}

        [data-testid="stTabs"] [data-baseweb="tab"] {{
            height: 2.65rem;
            border-radius: var(--radius-sm) var(--radius-sm) 0 0;
            color: var(--text-supporting);
            font-size: 0.9rem;
            font-weight: 650;
            padding: 0 0.9rem;
        }}

        [data-testid="stTabs"] [aria-selected="true"] {{
            color: var(--text-core);
            background: var(--surface-primary);
        }}

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {{
            background-color: var(--action-primary);
            height: 2px;
        }}

        [data-baseweb="select"] > div,
        [data-testid="stTextInput"] input {{
            min-height: 2.65rem;
            border-radius: var(--radius-md);
            border-color: var(--border-default);
            background: var(--surface-primary);
            color: var(--text-core);
        }}

        [data-baseweb="select"] > div:hover,
        [data-testid="stTextInput"] input:hover {{
            border-color: var(--text-muted);
        }}

        [data-testid="stProgress"] > div > div {{
            height: 0.5rem;
            border-radius: 999px;
            background: var(--surface-secondary);
        }}

        [data-testid="stProgress"] > div > div > div {{
            border-radius: 999px;
            background: var(--action-primary);
        }}

        div:has(> .providence-capacity-progress-healthy)
        + [data-testid="stProgress"] > div > div > div {{
            background: var(--text-muted);
        }}

        div:has(> .providence-capacity-progress-watch)
        + [data-testid="stProgress"] > div > div > div {{
            background: var(--status-watch);
        }}

        div:has(> .providence-capacity-progress-risk)
        + [data-testid="stProgress"] > div > div > div {{
            background: var(--status-risk);
        }}

        div:has(> .providence-capacity-progress-neutral)
        + [data-testid="stProgress"] > div > div > div {{
            background: var(--steel-500, #7D8790);
        }}

        [data-testid="stAlert"] {{
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
            box-shadow: none;
        }}

        [data-testid="stAlert"] p {{
            font-size: 0.92rem;
            line-height: 1.45;
        }}

        [data-testid="stDataFrame"] {{
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            overflow: hidden;
        }}

        hr {{
            border-color: var(--border-subtle);
        }}

        .providence-brand {{
            display: flex;
            align-items: center;
            gap: 0.7rem;
            padding: 0.35rem 0.35rem 1.5rem;
        }}

        .providence-mark {{
            width: 2rem;
            height: 2rem;
            display: grid;
            place-items: center;
            border-radius: 0.68rem;
            background: var(--text-core);
            color: #FFFFFF;
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: -0.06em;
            box-shadow: 0 5px 14px rgba(31, 33, 31, 0.15);
        }}

        .providence-brand-name {{
            color: var(--text-core);
            font-size: 1.1rem;
            font-weight: 700;
            letter-spacing: -0.035em;
            line-height: 1;
        }}

        .providence-brand-detail {{
            color: var(--text-muted);
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.045em;
            margin-top: 0.2rem;
            text-transform: uppercase;
        }}

        .providence-nav-title {{
            color: var(--text-muted);
            font-size: 0.68rem;
            font-weight: 750;
            letter-spacing: 0.1em;
            margin: 0.85rem 0.35rem 0.55rem;
            text-transform: uppercase;
        }}

        .providence-nav-note {{
            position: absolute;
            bottom: 1.2rem;
            left: 1.25rem;
            right: 1.25rem;
            padding: 0.85rem;
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            color: var(--text-supporting);
            font-size: 0.76rem;
            line-height: 1.4;
        }}

        .providence-page-header {{
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 1.5rem;
            margin-bottom: 2.1rem;
        }}

        .providence-eyebrow {{
            color: var(--action-primary);
            font-size: 0.72rem;
            font-weight: 750;
            letter-spacing: 0.1em;
            margin-bottom: 0.45rem;
            text-transform: uppercase;
        }}

        .providence-page-subtitle {{
            max-width: 42rem;
            color: var(--text-supporting);
            font-size: 1rem;
            line-height: 1.55;
            margin: 0;
        }}

        .providence-date-context {{
            flex: 0 0 auto;
            padding: 0.72rem 0.9rem;
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            color: var(--text-supporting);
            font-size: 0.82rem;
            font-weight: 600;
            white-space: nowrap;
        }}

        .providence-section-heading {{
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 1rem;
            margin: 2.25rem 0 1rem;
        }}

        .providence-section-heading h2 {{
            margin: 0;
        }}

        .providence-section-detail {{
            color: var(--text-muted);
            font-size: 0.82rem;
            font-weight: 500;
        }}

        .providence-status {{
            display: inline-flex;
            align-items: center;
            gap: 0.38rem;
            width: fit-content;
            border-radius: 999px;
            font-size: 0.74rem;
            font-weight: 750;
            letter-spacing: 0.01em;
            padding: 0.35rem 0.62rem;
            white-space: nowrap;
        }}

        .providence-status::before {{
            width: 0.42rem;
            height: 0.42rem;
            border-radius: 50%;
            background: currentColor;
            content: "";
        }}

        .providence-status-healthy {{
            background: var(--status-healthy-surface);
            color: var(--status-healthy);
        }}

        .providence-status-watch {{
            background: var(--status-watch-surface);
            color: var(--status-watch);
        }}

        .providence-status-risk {{
            background: var(--status-risk-surface);
            color: var(--status-risk);
        }}

        .providence-status-neutral {{
            background: var(--status-neutral-surface);
            color: var(--status-neutral);
        }}

        .providence-insight {{
            position: relative;
            overflow: hidden;
            padding: 1.25rem 1.35rem;
            background:
                linear-gradient(135deg, rgba(224, 90, 71, 0.09), transparent 52%),
                var(--surface-primary);
            border: 1px solid rgba(224, 90, 71, 0.22);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-card);
        }}

        .providence-insight-label {{
            color: var(--action-primary);
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.095em;
            margin-bottom: 0.45rem;
            text-transform: uppercase;
        }}

        .providence-insight-title {{
            color: var(--text-core);
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 0.35rem;
        }}

        .providence-insight-body {{
            color: var(--text-supporting);
            font-size: 0.9rem;
            line-height: 1.5;
            margin: 0;
        }}

        .providence-hero-label,
        .providence-health-hero-label {{
            color: var(--text-muted);
            font-size: 0.72rem;
            font-weight: 750;
            letter-spacing: 0.09em;
            margin-bottom: 0.6rem;
            text-transform: uppercase;
        }}

        .providence-hero-value,
        .providence-health-hero-value {{
            color: var(--text-core);
            font-size: clamp(3.2rem, 6vw, 5.5rem);
            font-weight: 680;
            letter-spacing: -0.07em;
            line-height: 0.92;
        }}

        .providence-hero-copy,
        .providence-health-hero-copy {{
            color: var(--text-supporting);
            font-size: 0.95rem;
            line-height: 1.5;
            margin: 0.75rem 0 1.35rem;
        }}

        .providence-hero-stat-label,
        .providence-preview-label,
        .providence-health-stat-label {{
            color: var(--text-muted);
            font-size: 0.7rem;
            font-weight: 750;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }}

        .providence-hero-stat-value,
        .providence-health-stat-value {{
            color: var(--text-core);
            font-size: 1.15rem;
            font-weight: 680;
            letter-spacing: -0.025em;
            margin-top: 0.22rem;
        }}

        .providence-preview-value,
        .providence-project-value,
        .providence-health-row-value {{
            color: var(--text-core);
            font-size: 1.15rem;
            font-weight: 680;
            letter-spacing: -0.03em;
            margin-top: 0.22rem;
        }}

        .providence-health-number {{
            font-size: 2.4rem;
            font-weight: 680;
            letter-spacing: -0.06em;
            line-height: 1;
            margin: 0.3rem 0 0.45rem;
        }}

        .providence-health-number-risk {{
            color: var(--status-risk);
        }}

        .providence-health-number-watch {{
            color: var(--status-watch);
        }}

        .providence-health-exposure-title {{
            color: var(--text-core);
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 1.1rem;
        }}

        .providence-empty-title {{
            color: var(--text-core);
            font-size: 1rem;
            font-weight: 680;
            letter-spacing: -0.02em;
            margin-bottom: 0.35rem;
        }}

        .providence-empty-copy {{
            color: var(--text-supporting);
            font-size: 0.9rem;
            line-height: 1.5;
            margin: 0;
        }}

        .providence-export-area {{
            display: flex;
            align-items: center;
            margin-top: 2.5rem;
            padding: 1.1rem 1.2rem;
            background: rgba(255, 255, 255, 0.54);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
        }}

        .providence-export-title {{
            color: var(--text-core);
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: -0.015em;
        }}

        .providence-export-copy {{
            color: var(--text-supporting);
            font-size: 0.84rem;
            line-height: 1.45;
            margin: 0.22rem 0 0;
        }}

        .providence-project-count-label {{
            color: var(--text-muted);
            font-size: 0.7rem;
            font-weight: 750;
            letter-spacing: 0.075em;
            margin-top: 0.2rem;
            text-transform: uppercase;
        }}

        .providence-project-count-value {{
            color: var(--text-core);
            font-size: 2rem;
            font-weight: 680;
            letter-spacing: -0.055em;
            line-height: 1;
            margin-top: 0.28rem;
        }}

        .providence-project-count-copy {{
            color: var(--text-supporting);
            font-size: 0.82rem;
            font-weight: 550;
            margin-top: 0.16rem;
        }}

        .providence-project-message {{
            color: var(--text-supporting);
            font-size: 0.88rem;
            line-height: 1.45;
            margin: 0.9rem 0 0;
        }}

        .providence-person-identity {{
            display: flex;
            align-items: center;
            gap: 0.72rem;
        }}

        .providence-person-mark {{
            display: grid;
            flex: 0 0 auto;
            place-items: center;
            width: 2.3rem;
            height: 2.3rem;
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            border-radius: 50%;
            color: var(--text-core);
            font-size: 0.74rem;
            font-weight: 800;
            letter-spacing: -0.03em;
        }}

        .providence-person-name {{
            color: var(--text-core);
            font-size: 0.96rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }}

        .providence-person-role {{
            color: var(--text-supporting);
            font-size: 0.8rem;
            line-height: 1.35;
            margin-top: 0.12rem;
        }}

        @media (max-width: 860px) {{
            .block-container {{
                padding: 1.35rem 1rem 2.25rem;
            }}

            .providence-page-header {{
                align-items: flex-start;
                flex-direction: column;
                gap: 1rem;
                margin-bottom: 1.6rem;
            }}

            .providence-date-context {{
                white-space: normal;
            }}

            .providence-hero-value,
            .providence-health-hero-value {{
                font-size: 3.4rem;
            }}

            .providence-export-area {{
                display: block;
            }}

            .providence-project-count-label {{
                margin-top: 0;
            }}

            .providence-nav-note {{
                display: none;
            }}
        }}

        /* Navigation and application-shell resilience */

        [data-testid="stSidebar"] > div:first-child {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        .providence-sidebar-footer {{
            margin-top: auto;
            padding: 1.5rem 0.25rem 0.5rem;
            color: var(--text-supporting);
            font-family: "Raleway", sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.04em;
        }}

        .providence-nav-tooltip,
        .providence-navigation-tooltip,
        [data-testid="stSidebar"] [role="tooltip"] {{
            display: none !important;
        }}

        .main .block-container,
        [data-testid="stMainBlockContainer"] {{
            padding-top: 4.5rem !important;
        }}

        @media (max-width: 860px) {{
            .main .block-container,
            [data-testid="stMainBlockContainer"] {{
                padding-top: 3.5rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }}

            .providence-sidebar-footer {{
                padding-top: 1rem;
            }}
        }}


        /* Phase 1: dark visual foundation */

        :root {{
            --providence-butter: #FFDE91;
            --providence-plum: #2C1338;
            --providence-blush: #FEF6F3;
            --providence-lavender: #A876F5;
            --providence-orchid: #E57CD8;
            --providence-coral: #FF8A7A;
            --providence-plum-glass: rgba(44, 19, 56, 0.74);
            --providence-blush-glass: rgba(254, 246, 243, 0.12);
            --providence-blush-border: rgba(254, 246, 243, 0.24);
            --providence-shadow-deep: 0 22px 64px rgba(17, 5, 24, 0.34);
        }}

        html,
        body,
        [class*="css"],
        [data-testid="stAppViewContainer"] {{
            background: var(--providence-plum);
            color: var(--providence-blush);
            font-family: "Raleway", ui-sans-serif, system-ui, sans-serif;
        }}

        .stApp {{
            min-height: 100vh;
            background:
                radial-gradient(circle at 83% 3%, rgba(168, 118, 245, 0.28), transparent 23rem),
                radial-gradient(circle at 18% 88%, rgba(229, 124, 216, 0.16), transparent 30rem),
                linear-gradient(145deg, #2C1338 0%, #20102A 52%, #2C1338 100%);
            color: var(--providence-blush);
        }}

        [data-testid="stHeader"] {{
            background: rgba(44, 19, 56, 0.78);
            border-bottom: 1px solid rgba(254, 246, 243, 0.12);
            backdrop-filter: blur(18px);
        }}

        [data-testid="stHeader"] *,
        [data-testid="stToolbar"] * {{
            color: var(--providence-blush) !important;
        }}

        .block-container,
        [data-testid="stMainBlockContainer"] {{
            max-width: 1480px;
        }}

        h1,
        h2,
        h3,
        h4,
        p,
        .stMarkdown,
        [data-testid="stCaptionContainer"] {{
            color: var(--providence-blush);
        }}

        h1 {{
            font-family: "Raleway", ui-sans-serif, system-ui, sans-serif;
            font-weight: 750;
            letter-spacing: -0.06em;
        }}

        h2,
        h3 {{
            font-family: "Raleway", ui-sans-serif, system-ui, sans-serif;
            color: var(--providence-blush);
        }}

        [data-testid="stSidebar"] {{
            background:
                radial-gradient(circle at 15% 0%, rgba(168, 118, 245, 0.24), transparent 18rem),
                linear-gradient(180deg, #2C1338 0%, #200F2A 100%);
            border-right: 1px solid rgba(254, 246, 243, 0.15);
        }}

        [data-testid="stSidebar"] > div:first-child {{
            background: transparent;
        }}

        .providence-mark {{
            background: var(--providence-butter);
            box-shadow: 0 10px 28px rgba(255, 222, 145, 0.26);
            color: var(--providence-plum);
        }}

        .providence-brand-name {{
            color: var(--providence-blush);
        }}

        .providence-brand-detail,
        .providence-nav-title,
        .providence-sidebar-footer {{
            color: rgba(254, 246, 243, 0.62);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label {{
            border: 1px solid transparent;
            color: rgba(254, 246, 243, 0.74);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
            background: rgba(254, 246, 243, 0.09);
            color: var(--providence-blush);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {{
            background: var(--providence-butter);
            border-color: var(--providence-butter);
            box-shadow: none;
            color: var(--providence-plum);
        }}

        .providence-page-header {{
            position: relative;
            padding: 1.55rem 1.7rem;
            border: 1px solid var(--providence-blush-border);
            border-radius: 1.45rem;
            background:
                linear-gradient(120deg, rgba(255, 222, 145, 0.10), transparent 42%),
                rgba(254, 246, 243, 0.07);
            box-shadow: var(--providence-shadow-deep);
            backdrop-filter: blur(18px);
        }}

        .providence-eyebrow {{
            color: var(--providence-butter);
            transform: rotate(-2deg);
            transform-origin: left center;
        }}

        .providence-page-subtitle,
        .providence-section-detail,
        .providence-hero-copy,
        .providence-health-hero-copy,
        .providence-insight-body,
        .providence-export-copy,
        .providence-empty-copy,
        .providence-person-role,
        .providence-project-count-copy,
        .providence-project-message {{
            color: rgba(254, 246, 243, 0.72);
        }}

        .providence-date-context {{
            background: rgba(254, 246, 243, 0.12);
            border-color: var(--providence-blush-border);
            color: var(--providence-blush);
            box-shadow: 0 10px 28px rgba(17, 5, 24, 0.18);
            backdrop-filter: blur(14px);
        }}

        [data-testid="stVerticalBlockBorderWrapper"],
        .providence-insight,
        .providence-export-area {{
            background:
                linear-gradient(135deg, rgba(168, 118, 245, 0.16), transparent 58%),
                var(--providence-blush-glass);
            border-color: var(--providence-blush-border);
            box-shadow: var(--providence-shadow-deep);
            backdrop-filter: blur(18px);
        }}

        .providence-insight {{
            border-color: rgba(255, 138, 122, 0.48);
        }}

        .providence-insight-label {{
            color: var(--providence-butter);
        }}

        .providence-insight-title,
        .providence-empty-title,
        .providence-export-title,
        .providence-person-name,
        .providence-preview-value,
        .providence-project-value,
        .providence-health-row-value,
        .providence-hero-value,
        .providence-health-hero-value,
        .providence-hero-stat-value,
        .providence-health-stat-value,
        .providence-project-count-value {{
            color: var(--providence-blush);
        }}

        [data-testid="stMetricLabel"],
        .providence-hero-label,
        .providence-health-hero-label,
        .providence-hero-stat-label,
        .providence-preview-label,
        .providence-health-stat-label,
        .providence-project-count-label {{
            color: rgba(255, 222, 145, 0.76);
        }}

        [data-testid="stMetricValue"] {{
            color: var(--providence-blush);
        }}

        .stButton > button {{
            background: var(--providence-coral);
            border-color: var(--providence-coral);
            box-shadow: 0 12px 28px rgba(255, 138, 122, 0.22);
            color: var(--providence-plum);
            font-family: "Raleway", ui-sans-serif, system-ui, sans-serif;
            font-weight: 800;
        }}

        .stButton > button:hover {{
            background: var(--providence-butter);
            border-color: var(--providence-butter);
            box-shadow: 0 16px 34px rgba(255, 222, 145, 0.22);
        }}

        .stDownloadButton > button {{
            background: rgba(254, 246, 243, 0.10);
            border-color: var(--providence-blush-border);
            color: var(--providence-blush);
            backdrop-filter: blur(12px);
        }}

        .stDownloadButton > button:hover {{
            background: rgba(254, 246, 243, 0.18);
            border-color: var(--providence-butter);
        }}

        [data-baseweb="select"] > div,
        [data-testid="stTextInput"] input {{
            background: rgba(254, 246, 243, 0.10);
            border-color: var(--providence-blush-border);
            color: var(--providence-blush);
        }}

        [data-testid="stTabs"] [data-baseweb="tab-list"] {{
            border-bottom-color: rgba(254, 246, 243, 0.18);
        }}

        [data-testid="stTabs"] [data-baseweb="tab"] {{
            color: rgba(254, 246, 243, 0.66);
        }}

        [data-testid="stTabs"] [aria-selected="true"] {{
            background: rgba(254, 246, 243, 0.10);
            color: var(--providence-butter);
        }}

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {{
            background-color: var(--providence-coral);
        }}

        [data-testid="stProgress"] > div > div {{
            background: rgba(254, 246, 243, 0.16);
        }}

        [data-testid="stProgress"] > div > div > div {{
            background: linear-gradient(
                90deg,
                var(--providence-lavender),
                var(--providence-orchid),
                var(--providence-coral)
            );
        }}

        [data-testid="stAlert"] {{
            background: rgba(254, 246, 243, 0.09);
            border-color: var(--providence-blush-border);
            color: var(--providence-blush);
            backdrop-filter: blur(14px);
        }}

        [data-testid="stAlert"] * {{
            color: var(--providence-blush) !important;
        }}

        [data-testid="stDataFrame"] {{
            border-color: var(--providence-blush-border);
            box-shadow: var(--providence-shadow-deep);
        }}

        hr {{
            border-color: rgba(254, 246, 243, 0.16);
        }}

        .providence-status-healthy {{
            background: rgba(168, 118, 245, 0.22);
            color: #EADFFF;
        }}

        .providence-status-watch {{
            background: rgba(255, 222, 145, 0.18);
            color: var(--providence-butter);
        }}

        .providence-status-risk {{
            background: rgba(255, 138, 122, 0.20);
            color: #FFC5BD;
        }}

        .providence-status-neutral {{
            background: rgba(229, 124, 216, 0.18);
            color: #F7C8EF;
        }}

        .providence-person-mark {{
            background: rgba(168, 118, 245, 0.24);
            border-color: rgba(254, 246, 243, 0.22);
            color: var(--providence-blush);
        }}

        .stButton > button:focus-visible,
        .stDownloadButton > button:focus-visible,
        button:focus-visible,
        input:focus-visible,
        [role="tab"]:focus-visible,
        [role="radio"]:focus-visible {{
            outline-color: var(--providence-butter) !important;
        }}

        @media (max-width: 860px) {{
            .providence-page-header {{
                padding: 1.2rem;
                border-radius: 1.1rem;
            }}

            .providence-date-context {{
                width: 100%;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            *,
            *::before,
            *::after {{
                scroll-behavior: auto !important;
                transition-duration: 0.01ms !important;
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
            }}
        }}


        /* Phase 2: shell, navigation, and shared component elevation */

        :root {{
            --providence-sidebar-width: 17.25rem;
            --providence-shell-gutter: clamp(1rem, 2.4vw, 2.6rem);
            --providence-shell-top: clamp(5.2rem, 7vw, 6.6rem);
            --providence-glass-strong: rgba(254, 246, 243, 0.15);
            --providence-glass-soft: rgba(254, 246, 243, 0.08);
            --providence-glow-violet: rgba(168, 118, 245, 0.30);
            --providence-glow-coral: rgba(255, 138, 122, 0.24);
        }}

        [data-testid="stSidebar"] {{
            min-width: var(--providence-sidebar-width);
            width: var(--providence-sidebar-width);
        }}

        [data-testid="stSidebar"] > div:first-child {{
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            padding: 1.35rem 1rem 1.15rem;
        }}

        [data-testid="stSidebar"] > div:first-child::before {{
            position: absolute;
            top: 0;
            right: 0;
            left: 0;
            height: 0.22rem;
            background: linear-gradient(
                90deg,
                var(--providence-butter),
                var(--providence-lavender),
                var(--providence-orchid),
                var(--providence-coral)
            );
            content: "";
        }}

        .providence-brand {{
            position: relative;
            margin: 0.35rem 0 1.8rem;
            padding: 0.7rem;
            border: 1px solid rgba(254, 246, 243, 0.12);
            border-radius: 1.2rem;
            background:
                linear-gradient(135deg, rgba(255, 222, 145, 0.14), transparent 55%),
                rgba(254, 246, 243, 0.06);
            box-shadow: 0 14px 30px rgba(12, 4, 18, 0.20);
        }}

        .providence-brand::after {{
            position: absolute;
            top: -0.28rem;
            right: 1rem;
            width: 0.55rem;
            height: 0.55rem;
            border-radius: 999px;
            background: var(--providence-coral);
            box-shadow: 0 0 0 0.24rem rgba(255, 138, 122, 0.16);
            content: "";
        }}

        .providence-mark {{
            width: 2.35rem;
            height: 2.35rem;
            border-radius: 0.88rem;
            font-size: 0.9rem;
        }}

        .providence-brand-name {{
            font-size: 1.18rem;
            font-weight: 800;
        }}

        .providence-brand-detail {{
            color: rgba(254, 246, 243, 0.56);
            font-size: 0.66rem;
            letter-spacing: 0.12em;
        }}

        .providence-nav-title {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 0.35rem 0.4rem 0.78rem;
            color: var(--providence-butter);
            font-size: 0.64rem;
            font-weight: 800;
            letter-spacing: 0.13em;
        }}

        .providence-nav-title::after {{
            height: 1px;
            flex: 1;
            background: linear-gradient(90deg, rgba(255, 222, 145, 0.45), transparent);
            content: "";
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] > div {{
            gap: 0.42rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label {{
            position: relative;
            min-height: 3.05rem;
            display: flex;
            align-items: center;
            border-radius: 0.92rem;
            font-size: 0.94rem;
            font-weight: 700;
            letter-spacing: -0.015em;
            padding: 0.72rem 0.85rem 0.72rem 1.04rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label::before {{
            width: 0.52rem;
            height: 0.52rem;
            flex: 0 0 auto;
            margin-right: 0.1rem;
            border: 1px solid rgba(254, 246, 243, 0.40);
            border-radius: 50%;
            content: "";
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
            transform: translateX(0.18rem);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {{
            position: relative;
            background:
                linear-gradient(100deg, var(--providence-butter), #FFD582);
            box-shadow: 0 12px 24px rgba(255, 222, 145, 0.16);
            color: var(--providence-plum);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked)::before {{
            border-color: var(--providence-plum);
            background: var(--providence-coral);
            box-shadow: 0 0 0 0.2rem rgba(44, 19, 56, 0.12);
        }}

        .providence-sidebar-footer {{
            position: relative;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: auto;
            padding: 1.25rem 0.55rem 0.3rem;
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.05em;
        }}

        .providence-sidebar-footer::before {{
            width: 1.5rem;
            height: 1px;
            background: var(--providence-lavender);
            content: "";
        }}

        [data-testid="stMainBlockContainer"],
        .main .block-container {{
            position: relative;
            padding:
                var(--providence-shell-top)
                var(--providence-shell-gutter)
                clamp(2.5rem, 5vw, 5rem) !important;
        }}

        [data-testid="stMainBlockContainer"]::before {{
            position: fixed;
            z-index: -1;
            top: 7.5rem;
            right: clamp(1rem, 4vw, 4rem);
            width: min(22vw, 20rem);
            height: min(22vw, 20rem);
            border-radius: 50%;
            background: var(--providence-butter);
            filter: blur(1px);
            opacity: 0.08;
            content: "";
        }}

        .providence-page-header {{
            align-items: stretch;
            overflow: hidden;
            isolation: isolate;
            margin-bottom: clamp(2rem, 4vw, 3.4rem);
            padding: clamp(1.3rem, 3vw, 2.2rem);
            border-radius: 1.55rem;
        }}

        .providence-page-header::after {{
            position: absolute;
            z-index: -1;
            top: -7rem;
            right: -5rem;
            width: 15rem;
            height: 15rem;
            border-radius: 50%;
            background: radial-gradient(
                circle,
                rgba(168, 118, 245, 0.38) 0%,
                transparent 68%
            );
            content: "";
        }}

        .providence-page-header > div:first-child {{
            max-width: 47rem;
        }}

        .providence-eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            margin-bottom: 0.72rem;
        }}

        .providence-eyebrow::before {{
            width: 0.56rem;
            height: 0.56rem;
            border-radius: 50%;
            background: var(--providence-coral);
            box-shadow: 0 0 0 0.22rem rgba(255, 138, 122, 0.16);
            content: "";
        }}

        .providence-page-header h1 {{
            max-width: 12ch;
            font-size: clamp(2.6rem, 5vw, 4.8rem);
            line-height: 0.93;
        }}

        .providence-page-subtitle {{
            max-width: 39rem;
            font-size: clamp(0.98rem, 1.5vw, 1.1rem);
        }}

        .providence-date-context {{
            display: inline-flex;
            align-items: center;
            height: fit-content;
            gap: 0.5rem;
            border-color: rgba(255, 222, 145, 0.34);
            border-radius: 999px;
            background: rgba(44, 19, 56, 0.34);
            color: var(--providence-butter);
            font-size: 0.76rem;
            letter-spacing: 0.025em;
        }}

        .providence-date-context::before {{
            width: 0.46rem;
            height: 0.46rem;
            border-radius: 50%;
            background: var(--providence-lavender);
            box-shadow: 0 0 0 0.2rem rgba(168, 118, 245, 0.16);
            content: "";
        }}

        .providence-section-heading {{
            position: relative;
            margin: clamp(2.5rem, 5vw, 4.5rem) 0 1.25rem;
            padding-bottom: 0.8rem;
        }}

        .providence-section-heading::after {{
            position: absolute;
            right: 0;
            bottom: 0;
            left: 0;
            height: 1px;
            background: linear-gradient(
                90deg,
                rgba(255, 222, 145, 0.48),
                rgba(168, 118, 245, 0.22),
                transparent
            );
            content: "";
        }}

        .providence-section-heading h2 {{
            font-size: clamp(1.5rem, 2.5vw, 2.05rem);
            letter-spacing: -0.045em;
        }}

        .providence-section-detail {{
            padding: 0.38rem 0.65rem;
            border: 1px solid rgba(254, 246, 243, 0.16);
            border-radius: 999px;
            background: rgba(254, 246, 243, 0.07);
            color: rgba(254, 246, 243, 0.68);
        }}

        .providence-insight {{
            padding: 1.45rem;
            border-width: 1px;
            border-radius: 1.3rem;
            background:
                radial-gradient(circle at 100% 0%, rgba(255, 138, 122, 0.25), transparent 40%),
                linear-gradient(135deg, rgba(168, 118, 245, 0.20), transparent 68%),
                rgba(254, 246, 243, 0.10);
        }}

        .providence-insight::before {{
            position: absolute;
            top: 0;
            left: 0;
            width: 0.28rem;
            height: 100%;
            border-radius: 1rem 0 0 1rem;
            background: linear-gradient(
                180deg,
                var(--providence-butter),
                var(--providence-coral),
                var(--providence-orchid)
            );
            content: "";
        }}

        .providence-insight-label {{
            display: inline-flex;
            padding: 0.32rem 0.55rem;
            border-radius: 999px;
            background: rgba(255, 222, 145, 0.15);
            color: var(--providence-butter);
        }}

        .providence-status {{
            border: 1px solid rgba(254, 246, 243, 0.14);
            box-shadow: inset 0 1px 0 rgba(254, 246, 243, 0.12);
            padding: 0.4rem 0.7rem;
        }}

        .stButton > button {{
            min-height: 2.9rem;
            border-radius: 999px;
            padding: 0.66rem 1.15rem;
        }}

        .stDownloadButton > button {{
            min-height: 2.9rem;
            border-radius: 999px;
            padding: 0.66rem 1.1rem;
        }}

        [data-testid="stTabs"] [data-baseweb="tab-list"] {{
            padding: 0.32rem;
            border: 1px solid rgba(254, 246, 243, 0.14);
            border-radius: 1rem;
            background: rgba(254, 246, 243, 0.06);
        }}

        [data-testid="stTabs"] [data-baseweb="tab"] {{
            border-radius: 0.7rem;
        }}

        [data-testid="stTabs"] [aria-selected="true"] {{
            background: rgba(255, 222, 145, 0.16);
        }}

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {{
            display: none;
        }}

        [data-baseweb="select"] > div,
        [data-testid="stTextInput"] input {{
            border-radius: 0.88rem;
        }}

        @media (max-width: 860px) {{
            [data-testid="stSidebar"] {{
                min-width: 0;
                width: auto;
            }}

            [data-testid="stMainBlockContainer"],
            .main .block-container {{
                padding-top: 5.2rem !important;
            }}

            .providence-page-header {{
                border-radius: 1.2rem;
            }}

            .providence-page-header h1 {{
                max-width: none;
                font-size: clamp(2.4rem, 12vw, 3.5rem);
            }}

            .providence-date-context {{
                width: fit-content;
            }}

            .providence-section-heading {{
                align-items: flex-start;
                flex-direction: column;
                gap: 0.7rem;
            }}
        }}


        /* Phase 2: active navigation contrast correction */

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked),
        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) * {{
            color: #2C1338 !important;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked)::before {{
            background: #2C1338;
            border-color: #2C1338;
        }}


        /* Phase 3: Overview flagship composition */

        .providence-overview-stage {{
            display: block;
            margin-top: -0.75rem;
        }}

        .providence-overview-hero {{
            position: relative;
            overflow: hidden;
            min-height: 29rem;
            padding: clamp(1.45rem, 3vw, 2.45rem);
            border: 1px solid rgba(44, 19, 56, 0.18);
            border-radius: 1.7rem;
            background:
                radial-gradient(circle at 89% 20%, rgba(168, 118, 245, 0.72), transparent 23%),
                radial-gradient(circle at 72% 88%, rgba(229, 124, 216, 0.52), transparent 25%),
                linear-gradient(135deg, #FFDE91 0%, #FFD88C 52%, #FFCF9B 100%);
            box-shadow: 0 26px 70px rgba(12, 4, 18, 0.24);
            color: var(--providence-plum);
        }}

        .providence-overview-hero::after {{
            position: absolute;
            right: -4.5rem;
            bottom: -7rem;
            width: 18rem;
            height: 18rem;
            border: 1px solid rgba(44, 19, 56, 0.18);
            border-radius: 50%;
            content: "";
        }}

        .providence-overview-hero-topline,
        .providence-overview-pace-labels,
        .providence-overview-hero-stats,
        .providence-overview-project,
        .providence-overview-decision-foot {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .providence-overview-kicker,
        .providence-overview-hero-label,
        .providence-overview-metric-label {{
            display: inline-flex;
            color: inherit;
            font-size: 0.68rem;
            font-weight: 850;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }}

        .providence-overview-live {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.42rem 0.62rem;
            border: 1px solid rgba(44, 19, 56, 0.16);
            border-radius: 999px;
            background: rgba(254, 246, 243, 0.34);
            color: rgba(44, 19, 56, 0.82);
            font-size: 0.7rem;
            font-weight: 750;
        }}

        .providence-overview-live i {{
            width: 0.45rem;
            height: 0.45rem;
            border-radius: 50%;
            background: #2C1338;
            box-shadow: 0 0 0 0.24rem rgba(44, 19, 56, 0.12);
        }}

        .providence-overview-hero-grid {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 1.5rem;
            margin: clamp(2.4rem, 5vw, 4.2rem) 0 1.45rem;
        }}

        .providence-overview-burn {{
            color: var(--providence-plum);
            font-size: clamp(4.7rem, 10vw, 8.4rem);
            font-weight: 850;
            letter-spacing: -0.1em;
            line-height: 0.76;
        }}

        .providence-overview-hero-copy {{
            max-width: 26rem;
            color: rgba(44, 19, 56, 0.75);
            font-size: 1rem;
            font-weight: 600;
            line-height: 1.45;
            margin: 1.1rem 0 0;
        }}

        .providence-overview-orbit {{
            width: clamp(7rem, 13vw, 10.5rem);
            height: clamp(7rem, 13vw, 10.5rem);
            display: grid;
            place-items: center;
            align-content: center;
            border: 1rem solid rgba(44, 19, 56, 0.10);
            border-top-color: var(--providence-plum);
            border-right-color: var(--providence-lavender);
            border-radius: 50%;
            background: rgba(254, 246, 243, 0.26);
            color: var(--providence-plum);
            transform: rotate(18deg);
        }}

        .providence-overview-orbit span,
        .providence-overview-orbit small {{
            transform: rotate(-18deg);
        }}

        .providence-overview-orbit span {{
            font-size: clamp(1.45rem, 3vw, 2.25rem);
            font-weight: 850;
            letter-spacing: -0.08em;
            line-height: 1;
        }}

        .providence-overview-orbit small {{
            margin-top: 0.2rem;
            font-size: 0.64rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        .providence-overview-pace {{
            position: relative;
            z-index: 1;
            margin-top: 1.3rem;
        }}

        .providence-overview-pace-track,
        .providence-overview-project-progress,
        .providence-overview-metric-line {{
            overflow: hidden;
            height: 0.7rem;
            border-radius: 999px;
            background: rgba(44, 19, 56, 0.15);
        }}

        .providence-overview-pace-track span,
        .providence-overview-project-progress span,
        .providence-overview-metric-line span {{
            display: block;
            height: 100%;
            border-radius: inherit;
        }}

        .providence-overview-pace-track span {{
            background: linear-gradient(
                90deg,
                var(--providence-plum),
                var(--providence-lavender),
                var(--providence-orchid),
                var(--providence-coral)
            );
        }}

        .providence-overview-pace-labels {{
            margin-top: 0.65rem;
            color: rgba(44, 19, 56, 0.7);
            font-size: 0.74rem;
            font-weight: 750;
        }}

        .providence-overview-hero-stats {{
            position: relative;
            z-index: 1;
            margin-top: 1.55rem;
            padding-top: 1.1rem;
            border-top: 1px solid rgba(44, 19, 56, 0.16);
        }}

        .providence-overview-hero-stats div {{
            flex: 1;
        }}

        .providence-overview-hero-stats span,
        .providence-overview-project-data span,
        .providence-overview-signal span {{
            display: block;
            color: rgba(44, 19, 56, 0.66);
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }}

        .providence-overview-hero-stats strong {{
            display: block;
            margin-top: 0.24rem;
            color: var(--providence-plum);
            font-size: clamp(1rem, 2vw, 1.35rem);
            font-weight: 850;
            letter-spacing: -0.055em;
        }}

        .providence-overview-decision {{
            position: relative;
            overflow: hidden;
            min-height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: clamp(1.4rem, 2.5vw, 2rem);
            border: 1px solid rgba(254, 246, 243, 0.26);
            border-radius: 1.7rem;
            background:
                radial-gradient(circle at 100% 0%, rgba(255, 138, 122, 0.32), transparent 34%),
                linear-gradient(145deg, rgba(168, 118, 245, 0.42), rgba(44, 19, 56, 0.92) 58%);
            box-shadow: var(--providence-shadow-deep);
            color: var(--providence-blush);
        }}

        .providence-overview-decision h2 {{
            max-width: 12ch;
            margin: 1.6rem 0 0.9rem;
            color: var(--providence-blush);
            font-size: clamp(1.55rem, 3vw, 2.2rem);
            font-weight: 800;
            letter-spacing: -0.06em;
            line-height: 1.04;
        }}

        .providence-overview-decision p {{
            position: relative;
            z-index: 1;
            margin: 0;
            color: rgba(254, 246, 243, 0.78);
            font-size: 0.94rem;
            line-height: 1.6;
        }}

        .providence-overview-decision .providence-overview-kicker {{
            color: var(--providence-butter);
        }}

        .providence-overview-decision-orb {{
            position: absolute;
            right: -3rem;
            bottom: -3rem;
            width: 10rem;
            height: 10rem;
            border: 1px solid rgba(254, 246, 243, 0.24);
            border-radius: 50%;
        }}

        .providence-overview-decision-foot {{
            position: relative;
            z-index: 1;
            margin-top: 2rem;
            padding-top: 0.9rem;
            border-top: 1px solid rgba(254, 246, 243, 0.18);
            color: rgba(254, 246, 243, 0.62);
            font-size: 0.7rem;
            font-weight: 750;
            letter-spacing: 0.04em;
        }}

        .providence-overview-decision-foot strong {{
            color: var(--providence-butter);
            font-size: 0.74rem;
        }}

        .providence-overview-metric {{
            position: relative;
            overflow: hidden;
            min-height: 13.2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 1.35rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.35rem;
            box-shadow: 0 18px 42px rgba(12, 4, 18, 0.18);
        }}

        .providence-overview-metric::after {{
            position: absolute;
            top: -2rem;
            right: -2rem;
            width: 7rem;
            height: 7rem;
            border-radius: 50%;
            content: "";
        }}

        .providence-overview-metric-violet {{
            background: linear-gradient(
                145deg,
                rgba(168, 118, 245, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-overview-metric-violet::after {{
            background: rgba(168, 118, 245, 0.38);
        }}

        .providence-overview-metric-pink {{
            background: linear-gradient(
                145deg,
                rgba(229, 124, 216, 0.40),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-overview-metric-pink::after {{
            background: rgba(229, 124, 216, 0.34);
        }}

        .providence-overview-metric-coral {{
            background: linear-gradient(
                145deg,
                rgba(255, 138, 122, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-overview-metric-coral::after {{
            background: rgba(255, 138, 122, 0.34);
        }}

        .providence-overview-metric-label {{
            position: relative;
            z-index: 1;
            color: var(--providence-butter);
        }}

        .providence-overview-metric strong {{
            position: relative;
            z-index: 1;
            display: block;
            margin-top: 1rem;
            color: var(--providence-blush);
            font-size: clamp(2.7rem, 5vw, 4.2rem);
            font-weight: 850;
            letter-spacing: -0.09em;
            line-height: 0.88;
        }}

        .providence-overview-metric p {{
            position: relative;
            z-index: 1;
            max-width: 16rem;
            margin: 0.9rem 0 0;
            color: rgba(254, 246, 243, 0.74);
            font-size: 0.82rem;
            font-weight: 600;
            line-height: 1.45;
        }}

        .providence-overview-metric-line {{
            position: relative;
            z-index: 1;
            margin-top: 1.3rem;
            background: rgba(254, 246, 243, 0.20);
        }}

        .providence-overview-metric-line span {{
            background: var(--providence-butter);
        }}

        .providence-overview-metric-dots {{
            position: relative;
            z-index: 1;
            display: flex;
            gap: 0.38rem;
            margin-top: 1.5rem;
        }}

        .providence-overview-metric-dots i {{
            width: 0.7rem;
            height: 0.7rem;
            border-radius: 50%;
            background: var(--providence-butter);
        }}

        .providence-overview-metric-dots i:nth-child(2) {{
            background: rgba(254, 246, 243, 0.74);
        }}

        .providence-overview-metric-dots i:nth-child(3) {{
            background: rgba(254, 246, 243, 0.32);
        }}

        .providence-overview-attention-badge {{
            position: relative;
            z-index: 1;
            width: fit-content;
            margin-top: 1.2rem;
            padding: 0.42rem 0.68rem;
            border: 1px solid rgba(254, 246, 243, 0.24);
            border-radius: 999px;
            color: var(--providence-blush);
            font-size: 0.72rem;
            font-weight: 800;
        }}

        .providence-overview-project {{
            position: relative;
            margin-bottom: 0.7rem;
            padding: 1rem;
            border: 1px solid rgba(254, 246, 243, 0.14);
            border-radius: 1.1rem;
            background: rgba(254, 246, 243, 0.07);
            box-shadow: inset 0 1px 0 rgba(254, 246, 243, 0.08);
        }}

        .providence-overview-project-index {{
            width: 2rem;
            color: var(--providence-butter);
            font-size: 0.76rem;
            font-weight: 850;
            letter-spacing: 0.04em;
        }}

        .providence-overview-project-main {{
            min-width: 0;
            flex: 1;
        }}

        .providence-overview-project-title-row h3 {{
            margin: 0;
            color: var(--providence-blush);
            font-size: 1rem;
            font-weight: 800;
            letter-spacing: -0.035em;
        }}

        .providence-overview-project-title-row p {{
            margin: 0.16rem 0 0;
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.76rem;
        }}

        .providence-overview-project-progress {{
            height: 0.4rem;
            margin-top: 0.75rem;
            background: rgba(254, 246, 243, 0.14);
        }}

        .providence-overview-project-progress span {{
            background: linear-gradient(90deg, var(--providence-lavender), var(--providence-coral));
        }}

        .providence-overview-project-data {{
            min-width: 5.4rem;
        }}

        .providence-overview-project-data strong {{
            display: block;
            margin-top: 0.22rem;
            color: var(--providence-blush);
            font-size: 1rem;
            font-weight: 850;
            letter-spacing: -0.05em;
        }}

        .providence-overview-project + div [class*="providence-status"] {{
            position: relative;
            top: -3.1rem;
            float: right;
            margin-right: 12.8rem;
        }}

        .providence-overview-signal-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.7rem;
        }}

        .providence-overview-signal {{
            min-height: 10rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 1.1rem;
            border: 1px solid rgba(254, 246, 243, 0.18);
            border-radius: 1.2rem;
        }}

        .providence-overview-signal-risk {{
            background: linear-gradient(145deg, rgba(255, 138, 122, 0.38), rgba(44, 19, 56, 0.45));
        }}

        .providence-overview-signal-watch {{
            background: linear-gradient(145deg, rgba(255, 222, 145, 0.28), rgba(44, 19, 56, 0.45));
        }}

        .providence-overview-signal strong {{
            margin-top: 0.7rem;
            color: var(--providence-blush);
            font-size: 3.1rem;
            font-weight: 850;
            letter-spacing: -0.09em;
            line-height: 0.8;
        }}

        .providence-overview-signal p {{
            margin: 0.7rem 0 0;
            color: rgba(254, 246, 243, 0.66);
            font-size: 0.74rem;
            font-weight: 650;
        }}

        .providence-overview-people {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-top: 0.75rem;
            padding: 1.25rem;
            border: 1px solid rgba(254, 246, 243, 0.16);
            border-radius: 1.25rem;
            background: rgba(254, 246, 243, 0.08);
        }}

        .providence-overview-people h3,
        .providence-overview-export h3,
        .providence-overview-empty h3 {{
            margin: 0.5rem 0 0;
            color: var(--providence-blush);
            font-size: 1.1rem;
            font-weight: 800;
            letter-spacing: -0.04em;
        }}

        .providence-overview-people p,
        .providence-overview-export p,
        .providence-overview-empty p {{
            margin: 0.55rem 0 0;
            color: rgba(254, 246, 243, 0.68);
            font-size: 0.84rem;
            line-height: 1.5;
        }}

        .providence-overview-people-mark {{
            width: 4.7rem;
            height: 4.7rem;
            display: grid;
            place-items: center;
            align-content: center;
            flex: 0 0 auto;
            border: 1px solid rgba(255, 222, 145, 0.35);
            border-radius: 50%;
            background: rgba(255, 222, 145, 0.14);
        }}

        .providence-overview-people-mark span {{
            color: var(--providence-butter);
            font-size: 1.15rem;
            font-weight: 850;
            letter-spacing: -0.06em;
        }}

        .providence-overview-people-mark small {{
            margin-top: 0.1rem;
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.58rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        .providence-overview-export,
        .providence-overview-empty {{
            position: relative;
            overflow: hidden;
            margin-top: 2.5rem;
            padding: 1.45rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.4rem;
            background:
                linear-gradient(100deg, rgba(168, 118, 245, 0.24), transparent 56%),
                rgba(254, 246, 243, 0.08);
        }}

        .providence-overview-export + div {{
            margin-top: 0.85rem;
        }}

        .providence-overview-export + div .stDownloadButton > button {{
            width: 100%;
        }}

        @media (max-width: 860px) {{
            .providence-overview-hero {{
                min-height: auto;
                border-radius: 1.35rem;
            }}

            .providence-overview-hero-grid {{
                grid-template-columns: 1fr;
                margin-top: 2rem;
            }}

            .providence-overview-orbit {{
                justify-self: end;
                margin-top: -5.5rem;
            }}

            .providence-overview-hero-stats {{
                flex-wrap: wrap;
            }}

            .providence-overview-hero-stats div {{
                min-width: 30%;
            }}

            .providence-overview-project {{
                align-items: flex-start;
                flex-wrap: wrap;
            }}

            .providence-overview-project-main {{
                order: 1;
                width: calc(100% - 3rem);
            }}

            .providence-overview-project-index {{
                order: 0;
            }}

            .providence-overview-project-data {{
                order: 2;
                margin-left: 2rem;
            }}

            .providence-overview-project + div [class*="providence-status"] {{
                position: static;
                float: none;
                display: inline-flex;
                margin: -0.15rem 0 0.85rem 3rem;
            }}
        }}

        @media (max-width: 540px) {{
            .providence-overview-hero {{
                padding: 1.2rem;
            }}

            .providence-overview-burn {{
                font-size: 4.5rem;
            }}

            .providence-overview-orbit {{
                width: 6.7rem;
                height: 6.7rem;
                border-width: 0.72rem;
                margin-top: -4.2rem;
            }}

            .providence-overview-hero-stats {{
                gap: 0.8rem;
            }}

            .providence-overview-hero-stats strong {{
                font-size: 0.98rem;
            }}

            .providence-overview-project-data {{
                min-width: 0;
                margin-left: 3rem;
            }}

            .providence-overview-signal-grid {{
                grid-template-columns: 1fr;
            }}
        }}


        /* Phase 4: Health and Project workflows */

        .providence-health-stage,
        .providence-project-stage {{
            display: block;
            margin-top: -0.75rem;
        }}

        .providence-health-kicker,
        .providence-project-kicker,
        .providence-health-hero-label,
        .providence-health-signal span,
        .providence-health-project-data span,
        .providence-project-metric span,
        .providence-project-card-data span {{
            display: inline-flex;
            color: var(--providence-butter);
            font-size: 0.66rem;
            font-weight: 850;
            letter-spacing: 0.11em;
            text-transform: uppercase;
        }}

        .providence-health-hero {{
            position: relative;
            overflow: hidden;
            min-height: 27rem;
            padding: clamp(1.4rem, 3vw, 2.3rem);
            border: 1px solid rgba(44, 19, 56, 0.18);
            border-radius: 1.65rem;
            background:
                radial-gradient(circle at 88% 18%, rgba(168, 118, 245, 0.70), transparent 24%),
                radial-gradient(circle at 68% 90%, rgba(229, 124, 216, 0.48), transparent 25%),
                linear-gradient(135deg, #FFDE91, #FFD88C 54%, #FFCF9B);
            box-shadow: 0 24px 65px rgba(12, 4, 18, 0.23);
            color: var(--providence-plum);
        }}

        .providence-health-hero::after {{
            position: absolute;
            right: -4rem;
            bottom: -6.5rem;
            width: 16rem;
            height: 16rem;
            border: 1px solid rgba(44, 19, 56, 0.17);
            border-radius: 50%;
            content: "";
        }}

        .providence-health-hero-topline,
        .providence-health-pace-labels,
        .providence-health-hero-stats,
        .providence-health-decision-foot {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .providence-health-live {{
            display: inline-flex;
            align-items: center;
            gap: 0.42rem;
            padding: 0.4rem 0.6rem;
            border: 1px solid rgba(44, 19, 56, 0.16);
            border-radius: 999px;
            background: rgba(254, 246, 243, 0.34);
            color: rgba(44, 19, 56, 0.82);
            font-size: 0.68rem;
            font-weight: 750;
        }}

        .providence-health-live i {{
            width: 0.42rem;
            height: 0.42rem;
            border-radius: 50%;
            background: #2C1338;
            box-shadow: 0 0 0 0.22rem rgba(44, 19, 56, 0.12);
        }}

        .providence-health-hero-grid {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 1.35rem;
            margin: clamp(2rem, 4.5vw, 3.5rem) 0 1.3rem;
        }}

        .providence-health-hero strong {{
            display: block;
            margin-top: 0.55rem;
            color: var(--providence-plum);
            font-size: clamp(4rem, 8vw, 6.8rem);
            font-weight: 850;
            letter-spacing: -0.1em;
            line-height: 0.78;
        }}

        .providence-health-hero p {{
            max-width: 25rem;
            margin: 0.9rem 0 0;
            color: rgba(44, 19, 56, 0.75);
            font-size: 0.94rem;
            font-weight: 600;
            line-height: 1.45;
        }}

        .providence-health-orbit {{
            width: clamp(6.5rem, 12vw, 9.5rem);
            height: clamp(6.5rem, 12vw, 9.5rem);
            display: grid;
            place-items: center;
            align-content: center;
            border: 0.9rem solid rgba(44, 19, 56, 0.10);
            border-top-color: var(--providence-plum);
            border-right-color: var(--providence-lavender);
            border-radius: 50%;
            background: rgba(254, 246, 243, 0.26);
            transform: rotate(18deg);
        }}

        .providence-health-orbit span,
        .providence-health-orbit small {{
            transform: rotate(-18deg);
        }}

        .providence-health-orbit span {{
            color: var(--providence-plum);
            font-size: clamp(1.3rem, 2.6vw, 1.9rem);
            font-weight: 850;
            letter-spacing: -0.08em;
        }}

        .providence-health-orbit small {{
            margin-top: 0.18rem;
            color: rgba(44, 19, 56, 0.7);
            font-size: 0.58rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        .providence-health-pace-track,
        .providence-health-project-progress,
        .providence-project-card-progress {{
            overflow: hidden;
            height: 0.62rem;
            border-radius: 999px;
            background: rgba(44, 19, 56, 0.15);
        }}

        .providence-health-pace-track span,
        .providence-health-project-progress span,
        .providence-project-card-progress span {{
            display: block;
            height: 100%;
            border-radius: inherit;
        }}

        .providence-health-pace-track span {{
            background: linear-gradient(
                90deg,
                var(--providence-plum),
                var(--providence-lavender),
                var(--providence-orchid),
                var(--providence-coral)
            );
        }}

        .providence-health-pace-labels {{
            margin-top: 0.6rem;
            color: rgba(44, 19, 56, 0.7);
            font-size: 0.72rem;
            font-weight: 750;
        }}

        .providence-health-hero-stats {{
            position: relative;
            z-index: 1;
            margin-top: 1.4rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(44, 19, 56, 0.16);
        }}

        .providence-health-hero-stats div {{
            flex: 1;
        }}

        .providence-health-hero-stats span,
        .providence-health-project-data span,
        .providence-health-signal span {{
            color: rgba(44, 19, 56, 0.66);
        }}

        .providence-health-hero-stats strong {{
            margin-top: 0.2rem;
            font-size: clamp(0.95rem, 1.8vw, 1.2rem);
            letter-spacing: -0.05em;
        }}

        .providence-health-decision {{
            position: relative;
            overflow: hidden;
            min-height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: clamp(1.35rem, 2.4vw, 1.9rem);
            border: 1px solid rgba(254, 246, 243, 0.26);
            border-radius: 1.65rem;
            background:
                radial-gradient(circle at 100% 0%, rgba(255, 138, 122, 0.32), transparent 34%),
                linear-gradient(145deg, rgba(168, 118, 245, 0.42), rgba(44, 19, 56, 0.92) 58%);
            box-shadow: var(--providence-shadow-deep);
            color: var(--providence-blush);
        }}

        .providence-health-decision h2,
        .providence-project-decision h2 {{
            max-width: 13ch;
            margin: 1.35rem 0 0.8rem;
            color: var(--providence-blush);
            font-size: clamp(1.45rem, 2.8vw, 2rem);
            font-weight: 800;
            letter-spacing: -0.06em;
            line-height: 1.05;
        }}

        .providence-health-decision p,
        .providence-project-decision p {{
            position: relative;
            z-index: 1;
            margin: 0;
            color: rgba(254, 246, 243, 0.78);
            font-size: 0.92rem;
            line-height: 1.6;
        }}

        .providence-health-decision::after,
        .providence-project-decision::after {{
            position: absolute;
            right: -2.8rem;
            bottom: -2.8rem;
            width: 9rem;
            height: 9rem;
            border: 1px solid rgba(254, 246, 243, 0.22);
            border-radius: 50%;
            content: "";
        }}

        .providence-health-decision-foot {{
            position: relative;
            z-index: 1;
            margin-top: 1.8rem;
            padding-top: 0.85rem;
            border-top: 1px solid rgba(254, 246, 243, 0.18);
            color: rgba(254, 246, 243, 0.62);
            font-size: 0.7rem;
            font-weight: 750;
        }}

        .providence-health-decision-foot strong {{
            color: var(--providence-butter);
            font-size: 0.82rem;
        }}

        .providence-health-signal,
        .providence-project-metric {{
            position: relative;
            overflow: hidden;
            min-height: 11.5rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 1.2rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.3rem;
            box-shadow: 0 16px 38px rgba(12, 4, 18, 0.18);
        }}

        .providence-health-signal::after,
        .providence-project-metric::after {{
            position: absolute;
            top: -2rem;
            right: -2rem;
            width: 6.5rem;
            height: 6.5rem;
            border-radius: 50%;
            content: "";
        }}

        .providence-health-signal-risk,
        .providence-project-metric-coral {{
            background: linear-gradient(
                145deg,
                rgba(255, 138, 122, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-health-signal-risk::after,
        .providence-project-metric-coral::after {{
            background: rgba(255, 138, 122, 0.32);
        }}

        .providence-health-signal-watch,
        .providence-project-metric-pink {{
            background: linear-gradient(
                145deg,
                rgba(229, 124, 216, 0.40),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-health-signal-watch::after,
        .providence-project-metric-pink::after {{
            background: rgba(229, 124, 216, 0.32);
        }}

        .providence-health-signal-capacity,
        .providence-project-metric-violet {{
            background: linear-gradient(
                145deg,
                rgba(168, 118, 245, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-health-signal-capacity::after,
        .providence-project-metric-violet::after {{
            background: rgba(168, 118, 245, 0.32);
        }}

        .providence-health-signal strong,
        .providence-project-metric strong {{
            position: relative;
            z-index: 1;
            display: block;
            margin-top: 0.7rem;
            color: var(--providence-blush);
            font-size: clamp(2.2rem, 4vw, 3.2rem);
            font-weight: 850;
            letter-spacing: -0.09em;
            line-height: 0.82;
        }}

        .providence-health-signal p,
        .providence-project-metric p {{
            position: relative;
            z-index: 1;
            margin: 0.75rem 0 0;
            color: rgba(254, 246, 243, 0.74);
            font-size: 0.8rem;
            font-weight: 600;
            line-height: 1.4;
        }}

        .providence-health-project,
        .providence-project-card {{
            position: relative;
            display: flex;
            align-items: center;
            gap: 1.1rem;
            margin-bottom: 0.7rem;
            padding: 1.05rem;
            border: 1px solid rgba(254, 246, 243, 0.14);
            border-radius: 1.15rem;
            background: rgba(254, 246, 243, 0.07);
            box-shadow: inset 0 1px 0 rgba(254, 246, 243, 0.08);
        }}

        .providence-health-project-main,
        .providence-project-card-main {{
            min-width: 0;
            flex: 1;
        }}

        .providence-health-project h3,
        .providence-project-card h3 {{
            margin: 0;
            color: var(--providence-blush);
            font-size: 1rem;
            font-weight: 800;
            letter-spacing: -0.035em;
        }}

        .providence-health-project p,
        .providence-project-card p {{
            margin: 0.15rem 0 0;
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.76rem;
        }}

        .providence-health-project-progress,
        .providence-project-card-progress {{
            height: 0.38rem;
            margin-top: 0.7rem;
            background: rgba(254, 246, 243, 0.14);
        }}

        .providence-health-project-progress span,
        .providence-project-card-progress span {{
            background: linear-gradient(
                90deg,
                var(--providence-lavender),
                var(--providence-coral)
            );
        }}

        .providence-health-project-data,
        .providence-project-card-data {{
            min-width: 5.5rem;
        }}

        .providence-health-project-data span,
        .providence-project-card-data span {{
            color: rgba(254, 246, 243, 0.58);
        }}

        .providence-health-project-data strong,
        .providence-project-card-data strong {{
            display: block;
            margin-top: 0.2rem;
            color: var(--providence-blush);
            font-size: 1rem;
            font-weight: 850;
            letter-spacing: -0.05em;
        }}

        .providence-health-project-data small,
        .providence-project-card-data small {{
            display: block;
            margin-top: 0.12rem;
            color: rgba(254, 246, 243, 0.48);
            font-size: 0.64rem;
        }}

        .providence-project-card-message {{
            margin-top: 0.65rem !important;
            color: rgba(254, 246, 243, 0.66) !important;
            font-size: 0.78rem !important;
            line-height: 1.45 !important;
        }}

        .providence-project-count {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 4.4rem;
            padding: 0.85rem 1rem;
            border: 1px solid rgba(254, 246, 243, 0.16);
            border-radius: 1rem;
            background: rgba(254, 246, 243, 0.07);
        }}

        .providence-project-count span,
        .providence-project-count small {{
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.62rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }}

        .providence-project-count strong {{
            color: var(--providence-butter);
            font-size: 1.6rem;
            font-weight: 850;
            letter-spacing: -0.07em;
        }}

        .providence-project-decision {{
            position: relative;
            overflow: hidden;
            margin-top: 1.5rem;
            padding: clamp(1.35rem, 2.4vw, 1.9rem);
            border: 1px solid rgba(254, 246, 243, 0.24);
            border-radius: 1.5rem;
            background:
                radial-gradient(circle at 100% 0%, rgba(255, 138, 122, 0.28), transparent 34%),
                linear-gradient(145deg, rgba(168, 118, 245, 0.38), rgba(44, 19, 56, 0.92) 58%);
            box-shadow: var(--providence-shadow-deep);
        }}

        .providence-project-empty,
        .providence-health-empty {{
            position: relative;
            overflow: hidden;
            margin-top: 1.5rem;
            padding: 1.4rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.35rem;
            background:
                linear-gradient(100deg, rgba(168, 118, 245, 0.24), transparent 56%),
                rgba(254, 246, 243, 0.08);
        }}

        .providence-project-empty h3,
        .providence-health-empty h3 {{
            margin: 0.5rem 0 0;
            color: var(--providence-blush);
            font-size: 1.1rem;
            font-weight: 800;
            letter-spacing: -0.04em;
        }}

        .providence-project-empty p,
        .providence-health-empty p {{
            margin: 0.55rem 0 0;
            color: rgba(254, 246, 243, 0.68);
            font-size: 0.84rem;
            line-height: 1.5;
        }}

        @media (max-width: 860px) {{
            .providence-health-hero,
            .providence-health-decision,
            .providence-project-decision {{
                border-radius: 1.3rem;
            }}

            .providence-health-hero {{
                min-height: auto;
            }}

            .providence-health-hero-grid {{
                grid-template-columns: 1fr;
                margin-top: 1.7rem;
            }}

            .providence-health-orbit {{
                justify-self: end;
                margin-top: -4.5rem;
            }}

            .providence-health-hero-stats {{
                flex-wrap: wrap;
            }}

            .providence-health-hero-stats div {{
                min-width: 30%;
            }}

            .providence-health-project,
            .providence-project-card {{
                align-items: flex-start;
                flex-wrap: wrap;
            }}

            .providence-health-project-main,
            .providence-project-card-main {{
                order: 1;
                width: calc(100% - 3rem);
            }}

            .providence-health-project-data,
            .providence-project-card-data {{
                order: 2;
                min-width: 0;
                margin-left: 3rem;
            }}

            .providence-project-card-message {{
                margin-left: 3rem !important;
            }}
        }}

        @media (max-width: 540px) {{
            .providence-health-hero {{
                padding: 1.15rem;
            }}

            .providence-health-hero strong {{
                font-size: 4rem;
            }}

            .providence-health-orbit {{
                width: 6.3rem;
                height: 6.3rem;
                border-width: 0.68rem;
                margin-top: -3.5rem;
            }}

            .providence-health-hero-stats {{
                gap: 0.75rem;
            }}

            .providence-health-hero-stats strong {{
                font-size: 0.95rem;
            }}

            .providence-health-signal,
            .providence-project-metric {{
                min-height: 9.5rem;
            }}

            .providence-health-project-data,
            .providence-project-card-data {{
                margin-left: 3rem;
            }}
        }}


        /* Phase 5: People, compact density, and sidebar navigation */

        .providence-nav-title {{
            display: none !important;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] {{
            width: 100%;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] > div {{
            width: 100%;
            gap: 0.5rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label {{
            box-sizing: border-box;
            width: 100%;
            min-height: 3.35rem;
            margin: 0;
            padding: 0.82rem 1rem;
            border: 1px solid transparent;
            border-radius: 1rem;
            background: transparent;
            color: rgba(254, 246, 243, 0.78);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label::before,
        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked)::before {{
            display: none !important;
            content: none !important;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
            transform: none;
            background: rgba(254, 246, 243, 0.10);
            color: var(--providence-blush);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {{
            width: 100%;
            background: linear-gradient(
                100deg,
                var(--providence-butter),
                #FFD582
            );
            border-color: rgba(255, 222, 145, 0.92);
            box-shadow: 0 12px 24px rgba(255, 222, 145, 0.16);
            color: var(--providence-plum);
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked),
        [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) * {{
            color: var(--providence-plum) !important;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:focus-within {{
            outline: 3px solid rgba(255, 222, 145, 0.72);
            outline-offset: 3px;
        }}

        .providence-people-stage {{
            display: block;
            margin-top: -0.75rem;
        }}

        .providence-people-kicker,
        .providence-people-hero-label,
        .providence-people-signal span,
        .providence-people-card-data span {{
            display: inline-flex;
            color: var(--providence-butter);
            font-size: 0.66rem;
            font-weight: 850;
            letter-spacing: 0.11em;
            text-transform: uppercase;
        }}

        .providence-people-count {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 4.4rem;
            padding: 0.85rem 1rem;
            border: 1px solid rgba(254, 246, 243, 0.16);
            border-radius: 1rem;
            background: rgba(254, 246, 243, 0.07);
        }}

        .providence-people-count span,
        .providence-people-count small {{
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.62rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }}

        .providence-people-count strong {{
            color: var(--providence-butter);
            font-size: 1.6rem;
            font-weight: 850;
            letter-spacing: -0.07em;
        }}

        .providence-people-hero {{
            position: relative;
            overflow: hidden;
            min-height: 27rem;
            padding: clamp(1.4rem, 3vw, 2.3rem);
            border: 1px solid rgba(44, 19, 56, 0.18);
            border-radius: 1.65rem;
            background:
                radial-gradient(
                    circle at 88% 18%,
                    rgba(168, 118, 245, 0.70),
                    transparent 24%
                ),
                radial-gradient(
                    circle at 68% 90%,
                    rgba(229, 124, 216, 0.48),
                    transparent 25%
                ),
                linear-gradient(135deg, #FFDE91, #FFD88C 54%, #FFCF9B);
            box-shadow: 0 24px 65px rgba(12, 4, 18, 0.23);
            color: var(--providence-plum);
        }}

        .providence-people-hero::after {{
            position: absolute;
            right: -4rem;
            bottom: -6.5rem;
            width: 16rem;
            height: 16rem;
            border: 1px solid rgba(44, 19, 56, 0.17);
            border-radius: 50%;
            content: "";
        }}

        .providence-people-hero-topline,
        .providence-people-pace-labels,
        .providence-people-hero-stats,
        .providence-people-decision-foot {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .providence-people-live {{
            display: inline-flex;
            align-items: center;
            gap: 0.42rem;
            padding: 0.4rem 0.6rem;
            border: 1px solid rgba(44, 19, 56, 0.16);
            border-radius: 999px;
            background: rgba(254, 246, 243, 0.34);
            color: rgba(44, 19, 56, 0.82);
            font-size: 0.68rem;
            font-weight: 750;
        }}

        .providence-people-live i {{
            width: 0.42rem;
            height: 0.42rem;
            border-radius: 50%;
            background: #2C1338;
            box-shadow: 0 0 0 0.22rem rgba(44, 19, 56, 0.12);
        }}

        .providence-people-hero-grid {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 1.35rem;
            margin: clamp(2rem, 4.5vw, 3.5rem) 0 1.3rem;
        }}

        .providence-people-hero strong {{
            display: block;
            margin-top: 0.55rem;
            color: var(--providence-plum);
            font-size: clamp(4rem, 8vw, 6.8rem);
            font-weight: 850;
            letter-spacing: -0.1em;
            line-height: 0.78;
        }}

        .providence-people-hero p {{
            max-width: 25rem;
            margin: 0.9rem 0 0;
            color: rgba(44, 19, 56, 0.75);
            font-size: 0.94rem;
            font-weight: 600;
            line-height: 1.45;
        }}

        .providence-people-orbit {{
            width: clamp(6.5rem, 12vw, 9.5rem);
            height: clamp(6.5rem, 12vw, 9.5rem);
            display: grid;
            place-items: center;
            align-content: center;
            border: 0.9rem solid rgba(44, 19, 56, 0.10);
            border-top-color: var(--providence-plum);
            border-right-color: var(--providence-lavender);
            border-radius: 50%;
            background: rgba(254, 246, 243, 0.26);
            transform: rotate(18deg);
        }}

        .providence-people-orbit span,
        .providence-people-orbit small {{
            transform: rotate(-18deg);
        }}

        .providence-people-orbit span {{
            color: var(--providence-plum);
            font-size: clamp(1.3rem, 2.6vw, 1.9rem);
            font-weight: 850;
            letter-spacing: -0.08em;
        }}

        .providence-people-orbit small {{
            margin-top: 0.18rem;
            color: rgba(44, 19, 56, 0.7);
            font-size: 0.58rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        .providence-people-pace-track,
        .providence-people-card-progress {{
            overflow: hidden;
            height: 0.62rem;
            border-radius: 999px;
            background: rgba(44, 19, 56, 0.15);
        }}

        .providence-people-pace-track span,
        .providence-people-card-progress span {{
            display: block;
            height: 100%;
            border-radius: inherit;
        }}

        .providence-people-pace-track span {{
            background: linear-gradient(
                90deg,
                var(--providence-plum),
                var(--providence-lavender),
                var(--providence-orchid),
                var(--providence-coral)
            );
        }}

        .providence-people-pace-labels {{
            margin-top: 0.6rem;
            color: rgba(44, 19, 56, 0.7);
            font-size: 0.72rem;
            font-weight: 750;
        }}

        .providence-people-hero-stats {{
            position: relative;
            z-index: 1;
            margin-top: 1.4rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(44, 19, 56, 0.16);
        }}

        .providence-people-hero-stats div {{
            flex: 1;
        }}

        .providence-people-hero-stats span {{
            display: block;
            color: rgba(44, 19, 56, 0.66);
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }}

        .providence-people-hero-stats strong {{
            margin-top: 0.2rem;
            font-size: clamp(0.95rem, 1.8vw, 1.2rem);
            letter-spacing: -0.05em;
        }}

        .providence-people-decision {{
            position: relative;
            overflow: hidden;
            min-height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: clamp(1.35rem, 2.4vw, 1.9rem);
            border: 1px solid rgba(254, 246, 243, 0.26);
            border-radius: 1.65rem;
            background:
                radial-gradient(
                    circle at 100% 0%,
                    rgba(255, 138, 122, 0.32),
                    transparent 34%
                ),
                linear-gradient(
                    145deg,
                    rgba(168, 118, 245, 0.42),
                    rgba(44, 19, 56, 0.92) 58%
                );
            box-shadow: var(--providence-shadow-deep);
            color: var(--providence-blush);
        }}

        .providence-people-decision::after {{
            position: absolute;
            right: -2.8rem;
            bottom: -2.8rem;
            width: 9rem;
            height: 9rem;
            border: 1px solid rgba(254, 246, 243, 0.22);
            border-radius: 50%;
            content: "";
        }}

        .providence-people-decision h2 {{
            max-width: 13ch;
            margin: 1.35rem 0 0.8rem;
            color: var(--providence-blush);
            font-size: clamp(1.45rem, 2.8vw, 2rem);
            font-weight: 800;
            letter-spacing: -0.06em;
            line-height: 1.05;
        }}

        .providence-people-decision p {{
            position: relative;
            z-index: 1;
            margin: 0;
            color: rgba(254, 246, 243, 0.78);
            font-size: 0.92rem;
            line-height: 1.6;
        }}

        .providence-people-decision-foot {{
            position: relative;
            z-index: 1;
            margin-top: 1.8rem;
            padding-top: 0.85rem;
            border-top: 1px solid rgba(254, 246, 243, 0.18);
            color: rgba(254, 246, 243, 0.62);
            font-size: 0.7rem;
            font-weight: 750;
        }}

        .providence-people-decision-foot strong {{
            color: var(--providence-butter);
            font-size: 0.82rem;
        }}

        .providence-people-signal {{
            position: relative;
            overflow: hidden;
            min-height: 11rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 1.2rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.3rem;
            box-shadow: 0 16px 38px rgba(12, 4, 18, 0.18);
        }}

        .providence-people-signal::after {{
            position: absolute;
            top: -2rem;
            right: -2rem;
            width: 6.5rem;
            height: 6.5rem;
            border-radius: 50%;
            content: "";
        }}

        .providence-people-signal-violet {{
            background: linear-gradient(
                145deg,
                rgba(168, 118, 245, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-people-signal-violet::after {{
            background: rgba(168, 118, 245, 0.32);
        }}

        .providence-people-signal-pink {{
            background: linear-gradient(
                145deg,
                rgba(229, 124, 216, 0.40),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-people-signal-pink::after {{
            background: rgba(229, 124, 216, 0.32);
        }}

        .providence-people-signal-coral {{
            background: linear-gradient(
                145deg,
                rgba(255, 138, 122, 0.42),
                rgba(254, 246, 243, 0.10)
            );
        }}

        .providence-people-signal-coral::after {{
            background: rgba(255, 138, 122, 0.32);
        }}

        .providence-people-signal strong {{
            position: relative;
            z-index: 1;
            display: block;
            margin-top: 0.7rem;
            color: var(--providence-blush);
            font-size: clamp(2.2rem, 4vw, 3.2rem);
            font-weight: 850;
            letter-spacing: -0.09em;
            line-height: 0.82;
        }}

        .providence-people-signal p {{
            position: relative;
            z-index: 1;
            margin: 0.75rem 0 0;
            color: rgba(254, 246, 243, 0.74);
            font-size: 0.8rem;
            font-weight: 600;
            line-height: 1.4;
        }}

        .providence-people-card {{
            position: relative;
            display: grid;
            grid-template-columns:
                minmax(11rem, 1.6fr)
                minmax(9rem, 1.45fr)
                repeat(3, minmax(4.5rem, 0.62fr));
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.25rem;
            padding: 1rem 1.1rem;
            border: 1px solid rgba(254, 246, 243, 0.14);
            border-radius: 1.15rem;
            background: rgba(254, 246, 243, 0.07);
            box-shadow: inset 0 1px 0 rgba(254, 246, 243, 0.08);
        }}

        .providence-people-card-person {{
            min-width: 0;
            display: flex;
            align-items: center;
            gap: 0.72rem;
        }}

        .providence-people-avatar {{
            width: 2.55rem;
            height: 2.55rem;
            display: grid;
            place-items: center;
            flex: 0 0 auto;
            border: 1px solid rgba(254, 246, 243, 0.22);
            border-radius: 0.82rem;
            background: rgba(168, 118, 245, 0.25);
            color: var(--providence-blush);
            font-size: 0.72rem;
            font-weight: 850;
            letter-spacing: -0.03em;
        }}

        .providence-people-card h3 {{
            overflow: hidden;
            margin: 0;
            color: var(--providence-blush);
            font-size: 0.98rem;
            font-weight: 800;
            letter-spacing: -0.035em;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        .providence-people-card-person p,
        .providence-people-card-capacity p {{
            margin: 0.15rem 0 0;
            color: rgba(254, 246, 243, 0.58);
            font-size: 0.74rem;
            line-height: 1.35;
        }}

        .providence-people-card-progress {{
            height: 0.42rem;
            background: rgba(254, 246, 243, 0.14);
        }}

        .providence-people-progress-healthy {{
            background: var(--providence-lavender);
        }}

        .providence-people-progress-watch {{
            background: var(--providence-butter);
        }}

        .providence-people-progress-risk {{
            background: var(--providence-coral);
        }}

        .providence-people-progress-neutral {{
            background: var(--providence-orchid);
        }}

        .providence-people-card-data span {{
            color: rgba(254, 246, 243, 0.58);
        }}

        .providence-people-card-data strong {{
            display: block;
            margin-top: 0.2rem;
            color: var(--providence-blush);
            font-size: 0.96rem;
            font-weight: 850;
            letter-spacing: -0.05em;
        }}

        .providence-people-card-status {{
            display: flex;
            justify-content: flex-end;
            min-height: 2rem;
            margin: -2.35rem 1.1rem 0.6rem;
            pointer-events: none;
        }}

        .providence-people-empty {{
            position: relative;
            overflow: hidden;
            margin-top: 1.5rem;
            padding: 1.4rem;
            border: 1px solid rgba(254, 246, 243, 0.20);
            border-radius: 1.35rem;
            background:
                linear-gradient(
                    100deg,
                    rgba(168, 118, 245, 0.24),
                    transparent 56%
                ),
                rgba(254, 246, 243, 0.08);
        }}

        .providence-people-empty h3 {{
            margin: 0.5rem 0 0;
            color: var(--providence-blush);
            font-size: 1.1rem;
            font-weight: 800;
            letter-spacing: -0.04em;
        }}

        .providence-people-empty p {{
            margin: 0.55rem 0 0;
            color: rgba(254, 246, 243, 0.68);
            font-size: 0.84rem;
            line-height: 1.5;
        }}

        @media (max-width: 860px) {{
            .providence-people-hero,
            .providence-people-decision {{
                border-radius: 1.3rem;
            }}

            .providence-people-hero {{
                min-height: auto;
            }}

            .providence-people-hero-grid {{
                grid-template-columns: 1fr;
                margin-top: 1.7rem;
            }}

            .providence-people-orbit {{
                justify-self: end;
                margin-top: -4.5rem;
            }}

            .providence-people-hero-stats {{
                flex-wrap: wrap;
            }}

            .providence-people-hero-stats div {{
                min-width: 30%;
            }}

            .providence-people-card {{
                grid-template-columns: minmax(0, 1fr) repeat(3, minmax(4rem, 0.7fr));
            }}

            .providence-people-card-person {{
                grid-column: 1 / -1;
            }}

            .providence-people-card-capacity {{
                grid-column: 1 / -1;
            }}

            .providence-people-card-status {{
                margin-top: -0.15rem;
                margin-right: 1.1rem;
            }}
        }}

        @media (max-width: 540px) {{
            .providence-people-hero {{
                padding: 1.15rem;
            }}

            .providence-people-hero strong {{
                font-size: 4rem;
            }}

            .providence-people-orbit {{
                width: 6.3rem;
                height: 6.3rem;
                border-width: 0.68rem;
                margin-top: -3.5rem;
            }}

            .providence-people-hero-stats {{
                gap: 0.75rem;
            }}

            .providence-people-hero-stats strong {{
                font-size: 0.95rem;
            }}

            .providence-people-signal {{
                min-height: 9.5rem;
            }}

            .providence-people-card {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 0.85rem;
            }}

            .providence-people-card-person,
            .providence-people-card-capacity {{
                grid-column: 1 / -1;
            }}

            .providence-people-card-data {{
                min-width: 0;
            }}
        }}}}


        /* Phase 6: responsive and accessibility audit */

        :where(
            [data-testid="stSidebar"] [data-testid="stRadio"] label,
            .stButton > button,
            .stDownloadButton > button,
            [data-testid="stTabs"] [data-baseweb="tab"]
        ) {{
            min-height: 2.75rem;
        }}

        :where(
            [data-baseweb="select"] > div,
            [data-testid="stTextInput"] input,
            [data-testid="stNumberInput"] input
        ) {{
            min-height: 2.75rem;
        }}

        :where(
            .stButton > button,
            .stDownloadButton > button,
            [data-baseweb="select"] > div,
            [data-testid="stTextInput"] input,
            [data-testid="stNumberInput"] input,
            [data-testid="stTabs"] [data-baseweb="tab"],
            [data-testid="stSidebar"] [data-testid="stRadio"] label
        ):focus-visible {{
            outline: 3px solid var(--providence-butter) !important;
            outline-offset: 3px;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label:focus-within {{
            box-shadow: 0 0 0 3px rgba(255, 222, 145, 0.72);
            outline: none;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label,
        [data-testid="stSidebar"] [data-testid="stRadio"] label * {{
            overflow-wrap: anywhere;
        }}

        .providence-page-header,
        .providence-overview-hero,
        .providence-health-hero,
        .providence-people-hero,
        .providence-overview-decision,
        .providence-health-decision,
        .providence-people-decision,
        .providence-project-decision,
        .providence-overview-metric,
        .providence-health-signal,
        .providence-project-metric,
        .providence-people-signal,
        .providence-overview-project,
        .providence-health-project,
        .providence-project-card,
        .providence-people-card {{
            min-width: 0;
        }}

        .providence-overview-project h3,
        .providence-health-project h3,
        .providence-project-card h3,
        .providence-people-card h3,
        .providence-overview-decision h2,
        .providence-health-decision h2,
        .providence-project-decision h2,
        .providence-people-decision h2 {{
            overflow-wrap: anywhere;
        }}

        .providence-overview-project-data,
        .providence-health-project-data,
        .providence-project-card-data,
        .providence-people-card-data {{
            min-width: 0;
        }}

        .providence-overview-project-data strong,
        .providence-health-project-data strong,
        .providence-project-card-data strong,
        .providence-people-card-data strong {{
            overflow-wrap: anywhere;
        }}

        @media (max-width: 980px) {{
            [data-testid="stMainBlockContainer"],
            .main .block-container {{
                padding-left: clamp(1rem, 3vw, 1.6rem) !important;
                padding-right: clamp(1rem, 3vw, 1.6rem) !important;
            }}

            .providence-overview-hero-stats,
            .providence-health-hero-stats,
            .providence-people-hero-stats {{
                gap: 0.75rem;
            }}

            .providence-overview-project,
            .providence-health-project,
            .providence-project-card {{
                gap: 0.85rem;
            }}

            .providence-project-card-data,
            .providence-health-project-data {{
                min-width: 4.4rem;
            }}
        }}

        @media (max-width: 760px) {{
            .providence-page-header {{
                gap: 1rem;
                padding: 1.2rem;
            }}

            .providence-page-header h1 {{
                overflow-wrap: anywhere;
            }}

            .providence-page-subtitle {{
                max-width: none;
            }}

            .providence-date-context {{
                max-width: 100%;
                white-space: normal;
            }}

            .providence-overview-hero-stats,
            .providence-health-hero-stats,
            .providence-people-hero-stats {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }}

            .providence-overview-project,
            .providence-health-project,
            .providence-project-card {{
                display: grid;
                grid-template-columns: minmax(0, 1fr) repeat(2, minmax(4rem, auto));
                align-items: start;
            }}

            .providence-overview-project-index {{
                display: none;
            }}

            .providence-overview-project-main,
            .providence-health-project-main,
            .providence-project-card-main {{
                grid-column: 1 / -1;
                width: auto;
            }}

            .providence-overview-project-data,
            .providence-health-project-data,
            .providence-project-card-data {{
                margin-left: 0;
            }}

            .providence-project-card-message {{
                margin-left: 0 !important;
            }}

            .providence-overview-project + div [class*="providence-status"],
            .providence-health-project + div [class*="providence-status"],
            .providence-project-card + div [class*="providence-status"] {{
                float: none;
                margin: 0 0 0.8rem;
            }}
        }}

        @media (max-width: 560px) {{
            [data-testid="stMainBlockContainer"],
            .main .block-container {{
                padding-top: 4.7rem !important;
                padding-bottom: 2.5rem !important;
            }}

            .providence-page-header {{
                margin-bottom: 1.75rem;
            }}

            .providence-eyebrow {{
                font-size: 0.64rem;
            }}

            .providence-date-context {{
                width: 100%;
                justify-content: center;
            }}

            .providence-overview-hero-topline,
            .providence-health-hero-topline,
            .providence-people-hero-topline,
            .providence-overview-pace-labels,
            .providence-health-pace-labels,
            .providence-people-pace-labels {{
                align-items: flex-start;
                flex-direction: column;
                gap: 0.55rem;
            }}

            .providence-overview-live,
            .providence-health-live,
            .providence-people-live {{
                max-width: 100%;
                white-space: normal;
            }}

            .providence-overview-hero-stats,
            .providence-health-hero-stats,
            .providence-people-hero-stats {{
                grid-template-columns: 1fr;
            }}

            .providence-overview-project,
            .providence-health-project,
            .providence-project-card {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
                padding: 1rem;
            }}

            .providence-overview-project-main,
            .providence-health-project-main,
            .providence-project-card-main {{
                grid-column: 1 / -1;
            }}

            .providence-overview-project-data,
            .providence-health-project-data,
            .providence-project-card-data {{
                min-width: 0;
            }}

            .providence-people-card-status {{
                justify-content: flex-start;
                margin-left: 1rem;
            }}

            [data-testid="stSidebar"] [data-testid="stRadio"] label {{
                min-height: 3rem;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            [data-testid="stSidebar"] [data-testid="stRadio"] label,
            .providence-overview-orbit,
            .providence-health-orbit,
            .providence-people-orbit,
            .stButton > button,
            .stDownloadButton > button {{
                transform: none !important;
                transition: none !important;
            }}
        }}

        @media (forced-colors: active) {{
            :where(
                .stButton > button,
                .stDownloadButton > button,
                [data-baseweb="select"] > div,
                [data-testid="stSidebar"] [data-testid="stRadio"] label
            ):focus-visible {{
                outline: 3px solid Highlight !important;
            }}

            [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {{
                border: 2px solid Highlight;
            }}
        }}


        /* Phase 7: quality and presentation refinement */

        :root {{
            --providence-card-radius: 1.3rem;
            --providence-card-border: rgba(254, 246, 243, 0.18);
            --providence-content-gap: clamp(1rem, 2vw, 1.5rem);
        }}

        [data-testid="stMainBlockContainer"],
        .main .block-container {{
            max-width: 92rem;
        }}

        [data-testid="stSidebar"] > div:first-child {{
            padding-right: 0.85rem;
            padding-left: 0.85rem;
        }}

        .providence-brand {{
            margin-bottom: 1.45rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] > div {{
            gap: 0.55rem;
        }}

        [data-testid="stSidebar"] [data-testid="stRadio"] label {{
            justify-content: flex-start;
            min-height: 3.2rem;
            padding-right: 1.05rem;
            padding-left: 1.05rem;
        }}

        .providence-page-header {{
            margin-bottom: clamp(1.85rem, 3vw, 2.75rem);
        }}

        .providence-page-header h1 {{
            text-wrap: balance;
        }}

        .providence-page-subtitle {{
            text-wrap: pretty;
        }}

        .providence-section-heading {{
            margin-top: clamp(2.25rem, 4vw, 3.5rem);
            margin-bottom: 1rem;
        }}

        .providence-section-detail {{
            line-height: 1.25;
        }}

        .providence-status {{
            justify-content: center;
            min-height: 2rem;
            padding: 0.36rem 0.7rem;
            line-height: 1;
        }}

        .providence-status::before {{
            flex: 0 0 auto;
        }}

        .providence-overview-hero,
        .providence-health-hero,
        .providence-people-hero {{
            border-radius: var(--providence-card-radius);
        }}

        .providence-overview-decision,
        .providence-health-decision,
        .providence-people-decision,
        .providence-project-decision {{
            border-radius: var(--providence-card-radius);
        }}

        .providence-overview-metric,
        .providence-health-signal,
        .providence-project-metric,
        .providence-people-signal {{
            min-height: 12rem;
            border-radius: var(--providence-card-radius);
        }}

        .providence-overview-project,
        .providence-health-project,
        .providence-project-card,
        .providence-people-card {{
            border-color: var(--providence-card-border);
            border-radius: 1.15rem;
        }}

        .providence-overview-project:hover,
        .providence-health-project:hover,
        .providence-project-card:hover,
        .providence-people-card:hover {{
            border-color: rgba(255, 222, 145, 0.38);
            background: rgba(254, 246, 243, 0.09);
        }}

        .providence-overview-project h3,
        .providence-health-project h3,
        .providence-project-card h3,
        .providence-people-card h3 {{
            line-height: 1.15;
        }}

        .providence-overview-project p,
        .providence-health-project p,
        .providence-project-card p,
        .providence-people-card p {{
            line-height: 1.4;
        }}

        .providence-overview-project-data,
        .providence-health-project-data,
        .providence-project-card-data,
        .providence-people-card-data {{
            align-self: center;
        }}

        .providence-overview-project-data strong,
        .providence-health-project-data strong,
        .providence-project-card-data strong,
        .providence-people-card-data strong {{
            font-variant-numeric: tabular-nums;
        }}

        .providence-overview-hero-stats strong,
        .providence-health-hero-stats strong,
        .providence-people-hero-stats strong,
        .providence-overview-metric strong,
        .providence-health-signal strong,
        .providence-project-metric strong,
        .providence-people-signal strong {{
            font-variant-numeric: tabular-nums;
        }}

        .providence-overview-project-progress,
        .providence-health-project-progress,
        .providence-project-card-progress,
        .providence-people-card-progress {{
            margin-bottom: 0.1rem;
        }}

        .providence-overview-empty,
        .providence-health-empty,
        .providence-project-empty,
        .providence-people-empty,
        .providence-overview-export {{
            border-radius: var(--providence-card-radius);
        }}

        .providence-overview-empty,
        .providence-health-empty,
        .providence-project-empty,
        .providence-people-empty {{
            border-color: var(--providence-card-border);
        }}

        @media (hover: hover) and (pointer: fine) {{
            .providence-overview-project,
            .providence-health-project,
            .providence-project-card,
            .providence-people-card {{
                transition:
                    border-color 160ms ease,
                    background-color 160ms ease;
            }}
        }}

        @media (max-width: 860px) {{
            [data-testid="stSidebar"] > div:first-child {{
                padding-right: 0.75rem;
                padding-left: 0.75rem;
            }}

            .providence-overview-metric,
            .providence-health-signal,
            .providence-project-metric,
            .providence-people-signal {{
                min-height: 10.5rem;
            }}
        }}

        @media (max-width: 560px) {{
            .providence-page-header {{
                padding: 1.1rem;
            }}

            .providence-section-heading {{
                margin-top: 2rem;
            }}

            .providence-section-detail {{
                width: 100%;
                padding: 0;
                border: 0;
                border-radius: 0;
                background: transparent;
            }}

            .providence-overview-metric,
            .providence-health-signal,
            .providence-project-metric,
            .providence-people-signal {{
                min-height: 9.25rem;
            }}

            .providence-status {{
                min-height: 2.2rem;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            .providence-overview-project,
            .providence-health-project,
            .providence-project-card,
            .providence-people-card {{
                transition: none !important;
            }}
        }}




        /* Export action spacing refinement */

        .providence-overview-export {{
            margin: 2.25rem 0 0.85rem;
            padding: 1.4rem 1.5rem;
        }}

        .providence-overview-export + div {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            width: 100%;
            margin: 0;
        }}

        .providence-overview-export + div > div {{
            min-width: 0;
            width: 100%;
        }}

        .providence-overview-export + div .stDownloadButton {{
            width: 100%;
            margin: 0;
        }}

        .providence-overview-export + div .stDownloadButton > button {{
            width: 100%;
            min-height: 2.9rem;
            margin: 0;
            white-space: nowrap;
        }}

        @media (max-width: 760px) {{
            .providence-overview-export {{
                margin-top: 1.75rem;
                padding: 1.2rem;
            }}

            .providence-overview-export + div {{
                grid-template-columns: 1fr;
                gap: 0.65rem;
            }}
        }}




        /* Three-up dashboard card boundaries */

        .providence-overview-metric,
        .providence-health-signal,
        .providence-people-signal {{
            box-sizing: border-box !important;
            display: block !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            overflow: hidden !important;
        }}


        /* Equal-height hero and decision cards. */
        .providence-equal-card-row {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            align-items: stretch;
            gap: clamp(1rem, 2vw, 1.5rem);
            margin-bottom: clamp(1rem, 2vw, 1.5rem);
        }}

        .providence-equal-card-row > .providence-overview-hero,
        .providence-equal-card-row > .providence-overview-decision,
        .providence-equal-card-row > .providence-health-hero,
        .providence-equal-card-row > .providence-health-decision,
        .providence-equal-card-row > .providence-people-hero,
        .providence-equal-card-row > .providence-people-decision {{
            width: 100%;
            min-width: 0;
            height: 100%;
        }}

        @media (max-width: 860px) {{
            .providence-equal-card-row {{
                grid-template-columns: minmax(0, 1fr);
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )
