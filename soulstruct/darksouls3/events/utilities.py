from pathlib import Path

from soulstruct.base.events.core import convert_events as convert_events_base, compare_events as compare_events_base
from .emevd import EMEVD
from ..maps.constants import ALL_MAPS


def convert_events(output_type, output_directory, input_type=None, input_directory=None, maps=None):
    input_directory = Path(input_directory) if input_directory is not None else Path(__file__.parent) / "vanilla"
    if not maps:
        maps = ALL_MAPS
    return convert_events_base(
        output_type=output_type,
        output_directory=output_directory,
        input_directory=input_directory,
        maps=maps,
        emevd_class=EMEVD,
        input_type=input_type,
    )


def compare_events(source_1, source_2, use_evs=True):
    return compare_events_base(source_1, source_2, emevd_class=EMEVD, use_evs=use_evs)