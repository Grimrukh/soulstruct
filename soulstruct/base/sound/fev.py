"""Adapted from `DarkSouls1SoundProjects` by HotPocketRemix, with much gratitude."""
from __future__ import annotations

import logging
import math
import struct
import typing as tp
import uuid
from enum import IntEnum, unique

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader

_LOGGER = logging.getLogger(__name__)


def tag(tag_name: str, value: tp.Any = ""):
    return f"<{tag_name}>{value}</{tag_name}>"


def new_guid() -> str:
    return "<guid>" + str(uuid.uuid4()) + "</guid>"


def read_string_from_length(reader: BinaryReader, strip=True) -> str:
    length = reader.unpack_value("I")
    return reader.unpack_string(length=length, strip=strip, encoding="utf-8")


def field_ratio_to_decibel(field_ratio) -> float:
    """Converts a field ratio to its corresponding decibel value.

    Value is clamped to -60 at minimum to prevent log(0) errors.
    """
    if field_ratio <= 0.001:
        return -60.0
    return 20 * math.log10(field_ratio)


CONSOLES = ("PC", "XBOX", "XBOX360", "GC", "PS2", "PSP", "PS3", "WII")
TEMPLATE_PROPS = (
    "LAYERS",
    "KEEP_EFFECTS_PARAMS",
    "VOLUME",
    "PITCH",
    "PITCH_RANDOMIZATION",
    "VOLUME_RANDOMIZATION",
    "PRIORITY",
    "MAX_PLAYBACKS",
    "MAX_PLAYBACKS_BEHAVIOR",
    "STEAL_PRIORITY",
    "MODE",
    "IGNORE_GEOMETRY",
    "X_3D_ROLLOFF",
    "X_3D_MIN_DISTANCE",
    "X_3D_MAX_DISTANCE",
    "X_3D_POSITION",
    "X_3D_POSITION_RANDOMIZATION",
    "X_3D_CONE_INSIDE_ANGLE",
    "X_3D_CONE_OUTSIDE_ANGLE",
    "X_3D_CONE_OUTSIDE_VOLUME",
    "X_3D_DOPPLER_FACTOR",
    "REVERB_WET_LEVEL",
    "REVERB_DRY_LEVEL",
    "X_3D_SPEAKER_SPREAD",
    "X_3D_PAN_LEVEL",
    "X_2D_SPEAKER_L",
    "X_2D_SPEAKER_C",
    "X_2D_SPEAKER_R",
    "X_2D_SPEAKER_LS",
    "X_2D_SPEAKER_RS",
    "X_2D_SPEAKER_LR",
    "X_2D_SPEAKER_RR",
    "X_SPEAKER_LFE",
    "ONESHOT",
    "FADEIN_TIME",
    "FADEOUT_TIME",
    "NOTES",
    "USER_PROPERTIES",
)


PROJECT_FOOTER_COMPOSITION = """
<Composition>
    <AuditionConsoleControlRepository>
        <AuditionConsoleControl Type="Utility" Xpos="18" Ypos="18">
            <SimpleRack>
                <ControlName>Reset</ControlName>
                <ControlRange>0, 1</ControlRange>
                <ControlWidget>
                    <ResetControl/>
                </ControlWidget>
                <ControlMapping Type="3" ID="0"/>
            </SimpleRack>
        </AuditionConsoleControl>
    </AuditionConsoleControlRepository>
    <CompositionUI>
        <SceneEditor>
            <SceneEditorItemRepository/>
        </SceneEditor>
        <ThemeEditor>
            <ThemeEditorItemRepository/>
        </ThemeEditor>
    </CompositionUI>
    <CueFactory>
        <UID>2</UID>
    </CueFactory>
    <CueRepository/>
    <ExtLinkFactory>
        <UID>1</UID>
    </ExtLinkFactory>
    <ExtLinkRepository/>
    <ExtSegmentFactory>
        <UID>1</UID>
    </ExtSegmentFactory>
    <MusicSettings>
        <BaseVolume>1</BaseVolume>
        <BaseReverbLevel>1</BaseReverbLevel>
    </MusicSettings>
    <ParameterFactory>
        <UID>1</UID>
    </ParameterFactory>
    <ParameterRepository/>
    <SceneRepository>
        <Scene ID="1">
            <CueSheet></CueSheet>
        </Scene>
    </SceneRepository>
    <SegmentRepository/>
    <SharedFile/>
    <ThemeFactory>
        <UID>1</UID>
    </ThemeFactory>
    <ThemeRepository/>
    <TimelineFactory>
        <UID>1</UID>
    </TimelineFactory>
    <TimelineRepository/>
</Composition>
"""


