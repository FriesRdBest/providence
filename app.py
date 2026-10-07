import streamlit as st
from src.domain.models import Workspace, Project, Log
from src.ui.project_view import render_project_view
from src.ui.people_view import render_people_view
from src.ui.health_view import render_health_view
from datetime import date, timedelta


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
            budget_hours=40.0,
            deadline=today + timedelta(days=30),
            logs=[
                Log(alice, 2.0, today - timedelta(days=1)),
                Log(bob, 1.5, today - timedelta(days=2)),
                Log(charlie, 3.0, today - timedelta(days=3)),
            ],
        ),
        Project(
            name="Beta",
            budget_hours=60.0,
            deadline=today + timedelta(days=45),
            logs=[
                Log(alice, 4.0, today - timedelta(days=1)),
                Log(bob, 2.5, today - timedelta(days=2)),
            ],
        ),
        Project(
            name="Gamma",
            budget_hours=80.0,
            deadline=today + timedelta(days=60),
            logs=[
                Log(alice, 1.0, today - timedelta(days=1)),
                Log(charlie, 2.0, today - timedelta(days=2)),
            ],
        ),
    ]

    return Workspace(projects=projects, today=today)


def main() -> None:
    workspace = load_workspace()

    st.title("Providence")

    tab_project, tab_people, tab_health = st.tabs(["Project", "People", "Health"])

    with tab_project:
        render_project_view(workspace)

    with tab_people:
        render_people_view(workspace)

    with tab_health:
        render_health_view(workspace)


if __name__ == "__main__":
    main()
