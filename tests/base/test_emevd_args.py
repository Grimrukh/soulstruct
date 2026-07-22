"""Unit tests for EMEVD instruction argument packing/unpacking and event-argument replacement.

These are almost all pure-unit tests: they build synthetic `Instruction`/`Event`/`EventArgRepl`
objects (using the Dark Souls 1 Remastered concrete subclasses purely as a vehicle for the
game-specific `EMEDF` class variable) and exercise the shared base machinery in
`soulstruct.base.events.emevd`.
"""
from __future__ import annotations

import struct

import pytest

from soulstruct.base.events.emevd.emedf import ArgType
from soulstruct.base.events.emevd.event import EVS_ARG_TYPES, EventSignature, SingleEventArg
from soulstruct.base.events.emevd.event_layers import EventLayers
from soulstruct.base.events.emevd.instruction import EventArgRepl
from soulstruct.base.events.emevd.utils import (
    EventArgumentData,
    boolify,
    format_event_layers,
    get_byte_offset_from_struct,
    get_write_offset,
)
from soulstruct.base.events.evs.decompiler import reprocess_opt_args
from soulstruct.base.events.evs.utils import EVS_TYPES, PY_TYPES, define_args
from soulstruct.darksouls1r.events.emevd.core import Event, Instruction

# Format strings that use only fixed-width numeric types (no 's' string-index type).
NUMERIC_FMTS = ["i", "B", "iIhb", "bhi", "BBH", "iiB", "iII", "fif", "BBBB", "hhi", "bbbbi", "IiHhBbf"]


# ---------------------------------------------------------------------------
# `ArgType` (EMEDF internal type enum)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("arg_type", list(ArgType))
def test_arg_type_fmt_roundtrip(arg_type: ArgType):
    """`get_fmt()` -> `from_fmt()` must be an exact round trip for every `ArgType`."""
    assert ArgType.from_fmt(arg_type.get_fmt()) is arg_type


@pytest.mark.parametrize("arg_type", [t for t in ArgType if t is not ArgType.fixstr])
def test_arg_type_size_matches_struct(arg_type: ArgType):
    """Declared size must match `struct.calcsize()` of the format character."""
    assert struct.calcsize(arg_type.get_fmt()) == arg_type.get_size()


def test_fixstr_size_disagrees_with_struct_calcsize():
    """`fixstr` is documented as a 4-byte string index but its format char 's' calcsizes to 1.

    This mismatch is the root cause of the `get_byte_offset_from_struct` bug below; the code works
    around it by replacing 's' with 'I' before packing (`Instruction.struct_args_fmt`).
    """
    assert ArgType.fixstr.get_size() == 4
    assert struct.calcsize(ArgType.fixstr.get_fmt()) == 1  # NOT 4


@pytest.mark.parametrize("arg_type", list(ArgType))
def test_arg_type_min_max_ordering(arg_type: ArgType):
    lo, hi = arg_type.get_type_min_max()
    assert lo <= 0 <= hi


def test_arg_type_min_max_matches_bit_width():
    assert ArgType.u8.get_type_min_max() == (0, 2 ** 8 - 1)
    assert ArgType.u16.get_type_min_max() == (0, 2 ** 16 - 1)
    assert ArgType.u32.get_type_min_max() == (0, 2 ** 32 - 1)
    assert ArgType.s8.get_type_min_max() == (-2 ** 7, 2 ** 7 - 1)
    assert ArgType.s16.get_type_min_max() == (-2 ** 15, 2 ** 15 - 1)
    assert ArgType.s32.get_type_min_max() == (-2 ** 31, 2 ** 31 - 1)


def test_arg_type_invalid_fmt_raises():
    with pytest.raises(ValueError):
        ArgType.from_fmt("q")


# ---------------------------------------------------------------------------
# `get_byte_offset_from_struct` / `get_write_offset` / `define_args`
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("fmt", NUMERIC_FMTS)
def test_byte_offset_dict_matches_native_struct_layout(fmt: str):
    """Offsets must match the real native-aligned layout of the packed args."""
    offsets = get_byte_offset_from_struct(fmt)
    assert len(offsets) == len(fmt), "one entry per format character (no offset collisions)"
    expected = {}
    for i in range(len(fmt)):
        offset = struct.calcsize("@" + fmt[:i + 1]) - struct.calcsize("@" + fmt[i])
        expected[offset] = (i, fmt[i])
    assert offsets == expected


