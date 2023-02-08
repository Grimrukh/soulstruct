from __future__ import annotations

__all__ = ["build_ffxbnd", "get_map", "import_map_piece_flver", "find_flver_textures", "dump_all_map_textures"]

import logging
import re
import shutil
import typing as tp
from pathlib import Path

from soulstruct.containers.entry import BinderEntry
from soulstruct.base.maps.utilities import get_map
from soulstruct.base.models.flver import FLVER
from soulstruct.config import DSR_PATH
from soulstruct.containers.bxf import BXF3
from soulstruct.containers.bnd import BND3

from ..constants import CHARACTER_FFX_SOURCES

if tp.TYPE_CHECKING:
    from . import MSB

_LOGGER = logging.getLogger(__name__)

_BLOCK_FFXBND_RE = re.compile(r"FRPG_SfxBnd_m(\d\d)_(\d\d)\.ffxbnd(\.dcx)?")
_MAP_PIECE_RE = re.compile(r"^m(\d\d\d\d)B(\d)A(\d\d)\.flver\.dcx$")

# The FFX and FLVER matches allow arbitrary non-numeric characters to appear after the ID digits
# (e.g. "f0000123_MyEffect.ffx"), but these characters will not be written to the FFXBND.
_FFX_FILE_MATCH = re.compile(r"f(\d+).*\.ffx")  # typically 7 digits
_FLVER_FILE_MATCH = re.compile(r"s(\d+).*\.flver")  # typically 5 digits
# TPF files may have material suffixes like "_n", so extra strings will be included in the file name. Make sure not to
# include any!
_TPF_FILE_MATCH = re.compile(r"s(\d+[_\w]*)\.tpf")  # typically 5 digits


