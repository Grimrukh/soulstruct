"""Tests for Elden Ring model/material handling (`soulstruct.eldenring.models`).

Elden Ring replaced DS3-era `MTD` files with `MATBIN` files, which reference a shader (`.spx`) and
carry `params` + `samplers`. Soulstruct's ER `MatDef.from_matbin()` needs *extra* information that
is not in the MATBIN at all -- the shader's `metaparam` sampler groups -- which are baked into the
bundled `eldenring/models/resources/er_shader_sampler_groups.json` (`MatDef.METAPARAMS`).

The three `allmaterial*.matbinbnd.dcx` archives are committed to the repo, so all MATBIN tests here
run without an Elden Ring install.
"""
from __future__ import annotations

import pytest

from soulstruct.base.models.matbin import MATBIN
from soulstruct.base.models.shaders import MatDefError
from soulstruct.containers import Binder
from soulstruct.eldenring.models import CHRBND, GEOMBND, MAPBND, PARTSBND, MatDef
from soulstruct.eldenring.models.shaders import (
    SHADER_GROUP_UV,
    SHADER_UV_SLOTS,
    SamplerGroupRole,
    ShaderProfile,
    extract_map_type,
    get_group_role,
    get_shader_group_uv,
    get_shader_uv_slots,
)
from soulstruct.utilities.files import SOULSTRUCT_PATH


MATBINBND_NAMES = (
    "allmaterial.matbinbnd.dcx",
    "allmaterial_dlc01.matbinbnd.dcx",
    "allmaterial_dlc02.matbinbnd.dcx",
)


@pytest.fixture(scope="module")
def base_matbinbnd() -> Binder:
    path = SOULSTRUCT_PATH("eldenring/models/resources/allmaterial.matbinbnd.dcx")
    if not path.is_file():
        pytest.skip(f"Bundled MATBINBND missing: {path}")
    return Binder.from_path(path)


# ---------------------------------------------------------------------------
# Binder subclass configuration (pure unit)
# ---------------------------------------------------------------------------


def test_flver_binder_entry_roots():
    assert CHRBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\INTERROOT_win64\\chr"
    assert PARTSBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\INTERROOT_win64\\parts"
    assert MAPBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\INTERROOT_win64\\map"
    assert GEOMBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\INTERROOT_win64\\asset\\aeg"


def test_mapbnd_entry_paths():
    mapbnd = MAPBND()
    stem = "m60_42_36_00_000000"
    assert mapbnd.get_flver_entry_path(stem).endswith(f"\\m60_42_36_00\\{stem}\\Model\\{stem}.flver")
    assert mapbnd.get_grass_entry_path(stem).endswith(f"\\m60_42_36_00\\{stem}\\Model\\{stem}.grass")
    with pytest.raises(TypeError):
        mapbnd.get_tpf_entry_path(stem)


def test_geombnd_entry_paths():
    geombnd = GEOMBND()
    stem = "AEG099_060"
    assert geombnd.get_flver_entry_path(stem).endswith(f"\\AEG099\\{stem}\\sib\\{stem}.flver")
    with pytest.raises(TypeError):
        geombnd.get_tpf_entry_path(stem)


def test_no_tpf_entry_ids_for_map_and_asset_binders():
    """ER map/asset textures live in separate `aet` TPFs, not inside the model Binder."""
    assert MAPBND.TPF_ENTRY_ID == -1
    assert GEOMBND.TPF_ENTRY_ID == -1
    assert MAPBND.GRASS_ENTRY_ID == 1200


# ---------------------------------------------------------------------------
# `ShaderProfile` parsing (pure unit)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "stem,category,base_type,tags,suffixes",
    [
        ("C[DetailBlend]", "C", "DetailBlend", [], []),
        ("C[DetailBlend][S2]_cloth", "C", "DetailBlend", ["S2"], ["cloth"]),
        ("M[AMSN_V][Mb2][Ov_AN]_Edge", "M", "AMSN_V", ["Mb2", "Ov_AN"], ["Edge"]),
        ("CS[VA_Frame][Fur]_FurBlur", "CS", "VA_Frame", ["Fur"], ["FurBlur"]),
        ("C[Fur]_cloth", "C", "Fur", [], ["cloth"]),
    ],
)
def test_shader_profile_parsing(stem, category, base_type, tags, suffixes):
    profile = ShaderProfile.from_shader_stem(stem)
    assert profile.category == category
    assert profile.base_type == base_type
    assert profile.tags == tags
    assert profile.suffixes == suffixes
    assert profile.is_recognized


