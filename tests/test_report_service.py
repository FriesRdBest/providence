from datetime import date
from decimal import Decimal

from src.domain.models import Person, Project, Workspace
from src.services.report_service import build_detailed_pdf, build_executive_pdf


def _workspace() -> Workspace:
    return Workspace(
        name="Test workspace",
        projects=[
            Project(
                name="Alpha",
                client="Northstar",
                budget_hours=Decimal("40"),
                logged_hours=Decimal("35"),
                delivery_date=date(2026, 10, 10),
            ),
            Project(
                name="Beta",
                client="Harbor",
                budget_hours=Decimal("60"),
                logged_hours=Decimal("12"),
                delivery_date=date(2026, 11, 20),
            ),
        ],
        people=[
            Person(
                name="Alice Morgan",
                role="Product design",
                daily_capacity_hours=Decimal("8"),
                logged_hours_today=Decimal("5"),
            ),
            Person(
                name="Ben Carter",
                role="Engineering",
                daily_capacity_hours=Decimal("8"),
                logged_hours_today=Decimal("9"),
            ),
        ],
    )


def test_executive_pdf_is_a_nonempty_pdf() -> None:
    pdf = build_executive_pdf(_workspace(), today=date(2026, 10, 7))

    assert pdf.startswith(b"%PDF")
    assert len(pdf) > 1_000


def test_detailed_pdf_is_a_nonempty_pdf() -> None:
    pdf = build_detailed_pdf(_workspace(), today=date(2026, 10, 7))

    assert pdf.startswith(b"%PDF")
    assert len(pdf) > 1_000
