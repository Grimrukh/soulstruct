from soulstruct.core import BinaryStruct
from soulstruct.esd import BaseESD


class ESD(BaseESD):
    EXTERNAL_HEADER_STRUCT = BinaryStruct(
        ('version', '4s', b'fSSL'),  # Note specific case.
        ('version_tail', '3i', [1, 1, 1]),
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
        ('magic', '4i'),  # (big, big, big, big)  TODO: constant within games, at least?
        ('state_machine_headers_offset', 'i', 44),
        ('state_machine_count', 'i'),
        ('esd_name_offset', 'i'),
        ('esd_name_size', 'i'),
        '8x',  # zero in DS1/DSR, -1 in later games
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
