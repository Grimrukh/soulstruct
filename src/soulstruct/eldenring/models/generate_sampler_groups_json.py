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

    # Full mapping of 'group_X' to `{full_sampler_name, default_texture_stem}`.
    # Includes ungrouped samplers.
    all_shader_sampler_groups = {}

    # Summarized mapping of group 'X' to `[short_sampler_name_1, short_sampler_name_2, ...]`.
    # The short sampler names have the shader stem prefix removed (converting '[' to '_'), then
    # also have '_snp_Texture_2D_' removed if still present.
    # We also include the default texture name if present and does not contain 'SYSTEX'.
    shader_group_summaries = {}

    for matbin_entry in matbinbnd.entries:
        matbin = MATBIN.from_binder_entry(matbin_entry)
        shader_stem = matbin.shader_name.split(".")[0]
        if shader_stem in all_shader_sampler_groups:
            continue  # done from previous MATBIN

        print(f"Finding metaparam for shader {shader_stem}...")
        # NOTE: Every shader has its own shaderbdle entry, so there's nothing to cache.
        try:
            shaderbdle_entry = shaderbdlebnd.find_entry_name(f"{shader_stem}.shaderbdle")
        except EntryNotFoundError:
            print(f"  No shaderbdle entry found for {shader_stem}.")
            all_shader_sampler_groups[shader_stem] = []  # don't look again
            continue

        shaderbdle = Binder.from_binder_entry(shaderbdle_entry)
        metaparam_entry = shaderbdle.find_entry_name(f"{shader_stem}.metaparam")

        shader_sampler_groups = read_metaparam(metaparam_entry)
        # Sort group keys by group index (if present).
        shader_sampler_groups = {
            group_name: shader_sampler_groups[group_name]
            for group_name in sorted(
                shader_sampler_groups,
                key=lambda x: int(x.removeprefix("group_")) if x else 1E9,
            )
        }
        all_shader_sampler_groups[shader_stem] = shader_sampler_groups

        if not shader_sampler_groups:
            continue  # no summary

        # Write summary content.
        shader_group_summaries[shader_stem] = {}
        shader_prefix = shader_stem.replace("][", "_").replace("[", "_").replace("]", "_")
        for group_name, samplers in shader_sampler_groups.items():
            short_sampler_names = []
            for sampler_name, default_texture_name in samplers:
                short_name = sampler_name.removeprefix(shader_prefix)
                short_name = short_name.removeprefix("_snp_Texture2D_")
                if default_texture_name and "SYSTEX" not in default_texture_name:
                    short_name += f" == {default_texture_name}"
                short_sampler_names.append(short_name)
            shader_group_summaries[shader_stem][group_name] = short_sampler_names

    # Sort by shader name.
    all_shader_sampler_groups = {
        k: v for k, v in sorted(all_shader_sampler_groups.items())
    }
    shader_group_summaries = {
        k: v for k, v in sorted(shader_group_summaries.items())
    }

    write_json("resources/er_shader_sampler_groups.json", all_shader_sampler_groups, indent=4)
    write_json("resources/er_shader_sampler_groups_summary.json", shader_group_summaries, indent=4)


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
