from __future__ import annotations

__all__ = ["TalkESDBND"]

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderFlags, DCXType
from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND):
    TALK_ESD_CLASS = TalkESD

    @classmethod
    def get_default_binder(cls) -> TalkESDBND:
        binder = cls(
            signature="07D7R6",
            flags=BinderFlags(0b00101110),
            big_endian=False,
            bit_big_endian=False,
            version=BinderVersion.V3,
            v4_info=None,
            is_split_bxf=False,
        )
        binder.dcx_type = DCXType.DCX_DFLT_10000_24_9
        return binder

    @classmethod
    def get_default_entry_path(cls, entry_name: str):
        return f"N:\\FRPG\\data\\INTERROOT_win32\\script\\talk\\{entry_name}"
