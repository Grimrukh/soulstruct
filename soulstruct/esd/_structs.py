from soulstruct.utilities.core import BinaryStruct
from soulstruct.esd import BaseESD


def get_esd_class(game_version: int, long: bool):

    if long:

        # End of internal header is zero padding DS1/DSR, -1 padding in later games
        internal_header_end = '16x' if game_version == 1 else ('internal_pad', '2q', [-1, -1])

        class ESD(BaseESD):
            EXTERNAL_HEADER_STRUCT = BinaryStruct(
                ('version', '4s', b'fsSL'),  # Note specific case.
                ('one', 'i', 1),
                ('game_version', '2i', [game_version, game_version]),
                ('table_size_offset', 'i', 84),
                ('internal_data_size', 'i'),  # excludes this external header
                ('unk', 'i', 6),
                ('internal_header_size', 'i', 72),
                ('internal_header_count', 'i', 1),
                ('state_machine_header_size', 'i', 32),
                ('state_machine_count', 'i'),
                ('state_size', 'i', 72),
                ('state_count', 'i'),
                ('condition_size', 'i', 56),
                ('condition_count', 'i'),
                ('command_size', 'i', 24),
                ('command_count', 'i'),
                ('command_arg_size', 'i', 16),
                ('command_arg_count', 'i'),
                ('condition_pointers_offset', 'i'),
                ('condition_pointers_count', 'i'),
                ('esd_name_offset_minus_1', 'i'),
                # Not sure why this is minus 1. Use the internal header for the real offset.
                ('esd_name_length', 'i'),  # equal to internal header
                ('unk_offset_1', 'i'),
                ('unk_size_1', 'i', 0),
                ('unk_offset_2', 'i'),
                ('unk_size_2', 'i', 0),
            )
            INTERNAL_HEADER_STRUCT = BinaryStruct(
                ('one', 'i', 1),
                ('magic', '4i'),
                '4x',
                ('state_machine_headers_offset', 'q', 72),
                ('state_machine_count', 'q'),
                ('esd_name_offset', 'q'),  # accurate, unlike external header
                ('esd_name_length', 'q'),
                # identical to external header entry; note this is only *half* the name byte size due to UTF-16
                internal_header_end
            )
            STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
                ('state_machine_index', 'q'),
                ('state_machine_offset', 'q'),
                ('state_count', 'q'),  # number of states
                ('state_machine_offset_2', 'q'),  # duplicate
            )
            DCX_MAGIC = (36, 44)

            class State(BaseESD.State):
                Condition = None
                Command = None

                STRUCT = BinaryStruct(
                    ('index', 'q'),
                    ('condition_pointers_offset', 'q'),
                    ('condition_pointers_count', 'q'),
                    ('enter_commands_offset', 'q'),
                    ('enter_commands_count', 'q'),
                    ('exit_commands_offset', 'q'),
                    ('exit_commands_count', 'q'),
                    ('ongoing_commands_offset', 'q'),
                    ('ongoing_commands_count', 'q'),
                )

            class Condition(BaseESD.Condition):
                STRUCT = BinaryStruct(
                    ('next_state_offset', 'q'),
                    ('pass_commands_offset', 'q'),
                    ('pass_commands_count', 'q'),
                    ('subcondition_pointers_offset', 'q'),
                    ('subcondition_pointers_count', 'q'),
                    ('test_ezl_offset', 'q'),
                    ('test_ezl_size', 'q'),
                )
                POINTER_STRUCT = BinaryStruct(
                    ('condition_offset', 'q'),
                )
                STATE_ID_FORMAT = 'q'

            class Command(BaseESD.Command):
                STRUCT = BinaryStruct(
                    ('bank', 'i'),  # Values of 1, 5, 6, 7 have been encountered.
                    ('index', 'i'),
                    ('args_offset', 'q'),
                    ('args_count', 'q'),
                )
                ARG_STRUCT = BinaryStruct(
                    ('arg_ezl_offset', 'q'),
                    ('arg_ezl_size', 'q'),
                )

    else:

        # End of internal header is zero padding DS1/DSR, -1 padding in later games
        internal_header_end = '8x' if game_version == 1 else ('internal_pad', '2i', [-1, -1])

        class ESD(BaseESD):
            EXTERNAL_HEADER_STRUCT = BinaryStruct(
                ('version', '4s', b'fSSL'),  # Note specific case.
                ('one', 'i', 1),
                ('game_version', '2i', [game_version, game_version]),
                ('table_size_offset', 'i', 84),
                ('internal_data_size', 'i'),  # excludes header size
                ('unk', 'i', 6),
                ('internal_header_size', 'i', 44),
                ('internal_header_count', 'i', 1),
                ('state_machine_header_size', 'i', 16),
                ('state_machine_count', 'i'),
                ('state_size', 'i', 36),
                ('state_count', 'i'),
                ('condition_size', 'i', 28),
                ('condition_count', 'i'),
                ('command_size', 'i', 16),
                ('command_count', 'i'),
                ('command_arg_size', 'i', 8),
                ('command_arg_count', 'i'),
                ('condition_pointers_offset', 'i'),
                ('condition_pointers_count', 'i'),
                ('esd_name_offset', 'i'),
                ('esd_name_size', 'i'),
                ('unk_offset_1', 'i'),
                ('unk_size_1', 'i', 0),
                ('unk_offset_2', 'i'),
                ('unk_size_2', 'i', 0),
            )
            INTERNAL_HEADER_STRUCT = BinaryStruct(
                ('one', 'i'),
                ('magic', '4i'),  # TODO: constant within games, at least?
                ('state_machine_headers_offset', 'i', 44),
                ('state_machine_count', 'i'),
                ('esd_name_offset', 'i'),
                ('esd_name_size', 'i'),
                internal_header_end,
            )
            STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
                ('state_machine_index', 'i'),
                ('state_machine_offset', 'i'),
                ('state_count', 'i'),  # number of states
                ('state_machine_offset_2', 'i'),  # duplicate
            )

            class State(BaseESD.State):
                STRUCT = BinaryStruct(
                    ('index', 'i'),
                    ('condition_pointers_offset', 'i'),
                    ('condition_pointers_count', 'i'),
                    ('enter_commands_offset', 'i'),
                    ('enter_commands_count', 'i'),
                    ('exit_commands_offset', 'i'),
                    ('exit_commands_count', 'i'),
                    ('ongoing_commands_offset', 'i'),
                    ('ongoing_commands_count', 'i'),
                )

            class Condition(BaseESD.Condition):
                STRUCT = BinaryStruct(
                    ('next_state_offset', 'i'),
                    ('pass_commands_offset', 'i'),
                    ('pass_commands_count', 'i'),
                    ('subcondition_pointers_offset', 'i'),
                    ('subcondition_pointers_count', 'i'),
                    ('test_ezl_offset', 'i'),
                    ('test_ezl_size', 'i'),
                )
                POINTER_STRUCT = BinaryStruct(
                    ('condition_offset', 'i'),
                )
                STATE_ID_FORMAT = 'q'

            class Command(BaseESD.Command):
                STRUCT = BinaryStruct(
                    ('bank', 'i'),  # Values of 1, 5, 6, 7 have been encountered.
                    ('index', 'i'),
                    ('args_offset', 'i'),
                    ('args_count', 'i'),
                )
                ARG_STRUCT = BinaryStruct(
                    ('arg_ezl_offset', 'i'),
                    ('arg_ezl_size', 'i'),
                )

    # Pass references between classes.
    ESD.State.Condition = ESD.Condition
    ESD.State.Command = ESD.Command
    ESD.Condition.Command = ESD.Command

    return ESD
