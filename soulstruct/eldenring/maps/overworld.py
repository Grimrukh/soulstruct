"""Maps of Elden Ring's "overworld", the Lands Between.

Complete map grid image: https://cdn.discordapp.com/attachments/944650430032519208/948525952261038101/mapcoords.jpg

Rules:
- All overworld maps have area 60, i.e., start with m60.
- Maps are shaped like tiles and come in three nested sizes: large, medium, and small.
- At any given position, you will be standing in one small, one medium, and one large tile.
- Large tiles contain four medium tiles and medium tiles contain four small tiles.
- Most enemies and interactable objects are in small tiles. Some larger enemies may be placed in large tiles.
- All Site of Grace objects/characters are placed in large tiles.
- Large tiles:
    - 'Block ID' is x coordinate, ranging left to right from 8 (west Liurnia) to 14 (slopes east of Mountaintops).
    - 'CC ID' is y coordinate, ranging bottom to top from 7 (Castle Morne) to 15 (Haligtree).
    - 'DD ID' is always 02.
- Medium tiles:
    - X (block) and Y (CC) IDs of the SW tile are double that of its parent large tile.
    - SE and NE tiles have +1 X relative to SW, and NW and NE tiles have +1 Y.
    - 'DD ID' is always 01.
- Small tiles:
    - Similarly, X and Y of the SW tile are double that of its parent medium tile.
    - Again, SE and NE tiles have +1 X relative to SW, and NW and NE tiles have +1 Y.
    - 'DD ID' is always 00.
- Maps use their own local coordinate system for MSB part positions, with (0,0) at the tile center.
- Small tiles have size 256x256 in-game units. Medium tile width is double that, and large tile quadruple.
"""
from __future__ import annotations

__all__ = [
    "MapTileException",
    "MapTile",
    "SOUTHWEST_LIURNIA",
    "SOUTHWEST_LIURNIA_SW",
    "SOUTHWEST_LIURNIA_SW_SE",
    "SOUTHWEST_LIURNIA_SW_NE",
    "SOUTHWEST_LIURNIA_NW",
    "SOUTHWEST_LIURNIA_NW_SE",
    "SOUTHWEST_LIURNIA_NW_NE",
    "SOUTHWEST_LIURNIA_SE",
    "SOUTHWEST_LIURNIA_SE_NW",
    "SOUTHWEST_LIURNIA_SE_NE",
    "SOUTHWEST_LIURNIA_NE",
    "SOUTHWEST_LIURNIA_NE_SW",
    "SOUTHWEST_LIURNIA_NE_NW",
    "SOUTHWEST_LIURNIA_NE_SE",
    "SOUTHWEST_LIURNIA_NE_NE",
    "WEST_LIURNIA",
    "WEST_LIURNIA_SW",
    "WEST_LIURNIA_SW_SE",
    "WEST_LIURNIA_SW_NE",
    "WEST_LIURNIA_NW",
    "WEST_LIURNIA_NW_SE",
    "WEST_LIURNIA_NW_NE",
    "WEST_LIURNIA_SE",
    "WEST_LIURNIA_SE_SW",
    "WEST_LIURNIA_SE_NW",
    "WEST_LIURNIA_SE_SE",
    "WEST_LIURNIA_SE_NE",
    "WEST_LIURNIA_NE",
    "WEST_LIURNIA_NE_SW",
    "WEST_LIURNIA_NE_NW",
    "WEST_LIURNIA_NE_SE",
    "WEST_LIURNIA_NE_NE",
    "NORTHWEST_LIURNIA",
    "NORTHWEST_LIURNIA_SE",
    "NORTHWEST_LIURNIA_SE_SW",
    "NORTHWEST_LIURNIA_SE_NW",
    "NORTHWEST_LIURNIA_SE_SE",
    "NORTHWEST_LIURNIA_SE_NE",
    "NORTHWEST_LIURNIA_NE",
    "NORTHWEST_LIURNIA_NE_SW",
    "NORTHWEST_LIURNIA_NE_NW",
    "NORTHWEST_LIURNIA_NE_SE",
    "NORTHWEST_LIURNIA_NE_NE",
    "FAR_WEST_ALTUS_PLATEAU",
    "FAR_WEST_ALTUS_PLATEAU_SE",
    "FAR_WEST_ALTUS_PLATEAU_SE_SE",
    "FAR_WEST_ALTUS_PLATEAU_SE_NE",
    "FAR_WEST_ALTUS_PLATEAU_NE",
    "FAR_WEST_ALTUS_PLATEAU_NE_SE",
    "FAR_WEST_LIMGRAVE",
    "FAR_WEST_LIMGRAVE_NE",
    "FAR_WEST_LIMGRAVE_NE_NW",
    "FAR_WEST_LIMGRAVE_NE_NE",
    "SOUTHEAST_LIURNIA",
    "SOUTHEAST_LIURNIA_SW",
    "SOUTHEAST_LIURNIA_SW_NW",
    "SOUTHEAST_LIURNIA_SW_NE",
    "SOUTHEAST_LIURNIA_NW",
    "SOUTHEAST_LIURNIA_NW_SW",
    "SOUTHEAST_LIURNIA_NW_NW",
    "SOUTHEAST_LIURNIA_NW_SE",
    "SOUTHEAST_LIURNIA_NW_NE",
    "SOUTHEAST_LIURNIA_SE",
    "SOUTHEAST_LIURNIA_SE_SW",
    "SOUTHEAST_LIURNIA_SE_NW",
    "SOUTHEAST_LIURNIA_SE_SE",
    "SOUTHEAST_LIURNIA_SE_NE",
    "SOUTHEAST_LIURNIA_NE",
    "SOUTHEAST_LIURNIA_NE_SW",
    "SOUTHEAST_LIURNIA_NE_NW",
    "SOUTHEAST_LIURNIA_NE_SE",
    "SOUTHEAST_LIURNIA_NE_NE",
    "EAST_LIURNIA",
    "EAST_LIURNIA_SW",
    "EAST_LIURNIA_SW_SW",
    "EAST_LIURNIA_SW_NW",
    "EAST_LIURNIA_SW_SE",
    "EAST_LIURNIA_SW_NE",
    "EAST_LIURNIA_NW",
    "EAST_LIURNIA_NW_SW",
    "EAST_LIURNIA_NW_NW",
    "EAST_LIURNIA_NW_SE",
    "EAST_LIURNIA_NW_NE",
    "EAST_LIURNIA_SE",
    "EAST_LIURNIA_SE_SW",
    "EAST_LIURNIA_SE_NW",
    "EAST_LIURNIA_SE_SE",
    "EAST_LIURNIA_SE_NE",
    "EAST_LIURNIA_NE",
    "EAST_LIURNIA_NE_SW",
    "EAST_LIURNIA_NE_NW",
    "EAST_LIURNIA_NE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU",
    "LIURNIA_TO_ALTUS_PLATEAU_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_NE",
    "WEST_ALTUS_PLATEAU",
    "WEST_ALTUS_PLATEAU_SW",
    "WEST_ALTUS_PLATEAU_SW_SW",
    "WEST_ALTUS_PLATEAU_SW_NW",
    "WEST_ALTUS_PLATEAU_SW_SE",
    "WEST_ALTUS_PLATEAU_SW_NE",
    "WEST_ALTUS_PLATEAU_NW",
    "WEST_ALTUS_PLATEAU_NW_SW",
    "WEST_ALTUS_PLATEAU_NW_SE",
    "WEST_ALTUS_PLATEAU_NW_NE",
    "WEST_ALTUS_PLATEAU_SE",
    "WEST_ALTUS_PLATEAU_SE_SW",
    "WEST_ALTUS_PLATEAU_SE_NW",
    "WEST_ALTUS_PLATEAU_SE_SE",
    "WEST_ALTUS_PLATEAU_SE_NE",
    "WEST_ALTUS_PLATEAU_NE",
    "WEST_ALTUS_PLATEAU_NE_SW",
    "WEST_ALTUS_PLATEAU_NE_SE",
    "SOUTH_WEEPING_PENINSULA",
    "SOUTH_WEEPING_PENINSULA_NE",
    "SOUTH_WEEPING_PENINSULA_NE_SE",
    "SOUTH_WEEPING_PENINSULA_NE_NE",
    "WEST_WEEPING_PENINSULA",
    "WEST_WEEPING_PENINSULA_SW",
    "WEST_WEEPING_PENINSULA_SW_NW",
    "WEST_WEEPING_PENINSULA_SW_SE",
    "WEST_WEEPING_PENINSULA_SW_NE",
    "WEST_WEEPING_PENINSULA_NW",
    "WEST_WEEPING_PENINSULA_NW_SE",
    "WEST_WEEPING_PENINSULA_NW_NE",
    "WEST_WEEPING_PENINSULA_SE",
    "WEST_WEEPING_PENINSULA_SE_SW",
    "WEST_WEEPING_PENINSULA_SE_NW",
    "WEST_WEEPING_PENINSULA_SE_SE",
    "WEST_WEEPING_PENINSULA_SE_NE",
    "WEST_WEEPING_PENINSULA_NE",
    "WEST_WEEPING_PENINSULA_NE_SW",
    "WEST_WEEPING_PENINSULA_NE_NW",
    "WEST_WEEPING_PENINSULA_NE_SE",
    "WEST_WEEPING_PENINSULA_NE_NE",
    "WEST_LIMGRAVE",
    "WEST_LIMGRAVE_SW",
    "WEST_LIMGRAVE_SW_SE",
    "WEST_LIMGRAVE_SW_NE",
    "WEST_LIMGRAVE_NW",
    "WEST_LIMGRAVE_NW_SW",
    "WEST_LIMGRAVE_NW_NW",
    "WEST_LIMGRAVE_NW_SE",
    "WEST_LIMGRAVE_NW_NE",
    "WEST_LIMGRAVE_SE",
    "WEST_LIMGRAVE_SE_SW",
    "WEST_LIMGRAVE_SE_NW",
    "WEST_LIMGRAVE_SE_SE",
    "WEST_LIMGRAVE_SE_NE",
    "WEST_LIMGRAVE_NE",
    "WEST_LIMGRAVE_NE_SW",
    "WEST_LIMGRAVE_NE_NW",
    "WEST_LIMGRAVE_NE_SE",
    "WEST_LIMGRAVE_NE_NE",
    "NORTHWEST_LIMGRAVE_COAST",
    "NORTHWEST_LIMGRAVE_COAST_SW",
    "NORTHWEST_LIMGRAVE_COAST_SW_SW",
    "NORTHWEST_LIMGRAVE_COAST_SE",
    "NORTHWEST_LIMGRAVE_COAST_SE_SW",
    "NORTHWEST_LIMGRAVE_COAST_SE_SE",
    "SOUTH_ALTUS_PLATEAU",
    "SOUTH_ALTUS_PLATEAU_NW",
    "SOUTH_ALTUS_PLATEAU_NW_SW",
    "SOUTH_ALTUS_PLATEAU_NW_NW",
    "SOUTH_ALTUS_PLATEAU_NW_SE",
    "SOUTH_ALTUS_PLATEAU_NW_NE",
    "SOUTH_ALTUS_PLATEAU_NE",
    "SOUTH_ALTUS_PLATEAU_NE_SW",
    "SOUTH_ALTUS_PLATEAU_NE_NW",
    "SOUTH_ALTUS_PLATEAU_NE_SE",
    "SOUTH_ALTUS_PLATEAU_NE_NE",
    "NORTH_ALTUS_PLATEAU",
    "NORTH_ALTUS_PLATEAU_SW",
    "NORTH_ALTUS_PLATEAU_SW_SW",
    "NORTH_ALTUS_PLATEAU_SW_NW",
    "NORTH_ALTUS_PLATEAU_SW_SE",
    "NORTH_ALTUS_PLATEAU_SW_NE",
    "NORTH_ALTUS_PLATEAU_NW",
    "NORTH_ALTUS_PLATEAU_NW_SW",
    "NORTH_ALTUS_PLATEAU_NW_NW",
    "NORTH_ALTUS_PLATEAU_NW_SE",
    "NORTH_ALTUS_PLATEAU_NW_NE",
    "NORTH_ALTUS_PLATEAU_SE",
    "NORTH_ALTUS_PLATEAU_SE_SW",
    "NORTH_ALTUS_PLATEAU_SE_NW",
    "NORTH_ALTUS_PLATEAU_SE_SE",
    "NORTH_ALTUS_PLATEAU_SE_NE",
    "NORTH_ALTUS_PLATEAU_NE",
    "NORTH_ALTUS_PLATEAU_NE_SW",
    "NORTH_ALTUS_PLATEAU_NE_NW",
    "NORTH_ALTUS_PLATEAU_NE_SE",
    "SOUTHEAST_WEEPING_PENINSULA_COAST",
    "SOUTHEAST_WEEPING_PENINSULA_COAST_NW",
    "SOUTHEAST_WEEPING_PENINSULA_COAST_NW_NW",
    "EAST_WEEPING_PENINSULA",
    "EAST_WEEPING_PENINSULA_SW",
    "EAST_WEEPING_PENINSULA_SW_SW",
    "EAST_WEEPING_PENINSULA_SW_NW",
    "EAST_WEEPING_PENINSULA_SW_SE",
    "EAST_WEEPING_PENINSULA_SW_NE",
    "EAST_WEEPING_PENINSULA_NW",
    "EAST_WEEPING_PENINSULA_NW_SW",
    "EAST_WEEPING_PENINSULA_NW_NW",
    "EAST_WEEPING_PENINSULA_NW_SE",
    "EAST_WEEPING_PENINSULA_NW_NE",
    "EAST_LIMGRAVE",
    "EAST_LIMGRAVE_SW",
    "EAST_LIMGRAVE_SW_SW",
    "EAST_LIMGRAVE_SW_NW",
    "EAST_LIMGRAVE_SW_SE",
    "EAST_LIMGRAVE_SW_NE",
    "EAST_LIMGRAVE_NW",
    "EAST_LIMGRAVE_NW_SW",
    "EAST_LIMGRAVE_NW_NW",
    "EAST_LIMGRAVE_NW_SE",
    "EAST_LIMGRAVE_NW_NE",
    "EAST_LIMGRAVE_SE",
    "EAST_LIMGRAVE_SE_SW",
    "EAST_LIMGRAVE_SE_NW",
    "EAST_LIMGRAVE_SE_NE",
    "EAST_LIMGRAVE_NE",
    "EAST_LIMGRAVE_NE_SW",
    "EAST_LIMGRAVE_NE_NW",
    "EAST_LIMGRAVE_NE_SE",
    "EAST_LIMGRAVE_NE_NE",
    "NORTHWEST_CAELID",
    "NORTHWEST_CAELID_SW",
    "NORTHWEST_CAELID_SW_SE",
    "NORTHWEST_CAELID_SE",
    "NORTHWEST_CAELID_SE_SW",
    "NORTHWEST_CAELID_SE_SE",
    "NORTHWEST_CAELID_SE_NE",
    "NORTHWEST_CAELID_NE",
    "NORTHWEST_CAELID_NE_SE",
    "SOUTHEAST_ALTUS_PLATEAU",
    "SOUTHEAST_ALTUS_PLATEAU_NW",
    "SOUTHEAST_ALTUS_PLATEAU_NW_NE",
    "SOUTHEAST_ALTUS_PLATEAU_NE",
    "SOUTHEAST_ALTUS_PLATEAU_NE_NE",
    "NORTHEAST_ALTUS_PLATEAU",
    "NORTHEAST_ALTUS_PLATEAU_SW",
    "NORTHEAST_ALTUS_PLATEAU_SW_SW",
    "NORTHEAST_ALTUS_PLATEAU_SW_NW",
    "NORTHEAST_ALTUS_PLATEAU_SW_SE",
    "NORTHEAST_ALTUS_PLATEAU_SW_NE",
    "NORTHEAST_ALTUS_PLATEAU_NE",
    "NORTHEAST_ALTUS_PLATEAU_NE_NW",
    "NORTHEAST_ALTUS_PLATEAU_NE_NE",
    "WEST_CONSECRATED_SNOWFIELD",
    "WEST_CONSECRATED_SNOWFIELD_SE",
    "WEST_CONSECRATED_SNOWFIELD_SE_NW",
    "WEST_CONSECRATED_SNOWFIELD_SE_SE",
    "WEST_CONSECRATED_SNOWFIELD_SE_NE",
    "WEST_CONSECRATED_SNOWFIELD_NE",
    "WEST_CONSECRATED_SNOWFIELD_NE_SE",
    "FAR_SOUTH_CAELID",
    "FAR_SOUTH_CAELID_NE",
    "FAR_SOUTH_CAELID_NE_NE",
    "SOUTH_CAELID",
    "SOUTH_CAELID_SW",
    "SOUTH_CAELID_SW_SW",
    "SOUTH_CAELID_SW_NW",
    "SOUTH_CAELID_SW_SE",
    "SOUTH_CAELID_SW_NE",
    "SOUTH_CAELID_NW",
    "SOUTH_CAELID_NW_SW",
    "SOUTH_CAELID_NW_NW",
    "SOUTH_CAELID_NW_SE",
    "SOUTH_CAELID_NW_NE",
    "SOUTH_CAELID_SE",
    "SOUTH_CAELID_SE_SW",
    "SOUTH_CAELID_SE_NW",
    "SOUTH_CAELID_SE_SE",
    "SOUTH_CAELID_SE_NE",
    "SOUTH_CAELID_NE",
    "SOUTH_CAELID_NE_SW",
    "SOUTH_CAELID_NE_NW",
    "SOUTH_CAELID_NE_SE",
    "SOUTH_CAELID_NE_NE",
    "NORTH_CAELID",
    "NORTH_CAELID_SW",
    "NORTH_CAELID_SW_SW",
    "NORTH_CAELID_SW_NW",
    "NORTH_CAELID_SW_SE",
    "NORTH_CAELID_SW_NE",
    "NORTH_CAELID_SE",
    "NORTH_CAELID_SE_SW",
    "NORTH_CAELID_SE_NW",
    "NORTH_CAELID_SE_SE",
    "NORTH_CAELID_SE_NE",
    "NORTH_CAELID_NE",
    "NORTH_CAELID_NE_SE",
    "NORTH_CAELID_NE_NE",
    "FORBIDDEN_LANDS",
    "FORBIDDEN_LANDS_NW",
    "FORBIDDEN_LANDS_NW_NW",
    "SOUTHWEST_MOUNTAINTOPS",
    "SOUTHWEST_MOUNTAINTOPS_SW",
    "SOUTHWEST_MOUNTAINTOPS_SW_SE",
    "SOUTHWEST_MOUNTAINTOPS_SW_NE",
    "SOUTHWEST_MOUNTAINTOPS_NW",
    "SOUTHWEST_MOUNTAINTOPS_NW_SW",
    "SOUTHWEST_MOUNTAINTOPS_NW_NW",
    "SOUTHWEST_MOUNTAINTOPS_NW_SE",
    "SOUTHWEST_MOUNTAINTOPS_NW_NE",
    "SOUTHWEST_MOUNTAINTOPS_SE",
    "SOUTHWEST_MOUNTAINTOPS_SE_NW",
    "SOUTHWEST_MOUNTAINTOPS_SE_SE",
    "SOUTHWEST_MOUNTAINTOPS_SE_NE",
    "SOUTHWEST_MOUNTAINTOPS_NE",
    "SOUTHWEST_MOUNTAINTOPS_NE_SW",
    "SOUTHWEST_MOUNTAINTOPS_NE_NW",
    "SOUTHWEST_MOUNTAINTOPS_NE_SE",
    "SOUTHWEST_MOUNTAINTOPS_NE_NE",
    "NORTHWEST_MOUNTAINTOPS",
    "NORTHWEST_MOUNTAINTOPS_SW",
    "NORTHWEST_MOUNTAINTOPS_SW_SW",
    "NORTHWEST_MOUNTAINTOPS_SW_NW",
    "NORTHWEST_MOUNTAINTOPS_SW_SE",
    "NORTHWEST_MOUNTAINTOPS_SW_NE",
    "NORTHWEST_MOUNTAINTOPS_NW",
    "NORTHWEST_MOUNTAINTOPS_NW_SW",
    "NORTHWEST_MOUNTAINTOPS_SE",
    "NORTHWEST_MOUNTAINTOPS_SE_SW",
    "NORTHWEST_MOUNTAINTOPS_SE_NW",
    "NORTHWEST_MOUNTAINTOPS_SE_SE",
    "NORTHWEST_MOUNTAINTOPS_SE_NE",
    "NORTHWEST_MOUNTAINTOPS_NE",
    "NORTHWEST_MOUNTAINTOPS_NE_SE",
    "SOUTHEAST_CAELID",
    "SOUTHEAST_CAELID_SW",
    "SOUTHEAST_CAELID_SW_NW",
    "SOUTHEAST_CAELID_NW",
    "SOUTHEAST_CAELID_NW_SW",
    "SOUTHEAST_CAELID_NW_NW",
    "SOUTHEAST_CAELID_NW_SE",
    "SOUTHEAST_CAELID_NW_NE",
    "NORTHEAST_CAELID",
    "NORTHEAST_CAELID_SW",
    "NORTHEAST_CAELID_SW_SW",
    "NORTHEAST_CAELID_SW_NW",
    "NORTHEAST_CAELID_NW",
    "NORTHEAST_CAELID_NW_SW",
    "NORTHEAST_CAELID_NW_NW",
    "SOUTHEAST_MOUNTAINTOPS",
    "SOUTHEAST_MOUNTAINTOPS_SW",
    "SOUTHEAST_MOUNTAINTOPS_SW_SW",
    "SOUTHEAST_MOUNTAINTOPS_SW_NW",
    "SOUTHEAST_MOUNTAINTOPS_SW_SE",
    "SOUTHEAST_MOUNTAINTOPS_SW_NE",
    "SOUTHEAST_MOUNTAINTOPS_NW",
    "SOUTHEAST_MOUNTAINTOPS_NW_SW",
    "SOUTHEAST_MOUNTAINTOPS_NW_NW",
    "SOUTHEAST_MOUNTAINTOPS_NW_SE",
    "SOUTHEAST_MOUNTAINTOPS_NW_NE",
    "SOUTHEAST_MOUNTAINTOPS_SE",
    "SOUTHEAST_MOUNTAINTOPS_SE_NW",
    "SOUTHEAST_MOUNTAINTOPS_NE",
    "SOUTHEAST_MOUNTAINTOPS_NE_NW",
    "NORTHEAST_MOUNTAINTOPS",
    "NORTHEAST_MOUNTAINTOPS_SW",
    "NORTHEAST_MOUNTAINTOPS_SW_SW",
    "NORTHEAST_MOUNTAINTOPS_SW_NW",
    "NORTHEAST_MOUNTAINTOPS_SW_SE",
    "NORTHEAST_MOUNTAINTOPS_SW_NE",
    "NORTHEAST_MOUNTAINTOPS_NW",
    "NORTHEAST_MOUNTAINTOPS_NW_SW",
    "NORTHEAST_MOUNTAINTOPS_NW_SE",
    "NORTHEAST_MOUNTAINTOPS_SE",
    "NORTHEAST_MOUNTAINTOPS_SE_SW",
    "NORTHEAST_MOUNTAINTOPS_SE_NW",
    "EAST_LIMGRAVE_METEOR",
    "EAST_LIMGRAVE_METEOR_SW",
    "EAST_LIMGRAVE_METEOR_SW_SE",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN_SW",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN_SW_SE",
]

