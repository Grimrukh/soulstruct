"""Dump raw metaparam bytes for analysis."""
from pathlib import Path
from soulstruct.config import ELDEN_RING_PATH
from soulstruct.containers import Binder
from soulstruct.utilities.binary import BinaryReader


def dump_metaparam(shader_stem: str, shaderbdlebnd: Binder):
    shaderbdle = Binder.from_binder_entry(shaderbdlebnd.find_entry_name(f"{shader_stem}.shaderbdle"))
    metaparam_entry = shaderbdle.find_entry_name(f"{shader_stem}.metaparam")
    data = metaparam_entry.get_uncompressed_data()
    r = BinaryReader(data)

    print(f"\n{'='*80}")
    print(f"SHADER: {shader_stem}")
    print(f"Total metaparam size: {len(data)} bytes (0x{len(data):X})")

    # Dump header
    print(f"\n--- HEADER (0x00 - 0x97) ---")
    r.seek(0)
    header_hex = data[:0x98].hex()
    for off in range(0, 0x98, 16):
        chunk = data[off:off+16]
        hex_str = ' '.join(f'{b:02X}' for b in chunk)
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"  0x{off:04X}: {hex_str:<48s} {ascii_str}")

    r.seek(0x0C)
    sampler_count = r.unpack_value("i")
    print(f"\n  sampler_count at 0x0C: {sampler_count}")

    # Try reading other potential header fields
    r.seek(0)
    print(f"  0x00 as int32: {r.unpack_value('i')}")
    r.seek(4)
    print(f"  0x04 as int32: {r.unpack_value('i')}")
    r.seek(8)
    print(f"  0x08 as int32: {r.unpack_value('i')}")

    # Dump each sampler record
    print(f"\n--- SAMPLER RECORDS ({sampler_count} samplers, each 0x30 bytes starting at 0x98) ---")
    for i in range(sampler_count):
        base = 0x98 + (0x30 * i)
        r.seek(base)

        # Read all fields
        sampler_name_off = r.unpack_value("q")  # +0x00
        unknown_08 = data[base+0x08:base+0x10]  # +0x08 (8 bytes, currently skipped)
        default_tex_off = r.unpack_value("q", offset=base+0x10)
        group_name_off = r.unpack_value("q", offset=base+0x18)
        unknown_20 = data[base+0x20:base+0x30]  # +0x20 (16 bytes, never read)

        sampler_name = r.unpack_string(offset=sampler_name_off, encoding="utf-16-le")
        default_tex = r.unpack_string(offset=default_tex_off, encoding="utf-16-le")
        group_name = r.unpack_string(offset=group_name_off, encoding="utf-16-le")

        # Interpret unknown bytes multiple ways
        unk08_as_int64 = int.from_bytes(unknown_08, 'little', signed=True)
        unk08_as_2int32 = (
            int.from_bytes(unknown_08[0:4], 'little', signed=True),
            int.from_bytes(unknown_08[4:8], 'little', signed=True),
        )
        unk20_as_2int64 = (
            int.from_bytes(unknown_20[0:8], 'little', signed=True),
            int.from_bytes(unknown_20[8:16], 'little', signed=True),
        )
        unk20_as_4int32 = (
            int.from_bytes(unknown_20[0:4], 'little', signed=True),
            int.from_bytes(unknown_20[4:8], 'little', signed=True),
            int.from_bytes(unknown_20[8:12], 'little', signed=True),
            int.from_bytes(unknown_20[12:16], 'little', signed=True),
        )

        # Check if +0x08 could be an offset to another string
        unk08_as_string = ""
        if 0 < unk08_as_int64 < len(data):
            try:
                unk08_as_string = r.unpack_string(offset=unk08_as_int64, encoding="utf-16-le")
            except Exception:
                pass

        print(f"\n  Sampler [{i}] at 0x{base:04X}:")
        print(f"    name:     {sampler_name}")
        print(f"    default:  {default_tex}")
        print(f"    group:    '{group_name}'")
        print(f"    +0x08 raw:     {' '.join(f'{b:02X}' for b in unknown_08)}")
        print(f"    +0x08 as i64:  {unk08_as_int64}")
        print(f"    +0x08 as 2xi32:{unk08_as_2int32}")
        if unk08_as_string:
            print(f"    +0x08 as str:  '{unk08_as_string}'")
        print(f"    +0x20 raw:     {' '.join(f'{b:02X}' for b in unknown_20)}")
        print(f"    +0x20 as 2xi64:{unk20_as_2int64}")
        print(f"    +0x20 as 4xi32:{unk20_as_4int32}")

    # Also dump the string table area (after all sampler records)
    string_area_start = 0x98 + (0x30 * sampler_count)
    print(f"\n--- STRING TABLE starts at 0x{string_area_start:04X} ---")
    # Show first 256 bytes of string table
    end = min(string_area_start + 512, len(data))
    for off in range(string_area_start, end, 16):
        chunk = data[off:min(off+16, end)]
        hex_str = ' '.join(f'{b:02X}' for b in chunk)
        print(f"  0x{off:04X}: {hex_str}")


if __name__ == '__main__':
    _shaderbdlebnd = Binder.from_path(ELDEN_RING_PATH / "shader/shaderbdle.shaderbdlebnd.dcx")
    for stem in ["C[DetailBlend]", "C[Fur]", "C[AMSN]", "C[DetailBlend][S2]"]:
        dump_metaparam(stem, _shaderbdlebnd)
