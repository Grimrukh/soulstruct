from __future__ import annotations

__all__ = ["EQUIP_MTRL_SET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_MTRL_SET_PARAM_ST(ParamRow):
    UpgradeGood: int = ParamField(
        int, "materialId01", game_type=GoodParam, default=-1,
        tooltip="Good required to upgrade weapon.",
    )
    UpgradeGood2: int = ParamField(
        int, "materialId02", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood3: int = ParamField(
        int, "materialId03", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood4: int = ParamField(
        int, "materialId04", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeGood5: int = ParamField(
        int, "materialId05", game_type=GoodParam, default=-1,
        tooltip="Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
                "may still work as a requirement).",
    )
    UpgradeQuantity: int = ParamField(
        sbyte, "itemNum01", default=-1,
        tooltip="Amount of Upgrade Good required for reinforcement.",
    )
    UpgradeQuantity2: int = ParamField(
        sbyte, "itemNum02", default=-1,
        tooltip="Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity3: int = ParamField(
        sbyte, "itemNum03", default=-1,
        tooltip="Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity4: int = ParamField(
        sbyte, "itemNum04", default=-1,
        tooltip="Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    UpgradeQuantity5: int = ParamField(
        sbyte, "itemNum05", default=-1,
        tooltip="Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it "
                "(though it may still work as a requirement).",
    )
    DisableQuantityIndicator: bool = ParamField(
        byte, "isDisableDispNum01:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is "
                "needed.",
    )
    DisableQuantityIndicator2: bool = ParamField(
        byte, "isDisableDispNum02:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator3: bool = ParamField(
        byte, "isDisableDispNum03:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator4: bool = ParamField(
        byte, "isDisableDispNum04:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    DisableQuantityIndicator5: bool = ParamField(
        byte, "isDisableDispNum05:1", bit_count=1, default=False,
        tooltip="If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
                "upgrade good is needed (though again, this slot is never used).",
    )
    _Pad0: bytes = ParamPad(6, "pad[6]")