from soulstruct.game_types.msb_types import Map
import typing as tp


class MapTileException(Exception):
    """Exception raised by an invalid X/Y coordinate for given size ID."""


class MapTile(Map):
    """Map subclass for Elden Ring that simplifies arguments and has references to parent tiles."""

    def __init__(
        self,
        x_id: int,
        y_id: int,
        size_id: int,
        name=None,
        emevd_file_stem=None,
        msb_file_stem=None,
        ai_file_stem=None,
        esd_file_stem=None,
        ffxbnd_file_name=None,
        variable_name=None,
        verbose_name=None,
        sites_of_grace=(),
        markers=(),
        parent_tile: tp.Optional[MapTile] = None,
        is_alternate=False,
    ):
        # Check X/Y validity.
        if x_id < 8 or x_id > 57:
            raise MapTileException(f"Map tile x = {x_id} is not valid for any map size.")
        if y_id < 7 or y_id > 63:
            raise MapTileException(f"Map tile y = {y_id} is not valid for any map size.")
        if size_id == 2:
            if not 8 <= x_id <= 14:
                raise MapTileException(f"Large tiles (02) cannot have x = {x_id}.")
            if not 7 <= y_id <= 15:
                raise MapTileException(f"Large tiles (02) cannot have y = {y_id}.")
        elif size_id == 1:
            if not 16 <= x_id <= 28:
                raise MapTileException(f"Medium tiles (01) cannot have x = {x_id}.")
            if not 15 <= y_id <= 31:
                raise MapTileException(f"Medium tiles (01) cannot have y = {y_id}.")
        elif size_id == 0:
            if not 32 <= x_id <= 57:
                raise MapTileException(f"Small tiles (00) cannot have x = {x_id}.")
            if not 30 <= y_id <= 63:
                raise MapTileException(f"Small tiles (00) cannot have y = {y_id}.")
        elif not is_alternate:
            raise MapTileException(f"Invalid tile size ID: {size_id}. Must be 2 (large), 1 (medium), or 0 (small).")

        # TODO: Can probably simplify stem arguments.
        super().__init__(
            area_id=60,
            block_id=x_id,
            cc_id=y_id,
            dd_id=size_id,
            name=name,
            emevd_file_stem=emevd_file_stem,
            msb_file_stem=msb_file_stem,
            ai_file_stem=ai_file_stem,
            esd_file_stem=esd_file_stem,
            ffxbnd_file_name=ffxbnd_file_name,
            variable_name=variable_name,
            verbose_name=verbose_name,
        )
        self.sites_of_grace = sites_of_grace
        self.markers = markers
        self.parent_tile = parent_tile


SOUTHWEST_LIURNIA = MapTile(  # LARGE
    8, 10, 2,
    name="SouthwestLiurnia",
    variable_name="SOUTHWEST_LIURNIA",
    verbose_name="Southwest Liurnia",
)
SOUTHWEST_LIURNIA_SW = MapTile(  # MEDIUM
    16, 20, 1,
    name="SouthwestLiurnia_SW",
    variable_name="SOUTHWEST_LIURNIA_SW",
    verbose_name="Southwest Liurnia (SW)",
    parent_tile=SOUTHWEST_LIURNIA,
)
SOUTHWEST_LIURNIA_SW_SE = MapTile(  # SMALL
    33, 40, 0,
    name="SouthwestLiurnia_SW_SE",
    variable_name="SOUTHWEST_LIURNIA_SW_SE",
    verbose_name="Southwest Liurnia (SW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Moonlight Altar - Altar South",
    ),
    markers=(
        "Chelona's Rise (Rise)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_SW,
)
SOUTHWEST_LIURNIA_SW_NE = MapTile(  # SMALL
    33, 41, 0,
    name="SouthwestLiurnia_SW_NE",
    variable_name="SOUTHWEST_LIURNIA_SW_NE",
    verbose_name="Southwest Liurnia (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_LIURNIA_SW,
)
SOUTHWEST_LIURNIA_NW = MapTile(  # MEDIUM
    16, 21, 1,
    name="SouthwestLiurnia_NW",
    variable_name="SOUTHWEST_LIURNIA_NW",
    verbose_name="Southwest Liurnia (NW)",
    parent_tile=SOUTHWEST_LIURNIA,
)
SOUTHWEST_LIURNIA_NW_SE = MapTile(  # SMALL
    33, 42, 0,
    name="SouthwestLiurnia_NW_SE",
    variable_name="SOUTHWEST_LIURNIA_NW_SE",
    verbose_name="Southwest Liurnia (NW) (SE)",
    sites_of_grace=(),
    markers=(
        "Ringleader's Evergaol (Evergaol)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_NW,
)
SOUTHWEST_LIURNIA_NW_NE = MapTile(  # SMALL
    33, 43, 0,
    name="SouthwestLiurnia_NW_NE",
    variable_name="SOUTHWEST_LIURNIA_NW_NE",
    verbose_name="Southwest Liurnia (NW) (NE)",
    sites_of_grace=(),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_NW,
)
SOUTHWEST_LIURNIA_SE = MapTile(  # MEDIUM
    17, 20, 1,
    name="SouthwestLiurnia_SE",
    variable_name="SOUTHWEST_LIURNIA_SE",
    verbose_name="Southwest Liurnia (SE)",
    parent_tile=SOUTHWEST_LIURNIA,
)
SOUTHWEST_LIURNIA_SE_NW = MapTile(  # SMALL
    34, 41, 0,
    name="SouthwestLiurnia_SE_NW",
    variable_name="SOUTHWEST_LIURNIA_SE_NW",
    verbose_name="Southwest Liurnia (SE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Moonlight Altar - Moonlight Altar",
    ),
    markers=(
        "Deep Ainsel Well (Well)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_SE,
)
SOUTHWEST_LIURNIA_SE_NE = MapTile(  # SMALL
    35, 41, 0,
    name="SouthwestLiurnia_SE_NE",
    variable_name="SOUTHWEST_LIURNIA_SE_NE",
    verbose_name="Southwest Liurnia (SE) (NE)",
    sites_of_grace=(),
    markers=(
        "Lunar Estate Ruins (Ruins)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_SE,
)
SOUTHWEST_LIURNIA_NE = MapTile(  # MEDIUM
    17, 21, 1,
    name="SouthwestLiurnia_NE",
    variable_name="SOUTHWEST_LIURNIA_NE",
    verbose_name="Southwest Liurnia (NE)",
    parent_tile=SOUTHWEST_LIURNIA,
)
SOUTHWEST_LIURNIA_NE_SW = MapTile(  # SMALL
    34, 42, 0,
    name="SouthwestLiurnia_NE_SW",
    variable_name="SOUTHWEST_LIURNIA_NE_SW",
    verbose_name="Southwest Liurnia (NE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Village of the Albinaurics",
    ),
    markers=(
        "Moonfolk Ruins (Ruins)"
        "Village of the Albinaurics (Unique)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_NE,
)
SOUTHWEST_LIURNIA_NE_NW = MapTile(  # SMALL
    34, 43, 0,
    name="SouthwestLiurnia_NE_NW",
    variable_name="SOUTHWEST_LIURNIA_NE_NW",
    verbose_name="Southwest Liurnia (NE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Converted Tower",
    ),
    markers=(
        "Converted Tower (Rise)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_NE,
)
SOUTHWEST_LIURNIA_NE_SE = MapTile(  # SMALL
    35, 42, 0,
    name="SouthwestLiurnia_NE_SE",
    variable_name="SOUTHWEST_LIURNIA_NE_SE",
    verbose_name="Southwest Liurnia (NE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Moonlight Altar - Cathedral of Manus Celes",
    ),
    markers=(
        "Cathedral of Manus Celes (Unique)",
    ),
    parent_tile=SOUTHWEST_LIURNIA_NE,
)
SOUTHWEST_LIURNIA_NE_NE = MapTile(  # SMALL
    35, 43, 0,
    name="SouthwestLiurnia_NE_NE",
    variable_name="SOUTHWEST_LIURNIA_NE_NE",
    verbose_name="Southwest Liurnia (NE) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Folly on the Lake",
    ),
    markers=(),
    parent_tile=SOUTHWEST_LIURNIA_NE,
)

WEST_LIURNIA = MapTile(  # LARGE
    8, 11, 2,
    name="WestLiurnia",
    variable_name="WEST_LIURNIA",
    verbose_name="West Liurnia",
)
WEST_LIURNIA_SW = MapTile(  # MEDIUM
    16, 22, 1,
    name="WestLiurnia_SW",
    variable_name="WEST_LIURNIA_SW",
    verbose_name="West Liurnia (SW)",
    parent_tile=WEST_LIURNIA,
)
WEST_LIURNIA_SW_SE = MapTile(  # SMALL
    33, 44, 0,
    name="WestLiurnia_SW_SE",
    variable_name="WEST_LIURNIA_SW_SE",
    verbose_name="West Liurnia (SW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Revenger's Shack",
    ),
    markers=(
        "Revenger's Shack (Shack)",
    ),
    parent_tile=WEST_LIURNIA_SW,
)
WEST_LIURNIA_SW_NE = MapTile(  # SMALL
    33, 45, 0,
    name="WestLiurnia_SW_NE",
    variable_name="WEST_LIURNIA_SW_NE",
    verbose_name="West Liurnia (SW) (NE)",
    sites_of_grace=(),
    markers=(
        "Cuckoo's Evergaol (Evergaol)",
    ),
    parent_tile=WEST_LIURNIA_SW,
)
WEST_LIURNIA_NW = MapTile(  # MEDIUM
    16, 23, 1,
    name="WestLiurnia_NW",
    variable_name="WEST_LIURNIA_NW",
    verbose_name="West Liurnia (NW)",
    parent_tile=WEST_LIURNIA,
)
WEST_LIURNIA_NW_SE = MapTile(  # SMALL
    33, 46, 0,
    name="WestLiurnia_NW_SE",
    variable_name="WEST_LIURNIA_NW_SE",
    verbose_name="West Liurnia (NW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Foot of the Four Belfries",
    ),
    markers=(),
    parent_tile=WEST_LIURNIA_NW,
)
WEST_LIURNIA_NW_NE = MapTile(  # SMALL
    33, 47, 0,
    name="WestLiurnia_NW_NE",
    variable_name="WEST_LIURNIA_NW_NE",
    verbose_name="West Liurnia (NW) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - The Four Belfries",
    ),
    markers=(
        "The Four Belfries (Unique)",
    ),
    parent_tile=WEST_LIURNIA_NW,
)
WEST_LIURNIA_SE = MapTile(  # MEDIUM
    17, 22, 1,
    name="WestLiurnia_SE",
    variable_name="WEST_LIURNIA_SE",
    verbose_name="West Liurnia (SE)",
    parent_tile=WEST_LIURNIA,
)
WEST_LIURNIA_SE_SW = MapTile(  # SMALL
    34, 44, 0,
    name="WestLiurnia_SE_SW",
    variable_name="WEST_LIURNIA_SE_SW",
    verbose_name="West Liurnia (SE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Temple Quarter",
    ),
    markers=(
        "Temple Quarter (Lake Town)",
    ),
    parent_tile=WEST_LIURNIA_SE,
)
WEST_LIURNIA_SE_NW = MapTile(  # SMALL
    34, 45, 0,
    name="WestLiurnia_SE_NW",
    variable_name="WEST_LIURNIA_SE_NW",
    verbose_name="West Liurnia (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIURNIA_SE,
)
WEST_LIURNIA_SE_SE = MapTile(  # SMALL
    35, 44, 0,
    name="WestLiurnia_SE_SE",
    variable_name="WEST_LIURNIA_SE_SE",
    verbose_name="West Liurnia (SE) (SE)",
    sites_of_grace=(),
    markers=(
        "Rose Church (Church)",
    ),
    parent_tile=WEST_LIURNIA_SE,
)
WEST_LIURNIA_SE_NE = MapTile(  # SMALL
    35, 45, 0,
    name="WestLiurnia_SE_NE",
    variable_name="WEST_LIURNIA_SE_NE",
    verbose_name="West Liurnia (SE) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - South Raya Lucaria Gate",
    ),
    markers=(),
    parent_tile=WEST_LIURNIA_SE,
)
WEST_LIURNIA_NE = MapTile(  # MEDIUM
    17, 23, 1,
    name="WestLiurnia_NE",
    variable_name="WEST_LIURNIA_NE",
    verbose_name="West Liurnia (NE)",
    parent_tile=WEST_LIURNIA,
)
WEST_LIURNIA_NE_SW = MapTile(  # SMALL
    34, 46, 0,
    name="WestLiurnia_NE_SW",
    variable_name="WEST_LIURNIA_NE_SW",
    verbose_name="West Liurnia (NE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Crystalline Woods",
    ),
    markers=(),
    parent_tile=WEST_LIURNIA_NE,
)
WEST_LIURNIA_NE_NW = MapTile(  # SMALL
    34, 47, 0,
    name="WestLiurnia_NE_NW",
    variable_name="WEST_LIURNIA_NE_NW",
    verbose_name="West Liurnia (NE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Sorcerer's Isle",
    ),
    markers=(),
    parent_tile=WEST_LIURNIA_NE,
)
WEST_LIURNIA_NE_SE = MapTile(  # SMALL
    35, 46, 0,
    name="WestLiurnia_NE_SE",
    variable_name="WEST_LIURNIA_NE_SE",
    verbose_name="West Liurnia (NE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Main Academy Gate",
    ),
    markers=(),
    parent_tile=WEST_LIURNIA_NE,
)
WEST_LIURNIA_NE_NE = MapTile(  # SMALL
    35, 47, 0,
    name="WestLiurnia_NE_NE",
    variable_name="WEST_LIURNIA_NE_NE",
    verbose_name="West Liurnia (NE) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - East Gate Bridge Trestle",
    ),
    markers=(
        "Testu's Rise (Rise)",
    ),
    parent_tile=WEST_LIURNIA_NE,
)

NORTHWEST_LIURNIA = MapTile(  # LARGE
    8, 12, 2,
    name="NorthwestLiurnia",
    variable_name="NORTHWEST_LIURNIA",
    verbose_name="Northwest Liurnia",
)
NORTHWEST_LIURNIA_SE = MapTile(  # MEDIUM
    17, 24, 1,
    name="NorthwestLiurnia_SE",
    variable_name="NORTHWEST_LIURNIA_SE",
    verbose_name="Northwest Liurnia (SE)",
    parent_tile=NORTHWEST_LIURNIA,
)
NORTHWEST_LIURNIA_SE_SW = MapTile(  # SMALL
    34, 48, 0,
    name="NorthwestLiurnia_SE_SW",
    variable_name="NORTHWEST_LIURNIA_SE_SW",
    verbose_name="Northwest Liurnia (SE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Northern Liurnia Lake Shore",
    ),
    markers=(
        "Kingsrealm Ruins (Ruins)",
    ),
    parent_tile=NORTHWEST_LIURNIA_SE,
)
NORTHWEST_LIURNIA_SE_NW = MapTile(  # SMALL
    34, 49, 0,
    name="NorthwestLiurnia_SE_NW",
    variable_name="NORTHWEST_LIURNIA_SE_NW",
    verbose_name="Northwest Liurnia (SE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Road to the Manor",
    ),
    markers=(),
    parent_tile=NORTHWEST_LIURNIA_SE,
)
NORTHWEST_LIURNIA_SE_SE = MapTile(  # SMALL
    35, 48, 0,
    name="NorthwestLiurnia_SE_SE",
    variable_name="NORTHWEST_LIURNIA_SE_SE",
    verbose_name="Northwest Liurnia (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_LIURNIA_SE,
)
NORTHWEST_LIURNIA_SE_NE = MapTile(  # SMALL
    35, 49, 0,
    name="NorthwestLiurnia_SE_NE",
    variable_name="NORTHWEST_LIURNIA_SE_NE",
    verbose_name="Northwest Liurnia (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_LIURNIA_SE,
)
NORTHWEST_LIURNIA_NE = MapTile(  # MEDIUM
    17, 25, 1,
    name="NorthwestLiurnia_NE",
    variable_name="NORTHWEST_LIURNIA_NE",
    verbose_name="Northwest Liurnia (NE)",
    parent_tile=NORTHWEST_LIURNIA,
)
NORTHWEST_LIURNIA_NE_SW = MapTile(  # SMALL
    34, 50, 0,
    name="NorthwestLiurnia_NE_SW",
    variable_name="NORTHWEST_LIURNIA_NE_SW",
    verbose_name="Northwest Liurnia (NE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Ranni's Rise"
        "Liurnia of the Lakes - Ranni's Chamber",
    ),
    markers=(
        "Seluvis's Rise (Rise)"
        "Ranni's Rise (Rise)",
    ),
    parent_tile=NORTHWEST_LIURNIA_NE,
)
NORTHWEST_LIURNIA_NE_NW = MapTile(  # SMALL
    34, 51, 0,
    name="NorthwestLiurnia_NE_NW",
    variable_name="NORTHWEST_LIURNIA_NE_NW",
    verbose_name="Northwest Liurnia (NE) (NW)",
    sites_of_grace=(),
    markers=(
        "Renna's Rise (Rise)",
    ),
    parent_tile=NORTHWEST_LIURNIA_NE,
)
NORTHWEST_LIURNIA_NE_SE = MapTile(  # SMALL
    35, 50, 0,
    name="NorthwestLiurnia_NE_SE",
    variable_name="NORTHWEST_LIURNIA_NE_SE",
    verbose_name="Northwest Liurnia (NE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Main Caria Manor Gate"
        "Liurnia of the Lakes - Manor Upper Level"
        "Liurnia of the Lakes - Manor Lower Level"
        "Liurnia of the Lakes - Royal Moongazing Grounds",
    ),
    markers=(
        "Caria Manor (Unique)",
    ),
    parent_tile=NORTHWEST_LIURNIA_NE,
)
NORTHWEST_LIURNIA_NE_NE = MapTile(  # SMALL
    35, 51, 0,
    name="NorthwestLiurnia_NE_NE",
    variable_name="NORTHWEST_LIURNIA_NE_NE",
    verbose_name="Northwest Liurnia (NE) (NE)",
    sites_of_grace=(),
    markers=(
        "Three Sisters (Other)",
    ),
    parent_tile=NORTHWEST_LIURNIA_NE,
)

FAR_WEST_ALTUS_PLATEAU = MapTile(  # LARGE
    8, 13, 2,
    name="FarWestAltusPlateau",
    variable_name="FAR_WEST_ALTUS_PLATEAU",
    verbose_name="Far West Altus Plateau",
)
FAR_WEST_ALTUS_PLATEAU_SE = MapTile(  # MEDIUM
    17, 26, 1,
    name="FarWestAltusPlateau_SE",
    variable_name="FAR_WEST_ALTUS_PLATEAU_SE",
    verbose_name="Far West Altus Plateau (SE)",
    parent_tile=FAR_WEST_ALTUS_PLATEAU,
)
FAR_WEST_ALTUS_PLATEAU_SE_SE = MapTile(  # SMALL
    35, 52, 0,
    name="FarWestAltusPlateau_SE_SE",
    variable_name="FAR_WEST_ALTUS_PLATEAU_SE_SE",
    verbose_name="Far West Altus Plateau (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=FAR_WEST_ALTUS_PLATEAU_SE,
)
FAR_WEST_ALTUS_PLATEAU_SE_NE = MapTile(  # SMALL
    35, 53, 0,
    name="FarWestAltusPlateau_SE_NE",
    variable_name="FAR_WEST_ALTUS_PLATEAU_SE_NE",
    verbose_name="Far West Altus Plateau (SE) (NE)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Seethewater Terminus",
    ),
    markers=(),
    parent_tile=FAR_WEST_ALTUS_PLATEAU_SE,
)
FAR_WEST_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    17, 27, 1,
    name="FarWestAltusPlateau_NE",
    variable_name="FAR_WEST_ALTUS_PLATEAU_NE",
    verbose_name="Far West Altus Plateau (NE)",
    parent_tile=FAR_WEST_ALTUS_PLATEAU,
)
FAR_WEST_ALTUS_PLATEAU_NE_SE = MapTile(  # SMALL
    35, 54, 0,
    name="FarWestAltusPlateau_NE_SE",
    variable_name="FAR_WEST_ALTUS_PLATEAU_NE_SE",
    verbose_name="Far West Altus Plateau (NE) (SE)",
    sites_of_grace=(),
    markers=(
        "Fort Laiedd (Fort)",
    ),
    parent_tile=FAR_WEST_ALTUS_PLATEAU_NE,
)

