from __future__ import annotations

__all__ = ["BUDGET_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class BUDGET_PARAM_ST(ParamRow):
    Vramall: float = ParamField(
        float32, "vram_all", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrammapobjtex: float = ParamField(
        float32, "vram_mapobj_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrammapobjmdl: float = ParamField(
        float32, "vram_mapobj_mdl", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrammap: float = ParamField(
        float32, "vram_map", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramchr: float = ParamField(
        float32, "vram_chr", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramparts: float = ParamField(
        float32, "vram_parts", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfx: float = ParamField(
        float32, "vram_sfx", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrtex: float = ParamField(
        float32, "vram_chr_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrmdl: float = ParamField(
        float32, "vram_chr_mdl", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrampartstex: float = ParamField(
        float32, "vram_parts_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrampartsmdl: float = ParamField(
        float32, "vram_parts_mdl", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfxtex: float = ParamField(
        float32, "vram_sfx_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramsfxmdl: float = ParamField(
        float32, "vram_sfx_mdl", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramgi: float = ParamField(
        float32, "vram_gi", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vrammenutex: float = ParamField(
        float32, "vram_menu_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramdecalrt: float = ParamField(
        float32, "vram_decal_rt", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramdecal: float = ParamField(
        float32, "vram_decal", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserve_0[4]")
    Vramothertex: float = ParamField(
        float32, "vram_other_tex", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramothermdl: float = ParamField(
        float32, "vram_other_mdl", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Havokanim: float = ParamField(
        float32, "havok_anim", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Havokins: float = ParamField(
        float32, "havok_ins", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Havokhit: float = ParamField(
        float32, "havok_hit", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramother: float = ParamField(
        float32, "vram_other", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramdetailall: float = ParamField(
        float32, "vram_detail_all", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Vramchrandparts: float = ParamField(
        float32, "vram_chr_and_parts", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Havoknavimesh: float = ParamField(
        float32, "havok_navimesh", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "reserve_1[24]")
