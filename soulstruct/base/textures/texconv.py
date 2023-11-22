from __future__ import annotations

__all__ = ["TexconvError", "texconv", "texconv_to_dds", "batch_texconv_to_dds"]

import multiprocessing
import subprocess
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.files import PACKAGE_PATH


class TexconvError(SoulstructError):
    """Error raised by `texconv` subprocess."""
    pass


def texconv(*args):
    texconv_path = PACKAGE_PATH("base/textures/texconv.exe")
    if not texconv_path.is_file():
        raise FileNotFoundError("Cannot find `texconv.exe` that should be bundled with Soulstruct in 'base/textures'.")
    return subprocess.run(
        [texconv_path, *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def texconv_to_dds(output_dir: str, dds_format: str, is_dx10: bool, mipmap_count: int, input_path: str) -> bytes | None:
    """Run `texconv` on a single file, returning the output DDS data."""
    args = [
        "-o", output_dir, "-ft", "dds", "-f", dds_format,
        "-m", str(mipmap_count), "-nologo", input_path
    ]
    if is_dx10:
        args.insert(4, "-dx10")  # use extended DX10 header
    texconv_result = texconv(*args)
    output_name = Path(input_path).with_suffix(".dds").name
    try:
        return Path(output_dir, output_name).read_bytes()
    except FileNotFoundError:
        print(f"Could not find converted DDS file. Stdout: {texconv_result.stdout.decode()}")
        return None


def batch_texconv_to_dds(output_dir: Path, dds_kwargs: dict[str, dict]) -> dict[str, bytes]:
    """Run `texconv` in parallel on multiple files, returning a dictionary of output DDS data.

    `output_dir` should be a temporary location that can be used to write the DDS files (which are immediately read).

    `dds_format`, `is_dx10`, `mipmap_count`, and `input_path` are all required in `dds_kwargs` for each key.
    """

    dds_args = []
    for input_path, kwargs in dds_kwargs.items():
        dds_args.append((
            str(output_dir),
            kwargs["dds_format"],
            kwargs["is_dx10"],
            kwargs["mipmap_count"],
            kwargs["input_path"],
        ))

    with multiprocessing.Pool() as pool:
        all_dds_bytes = pool.starmap(texconv_to_dds, dds_args)

    failed_keys = []
    dds_dict = {}
    for dds_key, dds_bytes in zip(dds_kwargs.keys(), all_dds_bytes):
        if dds_bytes is None:
            failed_keys.append(dds_key)
            dds_dict[dds_key] = b""
        else:
            dds_dict[dds_key] = dds_bytes

    return dds_dict