def test_byte_offset_dict_known_values():
    assert get_byte_offset_from_struct("iIhb") == {0: (0, "i"), 4: (1, "I"), 8: (2, "h"), 10: (3, "b")}
    assert get_byte_offset_from_struct("bhi") == {0: (0, "b"), 2: (1, "h"), 4: (2, "i")}


def test_byte_offset_dict_ignores_optional_arg_separator():
    """The '|' required/optional separator must not shift any offsets."""
    assert get_byte_offset_from_struct("iII|III") == get_byte_offset_from_struct("iIIIII")


@pytest.mark.parametrize("fmt", NUMERIC_FMTS)
def test_write_offset_agrees_with_byte_offset_dict(fmt: str):
    """`get_write_offset` (used when COMPILING) must agree with `get_byte_offset_from_struct`
    (used when DECOMPILING); otherwise event args are written to the wrong instruction arg."""
    offsets = {index: offset for offset, (index, _) in get_byte_offset_from_struct(fmt).items()}
    for i in range(len(fmt)):
        assert get_write_offset(fmt, i) == offsets[i], f"arg {i} of '{fmt}'"


@pytest.mark.parametrize("fmt", NUMERIC_FMTS)
def test_define_args_offsets_and_sizes(fmt: str):
    """`define_args` must produce `(write_offset, size)` matching the real packed layout."""
    args = define_args(fmt)
    assert len(args) == len(fmt)
    offsets = {index: offset for offset, (index, _) in get_byte_offset_from_struct(fmt).items()}
    for i, (offset, size) in enumerate(args):
        assert offset == offsets[i]
        assert size == struct.calcsize(fmt[i])


def test_define_args_rejects_unknown_format_char():
    with pytest.raises(ValueError):
        define_args("iq")


@pytest.mark.xfail(
    reason="`PY_TYPES['str']`/`EVS_TYPES` advertise the 's' (fixstr) event-arg type, but "
           "`define_args`/`get_write_offset` do not handle it. API inconsistency.",
    strict=False,
)
def test_define_args_supports_advertised_string_type():
    assert "s" in EVS_TYPES and PY_TYPES["str"] == "s"
    assert define_args("is") == [(0, 4), (4, 4)]


@pytest.mark.xfail(
    reason="BUG: `get_byte_offset_from_struct` calcsizes 's' as 1 byte instead of 4, so any "
           "instruction with an 's' arg followed by another arg gets wrong offsets "
           "(e.g. Bloodborne/DS3 instructions (2013, 2) and (2013, 4)).",
    strict=False,
)
@pytest.mark.parametrize("fmt", ["IsB", "BsB", "ss", "sh"])
def test_byte_offset_dict_handles_string_args(fmt: str):
    """'s' is a 4-byte index into the packed string block, exactly like 'I'."""
    assert get_byte_offset_from_struct(fmt) == {
        offset: (index, fmt[index])
        for offset, (index, _) in get_byte_offset_from_struct(fmt.replace("s", "I")).items()
    }


# ---------------------------------------------------------------------------
# `Instruction` argument packing
# ---------------------------------------------------------------------------


def test_instruction_struct_fmt_strips_separator_and_string_type():
    instr = Instruction(category=2000, index=0, display_args_fmt="iIi|If", args_list=[0, 1, 2, 3, 4.0])
    assert instr.struct_args_fmt == "iIiIf"
    assert instr.instruction_id == "2000[00]"


def test_instruction_rejects_arg_count_mismatch():
    with pytest.raises(ValueError, match="does not match length of format string"):
        Instruction(category=2003, index=2, display_args_fmt="iB", args_list=[1])


@pytest.mark.parametrize("fmt", NUMERIC_FMTS)
def test_instruction_base_args_size_is_four_aligned(fmt: str):
    args = [1.0 if c == "f" else 1 for c in fmt]
    instr = Instruction(category=2003, index=2, display_args_fmt=fmt, args_list=args)
    assert instr.base_args_size == struct.calcsize(f"@{fmt}0i")
    assert instr.base_args_size % 4 == 0
    # Actual packed data must be exactly this long.
    assert len(struct.pack(f"@{fmt}0i", *args)) == instr.base_args_size