def build_ffxbnd(
    msb: MSB | None,
    ffxbnd_path: Path,
    ffxbnd_search_directory: Path = None,
    write_ffxbnd_path: Path = None,
    extra_sources: tp.Sequence[tuple[tp.Union[int, str], str, str]] = (),
    extra_character_ffx_directory: Path = None,
    check_area_ffxbnd=True,
    prefer_bak=True,
) -> BND3:
    """Iterate over all character models in given `msb` and ensure all their FFX files (including FLVER and TPF files)
    are present in the given FFXBND file `ffxbnd_path`. Missing FFXBND files will be taken from their vanilla locations
    (known by Soulstruct) and added.

    Loose sources of FFX files can also be specified with `extra_sources`. These may be '.ffx', '.flver', or '.tpf'
    files.

    Use `write_ffxbnd_path` to write to a location other than `ffxbnd_path` (default if `write_ffxbnd_path` not given).

    Args:
        msb (MSB): MSB structure to check.
        ffxbnd_path (Path): path to FFXBND to scan and potentially modify, likely in `{game}/sfx`.
        ffxbnd_search_directory (Path, optional): path to directory containing FFXBND files to search for missing FFX
            in. It should contain all FFXBND files in the game (e.g. a vanilla backup folder). If not given, it will
            default to the same directory as `ffxbnd_path`.
        write_ffxbnd_path (Path): path to write final FFXBND. If not given (default), uses `ffxbnd_path`.
        extra_sources (sequence of tuples): sequence of `(file_id, file_type, source_file)` tuples that specify extra
            FFX, FLVER, and/or TPF files to import (e.g. for VFX events in the MSB). The source files can be FFXBND
            files to look inside, or just raw unpacked FFX files (in which case, anything after their ID in the filename
            will be removed for FFX/FLVER files). For TPF files with name suffixes like "_n", the given `file_id` may
            be a string.
        extra_character_ffx_directory: optional path to a directory containing loose FFX/FLVER/TPF files in character
            model subdirectories, to be used for models not on the known path.
        check_area_ffxbnd (bool): if True (default), and if `ffxbnd_path` is a block FFXBND file (with 'mAA_BB' in its
            file stem), the corresponding area FFXBND file ('mAA.ffxbnd') will also be checked if it exists. Any FFX
            already existing in that file will count just like existing FFX in the given block file.
        prefer_bak (bool): if True (default), look for '.bak' source files first, in case the FFXBNDs have been modded
            and some vanilla FFX entries removed.
    """
    ffxbnd_path = Path(ffxbnd_path)
    if write_ffxbnd_path is None:
        write_ffxbnd_path = ffxbnd_path
    if ffxbnd_search_directory is None:
        ffxbnd_search_directory = ffxbnd_path.parent
    try:
        ffxbnd = BND3(ffxbnd_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find FFXBND file to modify: {ffxbnd_path}")
    open_ffxbnd_sources = {}  # type: dict[str, BND3]
    existing_file_names = {entry.name for entry in ffxbnd._entries}
    existing_ffx_ids = [i for i in ffxbnd.entries_by_id if i < 100000]
    existing_tpf_ids = [i for i in ffxbnd.entries_by_id if 100000 <= i < 200000]
    existing_flver_ids = [i for i in ffxbnd.entries_by_id if 200000 <= i < 300000]
    next_ffx_id = max(existing_ffx_ids) + 1 if existing_ffx_ids else 0
    next_tpf_id = max(existing_tpf_ids) + 1 if existing_tpf_ids else 0
    next_flver_id = max(existing_flver_ids) + 1 if existing_flver_ids else 0

    # If a block) FFXBND is specified, also check its area FFXBND for existing files, if requested.
    if check_area_ffxbnd and (block_match := _BLOCK_FFXBND_RE.match(str(ffxbnd_path))):
        area_ffxbnd_path = ffxbnd_path.parent / f"FRPG_SfxBnd_m{block_match.group(1)}.ffxbnd{block_match.group(3)}"
        try:
            area_ffxbnd = BND3(area_ffxbnd_path)
        except FileNotFoundError:
            _LOGGER.warning(
                f"Could not find area-level FFXBND file {area_ffxbnd_path}. It will not be checked for existing files."
            )
        else:
            existing_file_names |= {entry.name for entry in area_ffxbnd._entries if entry.name}
            # The next available IDs, of course, are still the same in the block file.

    # Add extra FFX sources. These will take precedence over any vanilla files or extra character files that are found
    # in the subsequent sections.
    for extra_id, file_type, extra_source_file_name in extra_sources:
        # `extra_source_file_name` may be a naked FFX/FLVER/TPF file or an FFXBND containing the given FFX ID.

        extra_source_path = Path(extra_source_file_name)
        extra_source_file_name = str(extra_source_path)  # for dictionary

        if file_type is None:
            # Auto-detect file type from path suffix.
            file_type = extra_source_path.suffix
            if file_type not in {".ffx", ".flver", ".tpf"}:
                raise ValueError(
                    f"Invalid source file suffix for FFX file type detection: {file_type}. Should be '.ffx', '.tpf', "
                    f"or '.flver"
                )
        else:
            file_type = "." + file_type.lower().lstrip(".")

        if extra_id is None:
            # Auto-detect file ID from path name.
            try:
                if file_type == ".ffx":
                    extra_id = int(_FFX_FILE_MATCH.match(extra_source_path.name).group(1))
                elif file_type == ".flver":
                    extra_id = int(_FLVER_FILE_MATCH.match(extra_source_path.name).group(1))
                elif file_type == ".tpf":
                    extra_id = _TPF_FILE_MATCH.match(extra_source_path.name).group(1)  # string, not int
            except AttributeError:
                # No match.
                raise ValueError(f"Cannot auto-detect FFX file ID from '{file_type}' file: {extra_source_path}")

        if file_type == ".ffx":
            if not isinstance(extra_id, int):
                raise ValueError(f"Extra file ID for FFX must be an `int`.")
            file_name = f"f{extra_id:07d}.ffx"  # this formatting will still allow ID to be longer than 7 digits
            entry_id = next_ffx_id
            entry_path = f"N:\\FRPG\\data\\Sfx\\OutputData\\Main\\Effect_x64\\{file_name}"
        elif file_type == ".tpf":
            if isinstance(extra_id, int):
                file_name = f"s{extra_id:05d}.tpf"
            else:
                file_name = f"s{extra_id}.tpf"  # use full given name string
            entry_id = next_tpf_id
            entry_path = f"N:\\FRPG\\data\\Sfx\\tex\\{file_name}"
        elif file_type == ".flver":
            if not isinstance(extra_id, int):
                raise ValueError(f"Extra file ID for FFX FLVER must be an `int`.")
            file_name = f"s{extra_id:05d}.flver"
            entry_id = next_flver_id
            entry_path = f"N:\\FRPG\\data\\Sfx\\model\\{file_name}"
        else:
            raise ValueError(f"Invalid extra FFX file type: {file_type}. Must be 'ffx', 'tpf', or 'flver'.")

        if file_name in existing_file_names:
            continue

        if extra_source_path.name.startswith("FRPG"):
            # Find file in FFXBND file source.
            if extra_source_path.is_absolute():
                source_path = extra_source_path
            else:
                source_path = ffxbnd_search_directory / f"{extra_source_path.name.split('.')[0]}.ffxbnd.dcx"
            if prefer_bak:
                if (bak_path := source_path.with_suffix(source_path.suffix + ".bak")).is_file():
                    source_path = bak_path
            if not source_path.is_file():
                _LOGGER.error(f"Could not find FFXBND source file '{source_path}' for extra {file_type} {extra_id}.")
                continue
            source_bnd = open_ffxbnd_sources.setdefault(extra_source_file_name, BND3(source_path))
            try:
                # No need to make a copy of the source file.
                source_entry = source_bnd.entries_by_name[file_name]
            except KeyError:
                _LOGGER.error(
                    f"Could not find extra {file_type} file '{file_name}' in given source FFXBND '{source_path}'."
                )
                continue
            source_entry.entry_id = entry_id
        else:
            if extra_source_path.suffix != file_type:
                raise ValueError(
                    f"Source path suffix '{extra_source_path.suffix}' does not match file type {file_type}."
                )
            source_entry = BND3.BinderEntry(
                data=extra_source_path.read_bytes(),
                entry_id=entry_id,
                path=entry_path,
                flags=2,
            )

        ffxbnd.add_entry(source_entry)
        existing_file_names.add(file_name)

        if file_type == ".ffx":
            next_ffx_id += 1
        elif file_type == ".tpf":
            next_tpf_id += 1
        elif file_type == ".flver":
            next_flver_id += 1
        # No way for `else` to occur.

    if msb is None:
        # Do not check character FFX.
        ffxbnd.write(write_ffxbnd_path)
        return ffxbnd

    for chr_model in msb.models.Characters:
        model_id = int(chr_model.name[1:])

        # Check extra character directory.
        if extra_character_ffx_directory is not None:
            extra_chr_dir = (extra_character_ffx_directory / chr_model.name).resolve()
            if extra_chr_dir.is_dir():
                for extra_file_path in extra_chr_dir.rglob("*"):
                    if extra_file_path.is_dir():
                        continue  # skip directories
                    is_ffx = is_tpf = is_flver = False
                    if ffx_id_match := _FFX_FILE_MATCH.match(extra_file_path.name):
                        is_ffx = True
                        file_name = f"f{int(ffx_id_match.group(1)):07d}.ffx"
                        entry_id = next_ffx_id
                        entry_path = f"N:\\FRPG\\data\\Sfx\\OutputData\\Main\\Effect_x64\\{file_name}"
                    elif flver_id_match := _FLVER_FILE_MATCH.match(extra_file_path.name):
                        is_flver = True
                        file_name = f"s{int(flver_id_match.group(1)):05d}.flver"
                        entry_id = next_flver_id
                        entry_path = f"N:\\FRPG\\data\\Sfx\\model\\{file_name}"
                    elif tpf_id_match := _TPF_FILE_MATCH.match(extra_file_path.name):
                        # NOTE: TPF name match includes any characters after the ID digits (e.g. "_n").
                        is_tpf = True
                        file_name = f"s{tpf_id_match.group(1)}.tpf"
                        entry_id = next_tpf_id
                        entry_path = f"N:\\FRPG\\data\\Sfx\\tex\\{file_name}"
                    else:
                        _LOGGER.warning(
                            f"Ignoring non-FFX/FLVER/TPF file in extra character folder: {extra_file_path.name}"
                        )
                        continue

                    source_entry = BND3.BinderEntry(
                        data=extra_file_path.read_bytes(),
                        entry_id=entry_id,
                        path=entry_path,
                        flags=2,
                    )
                    ffxbnd.add_entry(source_entry)
                    existing_file_names.add(file_name)

                    if is_ffx:
                        _LOGGER.info(f"    Added loose FFX for {chr_model.name}: {file_name}")
                        next_ffx_id += 1
                    elif is_tpf:
                        _LOGGER.info(f"    Added loose FFX TPF for {chr_model.name}: {file_name}")
                        next_tpf_id += 1
                    elif is_flver:
                        _LOGGER.info(f"    Added loose FFX FLVER for {chr_model.name}: {file_name}")
                        next_flver_id += 1

                # Found character model's folder, so stop searching for it.
                continue

        if model_id not in CHARACTER_FFX_SOURCES:
            _LOGGER.warning(f"Vanilla FFX sources for character model {chr_model.name} are not known.")
            continue

        # TODO: Only FFX files (not FLVER or TPF) are in `CHARACTER_FFX_SOURCES` at the moment.
        for ffx_id, source_file_name in CHARACTER_FFX_SOURCES[model_id].items():
            ffx_file_name = f"f{ffx_id:07d}.ffx"  # ID can still be longer than seven digits
            if ffx_file_name in existing_file_names:
                # Already existing (or added from extra character sources).
                continue
            source_path = ffxbnd_search_directory / f"{source_file_name}.ffxbnd.dcx"
            if prefer_bak:
                if (bak_path := source_path.with_suffix(source_path.suffix + ".bak")).is_file():
                    source_path = bak_path
            if not source_path.is_file():
                _LOGGER.error(f"Could not find FFX source file '{source_path}' for FFX {ffx_id} "
                              f"(character model {model_id}).")
                continue
            source_bnd = open_ffxbnd_sources.setdefault(source_file_name, BND3(source_path))
            try:
                source_entry = source_bnd.entries_by_name[ffx_file_name]
            except KeyError:
                _LOGGER.error(
                    f"Could not find FFX file '{ffx_file_name}' in source BND '{source_path}' (character model "
                    f"{model_id})."
                )
                continue
            source_entry.entry_id = next_ffx_id
            next_ffx_id += 1
            ffxbnd.add_entry(source_entry)
            existing_file_names.add(ffx_file_name)

    ffxbnd.write(write_ffxbnd_path)
    return ffxbnd


def import_map_piece_flver(
    source_flver_path: str | Path,
    dest_flver_path: str | Path,
    overwrite=False,
):
    """Move (copy) a map piece from one map to another. Handles all FLVER (model) and TPF (texture) files - everything
    that is required to simply add the new model entry to the MSB and create MSB parts with it.

    You will still need to add the new map piece to the destination's MSB to have it appear.

    DOCUMENTATION:
        - Map piece FLVERs are named as: mXXXXBYAZZ, where XXXX is the model ID, ZZ is the area, and Y is the one-digit
        block. So map piece model 2000 in Firelink Shrine (m10_02) is `m2000B2A10.flver.dcx`.
        - If a model file is not found for any reason, that map piece will simply not appear (as with other MSB parts).
        - The BY and AZZ parts of the model file name are required. Presumably, these are automatically appended to the
        model name given in the MSB model section, so that files with the same model ID from different maps can't be
        confused.
        - Changing the model NAME in the MSB appears to do nothing. It's the SIB path that needs to be correct! The map
        piece loads if and only if the SIB is correct.
        - I'm guessing my previous finding that "existing map piece names couldn't be changed" was because I didn't
        change the SIB path (when I moved `m2000B1` to `m2009B1` in Parish to make room for `m2000B1` from Tomb). So
        that's good to know.
        - The SIB path name is `mXXXXBY.sib`, with no `AZZ` part. That suggests that only the `AZZ` part is being tacked
        on automatically. It's more complicated than that, though.
        - Changing the `mXXXX` part of the SIB path, and changing the FLVER name accordingly, works fine, as I already
        knew - but ONLY if the ID is FOUR OR LESS digits. It does not work if the ID has 5+ digits (well, I've tested 5
        and 8 and am extrapolating from there). Similar, the `BY` part can be changed as long as Y is only one digit.
        - Changing the map folder in the SIB path and moving the FLVER to that folder does NOT work, even if the other
        map is loaded (e.g. tried moving `m2000B2` to `m10_01_00_00` from Firelink). Even if this somehow did work, the
        textures wouldn't be loaded in general.
        - In fact, the parent and file extension can be removed from the SIB path, so it's literally just `mXXXXBY`, and
        it works fine. The game engine must just be reading the stem from the path.
        - Furthermore, the `B` letter doesn't matter - it can be anything, even a digit.

    So, this ultimately means I have six characters to work with after the `m` prefix. That's fine - I can use the first
    two digits for the source area and block (AB) and the last four for the source ID. So `m2000B2A10` from Firelink,
    moved to another map, would become `m022000`. Piece `m1234B1A15` from Anor Londo would become `m511234`.
    """
    if not source_flver_path.is_file():
        raise FileNotFoundError(f"Could not find source FLVER: '{source_flver_path}'")
    if dest_flver_path.exists() and not overwrite:
        raise FileExistsError(f"FLVER destination path '{dest_flver_path}' already exists and `overwrite=False`.")

    if not _MAP_PIECE_RE.match(source_flver_path.name):
        raise ValueError(f"Invalid source map piece name: '{source_flver_path.name}'. Must be an original map piece.")

    dest_texture_dir = dest_flver_path.parent.parent / dest_flver_path.parent.name[0:3]  # e.g. "m10"

    tpf_entries = find_flver_textures(source_flver_path)
    existing_tpf_paths = set()
    bhd = None
    for bhd_path in dest_texture_dir.glob("m*tpfbhd"):  # does not search `GI_EnvM_mXX.tpfbhd`
        bhd = BXF3(bhd_path)
        for entry in bhd._entries:
            existing_tpf_paths.add(entry.path)
    if bhd is None:
        raise FileNotFoundError(f"No texture TPFBHD archives found in destination map area: {dest_texture_dir}")
    next_entry_id = max(entry.entry_id for entry in bhd.entries) + 1
    do_write = False
    for tpf_entry in [entry for entry in tpf_entries if entry.path not in existing_tpf_paths]:
        tpf_entry.entry_id = next_entry_id  # this entry instance can be modified safely
        next_entry_id += 1
        bhd.add_entry(tpf_entry)
        do_write = True
    if do_write:  # at least one new entry was added
        bhd.write()

    shutil.copy(source_flver_path, dest_flver_path)  # intentionally not using `copy2` so file appears modified


def find_flver_textures(flver_path: str | Path) -> list[BinderEntry]:
    """Search all TPFBHD binders in the area folder (e.g. "map/m10") of the given FLVER for that FLVER's textures."""
    flver_path = Path(flver_path)
    texture_dir = flver_path.parent.parent / flver_path.parent.name[0:3]  # e.g. "m10"

    flver = FLVER(flver_path)
    tpf_paths = {f"\\{Path(texture_path).stem}.tpf.dcx" for texture_path in flver.get_all_texture_paths()}
    tpf_count = len(tpf_paths)
    tpf_entries = []

    for bhd_path in texture_dir.glob("m*tpfbhd"):  # does not search `GI_EnvM_mXX.tpfbhd`
        bhd = BXF3(bhd_path)
        print(f"Searching BHD: {bhd_path}")
        for entry in bhd._entries:
            if entry.path in tpf_paths:
                tpf_entries.append(entry)
                tpf_paths.remove(entry.path)
            if not tpf_paths:
                break  # no need to search further
        if not tpf_paths:
            break  # no need to search further

    if tpf_paths:
        _LOGGER.warning(f"Could not find {len(tpf_paths)} out of {tpf_count} FLVER {flver_path} textures: {tpf_paths}")
    return tpf_entries


def dump_all_map_textures(dump_directory: str | Path, map_directory: str | Path = None):
    """Unpacks all `TPFBHD` binders in all map area folders (e.g. `MapStudio/m10`) and dumps the textures into the given
    folder. For vanilla installations, this amounts to 5912 files taking up a total of 1.7 GB.

    This is useful when map pieces are being moved between maps, so their textures can be easily sourced from
    the dumped folder and added to the destination map. The texture bundles (`*.tpf.dcx`) are neither decompressed or
    unpacked, as this isn't needed to move them between maps. (The map piece `FLVER` files reference `*.tga` files which
    have identical stems to the `*.tpf.dcx` files.)

    This function explicitly searches for the known folders (m10, m11, m12, ...) and will not blindly unpack textures
    from any other folders that happen to be there. However, it does not assume how many BXF binders are inside each
    map area folder.

    If `map_directory` is not given, the `DSR_PATH` from Soulstruct's config will be used.

    Always prefers `bak` files if present, but does not create any.

    Duplicate `tpf` files (with the same name) found in multiple maps are ignored.
    """
    dump_directory = Path(dump_directory)
    dump_directory.mkdir(parents=True, exist_ok=True)
    map_directory = Path(map_directory) if map_directory is not None else Path(DSR_PATH) / "map"

    for area in range(10, 18 + 1):
        area_dir = map_directory / f"m{area}"
        for bhd_path in area_dir.glob("*.tpfbhd"):
            bxf = BXF3.from_bak(bhd_path, create_bak_if_missing=False)
            for entry in bxf._entries:
                tpf_path = dump_directory / entry.name
                if not tpf_path.exists():  # may have been unpacked elsewhere already
                    with tpf_path.open("wb") as f:
                        f.write(entry.data)  # not decompressed