FAR_WEST_LIMGRAVE = MapTile(  # LARGE
    9, 9, 2,
    name="FarWestLimgrave",
    variable_name="FAR_WEST_LIMGRAVE",
    verbose_name="Far West Limgrave",
)
FAR_WEST_LIMGRAVE_NE = MapTile(  # MEDIUM
    19, 19, 1,
    name="FarWestLimgrave_NE",
    variable_name="FAR_WEST_LIMGRAVE_NE",
    verbose_name="Far West Limgrave (NE)",
    parent_tile=FAR_WEST_LIMGRAVE,
)
FAR_WEST_LIMGRAVE_NE_NW = MapTile(  # SMALL
    38, 39, 0,
    name="FarWestLimgrave_NE_NW",
    variable_name="FAR_WEST_LIMGRAVE_NE_NW",
    verbose_name="Far West Limgrave (NE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=FAR_WEST_LIMGRAVE_NE,
)
FAR_WEST_LIMGRAVE_NE_NE = MapTile(  # SMALL
    39, 39, 0,
    name="FarWestLimgrave_NE_NE",
    variable_name="FAR_WEST_LIMGRAVE_NE_NE",
    verbose_name="Far West Limgrave (NE) (NE)",
    sites_of_grace=(),
    markers=(
        "Church of Irith (Church)",
    ),
    parent_tile=FAR_WEST_LIMGRAVE_NE,
)

SOUTHEAST_LIURNIA = MapTile(  # LARGE
    9, 10, 2,
    name="SoutheastLiurnia",
    variable_name="SOUTHEAST_LIURNIA",
    verbose_name="Southeast Liurnia",
)
SOUTHEAST_LIURNIA_SW = MapTile(  # MEDIUM
    18, 20, 1,
    name="SoutheastLiurnia_SW",
    variable_name="SOUTHEAST_LIURNIA_SW",
    verbose_name="Southeast Liurnia (SW)",
    parent_tile=SOUTHEAST_LIURNIA,
)
SOUTHEAST_LIURNIA_SW_NW = MapTile(  # SMALL
    36, 41, 0,
    name="SoutheastLiurnia_SW_NW",
    variable_name="SOUTHEAST_LIURNIA_SW_NW",
    verbose_name="Southeast Liurnia (SW) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Slumbering Wolf's Shack",
    ),
    markers=(
        "Slumbering Wolf's Shack (Shack)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_SW,
)
SOUTHEAST_LIURNIA_SW_NE = MapTile(  # SMALL
    37, 41, 0,
    name="SoutheastLiurnia_SW_NE",
    variable_name="SOUTHEAST_LIURNIA_SW_NE",
    verbose_name="Southeast Liurnia (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_SW,
)
SOUTHEAST_LIURNIA_NW = MapTile(  # MEDIUM
    18, 21, 1,
    name="SoutheastLiurnia_NW",
    variable_name="SOUTHEAST_LIURNIA_NW",
    verbose_name="Southeast Liurnia (NW)",
    parent_tile=SOUTHEAST_LIURNIA,
)
SOUTHEAST_LIURNIA_NW_SW = MapTile(  # SMALL
    36, 42, 0,
    name="SoutheastLiurnia_NW_SW",
    variable_name="SOUTHEAST_LIURNIA_NW_SW",
    verbose_name="Southeast Liurnia (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_NW,
)
SOUTHEAST_LIURNIA_NW_NW = MapTile(  # SMALL
    36, 43, 0,
    name="SoutheastLiurnia_NW_NW",
    variable_name="SOUTHEAST_LIURNIA_NW_NW",
    verbose_name="Southeast Liurnia (NW) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Boilprawn Shack"
        "Liurnia of the Lakes - Fallen Ruins of the Lake",
    ),
    markers=(
        "Boilprawn Shack (Shack)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_NW,
)
SOUTHEAST_LIURNIA_NW_SE = MapTile(  # SMALL
    37, 42, 0,
    name="SoutheastLiurnia_NW_SE",
    variable_name="SOUTHEAST_LIURNIA_NW_SE",
    verbose_name="Southeast Liurnia (NW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Scenic Isle",
    ),
    markers=(
        "Laskyar Ruins (Ruins)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_NW,
)
SOUTHEAST_LIURNIA_NW_NE = MapTile(  # SMALL
    37, 43, 0,
    name="SoutheastLiurnia_NW_NE",
    variable_name="SOUTHEAST_LIURNIA_NW_NE",
    verbose_name="Southeast Liurnia (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_NW,
)
SOUTHEAST_LIURNIA_SE = MapTile(  # MEDIUM
    19, 20, 1,
    name="SoutheastLiurnia_SE",
    variable_name="SOUTHEAST_LIURNIA_SE",
    verbose_name="Southeast Liurnia (SE)",
    parent_tile=SOUTHEAST_LIURNIA,
)
SOUTHEAST_LIURNIA_SE_SW = MapTile(  # SMALL
    38, 40, 0,
    name="SoutheastLiurnia_SE_SW",
    variable_name="SOUTHEAST_LIURNIA_SE_SW",
    verbose_name="Southeast Liurnia (SE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Liurnia Lake Shore",
    ),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_SE,
)
SOUTHEAST_LIURNIA_SE_NW = MapTile(  # SMALL
    38, 41, 0,
    name="SoutheastLiurnia_SE_NW",
    variable_name="SOUTHEAST_LIURNIA_SE_NW",
    verbose_name="Southeast Liurnia (SE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Laskyar Ruins",
    ),
    markers=(
        "Malefactor's Evergaol (Evergaol)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_SE,
)
SOUTHEAST_LIURNIA_SE_SE = MapTile(  # SMALL
    39, 40, 0,
    name="SoutheastLiurnia_SE_SE",
    variable_name="SOUTHEAST_LIURNIA_SE_SE",
    verbose_name="Southeast Liurnia (SE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Lake-Facing Cliffs",
    ),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_SE,
)
SOUTHEAST_LIURNIA_SE_NE = MapTile(  # SMALL
    39, 41, 0,
    name="SoutheastLiurnia_SE_NE",
    variable_name="SOUTHEAST_LIURNIA_SE_NE",
    verbose_name="Southeast Liurnia (SE) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Liurnia Highway South",
    ),
    markers=(
        "Purified Ruins (Ruins)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_SE,
)
SOUTHEAST_LIURNIA_NE = MapTile(  # MEDIUM
    19, 21, 1,
    name="SoutheastLiurnia_NE",
    variable_name="SOUTHEAST_LIURNIA_NE",
    verbose_name="Southeast Liurnia (NE)",
    parent_tile=SOUTHEAST_LIURNIA,
)
SOUTHEAST_LIURNIA_NE_SW = MapTile(  # SMALL
    38, 42, 0,
    name="SoutheastLiurnia_NE_SW",
    variable_name="SOUTHEAST_LIURNIA_NE_SW",
    verbose_name="Southeast Liurnia (NE) (SW)",
    sites_of_grace=(),
    markers=(
        "Highway Lookout Tower (Tower)",
    ),
    parent_tile=SOUTHEAST_LIURNIA_NE,
)
SOUTHEAST_LIURNIA_NE_NW = MapTile(  # SMALL
    38, 43, 0,
    name="SoutheastLiurnia_NE_NW",
    variable_name="SOUTHEAST_LIURNIA_NE_NW",
    verbose_name="Southeast Liurnia (NE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Gate Town Bridge",
    ),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_NE,
)
SOUTHEAST_LIURNIA_NE_SE = MapTile(  # SMALL
    39, 42, 0,
    name="SoutheastLiurnia_NE_SE",
    variable_name="SOUTHEAST_LIURNIA_NE_SE",
    verbose_name="Southeast Liurnia (NE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Liurnia Highway North",
    ),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_NE,
)
SOUTHEAST_LIURNIA_NE_NE = MapTile(  # SMALL
    39, 43, 0,
    name="SoutheastLiurnia_NE_NE",
    variable_name="SOUTHEAST_LIURNIA_NE_NE",
    verbose_name="Southeast Liurnia (NE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_LIURNIA_NE,
)

EAST_LIURNIA = MapTile(  # LARGE
    9, 11, 2,
    name="EastLiurnia",
    variable_name="EAST_LIURNIA",
    verbose_name="East Liurnia",
)
EAST_LIURNIA_SW = MapTile(  # MEDIUM
    18, 22, 1,
    name="EastLiurnia_SW",
    variable_name="EAST_LIURNIA_SW",
    verbose_name="East Liurnia (SW)",
    parent_tile=EAST_LIURNIA,
)
EAST_LIURNIA_SW_SW = MapTile(  # SMALL
    36, 44, 0,
    name="EastLiurnia_SW_SW",
    variable_name="EAST_LIURNIA_SW_SW",
    verbose_name="East Liurnia (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_SW,
)
EAST_LIURNIA_SW_NW = MapTile(  # SMALL
    36, 45, 0,
    name="EastLiurnia_SW_NW",
    variable_name="EAST_LIURNIA_SW_NW",
    verbose_name="East Liurnia (SW) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Gate Town North",
    ),
    markers=(),
    parent_tile=EAST_LIURNIA_SW,
)
EAST_LIURNIA_SW_SE = MapTile(  # SMALL
    37, 44, 0,
    name="EastLiurnia_SW_SE",
    variable_name="EAST_LIURNIA_SW_SE",
    verbose_name="East Liurnia (SW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Academy Gate Town",
    ),
    markers=(
        "Academy Gate Town (Lake Town)",
    ),
    parent_tile=EAST_LIURNIA_SW,
)
EAST_LIURNIA_SW_NE = MapTile(  # SMALL
    37, 45, 0,
    name="EastLiurnia_SW_NE",
    variable_name="EAST_LIURNIA_SW_NE",
    verbose_name="East Liurnia (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_SW,
)
EAST_LIURNIA_NW = MapTile(  # MEDIUM
    18, 23, 1,
    name="EastLiurnia_NW",
    variable_name="EAST_LIURNIA_NW",
    verbose_name="East Liurnia (NW)",
    parent_tile=EAST_LIURNIA,
)
EAST_LIURNIA_NW_SW = MapTile(  # SMALL
    36, 46, 0,
    name="EastLiurnia_NW_SW",
    variable_name="EAST_LIURNIA_NW_SW",
    verbose_name="East Liurnia (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_NW,
)
EAST_LIURNIA_NW_NW = MapTile(  # SMALL
    36, 47, 0,
    name="EastLiurnia_NW_NW",
    variable_name="EAST_LIURNIA_NW_NW",
    verbose_name="East Liurnia (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_NW,
)
EAST_LIURNIA_NW_SE = MapTile(  # SMALL
    37, 46, 0,
    name="EastLiurnia_NW_SE",
    variable_name="EAST_LIURNIA_NW_SE",
    verbose_name="East Liurnia (NW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Church of Vows",
    ),
    markers=(
        "Church of Vows (Church)",
    ),
    parent_tile=EAST_LIURNIA_NW,
)
EAST_LIURNIA_NW_NE = MapTile(  # SMALL
    37, 47, 0,
    name="EastLiurnia_NW_NE",
    variable_name="EAST_LIURNIA_NW_NE",
    verbose_name="East Liurnia (NW) (NE)",
    sites_of_grace=(),
    markers=(
        "Raya Lucaria Crystal Tunnel (Tunnel)",
    ),
    parent_tile=EAST_LIURNIA_NW,
)
EAST_LIURNIA_SE = MapTile(  # MEDIUM
    19, 22, 1,
    name="EastLiurnia_SE",
    variable_name="EAST_LIURNIA_SE",
    verbose_name="East Liurnia (SE)",
    parent_tile=EAST_LIURNIA,
)
EAST_LIURNIA_SE_SW = MapTile(  # SMALL
    38, 44, 0,
    name="EastLiurnia_SE_SW",
    variable_name="EAST_LIURNIA_SE_SW",
    verbose_name="East Liurnia (SE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_SE,
)
EAST_LIURNIA_SE_NW = MapTile(  # SMALL
    38, 45, 0,
    name="EastLiurnia_SE_NW",
    variable_name="EAST_LIURNIA_SE_NW",
    verbose_name="East Liurnia (SE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Artist's Shack"
        "Liurnia of the Lakes - Eastern Liurnia Lake Shore",
    ),
    markers=(
        "Artist's Shack (Shack)",
    ),
    parent_tile=EAST_LIURNIA_SE,
)
EAST_LIURNIA_SE_SE = MapTile(  # SMALL
    39, 44, 0,
    name="EastLiurnia_SE_SE",
    variable_name="EAST_LIURNIA_SE_SE",
    verbose_name="East Liurnia (SE) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Jarburg",
    ),
    markers=(
        "Jarburg (Unique)",
    ),
    parent_tile=EAST_LIURNIA_SE,
)
EAST_LIURNIA_SE_NE = MapTile(  # SMALL
    39, 45, 0,
    name="EastLiurnia_SE_NE",
    variable_name="EAST_LIURNIA_SE_NE",
    verbose_name="East Liurnia (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_SE,
)
EAST_LIURNIA_NE = MapTile(  # MEDIUM
    19, 23, 1,
    name="EastLiurnia_NE",
    variable_name="EAST_LIURNIA_NE",
    verbose_name="East Liurnia (NE)",
    parent_tile=EAST_LIURNIA,
)
EAST_LIURNIA_NE_SW = MapTile(  # SMALL
    38, 46, 0,
    name="EastLiurnia_NE_SW",
    variable_name="EAST_LIURNIA_NE_SW",
    verbose_name="East Liurnia (NE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Eastern Tableland",
    ),
    markers=(
        "Ainsel River Well (Well)",
    ),
    parent_tile=EAST_LIURNIA_NE,
)
EAST_LIURNIA_NE_NW = MapTile(  # SMALL
    38, 47, 0,
    name="EastLiurnia_NE_NW",
    variable_name="EAST_LIURNIA_NE_NW",
    verbose_name="East Liurnia (NE) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Ruined Labyrinth",
    ),
    markers=(
        "Uld Palace Ruins (Other)",
    ),
    parent_tile=EAST_LIURNIA_NE,
)
EAST_LIURNIA_NE_SE = MapTile(  # SMALL
    39, 46, 0,
    name="EastLiurnia_NE_SE",
    variable_name="EAST_LIURNIA_NE_SE",
    verbose_name="East Liurnia (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIURNIA_NE,
)

