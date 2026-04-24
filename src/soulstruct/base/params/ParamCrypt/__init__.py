from __future__ import annotations

__all__ = ["ParamCrypt", "ParamCryptError"]

import logging
import os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from soulstruct.exceptions import SoulstructError

_LOGGER = logging.getLogger(__name__)


class ParamCryptError(SoulstructError):
    pass


DS3_REGULATION_KEY = b"ds3#jn/8_7(rsY9pg55GFN7VFL#+3n/)"
ER_REGULATION_KEY = bytes([
    0x99, 0xBF, 0xFC, 0x36, 0x6A, 0x6B, 0xC8, 0xC6, 0xF5, 0x82, 0x7D, 0x09, 0x36, 0x02, 0xD6, 0x76,
    0xC4, 0x28, 0x92, 0xA0, 0x1C, 0x20, 0x7F, 0xB0, 0x24, 0xD3, 0xAF, 0x4E, 0x49, 0x3F, 0xEF, 0x99
])


def decrypt_byte_array(key: bytes, data: bytes) -> bytes:
    iv = data[:16]
    encrypted_content = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # No padding for decryption in ParamCrypt
    return decryptor.update(encrypted_content) + decryptor.finalize()


def encrypt_byte_array(key: bytes, data: bytes) -> bytes:
    # Use random IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # PKCS7 padding for encryption in ParamCrypt
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_content = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_content


def ParamCrypt(input_file_path: Path | str, mode="", game_type="", output_file_path: Path | str = ""):
    """
    Args:
        input_file_path: path of file to encrypt/decrypt.
        mode: 'encrypt' or 'decrypt' (auto-detected from input name if possible).
        game_type: 'ds3' or 'er' (auto-detected from input name if possible).
        output_file_path: path of file to write. Defaults to `input_file_path` with appropriate new extension.
    """
    input_file_path = Path(input_file_path)
    if not input_file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_file_path}")

    do_encrypt = None
    key = None

    if not mode or not game_type:
        # Auto-detect
        name = input_file_path.name
        if name == "Data0.bdt":
            do_encrypt = False
            key = DS3_REGULATION_KEY
            if not output_file_path:
                output_file_path = input_file_path.with_suffix(".parambnd.dcx")
        elif name == "Data0.parambnd.dcx":
            do_encrypt = True
            key = DS3_REGULATION_KEY
            if not output_file_path:
                output_file_path = input_file_path.with_suffix(".bdt")
        elif name == "regulation.bin":
            do_encrypt = False
            key = ER_REGULATION_KEY
            if not output_file_path:
                output_file_path = input_file_path.with_suffix(".parambnd.dcx")
        elif name == "regulation.parambnd.dcx":
            do_encrypt = True
            key = ER_REGULATION_KEY
            if not output_file_path:
                output_file_path = input_file_path.with_suffix(".bin")
        else:
            if not mode or not game_type:
                raise ValueError(f"Cannot auto-determine mode or game from file name '{name}'.")

    if mode:
        if mode == "encrypt":
            do_encrypt = True
        elif mode == "decrypt":
            do_encrypt = False
        else:
            raise ValueError(f"Invalid mode: {mode}")

    if game_type:
        if game_type.lower() == "ds3":
            key = DS3_REGULATION_KEY
        elif game_type.lower() == "er":
            key = ER_REGULATION_KEY
        else:
            raise ValueError(f"Invalid game type: {game_type}")

    if not output_file_path:
        ext = ".bin" if do_encrypt else ".parambnd.dcx"
        output_file_path = input_file_path.with_suffix(ext)
    else:
        output_file_path = Path(output_file_path)

    data = input_file_path.read_bytes()
    try:
        if do_encrypt:
            result = encrypt_byte_array(key, data)
        else:
            result = decrypt_byte_array(key, data)
    except Exception as e:
        raise ParamCryptError(f"Error during ParamCrypt {mode}: {e}")

    # Create backup if it doesn't already exist.
    if output_file_path.exists() and not output_file_path.with_suffix(output_file_path.suffix + ".bak").exists():
        import shutil
        shutil.copy2(output_file_path, str(output_file_path) + ".bak")

    output_file_path.write_bytes(result)