def test_shader_profile_unrecognized_stem():
    profile = ShaderProfile.from_shader_stem("GXFlver_ColDifSpcBumpIbl")
    assert profile == ShaderProfile()
    assert not profile.is_recognized


def test_shader_profile_family_normalization():
    assert ShaderProfile.from_shader_stem("C[AMSN_V]").family == "AMSN"
    assert ShaderProfile.from_shader_stem("CS[VA_Frame][Fur]").family == "Fur"
    assert ShaderProfile.from_shader_stem("C[DetailBlend][S2]").family == "DetailBlend"


def test_shader_profile_flags():
    p = ShaderProfile.from_shader_stem("M[AMSN][Mb3][Ov_AN]_Alpha")
    assert p.multi_blend_count == 3
    assert p.has_overlay
    assert p.overlay_types == "AN"
    assert p.is_alpha
    assert p.is_map
    assert not p.is_character
    assert ShaderProfile.from_shader_stem("C[Fur]_cloth").is_cloth
    assert ShaderProfile.from_shader_stem("C[DetailBlend]_SSS").is_sss
    assert ShaderProfile.from_shader_stem("C[c2030]_Fabric").is_specific_character


def test_shader_profile_no_multi_blend_default():
    assert ShaderProfile.from_shader_stem("C[AMSN]").multi_blend_count == 1
    assert not ShaderProfile.from_shader_stem("C[AMSN]").has_overlay
    assert ShaderProfile.from_shader_stem("C[AMSN]").overlay_types == ""


# ---------------------------------------------------------------------------
# Sampler map-type extraction (pure unit)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "sampler_name,expected",
    [
        ("C_DetailBlend__snp_Texture2D_7_AlbedoMap", "Albedo"),
        ("M_AMSN_Mb2__snp_Texture2D_1_GSBlendMap_AlbedoMap_0", "Albedo"),
        ("C_Crystal__snp_Texture2D_2__DistortionDepth", "DistortionDepth"),
        ("C_Face_S2__SSS_snp_Texture2D_2_Mask3Map", "Mask3"),
        ("C_DetailBlend__snp_Texture2D_3_NormalMap", "Normal"),
        ("C_DetailBlend__snp_Texture2D_4_MetallicMap", "Metallic"),
    ],
)
def test_extract_map_type(sampler_name, expected):
    assert extract_map_type(sampler_name) == expected


def test_extract_map_type_unparseable_returns_empty():
    assert extract_map_type("not a sampler name at all") == ""


# ---------------------------------------------------------------------------
# UV slot tables (pure unit)
# ---------------------------------------------------------------------------


def test_shader_group_uv_semantics_all_appear_in_uv_slots():
    """Documented invariant: every UV semantic in `SHADER_GROUP_UV` must be in `SHADER_UV_SLOTS`."""
    violations = []
    for stem, group_map in SHADER_GROUP_UV.items():
        slots = SHADER_UV_SLOTS.get(stem)
        if slots is None:
            violations.append((stem, "no SHADER_UV_SLOTS entry"))
            continue
        for group, uv in group_map.items():
            if uv not in slots:
                violations.append((stem, group, uv, slots))
    assert not violations, f"SHADER_GROUP_UV/SHADER_UV_SLOTS invariant violated: {violations[:5]}"


def test_uv_semantics_are_valid_uv_layer_names():
    for stem, slots in SHADER_UV_SLOTS.items():
        for name in slots:
            assert name in MatDef.UVLayer.__members__, f"{stem}: unknown UV layer '{name}'"


def test_cloth_stems_normalize_to_base_shader():
    base = next(iter(SHADER_UV_SLOTS))
    assert get_shader_uv_slots(base + "_cloth") == SHADER_UV_SLOTS[base]
    if base in SHADER_GROUP_UV:
        assert get_shader_group_uv(base + "_cloth") == SHADER_GROUP_UV[base]


def test_unknown_shader_lookups_return_none():
    assert get_shader_uv_slots("NoSuchShader") is None
    assert get_shader_group_uv("NoSuchShader") is None


# ---------------------------------------------------------------------------
# `get_group_role` (pure unit)
# ---------------------------------------------------------------------------


def test_group_index_zero_is_ungrouped():
    profile = ShaderProfile.from_shader_stem("C[AMSN]")
    assert get_group_role(profile, 0, [], is_first=True) == SamplerGroupRole.UNGROUPED


