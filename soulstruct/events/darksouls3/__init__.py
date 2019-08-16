""" Import order is very specific due to my lazy star import abuse. """

import sys
from soulstruct.utilities.core import BinaryStruct
from soulstruct.events import BaseEMEVD
from .constants import *
from . import decompiler
from .instructions import *
from .tests import *


NAME = 'darksouls3'


def get_enums():
    import soulstruct.enums.darksouls3
    return soulstruct.enums.darksouls3


class EMEVD(BaseEMEVD):

    GAME_MODULE = sys.modules[globals()['__name__']]
    STRING_ENCODING = 'utf-16le'
    DCX_MAGIC = (68, 76)

    HEADER_STRUCT = BinaryStruct(
        ('version', '4s', b'EVD\x00'),
        ('ds3_marker_1', 'I', 130816),
        ('ds3_marker_2', 'I', 205),
        ('file_size_1', 'I'),
        ('event_count', 'Q'),
        ('event_table_offset', 'Q'),
        ('instruction_count', 'Q'),
        ('instruction_table_offset', 'Q'),
        '8x',  # unknown table, unused in all games
        ('unknown_table_offset', 'Q'),
        ('event_layers_count', 'Q'),
        ('event_layers_table_offset', 'Q'),
        ('event_arg_count', 'Q'),
        ('event_arg_table_offset', 'Q'),
        ('linked_files_count', 'Q'),
        ('linked_files_table_offset', 'Q'),
        ('base_arg_data_size', 'Q'),
        ('base_arg_data_offset', 'Q'),
        ('packed_strings_size', 'Q'),
        ('packed_strings_offset', 'Q'),
        # No more 4x at the end.
    )

    def compute_base_args_size(self, existing_data_size):
        """ Pad to multiple of 16 bytes. """
        total_arg_size = sum([e.total_args_size for e in self.events.values()])
        while (existing_data_size + total_arg_size) % 16 != 0:
            total_arg_size += 1
        return total_arg_size

    def pad_after_base_args(self, emevd_binary_after_base_args):
        """ Pad to multiple of 16 bytes. """
        while len(emevd_binary_after_base_args) % 16 != 0:
            emevd_binary_after_base_args += b'\0'
        return emevd_binary_after_base_args

    class Event(BaseEMEVD.Event):

        STRUCT = BinaryStruct(
            ('event_id', 'Q'),
            ('instruction_count', 'Q'),
            ('first_instruction_offset', 'Q'),
            ('event_arg_count', 'Q'),
            ('first_event_arg_offset', 'q'),
            ('restart_type', 'I'),
            '4x',
        )

        class Instruction(BaseEMEVD.Event.Instruction):

            STRUCT = BinaryStruct(
                ('instruction_class', 'I'),
                ('instruction_index', 'I'),
                ('base_args_size', 'Q'),
                ('first_base_arg_offset', 'i'),
                '4x',
                ('first_event_layers_offset', 'q'),
            )

            INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES

            class EventLayers(BaseEMEVD.Event.Instruction.EventLayers):

                STRUCT = BinaryStruct(
                    ('two', 'I', 2),
                    ('event_layers', 'I'),  # 32-bit bit field
                    ('zero', 'Q', 0),
                    ('minus_one', 'q', -1),
                    ('one', 'Q', 1),
                )

        class EventArg(BaseEMEVD.Event.EventArg):

            STRUCT = BinaryStruct(
                ('instruction_line', 'Q'),
                ('write_from_byte', 'Q'),
                ('read_from_byte', 'Q'),
                ('bytes_to_write', 'Q'),
            )
