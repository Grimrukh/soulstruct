__all__ = ["TalkESDBND"]

from soulstruct.containers.base import BinderFlags
from soulstruct.containers.bnd import BND3
from soulstruct.containers.dcx import DCXType
from soulstruct.base.ezstate.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND, BND3):
    TALK_ESD_CLASS = TalkESD
    BND_ROOT = "N:\\FRPG\\data\\INTERROOT_win32\\script\\talk"

    def set_default_bnd(self):
        self.signature = "07D7R6"
        self.flags = BinderFlags(46)
        self.big_endian = False
        self.bit_big_endian = False
        self.dcx_type = DCXType.DCX_DFLT_10000_24_9  # TODO: Move to Game default for DS1.
