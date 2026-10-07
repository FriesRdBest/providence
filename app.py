from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal

import streamlit as st

from src.domain.models import Person, Project, Workspace
from src.ui.air_view import render_air_view
from src.ui.components import render_brand
from src.ui.land_view import render_land_view
from src.ui.overview_view import render_overview_view
from src.ui.sea_view import render_sea_view
from src.ui.styles import apply_global_styles

st.set_page_config(
    page_title="Providence",
    page_icon="P",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_workspace() -> Workspace:
    today = date.today()

    projects = [
        Project(
            name="Alpha",
            client="Northstar",
            budget_hours=Decimal("40.0"),
            logged_hours=Decimal("6.5"),
            delivery_date=today + timedelta(days=30),
        ),
        Project(
            name="Beta",
            client="Harbor",
            budget_hours=Decimal("60.0"),
            logged_hours=Decimal("9.0"),
            delivery_date=today + timedelta(days=45),
        ),
        Project(
            name="Gamma",
            client="Summit",
            budget_hours=Decimal("80.0"),
            logged_hours=Decimal("3.0"),
            delivery_date=today + timedelta(days=60),
        ),
    ]

    people = [
        Person(
            name="Alice Morgan",
            role="Product design",
            daily_capacity_hours=Decimal("8.0"),
            logged_hours_today=Decimal("4.5"),
        ),
        Person(
            name="Ben Carter",
            role="Engineering",
            daily_capacity_hours=Decimal("8.0"),
            logged_hours_today=Decimal("6.5"),
        ),
        Person(
            name="Charlie Reed",
            role="Client delivery",
            daily_capacity_hours=Decimal("8.0"),
            logged_hours_today=Decimal("9.5"),
        ),
        Person(
            name="Dana Brooks",
            role="Operations",
            daily_capacity_hours=Decimal("8.0"),
            logged_hours_today=Decimal("0.0"),
        ),
    ]

    return Workspace(
        name="Providence workspace",
        projects=projects,
        people=people,
        today=today,
    )


def render_navigation() -> str:
    with st.sidebar:
        render_brand()
        st.markdown('<div class="providence-nav-title">Workspace</div>', unsafe_allow_html=True)
        page = st.radio(
            label="Navigation",
            options=("Overview", "Health", "Project", "People"),
            label_visibility="collapsed",
            key="providence_navigation",
        )
        st.markdown(
            """
            <div class="providence-nav-note">
                Clear view of delivery pace, budget boundaries, and team capacity.
            </div>
            """,
            unsafe_allow_html=True,
        )
    return page


def main() -> None:
    apply_global_styles()
    workspace = load_workspace()
    page = render_navigation()

    if page == "Overview":
        render_overview_view(workspace)
    elif page == "Health":
        render_land_view(workspace)
    elif page == "Project":
        render_sea_view(workspace)
    else:
        render_air_view(workspace)


if __name__ == "__main__":
    main()
