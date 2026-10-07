from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrimitiveTokens:
    red: str = "#E05A47"
    charcoal: str = "#2C2C2C"
    ivory: str = "#FDFBF7"
    steel: str = "#6E7780"
    slate: str = "#D8DDE3"
    focus: str = "#2F6F8F"
    positive: str = "#2F7D5C"
    warning: str = "#B26A00"
    danger: str = "#B84232"
    space_one: str = "0.25rem"
    space_two: str = "0.5rem"
    space_three: str = "0.75rem"
    space_four: str = "1rem"
    space_six: str = "1.5rem"
    space_eight: str = "2rem"
    radius_small: str = "0.5rem"
    radius_medium: str = "0.875rem"


@dataclass(frozen=True)
class SemanticTokens:
    primitives: PrimitiveTokens = PrimitiveTokens()

    @property
    def page_background(self) -> str:
        return self.primitives.ivory

    @property
    def surface_background(self) -> str:
        return "#FFFFFF"

    @property
    def primary_text(self) -> str:
        return self.primitives.charcoal

    @property
    def secondary_text(self) -> str:
        return self.primitives.steel

    @property
    def primary_action(self) -> str:
        return self.primitives.red

    @property
    def focus_ring(self) -> str:
        return self.primitives.focus


TOKENS = SemanticTokens()