LIURNIA_TO_ALTUS_PLATEAU = MapTile(  # LARGE
    9, 12, 2,
    name="LiurniaToAltusPlateau",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU",
    verbose_name="Liurnia to Altus Plateau",
)
LIURNIA_TO_ALTUS_PLATEAU_SW = MapTile(  # MEDIUM
    18, 24, 1,
    name="LiurniaToAltusPlateau_SW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SW",
    verbose_name="Liurnia to Altus Plateau (SW)",
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU,
)
LIURNIA_TO_ALTUS_PLATEAU_SW_SW = MapTile(  # SMALL
    36, 48, 0,
    name="LiurniaToAltusPlateau_SW_SW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SW_SW",
    verbose_name="Liurnia to Altus Plateau (SW) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Bellum Highway - East Raya Lucaria Gate",
    ),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SW,
)
LIURNIA_TO_ALTUS_PLATEAU_SW_NW = MapTile(  # SMALL
    36, 49, 0,
    name="LiurniaToAltusPlateau_SW_NW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SW_NW",
    verbose_name="Liurnia to Altus Plateau (SW) (NW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Bellum Highway - Bellum Church"
        "Liurnia of the Lakes - The Ravine",
    ),
    markers=(
        "Bellum Church (Church)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SW,
)
LIURNIA_TO_ALTUS_PLATEAU_SW_SE = MapTile(  # SMALL
    37, 48, 0,
    name="LiurniaToAltusPlateau_SW_SE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SW_SE",
    verbose_name="Liurnia to Altus Plateau (SW) (SE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Mausoleum Compound",
    ),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SW,
)
LIURNIA_TO_ALTUS_PLATEAU_SW_NE = MapTile(  # SMALL
    37, 49, 0,
    name="LiurniaToAltusPlateau_SW_NE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SW_NE",
    verbose_name="Liurnia to Altus Plateau (SW) (NE)",
    sites_of_grace=(
        "Liurnia of the Lakes - Bellum Highway - Church of Inhibition",
    ),
    markers=(
        "Church of Inhibition (Church)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SW,
)
LIURNIA_TO_ALTUS_PLATEAU_NW = MapTile(  # MEDIUM
    18, 25, 1,
    name="LiurniaToAltusPlateau_NW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NW",
    verbose_name="Liurnia to Altus Plateau (NW)",
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU,
)
LIURNIA_TO_ALTUS_PLATEAU_NW_SW = MapTile(  # SMALL
    36, 50, 0,
    name="LiurniaToAltusPlateau_NW_SW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NW_SW",
    verbose_name="Liurnia to Altus Plateau (NW) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Behind Caria Manor",
    ),
    markers=(
        "Royal Grave Evergaol (Evergaol)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NW,
)
LIURNIA_TO_ALTUS_PLATEAU_NW_NW = MapTile(  # SMALL
    36, 51, 0,
    name="LiurniaToAltusPlateau_NW_NW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NW_NW",
    verbose_name="Liurnia to Altus Plateau (NW) (NW)",
    sites_of_grace=(),
    markers=(
        "Perfumer's Ruins (Ruins)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NW,
)
LIURNIA_TO_ALTUS_PLATEAU_NW_SE = MapTile(  # SMALL
    37, 50, 0,
    name="LiurniaToAltusPlateau_NW_SE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NW_SE",
    verbose_name="Liurnia to Altus Plateau (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NW,
)
LIURNIA_TO_ALTUS_PLATEAU_NW_NE = MapTile(  # SMALL
    37, 51, 0,
    name="LiurniaToAltusPlateau_NW_NE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NW_NE",
    verbose_name="Liurnia to Altus Plateau (NW) (NE)",
    sites_of_grace=(
        "Altus Plateau - Abandoned Coffin",
    ),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NW,
)
LIURNIA_TO_ALTUS_PLATEAU_SE = MapTile(  # MEDIUM
    19, 24, 1,
    name="LiurniaToAltusPlateau_SE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SE",
    verbose_name="Liurnia to Altus Plateau (SE)",
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU,
)
LIURNIA_TO_ALTUS_PLATEAU_SE_SW = MapTile(  # SMALL
    38, 48, 0,
    name="LiurniaToAltusPlateau_SE_SW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SE_SW",
    verbose_name="Liurnia to Altus Plateau (SE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Bellum Highway - Frenzied Flame Village Outskirts",
    ),
    markers=(
        "Frenzied Flame Village (Unique)"
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SE,
)
LIURNIA_TO_ALTUS_PLATEAU_SE_NW = MapTile(  # SMALL
    38, 49, 0,
    name="LiurniaToAltusPlateau_SE_NW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SE_NW",
    verbose_name="Liurnia to Altus Plateau (SE) (NW)",
    sites_of_grace=(),
    markers=(
        "Frenzy-Flaming Tower (Tower)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SE,
)
LIURNIA_TO_ALTUS_PLATEAU_SE_SE = MapTile(  # SMALL
    39, 48, 0,
    name="LiurniaToAltusPlateau_SE_SE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SE_SE",
    verbose_name="Liurnia to Altus Plateau (SE) (SE)",
    sites_of_grace=(),
    markers=(
        "Converted Fringe Tower (Rise)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SE,
)
LIURNIA_TO_ALTUS_PLATEAU_SE_NE = MapTile(  # SMALL
    39, 49, 0,
    name="LiurniaToAltusPlateau_SE_NE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_SE_NE",
    verbose_name="Liurnia to Altus Plateau (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_SE,
)
LIURNIA_TO_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    19, 25, 1,
    name="LiurniaToAltusPlateau_NE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NE",
    verbose_name="Liurnia to Altus Plateau (NE)",
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU,
)
LIURNIA_TO_ALTUS_PLATEAU_NE_SW = MapTile(  # SMALL
    38, 50, 0,
    name="LiurniaToAltusPlateau_NE_SW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NE_SW",
    verbose_name="Liurnia to Altus Plateau (NE) (SW)",
    sites_of_grace=(
        "Liurnia of the Lakes - Bellum Highway - Grand Lift of Dectus"
        "Liurnia of the Lakes - Ravine-Veiled Village"
        "Altus Plateau - Altus Plateau",
    ),
    markers=(
        "Grand Lift of Dectus (Lift)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NE,
)
LIURNIA_TO_ALTUS_PLATEAU_NE_NW = MapTile(  # SMALL
    38, 51, 0,
    name="LiurniaToAltusPlateau_NE_NW",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NE_NW",
    verbose_name="Liurnia to Altus Plateau (NE) (NW)",
    sites_of_grace=(
        "Altus Plateau - Erdtree-Gazing Hill",
    ),
    markers=(
        "Lux Ruins (Ruins)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NE,
)
LIURNIA_TO_ALTUS_PLATEAU_NE_SE = MapTile(  # SMALL
    39, 50, 0,
    name="LiurniaToAltusPlateau_NE_SE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NE_SE",
    verbose_name="Liurnia to Altus Plateau (NE) (SE)",
    sites_of_grace=(),
    markers=(
        "Golden Lineage Evergaol (Evergaol)",
    ),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NE,
)
LIURNIA_TO_ALTUS_PLATEAU_NE_NE = MapTile(  # SMALL
    39, 51, 0,
    name="LiurniaToAltusPlateau_NE_NE",
    variable_name="LIURNIA_TO_ALTUS_PLATEAU_NE_NE",
    verbose_name="Liurnia to Altus Plateau (NE) (NE)",
    sites_of_grace=(
        "Altus Plateau - Altus Highway Junction",
    ),
    markers=(),
    parent_tile=LIURNIA_TO_ALTUS_PLATEAU_NE,
)

WEST_ALTUS_PLATEAU = MapTile(  # LARGE
    9, 13, 2,
    name="WestAltusPlateau",
    variable_name="WEST_ALTUS_PLATEAU",
    verbose_name="West Altus Plateau",
)
WEST_ALTUS_PLATEAU_SW = MapTile(  # MEDIUM
    18, 26, 1,
    name="WestAltusPlateau_SW",
    variable_name="WEST_ALTUS_PLATEAU_SW",
    verbose_name="West Altus Plateau (SW)",
    parent_tile=WEST_ALTUS_PLATEAU,
)
WEST_ALTUS_PLATEAU_SW_SW = MapTile(  # SMALL
    36, 52, 0,
    name="WestAltusPlateau_SW_SW",
    variable_name="WEST_ALTUS_PLATEAU_SW_SW",
    verbose_name="West Altus Plateau (SW) (SW)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Craftsman's Shack",
    ),
    markers=(
        "Hermit's Shack (Shack)"
        "Craftsman's Shack (Shack)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SW,
)
WEST_ALTUS_PLATEAU_SW_NW = MapTile(  # SMALL
    36, 53, 0,
    name="WestAltusPlateau_SW_NW",
    variable_name="WEST_ALTUS_PLATEAU_SW_NW",
    verbose_name="West Altus Plateau (SW) (NW)",
    sites_of_grace=(),
    markers=(
        "Volcano Manor (Unique)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SW,
)
WEST_ALTUS_PLATEAU_SW_SE = MapTile(  # SMALL
    37, 52, 0,
    name="WestAltusPlateau_SW_SE",
    variable_name="WEST_ALTUS_PLATEAU_SW_SE",
    verbose_name="West Altus Plateau (SW) (SE)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Seethewater River",
    ),
    markers=(
        "Hermit Village (Unique)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SW,
)
WEST_ALTUS_PLATEAU_SW_NE = MapTile(  # SMALL
    37, 53, 0,
    name="WestAltusPlateau_SW_NE",
    variable_name="WEST_ALTUS_PLATEAU_SW_NE",
    verbose_name="West Altus Plateau (SW) (NE)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Primeval Sorcerer Azur",
    ),
    markers=(),
    parent_tile=WEST_ALTUS_PLATEAU_SW,
)
WEST_ALTUS_PLATEAU_NW = MapTile(  # MEDIUM
    18, 27, 1,
    name="WestAltusPlateau_NW",
    variable_name="WEST_ALTUS_PLATEAU_NW",
    verbose_name="West Altus Plateau (NW)",
    parent_tile=WEST_ALTUS_PLATEAU,
)
WEST_ALTUS_PLATEAU_NW_SW = MapTile(  # SMALL
    36, 54, 0,
    name="WestAltusPlateau_NW_SW",
    variable_name="WEST_ALTUS_PLATEAU_NW_SW",
    verbose_name="West Altus Plateau (NW) (SW)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Ninth Mt. Gelmir Campsite"
        "Altus Plateau - Mt. Gelmir - Road of Iniquity",
    ),
    markers=(),
    parent_tile=WEST_ALTUS_PLATEAU_NW,
)
WEST_ALTUS_PLATEAU_NW_SE = MapTile(  # SMALL
    37, 54, 0,
    name="WestAltusPlateau_NW_SE",
    variable_name="WEST_ALTUS_PLATEAU_NW_SE",
    verbose_name="West Altus Plateau (NW) (SE)",
    sites_of_grace=(),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_NW,
)
WEST_ALTUS_PLATEAU_NW_NE = MapTile(  # SMALL
    37, 55, 0,
    name="WestAltusPlateau_NW_NE",
    variable_name="WEST_ALTUS_PLATEAU_NW_NE",
    verbose_name="West Altus Plateau (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_ALTUS_PLATEAU_NW,
)
WEST_ALTUS_PLATEAU_SE = MapTile(  # MEDIUM
    19, 26, 1,
    name="WestAltusPlateau_SE",
    variable_name="WEST_ALTUS_PLATEAU_SE",
    verbose_name="West Altus Plateau (SE)",
    parent_tile=WEST_ALTUS_PLATEAU,
)
WEST_ALTUS_PLATEAU_SE_SW = MapTile(  # SMALL
    38, 52, 0,
    name="WestAltusPlateau_SE_SW",
    variable_name="WEST_ALTUS_PLATEAU_SE_SW",
    verbose_name="West Altus Plateau (SE) (SW)",
    sites_of_grace=(),
    markers=(
        "Wyndham Ruins (Ruins)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SE,
)
WEST_ALTUS_PLATEAU_SE_NW = MapTile(  # SMALL
    38, 53, 0,
    name="WestAltusPlateau_SE_NW",
    variable_name="WEST_ALTUS_PLATEAU_SE_NW",
    verbose_name="West Altus Plateau (SE) (NW)",
    sites_of_grace=(),
    markers=(
        "Old Altus Tunnel (Tunnel)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SE,
)
WEST_ALTUS_PLATEAU_SE_SE = MapTile(  # SMALL
    39, 52, 0,
    name="WestAltusPlateau_SE_SE",
    variable_name="WEST_ALTUS_PLATEAU_SE_SE",
    verbose_name="West Altus Plateau (SE) (SE)",
    sites_of_grace=(),
    markers=(
        "Second Church of Marika (Church)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SE,
)
WEST_ALTUS_PLATEAU_SE_NE = MapTile(  # SMALL
    39, 53, 0,
    name="WestAltusPlateau_SE_NE",
    variable_name="WEST_ALTUS_PLATEAU_SE_NE",
    verbose_name="West Altus Plateau (SE) (NE)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - Bridge of Iniquity",
    ),
    markers=(
        "Mirage Rise (Rise)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_SE,
)
WEST_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    19, 27, 1,
    name="WestAltusPlateau_NE",
    variable_name="WEST_ALTUS_PLATEAU_NE",
    verbose_name="West Altus Plateau (NE)",
    parent_tile=WEST_ALTUS_PLATEAU,
)
WEST_ALTUS_PLATEAU_NE_SW = MapTile(  # SMALL
    38, 54, 0,
    name="WestAltusPlateau_NE_SW",
    variable_name="WEST_ALTUS_PLATEAU_NE_SW",
    verbose_name="West Altus Plateau (NE) (SW)",
    sites_of_grace=(
        "Altus Plateau - Mt. Gelmir - First Mt. Gelmir Campsite",
    ),
    markers=(
        "Corpse-Stench Shack (Shack)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_NE,
)
WEST_ALTUS_PLATEAU_NE_SE = MapTile(  # SMALL
    39, 54, 0,
    name="WestAltusPlateau_NE_SE",
    variable_name="WEST_ALTUS_PLATEAU_NE_SE",
    verbose_name="West Altus Plateau (NE) (SE)",
    sites_of_grace=(
        "Altus Plateau - Shaded Castle Ramparts"
        "Altus Plateau - Shaded Castle Inner Gate"
        "Altus Plateau - Castellan's Hall",
    ),
    markers=(
        "The Shaded Castle (Unique)",
    ),
    parent_tile=WEST_ALTUS_PLATEAU_NE,
)

SOUTH_WEEPING_PENINSULA = MapTile(  # LARGE
    10, 7, 2,
    name="SouthWeepingPeninsula",
    variable_name="SOUTH_WEEPING_PENINSULA",
    verbose_name="South Weeping Peninsula",
)
SOUTH_WEEPING_PENINSULA_NE = MapTile(  # MEDIUM
    21, 15, 1,
    name="SouthWeepingPeninsula_NE",
    variable_name="SOUTH_WEEPING_PENINSULA_NE",
    verbose_name="South Weeping Peninsula (NE)",
    parent_tile=SOUTH_WEEPING_PENINSULA,
)
SOUTH_WEEPING_PENINSULA_NE_SE = MapTile(  # SMALL
    43, 30, 0,
    name="SouthWeepingPeninsula_NE_SE",
    variable_name="SOUTH_WEEPING_PENINSULA_NE_SE",
    verbose_name="South Weeping Peninsula (NE) (SE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Morne Moangrave",
    ),
    markers=(),
    parent_tile=SOUTH_WEEPING_PENINSULA_NE,
)
SOUTH_WEEPING_PENINSULA_NE_NE = MapTile(  # SMALL
    43, 31, 0,
    name="SouthWeepingPeninsula_NE_NE",
    variable_name="SOUTH_WEEPING_PENINSULA_NE_NE",
    verbose_name="South Weeping Peninsula (NE) (NE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Castle Morne Lift"
        "Limgrave - Weeping Peninsula - Behind the Castle"
        "Limgrave - Weeping Peninsula - Beside the Rampart Gaol",
    ),
    markers=(
        "Castle Morne (Unique)",
    ),
    parent_tile=SOUTH_WEEPING_PENINSULA_NE,
)

WEST_WEEPING_PENINSULA = MapTile(  # LARGE
    10, 8, 2,
    name="WestWeepingPeninsula",
    variable_name="WEST_WEEPING_PENINSULA",
    verbose_name="West Weeping Peninsula",
)
WEST_WEEPING_PENINSULA_SW = MapTile(  # MEDIUM
    20, 16, 1,
    name="WestWeepingPeninsula_SW",
    variable_name="WEST_WEEPING_PENINSULA_SW",
    verbose_name="West Weeping Peninsula (SW)",
    parent_tile=WEST_WEEPING_PENINSULA,
)
WEST_WEEPING_PENINSULA_SW_NW = MapTile(  # SMALL
    40, 33, 0,
    name="WestWeepingPeninsula_SW_NW",
    variable_name="WEST_WEEPING_PENINSULA_SW_NW",
    verbose_name="West Weeping Peninsula (SW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_WEEPING_PENINSULA_SW,
)
WEST_WEEPING_PENINSULA_SW_SE = MapTile(  # SMALL
    41, 32, 0,
    name="WestWeepingPeninsula_SW_SE",
    variable_name="WEST_WEEPING_PENINSULA_SW_SE",
    verbose_name="West Weeping Peninsula (SW) (SE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Isolated Merchant's Shack",
    ),
    markers=(
        "Isolated Merchant's Shack (Shack)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_SW,
)
WEST_WEEPING_PENINSULA_SW_NE = MapTile(  # SMALL
    41, 33, 0,
    name="WestWeepingPeninsula_SW_NE",
    variable_name="WEST_WEEPING_PENINSULA_SW_NE",
    verbose_name="West Weeping Peninsula (SW) (NE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Fourth Church of Marika",
    ),
    markers=(
        "Fourth Church of Marika (Church)"
        "Witchbane Ruins (Ruins)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_SW,
)
WEST_WEEPING_PENINSULA_NW = MapTile(  # MEDIUM
    20, 17, 1,
    name="WestWeepingPeninsula_NW",
    variable_name="WEST_WEEPING_PENINSULA_NW",
    verbose_name="West Weeping Peninsula (NW)",
    parent_tile=WEST_WEEPING_PENINSULA,
)
WEST_WEEPING_PENINSULA_NW_SE = MapTile(  # SMALL
    41, 34, 0,
    name="WestWeepingPeninsula_NW_SE",
    variable_name="WEST_WEEPING_PENINSULA_NW_SE",
    verbose_name="West Weeping Peninsula (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_WEEPING_PENINSULA_NW,
)
WEST_WEEPING_PENINSULA_NW_NE = MapTile(  # SMALL
    41, 35, 0,
    name="WestWeepingPeninsula_NW_NE",
    variable_name="WEST_WEEPING_PENINSULA_NW_NE",
    verbose_name="West Weeping Peninsula (NW) (NE)",
    sites_of_grace=(
        "Limgrave - Church of Dragon Communion",
    ),
    markers=(
        "Church of Dragon Communion (Church)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_NW,
)
WEST_WEEPING_PENINSULA_SE = MapTile(  # MEDIUM
    21, 16, 1,
    name="WestWeepingPeninsula_SE",
    variable_name="WEST_WEEPING_PENINSULA_SE",
    verbose_name="West Weeping Peninsula (SE)",
    parent_tile=WEST_WEEPING_PENINSULA,
)
WEST_WEEPING_PENINSULA_SE_SW = MapTile(  # SMALL
    42, 32, 0,
    name="WestWeepingPeninsula_SE_SW",
    variable_name="WEST_WEEPING_PENINSULA_SE_SW",
    verbose_name="West Weeping Peninsula (SE) (SW)",
    sites_of_grace=(),
    markers=(
        "Tower of Return (Tower)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_SE,
)
WEST_WEEPING_PENINSULA_SE_NW = MapTile(  # SMALL
    42, 33, 0,
    name="WestWeepingPeninsula_SE_NW",
    variable_name="WEST_WEEPING_PENINSULA_SE_NW",
    verbose_name="West Weeping Peninsula (SE) (NW)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Tombsward",
    ),
    markers=(
        "Tombsward Cave (Cave)"
        "Weeping Evergaol (Evergaol)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_SE,
)
WEST_WEEPING_PENINSULA_SE_SE = MapTile(  # SMALL
    43, 32, 0,
    name="WestWeepingPeninsula_SE_SE",
    variable_name="WEST_WEEPING_PENINSULA_SE_SE",
    verbose_name="West Weeping Peninsula (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_WEEPING_PENINSULA_SE,
)
WEST_WEEPING_PENINSULA_SE_NE = MapTile(  # SMALL
    43, 33, 0,
    name="WestWeepingPeninsula_SE_NE",
    variable_name="WEST_WEEPING_PENINSULA_SE_NE",
    verbose_name="West Weeping Peninsula (SE) (NE)",
    sites_of_grace=(),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_SE,
)
WEST_WEEPING_PENINSULA_NE = MapTile(  # MEDIUM
    21, 17, 1,
    name="WestWeepingPeninsula_NE",
    variable_name="WEST_WEEPING_PENINSULA_NE",
    verbose_name="West Weeping Peninsula (NE)",
    parent_tile=WEST_WEEPING_PENINSULA,
)
WEST_WEEPING_PENINSULA_NE_SW = MapTile(  # SMALL
    42, 34, 0,
    name="WestWeepingPeninsula_NE_SW",
    variable_name="WEST_WEEPING_PENINSULA_NE_SW",
    verbose_name="West Weeping Peninsula (NE) (SW)",
    sites_of_grace=(),
    markers=(
        "Tombsward Ruins (Ruins)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_NE,
)
WEST_WEEPING_PENINSULA_NE_NW = MapTile(  # SMALL
    42, 35, 0,
    name="WestWeepingPeninsula_NE_NW",
    variable_name="WEST_WEEPING_PENINSULA_NE_NW",
    verbose_name="West Weeping Peninsula (NE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_WEEPING_PENINSULA_NE,
)
WEST_WEEPING_PENINSULA_NE_SE = MapTile(  # SMALL
    43, 34, 0,
    name="WestWeepingPeninsula_NE_SE",
    variable_name="WEST_WEEPING_PENINSULA_NE_SE",
    verbose_name="West Weeping Peninsula (NE) (SE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Church of Pilgrimage",
    ),
    markers=(
        "Church of Pilgrimage (Church)"
        "Demi-Human Forest Ruins (Ruins)",
    ),
    parent_tile=WEST_WEEPING_PENINSULA_NE,
)
WEST_WEEPING_PENINSULA_NE_NE = MapTile(  # SMALL
    43, 35, 0,
    name="WestWeepingPeninsula_NE_NE",
    variable_name="WEST_WEEPING_PENINSULA_NE_NE",
    verbose_name="West Weeping Peninsula (NE) (NE)",
    sites_of_grace=(
        "Limgrave - Seaside Ruins",
    ),
    markers=(),
    parent_tile=WEST_WEEPING_PENINSULA_NE,
)

WEST_LIMGRAVE = MapTile(  # LARGE
    10, 9, 2,
    name="WestLimgrave",
    variable_name="WEST_LIMGRAVE",
    verbose_name="West Limgrave",
)
WEST_LIMGRAVE_SW = MapTile(  # MEDIUM
    20, 18, 1,
    name="WestLimgrave_SW",
    variable_name="WEST_LIMGRAVE_SW",
    verbose_name="West Limgrave (SW)",
    parent_tile=WEST_LIMGRAVE,
)
WEST_LIMGRAVE_SW_SE = MapTile(  # SMALL
    41, 36, 0,
    name="WestLimgrave_SW_SE",
    variable_name="WEST_LIMGRAVE_SW_SE",
    verbose_name="West Limgrave (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_SW,
)
WEST_LIMGRAVE_SW_NE = MapTile(  # SMALL
    41, 37, 0,
    name="WestLimgrave_SW_NE",
    variable_name="WEST_LIMGRAVE_SW_NE",
    verbose_name="West Limgrave (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_SW,
)
WEST_LIMGRAVE_NW = MapTile(  # MEDIUM
    20, 19, 1,
    name="WestLimgrave_NW",
    variable_name="WEST_LIMGRAVE_NW",
    verbose_name="West Limgrave (NW)",
    parent_tile=WEST_LIMGRAVE,
)
WEST_LIMGRAVE_NW_SW = MapTile(  # SMALL
    40, 38, 0,
    name="WestLimgrave_NW_SW",
    variable_name="WEST_LIMGRAVE_NW_SW",
    verbose_name="West Limgrave (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NW,
)
WEST_LIMGRAVE_NW_NW = MapTile(  # SMALL
    40, 39, 0,
    name="WestLimgrave_NW_NW",
    variable_name="WEST_LIMGRAVE_NW_NW",
    verbose_name="West Limgrave (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NW,
)
WEST_LIMGRAVE_NW_SE = MapTile(  # SMALL
    41, 38, 0,
    name="WestLimgrave_NW_SE",
    variable_name="WEST_LIMGRAVE_NW_SE",
    verbose_name="West Limgrave (NW) (SE)",
    sites_of_grace=(
        "Limgrave - Stormhill - Stormhill Shack",
    ),
    markers=(
        "Stormhill Shack (Shack)",
    ),
    parent_tile=WEST_LIMGRAVE_NW,
)
WEST_LIMGRAVE_NW_NE = MapTile(  # SMALL
    41, 39, 0,
    name="WestLimgrave_NW_NE",
    variable_name="WEST_LIMGRAVE_NW_NE",
    verbose_name="West Limgrave (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NW,
)
WEST_LIMGRAVE_SE = MapTile(  # MEDIUM
    21, 18, 1,
    name="WestLimgrave_SE",
    variable_name="WEST_LIMGRAVE_SE",
    verbose_name="West Limgrave (SE)",
    parent_tile=WEST_LIMGRAVE,
)
WEST_LIMGRAVE_SE_SW = MapTile(  # SMALL
    42, 36, 0,
    name="WestLimgrave_SE_SW",
    variable_name="WEST_LIMGRAVE_SE_SW",
    verbose_name="West Limgrave (SE) (SW)",
    sites_of_grace=(
        "Limgrave - Church of Elleh"
        "Limgrave - The First Step",
    ),
    markers=(
        "Church of Elleh (Church)",
    ),
    parent_tile=WEST_LIMGRAVE_SE,
)
WEST_LIMGRAVE_SE_NW = MapTile(  # SMALL
    42, 37, 0,
    name="WestLimgrave_SE_NW",
    variable_name="WEST_LIMGRAVE_SE_NW",
    verbose_name="West Limgrave (SE) (NW)",
    sites_of_grace=(
        "Limgrave - Gatefront",
    ),
    markers=(
        "Limgrave Tunnels (Tunnel)"
        "Gatefront Ruins (Ruins)"
        "Stormhill Evergaol (Evergaol)",
    ),
    parent_tile=WEST_LIMGRAVE_SE,
)
WEST_LIMGRAVE_SE_SE = MapTile(  # SMALL
    43, 36, 0,
    name="WestLimgrave_SE_SE",
    variable_name="WEST_LIMGRAVE_SE_SE",
    verbose_name="West Limgrave (SE) (SE)",
    sites_of_grace=(),
    markers=(
        "Dragon-Burnt Ruins (Ruins)",
    ),
    parent_tile=WEST_LIMGRAVE_SE,
)
WEST_LIMGRAVE_SE_NE = MapTile(  # SMALL
    43, 37, 0,
    name="WestLimgrave_SE_NE",
    variable_name="WEST_LIMGRAVE_SE_NE",
    verbose_name="West Limgrave (SE) (NE)",
    sites_of_grace=(
        "Limgrave - Agheel Lake North",
    ),
    markers=(
        "Murkwater Cave (Cave)",
    ),
    parent_tile=WEST_LIMGRAVE_SE,
)
WEST_LIMGRAVE_NE = MapTile(  # MEDIUM
    21, 19, 1,
    name="WestLimgrave_NE",
    variable_name="WEST_LIMGRAVE_NE",
    verbose_name="West Limgrave (NE)",
    parent_tile=WEST_LIMGRAVE,
)
WEST_LIMGRAVE_NE_SW = MapTile(  # SMALL
    42, 38, 0,
    name="WestLimgrave_NE_SW",
    variable_name="WEST_LIMGRAVE_NE_SW",
    verbose_name="West Limgrave (NE) (SW)",
    sites_of_grace=(
        "Limgrave - Stormhill - Warmaster's Shack",
    ),
    markers=(
        "Stormgate (Gate)"
        "Warmaster's Shack (Shack)",
    ),
    parent_tile=WEST_LIMGRAVE_NE,
)
WEST_LIMGRAVE_NE_NW = MapTile(  # SMALL
    42, 39, 0,
    name="WestLimgrave_NE_NW",
    variable_name="WEST_LIMGRAVE_NE_NW",
    verbose_name="West Limgrave (NE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NE,
)
WEST_LIMGRAVE_NE_SE = MapTile(  # SMALL
    43, 38, 0,
    name="WestLimgrave_NE_SE",
    variable_name="WEST_LIMGRAVE_NE_SE",
    verbose_name="West Limgrave (NE) (SE)",
    sites_of_grace=(
        "Limgrave - Murkwater Coast",
    ),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NE,
)
WEST_LIMGRAVE_NE_NE = MapTile(  # SMALL
    43, 39, 0,
    name="WestLimgrave_NE_NE",
    variable_name="WEST_LIMGRAVE_NE_NE",
    verbose_name="West Limgrave (NE) (NE)",
    sites_of_grace=(
        "Limgrave - Stormhill - Saintsbridge",
    ),
    markers=(),
    parent_tile=WEST_LIMGRAVE_NE,
)

NORTHWEST_LIMGRAVE_COAST = MapTile(  # LARGE
    10, 10, 2,
    name="NorthwestLimgraveCoast",
    variable_name="NORTHWEST_LIMGRAVE_COAST",
    verbose_name="Northwest Limgrave Coast",
)
NORTHWEST_LIMGRAVE_COAST_SW = MapTile(  # MEDIUM
    20, 20, 1,
    name="NorthwestLimgraveCoast_SW",
    variable_name="NORTHWEST_LIMGRAVE_COAST_SW",
    verbose_name="Northwest Limgrave Coast (SW)",
    parent_tile=NORTHWEST_LIMGRAVE_COAST,
)
NORTHWEST_LIMGRAVE_COAST_SW_SW = MapTile(  # SMALL
    40, 40, 0,
    name="NorthwestLimgraveCoast_SW_SW",
    variable_name="NORTHWEST_LIMGRAVE_COAST_SW_SW",
    verbose_name="Northwest Limgrave Coast (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_LIMGRAVE_COAST_SW,
)
NORTHWEST_LIMGRAVE_COAST_SE = MapTile(  # MEDIUM
    21, 20, 1,
    name="NorthwestLimgraveCoast_SE",
    variable_name="NORTHWEST_LIMGRAVE_COAST_SE",
    verbose_name="Northwest Limgrave Coast (SE)",
    parent_tile=NORTHWEST_LIMGRAVE_COAST,
)
NORTHWEST_LIMGRAVE_COAST_SE_SW = MapTile(  # SMALL
    42, 40, 0,
    name="NorthwestLimgraveCoast_SE_SW",
    variable_name="NORTHWEST_LIMGRAVE_COAST_SE_SW",
    verbose_name="Northwest Limgrave Coast (SE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_LIMGRAVE_COAST_SE,
)
NORTHWEST_LIMGRAVE_COAST_SE_SE = MapTile(  # SMALL
    43, 40, 0,
    name="NorthwestLimgraveCoast_SE_SE",
    variable_name="NORTHWEST_LIMGRAVE_COAST_SE_SE",
    verbose_name="Northwest Limgrave Coast (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_LIMGRAVE_COAST_SE,
)

SOUTH_ALTUS_PLATEAU = MapTile(  # LARGE
    10, 12, 2,
    name="SouthAltusPlateau",
    variable_name="SOUTH_ALTUS_PLATEAU",
    verbose_name="South Altus Plateau",
)
SOUTH_ALTUS_PLATEAU_NW = MapTile(  # MEDIUM
    20, 25, 1,
    name="SouthAltusPlateau_NW",
    variable_name="SOUTH_ALTUS_PLATEAU_NW",
    verbose_name="South Altus Plateau (NW)",
    parent_tile=SOUTH_ALTUS_PLATEAU,
)
SOUTH_ALTUS_PLATEAU_NW_SW = MapTile(  # SMALL
    40, 50, 0,
    name="SouthAltusPlateau_NW_SW",
    variable_name="SOUTH_ALTUS_PLATEAU_NW_SW",
    verbose_name="South Altus Plateau (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NW,
)
SOUTH_ALTUS_PLATEAU_NW_NW = MapTile(  # SMALL
    40, 51, 0,
    name="SouthAltusPlateau_NW_NW",
    variable_name="SOUTH_ALTUS_PLATEAU_NW_NW",
    verbose_name="South Altus Plateau (NW) (NW)",
    sites_of_grace=(),
    markers=(
        "Stormcaller Church (Church)",
    ),
    parent_tile=SOUTH_ALTUS_PLATEAU_NW,
)
SOUTH_ALTUS_PLATEAU_NW_SE = MapTile(  # SMALL
    41, 50, 0,
    name="SouthAltusPlateau_NW_SE",
    variable_name="SOUTH_ALTUS_PLATEAU_NW_SE",
    verbose_name="South Altus Plateau (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NW,
)
SOUTH_ALTUS_PLATEAU_NW_NE = MapTile(  # SMALL
    41, 51, 0,
    name="SouthAltusPlateau_NW_NE",
    variable_name="SOUTH_ALTUS_PLATEAU_NW_NE",
    verbose_name="South Altus Plateau (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NW,
)
SOUTH_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    21, 25, 1,
    name="SouthAltusPlateau_NE",
    variable_name="SOUTH_ALTUS_PLATEAU_NE",
    verbose_name="South Altus Plateau (NE)",
    parent_tile=SOUTH_ALTUS_PLATEAU,
)
SOUTH_ALTUS_PLATEAU_NE_SW = MapTile(  # SMALL
    42, 50, 0,
    name="SouthAltusPlateau_NE_SW",
    variable_name="SOUTH_ALTUS_PLATEAU_NE_SW",
    verbose_name="South Altus Plateau (NE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NE,
)
SOUTH_ALTUS_PLATEAU_NE_NW = MapTile(  # SMALL
    42, 51, 0,
    name="SouthAltusPlateau_NE_NW",
    variable_name="SOUTH_ALTUS_PLATEAU_NE_NW",
    verbose_name="South Altus Plateau (NE) (NW)",
    sites_of_grace=(
        "Altus Plateau - Capital Outskirts - Outer Wall Phantom Tree",
    ),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NE,
)
SOUTH_ALTUS_PLATEAU_NE_SE = MapTile(  # SMALL
    43, 50, 0,
    name="SouthAltusPlateau_NE_SE",
    variable_name="SOUTH_ALTUS_PLATEAU_NE_SE",
    verbose_name="South Altus Plateau (NE) (SE)",
    sites_of_grace=(
        "Altus Plateau - Capital Outskirts - Minor Erdtree Church",
    ),
    markers=(
        "Sealed Tunnel (Tunnel)"
        "Minor Erdtree Church (Church)",
    ),
    parent_tile=SOUTH_ALTUS_PLATEAU_NE,
)
SOUTH_ALTUS_PLATEAU_NE_NE = MapTile(  # SMALL
    43, 51, 0,
    name="SouthAltusPlateau_NE_NE",
    variable_name="SOUTH_ALTUS_PLATEAU_NE_NE",
    verbose_name="South Altus Plateau (NE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_ALTUS_PLATEAU_NE,
)

NORTH_ALTUS_PLATEAU = MapTile(  # LARGE
    10, 13, 2,
    name="NorthAltusPlateau",
    variable_name="NORTH_ALTUS_PLATEAU",
    verbose_name="North Altus Plateau",
)
NORTH_ALTUS_PLATEAU_SW = MapTile(  # MEDIUM
    20, 26, 1,
    name="NorthAltusPlateau_SW",
    variable_name="NORTH_ALTUS_PLATEAU_SW",
    verbose_name="North Altus Plateau (SW)",
    parent_tile=NORTH_ALTUS_PLATEAU,
)
NORTH_ALTUS_PLATEAU_SW_SW = MapTile(  # SMALL
    40, 52, 0,
    name="NorthAltusPlateau_SW_SW",
    variable_name="NORTH_ALTUS_PLATEAU_SW_SW",
    verbose_name="North Altus Plateau (SW) (SW)",
    sites_of_grace=(
        "Altus Plateau - Forest-Spanning Greatbridge",
    ),
    markers=(
        "St. Trina's Hideaway (Shack)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_SW,
)
NORTH_ALTUS_PLATEAU_SW_NW = MapTile(  # SMALL
    40, 53, 0,
    name="NorthAltusPlateau_SW_NW",
    variable_name="NORTH_ALTUS_PLATEAU_SW_NW",
    verbose_name="North Altus Plateau (SW) (NW)",
    sites_of_grace=(
        "Altus Plateau - Bower of Bounty",
    ),
    markers=(
        "Writheblood Ruins (Ruins)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_SW,
)
NORTH_ALTUS_PLATEAU_SW_SE = MapTile(  # SMALL
    41, 52, 0,
    name="NorthAltusPlateau_SW_SE",
    variable_name="NORTH_ALTUS_PLATEAU_SW_SE",
    verbose_name="North Altus Plateau (SW) (SE)",
    sites_of_grace=(
        "Altus Plateau - Rampartside Path",
    ),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_SW,
)
NORTH_ALTUS_PLATEAU_SW_NE = MapTile(  # SMALL
    41, 53, 0,
    name="NorthAltusPlateau_SW_NE",
    variable_name="NORTH_ALTUS_PLATEAU_SW_NE",
    verbose_name="North Altus Plateau (SW) (NE)",
    sites_of_grace=(),
    markers=(
        "Woodfolk Ruins (Ruins)"
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_SW,
)
NORTH_ALTUS_PLATEAU_NW = MapTile(  # MEDIUM
    20, 27, 1,
    name="NorthAltusPlateau_NW",
    variable_name="NORTH_ALTUS_PLATEAU_NW",
    verbose_name="North Altus Plateau (NW)",
    parent_tile=NORTH_ALTUS_PLATEAU,
)
NORTH_ALTUS_PLATEAU_NW_SW = MapTile(  # SMALL
    40, 54, 0,
    name="NorthAltusPlateau_NW_SW",
    variable_name="NORTH_ALTUS_PLATEAU_NW_SW",
    verbose_name="North Altus Plateau (NW) (SW)",
    sites_of_grace=(
        "Altus Plateau - Road of Iniquity Side Path",
    ),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_NW,
)
NORTH_ALTUS_PLATEAU_NW_NW = MapTile(  # SMALL
    40, 55, 0,
    name="NorthAltusPlateau_NW_NW",
    variable_name="NORTH_ALTUS_PLATEAU_NW_NW",
    verbose_name="North Altus Plateau (NW) (NW)",
    sites_of_grace=(),
    markers=(
        "West Windmill Pasture (Pasture)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_NW,
)
NORTH_ALTUS_PLATEAU_NW_SE = MapTile(  # SMALL
    41, 54, 0,
    name="NorthAltusPlateau_NW_SE",
    variable_name="NORTH_ALTUS_PLATEAU_NW_SE",
    verbose_name="North Altus Plateau (NW) (SE)",
    sites_of_grace=(
        "Altus Plateau - Windmill Village",
    ),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_NW,
)
NORTH_ALTUS_PLATEAU_NW_NE = MapTile(  # SMALL
    41, 55, 0,
    name="NorthAltusPlateau_NW_NE",
    variable_name="NORTH_ALTUS_PLATEAU_NW_NE",
    verbose_name="North Altus Plateau (NW) (NE)",
    sites_of_grace=(),
    markers=(
        "East Windmill Pasture (Pasture)"
        "Village Windmill Pasture (Pasture)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_NW,
)
NORTH_ALTUS_PLATEAU_SE = MapTile(  # MEDIUM
    21, 26, 1,
    name="NorthAltusPlateau_SE",
    variable_name="NORTH_ALTUS_PLATEAU_SE",
    verbose_name="North Altus Plateau (SE)",
    parent_tile=NORTH_ALTUS_PLATEAU,
)
NORTH_ALTUS_PLATEAU_SE_SW = MapTile(  # SMALL
    42, 52, 0,
    name="NorthAltusPlateau_SE_SW",
    variable_name="NORTH_ALTUS_PLATEAU_SE_SW",
    verbose_name="North Altus Plateau (SE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_SE,
)
NORTH_ALTUS_PLATEAU_SE_NW = MapTile(  # SMALL
    42, 53, 0,
    name="NorthAltusPlateau_SE_NW",
    variable_name="NORTH_ALTUS_PLATEAU_SE_NW",
    verbose_name="North Altus Plateau (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_SE,
)
NORTH_ALTUS_PLATEAU_SE_SE = MapTile(  # SMALL
    43, 52, 0,
    name="NorthAltusPlateau_SE_SE",
    variable_name="NORTH_ALTUS_PLATEAU_SE_SE",
    verbose_name="North Altus Plateau (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_SE,
)
NORTH_ALTUS_PLATEAU_SE_NE = MapTile(  # SMALL
    43, 53, 0,
    name="NorthAltusPlateau_SE_NE",
    variable_name="NORTH_ALTUS_PLATEAU_SE_NE",
    verbose_name="North Altus Plateau (SE) (NE)",
    sites_of_grace=(
        "Altus Plateau - Capital Outskirts - Hermit Merchant's Shack"
        "Altus Plateau - Capital Outskirts - Outer Wall Battleground",
    ),
    markers=(
        "Hermit Merchant's Shack (Shack)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_SE,
)
NORTH_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    21, 27, 1,
    name="NorthAltusPlateau_NE",
    variable_name="NORTH_ALTUS_PLATEAU_NE",
    verbose_name="North Altus Plateau (NE)",
    parent_tile=NORTH_ALTUS_PLATEAU,
)
NORTH_ALTUS_PLATEAU_NE_SW = MapTile(  # SMALL
    42, 54, 0,
    name="NorthAltusPlateau_NE_SW",
    variable_name="NORTH_ALTUS_PLATEAU_NE_SW",
    verbose_name="North Altus Plateau (NE) (SW)",
    sites_of_grace=(),
    markers=(
        "Dominula, Windmill Village (Unique)"
        "Highway Lookout Tower (Tower)",
    ),
    parent_tile=NORTH_ALTUS_PLATEAU_NE,
)
NORTH_ALTUS_PLATEAU_NE_NW = MapTile(  # SMALL
    42, 55, 0,
    name="NorthAltusPlateau_NE_NW",
    variable_name="NORTH_ALTUS_PLATEAU_NE_NW",
    verbose_name="North Altus Plateau (NE) (NW)",
    sites_of_grace=(
        "Altus Plateau - Windmill Heights",
    ),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_NE,
)
NORTH_ALTUS_PLATEAU_NE_SE = MapTile(  # SMALL
    43, 54, 0,
    name="NorthAltusPlateau_NE_SE",
    variable_name="NORTH_ALTUS_PLATEAU_NE_SE",
    verbose_name="North Altus Plateau (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_ALTUS_PLATEAU_NE,
)

SOUTHEAST_WEEPING_PENINSULA_COAST = MapTile(  # LARGE
    11, 7, 2,
    name="SoutheastWeepingPeninsulaCoast",
    variable_name="SOUTHEAST_WEEPING_PENINSULA_COAST",
    verbose_name="Southeast Weeping Peninsula Coast",
)
SOUTHEAST_WEEPING_PENINSULA_COAST_NW = MapTile(  # MEDIUM
    22, 15, 1,
    name="SoutheastWeepingPeninsulaCoast_NW",
    variable_name="SOUTHEAST_WEEPING_PENINSULA_COAST_NW",
    verbose_name="Southeast Weeping Peninsula Coast (NW)",
    parent_tile=SOUTHEAST_WEEPING_PENINSULA_COAST,
)
SOUTHEAST_WEEPING_PENINSULA_COAST_NW_NW = MapTile(  # SMALL
    44, 31, 0,
    name="SoutheastWeepingPeninsulaCoast_NW_NW",
    variable_name="SOUTHEAST_WEEPING_PENINSULA_COAST_NW_NW",
    verbose_name="Southeast Weeping Peninsula Coast (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_WEEPING_PENINSULA_COAST_NW,
)

EAST_WEEPING_PENINSULA = MapTile(  # LARGE
    11, 8, 2,
    name="EastWeepingPeninsula",
    variable_name="EAST_WEEPING_PENINSULA",
    verbose_name="East Weeping Peninsula",
)
EAST_WEEPING_PENINSULA_SW = MapTile(  # MEDIUM
    22, 16, 1,
    name="EastWeepingPeninsula_SW",
    variable_name="EAST_WEEPING_PENINSULA_SW",
    verbose_name="East Weeping Peninsula (SW)",
    parent_tile=EAST_WEEPING_PENINSULA,
)
EAST_WEEPING_PENINSULA_SW_SW = MapTile(  # SMALL
    44, 32, 0,
    name="EastWeepingPeninsula_SW_SW",
    variable_name="EAST_WEEPING_PENINSULA_SW_SW",
    verbose_name="East Weeping Peninsula (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_WEEPING_PENINSULA_SW,
)
EAST_WEEPING_PENINSULA_SW_NW = MapTile(  # SMALL
    44, 33, 0,
    name="EastWeepingPeninsula_SW_NW",
    variable_name="EAST_WEEPING_PENINSULA_SW_NW",
    verbose_name="East Weeping Peninsula (SW) (NW)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Castle Morne Rampart"
        "Limgrave - Weeping Peninsula - South of the Lookout Tower"
        "Limgrave - Weeping Peninsula - Ailing Village Outskirts",
    ),
    markers=(
        "Callu Baptismal Church (Church)"
        "Ailing Village (Unique)",
    ),
    parent_tile=EAST_WEEPING_PENINSULA_SW,
)
EAST_WEEPING_PENINSULA_SW_SE = MapTile(  # SMALL
    45, 32, 0,
    name="EastWeepingPeninsula_SW_SE",
    variable_name="EAST_WEEPING_PENINSULA_SW_SE",
    verbose_name="East Weeping Peninsula (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_WEEPING_PENINSULA_SW,
)
EAST_WEEPING_PENINSULA_SW_NE = MapTile(  # SMALL
    45, 33, 0,
    name="EastWeepingPeninsula_SW_NE",
    variable_name="EAST_WEEPING_PENINSULA_SW_NE",
    verbose_name="East Weeping Peninsula (SW) (NE)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Beside the Crater-Pocked Glade",
    ),
    markers=(
        "Oridys's Rise (Rise)",
    ),
    parent_tile=EAST_WEEPING_PENINSULA_SW,
)
EAST_WEEPING_PENINSULA_NW = MapTile(  # MEDIUM
    22, 17, 1,
    name="EastWeepingPeninsula_NW",
    variable_name="EAST_WEEPING_PENINSULA_NW",
    verbose_name="East Weeping Peninsula (NW)",
    parent_tile=EAST_WEEPING_PENINSULA,
)
EAST_WEEPING_PENINSULA_NW_SW = MapTile(  # SMALL
    44, 34, 0,
    name="EastWeepingPeninsula_NW_SW",
    variable_name="EAST_WEEPING_PENINSULA_NW_SW",
    verbose_name="East Weeping Peninsula (NW) (SW)",
    sites_of_grace=(
        "Limgrave - Weeping Peninsula - Bridge of Sacrifice",
    ),
    markers=(
        "Bridge of Sacrifice (Unique)"
        "Forest Lookout Tower (Tower)",
    ),
    parent_tile=EAST_WEEPING_PENINSULA_NW,
)
EAST_WEEPING_PENINSULA_NW_NW = MapTile(  # SMALL
    44, 35, 0,
    name="EastWeepingPeninsula_NW_NW",
    variable_name="EAST_WEEPING_PENINSULA_NW_NW",
    verbose_name="East Weeping Peninsula (NW) (NW)",
    sites_of_grace=(
        "Limgrave - Agheel Lake South",
    ),
    markers=(
        "Forlorn Hound Evergaol (Evergaol)",
    ),
    parent_tile=EAST_WEEPING_PENINSULA_NW,
)
EAST_WEEPING_PENINSULA_NW_SE = MapTile(  # SMALL
    45, 34, 0,
    name="EastWeepingPeninsula_NW_SE",
    variable_name="EAST_WEEPING_PENINSULA_NW_SE",
    verbose_name="East Weeping Peninsula (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_WEEPING_PENINSULA_NW,
)
EAST_WEEPING_PENINSULA_NW_NE = MapTile(  # SMALL
    45, 35, 0,
    name="EastWeepingPeninsula_NW_NE",
    variable_name="EAST_WEEPING_PENINSULA_NW_NE",
    verbose_name="East Weeping Peninsula (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_WEEPING_PENINSULA_NW,
)

EAST_LIMGRAVE = MapTile(  # LARGE
    11, 9, 2,
    name="EastLimgrave",
    variable_name="EAST_LIMGRAVE",
    verbose_name="East Limgrave",
)
EAST_LIMGRAVE_SW = MapTile(  # MEDIUM
    22, 18, 1,
    name="EastLimgrave_SW",
    variable_name="EAST_LIMGRAVE_SW",
    verbose_name="East Limgrave (SW)",
    parent_tile=EAST_LIMGRAVE,
)
EAST_LIMGRAVE_SW_SW = MapTile(  # SMALL
    44, 36, 0,
    name="EastLimgrave_SW_SW",
    variable_name="EAST_LIMGRAVE_SW_SW",
    verbose_name="East Limgrave (SW) (SW)",
    sites_of_grace=(
        "Limgrave - Waypoint Ruins Cellar",
    ),
    markers=(
        "Waypoint Ruins (Ruins)",
    ),
    parent_tile=EAST_LIMGRAVE_SW,
)
EAST_LIMGRAVE_SW_NW = MapTile(  # SMALL
    44, 37, 0,
    name="EastLimgrave_SW_NW",
    variable_name="EAST_LIMGRAVE_SW_NW",
    verbose_name="East Limgrave (SW) (NW)",
    sites_of_grace=(
        "Limgrave - Mistwood Outskirts",
    ),
    markers=(),
    parent_tile=EAST_LIMGRAVE_SW,
)
EAST_LIMGRAVE_SW_SE = MapTile(  # SMALL
    45, 36, 0,
    name="EastLimgrave_SW_SE",
    variable_name="EAST_LIMGRAVE_SW_SE",
    verbose_name="East Limgrave (SW) (SE)",
    sites_of_grace=(
        "Limgrave - Fort Haight West",
    ),
    markers=(),
    parent_tile=EAST_LIMGRAVE_SW,
)
EAST_LIMGRAVE_SW_NE = MapTile(  # SMALL
    45, 37, 0,
    name="EastLimgrave_SW_NE",
    variable_name="EAST_LIMGRAVE_SW_NE",
    verbose_name="East Limgrave (SW) (NE)",
    sites_of_grace=(),
    markers=(
        "Siofra River Well (Well)"
        "Mistwood Ruins (Ruins)"
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=EAST_LIMGRAVE_SW,
)
EAST_LIMGRAVE_NW = MapTile(  # MEDIUM
    22, 19, 1,
    name="EastLimgrave_NW",
    variable_name="EAST_LIMGRAVE_NW",
    verbose_name="East Limgrave (NW)",
    parent_tile=EAST_LIMGRAVE,
)
EAST_LIMGRAVE_NW_SW = MapTile(  # SMALL
    44, 38, 0,
    name="EastLimgrave_NW_SW",
    variable_name="EAST_LIMGRAVE_NW_SW",
    verbose_name="East Limgrave (NW) (SW)",
    sites_of_grace=(
        "Limgrave - Artist's Shack",
    ),
    markers=(
        "Artist's Shack (Shack)",
    ),
    parent_tile=EAST_LIMGRAVE_NW,
)
EAST_LIMGRAVE_NW_NW = MapTile(  # SMALL
    44, 39, 0,
    name="EastLimgrave_NW_NW",
    variable_name="EAST_LIMGRAVE_NW_NW",
    verbose_name="East Limgrave (NW) (NW)",
    sites_of_grace=(
        "Limgrave - Summonwater Village Outskirts",
    ),
    markers=(),
    parent_tile=EAST_LIMGRAVE_NW,
)
EAST_LIMGRAVE_NW_SE = MapTile(  # SMALL
    45, 38, 0,
    name="EastLimgrave_NW_SE",
    variable_name="EAST_LIMGRAVE_NW_SE",
    verbose_name="East Limgrave (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIMGRAVE_NW,
)
EAST_LIMGRAVE_NW_NE = MapTile(  # SMALL
    45, 39, 0,
    name="EastLimgrave_NW_NE",
    variable_name="EAST_LIMGRAVE_NW_NE",
    verbose_name="East Limgrave (NW) (NE)",
    sites_of_grace=(),
    markers=(
        "Summonwater Village (Ruins)",
    ),
    parent_tile=EAST_LIMGRAVE_NW,
)
EAST_LIMGRAVE_SE = MapTile(  # MEDIUM
    23, 18, 1,
    name="EastLimgrave_SE",
    variable_name="EAST_LIMGRAVE_SE",
    verbose_name="East Limgrave (SE)",
    parent_tile=EAST_LIMGRAVE,
)
EAST_LIMGRAVE_SE_SW = MapTile(  # SMALL
    46, 36, 0,
    name="EastLimgrave_SE_SW",
    variable_name="EAST_LIMGRAVE_SE_SW",
    verbose_name="East Limgrave (SE) (SW)",
    sites_of_grace=(),
    markers=(
        "Fort Haight (Fort)",
    ),
    parent_tile=EAST_LIMGRAVE_SE,
)
EAST_LIMGRAVE_SE_NW = MapTile(  # SMALL
    46, 37, 0,
    name="EastLimgrave_SE_NW",
    variable_name="EAST_LIMGRAVE_SE_NW",
    verbose_name="East Limgrave (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIMGRAVE_SE,
)
EAST_LIMGRAVE_SE_NE = MapTile(  # SMALL
    47, 37, 0,
    name="EastLimgrave_SE_NE",
    variable_name="EAST_LIMGRAVE_SE_NE",
    verbose_name="East Limgrave (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIMGRAVE_SE,
)
EAST_LIMGRAVE_NE = MapTile(  # MEDIUM
    23, 19, 1,
    name="EastLimgrave_NE",
    variable_name="EAST_LIMGRAVE_NE",
    verbose_name="East Limgrave (NE)",
    parent_tile=EAST_LIMGRAVE,
)
EAST_LIMGRAVE_NE_SW = MapTile(  # SMALL
    46, 38, 0,
    name="EastLimgrave_NE_SW",
    variable_name="EAST_LIMGRAVE_NE_SW",
    verbose_name="East Limgrave (NE) (SW)",
    sites_of_grace=(
        "Limgrave - Third Church of Marika",
    ),
    markers=(
        "Third Church of Marika (Church)",
    ),
    parent_tile=EAST_LIMGRAVE_NE,
)
EAST_LIMGRAVE_NE_NW = MapTile(  # SMALL
    46, 39, 0,
    name="EastLimgrave_NE_NW",
    variable_name="EAST_LIMGRAVE_NE_NW",
    verbose_name="East Limgrave (NE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=EAST_LIMGRAVE_NE,
)
EAST_LIMGRAVE_NE_SE = MapTile(  # SMALL
    47, 38, 0,
    name="EastLimgrave_NE_SE",
    variable_name="EAST_LIMGRAVE_NE_SE",
    verbose_name="East Limgrave (NE) (SE)",
    sites_of_grace=(),
    markers=(
        "Caelid Waypoint Ruins (Ruins)"
        "Fort Gael (Fort)",
    ),
    parent_tile=EAST_LIMGRAVE_NE,
)
EAST_LIMGRAVE_NE_NE = MapTile(  # SMALL
    47, 39, 0,
    name="EastLimgrave_NE_NE",
    variable_name="EAST_LIMGRAVE_NE_NE",
    verbose_name="East Limgrave (NE) (NE)",
    sites_of_grace=(
        "Caelid - Fort Gael North",
    ),
    markers=(),
    parent_tile=EAST_LIMGRAVE_NE,
)

NORTHWEST_CAELID = MapTile(  # LARGE
    11, 10, 2,
    name="NorthwestCaelid",
    variable_name="NORTHWEST_CAELID",
    verbose_name="Northwest Caelid",
)
NORTHWEST_CAELID_SW = MapTile(  # MEDIUM
    22, 20, 1,
    name="NorthwestCaelid_SW",
    variable_name="NORTHWEST_CAELID_SW",
    verbose_name="Northwest Caelid (SW)",
    parent_tile=NORTHWEST_CAELID,
)
NORTHWEST_CAELID_SW_SE = MapTile(  # SMALL
    45, 40, 0,
    name="NorthwestCaelid_SW_SE",
    variable_name="NORTHWEST_CAELID_SW_SE",
    verbose_name="Northwest Caelid (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_CAELID_SW,
)
NORTHWEST_CAELID_SE = MapTile(  # MEDIUM
    23, 20, 1,
    name="NorthwestCaelid_SE",
    variable_name="NORTHWEST_CAELID_SE",
    verbose_name="Northwest Caelid (SE)",
    parent_tile=NORTHWEST_CAELID,
)
NORTHWEST_CAELID_SE_SW = MapTile(  # SMALL
    46, 40, 0,
    name="NorthwestCaelid_SE_SW",
    variable_name="NORTHWEST_CAELID_SE_SW",
    verbose_name="Northwest Caelid (SE) (SW)",
    sites_of_grace=(
        "Caelid - Smoldering Church"
        "Caelid - Rotview Balcony",
    ),
    markers=(
        "Smoldering Church (Church)"
        "Shack of the Rotting (Shack)",
    ),
    parent_tile=NORTHWEST_CAELID_SE,
)
NORTHWEST_CAELID_SE_SE = MapTile(  # SMALL
    47, 40, 0,
    name="NorthwestCaelid_SE_SE",
    variable_name="NORTHWEST_CAELID_SE_SE",
    verbose_name="Northwest Caelid (SE) (SE)",
    sites_of_grace=(
        "Caelid - Caelem Ruins",
    ),
    markers=(
        "Forsaken Ruins (Ruins)"
        "Minor Erdtree (Erdtree)"
        "Caelem Ruins (Ruins)"
        "Wailing Dunes (Other)",
    ),
    parent_tile=NORTHWEST_CAELID_SE,
)
NORTHWEST_CAELID_SE_NE = MapTile(  # SMALL
    47, 41, 0,
    name="NorthwestCaelid_SE_NE",
    variable_name="NORTHWEST_CAELID_SE_NE",
    verbose_name="Northwest Caelid (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_CAELID_SE,
)
NORTHWEST_CAELID_NE = MapTile(  # MEDIUM
    23, 21, 1,
    name="NorthwestCaelid_NE",
    variable_name="NORTHWEST_CAELID_NE",
    verbose_name="Northwest Caelid (NE)",
    parent_tile=NORTHWEST_CAELID,
)
NORTHWEST_CAELID_NE_SE = MapTile(  # SMALL
    47, 42, 0,
    name="NorthwestCaelid_NE_SE",
    variable_name="NORTHWEST_CAELID_NE_SE",
    verbose_name="Northwest Caelid (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_CAELID_NE,
)

SOUTHEAST_ALTUS_PLATEAU = MapTile(  # LARGE
    11, 12, 2,
    name="SoutheastAltusPlateau",
    variable_name="SOUTHEAST_ALTUS_PLATEAU",
    verbose_name="Southeast Altus Plateau",
)
SOUTHEAST_ALTUS_PLATEAU_NW = MapTile(  # MEDIUM
    22, 25, 1,
    name="SoutheastAltusPlateau_NW",
    variable_name="SOUTHEAST_ALTUS_PLATEAU_NW",
    verbose_name="Southeast Altus Plateau (NW)",
    parent_tile=SOUTHEAST_ALTUS_PLATEAU,
)
SOUTHEAST_ALTUS_PLATEAU_NW_NE = MapTile(  # SMALL
    45, 51, 0,
    name="SoutheastAltusPlateau_NW_NE",
    variable_name="SOUTHEAST_ALTUS_PLATEAU_NW_NE",
    verbose_name="Southeast Altus Plateau (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_ALTUS_PLATEAU_NW,
)
SOUTHEAST_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    23, 25, 1,
    name="SoutheastAltusPlateau_NE",
    variable_name="SOUTHEAST_ALTUS_PLATEAU_NE",
    verbose_name="Southeast Altus Plateau (NE)",
    parent_tile=SOUTHEAST_ALTUS_PLATEAU,
)
SOUTHEAST_ALTUS_PLATEAU_NE_NE = MapTile(  # SMALL
    47, 51, 0,
    name="SoutheastAltusPlateau_NE_NE",
    variable_name="SOUTHEAST_ALTUS_PLATEAU_NE_NE",
    verbose_name="Southeast Altus Plateau (NE) (NE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Forbidden Lands - Forbidden Lands",
    ),
    markers=(),
    parent_tile=SOUTHEAST_ALTUS_PLATEAU_NE,
)

NORTHEAST_ALTUS_PLATEAU = MapTile(  # LARGE
    11, 13, 2,
    name="NortheastAltusPlateau",
    variable_name="NORTHEAST_ALTUS_PLATEAU",
    verbose_name="Northeast Altus Plateau",
)
NORTHEAST_ALTUS_PLATEAU_SW = MapTile(  # MEDIUM
    22, 26, 1,
    name="NortheastAltusPlateau_SW",
    variable_name="NORTHEAST_ALTUS_PLATEAU_SW",
    verbose_name="Northeast Altus Plateau (SW)",
    parent_tile=NORTHEAST_ALTUS_PLATEAU,
)
NORTHEAST_ALTUS_PLATEAU_SW_SW = MapTile(  # SMALL
    44, 52, 0,
    name="NortheastAltusPlateau_SW_SW",
    variable_name="NORTHEAST_ALTUS_PLATEAU_SW_SW",
    verbose_name="Northeast Altus Plateau (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_SW,
)
NORTHEAST_ALTUS_PLATEAU_SW_NW = MapTile(  # SMALL
    44, 53, 0,
    name="NortheastAltusPlateau_SW_NW",
    variable_name="NORTHEAST_ALTUS_PLATEAU_SW_NW",
    verbose_name="Northeast Altus Plateau (SW) (NW)",
    sites_of_grace=(),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_SW,
)
NORTHEAST_ALTUS_PLATEAU_SW_SE = MapTile(  # SMALL
    45, 52, 0,
    name="NortheastAltusPlateau_SW_SE",
    variable_name="NORTHEAST_ALTUS_PLATEAU_SW_SE",
    verbose_name="Northeast Altus Plateau (SW) (SE)",
    sites_of_grace=(
        "Altus Plateau - Capital Outskirts - Capital Rampart",
    ),
    markers=(),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_SW,
)
NORTHEAST_ALTUS_PLATEAU_SW_NE = MapTile(  # SMALL
    45, 53, 0,
    name="NortheastAltusPlateau_SW_NE",
    variable_name="NORTHEAST_ALTUS_PLATEAU_SW_NE",
    verbose_name="Northeast Altus Plateau (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_SW,
)
NORTHEAST_ALTUS_PLATEAU_NE = MapTile(  # MEDIUM
    23, 27, 1,
    name="NortheastAltusPlateau_NE",
    variable_name="NORTHEAST_ALTUS_PLATEAU_NE",
    verbose_name="Northeast Altus Plateau (NE)",
    parent_tile=NORTHEAST_ALTUS_PLATEAU,
)
NORTHEAST_ALTUS_PLATEAU_NE_NW = MapTile(  # SMALL
    46, 55, 0,
    name="NortheastAltusPlateau_NE_NW",
    variable_name="NORTHEAST_ALTUS_PLATEAU_NE_NW",
    verbose_name="Northeast Altus Plateau (NE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_NE,
)
NORTHEAST_ALTUS_PLATEAU_NE_NE = MapTile(  # SMALL
    47, 55, 0,
    name="NortheastAltusPlateau_NE_NE",
    variable_name="NORTHEAST_ALTUS_PLATEAU_NE_NE",
    verbose_name="Northeast Altus Plateau (NE) (NE)",
    sites_of_grace=(),
    markers=(
        "Yelough Anix Tunnel (Tunnel)"
        "Yelough Anix Ruins (Ruins)",
    ),
    parent_tile=NORTHEAST_ALTUS_PLATEAU_NE,
)

WEST_CONSECRATED_SNOWFIELD = MapTile(  # LARGE
    11, 14, 2,
    name="WestConsecratedSnowfield",
    variable_name="WEST_CONSECRATED_SNOWFIELD",
    verbose_name="West Consecrated Snowfield",
)
WEST_CONSECRATED_SNOWFIELD_SE = MapTile(  # MEDIUM
    23, 28, 1,
    name="WestConsecratedSnowfield_SE",
    variable_name="WEST_CONSECRATED_SNOWFIELD_SE",
    verbose_name="West Consecrated Snowfield (SE)",
    parent_tile=WEST_CONSECRATED_SNOWFIELD,
)
WEST_CONSECRATED_SNOWFIELD_SE_NW = MapTile(  # SMALL
    46, 57, 0,
    name="WestConsecratedSnowfield_SE_NW",
    variable_name="WEST_CONSECRATED_SNOWFIELD_SE_NW",
    verbose_name="West Consecrated Snowfield (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_CONSECRATED_SNOWFIELD_SE,
)
WEST_CONSECRATED_SNOWFIELD_SE_SE = MapTile(  # SMALL
    47, 56, 0,
    name="WestConsecratedSnowfield_SE_SE",
    variable_name="WEST_CONSECRATED_SNOWFIELD_SE_SE",
    verbose_name="West Consecrated Snowfield (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_CONSECRATED_SNOWFIELD_SE,
)
WEST_CONSECRATED_SNOWFIELD_SE_NE = MapTile(  # SMALL
    47, 57, 0,
    name="WestConsecratedSnowfield_SE_NE",
    variable_name="WEST_CONSECRATED_SNOWFIELD_SE_NE",
    verbose_name="West Consecrated Snowfield (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=WEST_CONSECRATED_SNOWFIELD_SE,
)
WEST_CONSECRATED_SNOWFIELD_NE = MapTile(  # MEDIUM
    23, 29, 1,
    name="WestConsecratedSnowfield_NE",
    variable_name="WEST_CONSECRATED_SNOWFIELD_NE",
    verbose_name="West Consecrated Snowfield (NE)",
    parent_tile=WEST_CONSECRATED_SNOWFIELD,
)
WEST_CONSECRATED_SNOWFIELD_NE_SE = MapTile(  # SMALL
    47, 58, 0,
    name="WestConsecratedSnowfield_NE_SE",
    variable_name="WEST_CONSECRATED_SNOWFIELD_NE_SE",
    verbose_name="West Consecrated Snowfield (NE) (SE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Consecrated Snowfield - Apostate Derelict",
    ),
    markers=(
        "Apostate Derelict (Church)",
    ),
    parent_tile=WEST_CONSECRATED_SNOWFIELD_NE,
)

FAR_SOUTH_CAELID = MapTile(  # LARGE
    12, 8, 2,
    name="FarSouthCaelid",
    variable_name="FAR_SOUTH_CAELID",
    verbose_name="Far South Caelid",
)
FAR_SOUTH_CAELID_NE = MapTile(  # MEDIUM
    25, 17, 1,
    name="FarSouthCaelid_NE",
    variable_name="FAR_SOUTH_CAELID_NE",
    verbose_name="Far South Caelid (NE)",
    parent_tile=FAR_SOUTH_CAELID,
)
FAR_SOUTH_CAELID_NE_NE = MapTile(  # SMALL
    51, 35, 0,
    name="FarSouthCaelid_NE_NE",
    variable_name="FAR_SOUTH_CAELID_NE_NE",
    verbose_name="Far South Caelid (NE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=FAR_SOUTH_CAELID_NE,
)

SOUTH_CAELID = MapTile(  # LARGE
    12, 9, 2,
    name="SouthCaelid",
    variable_name="SOUTH_CAELID",
    verbose_name="South Caelid",
)
SOUTH_CAELID_SW = MapTile(  # MEDIUM
    24, 18, 1,
    name="SouthCaelid_SW",
    variable_name="SOUTH_CAELID_SW",
    verbose_name="South Caelid (SW)",
    parent_tile=SOUTH_CAELID,
)
SOUTH_CAELID_SW_SW = MapTile(  # SMALL
    48, 36, 0,
    name="SouthCaelid_SW_SW",
    variable_name="SOUTH_CAELID_SW_SW",
    verbose_name="South Caelid (SW) (SW)",
    sites_of_grace=(
        "Caelid - Cathedral of Dragon Communion",
    ),
    markers=(
        "Cathedral of Dragon Communion (Church)",
    ),
    parent_tile=SOUTH_CAELID_SW,
)
SOUTH_CAELID_SW_NW = MapTile(  # SMALL
    48, 37, 0,
    name="SouthCaelid_SW_NW",
    variable_name="SOUTH_CAELID_SW_NW",
    verbose_name="South Caelid (SW) (NW)",
    sites_of_grace=(
        "Caelid - Caelid Highway South",
    ),
    markers=(),
    parent_tile=SOUTH_CAELID_SW,
)
SOUTH_CAELID_SW_SE = MapTile(  # SMALL
    49, 36, 0,
    name="SouthCaelid_SW_SE",
    variable_name="SOUTH_CAELID_SW_SE",
    verbose_name="South Caelid (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_CAELID_SW,
)
SOUTH_CAELID_SW_NE = MapTile(  # SMALL
    49, 37, 0,
    name="SouthCaelid_SW_NE",
    variable_name="SOUTH_CAELID_SW_NE",
    verbose_name="South Caelid (SW) (NE)",
    sites_of_grace=(
        "Caelid - Southern Aeonia Swamp Bank",
    ),
    markers=(),
    parent_tile=SOUTH_CAELID_SW,
)
SOUTH_CAELID_NW = MapTile(  # MEDIUM
    24, 19, 1,
    name="SouthCaelid_NW",
    variable_name="SOUTH_CAELID_NW",
    verbose_name="South Caelid (NW)",
    parent_tile=SOUTH_CAELID,
)
SOUTH_CAELID_NW_SW = MapTile(  # SMALL
    48, 38, 0,
    name="SouthCaelid_NW_SW",
    variable_name="SOUTH_CAELID_NW_SW",
    verbose_name="South Caelid (NW) (SW)",
    sites_of_grace=(
        "Caelid - Swamp of Aeonia - Aeonia Swamp Shore"
        "Caelid - Swamp of Aeonia - Astray from Caelid Highway North",
    ),
    markers=(
        "Street of Sages Ruins (Ruins)",
    ),
    parent_tile=SOUTH_CAELID_NW,
)
SOUTH_CAELID_NW_NW = MapTile(  # SMALL
    48, 39, 0,
    name="SouthCaelid_NW_NW",
    variable_name="SOUTH_CAELID_NW_NW",
    verbose_name="South Caelid (NW) (NW)",
    sites_of_grace=(
        "Caelid - Smoldering Wall",
    ),
    markers=(),
    parent_tile=SOUTH_CAELID_NW,
)
SOUTH_CAELID_NW_SE = MapTile(  # SMALL
    49, 38, 0,
    name="SouthCaelid_NW_SE",
    variable_name="SOUTH_CAELID_NW_SE",
    verbose_name="South Caelid (NW) (SE)",
    sites_of_grace=(
        "Caelid - Swamp of Aeonia - Heart of Aeonia"
        "Caelid - Swamp of Aeonia - Inner Aeonia",
    ),
    markers=(
        "Swamp Lookout Tower (Tower)"
        "Sellia Gateway (Gate)",
    ),
    parent_tile=SOUTH_CAELID_NW,
)
SOUTH_CAELID_NW_NE = MapTile(  # SMALL
    49, 39, 0,
    name="SouthCaelid_NW_NE",
    variable_name="SOUTH_CAELID_NW_NE",
    verbose_name="South Caelid (NW) (NE)",
    sites_of_grace=(
        "Caelid - Sellia Backstreets"
        "Caelid - Chair-Crypt of Sellia"
        "Caelid - Sellia Under-Stair",
    ),
    markers=(
        "Sellia Evergaol (Evergaol)",
    ),
    parent_tile=SOUTH_CAELID_NW,
)
SOUTH_CAELID_SE = MapTile(  # MEDIUM
    25, 18, 1,
    name="SouthCaelid_SE",
    variable_name="SOUTH_CAELID_SE",
    verbose_name="South Caelid (SE)",
    parent_tile=SOUTH_CAELID,
)
SOUTH_CAELID_SE_SW = MapTile(  # SMALL
    50, 36, 0,
    name="SouthCaelid_SE_SW",
    variable_name="SOUTH_CAELID_SE_SW",
    verbose_name="South Caelid (SE) (SW)",
    sites_of_grace=(
        "Caelid - Impassable Greatbridge",
    ),
    markers=(),
    parent_tile=SOUTH_CAELID_SE,
)
SOUTH_CAELID_SE_NW = MapTile(  # SMALL
    50, 37, 0,
    name="SouthCaelid_SE_NW",
    variable_name="SOUTH_CAELID_SE_NW",
    verbose_name="South Caelid (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_CAELID_SE,
)
SOUTH_CAELID_SE_SE = MapTile(  # SMALL
    51, 36, 0,
    name="SouthCaelid_SE_SE",
    variable_name="SOUTH_CAELID_SE_SE",
    verbose_name="South Caelid (SE) (SE)",
    sites_of_grace=(
        "Caelid - Redmane Castle Plaza"
        "Caelid - Chamber Outside the Plaza",
    ),
    markers=(
        "Redmane Castle (Unique)",
    ),
    parent_tile=SOUTH_CAELID_SE,
)
SOUTH_CAELID_SE_NE = MapTile(  # SMALL
    51, 37, 0,
    name="SouthCaelid_SE_NE",
    variable_name="SOUTH_CAELID_SE_NE",
    verbose_name="South Caelid (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_CAELID_SE,
)
SOUTH_CAELID_NE = MapTile(  # MEDIUM
    25, 19, 1,
    name="SouthCaelid_NE",
    variable_name="SOUTH_CAELID_NE",
    verbose_name="South Caelid (NE)",
    parent_tile=SOUTH_CAELID,
)
SOUTH_CAELID_NE_SW = MapTile(  # SMALL
    50, 38, 0,
    name="SouthCaelid_NE_SW",
    variable_name="SOUTH_CAELID_NE_SW",
    verbose_name="South Caelid (NE) (SW)",
    sites_of_grace=(
        "Caelid - Church of the Plague",
    ),
    markers=(
        "Gowry's Shack (Shack)",
    ),
    parent_tile=SOUTH_CAELID_NE,
)
SOUTH_CAELID_NE_NW = MapTile(  # SMALL
    50, 39, 0,
    name="SouthCaelid_NE_NW",
    variable_name="SOUTH_CAELID_NE_NW",
    verbose_name="South Caelid (NE) (NW)",
    sites_of_grace=(),
    markers=(
        "Church of the Plague (Church)"
        "Sellia, Town of Sorcery (Unique)",
    ),
    parent_tile=SOUTH_CAELID_NE,
)
SOUTH_CAELID_NE_SE = MapTile(  # SMALL
    51, 38, 0,
    name="SouthCaelid_NE_SE",
    variable_name="SOUTH_CAELID_NE_SE",
    verbose_name="South Caelid (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTH_CAELID_NE,
)
SOUTH_CAELID_NE_NE = MapTile(  # SMALL
    51, 39, 0,
    name="SouthCaelid_NE_NE",
    variable_name="SOUTH_CAELID_NE_NE",
    verbose_name="South Caelid (NE) (NE)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Fort Faroth",
    ),
    markers=(
        "Fort Faroth (Fort)",
    ),
    parent_tile=SOUTH_CAELID_NE,
)

NORTH_CAELID = MapTile(  # LARGE
    12, 10, 2,
    name="NorthCaelid",
    variable_name="NORTH_CAELID",
    verbose_name="North Caelid",
)
NORTH_CAELID_SW = MapTile(  # MEDIUM
    24, 20, 1,
    name="NorthCaelid_SW",
    variable_name="NORTH_CAELID_SW",
    verbose_name="North Caelid (SW)",
    parent_tile=NORTH_CAELID,
)
NORTH_CAELID_SW_SW = MapTile(  # SMALL
    48, 40, 0,
    name="NorthCaelid_SW_SW",
    variable_name="NORTH_CAELID_SW_SW",
    verbose_name="North Caelid (SW) (SW)",
    sites_of_grace=(
        "Caelid - Deep Siofra Well"
        "Caelid - Greyoll's Dragonbarrow - Dragonbarrow West",
    ),
    markers=(),
    parent_tile=NORTH_CAELID_SW,
)
NORTH_CAELID_SW_NW = MapTile(  # SMALL
    48, 41, 0,
    name="NorthCaelid_SW_NW",
    variable_name="NORTH_CAELID_SW_NW",
    verbose_name="North Caelid (SW) (NW)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Isolated Merchant's Shack",
    ),
    markers=(
        "Isolated Merchant's Shack (Shack)",
    ),
    parent_tile=NORTH_CAELID_SW,
)
NORTH_CAELID_SW_SE = MapTile(  # SMALL
    49, 40, 0,
    name="NorthCaelid_SW_SE",
    variable_name="NORTH_CAELID_SW_SE",
    verbose_name="North Caelid (SW) (SE)",
    sites_of_grace=(),
    markers=(
        "Deep Siofra Well (Well)",
    ),
    parent_tile=NORTH_CAELID_SW,
)
NORTH_CAELID_SW_NE = MapTile(  # SMALL
    49, 41, 0,
    name="NorthCaelid_SW_NE",
    variable_name="NORTH_CAELID_SW_NE",
    verbose_name="North Caelid (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_CAELID_SW,
)
NORTH_CAELID_SE = MapTile(  # MEDIUM
    25, 20, 1,
    name="NorthCaelid_SE",
    variable_name="NORTH_CAELID_SE",
    verbose_name="North Caelid (SE)",
    parent_tile=NORTH_CAELID,
)
NORTH_CAELID_SE_SW = MapTile(  # SMALL
    50, 40, 0,
    name="NorthCaelid_SE_SW",
    variable_name="NORTH_CAELID_SE_SW",
    verbose_name="North Caelid (SE) (SW)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Dragonbarrow Fork",
    ),
    markers=(),
    parent_tile=NORTH_CAELID_SE,
)
NORTH_CAELID_SE_NW = MapTile(  # SMALL
    50, 41, 0,
    name="NorthCaelid_SE_NW",
    variable_name="NORTH_CAELID_SE_NW",
    verbose_name="North Caelid (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_CAELID_SE,
)
NORTH_CAELID_SE_SE = MapTile(  # SMALL
    51, 40, 0,
    name="NorthCaelid_SE_SE",
    variable_name="NORTH_CAELID_SE_SE",
    verbose_name="North Caelid (SE) (SE)",
    sites_of_grace=(),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=NORTH_CAELID_SE,
)
NORTH_CAELID_SE_NE = MapTile(  # SMALL
    51, 41, 0,
    name="NorthCaelid_SE_NE",
    variable_name="NORTH_CAELID_SE_NE",
    verbose_name="North Caelid (SE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_CAELID_SE,
)
NORTH_CAELID_NE = MapTile(  # MEDIUM
    25, 21, 1,
    name="NorthCaelid_NE",
    variable_name="NORTH_CAELID_NE",
    verbose_name="North Caelid (NE)",
    parent_tile=NORTH_CAELID,
)
NORTH_CAELID_NE_SE = MapTile(  # SMALL
    51, 42, 0,
    name="NorthCaelid_NE_SE",
    variable_name="NORTH_CAELID_NE_SE",
    verbose_name="North Caelid (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTH_CAELID_NE,
)
NORTH_CAELID_NE_NE = MapTile(  # SMALL
    51, 43, 0,
    name="NorthCaelid_NE_NE",
    variable_name="NORTH_CAELID_NE_NE",
    verbose_name="North Caelid (NE) (NE)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Bestial Sanctum",
    ),
    markers=(
        "Bestial Sanctum (Unique)",
    ),
    parent_tile=NORTH_CAELID_NE,
)

FORBIDDEN_LANDS = MapTile(  # LARGE
    12, 12, 2,
    name="ForbiddenLands",
    variable_name="FORBIDDEN_LANDS",
    verbose_name="Forbidden Lands",
)
FORBIDDEN_LANDS_NW = MapTile(  # MEDIUM
    24, 25, 1,
    name="ForbiddenLands_NW",
    variable_name="FORBIDDEN_LANDS_NW",
    verbose_name="Forbidden Lands (NW)",
    parent_tile=FORBIDDEN_LANDS,
)
FORBIDDEN_LANDS_NW_NW = MapTile(  # SMALL
    48, 51, 0,
    name="ForbiddenLands_NW_NW",
    variable_name="FORBIDDEN_LANDS_NW_NW",
    verbose_name="Forbidden Lands (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=FORBIDDEN_LANDS_NW,
)

SOUTHWEST_MOUNTAINTOPS = MapTile(  # LARGE
    12, 13, 2,
    name="SouthwestMountaintops",
    variable_name="SOUTHWEST_MOUNTAINTOPS",
    verbose_name="Southwest Mountaintops",
)
SOUTHWEST_MOUNTAINTOPS_SW = MapTile(  # MEDIUM
    24, 26, 1,
    name="SouthwestMountaintops_SW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SW",
    verbose_name="Southwest Mountaintops (SW)",
    parent_tile=SOUTHWEST_MOUNTAINTOPS,
)
SOUTHWEST_MOUNTAINTOPS_SW_SE = MapTile(  # SMALL
    49, 52, 0,
    name="SouthwestMountaintops_SW_SE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SW_SE",
    verbose_name="Southwest Mountaintops (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_SW,
)
SOUTHWEST_MOUNTAINTOPS_SW_NE = MapTile(  # SMALL
    49, 53, 0,
    name="SouthwestMountaintops_SW_NE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SW_NE",
    verbose_name="Southwest Mountaintops (SW) (NE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Zamor Ruins"
        "Mountaintops of the Giants - Forbidden Lands - Grand Lift of Rold",
    ),
    markers=(
        "Zamor Ruins (Ruins)"
        "Grand Lift of Rold (Lift)",
    ),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_SW,
)
SOUTHWEST_MOUNTAINTOPS_NW = MapTile(  # MEDIUM
    24, 27, 1,
    name="SouthwestMountaintops_NW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NW",
    verbose_name="Southwest Mountaintops (NW)",
    parent_tile=SOUTHWEST_MOUNTAINTOPS,
)
SOUTHWEST_MOUNTAINTOPS_NW_SW = MapTile(  # SMALL
    48, 54, 0,
    name="SouthwestMountaintops_NW_SW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NW_SW",
    verbose_name="Southwest Mountaintops (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NW,
)
SOUTHWEST_MOUNTAINTOPS_NW_NW = MapTile(  # SMALL
    48, 55, 0,
    name="SouthwestMountaintops_NW_NW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NW_NW",
    verbose_name="Southwest Mountaintops (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NW,
)
SOUTHWEST_MOUNTAINTOPS_NW_SE = MapTile(  # SMALL
    49, 54, 0,
    name="SouthwestMountaintops_NW_SE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NW_SE",
    verbose_name="Southwest Mountaintops (NW) (SE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Consecrated Snowfield - Consecrated Snowfield",
    ),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NW,
)
SOUTHWEST_MOUNTAINTOPS_NW_NE = MapTile(  # SMALL
    49, 55, 0,
    name="SouthwestMountaintops_NW_NE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NW_NE",
    verbose_name="Southwest Mountaintops (NW) (NE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Consecrated Snowfield - Inner Consecrated Snowfield",
    ),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NW,
)
SOUTHWEST_MOUNTAINTOPS_SE = MapTile(  # MEDIUM
    25, 26, 1,
    name="SouthwestMountaintops_SE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SE",
    verbose_name="Southwest Mountaintops (SE)",
    parent_tile=SOUTHWEST_MOUNTAINTOPS,
)
SOUTHWEST_MOUNTAINTOPS_SE_NW = MapTile(  # SMALL
    50, 53, 0,
    name="SouthwestMountaintops_SE_NW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SE_NW",
    verbose_name="Southwest Mountaintops (SE) (NW)",
    sites_of_grace=(),
    markers=(
        "Giant-Conquering Hero's Grave (Grave)"
        "Giants' Mountaintop Catacombs (Catacombs)",
    ),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_SE,
)
SOUTHWEST_MOUNTAINTOPS_SE_SE = MapTile(  # SMALL
    51, 52, 0,
    name="SouthwestMountaintops_SE_SE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SE_SE",
    verbose_name="Southwest Mountaintops (SE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_SE,
)
SOUTHWEST_MOUNTAINTOPS_SE_NE = MapTile(  # SMALL
    51, 53, 0,
    name="SouthwestMountaintops_SE_NE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_SE_NE",
    verbose_name="Southwest Mountaintops (SE) (NE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Flame Peak - Church of Repose",
    ),
    markers=(
        "Church of Repose (Church)",
    ),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_SE,
)
SOUTHWEST_MOUNTAINTOPS_NE = MapTile(  # MEDIUM
    25, 27, 1,
    name="SouthwestMountaintops_NE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NE",
    verbose_name="Southwest Mountaintops (NE)",
    parent_tile=SOUTHWEST_MOUNTAINTOPS,
)
SOUTHWEST_MOUNTAINTOPS_NE_SW = MapTile(  # SMALL
    50, 54, 0,
    name="SouthwestMountaintops_NE_SW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NE_SW",
    verbose_name="Southwest Mountaintops (NE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NE,
)
SOUTHWEST_MOUNTAINTOPS_NE_NW = MapTile(  # SMALL
    50, 55, 0,
    name="SouthwestMountaintops_NE_NW",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NE_NW",
    verbose_name="Southwest Mountaintops (NE) (NW)",
    sites_of_grace=(),
    markers=(
        "Consecrated Snowfield Catacombs (Catacombs)",
    ),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NE,
)
SOUTHWEST_MOUNTAINTOPS_NE_SE = MapTile(  # SMALL
    51, 54, 0,
    name="SouthwestMountaintops_NE_SE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NE_SE",
    verbose_name="Southwest Mountaintops (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NE,
)
SOUTHWEST_MOUNTAINTOPS_NE_NE = MapTile(  # SMALL
    51, 55, 0,
    name="SouthwestMountaintops_NE_NE",
    variable_name="SOUTHWEST_MOUNTAINTOPS_NE_NE",
    verbose_name="Southwest Mountaintops (NE) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHWEST_MOUNTAINTOPS_NE,
)

