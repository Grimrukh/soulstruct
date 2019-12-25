import sys
from pathlib import Path

from soulstruct.utilities.core import BinaryStruct
from soulstruct.events import BaseEMEVD
from .constants import *
from . import decompiler
from .instructions import *
from .tests import *
from soulstruct.enums.darksouls1 import *


NAME = 'darksouls1'


def get_enums():
    import soulstruct.enums.darksouls1
    return soulstruct.enums.darksouls1


class EMEVD(BaseEMEVD):
    GAME_MODULE = sys.modules[globals()['__name__']]
    STRING_ENCODING = 'utf-8'
    DCX_MAGIC = (36, 44)

    HEADER_STRUCT = BinaryStruct(
        ('version', '4s', b'EVD\x00'),
        ('ds1_marker_1', 'I', 0),
        ('ds1_marker_2', 'I', 204),
        ('file_size_1', 'I'),
        ('event_count', 'I'),
        ('event_table_offset', 'I'),
        ('instruction_count', 'I'),
        ('instruction_table_offset', 'I'),
        '4x',  # unknown table, unused in all games
        ('unknown_table_offset', 'I'),
        ('event_layers_count', 'I'),  # unused in DS1
        ('event_layers_table_offset', 'I'),  # unused in DS1
        ('event_arg_count', 'I'),
        ('event_arg_table_offset', 'I'),
        ('linked_files_count', 'I'),
        ('linked_files_table_offset', 'I'),
        ('base_arg_data_size', 'I'),
        ('base_arg_data_offset', 'I'),
        ('packed_strings_size', 'I'),
        ('packed_strings_offset', 'I'),
        '4x',
    )

    def compute_base_args_size(self, existing_data_size):
        return sum([e.total_args_size for e in self.events.values()]) + 4

    def pad_after_base_args(self, emevd_binary_after_base_args):
        # Terminate with z4.
        return emevd_binary_after_base_args + b'\x00\x00\x00\x00'

    class Event(BaseEMEVD.Event):
        use = 1

        STRUCT = BinaryStruct(
            ('event_id', 'I'),
            ('instruction_count', 'I'),
            ('first_instruction_offset', 'I'),
            ('event_arg_count', 'I'),
            ('first_event_arg_offset', 'i'),
            ('restart_type', 'I'),
            '4x',
        )

        class Instruction(BaseEMEVD.Event.Instruction):
            STRUCT = BinaryStruct(
                ('instruction_class', 'I'),
                ('instruction_index', 'I'),
                ('base_args_size', 'I'),
                ('first_base_arg_offset', 'i'),
                ('first_event_layers_offset', 'i'),
                '4x',
            )

            INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES

            class EventLayers(BaseEMEVD.Event.Instruction.EventLayers):
                """ Never used in DS1 and very probably not actually supported by the engine. """

                STRUCT = BinaryStruct(
                    ('two', 'I', 2),
                    ('event_layers', 'I'),  # 32-bit bit field
                    ('zero', 'I', 0),  # format is a guess
                    ('minus_one', 'i', -1),  # format is a guess
                    ('one', 'I', 1),  # format is a guess
                )

        class EventArg(BaseEMEVD.Event.EventArg):
            STRUCT = BinaryStruct(
                ('instruction_line', 'I'),
                ('write_from_byte', 'I'),
                ('read_from_byte', 'I'),
                ('bytes_to_write', 'I'),
                '4x',
            )


EVENT_EXTENSIONS = {
    "evs": {".evs", ".evs.py", ".py", ".emevd.py"},
    "emevd": {".emevd"},
    "emevd.dcx": {".emevd.dcx"},
    "numeric": {".numeric", ".txt", ".numeric.txt"},
}


def convert_events(output_type, output_directory, input_type=None, input_directory=None, maps=()):
    """Convert all events from one format to another.

    The possible formats are 'evs' (or 'py'), 'emevd', 'emevd.dcx', and 'numeric' (or 'txt'). By default, the input
    type is auto-detected from the name of each EMEVD file with the appropriate map formatting (e.g.
    'm10_00_00_00.emevd.py', 'm10_01_00_00.numeric.txt') in the input directory (which defaults to the packaged vanilla
    'evs.py' scripts).

    A subset of EMEVD map constants to convert can be passed to `maps`, or it can be left to default to looking for all
    EMEVD files used in this game (in which case an error will be raised if any are not found).
    """
    output_ext = "." + output_type.lower().lstrip(".")
    output_type = None
    for ext_type, exts in EVENT_EXTENSIONS.items():
        if output_ext in exts:
            output_type = ext_type
    if output_type is None:
        raise ValueError(f"Invalid EMEVD output extension: {repr(output_ext)}.")
    output_directory = Path(output_directory)
    input_ext = "." + input_type.lower().lstrip(".") if input_type is not None else None
    input_directory = Path(input_directory) if input_directory is not None else Path(__file__, 'evs')
    if not maps:
        maps = ALL_MAPS
    emevd_sources = {m.emevd_file_name: None for m in maps}
    all_exts = EVENT_EXTENSIONS["evs"].union(EVENT_EXTENSIONS["emevd"].union(
        EVENT_EXTENSIONS["emevd.dcx"].union(EVENT_EXTENSIONS["numeric"])))
    for available in input_directory.glob("*"):
        parts = available.name.split(".")
        name, ext = parts[0], '.' + '.'.join(parts[1:])
        if name in emevd_sources and (ext == input_ext or (input_ext is None and ext in all_exts)):
            if emevd_sources[name] is not None:
                raise FileExistsError(f"Found multiple files named {repr(name)} with different extensions.")
            emevd_sources[name] = available
    missing = [name for name, source in emevd_sources.items() if source is None]
    if missing:
        raise FileNotFoundError(f"Could not find EMEVD sources for: {missing}.")
    for name, source in emevd_sources.items():
        try:
            emevd = EMEVD(source)
            output_path = output_directory / (name + output_ext)
            if output_type == "evs":
                emevd.write_evs(output_path)
            elif output_type == "emevd":
                emevd.write_emevd(output_path, dcx=False)
            elif output_type == "emevd.dcx":
                emevd.write_emevd(output_path, dcx=True)
            elif output_type == "numeric":
                emevd.write_numeric(output_path)
        except Exception as e:
            raise ValueError(f"Encountered an error while attempting to compile {name + output_ext}: {str(e)}")