class WavebankInfo(BinaryObject):
    """Wavebank information from the 'Banks' view."""

    @unique
    class BankType(IntEnum):
        STREAM_FROM_DISK = 0x0080
        LOAD_INTO_MEM = 0x0200
        DECOMP_INTO_MEM = 0x0100

        def to_xml_name(self):
            return {
                self.STREAM_FROM_DISK: "Stream",
                self.LOAD_INTO_MEM: "Sample",
                self.DECOMP_INTO_MEM: "DecompressedSample",
            }[self]

    @unique
    class BankOutputFormat(IntEnum):
        PCM = 0
        ADPCM = 1
        MP3 = 2
        MP2 = 3

    STRUCT = BinaryStruct(
        ("_bank_type", "I"),
        ("max_streams", "I"),
        ("_bank_hash", "8s"),
    )

    bank_type: WavebankInfo.BankType
    max_streams: int
    bank_hash: str
    bank_name: str

    def unpack(self, reader: BinaryReader):
        kwargs = self.extract_kwargs_from_struct(reader)
        self.bank_type = self.BankType(kwargs.pop("_bank_type"))
        self.bank_hash = struct.unpack(">Q", kwargs.pop("_bank_hash"))[0]
        self.bank_name = read_string_from_length(reader)
        self.set(**kwargs)

    def __repr__(self):
        return (
            f"WaveBank(\n"
            f"    name={self.bank_name},\n"
            f"    bank_type={self.bank_type},\n"
            f"    max_streams={self.max_streams},\n"
            f"    bank_hash={self.bank_hash},\n"
            f")"
        )

    def to_xml_lines_header(self) -> list[str]:
        return [
            "<soundbank>",
            tag("name", self.bank_name),
            new_guid(),
            tag("load_into_rsx", 0),
            tag("disable_seeking", 0),
            tag("enable_syncpoints", 1),
            tag("hasbuiltwithsyncpoints", 0),
            tag("_PC_banktype", self.bank_type.to_xml_name()),
            tag("_XBOX_banktype", "DecompressedSample"),
            tag("_XBOX360_banktype", "DecompressedSample"),
            tag("_GC_banktype", "DecompressedSample"),
            tag("_PS2_banktype", "DecompressedSample"),
            tag("_PSP_banktype", "DecompressedSample"),
            tag("_PS3_banktype", "DecompressedSample"),
            tag("_WII_banktype", "DecompressedSample"),
            tag("notes"),
            tag("rebuild", 1),
        ]

    def to_xml_lines_footer(self, bank_output_format: BankOutputFormat) -> list[str]:
        console_info = [
            tag("_PC_format", bank_output_format.name),
            tag("_PC_quality", 50),
            tag("_PC_optimisesamplerate", 0),
            tag("_PC_forcesoftware", 1),
            tag("_PC_maxstreams", self.max_streams),
        ]
        for console in CONSOLES[1:]:  # PC done above
            console_info += [
                tag(f"_{console}_format", "PCM"),
                tag(f"_{console}_quality", 50),
                tag(f"_{console}_optimisesamplerate", 0),
                tag(f"_{console}_forcesoftware", 1 if console in {"XBOX360", "PS3"} else 0),
                tag(f"_{console}_maxstreams", 10),
            ]
        return console_info + ["</soundbank>"]

    @staticmethod
    def get_default_props():
        default_props = [
            "<default_soundbank_props>",
            tag("name", "default_soundbank_props"),
            new_guid(),
            tag("load_into_rsx", 0),
            tag("disable_seeking", 0),
            tag("enable_syncpoints", 1),
            tag("hasbuiltwithsyncpoints", 0),
        ]
        default_props += [tag(f"_{console}_banktype", "DecompressedSample") for console in CONSOLES]
        default_props += [
            tag("notes"),
            tag("rebuild", 0),
        ]
        for console in CONSOLES:
            default_props += [
                tag(f"_{console}_format", "PCM"),
                tag(f"_{console}_quality", 50),
                tag(f"_{console}_optimisesamplerate", 0),
                tag(f"_{console}_forcesoftware", 1 if console in {"PC", "XBOX360", "PS3"} else 0),
                tag(f"_{console}_maxstreams", 10),
            ]
        default_props += ["</default_soundbank_props>"]
        return default_props


class EventCategory(BinaryObject):
    """Event category from the 'Events' view, in the Event Categories pane.

    Used to organize Events for compile-time mixing, as opposed to Event Groups, which are used to organize Events for
    runtime referencing.
    """

    @unique
    class PlaybackBehavior(IntEnum):
        STEAL_OLDEST = 0
        STEAL_NEWEST = 1
        STEAL_QUIETEST = 2
        JUST_FAIL = 3
        JUST_FAIL_IF_QUIETEST = 4

        def to_xml_name(self):
            return {
                self.STEAL_OLDEST: "Steal_oldest",
                self.STEAL_NEWEST: "Steal_newest",
                self.STEAL_QUIETEST: "Steal_quietest",
                self.JUST_FAIL: "Just_fail",
                self.JUST_FAIL_IF_QUIETEST: "Just_fail_if_quietest",
            }[self]

    STRUCT = BinaryStruct(
        # Name comes first.
        ("volume", "f"),
        ("pitch", "f"),
        ("maxplaybacks", "I"),
        ("maxplaybacks_behavior", "I"),
        ("_subcategory_count", "I"),
    )

    name: str
    volume: float
    pitch: float
    maxplaybacks: int
    maxplaybacks_behavior: EventCategory.PlaybackBehavior
    subcategories: list[EventCategory]

    def unpack(self, reader: BinaryReader):
        self.name = read_string_from_length(reader)
        kwargs = self.extract_kwargs_from_struct(reader)
        self.subcategories = [EventCategory(reader) for _ in range(kwargs.pop("_subcategory_count"))]
        self.set(**kwargs)

    def to_xml_lines(self) -> list[str]:
        output = [
            "<eventcategory>",
            tag("name", self.name),
            new_guid(),
            tag("volume_db", field_ratio_to_decibel(self.volume)),
            tag("pitch", self.pitch / 4.0),
            tag("maxplaybacks", self.maxplaybacks),
            tag("maxplaybacks_behavior", self.maxplaybacks_behavior.to_xml_name()),
            tag("notes"),
            tag("open", 0),
        ]
        for sc in self.subcategories:
            output += sc.to_xml_lines()
        output += [
            f"</eventcategory>"
        ]
        return output


class UserProperty(BinaryObject):
    """User Property that can be attached to Layers, Event Groups, etc.

    Used to store user data that is referenced by the game's code (by name).
    """

    @unique
    class PropertyType(IntEnum):
        INTEGER = 0
        FLOATING_POINT = 1
        STRING = 2

        def get_tag(self):
            return {
                self.INTEGER: "data_int",
                self.FLOATING_POINT: "data_float",
                self.STRING: "data_string",
            }[self]

    STRUCT = BinaryStruct(
        # Name comes first.
        ("_property_type", "I"),
    )

    name: str
    property_type: UserProperty.PropertyType
    value: tp.Union[int, float, str]

    def unpack(self, reader: BinaryReader):
        self.name = read_string_from_length(reader)
        kwargs = self.extract_kwargs_from_struct(reader)
        self.property_type = self.PropertyType(kwargs.pop("_property_type"))
        if self.property_type == self.PropertyType.INTEGER:
            self.value = reader.unpack_value("i")
        elif self.property_type == self.PropertyType.FLOATING_POINT:
            self.value = reader.unpack_value("f")
        elif self.property_type == self.PropertyType.STRING:
            self.value = reader.unpack_string(offset=reader.unpack_value("I"))
        else:
            raise ValueError(f"Invalid `UserProperty.property_type`: {self.property_type}")
        # No other fields to set.

    def to_xml_lines(self) -> list[str]:
        return [
            "<userproperty>",
            tag("name", self.name),
            new_guid(),
            tag("description"),
            tag(self.property_type.get_tag(), self.value),
            "</userproperty>",
        ]


