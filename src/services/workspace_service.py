from __future__ import annotations

from pathlib import Path

from src.domain.models import Workspace
from src.repositories.workspace_repository import JsonWorkspaceRepository


class WorkspaceService:
    def __init__(self) -> None:
        ledger_path = Path(__file__).resolve().parents[2] / "data" / "workspace.json"
        self.repository = JsonWorkspaceRepository(ledger_path)

    def load_workspace(self) -> Workspace:
        return self.repository.read()

    @staticmethod
    def get_ledger_path() -> Path:
        return Path(__file__).resolve().parents[2] / "data" / "workspace.json"
