"""Tests for `soulstruct.darksouls1r.sound` (FMOD FEV event banks and FSB sample banks).

This package is a port of HotPocketRemix's `DarkSouls1SoundProjects` and is one of the least-trafficked
corners of Soulstruct. Several tests here are `xfail`-marked because the FEV/FSB readers currently raise
on *every* vanilla DSR file; see the audit report for details.

Write support intentionally does not exist: both `FEV.to_writer()` and `FSB.to_writer()` raise `TypeError`
telling the user to rebuild with FMOD Designer from a generated FDP.
"""
from __future__ import annotations

import dataclasses
import math
import re
import xml.dom.minidom
from pathlib import Path

import pytest

from soulstruct.darksouls1r.sound import fsb as fsb_module
from soulstruct.darksouls1r.sound import utilities as sound_utilities
from soulstruct.darksouls1r.sound.fev import core as fev_core
from soulstruct.darksouls1r.sound.fev.core import (
    FEV,
    Envelope,
    Event,
    EventCategory,
    EventGroup,
    Layer,
    Parameter,
    Point,
    SoundDef,
    SoundDefFolder,
    SoundDefProperty,
    SoundInstance,
    UserProperty,
    WavebankInfo,
    Waveform,
    XMLObject,
    decibel_to_field_ratio,
    field_ratio_to_decibel,
    new_guid,
)
from soulstruct.darksouls1r.sound.fsb import FSB, FSBHeaderMode, FSBSampleHeader, FSBSampleMode, fsbext


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make(cls, **kwargs):
    """Construct a `dataclass` filling every field that has no default with `0`.

    The FEV dataclasses have dozens of required fields, so this keeps the tests readable.
    """
    values = {}
    for f in dataclasses.fields(cls):
        if f.name in kwargs:
            continue
        if f.default is not dataclasses.MISSING or f.default_factory is not dataclasses.MISSING:
            continue
        values[f.name] = 0
    values.update(kwargs)
    return cls(**values)


def _make_event(name: str, sounddef_indices: list[int]) -> Event:
    instances = [_make(SoundInstance, sounddef_index=i) for i in sounddef_indices]
    layer = Layer(priority=-1, control_parameter=-1, sound_instances=instances, envelopes=[])
    return _make(
        Event,
        name=name,
        guid="00000000-0000-0000-0000-000000000000",
        layers=[layer],
        parameters=[],
        user_properties=[],
        category_names=["master"],
    )


def _make_fev(events: list[Event], sounddefs: list[SoundDef]) -> FEV:
    group = EventGroup(name="master", user_properties=[], subgroups=[], events=events)
    return FEV(
        project_name="test_project",
        wavebanks=[],
        top_event_category=None,
        top_event_groups=[group],
        sounddef_properties=[],
        sounddefs=sounddefs,
    )


def _sounddef(path: str) -> SoundDef:
    return SoundDef(name=path, sounddef_prop_index=0, waveforms=[])


# ---------------------------------------------------------------------------
# Pure-unit: decibel/field-ratio conversion
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("ratio", [1.0, 0.5, 0.25, 0.1, 0.01])
def test_field_ratio_decibel_roundtrip(ratio):
    db = field_ratio_to_decibel(ratio)
    assert decibel_to_field_ratio(db) == pytest.approx(ratio)


def test_field_ratio_to_decibel_clamps_at_minus_60():
    assert field_ratio_to_decibel(0.0) == -60.0
    assert field_ratio_to_decibel(0.001) == -60.0
    assert field_ratio_to_decibel(-5.0) == -60.0


def test_decibel_to_field_ratio_clamps():
    assert decibel_to_field_ratio(-60.0) == 0.001
    assert decibel_to_field_ratio(-1000.0) == 0.001
    assert decibel_to_field_ratio(0.0) == 1.0


def test_field_ratio_to_decibel_unity_is_zero_db():
    assert field_ratio_to_decibel(1.0) == 0.0
    assert field_ratio_to_decibel(0.5) == pytest.approx(-6.0206, abs=1e-3)


def test_decibel_clamp_boundary_is_not_perfectly_invertible():
    """`field_ratio_to_decibel` clamps at 0.001, so tiny ratios all collapse to -60 dB."""
    assert field_ratio_to_decibel(1e-9) == -60.0
    # Round-trip does NOT recover 1e-9.
    assert decibel_to_field_ratio(-60.0) == 0.001


