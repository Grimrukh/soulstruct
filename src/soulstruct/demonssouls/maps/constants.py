__all__ = [
    "COMMON",
    "THE_NEXUS",
    "BOLETARIAN_PALACE_1",
    "BOLETARIAN_PALACE_2",
    "BOLETARIAN_PALACE_3",
    "BOLETARIAN_PALACE_4",
    "SHRINE_OF_STORMS_CUT",
    "SHRINE_OF_STORMS_1",
    "SHRINE_OF_STORMS_2",
    "SHRINE_OF_STORMS_3",
    "TOWER_OF_LATRIA_1",
    "TOWER_OF_LATRIA_2",
    "TOWER_OF_LATRIA_3",
    "VALLEY_OF_DEFILEMENT_1",
    "VALLEY_OF_DEFILEMENT_2",
    "VALLEY_OF_DEFILEMENT_3",
    "STONEFANG_TUNNEL_1",
    "STONEFANG_TUNNEL_2",
    "STONEFANG_TUNNEL_3",
    "NORTHERN_LIMIT_1",
    "NORTHERN_LIMIT_2",
    "NORTHERN_LIMIT_3",
    "TUTORIAL_1",
    "TUTORIAL_2",
    "TUTORIAL_3",
    "ALL_MAPS",
    "get_map",
    "get_map_variable_name",
]

from soulstruct.base.maps.utilities import get_map as _get_map_base, MAP_SOURCE_TYPING
from soulstruct.darksouls1ptde.game_types.map_types import Map

COMMON = Map(
    None,
    None,
    name="Common",
    emevd_file_stem="common",
    msb_file_stem=None,
    ai_file_stem="aiCommon",
    esd_file_stem=None,
    variable_name="COMMON",
    verbose_name="Common",
)
THE_NEXUS = Map(
    1,
    0,
    name="TheNexus",
    variable_name="THE_NEXUS",
    verbose_name="The Nexus",
)
BOLETARIAN_PALACE_1 = Map(
    2,
    0,
    name="BoletarianPalace1",
    variable_name="BOLETARIAN_PALACE_1",
    verbose_name="Boletarian Palace (1-1)",
)
BOLETARIAN_PALACE_2 = Map(
    2,
    1,
    name="BoletarianPalace2",
    variable_name="BOLETARIAN_PALACE_2",
    verbose_name="Boletarian Palace (1-2)",
)
BOLETARIAN_PALACE_3 = Map(
    2,
    2,
    name="BoletarianPalace3",
    variable_name="BOLETARIAN_PALACE_3",
    verbose_name="Boletarian Palace (1-3)",
)
BOLETARIAN_PALACE_4 = Map(
    2,
    3,
    name="BoletarianPalace4",
    variable_name="BOLETARIAN_PALACE_4",
    verbose_name="Boletarian Palace (1-4)",
)
SHRINE_OF_STORMS_CUT = Map(
    3,
    0,
    name="ShrineOfStormsCut",
    variable_name="SHRINE_OF_STORMS_CUT",
    verbose_name="Shrine of Storms (Cut)",
)
SHRINE_OF_STORMS_1 = Map(
    3,
    1,
    name="ShrineOfStorms1",
    variable_name="SHRINE_OF_STORMS_1",
    verbose_name="Shrine of Storms (4-1)",
)
SHRINE_OF_STORMS_2 = Map(
    3,
    2,
    name="ShrineOfStorms2",
    variable_name="SHRINE_OF_STORMS_2",
    verbose_name="Shrine of Storms (4-2)",
)
SHRINE_OF_STORMS_3 = Map(
    3,
    3,
    name="ShrineOfStorms3",
    variable_name="SHRINE_OF_STORMS_3",
    verbose_name="Shrine of Storms (4-3)",
)
TOWER_OF_LATRIA_1 = Map(
    4,
    0,
    name="TowerOfLatria1",
    variable_name="TOWER_OF_LATRIA_1",
    verbose_name="Tower of Latria (3-1)",
)
TOWER_OF_LATRIA_2 = Map(
    4,
    1,
    name="TowerOfLatria2",
    variable_name="TOWER_OF_LATRIA_2",
    verbose_name="Tower of Latria (3-2)",
)
TOWER_OF_LATRIA_3 = Map(
    4,
    2,
    name="TowerOfLatria3",
    variable_name="TOWER_OF_LATRIA_3",
    verbose_name="Tower of Latria (3-3)",
)
VALLEY_OF_DEFILEMENT_1 = Map(
    5,
    0,
    name="ValleyOfDefilement1",
    variable_name="VALLEY_OF_DEFILEMENT_1",
    verbose_name="Valley of Defilement (5-1)",
)
VALLEY_OF_DEFILEMENT_2 = Map(
    5,
    1,
    name="ValleyOfDefilement2",
    variable_name="VALLEY_OF_DEFILEMENT_2",
    verbose_name="Valley of Defilement (5-2)",
)
VALLEY_OF_DEFILEMENT_3 = Map(
    5,
    2,
    name="ValleyOfDefilement3",
    variable_name="VALLEY_OF_DEFILEMENT_3",
    verbose_name="Valley of Defilement (5-3)",
)
STONEFANG_TUNNEL_1 = Map(
    6,
    0,
    name="StonefangTunnel1",
    variable_name="STONEFANG_TUNNEL_1",
    verbose_name="Stonefang Tunnel (2-1)",
)
STONEFANG_TUNNEL_2 = Map(
    6,
    1,
    name="StonefangTunnel2",
    variable_name="STONEFANG_TUNNEL_2",
    verbose_name="Stonefang Tunnel (2-2)",
)
STONEFANG_TUNNEL_3 = Map(
    6,
    2,
    name="StonefangTunnel3",
    variable_name="STONEFANG_TUNNEL_3",
    verbose_name="Stonefang Tunnel (2-3)",
)
NORTHERN_LIMIT_1 = Map(
    7,
    0,
    name="NorthernLimit1",
    variable_name="NORTHERN_LIMIT_1",
    verbose_name="Northern Limit (1)",
)
NORTHERN_LIMIT_2 = Map(
    7,
    1,
    name="NorthernLimit2",
    variable_name="NORTHERN_LIMIT_2",
    verbose_name="Northern Limit (2)",
)
NORTHERN_LIMIT_3 = Map(
    7,
    2,
    name="NorthernLimit3",
    variable_name="NORTHERN_LIMIT_3",
    verbose_name="Northern Limit (3)",
)
TUTORIAL_1 = Map(
    8,
    0,
    name="Tutorial1",
    variable_name="TUTORIAL_1",
    verbose_name="Tutorial (1)",
)
TUTORIAL_2 = Map(
    8,
    1,
    name="Tutorial2",
    variable_name="TUTORIAL_2",
    verbose_name="Tutorial (2)",
)
TUTORIAL_3 = Map(
    8,
    2,
    name="Tutorial3",
    variable_name="TUTORIAL_3",
    verbose_name="Tutorial (3)",
)