@pytest.mark.parametrize("fmt", NUMERIC_FMTS)
def test_instruction_arg_pack_unpack_roundtrip(fmt: str):
    """Pack -> unpack of instruction base args must be value-stable for representative values."""
    values = []
    for c in fmt:
        values.append({"i": -5, "I": 4000000000, "h": -300, "H": 40000, "b": -7, "B": 200, "f": 1.5}[c])
    packed = struct.pack(f"@{fmt}0i", *values)
    unpacked = list(struct.unpack(f"@{fmt}0i", packed))
    assert unpacked == values


def test_reprocess_opt_args_reinterprets_ints_as_floats():
    """`RunEvent` optional args are read as `I` and re-typed once the event signature is known."""
    raw = struct.unpack("2I", struct.pack("if", -3, 2.5))
    assert reprocess_opt_args(list(raw), "if") == (-3, 2.5)


def test_reprocess_opt_args_handles_string_type_as_uint():
    raw = struct.unpack("1I", struct.pack("I", 12))
    assert reprocess_opt_args(list(raw), "s") == (12,)


# ---------------------------------------------------------------------------
# `EventArgRepl` / event-argument replacement processing
# ---------------------------------------------------------------------------


def _make_instr_with_repls(category, index, fmt, args, repls) -> Instruction:
    instr = Instruction(category=category, index=index, display_args_fmt=fmt, args_list=list(args))
    for write_offset, read_offset, size in repls:
        instr.event_arg_replacements.append(
            EventArgRepl(instruction_line=0, write_offset=write_offset, read_offset=read_offset, size=size)
        )
    return instr


def test_event_arg_repl_arg_range_is_inclusive():
    repl = EventArgRepl(instruction_line=0, write_offset=0, read_offset=4, size=4)
    assert repl.arg_range == (4, 7)


def test_process_event_arg_replacements_assigns_names_fmts_and_indices():
    # (2004, 6) EzstateAIRequest(character: i, command_id: i, command_slot: B)
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4), (8, 4, 1)])
    instr.process_event_arg_replacements()
    assert instr.evs_args_list == ["arg_0_3", 0, "arg_4_4"]
    by_index = {r.arg_index: r for r in instr.event_arg_replacements}
    assert by_index[0].name == "character" and by_index[0].fmt == "i"
    assert by_index[2].name == "command_slot" and by_index[2].fmt == "B"


def test_process_event_arg_replacements_sorts_by_read_offset():
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(8, 4, 1), (0, 0, 4)])
    instr.process_event_arg_replacements()
    assert [r.arg_range for r in instr.event_arg_replacements] == [(0, 3), (4, 4)]


def test_process_event_arg_replacements_rejects_misaligned_write_offset():
    """A replacement that does not start exactly at an argument boundary must be rejected."""
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(2, 0, 4)])
    with pytest.raises(ValueError, match="misaligned|begins at byte"):
        instr.process_event_arg_replacements()


def test_process_event_arg_replacements_rejects_oversized_replacement():
    """A 4-byte event arg cannot be written over a 1-byte instruction argument."""
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(8, 0, 4)])
    with pytest.raises(ValueError, match="too small"):
        instr.process_event_arg_replacements()


def test_run_event_replacement_inside_args_tuple():
    """`RunEvent`'s variable `args` tuple is typed as `tuple` in EMEDF; replacements inside it get
    the placeholder name 'event_arg' (later replaced by consensus naming)."""
    instr = _make_instr_with_repls(2000, 0, "iII", [0, 11000100, 0], [(8, 0, 4)])
    instr.process_event_arg_replacements()
    repl = instr.event_arg_replacements[0]
    assert repl.arg_index == 2
    assert repl.name == "event_arg"
    assert instr.evs_args_list[2] == "arg_0_3"


def test_get_required_and_optional_args_split():
    instr = Instruction(
        category=2000, index=0, display_args_fmt="iIi|II", args_list=[0, 1, 2, 3, 4]
    )
    instr.process_event_arg_replacements()
    required, optional = instr.get_required_and_optional_args()
    assert required == [0, 1, 2]
    assert optional == [3, 4]


def test_get_called_event():
    assert Instruction(2000, 0, "iII", args_list=[0, 11000100, 0]).get_called_event() == 11000100
    assert Instruction(2000, 6, "II", args_list=[9000, 0]).get_called_event() == 9000
    assert Instruction(2003, 2, "iB", args_list=[1, 1]).get_called_event() is None