# ---------------------------------------------------------------------------
# Pure-unit: XML helpers
# ---------------------------------------------------------------------------


def test_new_guid_format():
    guid = new_guid()
    assert re.fullmatch(r"<guid>\{[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}}</guid>", guid), guid
    assert new_guid() != new_guid(), "GUIDs must be unique per call."


def test_fev_and_fsb_tag_helpers_disagree_on_empty_value():
    """`fev.core.tag` and `fsb.tag` are near-duplicates that differ for empty values.

    This is an API inconsistency worth pinning: the FEV version emits `<x></x>`, the FSB
    version emits `<x/>`. Both are valid XML but the duplication is a maintenance hazard.
    """
    assert fev_core.tag("notes") == "<notes></notes>"
    assert fsb_module.tag("notes") == "<notes/>"
    assert fev_core.tag("x", 5) == fsb_module.tag("x", 5) == "<x>5</x>"


def test_read_lp_string_reads_length_prefixed_utf8():
    from soulstruct.utilities.binary import BinaryReader

    data = (5).to_bytes(4, "little") + b"hello"
    reader = BinaryReader(data)
    assert fev_core.read_lp_string(reader) == "hello"
    assert reader.position == 9


# ---------------------------------------------------------------------------
# Pure-unit: enums
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("bank_type", list(WavebankInfo.BankType))
def test_wavebank_bank_type_xml_name_roundtrip(bank_type):
    assert WavebankInfo.BankType.from_xml_name(bank_type.to_xml_name()) is bank_type


@pytest.mark.parametrize("behavior", list(EventCategory.PlaybackBehavior))
def test_event_category_playback_behavior_xml_roundtrip(behavior):
    assert EventCategory.PlaybackBehavior.from_xml_name(behavior.to_xml_name()) is behavior


@pytest.mark.parametrize(
    "prop_type, expected_tag",
    [
        (UserProperty.PropertyType.INTEGER, "data_int"),
        (UserProperty.PropertyType.FLOATING_POINT, "data_float"),
        (UserProperty.PropertyType.STRING, "data_string"),
    ],
)
def test_user_property_get_tag(prop_type, expected_tag):
    assert prop_type.get_tag() == expected_tag


def test_event_enum_xml_names_are_total():
    """Every member of every `Event` sub-enum with a `to_xml_name` must be mapped."""
    for enum_cls in (
        Event.EventMode,
        Event.ThreeDimRolloff,
        Event.ThreeDimPosition,
        Event.PitchUnits,
        Event.PlaybackBehavior,
    ):
        for member in enum_cls:
            assert isinstance(member.to_xml_name(), str)


def test_envelope_effect_type_xml_names_are_total():
    for member in Envelope.EffectType:
        assert isinstance(member.to_xml_name(), str)


def test_sounddef_property_play_mode_xml_names_are_total_and_unique():
    names = [m.to_xml_name() for m in SoundDefProperty.PlayMode]
    assert len(set(names)) == len(names)


def test_parameter_loop_behavior_xml_names():
    assert Parameter.LoopBehavior.ONESHOT.to_xml_name() == "0"
    assert Parameter.LoopBehavior.ONESHOT_AND_STOP.to_xml_name() == "1"
    assert Parameter.LoopBehavior.LOOP.to_xml_name() == "2"


def test_sound_instance_autopitch_param_xml_name_is_lossy():
    """`AutopitchParameter.LAYER_CONTROL` (2) maps to XML '1'; the mapping has no inverse."""
    assert SoundInstance.AutopitchParameter.EVENT_PRIMARY.to_xml_name() == "0"
    assert SoundInstance.AutopitchParameter.LAYER_CONTROL.to_xml_name() == "1"
    assert not hasattr(SoundInstance.AutopitchParameter, "from_xml_name")


# ---------------------------------------------------------------------------
# Pure-unit: SoundDefFolder hierarchy building
# ---------------------------------------------------------------------------


def test_sounddef_folder_builds_nested_hierarchy():
    master = SoundDefFolder("master")
    sd_a = _sounddef("/chr/c1000/footstep")
    sd_b = _sounddef("/chr/c1000/voice")
    sd_c = _sounddef("/obj/door")
    for sd in (sd_a, sd_b, sd_c):
        master.add_new_sounddef(sd.name, sd)

    assert set(master.subfolders) == {"chr", "obj"}
    assert master.sounddefs == []
    assert set(master.subfolders["chr"].subfolders) == {"c1000"}
    assert master.subfolders["chr"].subfolders["c1000"].sounddefs == [sd_a, sd_b]
    assert master.subfolders["obj"].sounddefs == [sd_c]


