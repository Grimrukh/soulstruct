from soulstruct.bnd import BND3
from soulstruct.esd.base.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND, TalkDirectory as _BaseTalkDirectory
from soulstruct.maps.darksouls1.maps import ALL_MAPS, get_map

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND, BND3):
    TALK_ESD_CLASS = TalkESD
    BND_ROOT = "N:\\FRPG\\data\\INTERROOT_x32\\script\\talk"

    def set_default_bnd(self):
        self.version = "BND3"
        self.signature = "07D7R7"
        self.magic = 116
        self.big_endian = False
        self.unknown = False
        self.dcx_magic = ()


class TalkDirectory(_BaseTalkDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
    IS_DCX = True
    TALKESDBND_CLASS = TalkESDBND

    Depths: TalkESDBND
    UndeadBurg: TalkESDBND  # and Undead Parish
    FirelinkShrine: TalkESDBND
    PaintedWorld: TalkESDBND
    DarkrootGarden: TalkESDBND  # and Darkroot Basin
    Oolacile: TalkESDBND  # and all DLC
    Catacombs: TalkESDBND
    TombOfTheGiants: TalkESDBND
    AshLake: TalkESDBND  # and Great Hollow
    Blighttown: TalkESDBND
    LostIzalith: TalkESDBND  # and Demon Ruins
    # There's an unused "m14_02_00_00.talkesdbnd.dcx" file that is ignored.
    SensFortress: TalkESDBND
    AnorLondo: TalkESDBND
    NewLondoRuins: TalkESDBND  # and Valley of Drakes
    DukesArchives: TalkESDBND
    KilnOfTheFirstFlame: TalkESDBND
    UndeadAsylum: TalkESDBND
