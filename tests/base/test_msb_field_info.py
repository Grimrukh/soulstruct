"""Tests for `soulstruct.base.maps.msb.field_info` -- the shared GUI display metadata for MSB
entry fields -- and for `MSBEntry.get_field_display_info()`, which consumes it.

`FIELD_INFO` is a hand-maintained dict keyed by `"<Subtype>[<field_name>]"` with a
`"<SUPERTYPE>[<field_name>]"` fallback, so it drifts out of sync with the dataclass fields very
easily. These tests pin the current state of that sync.
"""
from __future__ import annotations

import ast
import importlib
import re
from pathlib import Path

import pytest

import soulstruct.base.maps.msb.field_info as field_info_module
from soulstruct.base.maps.msb.enums import MSBSupertype
from soulstruct.base.maps.msb.field_info import FIELD_INFO, MapFieldInfo, MapFieldMetadata
from soulstruct.base.maps.msb.msb_entry import MSBFieldDisplayInfo
from soulstruct.base.maps.msb.utils import BitSet128


KEY_RE = re.compile(r"^(?P<type>[A-Za-z0-9]+)\[(?P<field>[A-Za-z0-9_]+)\]$")

# Games whose `maps.msb` module exists in this repo.
_CANDIDATE_GAMES = ("demonssouls", "darksouls1ptde", "darksouls1r", "bloodborne", "eldenring")


def _game_msb(submodule: str):
    try:
        return importlib.import_module(f"soulstruct.{submodule}.maps.msb").MSB
    except ImportError:
        pytest.skip(f"`soulstruct.{submodule}.maps.msb` not available.")


def _registered_entry_classes(msb_class):
    for subtypes in msb_class.MSB_ENTRY_SUBTYPES.values():
        for info in subtypes.values():
            yield info.entry_class


# ---------------------------------------------------------------------------
# FIELD_INFO structure
# ---------------------------------------------------------------------------


def test_field_info_keys_are_well_formed():
    bad = [key for key in FIELD_INFO if not KEY_RE.match(key)]
    assert not bad, f"Malformed `FIELD_INFO` keys: {bad}"


def test_field_info_values_are_nickname_tooltip_pairs():
    bad = [
        key for key, value in FIELD_INFO.items()
        if not (isinstance(value, tuple) and len(value) == 2 and all(isinstance(s, str) and s for s in value))
    ]
    assert not bad, f"`FIELD_INFO` values must be (nickname, tooltip) string pairs: {bad}"