def test_sounddef_folder_direct_child():
    master = SoundDefFolder("master")
    sd = _sounddef("/loose_sound")
    master.add_new_sounddef(sd.name, sd)
    assert master.sounddefs == [sd]
    assert master.subfolders == {}


def test_sounddef_folder_rejects_relative_path():
    master = SoundDefFolder("master")
    with pytest.raises(ValueError):
        master.add_new_sounddef("chr/c1000/footstep", _sounddef("chr/c1000/footstep"))


@pytest.mark.xfail(
    reason="BUG: docstring says a path with no separators is legal, but `add_new_sounddef` raises for it "
           "(len(split)==1 falls through to the ValueError branch).",
    strict=False,
)
def test_sounddef_folder_accepts_bare_name_per_docstring():
    master = SoundDefFolder("master")
    sd = _sounddef("bare_name")
    master.add_new_sounddef(sd.name, sd)
    assert master.sounddefs == [sd]


def test_sounddef_folder_xml_is_well_formed():
    master = SoundDefFolder("master")
    sd = _sounddef("/chr/c1000/footstep")
    master.add_new_sounddef(sd.name, sd)
    prop = _make(SoundDefProperty, play_mode=SoundDefProperty.PlayMode.RANDOM,
                 recalc_pitch_rand=SoundDefProperty.RecalculateRand.ON_START)
    xml_string = "\n".join(master.to_xml_lines([prop]))
    # Should parse as XML once wrapped (it is a single root element).
    xml.dom.minidom.parseString(xml_string)


# ---------------------------------------------------------------------------
# Pure-unit: FEV object model (no game data required)
# ---------------------------------------------------------------------------


def test_fev_get_all_events_walks_subgroups():
    inner_event = _make_event("inner", [0])
    outer_event = _make_event("outer", [1])
    inner_group = EventGroup(name="inner_group", user_properties=[], subgroups=[], events=[inner_event])
    outer_group = EventGroup(name="outer_group", user_properties=[], subgroups=[inner_group], events=[outer_event])
    fev = FEV(
        project_name="p", wavebanks=[], top_event_category=None, top_event_groups=[outer_group],
        sounddef_properties=[], sounddefs=[],
    )
    assert [e.name for e in fev.get_all_events()] == ["outer", "inner"]


def test_fev_get_all_event_names_with_regex():
    fev = _make_fev([_make_event("aaa", [0]), _make_event("bbb", [1])], [_sounddef("/a"), _sounddef("/b")])
    assert fev.get_all_event_names(re.compile("a.*")) == ["aaa"]


@pytest.mark.xfail(
    reason="BUG (fev/core.py:1537): `get_all_event_names()` has no `return` on the `name_regex is None` "
           "branch, so it silently returns `None` instead of all event names.",
    strict=False,
)
def test_fev_get_all_event_names_without_regex():
    fev = _make_fev([_make_event("aaa", [0]), _make_event("bbb", [1])], [_sounddef("/a"), _sounddef("/b")])
    assert fev.get_all_event_names() == ["aaa", "bbb"]


def test_event_has_name_string_and_pattern():
    event = _make_event("frpg_sfx_chr", [0])
    assert event.has_name("frpg_sfx_chr")
    assert not event.has_name("frpg_sfx_obj")
    assert event.has_name(re.compile("frpg_sfx_.*"))
    # NOTE: uses `.match`, not `.fullmatch`, so a prefix pattern matches.
    assert event.has_name(re.compile("frpg"))


def test_fev_remove_events_removes_matching_events():
    sounddefs = [_sounddef("/a"), _sounddef("/b"), _sounddef("/c")]
    fev = _make_fev([_make_event("keep", [0]), _make_event("drop", [1]), _make_event("keep2", [2])], sounddefs)
    removed = fev.remove_events("drop", remove_unused_sounddefs=False)
    assert [e.name for e in removed] == ["drop"]
    assert [e.name for e in fev.get_all_events()] == ["keep", "keep2"]
    assert len(fev.sounddefs) == 3  # not removed


