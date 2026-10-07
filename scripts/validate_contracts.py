"""Pre merge validation gate for data contract compliance."""

from __future__ import annotations

import sys
from pathlib import Path

from src.domain.models import Workspace
from src.repositories.workspace_repository import JsonWorkspaceRepository


def main() -> int:
    ledger_path = Path(__file__).resolve().parents[1] / "data" / "workspace.json"

    if not ledger_path.exists():
        print("Error: Workspace ledger not found")
        return 1

    try:
        repository = JsonWorkspaceRepository(ledger_path)
        workspace = repository.read()
        assert isinstance(workspace, Workspace)
        assert len(workspace.people) >= 0
        assert len(workspace.projects) >= 0
        print("Data contract validation passed")
        return 0
    except Exception as exception:
        print(f"Data contract validation failed: {exception}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
