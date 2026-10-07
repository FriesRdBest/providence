from __future__ import annotations

from datetime import date
from decimal import Decimal
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from src.domain.models import PersonStatus, ProjectStatus, Workspace
from src.services.rule_engine import RuleEngine

PLUM = colors.HexColor("#2C1338")
BLUSH = colors.HexColor("#FEF6F3")
BUTTER = colors.HexColor("#FFDE91")
LAVENDER = colors.HexColor("#A876F5")
ORCHID = colors.HexColor("#E57CD8")
CORAL = colors.HexColor("#FF8A7A")
MUTED = colors.HexColor("#6D6274")
LINE = colors.HexColor("#E7DCE8")
SOFT_PLUM = colors.HexColor("#F6EFF7")
SOFT_BUTTER = colors.HexColor("#FFF4D5")
SOFT_CORAL = colors.HexColor("#FFF0ED")
SOFT_LAVENDER = colors.HexColor("#F0E9FF")


def _format_hours(value: Decimal) -> str:
    return f"{value:,.1f} h"


def _status_label(status: ProjectStatus) -> str:
    return {
        ProjectStatus.HEALTHY: "Healthy",
        ProjectStatus.WATCH: "Watch",
        ProjectStatus.AT_RISK: "At risk",
    }[status]


def _person_status_label(status: PersonStatus) -> str:
    return {
        PersonStatus.AVAILABLE: "Available",
        PersonStatus.BUSY: "Busy",
        PersonStatus.OVERBOOKED: "Overbooked",
        PersonStatus.MISSING_TIME: "Time missing",
    }[status]


def _status_color(status: ProjectStatus) -> colors.Color:
    return {
        ProjectStatus.HEALTHY: LAVENDER,
        ProjectStatus.WATCH: BUTTER,
        ProjectStatus.AT_RISK: CORAL,
    }[status]