def test_fev_remove_events_removes_unused_sounddefs_and_reindexes():
    sounddefs = [_sounddef("/a"), _sounddef("/b"), _sounddef("/c")]
    fev = _make_fev([_make_event("keep", [0]), _make_event("drop", [1]), _make_event("keep2", [2])], sounddefs)
    fev.remove_events("drop", remove_unused_sounddefs=True)
    assert [sd.name for sd in fev.sounddefs] == ["/a", "/c"]
    remaining = {e.name: e.layers[0].sound_instances[0].sounddef_index for e in fev.get_all_events()}
    assert remaining == {"keep": 0, "keep2": 1}


def test_fev_remove_events_keeps_shared_sounddefs():
    sounddefs = [_sounddef("/shared"), _sounddef("/only_dropped")]
    fev = _make_fev([_make_event("keep", [0]), _make_event("drop", [0, 1])], sounddefs)
    fev.remove_events("drop")
    assert [sd.name for sd in fev.sounddefs] == ["/shared"]
    assert fev.get_all_events()[0].layers[0].sound_instances[0].sounddef_index == 0


@pytest.mark.xfail(
    reason="BUG (fev/core.py:1496-1501): `_remove_event_from_group` appends the event to "
           "`removed_events` once per SoundInstance (the check is inside the innermost loop), so an "
           "event with several sound instances is reported multiple times.",
    strict=False,
)
def test_fev_remove_events_reports_each_event_once():
    sounddefs = [_sounddef("/a"), _sounddef("/b"), _sounddef("/c")]
    fev = _make_fev([_make_event("drop", [0, 1, 2])], sounddefs)
    removed = fev.remove_events("drop", remove_unused_sounddefs=False)
    assert [e.name for e in removed] == ["drop"]


@pytest.mark.xfail(
    reason="BUG (fev/core.py:1496-1504): an event with no layers/sound instances is removed from the "
           "group (line 1504) but never recorded in `removed_events`, because the recording happens "
           "inside the SoundInstance loop.",
    strict=False,
)
def test_fev_remove_events_reports_events_with_no_sound_instances():
    event = _make(
        Event, name="silent", guid="0", layers=[], parameters=[], user_properties=[], category_names=[],
    )
    fev = _make_fev([event], [])
    removed = fev.remove_events("silent", remove_unused_sounddefs=False)
    assert fev.get_all_events() == []  # actually removed...
    assert [e.name for e in removed] == ["silent"]  # ...but not reported


def test_fev_remove_events_with_regex():
    sounddefs = [_sounddef("/a"), _sounddef("/b")]
    fev = _make_fev([_make_event("x_one", [0]), _make_event("y_two", [1])], sounddefs)
    removed = fev.remove_events(re.compile("x_.*"), remove_unused_sounddefs=False)
    assert [e.name for e in removed] == ["x_one"]


def test_fev_find_paths_from_waveforms_with_bank_index():
    waveform = _make(Waveform, weight=1, name="/bank/sound.wav", bank_name="frpg_main", index_in_bank=3, playtime=0)
    sounddef = SoundDef(name="/sd", sounddef_prop_index=0, waveforms=[waveform])
    fev = _make_fev([], [sounddef])
    assert fev.find_paths_from_waveforms_with_bank_index("frpg_main", 3) == ["/bank/sound.wav"]
    assert fev.find_paths_from_waveforms_with_bank_index("frpg_main", 4) == []
    assert fev.find_paths_from_waveforms_with_bank_index("other", 3) == []


# ---------------------------------------------------------------------------
# Pure-unit: XML generation
# ---------------------------------------------------------------------------


def test_event_category_to_xml_lines_is_well_formed():
    sub = EventCategory(
        name="sub", volume=1.0, pitch=0.0, maxplaybacks=32,
        maxplaybacks_behavior=EventCategory.PlaybackBehavior.STEAL_OLDEST, subcategories=[],
    )
    top = EventCategory(
        name="master", volume=1.0, pitch=0.0, maxplaybacks=64,
        maxplaybacks_behavior=EventCategory.PlaybackBehavior.JUST_FAIL, subcategories=[sub],
    )
    xml.dom.minidom.parseString("\n".join(top.to_xml_lines()))