NORTHWEST_MOUNTAINTOPS = MapTile(  # LARGE
    12, 14, 2,
    name="NorthwestMountaintops",
    variable_name="NORTHWEST_MOUNTAINTOPS",
    verbose_name="Northwest Mountaintops",
)
NORTHWEST_MOUNTAINTOPS_SW = MapTile(  # MEDIUM
    24, 28, 1,
    name="NorthwestMountaintops_SW",
    variable_name="NORTHWEST_MOUNTAINTOPS_SW",
    verbose_name="Northwest Mountaintops (SW)",
    parent_tile=NORTHWEST_MOUNTAINTOPS,
)
NORTHWEST_MOUNTAINTOPS_SW_SW = MapTile(  # SMALL
    48, 56, 0,
    name="NorthwestMountaintops_SW_SW",
    variable_name="NORTHWEST_MOUNTAINTOPS_SW_SW",
    verbose_name="Northwest Mountaintops (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SW,
)
NORTHWEST_MOUNTAINTOPS_SW_NW = MapTile(  # SMALL
    48, 57, 0,
    name="NorthwestMountaintops_SW_NW",
    variable_name="NORTHWEST_MOUNTAINTOPS_SW_NW",
    verbose_name="Northwest Mountaintops (SW) (NW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Consecrated Snowfield - Ordina, Liturgical Town",
    ),
    markers=(
        "Ordina, Liturgical Town (Unique)",
    ),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SW,
)
NORTHWEST_MOUNTAINTOPS_SW_SE = MapTile(  # SMALL
    49, 56, 0,
    name="NorthwestMountaintops_SW_SE",
    variable_name="NORTHWEST_MOUNTAINTOPS_SW_SE",
    verbose_name="Northwest Mountaintops (SW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SW,
)
NORTHWEST_MOUNTAINTOPS_SW_NE = MapTile(  # SMALL
    49, 57, 0,
    name="NorthwestMountaintops_SW_NE",
    variable_name="NORTHWEST_MOUNTAINTOPS_SW_NE",
    verbose_name="Northwest Mountaintops (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SW,
)
NORTHWEST_MOUNTAINTOPS_NW = MapTile(  # MEDIUM
    24, 29, 1,
    name="NorthwestMountaintops_NW",
    variable_name="NORTHWEST_MOUNTAINTOPS_NW",
    verbose_name="Northwest Mountaintops (NW)",
    parent_tile=NORTHWEST_MOUNTAINTOPS,
)
NORTHWEST_MOUNTAINTOPS_NW_SW = MapTile(  # SMALL
    48, 58, 0,
    name="NorthwestMountaintops_NW_SW",
    variable_name="NORTHWEST_MOUNTAINTOPS_NW_SW",
    verbose_name="Northwest Mountaintops (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_NW,
)
NORTHWEST_MOUNTAINTOPS_SE = MapTile(  # MEDIUM
    25, 28, 1,
    name="NorthwestMountaintops_SE",
    variable_name="NORTHWEST_MOUNTAINTOPS_SE",
    verbose_name="Northwest Mountaintops (SE)",
    parent_tile=NORTHWEST_MOUNTAINTOPS,
)
NORTHWEST_MOUNTAINTOPS_SE_SW = MapTile(  # SMALL
    50, 56, 0,
    name="NorthwestMountaintops_SE_SW",
    variable_name="NORTHWEST_MOUNTAINTOPS_SE_SW",
    verbose_name="Northwest Mountaintops (SE) (SW)",
    sites_of_grace=(),
    markers=(
        "Shack of the Lofty (Shack)"
        "Minor Erdtree (Erdtree)"
        "Albinauric Rise (Rise)",
    ),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SE,
)
NORTHWEST_MOUNTAINTOPS_SE_NW = MapTile(  # SMALL
    50, 57, 0,
    name="NorthwestMountaintops_SE_NW",
    variable_name="NORTHWEST_MOUNTAINTOPS_SE_NW",
    verbose_name="Northwest Mountaintops (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SE,
)
NORTHWEST_MOUNTAINTOPS_SE_SE = MapTile(  # SMALL
    51, 56, 0,
    name="NorthwestMountaintops_SE_SE",
    variable_name="NORTHWEST_MOUNTAINTOPS_SE_SE",
    verbose_name="Northwest Mountaintops (SE) (SE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Ancient Snow Valley Ruins",
    ),
    markers=(
        "Stargazers' Ruins (Ruins)",
    ),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SE,
)
NORTHWEST_MOUNTAINTOPS_SE_NE = MapTile(  # SMALL
    51, 57, 0,
    name="NorthwestMountaintops_SE_NE",
    variable_name="NORTHWEST_MOUNTAINTOPS_SE_NE",
    verbose_name="Northwest Mountaintops (SE) (NE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Snow Valley Ruins Overlook"
        "Mountaintops of the Giants - Castle Sol Main Gate"
        "Mountaintops of the Giants - Church of the Eclipse"
        "Mountaintops of the Giants - Castle Sol Rooftop",
    ),
    markers=(
        "Castle Sol (Unique)",
    ),
    parent_tile=NORTHWEST_MOUNTAINTOPS_SE,
)
NORTHWEST_MOUNTAINTOPS_NE = MapTile(  # MEDIUM
    25, 29, 1,
    name="NorthwestMountaintops_NE",
    variable_name="NORTHWEST_MOUNTAINTOPS_NE",
    verbose_name="Northwest Mountaintops (NE)",
    parent_tile=NORTHWEST_MOUNTAINTOPS,
)
NORTHWEST_MOUNTAINTOPS_NE_SE = MapTile(  # SMALL
    51, 58, 0,
    name="NorthwestMountaintops_NE_SE",
    variable_name="NORTHWEST_MOUNTAINTOPS_NE_SE",
    verbose_name="Northwest Mountaintops (NE) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHWEST_MOUNTAINTOPS_NE,
)