class SoundDefInstance(BinaryObject):
    """Sound Definition Instance included on Layers in Events.

    Each Sound Definition Instance is an occurrence of a base Sound Definition.
    """

    @unique
    class StartMode(IntEnum):
        IMMEDIATE = 0
        WAIT_FOR_END = 1

    @unique
    class LoopMode(IntEnum):
        LOOP_AND_CUTOFF = 0
        ONESHOT = 1
        LOOP_AND_PLAY_TO_END = 2

    @unique
    class AutopitchParameter(IntEnum):
        EVENT_PRIMARY = 0
        LAYER_CONTROL = 2

        def to_xml_name(self):
            return {
                self.EVENT_PRIMARY: "0",
                self.LAYER_CONTROL: "1",
            }[self]

    @unique
    class CrossfadeType(IntEnum):
        BEZIER = 0
        LINEAR = 1
        RAISED = 2
        POWER_05_MID = 3
        POWER_30_MID = 4
        POWER_45_MID = 5
        POWER_30_LATE = 6
        POWER_30_EARLY = 7

    index: int
    start: int
    length: int
    start_mode: SoundDefInstance.StartMode
    loop_mode: SoundDefInstance.LoopMode
    autopitch_param: SoundDefInstance.AutopitchParameter
    loop_count: int
    autopitch_enabled: int
    autopitch_reference: int
    autopitch_at_min: int
    fine_tune: int
    volume: int
    fade_in_length: int
    fade_out_length: int
    fade_in_type: SoundDefInstance.CrossfadeType
    fade_out_type: SoundDefInstance.CrossfadeType

    STRUCT = BinaryStruct(
        ("index", "H"),
        ("start", "f"),
        ("length", "f"),
        ("start_mode", "I"),
        ("loop_mode", "B"),
        ("autopitch_param", "B"),
        "2x",
        ("loop_count", "i"),
        ("autopitch_enabled", "I"),  # long bool
        ("autopitch_reference", "f"),
        ("autopitch_at_min", "f"),
        ("fine_tune", "f"),
        ("volume", "f"),
        ("fade_in_length", "f"),
        ("fade_out_length", "f"),
        ("fade_in_type", "I"),
        ("fade_out_type", "I"),
    )

    unpack = BinaryObject.default_unpack

    def to_xml_lines(self, sounddefs: list[SoundDef]) -> list[str]:
        return [
            "<sound>",
            tag("name", sounddefs[self.index].name),
            tag("x", self.start),
            tag("width", self.length),
            tag("startmode", self.start_mode.value),
            tag("loopmode", self.loop_mode.value),
            tag("loopcount2", self.loop_count),
            tag("autopitchenabled", "1" if self.autopitch_enabled else "0"),
            tag("autopitchparameter", self.autopitch_param.to_xml_name()),
            tag("autopitchreference", self.autopitch_reference),
            tag("autopitchatzero", self.autopitch_at_min),
            tag("finetune", self.fine_tune),
            tag("volume", self.volume),
            tag("fadeintype", self.fade_in_type.value),
            tag("fadeouttype", self.fade_out_type.value),
            "</sound>",
        ]


class Point(BinaryObject):
    """An `(x, y, is_first, curve_shape)` tuple that is used to describe an Envelope."""

    @unique
    class CurveShape(IntEnum):
        FLAT_ENDED = 1
        LINEAR = 2
        LOGARITHMIC = 4
        FLAT_MIDDLE = 8

    STRUCT = BinaryStruct(
        ("point_x", "f"),
        ("point_y", "f"),
        ("curve_shape", "I"),
    )

    point_x: float
    point_y: float
    curve_shape: Point.CurveShape

    def to_xml_string(self, index: int) -> str:
        is_first = "1" if index == 0 else "0"
        return tag("point", ",".join([str(self.point_x), str(self.point_y), is_first, str(self.curve_shape.value)]))


# Attached to Layers by effects. Unlike what might be expected,
#  the effect type is saved as part of all its constituent Envelopes,
#  which are attached directly to the Layer, rather than Envelopes
#  being attached to the effect, which is then attached to the Layer 
#  itself.
class Envelope(BinaryObject):
    @unique
    class EffectType(IntEnum):
        DSP_EFFECT = 0x0004
        VOLUME = 0x000c
        PITCH = 0x0014
        PAN = 0x0024
        SURROUND_PAN = 0x0048
        THREE_DIM_PAN_LEVEL = 0x0404
        THREE_DIM_SPEAKER_SPREAD = 0x0104
        OCCLUSION = 0x2004
        REVERB_LEVEL = 0x0204
        REVERB_BALANCE = 0x0804
        TIME_OFFSET = 0x0044
        SPAWN_INTENSITY = 0x1004

        def to_xml_name(self):
            return {
                self.DSP_EFFECT: "",
                self.VOLUME: "Volume",
                self.PITCH: "Pitch",
                self.PAN: "Pan",
                self.SURROUND_PAN: "Surround pan",
                self.THREE_DIM_PAN_LEVEL: "3D Pan Level",
                self.THREE_DIM_SPEAKER_SPREAD: "3D Speaker spread",
                self.OCCLUSION: "Occlusion",
                self.REVERB_LEVEL: "Reverb Level",
                self.REVERB_BALANCE: "Reverb Balance",
                self.TIME_OFFSET: "Time offset",
                self.SPAWN_INTENSITY: "Spawn Intensity",
            }[self]

    STRUCT = BinaryStruct(
        # Parent index and name come first.
        ("effect_parameter_index", "I"),
        ("_combined_flags", "I"),
        "4x",
        ("_point_count", "I"),
    )

    STRUCT_2 = BinaryStruct(
        ("control_parameter_index", "I"),
        ("mapping_method", "I"),
    )

    parent_index: int
    name: str
    effect_parameter_index: int
    effect: Envelope.EffectType
    is_muted: bool
    flags: int
    points: list[Point]
    control_parameter_index: int
    mapping_method: int

    def unpack(self, reader: BinaryReader, encoding=None, byte_order=None):
        self.parent_index = reader.unpack_value("i")
        self.name = read_string_from_length(reader)
        kwargs = self.extract_kwargs_from_struct(reader, self.STRUCT, encoding, byte_order)
        combined_flags = kwargs.pop("_combined_flags")
        self.effect = self.EffectType(combined_flags & ~0x01 & 0xFFFF)
        self.is_muted = bool(combined_flags & 0x01)
        self.flags = combined_flags & ~0xFFFF
        self.points = [Point(reader) for _ in range(kwargs.pop("_point_count"))]
        kwargs |= self.extract_kwargs_from_struct(reader, self.STRUCT_2, encoding, byte_order)
        self.set(**kwargs)

    def to_xml_lines(self, envelope_name: str, envelopes: list[Envelope], parameters: list[Parameter]) -> list[str]:
        """Get XML representation of Envelope.

        In normal use, effect envelopes are given a unique color upon creation, but this color is not important to the
        event data and is not saved in the FEV. Because of this, Envelopes all default to the same color  which can then
        be manually set by the user should the need arise.

        Args:
            envelope_name: the name that this Envelope should be given in the FDP data, since this name is not saved to
                the FEV and must be recreated.
            envelopes: list of all Envelopes attached to the Layer this Envelope is attached to. Envelopes are grouped
                into effects, and need to index this list to determine their master Envelope which holds the effect
                information.
            parameters: list of all Parameters attached to the Event to which this Envelope's Layer is attached.
                Envelopes are controlled by some Parameter, and index this list to determine information about that
                Parameter.
        """
        envelope = envelopes[self.parent_index] if self.parent_index != -1 else self
        dsp_name = envelope.effect.to_xml_name() if envelope.effect != self.EffectType.DSP_EFFECT else envelope.name
        layer_enables = [tag(f"_{console}_enable", 1) for console in CONSOLES]

        return [
           "<envelope>",
           tag("name", envelope_name),
           tag("dsp_name", dsp_name),
           tag("dsp_paramindex", self.effect_parameter_index),
           tag("colour", "#7f0000")  # NOTE: all use the same default color. TODO: randomize for variety?
               ] + [point.to_xml_string(i) for i, point in enumerate(self.points)] + [
           tag("parametername", parameters[0].name),
           tag("controlparameter", parameters[self.control_parameter_index].name)
               ] + layer_enables + [
           tag("mute", "1" if self.is_muted else "0"),
           tag("visible", "1"),
           tag("hidden", "0"),
           tag("fromtemplate", "No"),
           tag("mappingmethod", self.mapping_method),
           tag("flags", self.flags),
           tag("exflags", "0"),
           "</envelope>",
               ]