def test_user_property_to_xml_lines():
    prop = UserProperty("volume_scale", UserProperty.PropertyType.FLOATING_POINT, 0.5)
    lines = prop.to_xml_lines()
    assert lines[0] == "<userproperty>"
    assert "<data_float>0.5</data_float>" in lines
    xml.dom.minidom.parseString("\n".join(lines))


def test_parameter_to_xml_lines_range_spacing():
    param = Parameter(
        name="p", velocity=0.0, param_min=0.0, param_max=100.0, is_primary=True,
        loop_behavior=Parameter.LoopBehavior.LOOP, seek_speed=0.0, controlled_envelope_count=0,
    )
    lines = param.to_xml_lines()
    assert "<rangespacing>10.0</rangespacing>" in lines
    xml.dom.minidom.parseString("\n".join(lines))


def test_waveform_to_xml_lines():
    waveform = _make(Waveform, weight=100, name="a.wav", bank_name="bank", index_in_bank=0, playtime=1234)
    lines = waveform.to_xml_lines()
    assert "<filename>a.wav</filename>" in lines
    assert "<weight>100</weight>" in lines
    # `playtime` is deliberately not stored in FDP XML.
    assert not any("playtime" in line for line in lines)
    xml.dom.minidom.parseString("\n".join(lines))


def test_point_to_xml_string():
    from soulstruct.utilities.maths import Vector2

    point = Point(xy=Vector2([1.5, 2.5]), curve_shape=Point.CurveShape.LINEAR)
    assert point.to_xml_string(0) == "<point>1.5,2.5,1,2</point>"
    assert point.to_xml_string(3) == "<point>1.5,2.5,0,2</point>"


def test_wavebank_info_default_props_is_well_formed():
    xml.dom.minidom.parseString("\n".join(WavebankInfo.get_default_props()))


def test_fev_to_xml_lines_end_is_well_formed_fragment():
    lines = FEV.to_xml_lines_end()
    assert lines[-1] == "</project>"
    xml.dom.minidom.parseString("<project>" + "\n".join(lines))


def test_event_to_xml_lines_is_well_formed():
    event = _make_event("ev", [0])
    event.mode = Event.EventMode.THREE_DIM
    event.three_dim_rolloff = Event.ThreeDimRolloff.LOGARITHMIC
    event.three_dim_position = Event.ThreeDimPosition.HEAD_RELATIVE
    event.pitch_rand_units = Event.PitchUnits.OCTAVES
    event.max_playback_behavior = Event.PlaybackBehavior.STEAL_OLDEST
    event.volume = 1.0
    event.cone_outside_volume = 1.0
    sound_instance = event.layers[0].sound_instances[0]
    sound_instance.start_mode = SoundInstance.StartMode.IMMEDIATE
    sound_instance.loop_mode = SoundInstance.LoopMode.ONESHOT
    sound_instance.autopitch_param = SoundInstance.AutopitchParameter.EVENT_PRIMARY
    sound_instance.fade_in_type = SoundInstance.CrossfadeType.LINEAR
    sound_instance.fade_out_type = SoundInstance.CrossfadeType.LINEAR
    xml.dom.minidom.parseString("\n".join(event.to_xml_lines([_sounddef("/a")])))


# ---------------------------------------------------------------------------
# Pure-unit: known broken class-level wiring
# ---------------------------------------------------------------------------


def test_point_has_struct_class_var():
    assert Point.STRUCT is not None


def test_sounddef_property_struct_fields_match_dataclass_fields():
    struct_names = {f.name for f in dataclasses.fields(SoundDefProperty.STRUCT) if not f.name.startswith("_")}
    dataclass_names = {f.name for f in dataclasses.fields(SoundDefProperty)}
    assert struct_names <= dataclass_names, struct_names - dataclass_names


@pytest.mark.xfail(
    reason="BUG (fev/core.py:170, 370, 444): `XMLObject.from_xml` calls `Element.getchildren()`, removed "
           "in Python 3.9 (and `EventCategory` even calls a non-existent `getChildren`). It also calls "
           "`cls()` with no arguments, which no FEV dataclass supports. The entire FROM_XML path is dead.",
    strict=False,
)
def test_xmlobject_from_xml_works():
    from xml.etree import ElementTree

    element = ElementTree.fromstring(
        "<soundbank><name>frpg_main</name><_PC_banktype>Stream</_PC_banktype>"
        "<_PC_maxstreams>10</_PC_maxstreams></soundbank>"
    )
    bank = WavebankInfo.from_xml(element)
    assert bank.bank_name == "frpg_main"