def _person_status_color(status: PersonStatus) -> colors.Color:
    return {
        PersonStatus.AVAILABLE: LAVENDER,
        PersonStatus.BUSY: BUTTER,
        PersonStatus.OVERBOOKED: CORAL,
        PersonStatus.MISSING_TIME: ORCHID,
    }[status]


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "ProvidenceTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=PLUM,
            spaceAfter=4,
        ),
        "subtitle": ParagraphStyle(
            "ProvidenceSubtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=13,
            textColor=MUTED,
            spaceAfter=16,
        ),
        "section": ParagraphStyle(
            "ProvidenceSection",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=PLUM,
            spaceBefore=12,
            spaceAfter=7,
        ),
        "body": ParagraphStyle(
            "ProvidenceBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=PLUM,
        ),
        "small": ParagraphStyle(
            "ProvidenceSmall",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.5,
            leading=10,
            textColor=MUTED,
        ),
        "metric_label": ParagraphStyle(
            "ProvidenceMetricLabel",
            parent=base["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            fontSize=7,
            leading=9,
            textColor=MUTED,
            spaceAfter=3,
        ),
        "metric_value": ParagraphStyle(
            "ProvidenceMetricValue",
            parent=base["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=21,
            textColor=PLUM,
            spaceAfter=2,
        ),
        "metric_note": ParagraphStyle(
            "ProvidenceMetricNote",
            parent=base["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica",
            fontSize=7,
            leading=9,
            textColor=MUTED,
        ),
        "table_header": ParagraphStyle(
            "ProvidenceTableHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7,
            leading=9,
            textColor=BLUSH,
        ),
        "table_body": ParagraphStyle(
            "ProvidenceTableBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.5,
            leading=10,
            textColor=PLUM,
        ),
    }


def _footer(canvas: object, document: object) -> None:
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(document.leftMargin, 0.52 * inch, A4[0] - document.rightMargin, 0.52 * inch)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(document.leftMargin, 0.34 * inch, "Providence · Time intelligence")
    canvas.drawRightString(
        A4[0] - document.rightMargin,
        0.34 * inch,
        f"Page {document.page}",
    )
    canvas.restoreState()


def _document(title: str) -> tuple[BytesIO, SimpleDocTemplate, dict[str, ParagraphStyle]]:
    buffer = BytesIO()
    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        title=title,
        author="Providence",
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.72 * inch,
    )
    return buffer, document, _styles()


def _header(
    styles: dict[str, ParagraphStyle],
    title: str,
    subtitle: str,
) -> list[object]:
    return [
        Paragraph(title, styles["title"]),
        Paragraph(subtitle, styles["subtitle"]),
        HRFlowable(width="100%", thickness=1, color=LINE, spaceAfter=9),
    ]


def _metric_card(
    styles: dict[str, ParagraphStyle],
    label: str,
    value: str,
    note: str,
    background: colors.Color,
) -> Table:
    content = [
        [
            Paragraph(label.upper(), styles["metric_label"]),
            Paragraph(value, styles["metric_value"]),
            Paragraph(note, styles["metric_note"]),
        ]
    ]
    table = Table(content, colWidths=[1.64 * inch], rowHeights=[0.95 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def _project_table(
    workspace: Workspace,
    today: date,
    styles: dict[str, ParagraphStyle],
) -> Table:
    header = [
        Paragraph("PROJECT", styles["table_header"]),
        Paragraph("CLIENT", styles["table_header"]),
        Paragraph("BUDGET USED", styles["table_header"]),
        Paragraph("REMAINING", styles["table_header"]),
        Paragraph("DELIVERY", styles["table_header"]),
        Paragraph("STATUS", styles["table_header"]),
    ]
    rows: list[list[Paragraph]] = [header]

    status_order = {
        ProjectStatus.AT_RISK: 0,
        ProjectStatus.WATCH: 1,
        ProjectStatus.HEALTHY: 2,
    }
    projects = sorted(
        workspace.projects,
        key=lambda project: (
            status_order[project.status(today)],
            -float(project.budget_burn_percentage),
        ),
    )

    for project in projects:
        status = project.status(today)
        status_text = _status_label(status)
        status_style = ParagraphStyle(
            f"ProjectStatus-{status.value}",
            parent=styles["table_body"],
            fontName="Helvetica-Bold",
            textColor=_status_color(status),
        )
        rows.append(
            [
                Paragraph(project.name, styles["table_body"]),
                Paragraph(project.client, styles["table_body"]),
                Paragraph(f"{project.budget_burn_percentage}%", styles["table_body"]),
                Paragraph(_format_hours(project.budget_remaining_hours), styles["table_body"]),
                Paragraph(f"{project.days_until_delivery(today)} days", styles["table_body"]),
                Paragraph(status_text, status_style),
            ]
        )

    table = Table(
        rows,
        colWidths=[1.1 * inch, 1.05 * inch, 0.85 * inch, 0.85 * inch, 0.75 * inch, 0.85 * inch],
        repeatRows=1,
        hAlign="LEFT",
    )
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), PLUM),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    for row_index in range(1, len(rows)):
        style.append(
            (
                "BACKGROUND",
                (0, row_index),
                (-1, row_index),
                SOFT_PLUM if row_index % 2 else colors.white,
            )
        )
    table.setStyle(TableStyle(style))
    return table


def _people_table(workspace: Workspace, styles: dict[str, ParagraphStyle]) -> Table:
    header = [
        Paragraph("PERSON", styles["table_header"]),
        Paragraph("ROLE", styles["table_header"]),
        Paragraph("LOGGED", styles["table_header"]),
        Paragraph("CAPACITY", styles["table_header"]),
        Paragraph("REMAINING", styles["table_header"]),
        Paragraph("STATUS", styles["table_header"]),
    ]
    rows: list[list[Paragraph]] = [header]

    status_order = {
        PersonStatus.OVERBOOKED: 0,
        PersonStatus.MISSING_TIME: 1,
        PersonStatus.BUSY: 2,
        PersonStatus.AVAILABLE: 3,
    }
    people = sorted(
        workspace.people,
        key=lambda person: (status_order[person.status], person.name.lower()),
    )

    for person in people:
        status = person.status
        status_style = ParagraphStyle(
            f"PersonStatus-{status.value}",
            parent=styles["table_body"],
            fontName="Helvetica-Bold",
            textColor=_person_status_color(status),
        )
        rows.append(
            [
                Paragraph(person.name, styles["table_body"]),
                Paragraph(person.role, styles["table_body"]),
                Paragraph(_format_hours(person.logged_hours_today), styles["table_body"]),
                Paragraph(_format_hours(person.daily_capacity_hours), styles["table_body"]),
                Paragraph(_format_hours(person.capacity_remaining), styles["table_body"]),
                Paragraph(_person_status_label(status), status_style),
            ]
        )

    table = Table(
        rows,
        colWidths=[1.15 * inch, 1.35 * inch, 0.75 * inch, 0.8 * inch, 0.8 * inch, 1.0 * inch],
        repeatRows=1,
        hAlign="LEFT",
    )
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), PLUM),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    for row_index in range(1, len(rows)):
        style.append(
            (
                "BACKGROUND",
                (0, row_index),
                (-1, row_index),
                SOFT_PLUM if row_index % 2 else colors.white,
            )
        )
    table.setStyle(TableStyle(style))
    return table


def _decision_copy(workspace: Workspace, today: date) -> tuple[str, str]:
    health = RuleEngine().assess_workspace(workspace, today=today)
    if health.projects_at_risk:
        return (
            "Immediate attention required",
            f"{health.projects_at_risk} project(s) are at risk. Review budget pace "
            "and allocation before assigning further work.",
        )
    if health.projects_on_watch:
        return (
            "Delivery pace needs review",
            f"{health.projects_on_watch} project(s) are on watch. Protect remaining "
            "budget and delivery time in the next allocation decision.",
        )
    return (
        "Delivery is within current boundaries",
        f"{_format_hours(health.remaining_budget_hours)} remains across active project budgets.",
    )


