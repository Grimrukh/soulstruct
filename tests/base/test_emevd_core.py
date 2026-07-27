"""Tests for the shared binary EMEVD reader/writer and the 'numeric' text format.

Dark Souls 1: Remastered is used as a concrete vehicle for the base machinery in
`soulstruct.base.events.emevd`; per-game EMEVD behaviour is tested elsewhere.
"""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from soulstruct.base.events.emevd.core import EMEVDHeaderStruct
from soulstruct.base.events.emevd.event import EventStruct
from soulstruct.base.events.emevd.event_layers import EventLayers, EventLayersStruct
from soulstruct.base.events.emevd.exceptions import NumericEmevdError
from soulstruct.base.events.emevd.instruction import EventArgStruct, InstructionStruct
from soulstruct.base.events.enums import OnRestBehavior
from soulstruct.darksouls1r.events import EMEVD
from soulstruct.darksouls1r.events.emevd.core import Event, Instruction
from soulstruct.utilities.binary import BinaryReader, ByteOrder

EVS_HEADER = '"""m10_00_00_00\n\nlinked:\n\n\nstrings:\n\n"""\n'


@pytest.fixture(scope="session")
def ds1r_emevd_path(tests_dir: Path) -> Path:
    """Path to the committed DSR test EMEVD (used as a realistic vehicle for base machinery)."""
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_00_00.emevd.dcx"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture
def ds1r_emevd(ds1r_emevd_path: Path) -> EMEVD:
    return EMEVD.from_path(ds1r_emevd_path)


def _simple_emevd(body: str) -> EMEVD:
    return EMEVD.from_evs_string(EVS_HEADER + body, map_name="m10_00_00_00")


# ---------------------------------------------------------------------------
# Binary structure sanity (no game data required)
# ---------------------------------------------------------------------------


def test_header_struct_field_order():
    """Header field order is load-bearing: offsets are filled by name after reservation."""
    names = [f.name for f in EMEVDHeaderStruct.get_binary_fields()]
    assert names[:6] == [
        "_signature", "big_endian", "varint_size_check", "version_unk_1", "version_unk_2", "version"
    ]
    for name in (
        "events_count", "events_offset", "instructions_count", "instructions_offset",
        "event_layers_count", "event_layers_offset", "event_arg_replacements_count",
        "event_arg_replacements_offset", "linked_files_count", "linked_files_offset",
        "base_arg_data_size", "base_arg_data_offset", "packed_strings_size", "packed_strings_offset",
    ):
        assert name in names


def test_sub_struct_fields_present():
    assert [f.name for f in EventStruct.get_binary_fields()][:5] == [
        "event_id", "instructions_count", "instructions_local_offset",
        "event_arg_replacements_count", "event_arg_replacements_local_offset",
    ]
    assert [f.name for f in InstructionStruct.get_binary_fields()] == [
        "category", "index", "base_args_size", "base_args_local_offset", "event_layers_local_offset"
    ]
    assert [f.name for f in EventArgStruct.get_binary_fields()] == [
        "instruction_line", "write_offset", "read_offset", "size", "unknown"
    ]
    assert "event_layers_uint" in [f.name for f in EventLayersStruct.get_binary_fields()]


def test_on_rest_behavior_enum():
    assert OnRestBehavior.ContinueOnRest == 0
    assert OnRestBehavior.RestartOnRest == 1
    assert OnRestBehavior.EndOnRest == 2


# ---------------------------------------------------------------------------
# Binary round trips (need the committed test resource)
# ---------------------------------------------------------------------------


def test_emevd_unpack(ds1r_emevd: EMEVD):
    assert ds1r_emevd.map_name == "m10_00_00_00"
    assert 0 in ds1r_emevd.events and 50 in ds1r_emevd.events
    assert all(isinstance(e, Event) for e in ds1r_emevd.events.values())
    assert all(isinstance(i, Instruction) for e in ds1r_emevd.events.values() for i in e.instructions)
    assert ds1r_emevd.byte_order == ByteOrder.LittleEndian


def test_emevd_pack_is_deterministic(ds1r_emevd: EMEVD):
    assert bytes(ds1r_emevd.to_writer()) == bytes(ds1r_emevd.to_writer())


