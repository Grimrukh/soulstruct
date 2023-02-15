from __future__ import annotations

__all__ = ["ITEMLOT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ITEMLOT_PARAM_ST(ParamRow):
    LotItemId01: int = ParamField(
        int, "lotItemId01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId02: int = ParamField(
        int, "lotItemId02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId03: int = ParamField(
        int, "lotItemId03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId04: int = ParamField(
        int, "lotItemId04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId05: int = ParamField(
        int, "lotItemId05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId06: int = ParamField(
        int, "lotItemId06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId07: int = ParamField(
        int, "lotItemId07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemId08: int = ParamField(
        int, "lotItemId08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory01: int = ParamField(
        int, "lotItemCategory01", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory02: int = ParamField(
        int, "lotItemCategory02", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory03: int = ParamField(
        int, "lotItemCategory03", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory04: int = ParamField(
        int, "lotItemCategory04", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory05: int = ParamField(
        int, "lotItemCategory05", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory06: int = ParamField(
        int, "lotItemCategory06", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory07: int = ParamField(
        int, "lotItemCategory07", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemCategory08: int = ParamField(
        int, "lotItemCategory08", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint01: int = ParamField(
        ushort, "lotItemBasePoint01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint02: int = ParamField(
        ushort, "lotItemBasePoint02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint03: int = ParamField(
        ushort, "lotItemBasePoint03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint04: int = ParamField(
        ushort, "lotItemBasePoint04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint05: int = ParamField(
        ushort, "lotItemBasePoint05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint06: int = ParamField(
        ushort, "lotItemBasePoint06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint07: int = ParamField(
        ushort, "lotItemBasePoint07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemBasePoint08: int = ParamField(
        ushort, "lotItemBasePoint08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint01: int = ParamField(
        ushort, "cumulateLotPoint01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint02: int = ParamField(
        ushort, "cumulateLotPoint02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint03: int = ParamField(
        ushort, "cumulateLotPoint03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint04: int = ParamField(
        ushort, "cumulateLotPoint04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint05: int = ParamField(
        ushort, "cumulateLotPoint05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint06: int = ParamField(
        ushort, "cumulateLotPoint06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint07: int = ParamField(
        ushort, "cumulateLotPoint07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateLotPoint08: int = ParamField(
        ushort, "cumulateLotPoint08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId01: int = ParamField(
        uint, "getItemFlagId01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId02: int = ParamField(
        uint, "getItemFlagId02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId03: int = ParamField(
        uint, "getItemFlagId03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId04: int = ParamField(
        uint, "getItemFlagId04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId05: int = ParamField(
        uint, "getItemFlagId05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId06: int = ParamField(
        uint, "getItemFlagId06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId07: int = ParamField(
        uint, "getItemFlagId07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId08: int = ParamField(
        uint, "getItemFlagId08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetItemFlagId: int = ParamField(
        uint, "getItemFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateNumFlagId: int = ParamField(
        uint, "cumulateNumFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CumulateNumMax: int = ParamField(
        byte, "cumulateNumMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemRarity: int = ParamField(
        sbyte, "lotItem_Rarity", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum01: int = ParamField(
        byte, "lotItemNum01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum02: int = ParamField(
        byte, "lotItemNum02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum03: int = ParamField(
        byte, "lotItemNum03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum04: int = ParamField(
        byte, "lotItemNum04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum05: int = ParamField(
        byte, "lotItemNum05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum06: int = ParamField(
        byte, "lotItemNum06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum07: int = ParamField(
        byte, "lotItemNum07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotItemNum08: int = ParamField(
        byte, "lotItemNum08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck01: bool = ParamField(
        ushort, "enableLuck01:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck02: bool = ParamField(
        ushort, "enableLuck02:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck03: bool = ParamField(
        ushort, "enableLuck03:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck04: bool = ParamField(
        ushort, "enableLuck04:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck05: bool = ParamField(
        ushort, "enableLuck05:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck06: bool = ParamField(
        ushort, "enableLuck06:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck07: bool = ParamField(
        ushort, "enableLuck07:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLuck08: bool = ParamField(
        ushort, "enableLuck08:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset01: bool = ParamField(
        ushort, "cumulateReset01:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset02: bool = ParamField(
        ushort, "cumulateReset02:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset03: bool = ParamField(
        ushort, "cumulateReset03:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset04: bool = ParamField(
        ushort, "cumulateReset04:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset05: bool = ParamField(
        ushort, "cumulateReset05:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset06: bool = ParamField(
        ushort, "cumulateReset06:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset07: bool = ParamField(
        ushort, "cumulateReset07:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CumulateReset08: bool = ParamField(
        ushort, "cumulateReset08:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    GameClearOffset: int = ParamField(
        sbyte, "GameClearOffset", ITEMLOT_ROUND_COUNT, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CanExecByFriendlyGhost: bool = ParamField(
        byte, "canExecByFriendlyGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanExecByHostileGhost: bool = ParamField(
        byte, "canExecByHostileGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    PAD1: int = ParamField(
        byte, "PAD1:6", bit_count=6, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PAD2: int = ParamField(
        ushort, "PAD2", default=0,
        tooltip="TOOLTIP-TODO",
    )