# ---------------------------------------------------------------------------
# `SingleEventArg` / `EventSignature`
# ---------------------------------------------------------------------------


def _single_arg(fmts: set[str], size: int) -> SingleEventArg:
    arg = SingleEventArg(arg_range=(0, size - 1))
    arg.fmts = set(fmts)
    arg.sizes = {size}
    return arg


@pytest.mark.parametrize(
    "fmts, size, expected",
    [
        ({"i"}, 4, "i"),          # unique matching format wins
        ({"f"}, 4, "f"),
        ({"B"}, 1, "B"),
        ({"h"}, 2, "h"),
        ({"i", "I"}, 4, "I"),     # ambiguous same-size ints -> unsigned default
        ({"i"}, 1, "B"),          # usage format larger than replacement size -> size default
        ({"f"}, 1, "B"),          # incompatible float usage -> size default
        ({"i", "f"}, 4, "I"),     # incompatible mixed usage -> size default
    ],
)
def test_guess_arg_fmt(fmts, size, expected):
    arg = _single_arg(fmts, size)
    assert arg.guess_arg_fmt(-1, "test_arg", size) == expected


def test_guess_arg_fmt_smaller_usage_than_size_falls_back():
    """A 1-byte usage of a 4-byte event arg is invalid; the default 4-byte type is used."""
    arg = _single_arg({"B", "i"}, 4)
    assert arg.guess_arg_fmt(-1, "test_arg", 4) == "I"


def test_remove_generic_names_keeps_specific_name():
    arg = SingleEventArg(arg_range=(0, 3))
    arg.names = {"entity", "character"}
    arg.remove_generic_names()
    assert arg.names == {"character"}


def test_remove_generic_names_keeps_lone_generic_name():
    arg = SingleEventArg(arg_range=(0, 3))
    arg.names = {"entity"}
    arg.remove_generic_names()
    assert arg.names == {"entity"}


def test_combined_name_joins_multiple_usages():
    arg = SingleEventArg(arg_range=(0, 3))
    arg.names = {"character", "attacker"}
    arg.fmts = {"i"}
    arg.sizes = {4}
    arg.py_types = {int}
    arg.compute_combined_info(set())
    assert arg.combined_name == "attacker__character"  # sorted and joined with '__'


def test_event_signature_arg_names_deduplicated():
    args = []
    for _ in range(3):
        arg = SingleEventArg(arg_range=(0, 3))
        arg.combined_name = "flag"
        args.append(arg)
    sig = EventSignature(args)
    assert sig.get_evs_arg_names() == ["flag", "flag_1", "flag_2"]


def test_event_signature_full_fmt_and_arg_string():
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4), (8, 4, 1)])
    event = Event(11000100, 0, [instr])
    assert event.signature.get_full_fmt() == "iB"
    assert event.signature.get_evs_arg_names() == ["character", "command_slot"]
    arg_string = event.signature.get_evs_arg_string()
    assert arg_string.startswith("_, ")  # slot placeholder prepended
    assert "character: Character | int" in arg_string
    assert "command_slot: uchar" in arg_string


def test_event_signature_empty_has_no_slot_placeholder():
    event = Event(11000100, 0, [Instruction(2003, 2, "iB", args_list=[1, 1])])
    assert event.signature.event_args == []
    assert event.signature.get_evs_arg_string() == ""
    assert event.signature.get_full_fmt() == ""


def test_event_signature_arg_string_crashes_without_combined_fmt():
    """Documents a fragile path: if `compute_combined_info` bails out early (e.g. conflicting
    replacement sizes), `combined_fmt` stays empty and `get_evs_arg_string` raises `KeyError`
    instead of a helpful error."""
    arg = SingleEventArg(arg_range=(0, 3))
    arg.combined_name = "broken"
    assert arg.combined_fmt == ""
    assert "" not in EVS_ARG_TYPES
    with pytest.raises(KeyError):
        EventSignature([arg]).get_evs_arg_string()


