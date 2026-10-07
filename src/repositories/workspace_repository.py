from __future__ import annotations

import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.domain.models import Workspace


class WorkspaceRepository(ABC):
    @abstractmethod
    def read(self) -> Workspace:
        raise NotImplementedError

    @abstractmethod
    def write(self, workspace: Workspace) -> None:
        raise NotImplementedError


class JsonWorkspaceRepository(WorkspaceRepository):
    def __init__(self, ledger_path: str | Path) -> None:
        self.ledger_path = Path(ledger_path)

    def read(self) -> Workspace:
        content = json.loads(self.ledger_path.read_text(encoding="utf-8"))
        return Workspace.model_validate(content)

    def write(self, workspace: Workspace) -> None:
        validated_workspace = Workspace.model_validate(workspace)
        serialised = validated_workspace.model_dump(mode="json")
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        self.ledger_path.write_text(
            json.dumps(serialised, indent=2, sort_keys=True),
            encoding="utf-8",
        )
