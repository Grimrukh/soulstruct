from __future__ import annotations

__all__ = ["ParamCrypt", "ParamCryptError"]

import logging
import subprocess
from pathlib import Path

from soulstruct.exceptions import SoulstructError

_LOGGER = logging.getLogger("soulstruct")


PARAM_CRYPT_EXE = Path(__file__).parent / "ParamCrypt.exe"


class ParamCryptError(SoulstructError):
    pass


def ParamCrypt(input_file_path: Path | str, mode="", game_type="", output_file_path: Path | str = ""):
    """Run `ParamCrypt` executable to encrypt/decrypt DS3 or ER Param binder.

    Does not touch DCX, open the Binder, etc.

    Args:
        input_file_path: path of file to encrypt/decrypt.
        mode: 'encrypt' or 'decrypt' (auto-detected from input name if possible).
        game_type: 'ds3' or 'er' (auto-detected from input name if possible).
        output_file_path: path of file to write. Defaults to `input_file_path` with appropriate new extension.
    """
    args = [str(PARAM_CRYPT_EXE), str(input_file_path)]
    if mode:
        if mode not in {"encrypt", "decrypt"}:
            raise ValueError(f"`mode` must be 'encrypt' or 'decrypt' if given, not: {mode}")
        args.append(mode)
    if game_type:
        if game_type.lower() not in {"ds3", "er"}:
            raise ValueError(f"`game_type` must be 'ds3' or 'er' if given, not: {game_type}")
        args.append(game_type.lower())
    if output_file_path:
        args.append(str(output_file_path))

    output = subprocess.run(args, text=True, capture_output=True)
    if output.stdout:
        _LOGGER.info(output.stdout)

    if output.returncode != 0:
        raise ParamCryptError(f"`ParamCrypt` encountered an error: {output.stderr}")
