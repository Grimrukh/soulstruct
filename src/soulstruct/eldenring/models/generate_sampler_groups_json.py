from __future__ import annotations

import logging
from pathlib import Path

from soulstruct.base.models.matbin import MATBIN, MATBINBND
from soulstruct.config import ELDEN_RING_PATH
from soulstruct.containers import Binder, BinderEntry, EntryNotFoundError
from soulstruct.utilities.binary import BinaryReader
from soulstruct.utilities.files import write_json

_LOGGER = logging.getLogger(__name__)


def generate_metaparam(elden_ring_path: Path):
    matbinbnd = MATBINBND.from_bundled("ELDEN_RING")
    shaderbdlebnd_path = Path(elden_ring_path, "shader/shaderbdle.shaderbdlebnd.dcx")
    shaderbdlebnd_dlc01_path = Path(elden_ring_path, "shader/shaderbdle_dlc01.shaderbdlebnd.dcx")
    shaderbdlebnd_dlc02_path = Path(elden_ring_path, "shader/shaderbdle_dlc02.shaderbdlebnd.dcx")

    shaderbdlebnd = Binder.from_path(shaderbdlebnd_path)
    shaderbdlebnd_dlc01 = Binder.from_path(shaderbdlebnd_dlc01_path)
    shaderbdlebnd_dlc02 = Binder.from_path(shaderbdlebnd_dlc02_path)

    entries_by_name = shaderbdlebnd.get_entries_by_name()
    for entry in shaderbdlebnd_dlc01.entries:
        if entry.name in entries_by_name:
            # Replace base game entry with DLC entry.
            shaderbdlebnd.remove_entry_name(entry.name)
        shaderbdlebnd.entries.append(entry)
    for entry in shaderbdlebnd_dlc02.entries:
        if entry.name in entries_by_name:
            # Replace base game entry with DLC entry.
            shaderbdlebnd.remove_entry_name(entry.name)
        shaderbdlebnd.entries.append(entry)

    all_shader_sampler_groups = {}

    for matbin_entry in matbinbnd.entries:
        matbin = MATBIN.from_binder_entry(matbin_entry)
        shader_stem = matbin.shader_name.split(".")[0]
        if shader_stem in all_shader_sampler_groups:
            continue  # done from previous MATBIN

        print(f"Finding metaparam for shader {shader_stem}...")
        try:
            shaderbdle_entry = shaderbdlebnd.find_entry_name(f"{shader_stem}.shaderbdle")
        except EntryNotFoundError:
            print(f"  No shaderbdle entry found for {shader_stem}.")
            all_shader_sampler_groups[shader_stem] = []  # don't look again
            continue

        shaderbdle = Binder.from_binder_entry(shaderbdle_entry)
        metaparam_entry = shaderbdle.find_entry_name(f"{shader_stem}.metaparam")

        shader_sampler_groups = read_metaparam(metaparam_entry)
        # Sort group keys.
        shader_sampler_groups = {
            group_name: shader_sampler_groups[group_name] for group_name in sorted(shader_sampler_groups)
        }
        all_shader_sampler_groups[shader_stem] = shader_sampler_groups

    write_json("resources/er_shader_sampler_groups.json", all_shader_sampler_groups, indent=4)


def read_metaparam(metaparam_entry: BinderEntry) -> dict[str, list[tuple[str, str]]]:
    """Read metaparam data as a dictionary mapping sampler group names to lists of sampler names with their default
    texture paths ('SYSTEX' stuff usually).

    Note that an empty group name key may exist.
    """
    metaparam = BinaryReader(metaparam_entry.get_uncompressed_data())

    shader_dict = {}
    metaparam.seek(0xC)
    sampler_count = metaparam.unpack_value("i")
    for i in range(sampler_count):
        metaparam.seek(0x98 + (0x30 * i))
        sampler_name_offset = metaparam.unpack_value("q")
        metaparam.seek(8, 1)
        default_texture_path_offset = metaparam.unpack_value("q")
        sampler_group_name_offset = metaparam.unpack_value("q")

        sampler_name = metaparam.unpack_string(offset=sampler_name_offset, encoding="utf-16-le")
        default_texture_path = metaparam.unpack_string(offset=default_texture_path_offset, encoding="utf-16-le")
        group_name = metaparam.unpack_string(offset=sampler_group_name_offset, encoding="utf-16-le")  # could be empty

        shader_dict.setdefault(group_name, []).append((sampler_name, default_texture_path))

    return shader_dict


if __name__ == '__main__':
    generate_metaparam(ELDEN_RING_PATH)
