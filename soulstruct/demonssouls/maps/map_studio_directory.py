from __future__ import annotations

__all__ = ["MapStudioDirectory"]

import typing as tp
from dataclasses import field

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
    files: dict[str, MSB] = field(default_factory=dict)

    Common = map_property(COMMON)  # type: MSB
    TheNexus: map_property(THE_NEXUS)  # type: MSB
    BoletarianPalace1: map_property(BOLETARIAN_PALACE_1)  # type: MSB
    BoletarianPalace2: map_property(BOLETARIAN_PALACE_2)  # type: MSB
    BoletarianPalace3: map_property(BOLETARIAN_PALACE_3)  # type: MSB
    BoletarianPalace4: map_property(BOLETARIAN_PALACE_4)  # type: MSB
    ShrineOfStormsCut: map_property(SHRINE_OF_STORMS_CUT)  # type: MSB
    ShrineOfStorms1: map_property(SHRINE_OF_STORMS_1)  # type: MSB
    ShrineOfStorms2: map_property(SHRINE_OF_STORMS_2)  # type: MSB
    ShrineOfStorms3: map_property(SHRINE_OF_STORMS_3)  # type: MSB
    TowerOfLatria1: map_property(TOWER_OF_LATRIA_1)  # type: MSB
    TowerOfLatria2: map_property(TOWER_OF_LATRIA_2)  # type: MSB
    TowerOfLatria3: map_property(TOWER_OF_LATRIA_3)  # type: MSB
    ValleyOfDefilement1: map_property(VALLEY_OF_DEFILEMENT_1)  # type: MSB
    ValleyOfDefilement2: map_property(VALLEY_OF_DEFILEMENT_2)  # type: MSB
    ValleyOfDefilement3: map_property(VALLEY_OF_DEFILEMENT_3)  # type: MSB
    StonefangTunnel1: map_property(STONEFANG_TUNNEL_1)  # type: MSB
    StonefangTunnel2: map_property(STONEFANG_TUNNEL_2)  # type: MSB
    StonefangTunnel3: map_property(STONEFANG_TUNNEL_3)  # type: MSB
    NorthernLimit1: map_property(NORTHERN_LIMIT_1)  # type: MSB
    NorthernLimit2: map_property(NORTHERN_LIMIT_2)  # type: MSB
    NorthernLimit3: map_property(NORTHERN_LIMIT_3)  # type: MSB
    Tutorial1: map_property(TUTORIAL_1)  # type: MSB
    Tutorial2: map_property(TUTORIAL_2)  # type: MSB
    Tutorial3: map_property(TUTORIAL_3)  # type: MSB
