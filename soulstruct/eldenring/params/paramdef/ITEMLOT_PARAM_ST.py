from __future__ import annotations

__all__ = ["ITEMLOT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ITEMLOT_PARAM_ST(ParamRow):
    Item1: int = ParamField(
        int, "lotItemId01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2: int = ParamField(
        int, "lotItemId02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3: int = ParamField(
        int, "lotItemId03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4: int = ParamField(
        int, "lotItemId04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5: int = ParamField(
        int, "lotItemId05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6: int = ParamField(
        int, "lotItemId06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7: int = ParamField(
        int, "lotItemId07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8: int = ParamField(
        int, "lotItemId08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1Category: int = ParamField(
        int, "lotItemCategory01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2Category: int = ParamField(
        int, "lotItemCategory02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3Category: int = ParamField(
        int, "lotItemCategory03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4Category: int = ParamField(
        int, "lotItemCategory04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5Category: int = ParamField(
        int, "lotItemCategory05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6Category: int = ParamField(
        int, "lotItemCategory06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7Category: int = ParamField(
        int, "lotItemCategory07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8Category: int = ParamField(
        int, "lotItemCategory08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1Flag: int = ParamField(
        uint, "getItemFlagId01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2Flag: int = ParamField(
        uint, "getItemFlagId02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3Flag: int = ParamField(
        uint, "getItemFlagId03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4Flag: int = ParamField(
        uint, "getItemFlagId04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5Flag: int = ParamField(
        uint, "getItemFlagId05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6Flag: int = ParamField(
        uint, "getItemFlagId06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7Flag: int = ParamField(
        uint, "getItemFlagId07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8Flag: int = ParamField(
        uint, "getItemFlagId08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemFlag: int = ParamField(
        uint, "getItemFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FirstCumulativeFlag: int = ParamField(
        uint, "cumulateNumFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxCumulativeAdditions: int = ParamField(
        byte, "cumulateNumMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemLotRarity: int = ParamField(
        sbyte, "lotItem_Rarity", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item1Count: int = ParamField(
        byte, "lotItemNum01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2Count: int = ParamField(
        byte, "lotItemNum02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3Count: int = ParamField(
        byte, "lotItemNum03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4Count: int = ParamField(
        byte, "lotItemNum04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5Count: int = ParamField(
        byte, "lotItemNum05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6Count: int = ParamField(
        byte, "lotItemNum06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7Count: int = ParamField(
        byte, "lotItemNum07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8Count: int = ParamField(
        byte, "lotItemNum08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1LuckEnabled: int = ParamField(
        ushort, "enableLuck01:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2LuckEnabled: int = ParamField(
        ushort, "enableLuck02:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3LuckEnabled: int = ParamField(
        ushort, "enableLuck03:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4LuckEnabled: int = ParamField(
        ushort, "enableLuck04:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5LuckEnabled: int = ParamField(
        ushort, "enableLuck05:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6LuckEnabled: int = ParamField(
        ushort, "enableLuck06:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7LuckEnabled: int = ParamField(
        ushort, "enableLuck07:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8LuckEnabled: int = ParamField(
        ushort, "enableLuck08:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item1ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset01:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item2ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset02:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item3ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset03:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item4ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset04:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item5ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset05:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item6ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset06:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item7ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset07:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Item8ResetCumulativePointsOnDrop: int = ParamField(
        ushort, "cumulateReset08:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GameClearOffset: int = ParamField(
        sbyte, "GameClearOffset", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CanExecByFriendlyGhost: int = ParamField(
        byte, "canExecByFriendlyGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanExecByHostileGhost: int = ParamField(
        byte, "canExecByHostileGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PAD1: int = ParamField(
        byte, "PAD1:6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PAD2: int = ParamField(
        ushort, "PAD2", default=0,
        tooltip="TOOLTIP-TODO",
    )
