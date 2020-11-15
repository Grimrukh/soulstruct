from __future__ import annotations

import logging
import typing as tp
from pathlib import Path

from soulstruct.bnd import BND3
from soulstruct.models.darksouls1 import CHARACTER_FFX_SOURCES

if tp.TYPE_CHECKING:
    from soulstruct.maps.msb import MSB

_LOGGER = logging.getLogger(__name__)


def build_ffxbnd(msb: MSB, ffxbnd_path: Path, ffxbnd_search_directory: Path = None):
    """Iterate over all enemy models in given `msb` and ensure all their FFX files are present in the given FFXBND file
    `ffxbnd_path`. Missing FFXBND files will be taken from their vanilla locations (known by Soulstruct) and added.

    Args:
        msb (MSB): MSB structure to check.
        ffxbnd_path (Path): path to initial FFXBND to check, e.g. a vanilla FFXBND.
        ffxbnd_search_directory (Path, optional): path to directory containing FFXBND files to search for missing FFX
            in. It should contain all FFXBND files in the game (e.g. a vanilla backup folder). If not given, it will
            default to the same directory as `ffxbnd_path`.
    """
    ffxbnd_path = Path(ffxbnd_path)
    if ffxbnd_search_directory is None:
        ffxbnd_search_directory = ffxbnd_path.parent
    try:
        ffxbnd = BND3(ffxbnd_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find FFXBND file to modify: {ffxbnd_path}")
    open_sources = {}  # type: tp.Dict[str, BND3]
    existing_ffx_files = [entry.name for entry in ffxbnd.entries]
    next_id = max(i for i in ffxbnd.entries_by_id if i < 100000) + 1

    for chr_model in msb.models.Characters:
        model_id = int(chr_model.name[1:])
        if model_id not in CHARACTER_FFX_SOURCES:
            _LOGGER.warning(f"FFX sources for character model {chr_model} are not known.")
            continue  # model not handled
        for ffx_id, source_path in CHARACTER_FFX_SOURCES[model_id].items():
            ffx_file_name = f"f{ffx_id:07d}.ffx"
            if ffx_file_name in existing_ffx_files:
                continue
            try:
                source_bnd = open_sources.setdefault(
                    source_path,
                    BND3(ffxbnd_search_directory / f"{source_path}.ffxbnd.dcx"),
                )
            except FileNotFoundError:
                _LOGGER.error(f"Could not find FFX source file '{source_path}.ffxbnd.dcx' for FFX {ffx_id} "
                              f"(character model {model_id}).")
                continue
            matches = [entry for entry in source_bnd.entries if entry.name == ffx_file_name]
            if not matches:
                _LOGGER.error(f"Could not find FFX file '{ffx_file_name}' in source BND '{source_path}.ffxbnd.dcx' "
                              f"(character model {model_id}).")
                continue
            source_entry = matches[0]
            source_entry.id = next_id
            next_id += 1
            ffxbnd.add_entry(source_entry)
            existing_ffx_files.append(ffx_file_name)

    ffxbnd.write()