def test_group_index_zero_is_blend_control_for_multi_blend():
    profile = ShaderProfile.from_shader_stem("M[AMSN][Mb2]")
    assert get_group_role(profile, 0, [], is_first=True) == SamplerGroupRole.BLEND_CONTROL


def test_family_group_role_lookup():
    profile = ShaderProfile.from_shader_stem("C[DetailBlend]")
    assert get_group_role(profile, 1, [], is_first=True) == SamplerGroupRole.PRIMARY
    assert get_group_role(profile, 2, [], is_first=False) == SamplerGroupRole.DETAIL
    assert get_group_role(profile, 5, [], is_first=False) == SamplerGroupRole.SECONDARY
    # Unknown group index falls back to MISC.
    assert get_group_role(profile, 99, [], is_first=False) == SamplerGroupRole.MISC


def test_amsn_first_group_is_always_primary():
    profile = ShaderProfile.from_shader_stem("C[AMSN]")
    assert get_group_role(profile, 2, [], is_first=True) == SamplerGroupRole.PRIMARY


# ---------------------------------------------------------------------------
# Bundled MATBIN archives
# ---------------------------------------------------------------------------


def test_bundled_matbinbnds_exist():
    for name in MATBINBND_NAMES:
        assert SOULSTRUCT_PATH(f"eldenring/models/resources/{name}").is_file(), name


def test_metaparams_json_is_loaded():
    assert len(MatDef.METAPARAMS) > 500
    # Each non-empty metaparam maps group names to lists of (sampler_name, default_texture_path) pairs.
    checked = 0
    for stem, groups in MatDef.METAPARAMS.items():
        if not groups:
            continue  # 129 shaders have empty metaparams (see `test_metaparams_values_are_all_dicts`)
        assert isinstance(groups, dict), f"{stem}: metaparam is {type(groups).__name__}, not dict"
        for group_name, samplers in groups.items():
            assert isinstance(group_name, str)
            for pair in samplers:
                assert len(pair) == 2
        checked += 1
    assert checked > 500


@pytest.mark.xfail(
    reason="`er_shader_sampler_groups.json` stores 121 empty shader metaparams as JSON arrays `[]` "
           "instead of objects `{}`, contradicting the "
           "`METAPARAMS: dict[str, dict[str, list[tuple[str, str]]]]` annotation. Harmless only because "
           "`from_matbin` short-circuits on falsy metaparams.",
    strict=False,
)
def test_metaparams_values_are_all_dicts():
    non_dicts = [stem for stem, groups in MatDef.METAPARAMS.items() if not isinstance(groups, dict)]
    assert not non_dicts, f"{len(non_dicts)} metaparam entries are not dicts, e.g. {non_dicts[:5]}"


def test_matbin_unpack_and_matdef_sample(base_matbinbnd):
    """Sample MATBINs from across the bundled archive and build `MatDef`s from them."""
    parsed = 0
    sampled = 0
    for entry in base_matbinbnd.entries[::20]:  # ~755 entries spread across the archive
        sampled += 1
        matbin = MATBIN.from_binder_entry(entry)
        assert matbin.shader_path
        assert matbin.shader_stem
        try:
            matdef = MatDef.from_matbin(matbin)
        except (MatDefError, KeyError):
            continue  # legacy GXFlver shader or missing sampler (see xfails below)
        parsed += 1
        assert matdef.shader_stem == matbin.shader_stem
        assert matdef.samplers, f"{entry.name} produced no samplers."
        for sampler in matdef.samplers:
            assert sampler.name
            assert sampler.alias
            assert isinstance(sampler.uv_layer, MatDef.UVLayer)
        assert matdef.get_uv_slot_tuple()
    assert parsed / sampled > 0.9, f"Only {parsed}/{sampled} sampled MATBINs produced a `MatDef`."


def test_matbin_binary_read_is_stable(base_matbinbnd):
    """Reading the same MATBIN entry twice must give identical content."""
    for entry in base_matbinbnd.entries[:50]:
        a = MATBIN.from_binder_entry(entry)
        b = MATBIN.from_binder_entry(entry)
        assert a.shader_path == b.shader_path
        assert a.source_path == b.source_path
        assert [(s.sampler_type, s.path) for s in a.samplers] == [(s.sampler_type, s.path) for s in b.samplers]
        assert [(p.name, p.value) for p in a.params] == [(p.name, p.value) for p in b.params]


