from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrimitiveTokens:
    ivory_25: str = "#FEFDFB"
    ivory_50: str = "#FDFBF7"
    ivory_100: str = "#F7F3ED"
    white: str = "#FFFFFF"

    charcoal_950: str = "#1F211F"
    charcoal_800: str = "#353632"
    charcoal_700: str = "#4D4E49"

    steel_600: str = "#65707A"
    steel_500: str = "#7D8790"
    steel_300: str = "#C9CFD2"
    steel_200: str = "#DDE1E2"
    steel_100: str = "#ECEFED"

    red_600: str = "#D94F3D"
    red_500: str = "#E05A47"
    red_100: str = "#FCE8E4"

    green_700: str = "#267355"
    green_100: str = "#E4F3EB"

    amber_700: str = "#94621B"
    amber_100: str = "#FFF2D7"

    blue_700: str = "#285A78"
    blue_100: str = "#E5F0F6"

    focus: str = "#285A78"

    space_1: str = "0.25rem"
    space_2: str = "0.5rem"
    space_3: str = "0.75rem"
    space_4: str = "1rem"
    space_5: str = "1.25rem"
    space_6: str = "1.5rem"
    space_8: str = "2rem"
    space_10: str = "2.5rem"
    space_12: str = "3rem"

    radius_sm: str = "0.5rem"
    radius_md: str = "0.75rem"
    radius_lg: str = "1rem"
    radius_xl: str = "1.25rem"

    shadow_card: str = "0 1px 2px rgba(31, 33, 31, 0.04), 0 8px 24px rgba(31, 33, 31, 0.04)"
    shadow_float: str = "0 8px 28px rgba(31, 33, 31, 0.08)"


@dataclass(frozen=True)
class SemanticTokens:
    primitives: PrimitiveTokens = PrimitiveTokens()

    @property
    def app_surface(self) -> str:
        return self.primitives.ivory_50

    @property
    def surface_primary(self) -> str:
        return self.primitives.white

    @property
    def surface_secondary(self) -> str:
        return self.primitives.ivory_100

    @property
    def surface_subtle(self) -> str:
        return self.primitives.ivory_25

    @property
    def text_core(self) -> str:
        return self.primitives.charcoal_950

    @property
    def text_supporting(self) -> str:
        return self.primitives.steel_600

    @property
    def text_muted(self) -> str:
        return self.primitives.steel_500

    @property
    def border_subtle(self) -> str:
        return self.primitives.steel_100

    @property
    def border_default(self) -> str:
        return self.primitives.steel_200

    @property
    def action_primary(self) -> str:
        return self.primitives.red_500

    @property
    def action_primary_hover(self) -> str:
        return self.primitives.red_600

    @property
    def action_secondary(self) -> str:
        return self.primitives.charcoal_950

    @property
    def status_healthy(self) -> str:
        return self.primitives.green_700

    @property
    def status_healthy_surface(self) -> str:
        return self.primitives.green_100

    @property
    def status_watch(self) -> str:
        return self.primitives.amber_700

    @property
    def status_watch_surface(self) -> str:
        return self.primitives.amber_100

    @property
    def status_risk(self) -> str:
        return self.primitives.red_600

    @property
    def status_risk_surface(self) -> str:
        return self.primitives.red_100

    @property
    def status_neutral(self) -> str:
        return self.primitives.blue_700

    @property
    def status_neutral_surface(self) -> str:
        return self.primitives.blue_100

    @property
    def focus_ring(self) -> str:
        return self.primitives.focus


TOKENS = SemanticTokens()
