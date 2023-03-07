from __future__ import annotations

__all__ = ["MapStudioDirectory"]

import typing as tp

from soulstruct.base.game_file_directory import map_property
from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory

from .constants import *
from .msb import MSB


class MapStudioDirectory(_BaseMapStudioDirectory):
    """Dark Souls (either version) `MapStudio` directory.

    The format of these files is exactly the same in PTD and DSR. The vanilla DSR files have a few new additions (the
    bonfire near Vamos and lots of Arena-related entries), but you can safely use the exact same MSB files in either
    version of the game if you're not concerned with these differences.

    Note that Darkroot Garden (m12_00) has two MSB files, one ending in '00' (pre-DLC map data) and one ending in
    '01' (post-DLC map data). The PC version of the game will always have the DLC, so the '00' version is completely
    unused and ignored by Soulstruct. (You can even just delete the MSB file.) Note that 'm12_00_00_00.emevd[.dcx]'
    is still used for Darkroot's event scripts, however.
    """

    FILE_CLASS: tp.ClassVar = MSB
    ALL_MAPS: tp.ClassVar = tuple(m for m in ALL_MAPS if m.msb_file_stem)
    GET_MAP: tp.ClassVar = staticmethod(get_map)

    # Type hint override.
    files: dict[str, MSB]

    Common = map_property(COMMON)  # type: MSB
    Depths = map_property(DEPTHS)  # type: MSB
    UndeadBurg = map_property(UNDEAD_BURG)  # type: MSB  # and Undead Parish
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: MSB
    PaintedWorld = map_property(PAINTED_WORLD)  # type: MSB
    DarkrootGarden = map_property(DARKROOT_GARDEN)  # type: MSB  # and Darkroot Basin
    Oolacile = map_property(OOLACILE)  # type: MSB  # and all DLC
    Catacombs = map_property(CATACOMBS)  # type: MSB
    TombOfTheGiants = map_property(TOMB_OF_THE_GIANTS)  # type: MSB
    AshLake = map_property(ASH_LAKE)  # type: MSB  # and Great Hollow
    Blighttown = map_property(BLIGHTTOWN)  # type: MSB
    LostIzalith = map_property(LOST_IZALITH)  # type: MSB  # and Demon Ruins
    SensFortress = map_property(SENS_FORTRESS)  # type: MSB
    AnorLondo = map_property(ANOR_LONDO)  # type: MSB
    NewLondoRuins = map_property(NEW_LONDO_RUINS)  # type: MSB  # and Valley of Drakes
    DukesArchives = map_property(DUKES_ARCHIVES)  # type: MSB
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: MSB
    UndeadAsylum = map_property(UNDEAD_ASYLUM)  # type: MSB
