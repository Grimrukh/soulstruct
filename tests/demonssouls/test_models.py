"""Demon's Souls model/Binder support.

DeS binders are all `BinderVersion.V3` (no `v4_info`) and DCX-compressed with the PS3-era
`DCX_EDGE` type. The only bundled resource for DeS is its MTDBND.
"""
from __future__ import annotations

import dataclasses

import pytest

from soulstruct.containers import BinderVersion
from soulstruct.dcx import DCXType
from soulstruct.demonssouls.models import CHRBND, MatDef, OBJBND, PARTSBND
from soulstruct.games import DEMONS_SOULS


BINDERS = [CHRBND, OBJBND, PARTSBND]


def test_des_default_dcx_type_is_edge():
    assert DEMONS_SOULS.default_dcx_type == DCXType.DCX_EDGE
    # These file types are NOT compressed in DeS.
    for suffix in (".hkx", ".msb", ".nvmbnd"):
        assert DEMONS_SOULS.get_dcx_type(suffix) == DCXType.Null


def test_process_dcx_path_respects_special_types():
    from pathlib import Path

    assert DEMONS_SOULS.process_dcx_path(Path("chr/c1000.chrbnd")) == Path("chr/c1000.chrbnd.dcx")
    assert DEMONS_SOULS.process_dcx_path(Path("map/mapstudio/m01_00_00_00.msb")) == Path(
        "map/mapstudio/m01_00_00_00.msb"
    )
    # Idempotent: an existing '.dcx' suffix is stripped before re-deciding.
    assert DEMONS_SOULS.process_dcx_path(Path("chr/c1000.chrbnd.dcx")) == Path("chr/c1000.chrbnd.dcx")


def test_process_dcx_path_str_overload_rewrites_separators():
    """NOTE: the `str` overload round-trips through `Path`, so on Windows it also flips '/' to '\'."""
    result = DEMONS_SOULS.process_dcx_path("chr/c1000.chrbnd")
    assert isinstance(result, str)
    assert result.replace("\\", "/") == "chr/c1000.chrbnd.dcx"


@pytest.mark.parametrize("binder_cls", BINDERS, ids=lambda c: c.__name__)
def test_binders_instantiate_with_des_defaults(binder_cls):
    binder = binder_cls()
    assert binder.version == BinderVersion.V3
    assert binder.dcx_type == DEMONS_SOULS.default_dcx_type
    assert binder_cls.DEFAULT_ENTRY_ROOT.startswith(DEMONS_SOULS.interroot_prefix)


@pytest.mark.parametrize("binder_cls", BINDERS, ids=lambda c: c.__name__)
def test_binder_v4_info_class_attribute_is_not_a_field_override(binder_cls):
    """`v4_info = None` in DeS binder modules is written WITHOUT a type annotation.

    In a dataclass, an un-annotated assignment is not a field override, so `v4_info` keeps the
    inherited V4 default even though these binders are V3. Harmless today (V3 binders ignore
    `v4_info` when packing) but it is a latent inconsistency: `CHRBND().v4_info` is a
    `BinderVersion4Info`, not `None` as the source suggests.
    """
    field = {f.name: f for f in dataclasses.fields(binder_cls)}["v4_info"]
    instance = binder_cls()
    if instance.v4_info is not None:
        pytest.xfail(
            f"{binder_cls.__name__}.v4_info is {instance.v4_info!r}, not `None`: the un-annotated "
            f"`v4_info = None` in demonssouls/models/{binder_cls.__name__.lower()}.py is not a "
            f"dataclass field override (field default_factory={field.default_factory})."
        )


def test_chrbnd_entry_root():
    assert CHRBND.DEFAULT_ENTRY_ROOT.endswith("\\chr")
    assert OBJBND.DEFAULT_ENTRY_ROOT.endswith("\\obj")
    assert PARTSBND.DEFAULT_ENTRY_ROOT.endswith("\\parts")


def test_objbnd_supports_multiple_flvers():
    assert OBJBND.MAX_FLVER_COUNT == 99


def test_mtdbnd_bundled_resource_exists():
    path = DEMONS_SOULS.bundled_resource_paths["MTDBND"]
    assert path.is_file(), path
    assert path.name.endswith(".mtdbnd.dcx")


@pytest.mark.slow
def test_bundled_mtdbnd_loads():
    from soulstruct.base.models.mtd import MTDBND

    mtdbnd = MTDBND.from_bundled(DEMONS_SOULS)
    # `MTDBND.mtds` is populated lazily; `entries` are the raw Binder entries.
    assert mtdbnd.entries, "Bundled DeS MTDBND contained no entries."
    mtdbnd.load_all_mtds()
    assert mtdbnd.mtds, "Bundled DeS MTDBND contained no MTDs."


def test_matdef_is_a_dataclass_with_uv_layers():
    assert dataclasses.is_dataclass(MatDef)
    assert hasattr(MatDef, "UVLayer")
    assert hasattr(MatDef, "SAMPLER_ALIASES")


def test_matdef_sampler_aliases_are_unique():
    aliases = list(MatDef.SAMPLER_ALIASES.values())
    assert len(aliases) == len(set(aliases)), f"Duplicate DeS sampler aliases: {aliases}"


def test_character_models_constant_is_sane():
    from soulstruct.demonssouls.constants import CHARACTER_MODELS

    assert CHARACTER_MODELS[0] == "Player"
    assert all(isinstance(k, int) for k in CHARACTER_MODELS)
    assert all(isinstance(v, str) and v for v in CHARACTER_MODELS.values())
    # Model IDs are used to build 'cXXXX' stems, so they must fit four digits.
    assert all(0 <= k <= 9999 for k in CHARACTER_MODELS)


def test_character_model_names_are_unique_except_known_duplicates():
    from soulstruct.demonssouls.constants import CHARACTER_MODELS

    names = list(CHARACTER_MODELS.values())
    duplicates = sorted({n for n in names if names.count(n) > 1})
    # 'Mind Flayer' legitimately appears at 3160/4030/5050 in DeS.
    assert duplicates == ["Mind Flayer"], duplicates


def test_nvmbnd_overrides_are_effective():
    from soulstruct.demonssouls.maps.navmesh import NVMBND

    nvmbnd = NVMBND()
    assert nvmbnd.version == BinderVersion.V3
    assert nvmbnd.v4_info is None
    assert nvmbnd.dcx_type == DCXType.Null  # DeS NVMBNDs are uncompressed


@pytest.mark.game_data
def test_real_chrbnd_loads(des_root, tmp_path):
    from conftest import binary_roundtrip

    path = DEMONS_SOULS.process_dcx_path(des_root / "chr/c1000.chrbnd")
    if not path.is_file():
        pytest.skip(f"Missing DeS CHRBND: {path}")
    chrbnd = CHRBND.from_path(path)
    assert chrbnd.entries
    reloaded = binary_roundtrip(chrbnd, tmp_path, path.name)
    assert len(reloaded.entries) == len(chrbnd.entries)


@pytest.mark.game_data
def test_real_nvmbnd_loads(des_root):
    from soulstruct.demonssouls.maps.navmesh import NVMBND

    nvmbnd_dir = des_root / "map/m01_00_00_00"
    candidates = sorted(nvmbnd_dir.glob("*.nvmbnd")) if nvmbnd_dir.is_dir() else []
    if not candidates:
        pytest.skip(f"No DeS NVMBND found under {nvmbnd_dir}.")
    nvmbnd = NVMBND.from_path(candidates[0])
    assert nvmbnd.navmeshes