def test_emevd_binary_roundtrip_is_byte_identical(ds1r_emevd: EMEVD, tmp_path: Path):
    """unpack -> pack -> unpack -> pack must be byte-stable."""
    first = bytes(ds1r_emevd.to_writer())
    out = tmp_path / "m10_00_00_00.emevd.dcx"
    ds1r_emevd.write(out)
    reloaded = EMEVD.from_path(out)
    assert bytes(reloaded.to_writer()) == first
    assert list(reloaded.events) == list(ds1r_emevd.events)


def test_emevd_header_counts_match_content(ds1r_emevd: EMEVD):
    data = bytes(ds1r_emevd.to_writer())
    reader = BinaryReader(data)
    reader.byte_order = ByteOrder.LittleEndian
    reader.long_varints = EMEVD.LONG_VARINTS
    header = EMEVDHeaderStruct.from_bytes(reader)
    assert header.file_size == len(data)
    assert header.events_count == len(ds1r_emevd.events)
    assert header.instructions_count == sum(e.instruction_count for e in ds1r_emevd.events.values())
    assert header.event_arg_replacements_count == ds1r_emevd.event_arg_count
    assert header.base_arg_data_size % 16 == 0  # padded to 16


def test_define_label_instructions_have_no_base_arg_offset(ds1r_emevd: EMEVD):
    """Category 1014 ('DefineLabel') is special-cased to write a -1 base-arg offset."""
    data = bytes(ds1r_emevd.to_writer())
    reader = BinaryReader(data)
    reader.byte_order = ByteOrder.LittleEndian
    reader.long_varints = EMEVD.LONG_VARINTS
    header = EMEVDHeaderStruct.from_bytes(reader)
    reader.seek(header.instructions_offset)
    found_any = False
    for _ in range(header.instructions_count):
        instr = InstructionStruct.from_bytes(reader)
        reader.assert_pad(4)
        if instr.base_args_size == 0:
            found_any = True
            assert instr.base_args_local_offset == -1
        else:
            assert instr.base_args_local_offset >= 0
    if not found_any:
        pytest.skip("No zero-arg instructions in this EMEVD.")


def test_emevd_evs_roundtrip_is_byte_identical(ds1r_emevd: EMEVD, tmp_path: Path):
    """The flagship feature: EMEVD -> EVS -> EMEVD must reproduce the original bytes."""
    original = bytes(ds1r_emevd.to_writer())
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    evs_path.write_text(ds1r_emevd.to_evs(), encoding="utf-8")
    recompiled = EMEVD.from_evs_path(evs_path)
    assert bytes(recompiled.to_writer()) == original


def test_emevd_numeric_roundtrip_is_byte_identical(ds1r_emevd: EMEVD):
    original = bytes(ds1r_emevd.to_writer())
    numeric = ds1r_emevd.to_numeric()
    recompiled = EMEVD.from_numeric_string(numeric, map_name="m10_00_00_00")
    assert bytes(recompiled.to_writer()) == original


def test_emevd_numeric_path_roundtrip(ds1r_emevd: EMEVD, tmp_path: Path):
    numeric_path = tmp_path / "m10_00_00_00.numeric.txt"
    ds1r_emevd.write_numeric(numeric_path)
    recompiled = EMEVD.from_numeric_path(numeric_path, map_name="m10_00_00_00")
    assert bytes(recompiled.to_writer()) == bytes(ds1r_emevd.to_writer())


def test_evs_output_is_valid_python(ds1r_emevd: EMEVD):
    import ast
    ast.parse(ds1r_emevd.to_evs())


def test_from_reader_rejects_wrong_header_version(ds1r_emevd: EMEVD):
    """Header version info is asserted per game module (DS1 expects `(False, 0, 204)`)."""
    data = bytearray(bytes(ds1r_emevd.to_writer()))
    assert struct.unpack_from("<I", data, 8)[0] == EMEVD.HEADER_VERSION_INFO[2]
    struct.pack_into("<I", data, 8, 999)  # bogus version
    with pytest.raises(ValueError, match="not compatible with this `EMEVD` game module"):
        EMEVD.from_reader(BinaryReader(bytes(data)))


# ---------------------------------------------------------------------------
# 'numeric' text format (pure unit)
# ---------------------------------------------------------------------------


