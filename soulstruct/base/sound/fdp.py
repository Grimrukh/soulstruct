import logging
import typing as tp
import xml.dom.minidom
from pathlib import Path

from soulstruct.base.sound.fev import FEV, WavebankInfo
from soulstruct.base.sound.fsb import FSB, FSBSampleMode


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


def generate_fdp_xml(fev_path: Path, write_bank_path: tp.Union[str, Path] = "") -> str:
    """Read FEV and FSB files and reconstruct FDP project file for FMOD Designer (just plaintext XML).

    If `write_bank_path` is given, the FSB sample data (usually MP3 files) will be written to
    `{write_bank_path}/bank/{bank_name}/{file_name}`.
    """
    fev_path = Path(fev_path)
    fev = FEV(fev_path)
    open_fsbs = {}  # type: dict[str, FSB]
    open_fevs = {}  # type: dict[str, FEV]

    xml_lines = fev.to_xml_lines_start()

    if write_bank_path:
        write_bank_path = Path(write_bank_path)

    for bank in fev.wavebanks:
        bank_format = WavebankInfo.BankOutputFormat.PCM
        xml_lines += bank.to_xml_lines_header()

        fsb_path = fev_path.parent / (bank.bank_name + ".fsb")
        fsb = open_fsbs.setdefault(str(fsb_path), FSB(fsb_path))

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
                    if write_bank_path and suffix:
                        sample.write_mp3((write_bank_path / default_path).with_suffix(suffix))
                elif len(paths) == 1:
                    # Ideal outcome: found exactly one matching path.
                    xml_lines += sample.header.to_xml_lines(Path(paths[0]))
                    if write_bank_path and suffix:
                        print(sample)
                        sample.write_mp3((write_bank_path / paths[0]).with_suffix(suffix))
                else:
                    _LOGGER.warning(
                        f"Searching SoundDefs for Wavebank with name '{bank.bank_name}' and index {index} "
                        f"yielded {paths}."
                    )
                    suspected_paths = [path for path in paths if sample.header.name in path]
                    if len(suspected_paths) == 1:
                        xml_lines += sample.header.to_xml_lines(Path(suspected_paths[0]))
                        if write_bank_path and suffix:
                            sample.write_mp3((write_bank_path / suspected_paths[0]).with_suffix(suffix))
                    else:
                        raise ValueError(
                            f"Searching SoundDefs for Wavebank '{bank.bank_name}' and index {index} yielded {paths}, "
                            f"which could not be reduced to one choice using sample name '{sample.header.name}'."
                        )

        xml_lines += bank.to_xml_lines_footer(bank_format)

    xml_lines += fev.to_xml_lines_end()

    # XML indentation.
    xml_string = "\n".join(xml_lines)
    dom = xml.dom.minidom.parseString(xml_string)
    return dom.toprettyxml(indent="    ", newl="")


if __name__ == '__main__':
    p = Path("C:/Steam/steamapps/common/DARK SOULS REMASTERED (Nightfall)/sound/fdlc_c4510.fev")
    s = generate_fdp_xml(p, write_bank_path="C:/Dark Souls/Projects/NightfallMod/GrimAudio")
    Path("C:/Dark Souls/Projects/NightfallMod/GrimAudio/fdlc_c4510.fdp").write_text(s)
