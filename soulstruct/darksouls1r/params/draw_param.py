from __future__ import annotations

__all__ = ["DrawParam", "DrawParamBND", "DrawParamDirectory"]

import logging

from soulstruct.base.params.draw_param import (
    DrawParamBND as _BaseDrawParamBND,
    DrawParamDirectory as _BaseDrawParamDirectory,
)
from soulstruct.games import DarkSoulsDSRType

from .core import Param
from .paramdef import GET_BUNDLED_PARAMDEF

_LOGGER = logging.getLogger(__name__)


class DrawParam(Param):
    """`Param` with some extra methods that are specific to DrawParam tables."""

    def get_nonzero_entries(self, ignore_polyg=True):
        """Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if ignore_polyg:
            return {
                index: row for index, row in self.rows.items() if row.name and not row.name.startswith("0")
            }
        return {
            index: row
            for index, row in self.rows.items()
            if row.name and not row.name.startswith("0") and not row.name.lower().startswith("polyg")
        }


class DrawParamBND(_BaseDrawParamBND, DarkSoulsDSRType):

    DRAW_PARAM_CLASS = DrawParam
    GET_BUNDLED_PARAMDEF = staticmethod(GET_BUNDLED_PARAMDEF)

    DepthOfField: list[DrawParam]
    # EnvLightTex: list[DrawParam]
    Fog: list[DrawParam]
    LensFlares: list[DrawParam]
    LensFlareSources: list[DrawParam]
    AmbientLight: list[DrawParam]
    ScatteredLight: list[DrawParam]
    PointLights: list[DrawParam]
    Shadows: list[DrawParam]
    ToneCorrection: list[DrawParam]
    ToneMapping: list[DrawParam]
    # DebugAmbientLight: list[DrawParam]

    params: dict[str, list[DrawParam | None]]


class DrawParamDirectory(_BaseDrawParamDirectory, DarkSoulsDSRType):

    DRAW_PARAM_BND_CLASS = DrawParamBND
    DRAW_PARAM_MAPS = {
        "m10": "Depths, Undead Burg/Parish, Firelink Shrine",
        "m11": "Painted World",
        "m12": "Darkroot, Oolacile",
        "m13": "Catacombs, Tomb of the Giants, Great Hollow, Ash Lake",
        "m14": "Blighttown, Quelaag's Domain, Demon Ruins, Lost Izalith",
        "m15": "Sen's Fortress, Anor Londo",
        "m16": "New Londo Ruins, Valley of Drakes",
        "m17": "Duke's Archives",
        "m18": "Kiln of the First Flame, Undead Asylum",
        "default": "Menus",
    }

    m10: DrawParamBND
    m11: DrawParamBND
    m12: DrawParamBND
    m13: DrawParamBND
    m14: DrawParamBND
    m15: DrawParamBND
    m16: DrawParamBND
    m17: DrawParamBND
    m18: DrawParamBND
    m99: DrawParamBND
    default: DrawParamBND

    bnds: dict[str, DrawParamBND]
