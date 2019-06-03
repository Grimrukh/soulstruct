""" Import order is very specific due to my lazy star import abuse. """

import sys
from soulstruct.core import BinaryStruct
from soulstruct.emevd import BaseEMEVD
from .constants import *
from . import decompiler
from . import verbose
from .enums import *
from .tests import *
from .instructions import *


NAME = 'ds1'


class EMEVD(BaseEMEVD):

    GAME_MODULE = sys.modules[globals()['__name__']]
    STRING_ENCODING = 'utf-8'
    DCX_MAGIC = (36, 44)

    HEADER_STRUCT = BinaryStruct(
        ('version', '4s', b'EVD\x00'),
        ('ds1_marker', 'I', 0),
        ('unknown', 'I', 204),
        ('file_size_1', 'I'),
        ('event_count', 'I'),
        ('event_table_offset', 'I'),
        ('instruction_count', 'I'),
        ('instruction_table_offset', 'I'),
        '4x',  # unknown table, unused in all games
        ('unknown_table_offset', 'I'),
        '4x',  # "event_layer_count" unused in DS1
        ('event_layer_table_offset', 'I'),  # unused in DS1
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
                ('unk1', 'i', -1),
                ('unk2', 'I', 0),
            )

            INSTRUCTION_ARG_TYPES = {
                2000: {0: '@iII', 1: '@iI', 2: '@B', 3: '@B', 4: '@I', 5: '@B'},
                2001: {},
                2002: {1: '@iI', 2: '@iIiBB', 3: '@iIi', 4: '@iIiBBi', 5: '@iIffifi'},
                2003: {1: '@iiBB', 2: '@iB', 3: '@iB', 4: '@i', 5: '@iiiiiii', 6: '@iB',
                       7: '@iB', 8: '@iiB', 9: '@i', 10: '@h', 11: '@bihh', 12: '@i',
                       13: '@iIB', 14: '@BBi', 15: '@i', 16: '@I', 17: '@IIB', 18: '@iiBBB',
                       19: '@hh', 20: '@i', 21: '@B', 22: '@iiB', 23: '@i', 24: '@iii',
                       25: '@iiiii', 26: '@iB', 27: '@B', 28: '@i', 29: '@Bb', 30: '@B',
                       31: '@iII', 32: '@iI', 33: '@i', 34: '@iiii', 35: '@ii', 36: '@i',
                       37: '@', 38: '@', 39: '@', 40: '@', 41: '@iifi', 49: '@i'},
                2004: {1: '@iB', 2: '@iB', 3: '@iBii', 4: '@iB', 5: '@iB', 6: '@iiB',
                       7: '@i', 8: '@ii', 9: '@iiiiii', 10: '@iB', 11: '@ii', 12: '@iB',
                       13: '@ii', 14: '@ii', 15: '@iB', 16: '@i', 17: '@iiB', 18: '@iif',
                       19: '@ii', 20: '@i', 21: '@ii', 22: '@ihhiffBB', 23: '@iiiB',
                       24: '@iiii', 25: '@iif', 26: '@iBB', 27: '@iBB', 28: '@ii',
                       29: '@iB', 30: '@iB', 31: '@iB', 32: '@iiBii', 33: '@ii', 34: '@iBb',
                       35: '@iB', 36: '@iii', 37: '@i', 38: '@B', 39: '@iB', 40: '@iBiii',
                       41: '@iBii', 42: '@iBiii', 43: '@iB', 44: '@iB', 45: '@ii',
                       46: '@B', 47: '@'},
                2005: {1: '@ib', 2: '@i', 3: '@iB', 4: '@iB', 5: '@iii', 6: '@iiB',
                       7: '@ii', 8: '@ib', 9: '@iiiiifff', 10: '@iBBB', 11: '@iih',
                       12: '@i', 13: '@iB', 14: '@iiiB', 15: '@i'},
                2006: {1: '@iB', 2: '@i', 3: '@iiii', 4: '@iii', 5: '@ii'},
                2007: {1: '@ihhif', 2: '@B', 3: '@iB', 4: '@iB', 5: '@i', 6: '@i', 7: '@i',
                       8: '@i', 9: '@i'},
                2008: {1: '@ii', 2: '@iiiiff', 3: '@BBH'},
                2009: {0: '@iii', 1: '@iii', 2: '@iii', 3: '@iiffi', 4: '@i', 5: '@ii', 6: '@B'},
                2010: {1: '@BHiii', 2: '@iii', 3: '@iB'},
                2011: {1: '@iB', 2: '@iB'},
                2012: {1: '@iB'},
                1000: {0: '@Bb', 1: '@BBb', 2: '@BBb', 3: '@B', 4: '@B', 5: '@Bbii',
                       6: '@Bbii', 7: '@BBb', 8: '@BBb', 9: '@f'},
                1001: {0: '@f', 1: '@i', 2: '@ff', 3: '@ii'},
                1003: {0: '@BBi', 1: '@BBBi', 2: '@BBBi', 3: '@BBBii', 4: '@BBBii', 5: '@Bb',
                       6: '@Bb', 7: '@BBBB', 8: '@BBBB'},
                1005: {0: '@Bi', 1: '@BBi', 2: '@BBi'},
                0: {0: '@bBb', 1: '@bbii'},
                1: {0: '@bf', 1: '@bi', 2: '@bff', 3: '@bii'},
                3: {0: '@bBBi', 1: '@bBBii', 2: '@bBii', 3: '@bBiif', 4: '@bBiB', 5: '@biifhfiBi',
                    6: '@bb', 7: '@bBi', 8: '@bBBB', 9: '@bI', 10: '@bBiibi', 11: '@bBBB',
                    12: '@biBBI', 13: '@biifhfiBi', 14: '@bi', 15: '@bii', 16: '@bBiB',
                    17: '@bBB', 18: '@biifhfiBii', 19: '@biifhfiBii', 20: '@biBBiB',
                    21: '@bB', 22: '@bB'},
                4: {0: '@biB', 1: '@bii', 2: '@bibf', 3: '@bib', 4: '@biiB', 5: '@biiB',
                    6: '@biiib', 7: '@biB', 8: '@biiB', 9: '@biB', 10: '@bB', 11: '@bB',
                    12: '@bB', 13: '@bBI', 14: '@biBi'},
                5: {0: '@bBi', 1: '@bii', 2: '@bi', 3: '@bibi'},
                11: {0: '@bi', 1: '@bi', 2: '@bi'}
            }

        class EventArg(BaseEMEVD.Event.EventArg):

            STRUCT = BinaryStruct(
                ('instruction_line', 'I'),
                ('write_from_byte', 'I'),
                ('read_from_byte', 'I'),
                ('bytes_to_write', 'I'),
                '4x',
            )