class Layer(BinaryObject):
    """Holds Sound Definition Instances, so that a single event may play several at the same time for the same control
    parameter value.
    """

    COMPLEX_STRUCT = BinaryStruct(
        ("signature", "2s", b"\x02\x00"),
        ("priority", "h"),
        ("control_parameter", "h"),
    )

    STRUCT = BinaryStruct(
        ("_sounddef_instance_count", "H"),
        ("_envelope_count", "H"),
    )

    priority: int
    control_parameter: int
    sounddef_instances: list[SoundDefInstance]
    envelopes: list[Envelope]

    def unpack(self, reader: BinaryReader, event_type: Event.EventType = None):
        if event_type == Event.EventType.COMPLEX:
            complex_data = reader.unpack_struct(self.COMPLEX_STRUCT, exclude_asserted=True)
            self.priority = complex_data["priority"]
            self.control_parameter = complex_data["control_parameter"]
        else:
            self.priority = -1
            self.control_parameter = -1
        data = reader.unpack_struct(self.STRUCT)
        self.sounddef_instances = [SoundDefInstance(reader) for _ in range(data["_sounddef_instance_count"])]
        self.envelopes = [Envelope(reader) for _ in range(data["_envelope_count"])]
        # No other fields to set.

    def to_xml_lines(self, layer_name: str, parameters: list[Parameter], sounddefs: list[SoundDef]) -> list[str]:
        """XML string for `Layer`, including all attached SoundDefInstances and Envelopes.

        Args:
            layer_name: name that should be given to this layer in the FDP, since this data is not saved into the FEV
                and must be recreated.
            parameters: list of Parameters from this Layer's Event, since the Layer indexs this list to determine its
                control parameter.
            sounddefs: list of SoundDefs found in the FEV containing this Layer's Event. SoundDefInstances attached to
                this Layer index this list.
        """
        xml_lines = [
            "<layer>",
            tag("name", layer_name),
            tag("height", 100),
            tag("envelope_nextid", 0),
            tag("mute", 0),
            tag("solo", 0),
            tag("soundlock", 0),
            tag("envlock", 0),
            tag("priority", self.priority),
        ]
        if self.control_parameter != -1:
            xml_lines += [tag("controlparameter", parameters[self.control_parameter].name)]
        for sdi in self.sounddef_instances:
            xml_lines += sdi.to_xml_lines(sounddefs)
        for i, envelope in enumerate(self.envelopes):
            xml_lines += envelope.to_xml_lines(f"parsed_envelope{i}", self.envelopes, parameters)
        xml_lines += [tag(f"_{console}_enable", 1) for console in CONSOLES]
        xml_lines += ["</layer>"]
        return xml_lines


class Parameter(BinaryObject):
    """Provides functionality to adjust playback characteristics of an Event in real-time during the game."""

    @unique
    class LoopBehavior(IntEnum):
        ONESHOT = 2
        ONESHOT_AND_STOP = 4
        LOOP = 8

        def to_xml_name(self):
            return {
                self.ONESHOT: "0",
                self.ONESHOT_AND_STOP: "1",
                self.LOOP: "2",
            }[self]

    name: str
    velocity: float
    param_min: float
    param_max: float
    is_primary: bool
    loop_behavior: Parameter.LoopBehavior
    seek_speed: float
    controlled_envelope_count: int

    STRUCT = BinaryStruct(
        # Name comes first.
        ("velocity", "f"),
        ("param_min", "f"),
        ("param_max", "f"),
        ("_param_info", "I"),
        ("seek_speed", "f"),
        ("controlled_envelope_count", "I"),
        "4x",
    )

    def unpack(self, reader: BinaryReader):
        self.name = read_string_from_length(reader)
        kwargs = self.extract_kwargs_from_struct(reader, self.STRUCT)
        param_info = kwargs.pop("_param_info")
        self.is_primary = bool(param_info & 0x01)
        self.loop_behavior = self.LoopBehavior(param_info & ~0x01)
        self.set(**kwargs)

    def to_xml_lines(self) -> list[str]:
        """

        The parameter ruler spacing is not needed by the event data, so it is not saved to the FEV. We set the spacing
        to be in 10% intervals, and it can later be changed by the user to their liking.

        TODO: Better default spacing that matches what From typically uses.
        """
        return [
            "<parameter>",
            tag("name", self.name),
            new_guid(),
            tag("primary", "1" if self.is_primary else "0"),
            tag("loopmode", self.loop_behavior.to_xml_name()),
            tag("rangeunits"),
            tag("rangemin", self.param_min),
            tag("rangemax", self.param_max),
            tag("rangespacing", (self.param_max - self.param_min) / 10.0),
            tag("keyoffonsilence", "0"),
            tag("velocity", self.velocity),
            tag("seekspeed", self.seek_speed),
            "</parameter>",
        ]


