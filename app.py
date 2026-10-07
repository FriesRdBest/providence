import streamlit as st
from src.domain.models import Workspace, Project, Log
from src.ui.land_view import render_land_view
from src.ui.sea_view import render_sea_view
from src.ui.air_view import render_air_view
from src.ui.overview_view import render_overview_view
from datetime import date, timedelta
from decimal import Decimal


st.set_page_config(page_title="Providence", layout="wide")


@st.cache_data
def load_workspace() -> Workspace:
    today = date.today()

    alice = "Alice"
    bob = "Bob"
    charlie = "Charlie"

    projects = [
        Project(
            name="Alpha",
            budget_hours=Decimal("40.0"),
            deadline=today + timedelta(days=30),
            logs=[
                Log(alice, Decimal("2.0"), today - timedelta(days=1)),
                Log(bob, Decimal("1.5"), today - timedelta(days=2)),
                Log(charlie, Decimal("3.0"), today - timedelta(days=3)),
            ],
        ),
        Project(
            name="Beta",
            budget_hours=Decimal("60.0"),
            deadline=today + timedelta(days=45),
            logs=[
                Log(alice, Decimal("4.0"), today - timedelta(days=1)),
                Log(bob, Decimal("2.5"), today - timedelta(days=2)),
            ],
        ),
        Project(
            name="Gamma",
            budget_hours=Decimal("80.0"),
            deadline=today + timedelta(days=60),
            logs=[
                Log(alice, Decimal("1.0"), today - timedelta(days=1)),
                Log(charlie, Decimal("2.0"), today - timedelta(days=2)),
            ],
        ),
    ]

    return Workspace(projects=projects, today=today)


def main() -> None:
    workspace = load_workspace()

    st.title("Providence")

    tab_project, tab_people, tab_health = st.tabs(["Project", "People", "Health"])

    with tab_project:
        render_sea_view(workspace)

    with tab_people:
        render_air_view(workspace)

    with tab_health:
        render_land_view(workspace)


if __name__ == "__main__":
    main()