def test_update_signature_renames_instruction_args_consistently():
    """Two instructions using the same event arg range must agree on the final EVS name."""
    instr_1 = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4)])  # 'character'
    instr_2 = _make_instr_with_repls(2003, 2, "iB", [0, 1], [(0, 0, 4)])  # 'flag' (vague)
    instr_2.event_arg_replacements[0].instruction_line = 1
    event = Event(11000100, 0, [instr_1, instr_2])
    assert event.signature.get_evs_arg_names() == ["character"]  # 'flag' is a vague name, dropped
    assert instr_1.evs_args_list[0] == "character"
    assert instr_2.evs_args_list[0] == "character"


def test_event_arg_replacements_count():
    instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4), (8, 4, 1)])
    event = Event(11000100, 0, [instr])
    assert event.event_arg_replacements_count == 2
    assert event.instruction_count == 1
    assert event.total_args_size == instr.base_args_size


# ---------------------------------------------------------------------------
# `Event.update_run_event_instructions` (arg re-typing from called event signature)
# ---------------------------------------------------------------------------


def test_update_run_event_instructions_retypes_float_args():
    """A `RunEvent` instruction's packed args are re-unpacked using the called event's signature."""
    called_instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4)])
    called_event = Event(11000100, 0, [called_instr])

    packed_float = struct.unpack("I", struct.pack("f", 2.5))[0]
    run_instr = Instruction(2000, 0, "iII", args_list=[0, 11000100, packed_float])
    caller = Event(0, 0, [run_instr])
    caller.update_run_event_instructions({11000100: called_event.signature})
    # `character` arg is 'i', so the packed float should be re-read as a signed int (not a float).
    assert run_instr.display_args_fmt == "iIi"
    assert run_instr.args_list == [0, 11000100, packed_float]

    # Now force the called event's arg format to float and re-run.
    called_event.signature.event_args[0].combined_fmt = "f"
    run_instr_2 = Instruction(2000, 0, "iII", args_list=[0, 11000100, packed_float])
    caller_2 = Event(0, 0, [run_instr_2])
    caller_2.update_run_event_instructions({11000100: called_event.signature})
    assert run_instr_2.display_args_fmt == "iIf"
    assert run_instr_2.args_list == [0, 11000100, pytest.approx(2.5)]


def test_update_run_event_instructions_handles_excess_args():
    """Extra packed arg data (more than the event uses) is preserved as unsigned integers."""
    called_instr = _make_instr_with_repls(2004, 6, "iiB", [0, 0, 0], [(0, 0, 4)])
    called_event = Event(11000100, 0, [called_instr])
    run_instr = Instruction(2000, 0, "iII|II", args_list=[0, 11000100, 1, 2, 3])
    caller = Event(0, 0, [run_instr])
    caller.update_run_event_instructions({11000100: called_event.signature})
    assert run_instr.args_list[:3] == [0, 11000100, 1]
    assert len(run_instr.args_list) == 5  # excess data retained


def test_update_run_event_instructions_noop_without_signatures():
    run_instr = Instruction(2000, 0, "iII", args_list=[0, 11000100, 7])
    event = Event(0, 0, [run_instr])
    event.update_run_event_instructions(None, None)
    assert run_instr.display_args_fmt == "iII"


# ---------------------------------------------------------------------------
# Misc utilities
# ---------------------------------------------------------------------------


def test_boolify():
    assert boolify(0) is False
    assert boolify(1) is True
    assert boolify(2) == 2
    assert boolify("arg_0_3") == "arg_0_3"


def test_format_event_layers():
    assert format_event_layers(None) == ""
    assert format_event_layers(3) == "<3>"
    assert format_event_layers([0, 2]) == "<0, 2>"
    assert format_event_layers((1,)) == "<1>"
    with pytest.raises(TypeError):
        format_event_layers("nope")


def test_event_layers_bitfield():
    layers = EventLayers(0b1011)
    assert layers.get_enabled_event_layers() == [0, 1, 3]
    assert layers.to_evs() == "event_layers=[0, 1, 3]"
    assert layers.to_numeric() == " <0, 1, 3>"
    assert EventLayers.flags_to_uint([0, 1, 3]) == 0b1011
    assert hash(layers) == hash(EventLayers(0b1011))


def test_event_argument_data_repr():
    assert repr(EventArgumentData(4, 4)) == "EventArgumentData(4, 4)"
    assert "Character" in repr(EventArgumentData(4, 4, _character_type()))


def _character_type():
    from soulstruct.darksouls1r.game_types import Character
    return Character