def test_from_xml_is_dead_code_on_modern_python():
    """Positive assertion of the *current* behaviour: `getchildren()` no longer exists."""
    from xml.etree import ElementTree

    element = ElementTree.fromstring("<a><b>1</b></a>")
    assert not hasattr(element, "getchildren")


# ---------------------------------------------------------------------------
# Pure-unit: write support does not exist
# ---------------------------------------------------------------------------


def test_fev_to_writer_raises():
    fev = _make_fev([], [])
    with pytest.raises(TypeError, match="FMOD Designer"):
        fev.to_writer()


def test_fsb_to_writer_raises():
    with pytest.raises(TypeError, match="FMOD Designer"):
        FSB().to_writer()


def test_fev_write_raises_because_to_writer_raises(tmp_path):
    fev = _make_fev([], [])
    with pytest.raises(TypeError):
        fev.write(tmp_path / "out.fev")


# ---------------------------------------------------------------------------
# Pure-unit: FSB structures
# ---------------------------------------------------------------------------


def test_fsb_sample_mode_flags_are_unique_powers_of_two():
    for member in FSBSampleMode:
        assert member.value & (member.value - 1) == 0, f"{member.name} is not a single bit"


def test_fsb_header_mode_flags_are_unique_powers_of_two():
    for member in FSBHeaderMode:
        assert member.value & (member.value - 1) == 0, f"{member.name} is not a single bit"


def test_fsb_sample_header_struct_size_is_stable():
    from soulstruct.utilities.binary import ByteOrder

    size = FSBSampleHeader.get_size(ByteOrder.LittleEndian, False)
    assert size == 80, size


def test_fsb_sample_header_compute_channel_mode():
    header = FSBSampleHeader(
        total_size=80, name="a.wav", length=0, compressed_length=0, loop_start=0, loop_end=0,
        mode_flags=0, deffreq=44100, defvol=255, defpan=128, defpri=128, channel_count=1,
        mindistance=1.0, maxdistance=10000.0, size_32bits=0, varvol=0, varpan=0,
    )
    assert header.compute_channel_mode() == 0
    header.mode_flags = FSBSampleMode.FSOUND_MULTICHANNEL | FSBSampleMode.FSOUND_CHANNELMODE_ALLSTEREO
    assert header.compute_channel_mode() == 2
    header.mode_flags = FSBSampleMode.FSOUND_MULTICHANNEL | FSBSampleMode.FSOUND_CHANNELMODE_PROTOOLS
    assert header.compute_channel_mode() == 3


def test_fsb_sample_header_to_xml_lines_rejects_mismatched_path():
    header = FSBSampleHeader(
        total_size=80, name="a.wav", length=0, compressed_length=0, loop_start=0, loop_end=0,
        mode_flags=0, deffreq=44100, defvol=255, defpan=128, defpri=128, channel_count=1,
        mindistance=1.0, maxdistance=10000.0, size_32bits=0, varvol=0, varpan=0,
    )
    with pytest.raises(ValueError):
        header.to_xml_lines(Path("bank/m10/b.wav"))
    lines = header.to_xml_lines(Path("bank/m10/a.wav"))
    assert lines[0] == "<waveform>"
    xml.dom.minidom.parseString("\n".join(lines))


def test_fsbext_executable_is_shipped():
    from soulstruct.utilities.files import SOULSTRUCT_PATH

    assert SOULSTRUCT_PATH("darksouls1r/sound/fsbext.exe").is_file(), (
        "fsbext.exe is required for FSB extraction and is expected to ship with the package."
    )


def test_fsbext_command_is_not_quoted():
    """`fsbext()` builds a shell string by f-string concatenation with no quoting of the executable.

    Documents the current (fragile) behaviour without actually running the executable.
    """
    import inspect

    source = inspect.getsource(fsbext)
    assert 'f"{executable} {options} {fsb_path}"' in source


# ---------------------------------------------------------------------------
# Pure-unit: sound.utilities (optional `pydub` dependency)
# ---------------------------------------------------------------------------


def test_pydub_import_is_guarded():
    """`sound/utilities.py` must import `pydub` inside a try/except so a default install works."""
    assert hasattr(sound_utilities, "pydub")  # module-level name always defined
    # Whether or not pydub is installed, importing the module must have succeeded (it did, above).


