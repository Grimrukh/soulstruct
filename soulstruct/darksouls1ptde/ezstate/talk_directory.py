from soulstruct.base.ezstate.talk_directory import TalkDirectory as _BaseTalkDirectory
from .talk_esd_bnd import TalkESDBND
from ..maps import ALL_MAPS, get_map


class TalkDirectory(_BaseTalkDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
    IS_DCX = False
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