def test_numeric_minimal_script():
    emevd = EMEVD.from_numeric_string(
        "0, 0\n 2003[02] (iB)[11000001, 1]\n\nlinked:\n\nstrings:\n"
    )
    assert list(emevd.events) == [0]
    instr = emevd.events[0].instructions[0]
    assert (instr.category, instr.index) == (2003, 2)
    assert instr.args_list == [11000001, 1]


def test_numeric_event_arg_replacement_line():
    emevd = EMEVD.from_numeric_string(
        "11000100, 1\n 2003[02] (iB)[0, 1]\n    ^(0 <- 0, 4)\n\nlinked:\n\nstrings:\n"
    )
    repls = emevd.events[11000100].instructions[0].event_arg_replacements
    assert len(repls) == 1
    assert (repls[0].write_offset, repls[0].read_offset, repls[0].size) == (0, 0, 4)
    assert emevd.events[11000100].on_rest_behavior == OnRestBehavior.RestartOnRest


def test_numeric_rejects_arg_count_mismatch():
    with pytest.raises(NumericEmevdError, match="Number of args"):
        EMEVD.from_numeric_string("0, 0\n 2003[02] (iB)[11000001]\n\nlinked:\n\nstrings:\n")


def test_numeric_rejects_out_of_range_arg():
    with pytest.raises(NumericEmevdError, match="not inside the permitted range"):
        EMEVD.from_numeric_string("0, 0\n 2003[02] (iB)[11000001, 999]\n\nlinked:\n\nstrings:\n")


def test_numeric_rejects_orphan_arg_replacement():
    with pytest.raises(NumericEmevdError, match="does not follow an instruction"):
        EMEVD.from_numeric_string("0, 0\n    ^(0 <- 0, 4)\n\nlinked:\n\nstrings:\n")


def test_numeric_rejects_malformed_line():
    with pytest.raises(NumericEmevdError, match="cannot be parsed"):
        EMEVD.from_numeric_string("0, 0\n this is not an instruction\n\nlinked:\n\nstrings:\n")


def test_numeric_rejects_bad_header():
    with pytest.raises(NumericEmevdError, match="Error parsing header line"):
        EMEVD.from_numeric_string("not_an_event_header\n 2003[02] (iB)[1, 1]\n\nlinked:\n\nstrings:\n")


def test_numeric_converts_minus_one_for_unsigned():
    emevd = EMEVD.from_numeric_string("0, 0\n 2000[00] (iII)[0, -1, 0]\n\nlinked:\n\nstrings:\n")
    assert emevd.events[0].instructions[0].args_list[1] == 2 ** 32 - 1


def test_numeric_converts_uint_max_for_signed():
    emevd = EMEVD.from_numeric_string(
        f"0, 0\n 2004[06] (iiB)[{2 ** 32 - 1}, 0, 0]\n\nlinked:\n\nstrings:\n"
    )
    assert emevd.events[0].instructions[0].args_list[0] == -1


def test_numeric_linked_offsets_and_strings_parsed():
    emevd = EMEVD.from_numeric_string("0, 0\n 2003[02] (iB)[1, 1]\n\nlinked:\n0\n\nstrings:\n0: abc\n")
    assert emevd.linked_file_offsets == [0]
    assert emevd.packed_strings == "abc".encode("utf-8") + b"\0\0"


@pytest.mark.xfail(
    reason="BUG: `build_numeric` hard-codes UTF-16LE for packed strings, but `unpack_strings` uses "
           "the game's `STRING_ENCODING` (UTF-8 for DS1 PTDE/DSR). Numeric/EVS round trip corrupts "
           "linked file names for DS1.",
    strict=False,
)
def test_numeric_string_roundtrip_respects_game_encoding(ds1r_emevd: EMEVD):
    ds1r_emevd.packed_strings = "N:\\FRPG\\data\\Event\\common.emevd".encode(EMEVD.STRING_ENCODING) + b"\0"
    ds1r_emevd.linked_file_offsets = [0]
    recompiled = EMEVD.from_numeric_string(ds1r_emevd.to_numeric())
    assert recompiled.packed_strings == ds1r_emevd.packed_strings