def test_field_info_source_has_no_duplicate_keys():
    """A duplicate key in the dict literal would be silently swallowed by Python."""
    source = Path(field_info_module.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    literal_keys = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "FIELD_INFO":
            literal_keys = [k.value for k in node.value.keys if isinstance(k, ast.Constant)]
            break
    assert literal_keys, "Could not locate the `FIELD_INFO` dict literal."
    duplicates = {k for k in literal_keys if literal_keys.count(k) > 1}
    assert not duplicates, f"Duplicate `FIELD_INFO` keys silently overwritten: {sorted(duplicates)}"
    assert len(literal_keys) == len(FIELD_INFO)


def test_field_info_key_prefixes_are_known_supertypes_or_subtypes():
    """Lookup keys are `f"{SUBTYPE_ENUM.name minus 'Unused'}[field]"` with a
    `f"{SUPERTYPE_ENUM.name}[field]"` fallback, so any other prefix is dead weight."""
    valid = {member.name for member in MSBSupertype}
    for submodule in _CANDIDATE_GAMES:
        try:
            msb_class = importlib.import_module(f"soulstruct.{submodule}.maps.msb").MSB
        except ImportError:
            continue
        for entry_class in _registered_entry_classes(msb_class):
            valid.add(entry_class.SUBTYPE_ENUM.name.replace("Unused", ""))
    bad = [key for key in FIELD_INFO if KEY_RE.match(key).group("type") not in valid]
    assert not bad, f"`FIELD_INFO` keys with unknown supertype/subtype prefix: {bad}"


# ---------------------------------------------------------------------------
# FIELD_INFO <-> real entry fields sync
# ---------------------------------------------------------------------------


def _all_lookup_keys() -> set[str]:
    """Every key that any registered entry class in any available game would look up."""
    keys = set()
    for submodule in _CANDIDATE_GAMES:
        try:
            msb_class = importlib.import_module(f"soulstruct.{submodule}.maps.msb").MSB
        except ImportError:
            continue
        for entry_class in _registered_entry_classes(msb_class):
            subtype_name = entry_class.SUBTYPE_ENUM.name.replace("Unused", "")
            supertype_name = entry_class.SUPERTYPE_ENUM.name
            for f in entry_class.get_entry_fields():
                if f.name.startswith("_"):
                    continue
                keys.add(f"{subtype_name}[{f.name}]")
                keys.add(f"{supertype_name}[{f.name}]")
    return keys


# Keys present in `FIELD_INFO` that no registered entry class can ever look up.
KNOWN_STALE_FIELD_INFO_KEYS = {
    "NPCInvasion[base_region_name]",
    "NPCInvasion[spawn_point_region_name]",
    "Wind[unk_x04_x08]",
    "Wind[unk_x0c_x10]",
}


def test_field_info_has_no_new_stale_keys():
    unused = set(FIELD_INFO) - _all_lookup_keys()
    assert unused <= KNOWN_STALE_FIELD_INFO_KEYS, (
        f"New stale `FIELD_INFO` keys (no entry field uses them): "
        f"{sorted(unused - KNOWN_STALE_FIELD_INFO_KEYS)}"
    )


# DS1 fields with no `FIELD_INFO` entry and no `MapFieldInfo` metadata (fall back to 'TODO-TOOLTIP').
DS1_KNOWN_MISSING_DISPLAY_INFO = {
    "MSBWindEvent.unk_x0c",
    "MSBWindEvent.unk_x1c",
    "MSBNPCInvasionEvent.activate_good_id",
}


def test_ds1_ptde_display_info_is_in_sync():
    import soulstruct.darksouls1ptde.game_types as game_types

    msb_class = _game_msb("darksouls1ptde")
    missing = set()
    for entry_class in _registered_entry_classes(msb_class):
        for field_name in entry_class.get_field_names():
            display_info = entry_class.get_field_display_info(field_name, game_types)
            assert isinstance(display_info, MSBFieldDisplayInfo)
            assert display_info.nickname
            assert display_info.display_type is not None
            if display_info.tooltip == "TODO-TOOLTIP":
                missing.add(f"{entry_class.__name__}.{field_name}")
    assert missing == DS1_KNOWN_MISSING_DISPLAY_INFO, (
        f"`FIELD_INFO` drift for DS1 PTDE. Newly missing: {sorted(missing - DS1_KNOWN_MISSING_DISPLAY_INFO)}; "
        f"newly documented: {sorted(DS1_KNOWN_MISSING_DISPLAY_INFO - missing)}"
    )


def test_display_info_resolves_reference_field_game_types():
    import soulstruct.darksouls1ptde.game_types as game_types

    msb_class = _game_msb("darksouls1ptde")
    character_class = msb_class.MSB_ENTRY_SUBTYPES["PARTS_PARAM_ST"][
        next(e for e in msb_class.MSB_ENTRY_SUBTYPES["PARTS_PARAM_ST"] if e.name == "Character")
    ].entry_class
    model_info = character_class.get_field_display_info("model", game_types)
    assert model_info.display_type is game_types.CharacterModel
    assert character_class.get_field_display_info("entity_id", game_types).display_type is int
    assert character_class.get_field_display_info("draw_groups", game_types).display_type is BitSet128


def test_display_info_raises_key_error_for_unknown_field():
    import soulstruct.darksouls1ptde.game_types as game_types

    msb_class = _game_msb("darksouls1ptde")
    entry_class = next(iter(_registered_entry_classes(msb_class)))
    with pytest.raises(KeyError):
        entry_class.get_field_display_info("definitely_not_a_field", game_types)


@pytest.mark.xfail(
    reason=(
        "Elden Ring adds ~900 MSB entry fields (mostly `asset_unk*`/`unk_*`) with neither "
        "`MapFieldInfo` metadata nor a `FIELD_INFO` entry, so the GUI falls back to "
        "'TODO-TOOLTIP' for most of them."
    ),
    strict=False,
)
def test_elden_ring_display_info_is_in_sync():
    import soulstruct.eldenring.game_types as game_types

    msb_class = _game_msb("eldenring")
    missing = []
    for entry_class in _registered_entry_classes(msb_class):
        for field_name in entry_class.get_field_names():
            if entry_class.get_field_display_info(field_name, game_types).tooltip == "TODO-TOOLTIP":
                missing.append(f"{entry_class.__name__}.{field_name}")
    assert not missing, f"{len(missing)} Elden Ring fields lack display metadata."


@pytest.mark.xfail(
    reason=(
        "`BaseMSBPart` annotates `draw_groups`/`display_groups` with the generic parameter "
        "`BIT_SET_T`. `MSBEntry.get_field_types()` only understands literal annotation strings, so "
        "any game class that does not re-annotate them (all 10 Bloodborne Part classes) raises "
        "`TypeError: Invalid field type annotation 'BIT_SET_T'` -- which also breaks "
        "`__setattr__` validation entirely for those classes."
    ),
    strict=False,
)
def test_all_registered_part_classes_resolve_field_types():
    broken = []
    for submodule in _CANDIDATE_GAMES:
        try:
            msb_class = importlib.import_module(f"soulstruct.{submodule}.maps.msb").MSB
        except ImportError:
            continue
        for entry_class in _registered_entry_classes(msb_class):
            try:
                entry_class.get_field_types()
            except TypeError as ex:
                broken.append(f"{submodule}.{entry_class.__name__}: {ex}")
    assert not broken, "\n".join(broken)


# ---------------------------------------------------------------------------
# MapFieldInfo / MapFieldMetadata
# ---------------------------------------------------------------------------


def test_map_field_info_builds_dataclass_metadata():
    metadata = MapFieldInfo("Nickname", "Tooltip", int)
    assert set(metadata) == {"metadata"}
    msb_metadata = metadata["metadata"]["msb"]
    assert isinstance(msb_metadata, MapFieldMetadata)
    assert (msb_metadata.nickname, msb_metadata.tooltip, msb_metadata.game_type) == ("Nickname", "Tooltip", int)


def test_map_field_metadata_defaults_are_empty():
    metadata = MapFieldMetadata()
    assert metadata.nickname == "" and metadata.tooltip == "" and metadata.game_type is None


def test_map_field_metadata_is_mutable():
    """`MSBEntry.get_field_display_info` relies on being able to read (not write) this, but the
    docstring explicitly requires mutability."""
    metadata = MapFieldMetadata()
    metadata.nickname = "X"
    assert metadata.nickname == "X"


def test_entry_metadata_overrides_field_info_defaults():
    """A `MapFieldInfo` nickname on the dataclass field must win over the `FIELD_INFO` default."""
    import soulstruct.darksouls1ptde.game_types as game_types

    msb_class = _game_msb("darksouls1ptde")
    for entry_class in _registered_entry_classes(msb_class):
        for f in entry_class.get_entry_fields():
            metadata = f.metadata.get("msb", None)
            if metadata is None or not metadata.nickname:
                continue
            display_info = entry_class.get_field_display_info(f.name, game_types)
            assert display_info.nickname == metadata.nickname
            return  # one confirmed example is enough
    pytest.skip("No DS1 MSB field defines an explicit `MapFieldInfo` nickname.")


@pytest.mark.xfail(
    reason=(
        "`_FIELD_DISPLAY_INFO` is cached via ordinary attribute lookup, so a subclass "
        "(e.g. `MSBDummyCharacter(MSBCharacter)`) inherits its parent's cached display info -- "
        "including the parent's subtype-specific nicknames -- if the parent is queried first. "
        "This makes display info order-dependent."
    ),
    strict=False,
)
def test_subclass_does_not_inherit_parent_display_info_cache():
    import soulstruct.darksouls1ptde.game_types as game_types
    from soulstruct.darksouls1ptde.maps.parts import MSBCharacter, MSBDummyCharacter

    assert issubclass(MSBDummyCharacter, MSBCharacter)
    MSBCharacter.get_field_display_info("entity_id", game_types)
    assert "_FIELD_DISPLAY_INFO" in MSBDummyCharacter.__dict__ or (
        MSBDummyCharacter.__dict__.get("_FIELD_DISPLAY_INFO") is not None
    )
