"""Unpacks all DSR TPF files into DDS files in the given folder, for Blender use.

This way, Blender doesn't have to unpack TPF files itself and embed DDS files into the `.blend`, which costs time and
memory. (Remember that Blender loads textures solely for convenience and to assist in accurate UV editing, and does not
export them along with any FLVER.)
"""
import re
import shutil
from pathlib import Path

from soulstruct.base.textures.dds import DDS, convert_dds_file
from soulstruct.containers.tpf import TPF


def dump_map_dds(game_map_dir: Path, dump_path: Path):
    dump_path.mkdir(exist_ok=True, parents=True)
    for map_subdir in game_map_dir.glob("m*"):
        if re.match(r"^m\d\d$", map_subdir.name):
            print(f"Dumping from {map_subdir}...")
            tpf_dict = TPF.collect_tpf_textures(map_subdir)
            for tga_path, texture in tpf_dict.items():
                dds_name = f"{Path(tga_path).stem}.dds"
                texture.write_dds(dump_path / dds_name)
                print(f"   {dds_name}")


def convert_dds_dump(source_dds_dump: Path, dest_dds_dump: Path, output_format="DXT1"):
    dest_dds_dump.mkdir(parents=True, exist_ok=True)
    for source_file in source_dds_dump.glob("*.dds"):
        dds = DDS.from_path(source_file)
        dest_file = dest_dds_dump / source_file.name
        if dds.fourcc == "DX10":
            convert_dds_file(source_file, dest_dds_dump, output_format)
            print(f"Converted DX10 DDS file to {output_format}: {source_file.name}")
        else:
            # Copy non-DX10 file without conversion.
            shutil.copy2(source_file, dest_file)


if __name__ == '__main__':
    # dump_map_dds(Path(DSR_PATH + "/map"), Path("D:/dds_dump_original"))
    convert_dds_dump(Path("D:/dds_dump_original"), Path("D:/dds_dump"))
