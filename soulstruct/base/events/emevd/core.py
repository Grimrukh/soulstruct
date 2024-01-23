from __future__ import annotations

__all__ = ["EMEVD"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.dcx import DCXType
from soulstruct.utilities.binary import *

from .event import Event as BaseEvent, EventSignature
from .event_layers import EventLayers
from .exceptions import EMEVDError
from .numeric import build_numeric

if tp.TYPE_CHECKING:
    from soulstruct.base.events.emevd.evs import EVSParser
    from soulstruct.base.game_types.game_enums_manager import GameEnumsManager

try:
    Self = tp.Self
except AttributeError:  # < Python 3.11
    Self = "EMEVD"

_LOGGER = logging.getLogger("soulstruct")

_EVENT_CALL_RE = re.compile(r"( *)(Event|CommonFunc)_(\d+)\(([\d\-,. \n]+)\) *(\n|$)?")


@dataclass(slots=True)
class EMEVDHeaderStruct(BinaryStruct):
    """Indicates fields that will always be present in this header, but cannot be used."""
    _signature: bytes = field(init=False, **BinaryString(4, asserted=b"EVD"))
    big_endian: bool
    varint_size_check: sbyte = field(**Binary(asserted=[-1, 0]))  # -1 if True, 0 if False
    version_unk_1: bool
    version_unk_2: sbyte
    version: uint
    file_size: uint
    events_count: varuint
    events_offset: varuint
    instructions_count: varuint
    instructions_offset: varuint
    _unknown_count: varuint = field(init=False, **Binary(asserted=0))  # unused in all games
    unknown_offset: varuint  # unused in all games (but still an offset, at `base_arg_data_offset`)
    event_layers_count: varuint
    event_layers_offset: varuint
    event_arg_replacements_count: varuint
    event_arg_replacements_offset: varuint
    linked_files_count: varuint
    linked_files_offset: varuint
    base_arg_data_size: varuint
    base_arg_data_offset: varuint
    packed_strings_size: varuint
    packed_strings_offset: varuint
    # TODO: only in 32-bit versions (PTDE, DSR). Can maybe just do a `pad_align(8)` to save the struct subclasses.
    # _pad2: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class EMEVD(GameFile, abc.ABC):
    """Packed list of "event scripts" that are loaded in a particular map, or all maps ("common").

    Event scripts 50 and 0 are run automatically, in that order. All other scripts are called from them, sometimes
    with a certain slot and set of arguments. Scripts are executed asynchronously and frequently wait for certain
    groups of conditions to be true before continuing. Entities in map MSBs are referenced by their entity ID; param
    IDs and other various internal IDs (sounds, visual effects, etc.) are also frequently referenced.

    Whenever a script finishes (or restarts), the flag with the same ID as that script (plus its `slot` number) is
    enabled. Event IDs are therefore almost always in dedicated ranges for that map, with the format:
        `1AABX***`
    where the map ID is `mAA_0B_00_00`, X is 0-5, and * is anything. Flags of this format where X is 4 or 5 are
    automatically disabled each time the game loads; flags where X is 0-3 are persistent and saved to your game
    file.

    If your `emevd_source` is a Python-like EVS script that uses any relative imports, you must pass
    `script_directory` to this class so those relative imports can be resolved. (If the EVS script is a path source,
    `script_directory` can be detected automatically.)
    """

    EVENT_CLASS: tp.ClassVar[type[BaseEvent]]
    ENTITY_ENUMS_MANAGER: tp.ClassVar[type[GameEnumsManager]]
    EVS_PARSER: tp.ClassVar[type[EVSParser]]
    STRING_ENCODING: tp.ClassVar[str]
    HEADER_VERSION_INFO: tp.ClassVar[tuple[bool, int, int]] = (False, 0, 204)  # DS1 default

    events: dict[int, BaseEvent] = field(default_factory=dict)
    packed_strings: bytes = b""
    # TODO: Should actually read the linked strings so they can be modified.
    #  But then I'd have to check all packed strings used by logging instructions as well...
    linked_file_offsets: list[int] = field(default_factory=list)
    map_name: str = ""

    # Internal usage.
    byte_order: ByteOrder = field(repr=False, default=ByteOrder.LittleEndian)
    long_varints: bool = field(repr=False, default=False)
    event_signatures: dict[int, EventSignature] = field(repr=False, default=dict)

    # region Numeric/EVS Read Methods

    @classmethod
    def from_numeric_string(cls, numeric_string: str, map_name: str = "") -> Self:
        events, linked_file_offsets, packed_strings = build_numeric(numeric_string, cls.EVENT_CLASS)
        emevd = cls(
            events=events, packed_strings=packed_strings, linked_file_offsets=linked_file_offsets, map_name=map_name
        )
        return emevd

    @classmethod
    def from_numeric_path(cls, numeric_path: Path | str, map_name: str = "") -> Self:
        return cls.from_numeric_string(numeric_path.read_text(), map_name)

    @classmethod
    def from_evs_parser(cls, evs_parser: EVSParser) -> Self:
        return cls.from_numeric_string(evs_parser.numeric_emevd, evs_parser.map_name)

    @classmethod
    def from_evs_string(cls, evs_string: str, map_name: str = None, script_directory: Path | str = None) -> Self:
        try:
            parser = cls.EVS_PARSER(evs_string, map_name=map_name, script_directory=script_directory)
        except Exception as ex:
            raise EMEVDError(f"Error occurred while parsing EVS string: {ex}")
        return cls.from_evs_parser(parser)

    @classmethod
    def from_evs_path(cls, evs_path: Path | str, map_name: str = None, script_directory: Path | str = None) -> Self:
        evs_path = Path(evs_path)
        if script_directory is None:
            script_directory = evs_path.parent
        try:
            if map_name is None:
                map_name = evs_path.name.split(".")[0]
            emevd = cls.from_evs_string(evs_path.read_text(), map_name=map_name, script_directory=script_directory)
        except Exception as ex:
            raise EMEVDError(f"Error while parsing EVS file: {evs_path}.\n  Error: {ex}")
        emevd.map_name = evs_path.name.split(".")[0]
        if emevd.dcx_type != DCXType.Null:
            emevd.path = evs_path.with_name(emevd.map_name + ".emevd.dcx")
        else:
            emevd.path = evs_path.with_name(emevd.map_name + ".emevd")
        return emevd

    # endregion

    @classmethod
    def from_path(cls, path: str | Path) -> Self:
        """Adds `map_name` attribute to the unpacked binary EMEVD."""
        # noinspection PyTypeChecker
        emevd = super(EMEVD, cls).from_path(path)  # type: Self
        emevd.map_name = emevd.path.name.split(".")[0]
        return emevd

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        byte_order = ByteOrder.from_reader_peek(reader, 1, 4, b"\01", b"\00")
        long_varints = long_varints_from_reader_peek(reader, 1, 5, b"\xFF", b"\00")
        reader.default_byte_order = byte_order
        reader.long_varints = long_varints

        header = EMEVDHeaderStruct.from_bytes(reader)
        # NOTE: 32-bit EMEVD files have four pad bytes at the end, but we're about to start seeking anyway.

        # Delayed, game-specific assertion of header version information.
        if (header.version_unk_1, header.version_unk_2, header.version) != cls.HEADER_VERSION_INFO:
            raise ValueError(
                f"EMEVD header data (version {header.version}) is not compatible with this `EMEVD` game module: "
                f"{cls.__module__}"
            )

        reader.seek(header.events_offset)
        event_dict = {}  # type: dict[int, BaseEvent]
        for _ in range(header.events_count):
            event = cls.EVENT_CLASS.from_emevd_reader(
                reader,
                header.instructions_offset,
                header.base_arg_data_offset,
                header.event_arg_replacements_offset,
                header.event_layers_offset,
            )
            if event.event_id in event_dict:
                _LOGGER.warning(
                    f"Event ID {event.event_id} appears multiple times in EMEVD file. Only the first one will be kept "
                    f"(as Soulstruct tracks events with a dictionary, and AFAWK games will only use the first one)."
                )
            else:
                event_dict[event.event_id] = event

        event_signatures = {event_id: event.signature for event_id, event in event_dict.items()}
        for event in event_dict.values():
            # NOTE: Should be called again when `common_func` EMEVD (with signatures) is available.
            event.update_run_event_instructions(event_signatures, common_signatures=None)

        if header.packed_strings_size != 0:
            reader.seek(header.packed_strings_offset)
            packed_strings = reader.read(header.packed_strings_size)
        else:
            packed_strings = b""

        linked_file_offsets = []
        if header.linked_files_count != 0:
            reader.seek(header.linked_files_offset)
            # These are relative offsets into the packed string data. They are always 64-bit.
            for _ in range(header.linked_files_count):
                linked_file_offsets.append(reader["Q"])

        emevd = cls(events=event_dict, packed_strings=packed_strings, linked_file_offsets=linked_file_offsets)
        emevd.byte_order = byte_order
        emevd.long_varints = long_varints
        emevd.event_signatures = event_signatures
        return emevd

    def load_dict(self, data: dict, clear_old_data=True):
        if clear_old_data:
            self.events = {}
            self.packed_strings = b""
            self.linked_file_offsets = []
            self.map_name = ""
        else:
            if self.map_name and (new_map_name := data.pop("map_name", "")) not in {"", self.map_name}:
                raise ValueError(f"New map name '{new_map_name}' conflicts with old map name '{self.map_name}'.")
        try:
            linked_file_offsets = data.pop("linked")
        except KeyError:
            _LOGGER.warning("No linked file offsets found in EMEVD source.")
        else:
            # Increment new offsets by existing packed string length.
            self.linked_file_offsets += [offset + len(self.packed_strings) for offset in linked_file_offsets]
        try:
            packed_strings = data.pop("strings")
        except KeyError:
            _LOGGER.warning("No strings found in EMEVD source.")
        else:
            self.packed_strings += packed_strings
        self.events.update(data)

    @property
    def event_arg_count(self):
        return sum([e.event_arg_replacements_count for e in self.events.values()])

    def unpack_strings(self) -> list[tuple[str, str]]:
        strings = []
        string_reader = BinaryReader(self.packed_strings)
        while string_reader.position != len(self.packed_strings):
            offset = string_reader.position
            string = string_reader.unpack_string(encoding=self.STRING_ENCODING)
            strings.append((str(offset), string))
        return strings

    def regenerate_signatures(self):
        for event in self.events.values():
            event.process_all_event_arg_replacements()
            event.update_signature()
        self.event_signatures = {event_id: event.signature for event_id, event in self.events.items()}

    def to_dict(self) -> dict[str, tp.Any]:
        self.regenerate_signatures()

        return {
            "map_name": self.map_name,
            "linked": self.linked_file_offsets,
            "strings": self.packed_strings,
            **self.events,
        }

    def to_numeric(self):
        for event in self.events.values():
            event.process_all_event_arg_replacements()
            event.update_signature()

        numeric_output = "\n\n".join([event.to_numeric() for event in self.events.values()])
        numeric_output += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_file_offsets)
        numeric_output += "\n\nstrings:\n" + "\n".join(s[0] + ": " + s[1] for s in self.unpack_strings())
        return numeric_output

    def get_evs_docstring(self, actual_docstring=""):
        docstring = '"""'
        if actual_docstring:
            docstring += "\n" + actual_docstring.rstrip("\n") + "\n"
        docstring += "\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_file_offsets)
        docstring += "\n\nstrings:\n" + "\n".join(s[0] + ": " + repr(s[1]).strip("'") for s in self.unpack_strings())
        docstring += '\n"""'
        return docstring

    def to_evs(
        self,
        enums_star_module_paths: list[str | Path] = (),
        enums_non_star_module_paths: list[str | Path] = (),
        warn_missing_enums=True,
        enums_module_prefix=".",
        event_function_prefix="Event",
        docstring="",
        common_func_emevd: EMEVD = None,
    ) -> str:
        """Convert EMEVD to a Python-style EVS string.

        Any `entity_module_paths` passed in will be star-imported into the EVS script with `enums_module_prefix`. These
        modules will be scanned for `MapEntity`-subclassed entity ID enumerations, the names of which will be
        substituted for entity IDs of matching type anywhere in the decompiled EVS script.

        NOTE: It is currently assumed that all entity modules can be imported using the same `enums_module_prefix`. It
        would be a confusing setup to do otherwise, but you can always edit the import lines yourself to adjust.

        For example:
        ```
            # without enums modules
            AddSpecialEffect(1510100, special_effect_id=1234)

            # enums module `m15_01_00_00_enums.py` defining `class Characters(Character)` enum with 1510100
            from .m15_01_00_00_enums.py import *
            ...
            AddSpecialEffect(Characters.BlackKnight3, special_effect_id=1234)
        ```

        If `warn_missing_enums=True` (default) and any `entity_module_paths` are given, entity IDs that are not found in
        any of the given enums modules will cause a warning to be logged and a TO-DO comment to be written at the end
        of that line. Entity IDs that appear multiple times in the given modules will always raise a `ValueError`.
        """
        enums_manager = self.ENTITY_ENUMS_MANAGER(
            list(enums_star_module_paths) + list(enums_non_star_module_paths), list(self.events)
        )
        star_module_names = [Path(path).name.split(".")[0] for path in enums_star_module_paths]
        enums_manager.star_module_names = star_module_names

        if common_func_emevd:
            # Add common event IDs to `GameEnumsManager`.
            enums_manager.all_common_event_ids = list(common_func_emevd.events)

        self.regenerate_signatures()

        docstring = self.get_evs_docstring(docstring)
        game = self.get_game()
        imports = f"from soulstruct.{game.submodule_name}.events import *"
        imports += f"\nfrom soulstruct.{game.submodule_name}.events.instructions import *"
        imports += f"\nfrom soulstruct.{game.submodule_name}.game_types import *"
        evs_events = [
            event.to_evs(enums_manager, self.event_signatures, event_function_prefix)
            for event in self.events.values()
        ]

        # TODO: Does not catch calls that are already multi-line.
        for i in range(len(evs_events)):
            evs_events[i] = self.add_event_call_keywords(evs_events[i], enums_manager, common_func_emevd)

        if common_func_emevd and any("CommonFunc_" in event_string for event_string in evs_events):
            # TODO: pass real path (or attach to common EMEVD) rather than guessing `common_func`.
            # Import written first to avoid 'unused' warnings for standard imports.
            imports = f"# [COMMON_FUNC]\nfrom .common_func import *\n" + imports

        # Create imports (if any modules were actually passed in here).
        if enums_manager and enums_manager.modules:
            if warn_missing_enums:
                missing_flag_count = 0
                missing_done = set()
                for game_types, value in enums_manager.get_sorted_missing_items():
                    if "Flag" in game_types:
                        missing_flag_count += 1
                        continue
                    if (game_types, value) in missing_done:
                        continue
                    _LOGGER.warning(
                        f"{self.map_name}: Missing '{game_types}' entity ID: {value}"
                    )
                    missing_done.add((game_types, value))
                if missing_flag_count > 0:
                    _LOGGER.warning(f"{self.map_name}: Missing {missing_flag_count} flag IDs.")
            imports += enums_manager.get_import_lines(star_module_names, enums_module_prefix)

        return docstring + "\n" + "\n\n\n".join([imports] + evs_events) + "\n"

    def add_event_call_keywords(
        self, event_string: str, enums_manager: GameEnumsManager, common_func_emevd: EMEVD = None
    ):
        """Add keyword argument names to `Event_{ID}(_, x, y, z)` calls.

        Also reformats calls to multiple lines if necessary.
        """
        new_event_string = event_string

        for match in _EVENT_CALL_RE.finditer(event_string):
            if match.group(4) == "":
                continue  # no arguments
            indent = match.group(1)
            call_name = match.group(2)  # 'Event' or 'CommonFunc'
            event_id = int(match.group(3))
            end = match.group(5)  # newline or empty
            if call_name == "CommonFunc" and not common_func_emevd:
                continue  # cannot parse common event calls
            try:
                if call_name == "CommonFunc":
                    event_args = common_func_emevd.event_signatures[event_id].event_args
                    arg_names = common_func_emevd.event_signatures[event_id].get_evs_arg_names()
                else:  # standard local "Event"
                    event_args = self.event_signatures[event_id].event_args
                    arg_names = self.event_signatures[event_id].get_evs_arg_names()
            except KeyError:
                pass  # event ID not defined in this script or in CommonFunc
            else:
                args = match.group(4).replace(" ", "").replace("\n", "").split(",")  # type: list[str]
                if args[-1] == "":
                    args = args[:-1]
                if len(args) != len(event_args) + 1:
                    if call_name == "CommonFunc":
                        _LOGGER.warning(f"Mismatch in defined/called event arg count for common func event {event_id}.")
                    else:
                        _LOGGER.warning(
                            f"Mismatch in defined/called event arg count for map event {event_id}.\n"
                            f"This is likely to be a serious problem for EVS compilation!"
                        )
                    continue
                slot = args[0]
                for j in range(1, len(args)):  # `j` offset by +1 to skip `_` slot argument
                    if not event_args[j - 1].py_types:
                        continue  # no Python type hints for this argument
                    try:
                        int_value = int(args[j])
                    except ValueError:
                        continue
                    game_types = event_args[j - 1].combined_game_types
                    if game_types:
                        try:
                            args[j] = f"{enums_manager.check_out_enum_variable(int_value, *game_types)}"
                        except enums_manager.EnumManagerError:
                            pass
                kwargs = [f"{arg_name}={arg_value}" for arg_name, arg_value in zip(arg_names, args[1:], strict=True)]
                one_line_event_call = f"{indent}{call_name}_{event_id}({slot}, {', '.join(kwargs)}){end}"
                if len(one_line_event_call) > 121:  # last newline character doesn't count
                    # Multiline call.
                    arg_indent = " " * (len(indent) + 4)
                    multi_line_kwargs = f",\n{arg_indent}".join([slot] + kwargs) + ","
                    multi_line_event_call = (
                        f"{indent}{call_name}_{event_id}(\n{arg_indent}{multi_line_kwargs}\n{indent}){end}"
                    )
                    new_event_string = new_event_string.replace(match.group(0), multi_line_event_call)
                else:
                    new_event_string = new_event_string.replace(match.group(0), one_line_event_call)
        return new_event_string

    def to_writer(self) -> BinaryWriter:

        self.regenerate_signatures()

        writer = BinaryWriter(byte_order=self.byte_order, long_varints=self.long_varints)

        header = EMEVDHeaderStruct(
            big_endian=self.byte_order == ByteOrder.BigEndian,
            varint_size_check=-1 if self.long_varints else 0,
            version_unk_1=self.HEADER_VERSION_INFO[0],
            version_unk_2=self.HEADER_VERSION_INFO[1],
            version=self.HEADER_VERSION_INFO[2],
            file_size=RESERVED,
            events_count=len(self.events),
            events_offset=RESERVED,
            instructions_count=sum([e.instruction_count for e in self.events.values()]),
            instructions_offset=RESERVED,
            unknown_offset=RESERVED,
            event_layers_count=RESERVED,
            event_layers_offset=RESERVED,
            event_arg_replacements_count=RESERVED,
            event_arg_replacements_offset=RESERVED,
            linked_files_count=len(self.linked_file_offsets),
            linked_files_offset=RESERVED,
            base_arg_data_size=RESERVED,
            base_arg_data_offset=RESERVED,
            packed_strings_size=len(self.packed_strings),
            packed_strings_offset=RESERVED,
        )
        header.to_writer(writer, reserve_obj=self)

        if not self.long_varints:
            writer.pad(4)

        # Write event headers.
        writer.fill_with_position("events_offset", obj=self)
        for event in self.events.values():
            event.to_emevd_writer(writer)
        # Count already written.

        # Write instruction headers.
        instructions_offset = writer.fill_with_position("instructions_offset", obj=self)
        for event in self.events.values():
            event.pack_instructions(writer, instructions_offset)
        # Count already written.

        # Write event layers.
        event_layers_offset = writer.fill_with_position("event_layers_offset", obj=self)
        existing_event_layers = {}  # type: dict[EventLayers, int]
        for event in self.events.values():
            event.pack_instruction_event_layers(writer, existing_event_layers, event_layers_offset)
        writer.fill("event_layers_count", len(existing_event_layers), obj=self)

        # NOTE: The order of tables from here (base args, event arg replacements, linked files, packed strings) does
        # NOT match the order of the offsets given in the EMEVD header.

        # Unknown (empty) table goes here (same as `base_args_offset`).
        writer.fill_with_position("unknown_offset", obj=self)

        # Write instruction base arg data.
        base_args_start = writer.position
        writer.fill_with_position("base_arg_data_offset", obj=self)
        for event in self.events.values():
            event.pack_instruction_base_args(writer, base_args_start)
        writer.pad_align(16)
        # Pad or alignment after base args, depending on `long_varints`.
        writer.fill("base_arg_data_size", writer.position - base_args_start, obj=self)

        # Write event arg replacements.
        event_arg_replacements_offset = writer.fill_with_position("event_arg_replacements_offset", obj=self)
        event_arg_replacements_count = 0
        for event in self.events.values():
            event_arg_replacements_count += event.pack_event_arg_replacements(writer, event_arg_replacements_offset)
        writer.fill("event_arg_replacements_count", event_arg_replacements_count, obj=self)

        # Write linked files (offsets to names in packed strings).
        # TODO: Linked file offsets currently can't be modified very easily, as packed strings also include rare logging
        #  instruction data (mostly in Bloodborne). The user currently has to manage `packed_strings` themselves.
        writer.fill_with_position("linked_files_offset", obj=self)
        writer.pack(f"{len(self.linked_file_offsets)}Q", *self.linked_file_offsets)
        # Count already written.

        writer.fill_with_position("packed_strings_offset", obj=self)
        writer.append(self.packed_strings)

        # Final offset.
        writer.fill_with_position("file_size", obj=self)

        return writer

    def write_numeric(self, numeric_path=None):
        if not numeric_path:
            numeric_path = self.map_name
            if not numeric_path.endswith(".numeric.txt"):
                numeric_path += ".numeric.txt"
        numeric_path = Path(numeric_path)
        if numeric_path.parent:
            numeric_path.parent.mkdir(exist_ok=True, parents=True)
        with numeric_path.open("w", encoding="utf-8") as f:
            f.write(self.to_numeric())

    def write_evs(
        self,
        evs_path: str | Path = None,
        enums_star_module_paths: list[str | Path] = (),
        enums_non_star_module_paths: list[str | Path] = (),
        warn_missing_enums=True,
        enums_module_prefix=".",
        event_prefix="Event",
        docstring="",
        common_func_emevd: EMEVD = None,
    ):
        if not evs_path:
            evs_path = self.map_name
            if not evs_path.endswith(".evs.py"):
                evs_path += ".evs.py"
        evs_path = Path(evs_path)
        if evs_path.parent:
            evs_path.parent.mkdir(exist_ok=True, parents=True)
        evs_string = self.to_evs(
            enums_star_module_paths,
            enums_non_star_module_paths,
            warn_missing_enums,
            enums_module_prefix,
            event_prefix,
            docstring,
            common_func_emevd,
        )
        with evs_path.open("w", encoding="utf-8") as f:
            f.write(evs_string)

    @classmethod
    def from_auto_detect_source_type(cls, emevd_source: Path | str | bytes | BinaryReader) -> str:
        """Tries to detect the type of `emevd_source` and load it.

        Returns the loaded `EMEVD` and a string from {"emevd", "evs", "numeric"}.
        """
        if isinstance(emevd_source, str) and "\n" in emevd_source:
            # Guess numeric string.
            return "numeric_string"

        if isinstance(emevd_source, (Path, str)):
            emevd_source = Path(emevd_source)
            if emevd_source.suffix == ".txt":
                return "numeric_path"
            if emevd_source.name.endswith(".evs") or emevd_source.name.endswith(".evs.py"):
                return "evs_path"
            if any(emevd_source.name.endswith(suffix) for suffix in (".emevd", ".emevd.dcx")):
                return "emevd_path"
            raise TypeError(f"Unknown EMEVD source path name: {emevd_source.name}")

        if isinstance(emevd_source, BinaryReader):
            return "emevd_reader"
        if isinstance(emevd_source, bytes):
            return "emevd_bytes"
        raise TypeError(f"Cannot detect EMEVD source type from object type: {type(emevd_source).__name__}")

    def merge(
        self,
        other_emevd: EMEVD,
        merge_events=(0, 50),
        event_id_offset=0,
    ) -> Self:
        """Return a new `EMEVD` creating by emerging all events of this instance with those of `other_emevd_source`.

        Event IDs in `merge_events` will have their instruction sets merged (with this instance's instrutions appearing
        first). By default, events 0 (constructor) and 50 (preconstructor) are merged this way. Any other event IDs that
        appear in both sources will raise a `ValueError`.

        Events from `other_emevd_source` will have `event_id_offset` added to their ID before being merged (default 0,
        so no change). This is useful for, say, defining some common events that will share an ID suffix across all
        maps. You will probably want to set `merge_events=()` for this use case.

        NOTE: Currently cannot merge any events that use event arguments.
        """
        combined_emevd = self.copy()
        for event_id, other_event in other_emevd.events.items():
            event_id += event_id_offset
            if event_id not in combined_emevd.events:
                combined_emevd.events[event_id] = other_event
            elif event_id in merge_events:
                existing_event = combined_emevd.events[event_id]
                if existing_event.event_arg_replacements_count > 0 or other_event.event_arg_replacements_count > 0:
                    raise ValueError(
                        f"Cannot merge event {event_id}, as it uses event arguments in at least one source."
                    )
                existing_event.instructions += other_event.instructions
            else:
                raise ValueError(
                    f"Event {event_id} appears in both EMEVD sources and is not in allowed `merge_events`."
                )
        return combined_emevd
