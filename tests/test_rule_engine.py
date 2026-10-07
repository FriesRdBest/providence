from datetime import date
from decimal import Decimal

from src.repositories.workspace_repository import JsonWorkspaceRepository
from src.services.rule_engine import RuleEngine


def test_workspace_health_is_deterministic() -> None:
    workspace = JsonWorkspaceRepository("data/workspace.json").read()
    health = RuleEngine().assess_workspace(workspace, today=date(2026, 10, 7))

    assert health.utilisation_percentage == Decimal("62.5")
    assert health.projects_at_risk == 1
    assert health.projects_on_watch == 1
