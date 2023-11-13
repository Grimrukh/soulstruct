from __future__ import annotations

__all__ = ["TexconvError", "texconv"]

import subprocess

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
