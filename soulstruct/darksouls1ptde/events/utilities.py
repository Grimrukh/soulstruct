from pathlib import Path

from soulstruct.base.events.core import convert_events as convert_events_base, compare_events as compare_events_base
from .emevd import EMEVD
from ..maps import ALL_MAPS


def convert_events(output_type, output_directory, input_type=None, input_directory=None, maps=None, check_hash=False):
    """Convert all Dark Souls 1 event files of any format (binary EMEVD, EVS script, numeric text) to any other format.

    Args:
        output_type (str): Output type (extension) of file. Should be one of:
            'emevd', 'emevd.dcx', 'evs' (or 'py' or 'evs.py' or 'emevd.py'), or 'numeric' (or 'txt' or 'numeric.txt')
        output_directory: Path to write event files to. Backups of existing files will be made if no backup exists.
        input_type (str): Input type (extension) of file, from same options as `output_type`. By default, any input
            type will be accepted for each map, with an error being raised if the same map has multiple file types.
        input_directory: Path to read event files from. Defaults to vanilla EVS scripts that come with Soulstruct.
        maps: Sequence of maps to look for. These should be `Map` constants. By default, all maps will be converted.
    """
    input_directory = Path(input_directory) if input_directory is not None else Path(__file__).parent / "vanilla"
    if maps is None:
        maps = ALL_MAPS
    return convert_events_base(
        output_type=output_type,
        output_directory=output_directory,
        input_directory=input_directory,
        maps=maps,
        emevd_class=EMEVD,
        input_type=input_type,
        check_hash=check_hash,
    )


def compare_events(source_1, source_2, use_evs=True):
    return compare_events_base(source_1, source_2, emevd_class=EMEVD, use_evs=use_evs)
