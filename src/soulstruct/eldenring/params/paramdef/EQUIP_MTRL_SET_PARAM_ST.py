from __future__ import annotations

__all__ = ["EQUIP_MTRL_SET_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_MTRL_SET_PARAM_ST(ParamRow):
    UpgradeGood: int = ParamField(
        int32, "materialId01", game_type=GoodParam, default=-1,
        tooltip="Good required to upgrade weapon.",
    )
    UpgradeGood2: int = ParamField(
        int32, "materialId02", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood3: int = ParamField(
        int32, "materialId03", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood4: int = ParamField(
        int32, "materialId04", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood5: int = ParamField(
        int32, "materialId05", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    MaterialId06: int = ParamField(
        int32, "materialId06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad_id[8]")
    UpgradeQuantity: int = ParamField(
        int8, "itemNum01", default=-1,
        tooltip="Amount of Upgrade Good required for reinforcement.",
    )
    UpgradeQuantity2: int = ParamField(
        int8, "itemNum02", default=-1,
        tooltip="Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity3: int = ParamField(
        int8, "itemNum03", default=-1,
        tooltip="Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity4: int = ParamField(
        int8, "itemNum04", default=-1,
        tooltip="Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity5: int = ParamField(
        int8, "itemNum05", default=-1,
        tooltip="Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    ItemNum06: int = ParamField(
        int8, "itemNum06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad_num[2]")
    MaterialCate01: int = ParamField(
        uint8, "materialCate01", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate02: int = ParamField(
        uint8, "materialCate02", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate03: int = ParamField(
        uint8, "materialCate03", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate04: int = ParamField(
        uint8, "materialCate04", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate05: int = ParamField(
        uint8, "materialCate05", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate06: int = ParamField(
        uint8, "materialCate06", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad_cate[2]")
    DisableQuantityIndicator: bool = ParamField(
        uint8, "isDisableDispNum01:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is "
                "needed.",
    )
    DisableQuantityIndicator2: bool = ParamField(
        uint8, "isDisableDispNum02:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator3: bool = ParamField(
        uint8, "isDisableDispNum03:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator4: bool = ParamField(
        uint8, "isDisableDispNum04:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator5: bool = ParamField(
        uint8, "isDisableDispNum05:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    IsDisableDispNum06: bool = ParamField(
        uint8, "isDisableDispNum06:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(3, "pad[3]")
