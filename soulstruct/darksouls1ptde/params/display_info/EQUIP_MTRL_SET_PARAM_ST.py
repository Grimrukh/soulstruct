from __future__ import annotations

__all__ = ["EQUIP_MTRL_SET_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *


EQUIP_MTRL_SET_PARAM_ST = {
    "param_type": "EQUIP_MTRL_SET_PARAM_ST",
    "file_name": "EquipMtrlSetParam",
    "nickname": "UpgradeMaterials",
    "fields": [
        ParamFieldInfo("materialId01", "UpgradeGood", True, GoodParam, "Good required to upgrade weapon."),
        ParamFieldInfo(
            "materialId02",
            "UpgradeGood2",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).",
        ),
        ParamFieldInfo(
            "materialId03",
            "UpgradeGood3",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).",
        ),
        ParamFieldInfo(
            "materialId04",
            "UpgradeGood4",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).",
        ),
        ParamFieldInfo(
            "materialId05",
            "UpgradeGood5",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).",
        ),
        ParamFieldInfo("itemNum01", "UpgradeQuantity", True, int, "Amount of Upgrade Good required for reinforcement."),
        ParamFieldInfo(
            "itemNum02",
            "UpgradeQuantity2",
            False,
            int,
            "Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).",
        ),
        ParamFieldInfo(
            "itemNum03",
            "UpgradeQuantity3",
            False,
            int,
            "Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).",
        ),
        ParamFieldInfo(
            "itemNum04",
            "UpgradeQuantity4",
            False,
            int,
            "Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).",
        ),
        ParamFieldInfo(
            "itemNum05",
            "UpgradeQuantity5",
            False,
            int,
            "Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).",
        ),
        ParamFieldInfo(
            "isDisableDispNum01:1",
            "DisableQuantityIndicator",
            True,
            bool,
            "If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is "
            "needed.",
        ),
        ParamFieldInfo(
            "isDisableDispNum02:1",
            "DisableQuantityIndicator2",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).",
        ),
        ParamFieldInfo(
            "isDisableDispNum03:1",
            "DisableQuantityIndicator3",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).",
        ),
        ParamFieldInfo(
            "isDisableDispNum04:1",
            "DisableQuantityIndicator4",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).",
        ),
        ParamFieldInfo(
            "isDisableDispNum05:1",
            "DisableQuantityIndicator5",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).",
        ),
        ParamFieldInfo("pad[6]", "Pad1", False, pad_field(6), "Null padding."),
    ],
}
