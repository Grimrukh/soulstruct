__all__ = ["convert_events", "compare_events", "scrape_event_info"]

import re
from pathlib import Path

from soulstruct.base.events.core import convert_events as convert_events_base, compare_events as compare_events_base
from .emevd import EMEVD
from ..maps.constants import ALL_MAPS_NO_CHALICE


def convert_events(
    output_type,
    output_directory,
    input_type=None,
    input_directory=None,
    maps=None,
    check_hash=False,
    merge_emevd_paths=(),
):
    """Convert all Dark Souls 1 event files of any format (binary EMEVD, EVS script, numeric text) to any other format.

    Args:
        output_type (str): Output type (extension) of file. Should be one of:
            'emevd', 'emevd.dcx', 'evs' (or 'py' or 'evs.py' or 'emevd.py'), or 'numeric' (or 'txt' or 'numeric.txt')
        output_directory: Path to write event files to. Backups of existing files will be made if no backup exists.
        input_type (str): Input type (extension) of file, from same options as `output_type`. By default, any input
            type will be accepted for each map, with an error being raised if the same map has multiple file types.
        input_directory: Path to read event files from. Defaults to vanilla EVS scripts that come with Soulstruct.
        maps: Sequence of maps to look for. These should be `Map` constants. By default, all maps will be converted.
        check_hash (bool): If True, will not replace existing file with same hash. (Default: False)
        merge_emevd_paths: Paths of files with valid EMEVD file stems to merge into matching input sources.
    """
    input_directory = Path(input_directory) if input_directory is not None else Path(__file__).parent / "vanilla"
    if maps is None:
        maps = ALL_MAPS_NO_CHALICE
    return convert_events_base(
        output_type=output_type,
        output_directory=output_directory,
        input_directory=input_directory,
        maps=maps,
        emevd_class=EMEVD,
        input_type=input_type,
        check_hash=check_hash,
        merge_emevd_paths=merge_emevd_paths,
    )


def compare_events(emevd_1, emevd_2, use_evs=True):
    return compare_events_base(emevd_1, emevd_2, use_evs=use_evs)


def scrape_event_info(evs_path: Path | str):
    """Parse an EVS file's text to create a dictionary mapping event IDs to their Python function names and docstrings.

    Useful if you've done some renaming work and want to turn it into an `EVENT_INFO` dictionary for `GameEnumsManager`.
    """

    def_re = re.compile(r"^def (.*)\(")  # NOTE: has no issue with multi-line defs
    doc_re = re.compile(r" {4}\"\"\" (\d+): (.*)\"\"\"", re.MULTILINE)

    evs_text = Path(evs_path).read_text(encoding="utf-8")
    event_info = {}
    event_name = None
    for line in evs_text.split("\n"):
        if match := def_re.match(line):
            event_name = match.group(1)
        if match := doc_re.match(line):
            if event_name is None:
                raise ValueError(f"Found docstring before event def: {line}")
            event_info[int(match.group(1))] = (event_name, match.group(2).strip())
            event_name = None
    print("EVENT_INFO = {")
    for k, v in event_info.items():
        print(f"    {k}: (\"{v[0]}\", \"{v[1]}\"),")
    print("}")
