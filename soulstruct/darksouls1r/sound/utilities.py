from __future__ import annotations

import logging
import os
import shutil
import typing as tp
from pathlib import Path

try:
    import pydub
except ImportError:
    pydub = None

if tp.TYPE_CHECKING:
    from .fsb import FSBSample

_LOGGER = logging.getLogger("soulstruct")

_PYDUB_WARNING_DONE = False


def move_extracted_mp3(
    extracted_dir: Path,
    sample: FSBSample,
    compressed_file_path: Path,
    convert_to_wav=False,
    delete_compressed_if_wav=True,
):
    """Find `file_path.name` in `extracted_dir`, and move it to actual `file_path`.

    `fsbext` dumps all FSB MP3s in one folder (`extracted_dir`), so this is needed to properly organize the bank.

    If `convert_to_wav=True`, also uses `pydub` (if installed) to convert MP3s to WAVs.
    """
    global _PYDUB_WARNING_DONE

    try:
        extracted_path = next(extracted_dir.glob(compressed_file_path.name))
    except StopIteration:
        _LOGGER.error(
            f"Cannot find extracted file '{extracted_dir / compressed_file_path.name}' to move to bank hierarchy."
        )
        return

    compressed_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(extracted_path, compressed_file_path)

    if convert_to_wav:
        if pydub is None:
            if not _PYDUB_WARNING_DONE:
                _LOGGER.warning("Cannot convert bank MP3 files to WAV files without `pydub` package.")
                _PYDUB_WARNING_DONE = True
        else:
            try:
                sound = pydub.AudioSegment.from_mp3(compressed_file_path)
            except Exception as ex:
                _LOGGER.error(f"Could not load compressed file {compressed_file_path.name} with pydub. Error:\n  {ex}")
            else:
                wav_path = compressed_file_path.parent / (compressed_file_path.name.split(".")[0] + ".wav")
                if sample.header.channel_count == 1:
                    sound.set_channels(1)
                    _LOGGER.info(f"Converting to WAV: {compressed_file_path} -> {wav_path.name} (MONO)")
                else:
                    _LOGGER.info(f"Converting to WAV: {compressed_file_path} -> {wav_path.name}")
                try:
                    sound.export(wav_path, format="wav")
                except Exception as ex:
                    _LOGGER.error(f"Could not write '.wav' file {compressed_file_path.name} with pydub. Error:\n  {ex}")
                if delete_compressed_if_wav:
                    os.remove(compressed_file_path)  # delete compressed file
