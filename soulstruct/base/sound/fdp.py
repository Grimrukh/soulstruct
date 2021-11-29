import logging
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


def generate_fdp_xml(fev_path: Path):
    """Read FEV and FSB files and reconstruct FDP project file for FMOD Designer (just plaintext XML)."""
    fev_path = Path(fev_path)
    fev = FEV(fev_path)
    open_fsbs = {}  # type: dict[str, FSB]
    open_fevs = {}  # type: dict[str, FEV]

    xml_lines = fev.to_xml_string_start()

    for bank in fev.wavebanks:
        bank_format = WavebankInfo.BankOutputFormat.PCM
        xml_lines += bank.to_xml_string_header()

        fsb_path = fev_path.parent / (bank.bank_name + ".fsb")
        fsb = open_fsbs.setdefault(str(fsb_path), FSB(fsb_path))

        # Determine bank format, if possible.
        if len(fsb.samples) > 0:
            sample = fsb.samples[0]
            if sample.header.mode_flags & FSBSampleMode.FSOUND_IMAADPCM:
                bank_format = WavebankInfo.BankOutputFormat.ADPCM
            if sample.header.mode_flags & FSBSampleMode.FSOUND_MPEG_LAYER2:
                bank_format = WavebankInfo.BankOutputFormat.MP2
            if sample.header.mode_flags & FSBSampleMode.FSOUND_MPEG_LAYER3:
                bank_format = WavebankInfo.BankOutputFormat.MP3

            # If the bank was not paired with this FEV (i.e. they have different names), search for and parse the
            # bank's FEV to identify paths for samples that are unused in this FEV.
            bank_original_fev = None
            if fev_path.stem != bank.bank_name:
                fsb_original_fev_filepath = fev_path.parent / (bank.bank_name + ".fev")
                if not fsb_original_fev_filepath.is_file():
                    raise FileNotFoundError(
                        f"Cannot find required file '{bank.bank_name + '.fev'}' associated with matching bank."
                    )
                bank_original_fev = open_fevs.setdefault(str(fsb_original_fev_filepath), FEV(fsb_original_fev_filepath))

            for index, sample in enumerate(fsb.samples):
                paths = find_paths_from_waveforms_with_bank_index(fev, bank.bank_name, index)
                if bank_original_fev:
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
                    xml_lines += sample.header.to_xml_string(Path(default_path))
                elif len(paths) == 1:
                    xml_lines += sample.header.to_xml_string(Path(paths[0]))
                else:
                    _LOGGER.warning(
                        f"Searching SoundDefs for Wavebank with name '{bank.bank_name}' and index {index} "
                        f"yielded {paths}."
                    )
                    suspected_paths = [path for path in paths if sample.header.name in path]
                    if len(suspected_paths) == 1:
                        xml_lines += sample.header.to_xml_string(Path(suspected_paths[0]))
                    else:
                        raise ValueError(
                            f"Searching SoundDefs for Wavebank '{bank.bank_name}' and index {index} yielded {paths}, "
                            f"which could not be reduced to one choice using suspection sample name "
                            f"'{sample.header.name}'."
                        )

        xml_lines += bank.to_xml_string_footer(bank_format)

    xml_lines += fev.to_xml_string_end()

    # XML indentation.
    xml_string = "\n".join(xml_lines)
    dom = xml.dom.minidom.parseString(xml_string)
    return dom.toprettyxml(indent="    ", newl="")


if __name__ == '__main__':
    p = Path("C:/Steam/steamapps/common/DARK SOULS REMASTERED (Nightfall)/sound/frpg_c2240.fev")
    # p = Path(r"C:\Users\Scott\Downloads\frpg_c5420_fdp\frpg_c5420.fev")
    s = generate_fdp_xml(p)
    with Path(r"C:\Users\Scott\Downloads\frpg_c5420_fdp\frpg_c5420_grim.fdp").open("w") as f:
        f.write(s)
