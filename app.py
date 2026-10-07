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

    projects = [
        Project(
            name="Alpha",
            client="Client A",
            budget_hours=Decimal("40.0"),
            delivery_date=today + timedelta(days=30),
        ),
        Project(
            name="Beta",
            client="Client B",
            budget_hours=Decimal("60.0"),
            delivery_date=today + timedelta(days=45),
        ),
        Project(
            name="Gamma",
            client="Client C",
            budget_hours=Decimal("80.0"),
            delivery_date=today + timedelta(days=60),
        ),
    ]

    return Workspace(name="Providence Workspace", projects=projects, today=today)


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