class Event(BinaryObject):
    """Core class of the FMOD Sound Event system.

    Responsible for packaging sound information that can be requested in-game. The playback of events is handled by
    FMOD. Events and their folders (Event Groups) are shown in the Events view, in the Event Groups pane. Each Event
    also belongs to an Event Category, which is shown in the same view in the Event Categories pane.
    """

    @unique
    class EventType(IntEnum):
        SIMPLE = 0x10
        COMPLEX = 0x08

    @unique
    class EventMode(IntEnum):
        TWO_DIM = 0x08
        THREE_DIM = 0x10

        def to_xml_name(self):
            return {
                self.TWO_DIM: "x_2d",
                self.THREE_DIM: "x_3d",
            }[self]

    @unique
    class ThreeDimRolloff(IntEnum):
        LOGARITHMIC = 0x0010
        LINEAR = 0x0020
        CUSTOM = 0x0400

        def to_xml_name(self):
            return {
                self.LOGARITHMIC: "Logarithmic",
                self.LINEAR: "Linear",
                self.CUSTOM: "Custom",
            }[self]

    @unique
    class ThreeDimPosition(IntEnum):
        HEAD_RELATIVE = 0x04
        WORLD_RELATIVE = 0x08

        def to_xml_name(self):
            return {
                self.HEAD_RELATIVE: "Head_relative",
                self.WORLD_RELATIVE: "World_relative",
            }[self]

    @unique
    class PitchUnits(IntEnum):
        OCTAVES = 0x00
        SEMITONES = 0x40
        TONES = 0x80

        def to_xml_name(self):
            return {
                self.OCTAVES: "Octaves",
                self.SEMITONES: "Semitones",
                self.TONES: "Tones",
            }[self]

    @unique
    class PlaybackBehavior(IntEnum):
        """Different from the enum used by `EventCategory`, for some reason."""
        STEAL_OLDEST = 1
        STEAL_NEWEST = 2
        STEAL_QUIETEST = 3
        JUST_FAIL = 4
        JUST_FAIL_IF_QUIETEST = 5

        def to_xml_name(self):
            return {
                self.STEAL_OLDEST: "Steal_oldest",
                self.STEAL_NEWEST: "Steal_newest",
                self.STEAL_QUIETEST: "Steal_quietest",
                self.JUST_FAIL: "Just_fail",
                self.JUST_FAIL_IF_QUIETEST: "Just_fail_if_quietest",
            }[self]

    name: str
    guid: str
    volume: float
    pitch: float
    pitch_rand: float
    volume_rand: float
    priority: int
    max_playbacks: int
    steal_priority: int
    mode: Event.EventMode
    ignore_geometry: bool
    three_dim_rolloff: Event.ThreeDimRolloff
    three_dim_position: Event.ThreeDimPosition
    three_dim_min_dist: float
    three_dim_max_dist: float
    oneshot: bool
    pitch_rand_units: Event.PitchUnits
    speaker_l: float
    speaker_r: float
    speaker_c: float
    speaker_lfe: float
    speaker_lr: float
    speaker_rr: float
    speaker_ls: float
    speaker_rs: float
    cone_inside_angle: float
    cone_outside_angle: float
    cone_outside_volume: float
    max_playback_behavior: Event.PlaybackBehavior
    doppler_factor: float
    reverb_dry: float
    reverb_wet: float
    speaker_spread: float
    fadein_time: int
    fadeout_time: int
    spawn_intensity: float
    spawn_intensity_rand: float
    pan_level: float
    position_rand: int
    layers: list[Layer]
    parameters: list[Parameter]
    user_properties: list[UserProperty]
    category_names: list[str]

    STRUCT = BinaryStruct(
        # Event type and name come first.
        ("_guid", "16s"),
        ("volume", "f"),
        ("pitch", "f"),
        ("volume_rand", "f"),
        ("pitch_rand", "f"),
        ("priority", "I"),
        ("max_playbacks", "I"),
        ("steal_priority", "i"),
        ("_mode", "H"),
        ("_geom_flags", "H"),
        ("three_dim_min_dist", "f"),
        ("three_dim_max_dist", "f"),
        "2x",
        ("_oneshot", "B"),
        ("_pitch_rand_units", "B"),
        ("speaker_l", "f"),
        ("speaker_r", "f"),
        ("speaker_c", "f"),
        ("speaker_lfe", "f"),
        ("speaker_lr", "f"),
        ("speaker_rr", "f"),
        ("speaker_ls", "f"),
        ("speaker_rs", "f"),
        ("cone_inside_angle", "f"),
        ("cone_outside_angle", "f"),
        ("cone_outside_volume", "f"),
        ("_max_playback_behavior", "I"),
        ("doppler_factor", "f"),
        ("reverb_dry", "f"),
        ("reverb_wet", "f"),
        ("speaker_spread", "f"),
        ("fadein_time", "I"),
        ("fadeout_time", "I"),
        ("spawn_intensity", "f"),
        ("spawn_intensity_rand", "f"),
        ("pan_level", "f"),
        ("position_rand", "I"),
    )

    def unpack(self, reader: BinaryReader):
        event_type = self.EventType(reader.unpack_value("I"))
        self.name = read_string_from_length(reader)
        print(f"EVENT NAME: {self.name}")
        kwargs = self.extract_kwargs_from_struct(reader)
        raw_guid = kwargs.pop("_guid")
        self.guid = "-".join((
            raw_guid[3::-1].hex(),  # first three chunks need to be reversed
            raw_guid[5:3:-1].hex(),
            raw_guid[7:5:-1].hex(),
            raw_guid[8:10].hex(),
            raw_guid[10:].hex(),
        ))
        self.mode = self.EventMode(kwargs.pop("_mode"))
        geom_flags = kwargs.pop("_geom_flags")
        self.ignore_geometry = geom_flags & 0xF000 == 0x4000
        self.three_dim_rolloff = self.ThreeDimRolloff(geom_flags & 0x0FF0)
        self.three_dim_position = self.ThreeDimPosition(geom_flags & 0x00F)
        self.oneshot = kwargs.pop("_oneshot") == 0x08
        self.pitch_rand_units = self.PitchUnits(kwargs.pop("_pitch_rand_units"))
        self.max_playback_behavior = self.PlaybackBehavior(kwargs.pop("_max_playback_behavior"))

        layer_count = reader.unpack_value("I") if event_type == Event.EventType.COMPLEX else 1
        self.layers = [Layer(reader, event_type=event_type) for _ in range(layer_count)]

        self.parameters = []
        self.user_properties = []
        if event_type == Event.EventType.COMPLEX:
            param_count = reader.unpack_value("I")
            self.parameters = [Parameter(reader) for _ in range(param_count)]
            user_prop_count = reader.unpack_value("I")
            self.user_properties = [UserProperty(reader) for _ in range(user_prop_count)]
        category_name_count = reader.unpack_value("I")
        self.category_names = [read_string_from_length(reader) for _ in range(category_name_count)]

        self.set(**kwargs)

    def to_xml_lines(self, sounddefs) -> list[str]:
        """XML string for Event class, including Layers, Parameters, and User Properties.

        Args:
            sounddefs: list of SoundDefs from the FEV that this Event is contained in. SoundDefInstances from Layers in
            this Event reference these SoundDefs.
        """
        xml_lines = [
            "<event>",
            tag("name", self.name),
            tag("guid", "{" + self.guid + "}"),
            tag("parameter_nextid", "0"),
            tag("layer_nextid", "0"),
        ]
        for i, layer in enumerate(self.layers):
            xml_lines += layer.to_xml_lines(f"parsed_layer{i}", self.parameters, sounddefs)
        for param in self.parameters:
            xml_lines += param.to_xml_lines()
        xml_lines += [
            tag("car_rpm", 0),
            tag("car_rpmsmooth", 0.075),
            tag("car_loadsmooth", 0.05),
            tag("car_loadscale", 6),
            tag("car_dialog", 0),
            tag("volume_db", field_ratio_to_decibel(self.volume)),
            tag("pitch", self.pitch / 4.0),
            tag("pitch_units", self.pitch_rand_units.to_xml_name()),  # used in place of lost pitch units
            tag("pitch_randomization", self.pitch_rand / 4.0),
            tag("pitch_randomization_units", self.pitch_rand_units.to_xml_name()),
            tag("volume_randomization", field_ratio_to_decibel(1 - self.volume_rand)),
            tag("priority", self.priority),
            tag("maxplaybacks", self.max_playbacks),
            tag("maxplaybacks_behavior", self.max_playback_behavior.to_xml_name()),
            tag("stealpriority", self.steal_priority),
            tag("mode", self.mode.to_xml_name()),
            tag("ignoregeometry", "Yes" if self.ignore_geometry else "No"),
            tag("rolloff", self.three_dim_rolloff.to_xml_name()),
            tag("mindistance", self.three_dim_min_dist),
            tag("maxdistance", self.three_dim_max_dist),
            tag("headrelative", self.three_dim_position.to_xml_name()),
            tag("oneshot", "Yes" if self.oneshot else "No"),
            tag("istemplate", "No"),
            tag("usetemplate"),
            tag("notes"),
        ]
        for user_prop in self.user_properties:
            xml_lines += user_prop.to_xml_lines()
        xml_lines += [
            tag("category", self.category_names[0]),
            tag("position_randomization", self.position_rand),
            tag("speaker_l", self.speaker_l),
            tag("speaker_c", self.speaker_c),
            tag("speaker_r", self.speaker_r),
            tag("speaker_ls", self.speaker_ls),
            tag("speaker_rs", self.speaker_rs),
            tag("speaker_lb", self.speaker_lr),
            tag("speaker_rb", self.speaker_rr),
            tag("speaker_lfe", self.speaker_lfe),
            tag("speaker_config", "0"),
            tag("speaker_pan_r", "1"),
            tag("speaker_pan_theta", "0"),
            tag("cone_inside_angle", self.cone_inside_angle),
            tag("cone_outside_angle", self.cone_outside_angle),
            tag("cone_outside_volumedb", field_ratio_to_decibel(self.cone_outside_volume)),
            tag("doppler_scale", self.doppler_factor),
            tag("reverbdrylevel_db", self.reverb_dry),
            tag("reverblevel_db", self.reverb_wet),
            tag("speaker_spread", self.speaker_spread),
            tag("panlevel3d", self.pan_level),
            tag("fadein_time", self.fadein_time),
            tag("fadeout_time", self.fadeout_time),
            tag("spawn_intensity", self.spawn_intensity),
            tag("spawn_intensity_randomization", self.spawn_intensity_rand),
        ]
        xml_lines += [tag(f"TEMPLATE_PROP_{prop_name}", 1) for prop_name in TEMPLATE_PROPS]
        xml_lines += ["</event>"]
        return xml_lines


