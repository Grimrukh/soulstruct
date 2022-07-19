import logging
import os
import shutil
import xml.dom.minidom
from pathlib import Path

try:
    import pydub
except ImportError:
    pydub = None

from .fev import FEV, WavebankInfo
from .fsb import FSB, FSBSample, FSBSampleMode, fsbext


_LOGGER = logging.getLogger(__name__)


def find_paths_from_waveforms_with_bank_index(fev: FEV, bank_name: str, index: int):
    """Parses the given `FEV` to find Sound Definitions that reference the wavetable in wavebank `bank_name` at the
    given `index`, in order to determine the filepath of the wavetable.

    Returns a list of possible filepaths.
    """
    return_set = set()
    for sounddef in fev.sounddefs:
        for waveform in sounddef.waveforms:
            if waveform.bank_name == bank_name and waveform.index_in_bank == index:
                return_set.add(waveform.name)
    return list(return_set)


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
        _LOGGER.error(f"Cannot find extracted file '{compressed_file_path.name}' to move to bank hierarchy. Ignoring.")
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
                    print(f"Converting to WAV: {compressed_file_path} -> {wav_path.name} (MONO)")
                else:
                    print(f"Converting to WAV: {compressed_file_path} -> {wav_path.name}")
                try:
                    sound.export(wav_path, format="wav")
                except Exception as ex:
                    _LOGGER.error(f"Could not write '.wav' file {compressed_file_path.name} with pydub. Error:\n  {ex}")
                if delete_compressed_if_wav:
                    os.remove(compressed_file_path)  # delete compressed file


def create_fdp_from_fev(
    fev_path: Path | str,
    write_bank_path: Path | str = "",
    convert_to_wav=False,
) -> str:
    """Read FEV and FSB files and reconstruct FDP project file for FMOD Designer (just plaintext XML).

    Args:
        fev_path (Path or str): path of `.fev` file to read. There must be a `.fsb` file next to it with the same stem.
        write_bank_path (Path or str): path of folder where MP3 files from FSB will be unpacked to "bank/{fev_name}".
            Optional; defaults to empty string.
        convert_to_wav (bool): if True, and `write_bank_path` is given, the MP3 files written to the bank directory
            will also be converted to WAV files for easy re-use in FMOD. Voice files starting with "v" will further be
            converted to single-channel, which is the format expected by DSR.
    """
    fev_path = Path(fev_path)
    fev = FEV(fev_path)
    open_fsbs = {}  # type: dict[str, FSB]
    open_fevs = {}  # type: dict[str, FEV]

    xml_lines = fev.to_xml_lines_start()

    if write_bank_path:
        write_bank_path = Path(write_bank_path)
    elif convert_to_wav:
        _LOGGER.warning("`convert_bank_to_wav=True`, but no `write_bank_path` was given. Ignoring.")

    for bank in fev.wavebanks:
        bank_format = WavebankInfo.BankOutputFormat.PCM
        xml_lines += bank.to_xml_lines_header()

        fsb_path = fev_path.parent / (bank.bank_name + ".fsb")
        fsb = open_fsbs.setdefault(str(fsb_path), FSB(fsb_path))
        if write_bank_path:
            fsbext(f"\"{fsb_path}\"", f"-d \"{str(write_bank_path)}\\bank\"")

        if len(fsb.samples) > 0:
            # Try to determined bank file format from first sample.
            suffix = ""
            if fsb.samples[0].header.mode_flags & FSBSampleMode.FSOUND_IMAADPCM:
                bank_format = WavebankInfo.BankOutputFormat.ADPCM
                suffix = ""  # TODO: unknown
            if fsb.samples[0].header.mode_flags & FSBSampleMode.FSOUND_MPEG_LAYER2:
                bank_format = WavebankInfo.BankOutputFormat.MP2
                suffix = ".mp2"
            if fsb.samples[0].header.mode_flags & FSBSampleMode.FSOUND_MPEG_LAYER3:
                bank_format = WavebankInfo.BankOutputFormat.MP3
                suffix = ".mp3"

            bank_original_fev = None
            if fev_path.stem != bank.bank_name:
                # If the bank was not paired with this FEV (i.e. they have different names), search for and parse the
                # bank's FEV to identify paths for samples that are unused in this FEV.
                fsb_original_fev_filepath = fev_path.parent / (bank.bank_name + ".fev")
                if not fsb_original_fev_filepath.is_file():
                    raise FileNotFoundError(
                        f"Cannot find required file '{bank.bank_name + '.fev'}' associated with matching bank."
                    )
                bank_original_fev = open_fevs.setdefault(str(fsb_original_fev_filepath), FEV(fsb_original_fev_filepath))

            for index, sample in enumerate(fsb.samples):
                paths = find_paths_from_waveforms_with_bank_index(fev, bank.bank_name, index)
                if bank_original_fev:
                    # Bank is from a different FEV.
                    original_fev_paths = find_paths_from_waveforms_with_bank_index(
                        bank_original_fev, bank.bank_name, index
                    )
                    if not set(paths).issubset(set(original_fev_paths)):
                        _LOGGER.warning(
                            f"Searching original FEV SoundDefs for wavebank with name '{bank.bank_name}' and index "
                            f"{index} yielded {original_fev_paths} but searching given FEV SoundDefs yielded {paths},"
                            f"which is not a superset of the former. Using given."
                        )
                    else:
                        paths = original_fev_paths

                if len(paths) == 0:
                    default_path = f"bank/{bank.bank_name}/{sample.header.name}"
                    _LOGGER.warning(
                        f"Could not find any SoundDef referencing Wavebank '{bank.bank_name}' and index {index}. "
                        f"Defaulting to '{default_path}', which may need manual correction."
                    )
                    xml_lines += sample.header.to_xml_lines(Path(default_path))
                    wav_path = write_bank_path / default_path

                elif len(paths) == 1:
                    # Ideal outcome: found exactly one matching path.
                    xml_lines += sample.header.to_xml_lines(Path(paths[0]))
                    # print(sample)
                    wav_path = write_bank_path / paths[0]
                else:
                    _LOGGER.warning(
                        f"Searching SoundDefs for Wavebank with name '{bank.bank_name}' and index {index} "
                        f"yielded {paths}."
                    )
                    suspected_paths = [path for path in paths if sample.header.name in path]
                    if len(suspected_paths) == 1:
                        xml_lines += sample.header.to_xml_lines(Path(suspected_paths[0]))
                        wav_path = write_bank_path / suspected_paths[0]
                    else:
                        raise ValueError(
                            f"Searching SoundDefs for Wavebank '{bank.bank_name}' and index {index} yielded {paths}, "
                            f"which could not be reduced to one choice using sample name '{sample.header.name}'."
                        )

                if write_bank_path and suffix:
                    compressed_file_path = wav_path.with_name(wav_path.name + suffix)
                    move_extracted_mp3(
                        write_bank_path / "bank", sample, compressed_file_path, convert_to_wav=convert_to_wav
                    )

        xml_lines += bank.to_xml_lines_footer(bank_format)

    xml_lines += fev.to_xml_lines_end()

    # XML indentation.
    xml_string = "\n".join(xml_lines)
    dom = xml.dom.minidom.parseString(xml_string)
    return dom.toprettyxml(indent="    ", newl="")
