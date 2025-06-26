from __future__ import annotations

__all__ = ["TalkDirectory"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talk_directory import TalkDirectory as _BaseTalkDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.darksouls1r.ezstate.talkesdbnd import TalkESDBND
from soulstruct.darksouls1r.maps.constants import *


class TalkDirectory(_BaseTalkDirectory):
    ALL_MAPS: tp.ClassVar = ALL_MAPS[1:]
    GET_MAP: tp.ClassVar = staticmethod(get_map)
    FILE_CLASS: tp.ClassVar = TalkESDBND

    Common = map_property(COMMON)  # type: TalkESDBND
    Depths = map_property(DEPTHS)  # type: TalkESDBND
    UndeadBurg = map_property(UNDEAD_BURG)  # type: TalkESDBND  # and Undead Parish
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: TalkESDBND
    PaintedWorld = map_property(PAINTED_WORLD)  # type: TalkESDBND
    DarkrootGarden = map_property(DARKROOT_GARDEN)  # type: TalkESDBND  # and Darkroot Basin
    Oolacile = map_property(OOLACILE)  # type: TalkESDBND  # and all DLC
    Catacombs = map_property(CATACOMBS)  # type: TalkESDBND
    TombOfTheGiants = map_property(TOMB_OF_THE_GIANTS)  # type: TalkESDBND
    AshLake = map_property(ASH_LAKE)  # type: TalkESDBND  # and Great Hollow
    Blighttown = map_property(BLIGHTTOWN)  # type: TalkESDBND
    LostIzalith = map_property(LOST_IZALITH)  # type: TalkESDBND  # and Demon Ruins
    # NOTE: There's an unused "m14_02_00_00.talkesdbnd.dcx" file that is ignored.
    SensFortress = map_property(SENS_FORTRESS)  # type: TalkESDBND
    AnorLondo = map_property(ANOR_LONDO)  # type: TalkESDBND
    NewLondoRuins = map_property(NEW_LONDO_RUINS)  # type: TalkESDBND  # and Valley of Drakes
    DukesArchives = map_property(DUKES_ARCHIVES)  # type: TalkESDBND
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: TalkESDBND
    UndeadAsylum = map_property(UNDEAD_ASYLUM)  # type: TalkESDBND