def test_move_extracted_mp3_missing_source_logs_and_returns(tmp_path, caplog):
    sample = object()
    missing = tmp_path / "bank" / "nothing.mp3"
    with caplog.at_level("ERROR"):
        result = sound_utilities.move_extracted_mp3(tmp_path, sample, missing, convert_to_wav=False)
    assert result is None
    assert not missing.exists()


def test_move_extracted_mp3_moves_file(tmp_path):
    extracted_dir = tmp_path / "extracted"
    extracted_dir.mkdir()
    (extracted_dir / "sound.mp3").write_bytes(b"\xff\xfb\x00\x00")
    target = tmp_path / "bank" / "chr" / "sound.mp3"
    sound_utilities.move_extracted_mp3(extracted_dir, object(), target, convert_to_wav=False)
    assert target.is_file()
    assert target.read_bytes() == b"\xff\xfb\x00\x00"
    assert not (extracted_dir / "sound.mp3").exists()


def test_move_extracted_mp3_wav_conversion_without_pydub(tmp_path, caplog):
    if sound_utilities.pydub is not None:
        pytest.skip("`pydub` is installed; this test covers the missing-dependency path.")
    extracted_dir = tmp_path / "extracted"
    extracted_dir.mkdir()
    (extracted_dir / "sound.mp3").write_bytes(b"\xff\xfb\x00\x00")
    target = tmp_path / "bank" / "sound.mp3"
    sound_utilities._PYDUB_WARNING_DONE = False
    with caplog.at_level("WARNING"):
        sound_utilities.move_extracted_mp3(extracted_dir, object(), target, convert_to_wav=True)
    assert target.is_file(), "File must still be moved even without pydub."
    assert any("pydub" in r.message for r in caplog.records)


# ---------------------------------------------------------------------------
# Game data: FSB / FEV reading (currently broken)
# ---------------------------------------------------------------------------


def _dsr_sound_dir(dsr_root: Path) -> Path:
    sound_dir = dsr_root / "sound"
    if not sound_dir.is_dir():
        pytest.skip(f"No `sound` directory in DSR install: {sound_dir}")
    return sound_dir


@pytest.mark.game_data
def test_fsb_from_path(dsr_root):
    sound_dir = _dsr_sound_dir(dsr_root)
    fsb_paths = sorted(sound_dir.glob("*.fsb"))
    if not fsb_paths:
        pytest.skip("No FSB files in DSR sound directory.")
    fsb = FSB.from_path(fsb_paths[0])
    assert fsb.samples
    assert fsb.bank_hash != 0


@pytest.mark.game_data
def test_fev_from_path(dsr_root):
    sound_dir = _dsr_sound_dir(dsr_root)
    fev_paths = sorted(sound_dir.glob("*.fev"))
    if not fev_paths:
        pytest.skip("No FEV files in DSR sound directory.")
    fev = FEV.from_path(fev_paths[0])
    assert fev.project_name


@pytest.mark.game_data
def test_fev_header_signature_is_fev1(dsr_root):
    """Even though full parsing fails, the header struct itself must validate."""
    from soulstruct.utilities.binary import BinaryReader

    sound_dir = _dsr_sound_dir(dsr_root)
    fev_paths = sorted(sound_dir.glob("*.fev"))
    if not fev_paths:
        pytest.skip("No FEV files in DSR sound directory.")
    for path in fev_paths[:20]:
        reader = BinaryReader(path.read_bytes()[:64])
        header = FEV.FEVHeaderStruct.from_bytes(reader)
        assert header.version_byte >= 0
        project_name = fev_core.read_lp_string(reader)
        assert isinstance(project_name, str)


@pytest.mark.game_data
def test_fsb_header_signature_is_fsb4(dsr_root):
    from soulstruct.utilities.binary import BinaryReader

    sound_dir = _dsr_sound_dir(dsr_root)
    fsb_paths = sorted(sound_dir.glob("*.fsb"))
    if not fsb_paths:
        pytest.skip("No FSB files in DSR sound directory.")
    for path in fsb_paths[:20]:
        reader = BinaryReader(path.read_bytes()[:64])
        header = fsb_module.FSBHeaderStruct.from_bytes(reader)
        assert header.sample_count > 0
        assert header.sample_headers_size > 0
