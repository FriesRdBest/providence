from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrimitiveTokens:
    red: str = "#E05A47"
    red_dark: str = "#C54A3A"
    charcoal: str = "#1A1A1A"
    charcoal_light: str = "#2D2D2D"
    ivory: str = "#FDFBF7"
    white: str = "#FFFFFF"
    steel: str = "#6B7280"
    slate: str = "#D1D5DB"
    slate_light: str = "#E5E7EB"
    focus: str = "#2F6F8F"
    positive: str = "#10B981"
    warning: str = "#F59E0B"
    danger: str = "#EF4444"
    purple: str = "#7C3AED"
    purple_light: str = "#A78BFA"
    space_one: str = "0.25rem"
    space_two: str = "0.5rem"
    space_three: str = "0.75rem"
    space_four: str = "1rem"
    space_six: str = "1.5rem"
    space_eight: str = "2rem"
    space_twelve: str = "3rem"
    radius_small: str = "0.5rem"
    radius_medium: str = "0.875rem"
    radius_large: str = "1.25rem"
    shadow_sm: str = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    shadow_md: str = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
    shadow_lg: str = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
    shadow_xl: str = "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"


@dataclass(frozen=True)
class SemanticTokens:
    primitives: PrimitiveTokens = PrimitiveTokens()

    @property
    def page_background(self) -> str:
        return self.primitives.ivory

    @property
    def surface_background(self) -> str:
        return self.primitives.white

    @property
    def surface_elevated(self) -> str:
        return "#FAFAFA"

    @property
    def primary_text(self) -> str:
        return self.primitives.charcoal

    @property
    def secondary_text(self) -> str:
        return self.primitives.steel

    @property
    def tertiary_text(self) -> str:
        return self.primitives.slate

    @property
    def primary_action(self) -> str:
        return self.primitives.red

    @property
    def primary_action_hover(self) -> str:
        return self.primitives.red_dark

    @property
    def focus_ring(self) -> str:
        return self.primitives.focus

    @property
    def border_subtle(self) -> str:
        return self.primitives.slate_light

    @property
    def border_default(self) -> str:
        return self.primitives.slate

    @property
    def success(self) -> str:
        return self.primitives.positive

    @property
    def warning(self) -> str:
        return self.primitives.warning

    @property
    def error(self) -> str:
        return self.primitives.danger

    @property
    def accent_purple(self) -> str:
        return self.primitives.purple


TOKENS = SemanticTokens()
