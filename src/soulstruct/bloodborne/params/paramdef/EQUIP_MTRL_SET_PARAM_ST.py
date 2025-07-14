from __future__ import annotations

__all__ = ["EQUIP_MTRL_SET_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
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
    _Pad0: bytes = ParamPad(6, "pad[6]")