SOUTHEAST_CAELID = MapTile(  # LARGE
    13, 9, 2,
    name="SoutheastCaelid",
    variable_name="SOUTHEAST_CAELID",
    verbose_name="Southeast Caelid",
)
SOUTHEAST_CAELID_SW = MapTile(  # MEDIUM
    26, 18, 1,
    name="SoutheastCaelid_SW",
    variable_name="SOUTHEAST_CAELID_SW",
    verbose_name="Southeast Caelid (SW)",
    parent_tile=SOUTHEAST_CAELID,
)
SOUTHEAST_CAELID_SW_NW = MapTile(  # SMALL
    52, 37, 0,
    name="SoutheastCaelid_SW_NW",
    variable_name="SOUTHEAST_CAELID_SW_NW",
    verbose_name="Southeast Caelid (SW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_CAELID_SW,
)
SOUTHEAST_CAELID_NW = MapTile(  # MEDIUM
    26, 19, 1,
    name="SoutheastCaelid_NW",
    variable_name="SOUTHEAST_CAELID_NW",
    verbose_name="Southeast Caelid (NW)",
    parent_tile=SOUTHEAST_CAELID,
)
SOUTHEAST_CAELID_NW_SW = MapTile(  # SMALL
    52, 38, 0,
    name="SoutheastCaelid_NW_SW",
    variable_name="SOUTHEAST_CAELID_NW_SW",
    verbose_name="Southeast Caelid (NW) (SW)",
    sites_of_grace=(
        "Caelid - Starscourge Radahn",
    ),
    markers=(),
    parent_tile=SOUTHEAST_CAELID_NW,
)
SOUTHEAST_CAELID_NW_NW = MapTile(  # SMALL
    52, 39, 0,
    name="SoutheastCaelid_NW_NW",
    variable_name="SOUTHEAST_CAELID_NW_NW",
    verbose_name="Southeast Caelid (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_CAELID_NW,
)
SOUTHEAST_CAELID_NW_SE = MapTile(  # SMALL
    53, 38, 0,
    name="SoutheastCaelid_NW_SE",
    variable_name="SOUTHEAST_CAELID_NW_SE",
    verbose_name="Southeast Caelid (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_CAELID_NW,
)
SOUTHEAST_CAELID_NW_NE = MapTile(  # SMALL
    53, 39, 0,
    name="SoutheastCaelid_NW_NE",
    variable_name="SOUTHEAST_CAELID_NW_NE",
    verbose_name="Southeast Caelid (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_CAELID_NW,
)

