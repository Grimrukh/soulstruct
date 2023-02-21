from __future__ import annotations

__all__ = ["EventDirectory"]

from soulstruct.base.events.event_directory import EventDirectory as _BaseEventDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.darksouls1r.events.emevd.core import EMEVD
from soulstruct.darksouls1ptde.maps.constants import *


class EventDirectory(_BaseEventDirectory):
    FILE_CLASS = EMEVD
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)

    Common = map_property(COMMON)  # type: EMEVD
    Depths = map_property(DEPTHS)  # type: EMEVD
    UndeadBurg = map_property(UNDEAD_BURG)  # type: EMEVD  # and Undead Parish
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: EMEVD
    PaintedWorld = map_property(PAINTED_WORLD)  # type: EMEVD
    DarkrootGarden = map_property(DARKROOT_GARDEN)  # type: EMEVD  # and Darkroot Basin
    Oolacile = map_property(OOLACILE)  # type: EMEVD  # and all DLC
    Catacombs = map_property(CATACOMBS)  # type: EMEVD
    TombOfTheGiants = map_property(TOMB_OF_THE_GIANTS)  # type: EMEVD
    AshLake = map_property(ASH_LAKE)  # type: EMEVD  # and Great Hollow
    Blighttown = map_property(BLIGHTTOWN)  # type: EMEVD
    LostIzalith = map_property(LOST_IZALITH)  # type: EMEVD  # and Demon Ruins
    SensFortress = map_property(SENS_FORTRESS)  # type: EMEVD
    AnorLondo = map_property(ANOR_LONDO)  # type: EMEVD
    NewLondoRuins = map_property(NEW_LONDO_RUINS)  # type: EMEVD  # and Valley of Drakes
    DukesArchives = map_property(DUKES_ARCHIVES)  # type: EMEVD
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: EMEVD
    UndeadAsylum = map_property(UNDEAD_ASYLUM)  # type: EMEVD
