from __future__ import annotations

__all__ = ["RANDOM_APPEAR_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RANDOM_APPEAR_PARAM_ST(ParamRow):
    Slot0: bool = ParamField(
        byte, "slot0:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot1: bool = ParamField(
        byte, "slot1:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot2: bool = ParamField(
        byte, "slot2:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot3: bool = ParamField(
        byte, "slot3:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot4: bool = ParamField(
        byte, "slot4:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot5: bool = ParamField(
        byte, "slot5:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot6: bool = ParamField(
        byte, "slot6:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot7: bool = ParamField(
        byte, "slot7:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot8: bool = ParamField(
        byte, "slot8:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot9: bool = ParamField(
        byte, "slot9:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot10: bool = ParamField(
        byte, "slot10:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot11: bool = ParamField(
        byte, "slot11:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot12: bool = ParamField(
        byte, "slot12:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot13: bool = ParamField(
        byte, "slot13:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot14: bool = ParamField(
        byte, "slot14:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot15: bool = ParamField(
        byte, "slot15:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot16: bool = ParamField(
        byte, "slot16:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot17: bool = ParamField(
        byte, "slot17:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot18: bool = ParamField(
        byte, "slot18:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot19: bool = ParamField(
        byte, "slot19:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot20: bool = ParamField(
        byte, "slot20:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot21: bool = ParamField(
        byte, "slot21:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot22: bool = ParamField(
        byte, "slot22:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot23: bool = ParamField(
        byte, "slot23:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot24: bool = ParamField(
        byte, "slot24:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot25: bool = ParamField(
        byte, "slot25:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot26: bool = ParamField(
        byte, "slot26:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot27: bool = ParamField(
        byte, "slot27:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot28: bool = ParamField(
        byte, "slot28:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot29: bool = ParamField(
        byte, "slot29:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot30: bool = ParamField(
        byte, "slot30:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot31: bool = ParamField(
        byte, "slot31:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot32: bool = ParamField(
        byte, "slot32:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot33: bool = ParamField(
        byte, "slot33:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot34: bool = ParamField(
        byte, "slot34:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot35: bool = ParamField(
        byte, "slot35:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot36: bool = ParamField(
        byte, "slot36:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot37: bool = ParamField(
        byte, "slot37:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot38: bool = ParamField(
        byte, "slot38:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot39: bool = ParamField(
        byte, "slot39:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot40: bool = ParamField(
        byte, "slot40:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot41: bool = ParamField(
        byte, "slot41:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot42: bool = ParamField(
        byte, "slot42:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot43: bool = ParamField(
        byte, "slot43:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot44: bool = ParamField(
        byte, "slot44:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot45: bool = ParamField(
        byte, "slot45:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot46: bool = ParamField(
        byte, "slot46:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot47: bool = ParamField(
        byte, "slot47:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot48: bool = ParamField(
        byte, "slot48:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot49: bool = ParamField(
        byte, "slot49:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot50: bool = ParamField(
        byte, "slot50:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot51: bool = ParamField(
        byte, "slot51:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot52: bool = ParamField(
        byte, "slot52:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot53: bool = ParamField(
        byte, "slot53:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot54: bool = ParamField(
        byte, "slot54:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot55: bool = ParamField(
        byte, "slot55:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot56: bool = ParamField(
        byte, "slot56:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot57: bool = ParamField(
        byte, "slot57:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot58: bool = ParamField(
        byte, "slot58:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot59: bool = ParamField(
        byte, "slot59:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot60: bool = ParamField(
        byte, "slot60:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot61: bool = ParamField(
        byte, "slot61:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot62: bool = ParamField(
        byte, "slot62:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot63: bool = ParamField(
        byte, "slot63:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot64: bool = ParamField(
        byte, "slot64:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot65: bool = ParamField(
        byte, "slot65:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot66: bool = ParamField(
        byte, "slot66:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot67: bool = ParamField(
        byte, "slot67:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot68: bool = ParamField(
        byte, "slot68:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot69: bool = ParamField(
        byte, "slot69:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot70: bool = ParamField(
        byte, "slot70:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot71: bool = ParamField(
        byte, "slot71:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot72: bool = ParamField(
        byte, "slot72:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot73: bool = ParamField(
        byte, "slot73:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot74: bool = ParamField(
        byte, "slot74:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot75: bool = ParamField(
        byte, "slot75:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot76: bool = ParamField(
        byte, "slot76:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot77: bool = ParamField(
        byte, "slot77:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot78: bool = ParamField(
        byte, "slot78:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot79: bool = ParamField(
        byte, "slot79:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot80: bool = ParamField(
        byte, "slot80:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot81: bool = ParamField(
        byte, "slot81:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot82: bool = ParamField(
        byte, "slot82:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot83: bool = ParamField(
        byte, "slot83:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot84: bool = ParamField(
        byte, "slot84:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot85: bool = ParamField(
        byte, "slot85:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot86: bool = ParamField(
        byte, "slot86:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot87: bool = ParamField(
        byte, "slot87:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot88: bool = ParamField(
        byte, "slot88:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot89: bool = ParamField(
        byte, "slot89:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot90: bool = ParamField(
        byte, "slot90:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot91: bool = ParamField(
        byte, "slot91:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot92: bool = ParamField(
        byte, "slot92:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot93: bool = ParamField(
        byte, "slot93:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot94: bool = ParamField(
        byte, "slot94:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot95: bool = ParamField(
        byte, "slot95:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot96: bool = ParamField(
        byte, "slot96:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot97: bool = ParamField(
        byte, "slot97:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot98: bool = ParamField(
        byte, "slot98:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Slot99: bool = ParamField(
        byte, "slot99:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad:4", bit_count=4)