NORTHEAST_CAELID = MapTile(  # LARGE
    13, 10, 2,
    name="NortheastCaelid",
    variable_name="NORTHEAST_CAELID",
    verbose_name="Northeast Caelid",
)
NORTHEAST_CAELID_SW = MapTile(  # MEDIUM
    26, 20, 1,
    name="NortheastCaelid_SW",
    variable_name="NORTHEAST_CAELID_SW",
    verbose_name="Northeast Caelid (SW)",
    parent_tile=NORTHEAST_CAELID,
)
NORTHEAST_CAELID_SW_SW = MapTile(  # SMALL
    52, 40, 0,
    name="NortheastCaelid_SW_SW",
    variable_name="NORTHEAST_CAELID_SW_SW",
    verbose_name="Northeast Caelid (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_CAELID_SW,
)
NORTHEAST_CAELID_SW_NW = MapTile(  # SMALL
    52, 41, 0,
    name="NortheastCaelid_SW_NW",
    variable_name="NORTHEAST_CAELID_SW_NW",
    verbose_name="Northeast Caelid (SW) (NW)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Lenne's Rise",
    ),
    markers=(
        "Lenne's Rise (Rise)",
    ),
    parent_tile=NORTHEAST_CAELID_SW,
)
NORTHEAST_CAELID_NW = MapTile(  # MEDIUM
    26, 21, 1,
    name="NortheastCaelid_NW",
    variable_name="NORTHEAST_CAELID_NW",
    verbose_name="Northeast Caelid (NW)",
    parent_tile=NORTHEAST_CAELID,
)
NORTHEAST_CAELID_NW_SW = MapTile(  # SMALL
    52, 42, 0,
    name="NortheastCaelid_NW_SW",
    variable_name="NORTHEAST_CAELID_NW_SW",
    verbose_name="Northeast Caelid (NW) (SW)",
    sites_of_grace=(
        "Caelid - Greyoll's Dragonbarrow - Farum Greatbridge",
    ),
    markers=(),
    parent_tile=NORTHEAST_CAELID_NW,
)
NORTHEAST_CAELID_NW_NW = MapTile(  # SMALL
    52, 43, 0,
    name="NortheastCaelid_NW_NW",
    variable_name="NORTHEAST_CAELID_NW_NW",
    verbose_name="Northeast Caelid (NW) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_CAELID_NW,
)

