from __future__ import annotations

__all__ = ["BUDGET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BUDGET_PARAM_ST(ParamRow):
    Vramall: float = ParamField(
        float, "vram_all", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrammapobjtex: float = ParamField(
        float, "vram_mapobj_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrammapobjmdl: float = ParamField(
        float, "vram_mapobj_mdl", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrammap: float = ParamField(
        float, "vram_map", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramchr: float = ParamField(
        float, "vram_chr", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramparts: float = ParamField(
        float, "vram_parts", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfx: float = ParamField(
        float, "vram_sfx", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrtex: float = ParamField(
        float, "vram_chr_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrmdl: float = ParamField(
        float, "vram_chr_mdl", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrampartstex: float = ParamField(
        float, "vram_parts_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrampartsmdl: float = ParamField(
        float, "vram_parts_mdl", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfxtex: float = ParamField(
        float, "vram_sfx_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfxmdl: float = ParamField(
        float, "vram_sfx_mdl", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramgi: float = ParamField(
        float, "vram_gi", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vrammenutex: float = ParamField(
        float, "vram_menu_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramdecalrt: float = ParamField(
        float, "vram_decal_rt", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramdecal: float = ParamField(
        float, "vram_decal", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserve_0[4]")
    Vramothertex: float = ParamField(
        float, "vram_other_tex", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramothermdl: float = ParamField(
        float, "vram_other_mdl", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Havokanim: float = ParamField(
        float, "havok_anim", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Havokins: float = ParamField(
        float, "havok_ins", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Havokhit: float = ParamField(
        float, "havok_hit", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramother: float = ParamField(
        float, "vram_other", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramdetailall: float = ParamField(
        float, "vram_detail_all", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrandparts: float = ParamField(
        float, "vram_chr_and_parts", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Havoknavimesh: float = ParamField(
        float, "havok_navimesh", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "reserve_1[24]")