ALL_MAPS = (
    COMMON,
    THE_NEXUS,
    BOLETARIAN_PALACE_1,
    BOLETARIAN_PALACE_2,
    BOLETARIAN_PALACE_3,
    BOLETARIAN_PALACE_4,
    SHRINE_OF_STORMS_CUT,
    SHRINE_OF_STORMS_1,
    SHRINE_OF_STORMS_2,
    SHRINE_OF_STORMS_3,
    TOWER_OF_LATRIA_1,
    TOWER_OF_LATRIA_2,
    TOWER_OF_LATRIA_3,
    VALLEY_OF_DEFILEMENT_1,
    VALLEY_OF_DEFILEMENT_2,
    VALLEY_OF_DEFILEMENT_3,
    STONEFANG_TUNNEL_1,
    STONEFANG_TUNNEL_2,
    STONEFANG_TUNNEL_3,
    NORTHERN_LIMIT_1,
    NORTHERN_LIMIT_2,
    NORTHERN_LIMIT_3,
    TUTORIAL_1,
    TUTORIAL_2,
    TUTORIAL_3,
)


def get_map(source: MAP_SOURCE_TYPING) -> Map:
    return _get_map_base(source, game_maps=ALL_MAPS)


def get_map_variable_name(source: MAP_SOURCE_TYPING):
    try:
        return get_map(source).variable_name
    except (KeyError, ValueError):
        try:
            area_id, block_id, cc_id, dd_id = source
        except ValueError:
            try:
                area_id, block_id = source
                cc_id = dd_id = 0
            except ValueError:
                raise ValueError(
                    f"Can only generate a variable name for an unknown map from source `(aa, bb, cc, dd)`, not: "
                    f"{repr(source)} of type {type(source)}"
                )
        return f"({area_id}, {block_id}, {cc_id}, {dd_id})"