SOUTHEAST_MOUNTAINTOPS = MapTile(  # LARGE
    13, 13, 2,
    name="SoutheastMountaintops",
    variable_name="SOUTHEAST_MOUNTAINTOPS",
    verbose_name="Southeast Mountaintops",
)
SOUTHEAST_MOUNTAINTOPS_SW = MapTile(  # MEDIUM
    26, 26, 1,
    name="SoutheastMountaintops_SW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SW",
    verbose_name="Southeast Mountaintops (SW)",
    parent_tile=SOUTHEAST_MOUNTAINTOPS,
)
SOUTHEAST_MOUNTAINTOPS_SW_SW = MapTile(  # SMALL
    52, 52, 0,
    name="SoutheastMountaintops_SW_SW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SW_SW",
    verbose_name="Southeast Mountaintops (SW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_SW,
)
SOUTHEAST_MOUNTAINTOPS_SW_NW = MapTile(  # SMALL
    52, 53, 0,
    name="SoutheastMountaintops_SW_NW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SW_NW",
    verbose_name="Southeast Mountaintops (SW) (NW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Flame Peak - Foot of the Forge",
    ),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_SW,
)
SOUTHEAST_MOUNTAINTOPS_SW_SE = MapTile(  # SMALL
    53, 52, 0,
    name="SoutheastMountaintops_SW_SE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SW_SE",
    verbose_name="Southeast Mountaintops (SW) (SE)",
    sites_of_grace=(
        "Mountaintops of the Giants - Flame Peak - Fire Giant",
    ),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_SW,
)
SOUTHEAST_MOUNTAINTOPS_SW_NE = MapTile(  # SMALL
    53, 53, 0,
    name="SoutheastMountaintops_SW_NE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SW_NE",
    verbose_name="Southeast Mountaintops (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_SW,
)
SOUTHEAST_MOUNTAINTOPS_NW = MapTile(  # MEDIUM
    26, 27, 1,
    name="SoutheastMountaintops_NW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NW",
    verbose_name="Southeast Mountaintops (NW)",
    parent_tile=SOUTHEAST_MOUNTAINTOPS,
)
SOUTHEAST_MOUNTAINTOPS_NW_SW = MapTile(  # SMALL
    52, 54, 0,
    name="SoutheastMountaintops_NW_SW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NW_SW",
    verbose_name="Southeast Mountaintops (NW) (SW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Flame Peak - Giants' Gravepost",
    ),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_NW,
)
SOUTHEAST_MOUNTAINTOPS_NW_NW = MapTile(  # SMALL
    52, 55, 0,
    name="SoutheastMountaintops_NW_NW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NW_NW",
    verbose_name="Southeast Mountaintops (NW) (NW)",
    sites_of_grace=(),
    markers=(
        "Guardians' Garrison (Fort)",
    ),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_NW,
)
SOUTHEAST_MOUNTAINTOPS_NW_SE = MapTile(  # SMALL
    53, 54, 0,
    name="SoutheastMountaintops_NW_SE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NW_SE",
    verbose_name="Southeast Mountaintops (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_NW,
)
SOUTHEAST_MOUNTAINTOPS_NW_NE = MapTile(  # SMALL
    53, 55, 0,
    name="SoutheastMountaintops_NW_NE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NW_NE",
    verbose_name="Southeast Mountaintops (NW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_NW,
)
SOUTHEAST_MOUNTAINTOPS_SE = MapTile(  # MEDIUM
    27, 26, 1,
    name="SoutheastMountaintops_SE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SE",
    verbose_name="Southeast Mountaintops (SE)",
    parent_tile=SOUTHEAST_MOUNTAINTOPS,
)
SOUTHEAST_MOUNTAINTOPS_SE_NW = MapTile(  # SMALL
    54, 53, 0,
    name="SoutheastMountaintops_SE_NW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_SE_NW",
    verbose_name="Southeast Mountaintops (SE) (NW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Flame Peak - Forge of the Giants",
    ),
    markers=(
        "Forge of the Giants (Unique)",
    ),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_SE,
)
SOUTHEAST_MOUNTAINTOPS_NE = MapTile(  # MEDIUM
    27, 27, 1,
    name="SoutheastMountaintops_NE",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NE",
    verbose_name="Southeast Mountaintops (NE)",
    parent_tile=SOUTHEAST_MOUNTAINTOPS,
)
SOUTHEAST_MOUNTAINTOPS_NE_NW = MapTile(  # SMALL
    54, 55, 0,
    name="SoutheastMountaintops_NE_NW",
    variable_name="SOUTHEAST_MOUNTAINTOPS_NE_NW",
    verbose_name="Southeast Mountaintops (NE) (NW)",
    sites_of_grace=(
        "Mountaintops of the Giants - First Church of Marika",
    ),
    markers=(
        "First Church of Marika (Church)",
    ),
    parent_tile=SOUTHEAST_MOUNTAINTOPS_NE,
)

NORTHEAST_MOUNTAINTOPS = MapTile(  # LARGE
    13, 14, 2,
    name="NortheastMountaintops",
    variable_name="NORTHEAST_MOUNTAINTOPS",
    verbose_name="Northeast Mountaintops",
)
NORTHEAST_MOUNTAINTOPS_SW = MapTile(  # MEDIUM
    26, 28, 1,
    name="NortheastMountaintops_SW",
    variable_name="NORTHEAST_MOUNTAINTOPS_SW",
    verbose_name="Northeast Mountaintops (SW)",
    parent_tile=NORTHEAST_MOUNTAINTOPS,
)
NORTHEAST_MOUNTAINTOPS_SW_SW = MapTile(  # SMALL
    52, 56, 0,
    name="NortheastMountaintops_SW_SW",
    variable_name="NORTHEAST_MOUNTAINTOPS_SW_SW",
    verbose_name="Northeast Mountaintops (SW) (SW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Whiteridge Road",
    ),
    markers=(
        "Minor Erdtree (Erdtree)",
    ),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SW,
)
NORTHEAST_MOUNTAINTOPS_SW_NW = MapTile(  # SMALL
    52, 57, 0,
    name="NortheastMountaintops_SW_NW",
    variable_name="NORTHEAST_MOUNTAINTOPS_SW_NW",
    verbose_name="Northeast Mountaintops (SW) (NW)",
    sites_of_grace=(
        "Mountaintops of the Giants - Freezing Lake",
    ),
    markers=(
        "Heretical Rise (Rise)",
    ),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SW,
)
NORTHEAST_MOUNTAINTOPS_SW_SE = MapTile(  # SMALL
    53, 56, 0,
    name="NortheastMountaintops_SW_SE",
    variable_name="NORTHEAST_MOUNTAINTOPS_SW_SE",
    verbose_name="Northeast Mountaintops (SW) (SE)",
    sites_of_grace=(),
    markers=(
        "Spiritcaller Cave (Cave)"
        "Lord Contender's Evergaol (Evergaol)",
    ),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SW,
)
NORTHEAST_MOUNTAINTOPS_SW_NE = MapTile(  # SMALL
    53, 57, 0,
    name="NortheastMountaintops_SW_NE",
    variable_name="NORTHEAST_MOUNTAINTOPS_SW_NE",
    verbose_name="Northeast Mountaintops (SW) (NE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SW,
)
NORTHEAST_MOUNTAINTOPS_NW = MapTile(  # MEDIUM
    26, 29, 1,
    name="NortheastMountaintops_NW",
    variable_name="NORTHEAST_MOUNTAINTOPS_NW",
    verbose_name="Northeast Mountaintops (NW)",
    parent_tile=NORTHEAST_MOUNTAINTOPS,
)
NORTHEAST_MOUNTAINTOPS_NW_SW = MapTile(  # SMALL
    52, 58, 0,
    name="NortheastMountaintops_NW_SW",
    variable_name="NORTHEAST_MOUNTAINTOPS_NW_SW",
    verbose_name="Northeast Mountaintops (NW) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_MOUNTAINTOPS_NW,
)
NORTHEAST_MOUNTAINTOPS_NW_SE = MapTile(  # SMALL
    53, 58, 0,
    name="NortheastMountaintops_NW_SE",
    variable_name="NORTHEAST_MOUNTAINTOPS_NW_SE",
    verbose_name="Northeast Mountaintops (NW) (SE)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_MOUNTAINTOPS_NW,
)
NORTHEAST_MOUNTAINTOPS_SE = MapTile(  # MEDIUM
    27, 28, 1,
    name="NortheastMountaintops_SE",
    variable_name="NORTHEAST_MOUNTAINTOPS_SE",
    verbose_name="Northeast Mountaintops (SE)",
    parent_tile=NORTHEAST_MOUNTAINTOPS,
)
NORTHEAST_MOUNTAINTOPS_SE_SW = MapTile(  # SMALL
    54, 56, 0,
    name="NortheastMountaintops_SE_SW",
    variable_name="NORTHEAST_MOUNTAINTOPS_SE_SW",
    verbose_name="Northeast Mountaintops (SE) (SW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SE,
)
NORTHEAST_MOUNTAINTOPS_SE_NW = MapTile(  # SMALL
    54, 57, 0,
    name="NortheastMountaintops_SE_NW",
    variable_name="NORTHEAST_MOUNTAINTOPS_SE_NW",
    verbose_name="Northeast Mountaintops (SE) (NW)",
    sites_of_grace=(),
    markers=(),
    parent_tile=NORTHEAST_MOUNTAINTOPS_SE,
)


# ALTERNATE OVERWORLD TILES

EAST_LIMGRAVE_METEOR = MapTile(  # LARGE
    11, 9, 12,
    name="EastLimgraveMeteor",
    variable_name="EAST_LIMGRAVE_METEOR",
    verbose_name="East Limgrave (Meteor)",
    is_alternate=True,
)
EAST_LIMGRAVE_METEOR_SW = MapTile(  # MEDIUM
    22, 18, 11,
    name="EastLimgraveMeteor_SW",
    variable_name="EAST_LIMGRAVE_METEOR_SW",
    verbose_name="East Limgrave (Meteor) (SW)",
    parent_tile=EAST_LIMGRAVE_METEOR,
    is_alternate=True,
)
EAST_LIMGRAVE_METEOR_SW_SE = MapTile(  # SMALL
    45, 36, 10,
    name="EastLimgraveMeteor_SW_SE",
    variable_name="EAST_LIMGRAVE_METEOR_SW_SE",
    verbose_name="East Limgrave (Meteor) (SW) (SE)",
    parent_tile=EAST_LIMGRAVE_METEOR_SW,
    is_alternate=True,
)

NORTHEAST_ALTUS_PLATEAU_ASHEN = MapTile(  # LARGE
    11, 13, 12,
    name="NortheastAltusPlateauAshen",
    variable_name="NORTHEAST_ALTUS_PLATEAU_ASHEN",
    verbose_name="Northeast Altus Plateau (Ashen)",
    is_alternate=True,
)
NORTHEAST_ALTUS_PLATEAU_ASHEN_SW = MapTile(  # MEDIUM
    22, 26, 11,
    name="NortheastAltusPlateauAshen_SW",
    variable_name="NORTHEAST_ALTUS_PLATEAU_ASHEN_SW",
    verbose_name="Northeast Altus Plateau (Ashen) (SW)",
    parent_tile=NORTHEAST_ALTUS_PLATEAU_ASHEN,
    is_alternate=True,
)
NORTHEAST_ALTUS_PLATEAU_ASHEN_SW_SE = MapTile(  # SMALL
    45, 52, 10,
    name="NortheastAltusPlateauAshen_SW_SE",
    variable_name="NORTHEAST_ALTUS_PLATEAU_ASHEN_SW_SE",
    verbose_name="Northeast Altus Plateau (Ashen) (SW) (SE)",
    parent_tile=NORTHEAST_ALTUS_PLATEAU_ASHEN_SW,
    is_alternate=True,
)


def gen_overworld():
    """See for parsed text:

    http://soulsmodding.wikidot.com/reference:elden-ring-map-list
    """
    s = ""  # replace with text from above URL

    lines = s.split("\n")
    i = 0
    large_tile = None
    medium_tile = None
    while i < len(lines):
        line = lines[i]
        # print(line)

        if line.startswith("m60"):
            # Large tile.
            a, b, c, d = [int(x) for x in line[1:12].split("_")]
            if d != 2:
                raise ValueError(f"Expected size ID 2. Line: {line}")
            verbose_name = line.split(": ")[1]
            depunc_name = verbose_name.replace("-", " ").replace("'", "")
            name = "".join(x.capitalize() for x in depunc_name.split(" "))
            variable_name = "_".join(x.upper() for x in depunc_name.split(" "))
            print(f"""
{variable_name} = MapTile(  # LARGE
    {b}, {c}, {d},
    name=\"{name}\",
    variable_name=\"{variable_name}\",
    verbose_name=\"{verbose_name}\",
)""")
            large_tile = (name, variable_name, verbose_name)
            i += 1
        elif line.startswith("("):
            # Medium or small tile.
            a, b, c, d = [int(x) for x in line[6:17].split("_")]
            quadrant = line[1:3]
            if d == 1:
                # Medium tile.
                name = f"{large_tile[0]}_{quadrant}"
                variable_name = f"{large_tile[1]}_{quadrant}"
                verbose_name = f"{large_tile[2]} ({quadrant})"
                print(f"""{variable_name} = MapTile(  # MEDIUM
    {b}, {c}, {d},
    name=\"{name}\",
    variable_name=\"{variable_name}\",
    verbose_name=\"{verbose_name}\",
    parent_tile={large_tile[1]},
)""")
                medium_tile = (name, variable_name, verbose_name)
                i += 1
            elif d == 0:
                # Small tile.
                name = f"{medium_tile[0]}_{quadrant}"
                variable_name = f"{medium_tile[1]}_{quadrant}"
                verbose_name = f"{medium_tile[2]} ({quadrant})"

                # Check next lines for sites of grace and markers.
                sites_of_grace = []
                i += 1
                if lines[i].startswith("Site of Grace: "):
                    sites_of_grace.append(lines[i].split(": ")[1])
                    i += 1
                elif lines[i].startswith("Sites of Grace:"):
                    i += 1
                    while not any(lines[i].startswith(x) for x in ("Marker", "(", "m60", "Connect")):
                        sites_of_grace.append(lines[i])
                        i += 1
                if sites_of_grace:
                    sites_of_grace_str = (
                        "(\n        " + "\n        ".join(f"\"{x}\"" for x in sites_of_grace) + ",\n    )"
                    )
                else:
                    sites_of_grace_str = "()"
                markers = []
                if lines[i].startswith("Marker: "):
                    markers.append(lines[i].split(": ")[1])
                    i += 1
                elif lines[i].startswith("Markers:"):
                    i += 1
                    while not any(lines[i].startswith(x) for x in ("Site", "(", "m60", "Connect")):
                        markers.append(lines[i])
                        i += 1
                if markers:
                    markers_str = "(\n        " + "\n        ".join(f"\"{x}\"" for x in markers) + ",\n    )"
                else:
                    markers_str = "()"

                print(f"""{variable_name} = MapTile(  # SMALL
    {b}, {c}, {d},
    name=\"{name}\",
    variable_name=\"{variable_name}\",
    verbose_name=\"{verbose_name}\",
    sites_of_grace={sites_of_grace_str},
    markers={markers_str},
    parent_tile={medium_tile[1]},
)""")
            else:
                raise ValueError(f"Unexpected tile size: {d}")

        else:
            # Ignore other lines.
            i += 1
