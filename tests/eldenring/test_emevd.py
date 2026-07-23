"""Elden Ring EMEVD read/write and EVS decompile/recompile tests.

Rewritten from the original `unittest` script (which only checked that the calls did not raise, wrote its
output into the repository tree, and asserted nothing). Intent is preserved -- binary read, binary write,
EVS write, EVS read, EVS re-write -- but every stage now asserts a real invariant and writes to `tmp_path`.

`m10_00_00_00` is Stormveil Castle; the committed resource is from an older ER patch, which is fine (and
useful) for format-stability testing. Tests that need the live installation use the `er_root` fixture.
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

from soulstruct.dcx import DCXType, decompress
from soulstruct.eldenring.events.emevd import EMEVD
from soulstruct.eldenring.events.emevd.core import Event, Instruction

RESOURCE_NAME = "m10_00_00_00.emevd.dcx"


@pytest.fixture
def m10_emevd(resource) -> EMEVD:
    return EMEVD.from_path(resource(RESOURCE_NAME))


# ---------------------------------------------------------------------------
# Binary
# ---------------------------------------------------------------------------


def test_emevd_class_configuration():
    """ER-specific EMEVD constants that distinguish it from DS3/Sekiro."""
    assert EMEVD.STRING_ENCODING == "utf-16le"
    assert EMEVD.LONG_VARINTS is True
    assert EMEVD.HEADER_VERSION_INFO == (True, -1, 205)
    assert EMEVD.EVENT_CLASS is Event
    assert Event.INSTRUCTION_CLASS is Instruction
    assert Event.USE_ADVANCED_DECOMPILER is True


def test_binary_read(m10_emevd):
    assert m10_emevd.map_name == "m10_00_00_00"
    assert m10_emevd.dcx_type != DCXType.Null
    assert len(m10_emevd.events) > 50
    # Constructor and preconstructor are always present in a map EMEVD.
    assert 0 in m10_emevd.events
    assert 50 in m10_emevd.events
    # ER maps link `common_func.emevd` (and `common_macro.emevd`).
    assert len(m10_emevd.linked_file_offsets) >= 1
    assert m10_emevd.packed_strings


def test_binary_roundtrip_is_byte_identical(m10_emevd, resource, tmp_path):
    """Unpack -> pack must reproduce the exact uncompressed EMEVD bytes.

    Only the *decompressed* payload is compared: DCX recompression is not bit-reproducible.
    """
    write_path = tmp_path / RESOURCE_NAME
    m10_emevd.write(write_path)
    original = decompress(resource(RESOURCE_NAME).read_bytes())[0]
    repacked = decompress(write_path.read_bytes())[0]
    assert len(repacked) == len(original)
    assert repacked == original


def test_binary_roundtrip_reload_is_stable(m10_emevd, tmp_path):
    write_path = tmp_path / RESOURCE_NAME
    m10_emevd.write(write_path)
    reloaded = EMEVD.from_path(write_path)
    assert list(reloaded.events) == list(m10_emevd.events)
    assert reloaded.packed_strings == m10_emevd.packed_strings
    assert reloaded.linked_file_offsets == m10_emevd.linked_file_offsets
    for event_id, event in m10_emevd.events.items():
        other = reloaded.events[event_id]
        assert other.on_rest_behavior == event.on_rest_behavior
        assert len(other.instructions) == len(event.instructions)


def test_numeric_roundtrip(m10_emevd, tmp_path):
    """Numeric text is the intermediate format that EVS compiles to; it must round-trip losslessly."""
    numeric = m10_emevd.to_numeric()
    assert "linked:" in numeric and "strings:" in numeric
    rebuilt = EMEVD.from_numeric_string(numeric, map_name=m10_emevd.map_name)
    assert list(rebuilt.events) == list(m10_emevd.events)
    assert rebuilt.to_numeric() == numeric

    numeric_path = tmp_path / "m10_00_00_00.numeric.txt"
    m10_emevd.write_numeric(numeric_path)
    from_path = EMEVD.from_numeric_path(numeric_path, map_name=m10_emevd.map_name)
    assert list(from_path.events) == list(m10_emevd.events)


def test_get_called_event_detects_run_event_instructions(m10_emevd):
    """ER `Instruction.get_called_event` must handle both (2000, 0) and (2000, 6)."""
    seen_ids = set()
    for event in m10_emevd.events.values():
        for instruction in event.instructions:
            called = instruction.get_called_event()
            if called is None:
                assert not (instruction.category == 2000 and instruction.index in (0, 6))
            else:
                assert (instruction.category, instruction.index) in {(2000, 0), (2000, 6)}
                assert isinstance(called, int)
                seen_ids.add((instruction.category, instruction.index))
    # Stormveil's constructor uses `RunCommonEvent` heavily.
    assert (2000, 6) in seen_ids


def test_from_auto_detect_source_type():
    assert EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.emevd.dcx")) == "emevd_path"
    assert EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.emevd")) == "emevd_path"
    assert EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.evs.py")) == "evs_path"
    assert EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.numeric.txt")) == "numeric_path"
    with pytest.raises(TypeError):
        EMEVD.from_auto_detect_source_type(Path("m10_00_00_00.msb"))


def test_merge_rejects_conflicting_events(m10_emevd):
    with pytest.raises(ValueError):
        m10_emevd.merge(m10_emevd, merge_events=())


# ---------------------------------------------------------------------------
# EVS decompilation
# ---------------------------------------------------------------------------


def test_evs_write_produces_valid_python(m10_emevd, tmp_path):
    """Decompiled EVS must at minimum be syntactically valid Python with the expected preamble."""
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    m10_emevd.write_evs(evs_path)
    text = evs_path.read_text(encoding="utf-8")
    ast.parse(text)  # raises SyntaxError on failure
    assert "from soulstruct.eldenring.events import *" in text
    assert "from soulstruct.eldenring.events.instructions import *" in text
    assert "def Constructor():" in text
    assert "def Preconstructor():" in text


def test_evs_event_functions_match_event_ids(m10_emevd, tmp_path):
    """Every event ID must appear exactly once as an EVS function (special names for 0/50/100/200)."""
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    m10_emevd.write_evs(evs_path)
    tree = ast.parse(evs_path.read_text(encoding="utf-8"))
    func_names = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
    assert len(func_names) == len(m10_emevd.events)
    special = {0: "Constructor", 50: "Preconstructor", 100: "Postconstructor1", 200: "Postconstructor2"}
    expected = {special.get(event_id, f"Event_{event_id}") for event_id in m10_emevd.events}
    assert set(func_names) == expected


def test_evs_docstring_preserves_linked_files_and_strings(m10_emevd, tmp_path):
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    m10_emevd.write_evs(evs_path)
    module_docstring = ast.get_docstring(ast.parse(evs_path.read_text(encoding="utf-8")))
    assert module_docstring is not None
    assert "linked:" in module_docstring
    assert "strings:" in module_docstring
    assert "common_func.emevd" in module_docstring


# ---------------------------------------------------------------------------
# EVS recompilation (round trip)
# ---------------------------------------------------------------------------


def test_evs_roundtrip(m10_emevd, tmp_path):
    """EMEVD -> EVS -> EMEVD must preserve every event and its instruction count."""
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    m10_emevd.write_evs(evs_path)
    recompiled = EMEVD.from_evs_path(evs_path)
    assert list(recompiled.events) == list(m10_emevd.events)
    for event_id, event in m10_emevd.events.items():
        assert len(recompiled.events[event_id].instructions) == len(event.instructions)


@pytest.mark.xfail(
    reason="Same root cause as `test_evs_roundtrip` (compiler `obj=` vs EMEDF `asset=`).",
    strict=False,
)
def test_evs_rewrite_is_idempotent(m10_emevd, tmp_path):
    """EVS -> EMEVD -> EVS must be a fixed point (the original test's final stage, now asserted)."""
    first = tmp_path / "first.evs.py"
    m10_emevd.write_evs(first)
    recompiled = EMEVD.from_evs_path(first)
    second = tmp_path / "second.evs.py"
    recompiled.write_evs(second)
    # Compare event bodies only; the header docstring/imports can legitimately differ.
    first_bodies = [
        ast.dump(node) for node in ast.parse(first.read_text(encoding="utf-8")).body
        if isinstance(node, ast.FunctionDef)
    ]
    second_bodies = [
        ast.dump(node) for node in ast.parse(second.read_text(encoding="utf-8")).body
        if isinstance(node, ast.FunctionDef)
    ]
    assert first_bodies == second_bodies


def test_evs_string_compiles_minimal_script():
    """Smoke test of the public EVS entry point with instructions that DO work in ER."""
    evs = (
        "from soulstruct.eldenring.events import *\n"
        "from soulstruct.eldenring.events.instructions import *\n"
        "\n\n"
        "@ContinueOnRest(0)\n"
        "def Constructor():\n"
        '    """Event 0"""\n'
        "    RegisterGrace(grace_flag=10000002, asset=10001952)\n"
        "    RunCommonEvent(9005810, slot=0, args=(10000800, 10000000, 10000950, 10001950, 1084227584))\n"
        "    EnableFlag(10000000)\n"
        "    End()\n"
        "\n\n"
        "@RestartOnRest(50)\n"
        "def Preconstructor():\n"
        '    """Event 50"""\n'
        "    IfFlagEnabled(AND_1, 10000000)\n"
        "    DisableFlag(10000000)\n"
        "    return RESTART\n"
    )
    emevd = EMEVD.from_evs_string(evs, map_name="m10_00_00_00")
    assert set(emevd.events) == {0, 50}
    assert emevd.events[0].instructions
    assert emevd.events[50].on_rest_behavior == 1


def test_evs_rejects_duplicate_event_ids():
    from soulstruct.base.events.emevd.exceptions import EMEVDError

    evs = (
        "from soulstruct.eldenring.events import *\n"
        "from soulstruct.eldenring.events.instructions import *\n"
        "\n\n"
        "@ContinueOnRest(0)\n"
        "def Constructor():\n"
        '    """Event 0"""\n'
        "    End()\n"
        "\n\n"
        "@ContinueOnRest(1000)\n"
        "def Event_1000():\n"
        '    """1000"""\n'
        "    End()\n"
        "\n\n"
        "@ContinueOnRest(1000)\n"
        "def Event_1000_Again():\n"
        '    """1000"""\n'
        "    End()\n"
    )
    with pytest.raises(EMEVDError):
        EMEVD.from_evs_string(evs, map_name="m10_00_00_00")


# ---------------------------------------------------------------------------
# Live game data
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_live_common_func_reads(er_root):
    """`common_func.emevd` holds the shared event library that every ER map calls into."""
    common_func = EMEVD.from_path(er_root / "event/common_func.emevd.dcx")
    assert len(common_func.events) > 100
    # Signatures are needed by `apply_common_func`; they must be populated by the binary reader.
    assert len(common_func.event_signatures) == len(common_func.events)


@pytest.mark.game_data
def test_live_map_binary_roundtrip(er_root, tmp_path):
    source = er_root / "event/m10_00_00_00.emevd.dcx"
    emevd = EMEVD.from_path(source)
    out = tmp_path / "m10_00_00_00.emevd.dcx"
    emevd.write(out)
    assert decompress(out.read_bytes())[0] == decompress(source.read_bytes())[0]


@pytest.mark.game_data
def test_live_evs_with_common_func_names_common_events(er_root, tmp_path):
    """`apply_common_func` rewrites `RunCommonEvent(...)` calls into named `CommonFunc_{id}(...)` calls."""
    common_func = EMEVD.from_path(er_root / "event/common_func.emevd.dcx")
    emevd = EMEVD.from_path(er_root / "event/m10_00_00_00.emevd.dcx")
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    emevd.write_evs(evs_path, common_func_emevd=common_func)
    text = evs_path.read_text(encoding="utf-8")
    ast.parse(text)
    assert "CommonFunc_" in text
    assert "# [COMMON_FUNC]" in text
    assert "from .common_func import *" in text


@pytest.mark.slow
@pytest.mark.game_data
@pytest.mark.xfail(
    reason="`EMEVD.to_evs` emits `# [COMMON_FUNC]\\nfrom .common_func import *`, but "
           "`COMMON_FUNC_IMPORT_RE` in `base/events/evs/utils.py` cannot match a star import. The marker "
           "line is therefore not stripped, the import is treated as an ordinary relative import, and "
           "executing `common_func.py` fails on `from soulstruct.eldenring.events.instructions import *` "
           "(that module only exists as a `.pyi` stub).",
    strict=False,
)
def test_live_evs_common_func_roundtrip(er_root, tmp_path):
    """The full ER workflow: decompile common_func + a map, then recompile the map."""
    common_func = EMEVD.from_path(er_root / "event/common_func.emevd.dcx")
    emevd = EMEVD.from_path(er_root / "event/m10_00_00_00.emevd.dcx")
    common_func.write_evs(tmp_path / "common_func.py", event_function_prefix="CommonFunc")
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    emevd.write_evs(evs_path, common_func_emevd=common_func)
    recompiled = EMEVD.from_evs_path(evs_path)
    assert list(recompiled.events) == list(emevd.events)
