import sys
from soulstruct.core import BinaryStruct
from soulstruct.emevd import BaseEMEVD
from .constants import *
from . import decompiler
from .instructions import *
from .tests import *


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