@pytest.mark.xfail(
    reason="CRITICAL BUG: `MATBIN.to_writer()` and `MATBINParam/MATBINSampler.fill_matbin_data()` append "
           "UTF-16 strings WITHOUT null terminators (`writer.append(name.encode('utf-16-le'))`), so all "
           "strings run together. 0/300 vanilla ER MATBINs survive a pack->unpack round-trip; most raise "
           "`UnicodeDecodeError`. MATBIN writing is unusable.",
    strict=False,
)
def test_matbin_binary_roundtrip(base_matbinbnd):
    """unpack -> pack -> unpack must be stable for MATBIN files."""
    for entry in base_matbinbnd.entries[:50]:
        matbin = MATBIN.from_binder_entry(entry)
        packed = bytes(matbin.to_writer())
        reloaded = MATBIN.from_bytes(packed)
        assert reloaded.shader_path == matbin.shader_path
        assert reloaded.source_path == matbin.source_path
        assert [(s.sampler_type, s.path) for s in reloaded.samplers] == [
            (s.sampler_type, s.path) for s in matbin.samplers
        ]
        assert [(p.name, p.value) for p in reloaded.params] == [(p.name, p.value) for p in matbin.params]
        assert bytes(reloaded.to_writer()) == packed


def test_matdef_from_matbin_name_is_unsupported():
    with pytest.raises(MatDefError):
        MatDef.from_matbin_name("C[AMSN].matbin")


def test_legacy_gxflver_shaders_raise_matdef_error(base_matbinbnd):
    """ER MATBINs that still use DS3-era `GXFlver_*` shaders have no metaparam and must fail loudly."""
    for entry in base_matbinbnd.entries:
        matbin = MATBIN.from_binder_entry(entry)
        if matbin.shader_stem.startswith("GXFlver"):
            with pytest.raises(MatDefError):
                MatDef.from_matbin(matbin)
            return
    pytest.skip("No legacy GXFlver MATBIN found in bundled archive.")


@pytest.mark.slow
def test_all_bundled_matbins_parse():
    """Full sweep of all ~20k bundled ER MATBINs.

    Currently ~439 fail with `MatDefError` (legacy `GXFlver_*` / unlisted shaders) and ~41 with
    `KeyError` (see `test_matdef_does_not_keyerror_on_missing_samplers`).
    """
    failures = {"MatDefError": 0, "KeyError": 0, "other": 0}
    total = 0
    for name in MATBINBND_NAMES:
        path = SOULSTRUCT_PATH(f"eldenring/models/resources/{name}")
        if not path.is_file():
            pytest.skip(f"Bundled MATBINBND missing: {path}")
        binder = Binder.from_path(path)
        for entry in binder.entries:
            total += 1
            matbin = MATBIN.from_binder_entry(entry)
            try:
                MatDef.from_matbin(matbin)
            except MatDefError:
                failures["MatDefError"] += 1
            except KeyError:
                failures["KeyError"] += 1
            except Exception:
                failures["other"] += 1
    assert total > 19000
    assert failures["other"] == 0, f"Unexpected MatDef failures: {failures}"
    # Guard against regressions: no more than 3% of materials may fail.
    assert (failures["MatDefError"] + failures["KeyError"]) / total < 0.03


@pytest.mark.slow
@pytest.mark.xfail(
    reason="BUG: `MatDef.from_matbin` calls `matbin.get_sampler_path(sampler_name)` for every sampler "
           "listed in the shader metaparam. If the MATBIN does not override that sampler, `get_sampler_path` "
           "raises `KeyError` and the whole material fails (41 vanilla ER materials, e.g. all "
           "`P[ChrCustomize][Skin]` ones). It should fall back to the metaparam default path.",
    strict=False,
)
def test_matdef_does_not_keyerror_on_missing_samplers():
    key_errors = []
    for name in MATBINBND_NAMES:
        path = SOULSTRUCT_PATH(f"eldenring/models/resources/{name}")
        if not path.is_file():
            pytest.skip(f"Bundled MATBINBND missing: {path}")
        binder = Binder.from_path(path)
        for entry in binder.entries:
            matbin = MATBIN.from_binder_entry(entry)
            try:
                MatDef.from_matbin(matbin)
            except MatDefError:
                pass
            except KeyError:
                key_errors.append((entry.name, matbin.shader_stem))
    assert not key_errors, f"{len(key_errors)} MATBINs raised KeyError, e.g. {key_errors[:3]}"