class EventGroup(BinaryObject):
    """Folders used to organize Events for more convenient referencing in-game.

    Unlike Event Categories, which are used to organize compile-time mixing of Events, Event Groups are used to organize
    Events in-game.
    """

    STRUCT = BinaryStruct(
        # Name comes first.
        ("_user_property_count", "I"),
        ("_subgroup_count", "I"),
        ("_event_count", "I"),
    )

    name: str
    user_properties: list[UserProperty]
    subgroups: list[EventGroup]
    events: list[Event]

    def unpack(self, reader: BinaryReader):
        self.name = read_string_from_length(reader)
        print(f"EVENT GROUP NAME: {self.name}")
        kwargs = self.extract_kwargs_from_struct(reader, self.STRUCT)
        self.user_properties = [UserProperty(reader) for _ in range(kwargs.pop("_user_property_count"))]
        self.subgroups = [EventGroup(reader) for _ in range(kwargs.pop("_subgroup_count"))]
        self.events = [Event(reader) for _ in range(kwargs.pop("_event_count"))]
        self.set(**kwargs)

    def to_xml_lines(self, sounddefs: list[SoundDef]) -> list[str]:
        xml_lines = [
            "<eventgroup>",
            tag("name", self.name),
            new_guid(),
            tag("eventgroup_nextid", "0"),
            tag("event_nextid", "0"),
            tag("open", "0"),
            tag("notes"),
        ]
        for user_prop in self.user_properties:
            xml_lines += user_prop.to_xml_lines()
        for subgroup in self.subgroups:
            xml_lines += subgroup.to_xml_lines(sounddefs)
        for event in self.events:
            xml_lines += event.to_xml_lines(sounddefs)
        xml_lines += [
            "</eventgroup>"
        ]
        return xml_lines