@pytest.mark.xfail(
    reason="BUG: numeric `INSTRUCTION_RE` arg character class is `[\\d, .-]*`, which cannot match "
           "float reprs in scientific notation (e.g. '1e-05'), 'inf' or 'nan'.",
    strict=False,
)
def test_numeric_roundtrip_of_small_float_arg(ds1r_emevd: EMEVD):
    for event in ds1r_emevd.events.values():
        for instr in event.instructions:
            if "f" in instr.display_args_fmt:
                index = instr.struct_args_fmt.index("f")
                instr.args_list[index] = 1e-5
                break
        else:
            continue
        break
    else:
        pytest.skip("No float arguments in test EMEVD.")
    EMEVD.from_numeric_string(ds1r_emevd.to_numeric())


def test_numeric_event_layers_produce_event_layers_object():
    emevd = EMEVD.from_numeric_string("0, 0\n 2003[02] (iB)[1, 1] <0, 2>\n\nlinked:\n\nstrings:\n")
    instr = emevd.events[0].instructions[0]
    assert isinstance(instr.event_layers, EventLayers)
    bytes(emevd.to_writer())


def test_numeric_blank_chunk_does_not_truncate_script():
    numeric = (
        "\n\n"  # leading blank lines produce an empty leading chunk
        "0, 0\n 2003[02] (iB)[1, 1]\n"
        "\n\n"
        "11000100, 0\n 2003[02] (iB)[2, 1]\n"
        "\n\nlinked:\n\nstrings:\n"
    )
    emevd = EMEVD.from_numeric_string(numeric)
    assert set(emevd.events) == {0, 11000100}


# ---------------------------------------------------------------------------
# Event layers
# ---------------------------------------------------------------------------


def test_event_layers_survive_binary_roundtrip(ds1r_emevd: EMEVD, tmp_path: Path):
    events = list(ds1r_emevd.events.values())
    events[0].instructions[0].event_layers = EventLayers(0b101)
    events[1].instructions[0].event_layers = EventLayers(0b1010)
    out = tmp_path / "layers.emevd.dcx"
    ds1r_emevd.write(out)
    reloaded = EMEVD.from_path(out)
    reloaded_events = list(reloaded.events.values())
    assert reloaded_events[0].instructions[0].event_layers == EventLayers(0b101)
    assert reloaded_events[1].instructions[0].event_layers == EventLayers(0b1010)


# ---------------------------------------------------------------------------
# `EMEVD` public API
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "source, expected",
    [
        (Path("m10_00_00_00.emevd"), "emevd_path"),
        (Path("m10_00_00_00.emevd.dcx"), "emevd_path"),
        (Path("m10_00_00_00.evs.py"), "evs_path"),
        (Path("m10_00_00_00.py"), "evs_path"),
        (Path("m10_00_00_00.numeric.txt"), "numeric_path"),
        ("0, 0\n 2003[02] (iB)[1, 1]\n", "numeric_string"),
        (b"EVD\0", "emevd_bytes"),
    ],
)
def test_from_auto_detect_source_type(source, expected):
    assert EMEVD.from_auto_detect_source_type(source) == expected


def test_from_auto_detect_source_type_rejects_unknown():
    with pytest.raises(TypeError):
        EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.msb"))
    with pytest.raises(TypeError):
        EMEVD.from_auto_detect_source_type(12345)


def test_unpack_strings():
    emevd = EMEVD()
    emevd.packed_strings = "abc".encode("utf-8") + b"\0" + "de".encode("utf-8") + b"\0"
    assert emevd.unpack_strings() == [("0", "abc"), ("4", "de")]


def test_event_arg_count(ds1r_emevd: EMEVD):
    assert ds1r_emevd.event_arg_count == sum(
        len(i.event_arg_replacements) for e in ds1r_emevd.events.values() for i in e.instructions
    )


def test_regenerate_signatures_is_idempotent(ds1r_emevd: EMEVD):
    ds1r_emevd.regenerate_signatures()
    first = {i: sig.get_full_fmt() for i, sig in ds1r_emevd.event_signatures.items()}
    ds1r_emevd.regenerate_signatures()
    second = {i: sig.get_full_fmt() for i, sig in ds1r_emevd.event_signatures.items()}
    assert first == second


def test_get_evs_docstring_contains_linked_and_strings():
    emevd = EMEVD()
    emevd.linked_file_offsets = [0, 4]
    emevd.packed_strings = "abc".encode("utf-8") + b"\0"
    docstring = emevd.get_evs_docstring("My Map")
    assert docstring.startswith('"""')
    assert "My Map" in docstring
    assert "linked:\n0\n4" in docstring
    assert "0: abc" in docstring


