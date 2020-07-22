"""Script that creates the extra DrawParam slot for maps in Dark Souls 1.

In the vanilla game, only map area 15 (Sen's Fortress and Anor Londo) uses the additional DrawParam slot, but it works
for all maps. The slot can be changed with the EMEVD instruction `SetMapDrawParamSlot`, but note that this will affect
all map blocks in that area (e.g. Firelink Shrine, Undead Burg, and the Depths will all change slot together). The slot
is always set to 0 when the map is loaded.

Unfortunately, no more than two slots can be used; the renderer glitches out with insane colors when slot 2 is assigned,
and shows nothing when any other slots are assigned.
"""
import logging
from pathlib import Path

from soulstruct import BND

_LOGGER = logging.getLogger(__name__)


def add_draw_slot_1_to_all_map_areas(game_root_path):
    """Add the second draw slot (slot 1) to all `aXX_DrawParam.parambnd[.dcx]` files that don't already have one."""
    game_root_path = Path(game_root_path)
    for parambnd_path in game_root_path.glob("param/DrawParam"):
        if parambnd_path.name.startswith("a"):
            add_draw_slot_1_to_drawparam(parambnd_path)


def add_draw_slot_1_to_map_area(game_root_path, map_area_id):
    parambnd_path = Path(game_root_path) / f"param/DrawParam/a{map_area_id}_DrawParam.parambnd"
    try:
        return add_draw_slot_1_to_drawparam(parambnd_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not locate DS1 DrawParam file for map area {map_area_id}.")


def add_draw_slot_1_to_drawparam(parambnd_path):
    """Add the second draw slot (slot 1) to the given `aXX_DrawParam.parambnd[.dcx]` file, if it doesn't already have a
    second slot (which only `a15_DrawParam.parambnd` does in vanilla).

    All draw parameters will be copied from slot 0.
    """
    parambnd_path = Path(parambnd_path)
    if not parambnd_path.is_file():
        raise FileNotFoundError(f"Could not locate DrawParam file: {str(parambnd_path)}")
    draw_param = BND(parambnd_path)

    if len(draw_param) != 12:
        _LOGGER.info(f"DrawParam file {str(parambnd_path)} already has more than one slot.")
        return

    try:
        area_id = parambnd_path.name.split("_")[0][1:]
    except IndexError:
        raise ValueError(f"Could not determine map area ID from DrawParam file name: {parambnd_path.name}")

    # slot 1 files ('mXX_1_LightBank') come before slot 0 files ('mXX_LightBank'), which are both before 'sXX_LightBank'
    s_ambient = draw_param[11]
    draw_param.remove_entry(11)
    for i in range(11):
        slot_0 = draw_param[i].copy()
        slot_0.id += 11
        draw_param[i].path = draw_param[i].path.replace(f"m{area_id}_", f"m{area_id}_1_")
        draw_param.add_entry(slot_0)
    s_ambient_0 = s_ambient.copy()
    s_ambient_0.id = 23
    s_ambient.path = s_ambient.path.replace(f"s{area_id}_", f"s{area_id}_1_")
    s_ambient.id = 22
    draw_param.add_entry(s_ambient)
    draw_param.add_entry(s_ambient_0)
    draw_param.write()