class SoundDefProperty(BinaryObject):
    """Properties that can be set about a Sound Definition in the Sound Definitions view.

    To save space, these collections of properties are saved seperate from the SoundDef itself in the FEV, so that
    multiple SoundDefs can reference the same SoundDefProperty.
    """

    @unique
    class PlayMode(IntEnum):
        SEQUENTIAL = 0
        RANDOM = 1
        RANDOM_NO_REPEAT = 2
        SEQUENTIAL_EVENT_RESTART = 3
        SHUFFLE = 4
        PROGRAMMER_SELECTED = 5
        SHUFFLE_GLOBAL = 6

        def to_xml_name(self):
            return {
                self.SEQUENTIAL: "sequentialnoeventrestart",
                self.RANDOM: "random",
                self.RANDOM_NO_REPEAT: "randomnorepeat",
                self.SEQUENTIAL_EVENT_RESTART: "sequential",
                self.SHUFFLE: "shuffle",
                self.PROGRAMMER_SELECTED: "programmerselected",
                self.SHUFFLE_GLOBAL: "shuffleglobal",
            }[self]

    @unique
    class RecalculateRand(IntEnum):
        EVERY_SPAWN = 0
        ON_TRIGGER = 1
        ON_START = 2

    play_mode: SoundDefProperty.PlayMode
    spawn_time_min: int
    spawn_time_max: int
    max_spawned: int
    volume: float
    volume_randmethod: int
    volume_randmin: float
    volume_randmax: float
    volume_rand: float
    pitch: float
    pitch_randmethod: int
    pitch_randmin: float
    pitch_randmax: float
    pitch_rand: float
    recalc_pitch_rand: SoundDefProperty.RecalculateRand
    three_dim_position_rand: float

    STRUCT = BinaryStruct(
        ("_play_mode", "I"),
        ("spawn_time_min", "I"),
        ("spawn_time_max", "I"),
        ("max_spawned", "I"),
        ("volume", "f"),
        ("volume_randmethod", "I"),
        ("volume_randmin", "f"),
        ("volume_randmax", "f"),
        ("volume_rand", "f"),
        ("pitch", "f"),
        ("pitch_randmethod", "I"),
        ("pitch_randmin", "f"),
        ("pitch_randmax", "f"),
        ("pitch_rand", "f"),
        ("_recalc_pitch_rand_value", "I"),
        ("three_dim_position_rand", "f"),
    )

    def unpack(self, reader: BinaryReader):
        kwargs = self.extract_kwargs_from_struct(reader)
        self.play_mode = self.PlayMode(kwargs.pop("_play_mode"))
        self.recalc_pitch_rand = self.RecalculateRand(kwargs.pop("_recalc_pitch_rand_value"))
        self.set(**kwargs)

    def to_xml_lines(self) -> list[str]:
        """Chunk of data to be inserted into a `SoundDef`."""
        return [
            tag("type", self.play_mode.to_xml_name()),
            tag("spawntime_min", self.spawn_time_min),
            tag("spawntime_max", self.spawn_time_max),
            tag("spawn_max", self.max_spawned),
            tag("mode", "0"),
            tag("pitch", self.pitch / 4.0),
            tag("pitch_randmethod", self.pitch_randmethod),
            tag("pitch_random_min", self.pitch_randmin / 4.0),
            tag("pitch_random_max", self.pitch_randmax / 4.0),
            tag("pitch_randomization", self.pitch_rand / 4.0),
            tag("pitch_recalculate", self.recalc_pitch_rand.value),
            tag("volume_db", field_ratio_to_decibel(self.volume)),
            tag("volume_randmethod", self.volume_randmethod),
            tag("volume_random_min", field_ratio_to_decibel(self.volume_randmin)),
            tag("volume_random_max", field_ratio_to_decibel(self.volume_randmax)),
            tag("volume_randomization", field_ratio_to_decibel(self.volume_rand)),
            tag("position_randomization", self.three_dim_position_rand),
        ]


class Waveform(BinaryObject):
    """Container for FEV-specific information about the wavetables found in a given wavebank.

    The audio data and specific format information before and after compression is saved into the FSB instead.
    """

    STRUCT = BinaryStruct(
        # 4x, weight, name, and bank name come first.
        ("index_in_bank", "I"),
        ("playtime", "I"),
    )

    weight: int
    name: str
    bank_name: str
    index_in_bank: int
    playtime: int

    def unpack(self, reader: BinaryReader):
        reader.assert_pad(4)
        self.weight = reader.unpack_value("I")
        self.name = read_string_from_length(reader)
        self.bank_name = read_string_from_length(reader)
        kwargs = self.extract_kwargs_from_struct(reader)
        self.set(**kwargs)

    def to_xml_lines(self) -> list[str]:
        """Note that `playtime` is not stored in the FDP XML."""
        return [
            "<waveform>",
            tag("filename", self.name),
            tag("soundbankname", self.bank_name),
            tag("weight", self.weight),
            tag("percentagelocked", "0"),
            "</waveform>",
        ]


class SoundDef(BinaryObject):
    """Container for sound-producing entities (e.g. wavetables)."""

    name: str
    sounddef_prop_index: int
    waveforms: list[Waveform]

    STRUCT = BinaryStruct(
        # Name comes first.
        ("sounddef_prop_index", "I"),
        ("_waveform_count", "I"),
    )

    def unpack(self, reader: BinaryReader):
        self.name = read_string_from_length(reader)
        print(f"SOUND DEF NAME: {self.name}")
        kwargs = self.extract_kwargs_from_struct(reader, self.STRUCT)
        self.waveforms = [Waveform(reader) for _ in range(kwargs.pop("_waveform_count"))]
        self.set(**kwargs)

    def to_xml_lines(self, sounddef_properties_list: list[SoundDefProperty]) -> list[str]:
        xml_lines = [
            "<sounddef>",
            tag("name", self.name),
            new_guid(),
        ]
        xml_lines += sounddef_properties_list[self.sounddef_prop_index].to_xml_lines()
        xml_lines += [
            tag("notes"),
        ]
        for wf in self.waveforms:
            xml_lines += wf.to_xml_lines()
        xml_lines += [
            "</sounddef>",
        ]
        return xml_lines


