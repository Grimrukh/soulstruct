import typing as tp
from pathlib import Path

from soulstruct.game_types import Map


def get_map(source, block_id=None, game_maps: tp.Sequence[Map] = ()):
    """Flexible-input function for retrieving map constants.

    Valid inputs:
        (area_id: int, block_id: int) (such as (10, 0))
        four_digit_id: int (such as 1000)
        file_stem: str (such as "m10_00_00_00"; file extensions don't matter, both EMEVD and MSB names will be checked)
        map_name: str (such as "UNDEAD_BURG" or "UndeadBurg"; case and underscores don't matter)
    """
    if game_maps is None:
        raise ImportError("No game maps given. (You should import `get_maps` from `soulstruct.constants.{game}.maps`.)")

    source_orig = source if block_id is None else (source, block_id)

    if isinstance(source, (list, tuple)):
        try:
            area_id, block_id = source
        except ValueError:
            raise ValueError(f"Sequence source for map-finding should be two values (area_id, block_id), not {source}.")
        matches = [g for g in game_maps if g.area_id == area_id and g.block_id == block_id]
    elif isinstance(source, int):
        if block_id is not None:
            try:
                area_id = int(source)
                block_id = int(block_id)
            except ValueError:
                raise ValueError(f"Invalid map-finding source: ({source}, {block_id})")
            matches = [g for g in game_maps if g.area_id == area_id and g.block_id == block_id]
        else:
            source = str(int)
            if len(source) != 4:
                raise ValueError("Abbreviated map ID should be exactly four digits (100 * area_id + block_id).")
            area_id, block_id = source[:2], source[2:]
            matches = [g for g in game_maps if g.area_id == area_id and g.block_id == block_id]
    elif isinstance(source, str):
        if (source.startswith("m") and "_" in source) or source == "aiCommon":
            source = Path(source).stem  # remove file extensions
            matches = [g for g in game_maps if source in g.stem_set()]
        else:
            # Canonical name. Change to lower case and remove underscores.
            source = source.lower().replace("_", "")
            matches = [g for g in game_maps if source == g.name.lower().replace("_", "")]
    else:
        raise TypeError(f"Invalid type for map-finding source: {source} (type {type(source)})")

    if len(matches) > 1:
        raise ValueError(f"Multiple maps matched for '{source_orig}': {[g.name for g in matches]}")
    elif not matches:
        raise ValueError(f"No maps matched for '{source_orig}'.")

    return matches[0]