def test_merge_combines_constructors():
    a = _simple_emevd('@ContinueOnRest(0)\ndef Constructor():\n    """Event 0"""\n    EnableFlag(1)\n')
    b = _simple_emevd('@ContinueOnRest(0)\ndef Constructor():\n    """Event 0"""\n    EnableFlag(2)\n')
    merged = a.merge(b)
    assert len(merged.events[0].instructions) == 2
    assert len(a.events[0].instructions) == 1  # source not mutated


def test_merge_rejects_duplicate_non_merge_event():
    body = '@ContinueOnRest(100)\ndef Event_100():\n    """Event 100"""\n    EnableFlag(1)\n'
    a = _simple_emevd(body)
    b = _simple_emevd(body)
    with pytest.raises(ValueError, match="appears in both EMEVD sources"):
        a.merge(b)


@pytest.mark.xfail(
    reason="BUG: `EMEVD.merge(event_id_offset=N)` only offsets the `events` dict key; the "
           "`Event.event_id` field (which is what gets packed) is left unchanged, producing "
           "duplicate event IDs in the output EMEVD.",
    strict=False,
)
def test_merge_event_id_offset_updates_event_id():
    a = _simple_emevd('@ContinueOnRest(0)\ndef Constructor():\n    """Event 0"""\n    EnableFlag(1)\n')
    b = _simple_emevd('@ContinueOnRest(100)\ndef Event_100():\n    """Event 100"""\n    EnableFlag(2)\n')
    merged = a.merge(b, merge_events=(), event_id_offset=1000)
    assert set(merged.events) == {0, 1100}
    assert {key: event.event_id for key, event in merged.events.items()} == {0: 0, 1100: 1100}


@pytest.mark.xfail(
    reason="BUG: `EMEVD.merge` inserts the OTHER EMEVD's `Event`/`Instruction` objects by "
           "reference, so mutating the merged result corrupts the source EMEVD.",
    strict=False,
)
def test_merge_does_not_share_event_objects():
    a = _simple_emevd('@ContinueOnRest(0)\ndef Constructor():\n    """Event 0"""\n    EnableFlag(1)\n')
    b = _simple_emevd('@ContinueOnRest(100)\ndef Event_100():\n    """Event 100"""\n    EnableFlag(2)\n')
    merged = a.merge(b, merge_events=())
    assert merged.events[100] is not b.events[100]
    assert merged.events[100].instructions[0] is not b.events[100].instructions[0]


# ---------------------------------------------------------------------------
# `Event` / `Instruction` numeric text emission
# ---------------------------------------------------------------------------


def test_instruction_to_numeric_format():
    instr = Instruction(2003, 2, "iB", args_list=[11000001, 1])
    assert instr.to_numeric() == [" 2003[02] (iB)[11000001, 1]"]


def test_instruction_to_numeric_with_event_layers_and_replacements():
    instr = Instruction(2003, 2, "iB", args_list=[0, 1], event_layers=EventLayers(0b101))
    instr.event_arg_replacements.append(
        __import__("soulstruct.base.events.emevd.instruction", fromlist=["EventArgRepl"]).EventArgRepl(0, 0, 0, 4)
    )
    lines = instr.to_numeric()
    assert lines[0].endswith(" <0, 2>")
    assert lines[1] == "    ^(0 <- 0, 4)"


def test_event_to_numeric_header():
    event = Event(11000100, OnRestBehavior.EndOnRest, [Instruction(2003, 2, "iB", args_list=[1, 1])])
    assert event.to_numeric().splitlines()[0] == "11000100, 2"


def test_instruction_uses_custom_base_repr():
    instr = Instruction(2003, 2, "iB", args_list=[1, 1], event_layers=EventLayers(3))
    text = repr(instr)
    assert text.startswith("Instruction(2003, 2, ")
    assert "event_layers=" in text


def test_packed_base_args_match_declared_size():
    """`base_args_size` written into the instruction header must equal the packed byte length."""
    for fmt, args in [("iB", [1, 1]), ("iiB", [1, 2, 3]), ("iII", [0, 1, 2]), ("bhi", [1, 2, 3])]:
        instr = Instruction(2003, 2, fmt, args_list=args)
        assert instr.base_args_size == len(struct.pack(f"@{fmt}0i", *args))