def build_executive_pdf(workspace: Workspace, today: date | None = None) -> bytes:
    report_date = today or date.today()
    health = RuleEngine().assess_workspace(workspace, today=report_date)
    buffer, document, styles = _document("Providence executive workspace summary")

    attention_count = health.projects_at_risk + health.projects_on_watch
    insight_title, insight_body = _decision_copy(workspace, report_date)

    metrics = Table(
        [
            [
                _metric_card(
                    styles,
                    "Budget used",
                    f"{workspace.overall_burn_percentage}%",
                    "Across active projects",
                    SOFT_BUTTER,
                ),
                _metric_card(
                    styles,
                    "Budget remaining",
                    _format_hours(health.remaining_budget_hours),
                    "Available project budget",
                    SOFT_LAVENDER,
                ),
                _metric_card(
                    styles,
                    "Team utilisation",
                    f"{health.utilisation_percentage}%",
                    "Current capacity use",
                    SOFT_PLUM,
                ),
                _metric_card(
                    styles,
                    "Attention needed",
                    str(attention_count),
                    "At risk or on watch",
                    SOFT_CORAL,
                ),
            ]
        ],
        colWidths=[1.64 * inch] * 4,
        hAlign="LEFT",
    )
    metrics.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))

    story: list[object] = _header(
        styles,
        "Providence workspace summary",
        f"Executive delivery snapshot · Generated {report_date.strftime('%d %B %Y')}",
    )
    story.extend(
        [
            metrics,
            Spacer(1, 14),
            Paragraph("Decision support", styles["section"]),
            KeepTogether(
                [
                    Paragraph(
                        insight_title,
                        ParagraphStyle(
                            "InsightTitle",
                            parent=styles["body"],
                            fontName="Helvetica-Bold",
                            fontSize=10,
                            leading=13,
                        ),
                    ),
                    Spacer(1, 3),
                    Paragraph(insight_body, styles["body"]),
                ]
            ),
            Spacer(1, 10),
            Paragraph("Portfolio at a glance", styles["section"]),
            _project_table(workspace, report_date, styles),
            Spacer(1, 10),
            Paragraph(
                f"{len(workspace.people)} people tracked · "
                f"{health.utilisation_percentage}% team utilisation · "
                f"{health.projects_at_risk} at risk · "
                f"{health.projects_on_watch} on watch",
                styles["small"],
            ),
        ]
    )

    document.build(story, onFirstPage=_footer, onLaterPages=_footer)
    return buffer.getvalue()


def build_detailed_pdf(workspace: Workspace, today: date | None = None) -> bytes:
    report_date = today or date.today()
    health = RuleEngine().assess_workspace(workspace, today=report_date)
    buffer, document, styles = _document("Providence detailed workspace report")

    story: list[object] = _header(
        styles,
        "Providence detailed workspace report",
        f"Portfolio, budget, delivery and capacity report · "
        f"Generated {report_date.strftime('%d %B %Y')}",
    )

    summary_rows = [
        [
            Paragraph("Projects tracked", styles["table_body"]),
            Paragraph(str(len(workspace.projects)), styles["table_body"]),
        ],
        [
            Paragraph("People tracked", styles["table_body"]),
            Paragraph(str(len(workspace.people)), styles["table_body"]),
        ],
        [
            Paragraph("Overall budget used", styles["table_body"]),
            Paragraph(f"{workspace.overall_burn_percentage}%", styles["table_body"]),
        ],
        [
            Paragraph("Remaining project budget", styles["table_body"]),
            Paragraph(_format_hours(health.remaining_budget_hours), styles["table_body"]),
        ],
        [
            Paragraph("Team utilisation", styles["table_body"]),
            Paragraph(f"{health.utilisation_percentage}%", styles["table_body"]),
        ],
        [
            Paragraph("Projects at risk", styles["table_body"]),
            Paragraph(str(health.projects_at_risk), styles["table_body"]),
        ],
        [
            Paragraph("Projects on watch", styles["table_body"]),
            Paragraph(str(health.projects_on_watch), styles["table_body"]),
        ],
    ]
    summary_table = Table(summary_rows, colWidths=[2.45 * inch, 1.35 * inch], hAlign="LEFT")
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SOFT_PLUM),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    insight_title, insight_body = _decision_copy(workspace, report_date)
    story.extend(
        [
            Paragraph("Workspace summary", styles["section"]),
            summary_table,
            Spacer(1, 10),
            Paragraph("Decision support", styles["section"]),
            Paragraph(
                f"<b>{insight_title}</b><br/>{insight_body}",
                styles["body"],
            ),
            Paragraph("Project portfolio", styles["section"]),
            _project_table(workspace, report_date, styles),
            Paragraph("People and capacity", styles["section"]),
            _people_table(workspace, styles),
            Spacer(1, 8),
            Paragraph(
                "This report is a point-in-time view of the Providence workspace. "
                "Use the JSON export for structured data interchange.",
                styles["small"],
            ),
        ]
    )

    document.build(story, onFirstPage=_footer, onLaterPages=_footer)
    return buffer.getvalue()