class SoundDefFolder:
    """Path-like container for `SoundDef`s.

    Unlike other objects, this is not saved into the FEV or FSB. Instead, the folder hierarchy of SoundDefFolders and
    SoundDefs must be reconstructed from the flattened filepaths of the SoundDefs.
    """

    name: str
    subfolders: dict[str, SoundDefFolder]
    sounddefs: list[SoundDef]

    def __init__(self, name: str):
        self.name = name
        self.subfolders = {}
        self.sounddefs = []

    def add_new_sounddef(self, sounddef_path: str, sounddef: SoundDef):
        """Adds a `SoundDef` as a (possibly indirect) child of this SoundDefFolder.

        New sub-SoundDefFolders will be created as necessary to reach `sounddef_path`, which is a Unix-style path
        relative to this folder. That is, the path must either start with the path separator '/' to signify that the
        SoundDef is contained in a sub-SoundDefFolder, or must contain no path separators at all.
        """
        split_path = sounddef_path.split("/")
        if len(split_path) == 2:  # this folder is correct
            self.sounddefs.append(sounddef)
        elif split_path[0] == "":  # path starts with "/"
            folder_name = split_path.pop(1)
            subpath = "/".join(split_path)
            subfolder = self.subfolders.setdefault(folder_name, SoundDefFolder(folder_name))
            subfolder.add_new_sounddef(subpath, sounddef)
        else:
            raise ValueError(f"Path '{sounddef_path}' is not relative to SoundDefFolder '{self.name}'.")

    def to_xml_lines(self, sounddef_properties_list: list[SoundDefProperty]) -> list[str]:
        """XML representation of the SoundDefFolder as it appears in the FDP.

        Recursively includes all contained SoundDefFolders and SoundDefs.

        Args:
            sounddef_properties_list is the list of SoundDefPropertys parsed from the FEV that held the contained
            SoundDefs. SoundDefs index this list to determine their properties.
        """
        xml_lines = [
            "<sounddeffolder>",
            tag("name", self.name),
            new_guid(),
            tag("open", "0"),
        ]
        for sf in self.subfolders.values():
            xml_lines += sf.to_xml_lines(sounddef_properties_list)
        for sounddef in self.sounddefs:
            xml_lines += sounddef.to_xml_lines(sounddef_properties_list)
        xml_lines += [
            "</sounddeffolder>",
        ]
        return xml_lines


class FEV(GameFile):
    """FMOD Event file that holes all event data about an FMOD project.

    Sister to FSB files, which hold the actual sound sample data (banks).
    """

    version_byte: int
    unk_offset1: int
    unk_offset2: int
    project_name: str
    wavebanks: list[WavebankInfo]
    top_event_category: EventCategory
    top_event_groups: list[EventGroup]
    sounddef_properties: list[SoundDefProperty]
    sounddefs: list[SoundDef]

    STRUCT = BinaryStruct(
        ("signature", "4s", b"FEV1"),
        ("version_byte", "I"),
        ("unk_offset1", "I"),
        ("unk_offset2", "I"),
        # Project name.
    )

    def unpack(self, reader: BinaryReader, **kwargs):
        data = reader.unpack_struct(self.STRUCT)
        self.version_byte = data.pop("version_byte")
        self.unk_offset1 = data.pop("unk_offset1")
        self.unk_offset2 = data.pop("unk_offset2")
        self.project_name = read_string_from_length(reader)

        print("PROJECT NAME:", self.project_name)

        wavebank_count = reader.unpack_value("I")
        self.wavebanks = [WavebankInfo(reader) for _ in range(wavebank_count)]

        self.top_event_category = EventCategory(reader)

        top_event_group_count = reader.unpack_value("I")
        self.top_event_groups = [EventGroup(reader) for _ in range(top_event_group_count)]

        sounddef_prop_count = reader.unpack_value("I")
        self.sounddef_properties = [SoundDefProperty(reader) for _ in range(sounddef_prop_count)]

        sounddef_count = reader.unpack_value("I")
        self.sounddefs = [SoundDef(reader) for _ in range(sounddef_count)]

        # TODO: Reverb?
        reader.assert_pad(4)

        # TODO: Music block?
        music_block_size = reader.unpack_value("I")
        reader.seek(music_block_size, 1)

    def pack(self):
        raise ValueError("FEV pack not implemented. Use FMOD Designer to build FEV/FSB from the generated FDP.")

    def to_xml_lines_start(self) -> list[str]:
        """Start of FDP XML contribution from FEV.

        Subsequent chunks are found from Wavebanks referenced by the FSB. Finally, `to_xml_lines_end()` below should be
        called.
        """
        xml_lines = [
            "<project>",
            tag("name", self.project_name),
            new_guid(),
            tag("version", 4),
            tag("eventgroup_nextid", 0),
            tag("soundbank_nextid", 0),
            tag("sounddef_nextid", 0),
            tag("build_project", 1),
            tag("build_headerfile", 0),
            tag("build_banklists", 0),
            tag("build_programmerreport", 0),
            tag("build_applytemplate", 0),
        ]
        if self.wavebanks:
            xml_lines += [tag("currentbank", self.wavebanks[0].bank_name)]
        xml_lines += [
            tag("currentlanguage", "default"),
            tag("primarylanguage", "default"),
            tag("language", "default"),
            tag("templatefilename"),
            tag("templatefileopen", 1),
        ]
        # Handle Event Categories. The top-level master category is not included.
        for event_category in self.top_event_category.subcategories:
            xml_lines += event_category.to_xml_lines()
        # Handle Sounddefs
        #  Build Sounddef directory structure and populate it with the Sounddefs
        master_sounddeffolder = SoundDefFolder("master")
        for sd in self.sounddefs:
            master_sounddeffolder.add_new_sounddef(sd.name, sd)
        xml_lines += master_sounddeffolder.to_xml_lines(self.sounddef_properties)
        # Handle Event Groups.
        for event_group in self.top_event_groups:
            xml_lines += event_group.to_xml_lines(self.sounddefs)
        xml_lines += WavebankInfo.get_default_props()
        return xml_lines

    @staticmethod
    def to_xml_lines_end() -> list[str]:
        """Last part of FDP XML."""
        project_footer = [
            tag("notes"),
            tag("currentplatform", "PC"),
        ]
        for console in CONSOLES:
            project_footer += [
                tag(f"_{console}_encryptionkey"),
                tag(f"_{console}_builddirectory"),
                tag(f"_{console}_audiosourcedirectory"),
                tag(f"_{console}_prebuildcommands"),
                tag(f"_{console}_postbuildcommands"),
                tag(f"_{console}_buildinteractivemusic", "Yes"),
            ]
        project_footer += [
            tag("presavecommands"),
            tag("postsavecommands"),
            tag("neweventusetemplate", 0),
            tag("neweventlasttemplatename"),
        ]
        project_footer += PROJECT_FOOTER_COMPOSITION.splitlines()
        project_footer += ["</project>"]
        return project_footer
