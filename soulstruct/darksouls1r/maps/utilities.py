from __future__ import annotations

__all__ = ["import_map_piece_flver", "find_flver_textures", "dump_all_map_textures"]

import logging
import re
import shutil
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry
from soulstruct.base.models.flver import FLVER
from soulstruct.config import DSR_PATH


_LOGGER = logging.getLogger("soulstruct")

_MAP_PIECE_RE = re.compile(r"^m(\d\d\d\d)B(\d)A(\d\d)\.flver\.dcx$")


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
        bhd = Binder.from_path(bhd_path)
        for entry in bhd.entries:
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

    flver = FLVER.from_path(flver_path)
    tpf_paths = {f"\\{Path(texture_path).stem}.tpf.dcx" for texture_path in flver.get_all_texture_paths()}
    tpf_count = len(tpf_paths)
    tpf_entries = []

    for bhd_path in texture_dir.glob("m*tpfbhd"):  # does not search `GI_EnvM_mXX.tpfbhd`
        bhd = Binder.from_path(bhd_path)
        print(f"Searching BHD: {bhd_path}")
        for entry in bhd.entries:
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
            bxf = Binder.from_path(bhd_path)
            for entry in bxf.entries:
                tpf_path = dump_directory / entry.name
                if not tpf_path.exists():  # may have been unpacked elsewhere already
                    with tpf_path.open("wb") as f:
                        f.write(entry.data)  # not decompressed
