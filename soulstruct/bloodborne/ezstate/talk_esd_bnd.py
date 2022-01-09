__all__ = ["TalkESDBND"]

from soulstruct.containers.base import BinderFlags
from soulstruct.containers.bnd import BND4
from soulstruct.base.ezstate.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND, BND4):
    TALK_ESD_CLASS = TalkESD
    BND_ROOT = "N:\\SPRJ\\data\\INTERROOT_ps4\\script\\talk"

    def set_default_bnd(self):
        self.signature = "07D7R6"
        self.flags = BinderFlags(46)
        self.big_endian = False
        self.unicode = True
        self.hash_table_type = 0
        self.unknown1 = False
        self.unknown2 = False
        self.dcx_magic = (68, 76)
