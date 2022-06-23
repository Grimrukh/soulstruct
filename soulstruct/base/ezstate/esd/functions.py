"""Constructs functions dynamically from their stub definition in `functions.pyi`, which should not be edited.

Currently identical for all (supported) games.
"""

__all__ = ["COMMANDS", "TEST_FUNCTIONS", "State"]

import re

from soulstruct.darksouls1ptde.game_types.internal_types import ESDType
from soulstruct.utilities.files import PACKAGE_PATH


COMMANDS = {ESDType.CHR: {}, ESDType.TALK: {}}
TEST_FUNCTIONS = {ESDType.CHR: {}, ESDType.TALK: {}}

# Construct command/function tables.

_COMMAND_RE = re.compile(r"^# command (chr|talk)\[(\d*)]\[(\d*)]")
_TEST_RE = re.compile(r"^# test (chr|talk)\[(\d*)]")
_FUNCTION_DEF_RE = re.compile(r"^def ([\w\d_]*)\(([\w\d :_,*]*)\)")


def _parse_function_def(i_: int, line: str):
    function_def_match_ = re.match(_FUNCTION_DEF_RE, line)
    if function_def_match_ is None:
        raise ValueError(f"functions.pyi LINE {i_}: Expected a function definition after '# COMMAND/TEST...' line.")
    name_ = function_def_match_.group(1)
    args_with_type_hints = [arg.strip() for arg in function_def_match_.group(2).split(",")]
    if "*args" in args_with_type_hints:
        # No argument names or types.
        return name_, (), ()
    args_ = []
    type_hints_ = []
    for arg_hint in args_with_type_hints:
        if not arg_hint:
            continue
        if ":" in arg_hint:
            arg, type_hint = [a.strip() for a in arg_hint.split(":")]
            args_.append(arg)
            type_hints_.append(type_hint)
        else:
            args_.append(arg_hint)
            type_hints_.append(None)
    return name_, tuple(args_), tuple(type_hints_)


_stubs_path = PACKAGE_PATH("base/ezstate/esd/functions.pyi")
with open(_stubs_path) as f:
    _stub_lines = f.readlines()
i = 0
while i < len(_stub_lines) - 1:
    command_match = re.match(_COMMAND_RE, _stub_lines[i])
    if command_match is not None:
        esd_type, bank, f_id = command_match.group(1, 2, 3)
        i += 1
        COMMANDS[ESDType(esd_type)].setdefault(int(bank), {})[int(f_id)] = _parse_function_def(i, _stub_lines[i])
        i += 1
        continue
    test_match = re.match(_TEST_RE, _stub_lines[i])
    if test_match is not None:
        esd_type, f_id = test_match.group(1, 2)
        i += 1
        TEST_FUNCTIONS[ESDType(esd_type)][int(f_id)] = _parse_function_def(i, _stub_lines[i])
        i += 1
        continue
    function_def_match = re.match(_FUNCTION_DEF_RE, _stub_lines[i])
    if function_def_match is not None:
        raise ValueError(f"functions.pyi LINE {i}: Found a function definition with no # COMMAND/TEST line before it.")
    i += 1


# Construct inverse dictionaries.

COMMANDS_BANK_ID_BY_TYPE_NAME = {}  # {(esd_type, command_name: (bank, f_id)}
for esd_type, banks in COMMANDS.items():
    for bank, commands in banks.items():
        for f_id, command in commands.items():
            COMMANDS_BANK_ID_BY_TYPE_NAME[esd_type, command[0]] = (bank, f_id)

TEST_FUNCTIONS_ID_BY_TYPE_NAME = {}  # {(esd_type, test_function_name: f_id}
for esd_type, commands in TEST_FUNCTIONS.items():
    for f_id, command in commands.items():
        TEST_FUNCTIONS_ID_BY_TYPE_NAME[esd_type, command[0]] = f_id


ATTACK_REQUEST_TYPE = {
    0: "R1",
    1: "L1",
    2: "Catalyst / Talisman / Pyromancy Flame R1",
    3: "Catalyst / Talisman / Pyromancy Flame L1",
    10: "Backstep",
    14: "Use Goods",
    15: "Roll Forward",
    16: "Roll Backward",
    17: "Roll Left",
    18: "Roll Right",
    22: "AttackArm_Gesture0 (Beckon)",
    23: "AttackArm_Gesture1 (Point Forward)",
    24: "AttackArm_Gesture2 (Hurrah!)",
    25: "AttackArm_Gesture3 (Bow)",
    26: "AttackArm_Gesture4 (Joy)",
    27: "AttackArm_Gesture5 (Shrug)",
    28: "AttackArm_Gesture6 (Wave)",
    29: "AttackArm_Gesture7 (Praise the Sun)",
    30: "AttackArm_Gesture8 (Point Up)",
    31: "AttackArm_Gesture9 (Point Down)",
    32: "AttackArm_Gesture10 (Look Skyward)",
    33: "AttackArm_Gesture11 (Well! What is it!)",
    34: "AttackArm_Gesture12 (Prostration)",
    35: "AttackArm_Gesture13 (Proper Bow)",
    36: "AttackArm_Gesture14 (Prayer)",
    37: "AttackArm_Gesture15 (Unused)",  # Has Prayer animation as placeholder
    38: "AttackArm_Gesture16 (Unused)",  # Has carving toss animation as placeholder
    39: "AttackArm_Gesture17 (Unused)",  # Has lever pull animation as placeholder
    40: "AttackArm_Gesture18 (Unused)",  # Has turn crank animation as placeholder
    41: "AttackArm_Gesture19 (Unused)",  # Has turn rotunda animation as placeholder
    42: "Jump",
    52: "Left Hand Crossbow Ammo Swap",
}

ANIM_CATEGORY = {
    0: "Based on Left Hand Motion Category",
    1: "Based on Right Hand Motion Category",
    2: "Based on current Move Param",
    3: "Absolute Animation ID",
}


ANIM_LAYER_INDEX = {
    0: "Wait",
    1: "SpWait",
    2: "WalkLR",
    3: "WalkFB",
    4: "Guard",
    5: "Attack",
    6: "SpecialAttack",
    7: "Action",
    8: "Damage S",
    9: "Damage L",
    10: "Event",
    11: "ExtraAnim",
    12: "TaeExtraAnim",
}


class State:
    """Dummy import for ESP intellisense. Intended usage defined in `functions.pyi`."""
    pass
