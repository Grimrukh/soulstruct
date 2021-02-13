from __future__ import annotations

__all__ = ["build_ffxbnd", "get_map"]

import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.base.maps.utilities import get_map
from soulstruct.containers.bnd import BND3

from ..models import CHARACTER_FFX_SOURCES

if tp.TYPE_CHECKING:
    from . import MSB

_LOGGER = logging.getLogger(__name__)

_BLOCK_FFXBND_RE = re.compile(r"FRPG_SfxBnd_m(\d\d)_(\d\d).ffxbnd(.dcx)?")


def build_ffxbnd(msb: MSB, ffxbnd_path: Path, ffxbnd_search_directory: Path = None, prefer_bak=True):
    """Iterate over all enemy models in given `msb` and ensure all their FFX files are present in the given FFXBND file
    `ffxbnd_path`. Missing FFXBND files will be taken from their vanilla locations (known by Soulstruct) and added.

    Args:
        msb (MSB): MSB structure to check.
        ffxbnd_path (Path): path to initial FFXBND to check, e.g. a vanilla FFXBND.
        ffxbnd_search_directory (Path, optional): path to directory containing FFXBND files to search for missing FFX
            in. It should contain all FFXBND files in the game (e.g. a vanilla backup folder). If not given, it will
            default to the same directory as `ffxbnd_path`.
        prefer_bak (bool): if True (default), look for '.bak' source files first.
    """
    ffxbnd_path = Path(ffxbnd_path)
    if ffxbnd_search_directory is None:
        ffxbnd_search_directory = ffxbnd_path.parent
    try:
        ffxbnd = BND3(ffxbnd_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find FFXBND file to modify: {ffxbnd_path}")
    open_sources = {}  # type: dict[str, BND3]
    existing_ffx_files = {entry.name for entry in ffxbnd.entries}
    next_id = max(i for i in ffxbnd.entries_by_id if i < 100000) + 1

    match = _BLOCK_FFXBND_RE.match(str(ffxbnd_path))
    if match:
        area_ffxbnd_path = ffxbnd_path.parent / f"FRPG_SfxBnd_m{match.group(1)}.ffxbnd.dcx{match.group(2)}"
        try:
            area_ffxbnd = BND3(area_ffxbnd_path)
        except FileNotFoundError:
            _LOGGER.warning(f"Could not find area-level FFXBND file {area_ffxbnd_path}. It will not be checked for "
                            f"existing FFX files.")
        else:
            existing_ffx_files |= {entry.name for entry in area_ffxbnd.entries}

    for chr_model in msb.models.Characters:
        model_id = int(chr_model.name[1:])
        if model_id not in CHARACTER_FFX_SOURCES:
            _LOGGER.warning(f"FFX sources for character model {chr_model.name} are not known.")
            continue  # model not handled
        for ffx_id, source_file_name in CHARACTER_FFX_SOURCES[model_id].items():
            ffx_file_name = f"f{ffx_id:07d}.ffx"
            if ffx_file_name in existing_ffx_files:
                continue
            source_path = ffxbnd_search_directory / f"{source_file_name}.ffxbnd.dcx"
            if prefer_bak:
                if (bak_path := source_path.with_suffix(source_path.suffix + ".bak")).is_file():
                    source_path = bak_path
            if not source_path.is_file():
                _LOGGER.error(f"Could not find FFX source file '{source_path}' for FFX {ffx_id} "
                              f"(character model {model_id}).")
                continue
            source_bnd = open_sources.setdefault(source_file_name, BND3(source_path))
            try:
                source_entry = source_bnd.entries_by_basename[ffx_file_name]
            except KeyError:
                _LOGGER.error(
                    f"Could not find FFX file '{ffx_file_name}' in source BND '{source_path}' (character model "
                    f"{model_id})."
                )
                continue
            source_entry.id = next_id
            next_id += 1
            ffxbnd.add_entry(source_entry)
            existing_ffx_files.add(ffx_file_name)

    ffxbnd.write()
