from __future__ import annotations

__all__ = ["EMEVD"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers.dcx import DCXType
from soulstruct.utilities.binary import *

from .event import Event as BaseEvent, EventSignature
from .event_layers import EventLayers
from .exceptions import EMEVDError
from .numeric import build_numeric

if tp.TYPE_CHECKING:
    from soulstruct.base.events.emevd.evs import EVSParser
    from .entity_enums_manager import EntityEnumsManager

try:
    Self = tp.Self
except AttributeError:  # < Python 3.11
    Self = "EMEVD"

_LOGGER = logging.getLogger(__name__)

_EVENT_CALL_RE = re.compile(r"( *)(Event|CommonFunc)_(\d+)\(([\d\-,. \n]+)\) *(\n|$)?")


@dataclass(slots=True)
class EMEVDHeaderStruct(NewBinaryStruct):
    """Indicates fields that will always be present in this header, but cannot be used."""
    _signature: bytes = field(**Binary(length=4, asserted=b"EVD\0"))
    big_endian: bool
    varint_size_check: byte = field(**Binary(asserted=[-1, 0]))  # -1 if True, 0 if False
    version_unk_1: bool
    version_unk_2: byte
    version: uint
    file_size: uint
    events_count: varuint
    events_offset: varuint
    instructions_count: varuint
    instructions_offset: varuint
    _unknown_count: varuint = field(**Binary(asserted=0))  # unused in all games
    unknown_offset: varuint  # unused in all games (but cannot be asserted)
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

    Event: tp.ClassVar[tp.Type[BaseEvent]]
    ENTITY_ENUMS_MANAGER: tp.ClassVar[tp.Type[EntityEnumsManager]]
    EVS_PARSER: tp.ClassVar[tp.Type[EVSParser]]
    STRING_ENCODING: tp.ClassVar[str]
    DCX_TYPE: tp.ClassVar[DCXType]  # TODO: rename `DEFAULT_DCX_TYPE`
    HEADER_VERSION_INFO: tp.ClassVar[tuple[bool, int, int]] = (False, 0, 204)  # DS1 default

    events: dict[int, BaseEvent] = field(default_factory=dict)
    packed_strings: bytes = b""
    # TODO: Should actually read the linked strings so they can be modified.
    #  But then I'd have to check all packed strings used by logging instructions as well...
    linked_file_offsets: list[int] = field(default_factory=list)
    map_name: str = ""

    # Internal usage.
    byte_order: ByteOrder = field(repr=False, default=ByteOrder.LittleEndian)
    varint_size: int = field(repr=False, default=4)
    event_signatures: dict[int, EventSignature] = field(repr=False, default=dict)

    # region Numeric/EVS Read Methods

    @classmethod
    def from_numeric_string(cls, numeric_string: str, map_name: str = "") -> Self:
        events, linked_file_offsets, packed_strings = build_numeric(numeric_string, cls.Event)
        emevd = cls(events, packed_strings, linked_file_offsets, map_name)
        emevd.dcx_type = cls.DCX_TYPE  # set default DCX
        return emevd

    @classmethod
    def from_numeric_path(cls, numeric_path: Path | str, map_name: str = "") -> Self:
        return cls.from_numeric_string(numeric_path.read_text(), map_name)

    @classmethod
    def from_evs_parser(cls, evs_parser: EVSParser) -> Self:
        return cls.from_numeric_string(evs_parser.numeric_emevd, evs_parser.map_name)

    @classmethod
    def from_evs_string(cls, evs_string: str, script_directory: Path | str = None) -> Self:
        try:
            parser = cls.EVS_PARSER(evs_string, script_directory=script_directory)
        except Exception as ex:
            raise EMEVDError(f"Error occurred while parsing EVS string: {ex}")
        return cls.from_evs_parser(parser)

    @classmethod
    def from_evs_path(cls, evs_path: Path | str, script_directory: Path | str = None) -> Self:
        evs_path = Path(evs_path)
        if script_directory is None:
            script_directory = evs_path.parent
        try:
            emevd = cls.from_evs_string(evs_path.read_text(), script_directory)
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
        emevd = super().from_path(path)  # type: Self
        emevd.map_name = emevd.path.name.split(".")[0]
        return emevd

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        byte_order = BinaryCondition((5, 1), [(ByteOrder.BigEndian, b"\01"), (ByteOrder.LittleEndian, b"\00")])
        varint_size = BinaryCondition((6, 1), [(4, b"\00"), (8, b"\xFF")])
        reader.default_byte_order = byte_order(reader)
        reader.varint_size = varint_size(reader)

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
        for _ in header.events_count:
            event = cls.Event.from_emevd_reader(
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
                linked_file_offsets.append(reader.unpack_value("Q"))

        emevd = cls(event_dict, packed_strings, linked_file_offsets)
        emevd.byte_order = byte_order
        emevd.varint_size = varint_size
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

    def to_dict(self) -> dict:
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
        entity_star_module_paths: tp.Sequence[str | Path, ...] = (),
        entity_non_star_module_paths: tp.Sequence[str | Path, ...] = (),
        warn_missing_enums=True,
        entity_module_prefix=".",
        event_function_prefix="Event",
        docstring="",
        common_func_emevd: EMEVD = None,
    ) -> str:
        """Convert EMEVD to a Python-style EVS string.

        Any `entity_module_paths` passed in will be star-imported into the EVS script with `entity_module_prefix`. These
        modules will be scanned for `MapEntity`-subclassed entity ID enumerations, the names of which will be
        substituted for entity IDs of matching type anywhere in the decompiled EVS script.

        NOTE: It is currently assumed that all entity modules can be imported using the same `entity_module_prefix`. It
        would be a confusing setup to do otherwise, but you can always edit the import lines yourself to adjust.

        For example:
        ```
            # without entities modules
            AddSpecialEffect(1510100, special_effect_id=1234)

            # entities module `m15_01_00_00_entities.py` defining `class Characters(Character)` enum with 1510100
            from .m15_01_00_00_entities.py import *
            ...
            AddSpecialEffect(Characters.BlackKnight3, special_effect_id=1234)
        ```

        If `warn_missing_enums=True` (default) and any `entity_module_paths` are given, entity IDs that are not found in
        any of the given entities modules will cause a warning to be logged and a TO-DO comment to be written at the end
        of that line. Entity IDs that appear multiple times in the given modules will always raise a `ValueError`.
        """
        enums_manager = self.ENTITY_ENUMS_MANAGER(
            entity_star_module_paths, entity_non_star_module_paths, list(self.events)
        )

        if common_func_emevd:
            # Add common event IDs to `EntityEnumsManager`.
            enums_manager.all_common_event_ids = list(common_func_emevd.events)

        self.regenerate_signatures()

        docstring = self.get_evs_docstring(docstring)
        game = self.get_game()
        imports = f"from soulstruct.{game.submodule_name}.events import *"
        imports += f"\nfrom soulstruct.{game.submodule_name}.events.instructions import *"
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

        # Create imports.
        if enums_manager:
            if warn_missing_enums:
                for entity_cls_name, missing_id in enums_manager.missing_enums:
                    if entity_cls_name == "Flag":
                        continue  # TODO: Too many missing Flags to print.
                    _LOGGER.warning(f"Missing '{entity_cls_name}' entity ID: {missing_id}")
            for name in sorted(enums_manager.used_star_modules):
                imports += f"\nfrom {entity_module_prefix}{name} import *"
            for name, enums in sorted(enums_manager.used_non_star_imports.items()):
                if enums:
                    import_strings = sorted({e.import_string for e in enums})
                    import_prefix = f"\nfrom {entity_module_prefix}{name} import "
                    one_line_suffix = ", ".join(import_strings)
                    if len(import_prefix + one_line_suffix) > 119:
                        # Split across multiple lines.
                        multi_line_imports = "\n    ".join(import_strings)
                        imports += f"{import_prefix}(\n    {multi_line_imports}\n)"
                    else:
                        imports += f"{import_prefix}{one_line_suffix}"

        return docstring + "\n" + "\n\n\n".join([imports] + evs_events) + "\n"

    def add_event_call_keywords(
        self, event_string: str, enums_manager: EntityEnumsManager, common_func_emevd: EMEVD = None
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
                else:  # standard local "Event"
                    event_args = self.event_signatures[event_id]
            except KeyError:
                pass  # event ID not defined in this script or in CommonFunc
            else:
                args = match.group(4).replace(" ", "").replace("\n", "").split(",")
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
                    try:
                        args[j] = f"{enums_manager.check_out_enum(int_value, *event_args[j - 1].py_types)}"
                    except enums_manager.MissingEntityError:
                        pass
                kwargs = [f"{arg.combined_name}={arg_value}" for arg, arg_value in zip(event_args, args[1:])]
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

        writer = EMEVDHeaderStruct.object_to_writer(
            self,
            byte_order=self.byte_order,
            varint_size=self.varint_size,
            big_endian=self.byte_order == ByteOrder.BigEndian,
            varint_size_check=-1 if self.varint_size == 8 else 0,
            version_unk_1=self.HEADER_VERSION_INFO[0],
            version_unk_2=self.HEADER_VERSION_INFO[1],
            version=self.HEADER_VERSION_INFO[2],
            events_count=len(self.events),
            instructions_count=sum([e.instruction_count for e in self.events.values()]),
            linked_files_count=len(self.linked_file_offsets),
            packed_strings_size=len(self.packed_strings),
            # All remaining fields (offsets/counts/file size) are reserved.
        )

        events = tuple(self.events.values())

        # Write event headers.
        writer.fill_with_position("events_offset", obj=self)
        for event in events:
            event.to_emevd_writer(writer)
        # Count already written.

        # Write instruction headers.
        writer.fill_with_position("instructions_offset", obj=self)
        for event in events:
            event.pack_instructions(writer)
        # Count already written.

        # Write event layers.
        writer.fill_with_position("event_layers_offset", obj=self)
        existing_event_layers = {}  # type: dict[EventLayers, int]
        for event in events:
            event.pack_instruction_event_layers(writer, existing_event_layers)
        writer.fill("event_layers_count", len(existing_event_layers))

        # NOTE: The order of tables from here (base args, event arg replacements, linked files, packed strings) does
        # NOT match the order of the offsets given in the EMEVD header.

        # Unknown (empty) table goes here (same as `base_args_offset`).
        writer.fill_with_position("unknown_offset", obj=self)

        # Write instruction base arg data.
        base_args_start = writer.position
        writer.fill_with_position("base_args_offset", obj=self)
        for event in events:
            event.pack_instruction_base_args(writer)
        # Pad or alignment after base args, depending on `varint_size`.
        if self.varint_size == 4:  # PTDE/DSR only
            writer.pad(4)
        elif self.varint_size == 8:
            writer.pad_align(16)
        else:
            raise ValueError(f"Invalid `varint_size` for packing: {self.varint_size}")
        writer.fill("base_args_size", writer.position - base_args_start, obj=self)

        # Write event arg replacements.
        writer.fill_with_position("event_arg_replacements_offset", obj=self)
        event_arg_replacements_count = 0
        for event in events:
            event_arg_replacements_count += event.pack_event_arg_replacements(writer)
        writer.fill("event_arg_replacements_count", obj=self)

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
        evs_path=None,
        entity_star_module_paths: tp.Sequence[str | Path, ...] = (),
        entity_non_star_module_paths: tp.Sequence[str | Path, ...] = (),
        warn_missing_enums=True,
        entity_module_prefix=".",
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
            entity_star_module_paths,
            entity_non_star_module_paths,
            warn_missing_enums,
            entity_module_prefix,
            event_prefix,
            docstring,
            common_func_emevd,
        )
        with evs_path.open("w", encoding="utf-8") as f:
            f.write(evs_string)

    @classmethod
    def from_auto_detect_source_type(cls, emevd_source: Path | str | bytes | BinaryReader) -> tuple[Self, str]:
        """Tries to detect the type of `emevd_source` and load it.

        Returns the loaded `EMEVD` and a string from {"emevd", "evs", "numeric"}.
        """
        if isinstance(emevd_source, str) and "\n" in emevd_source:
            # Guess numeric string.
            try:
                emevd = cls.from_numeric_string(emevd_source, map_name="")
                return emevd, "numeric"
            except Exception as ex:
                raise TypeError(f"Guessed that `emevd_source` was a numeric string, but failed to load it: {ex}")

        if isinstance(emevd_source, (Path, str)):
            try:
                emevd_source = Path(emevd_source)
                if emevd_source.suffix == ".txt":
                    emevd = cls.from_numeric_path(emevd_source, map_name=emevd_source.name.split(".")[0])
                    return emevd, "numeric"
                if emevd_source.name.endswith(".evs") or emevd_source.name.endswith(".evs.py"):
                    emevd = cls.from_evs_path(emevd_source)
                    return emevd, "evs"
                else:  # try EMEVD
                    emevd = cls.from_path(emevd_source)
                    return emevd, "emevd"
            except Exception as ex:
                raise TypeError(
                    f"Guessed that `emevd_source` was a path, but failed to load it as numeric/EVS/EMEVD: {ex}"
                )

        try:
            if isinstance(emevd_source, BinaryReader):
                emevd = cls.from_reader(emevd_source)
                return emevd, "emevd"
            if isinstance(emevd_source, bytes):
                emevd = cls.from_bytes(emevd_source)
                return emevd, "emevd"
        except Exception as ex:
            raise TypeError(f"Could not load binary `emevd_source` as an EMEVD: {ex}")

    def merge(
        self,
        other_emevd_source: EMEVD | Path | str | bytes | BinaryReader,
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
        if isinstance(other_emevd_source, self.__class__):
            other_emevd = other_emevd_source
        elif isinstance(other_emevd_source, (Path, str)):
            other_emevd_source = Path(other_emevd_source)
            if other_emevd_source.name.endswith(".evs") or other_emevd_source.name.endswith(".evs.py"):
                other_emevd = self.from_evs_path(other_emevd_source)
            else:
                other_emevd = self.from_path(other_emevd_source)
        elif isinstance(other_emevd_source, BinaryReader):
            other_emevd = self.from_reader(other_emevd_source)
        elif isinstance(other_emevd_source, bytes):
            other_emevd = self.from_bytes(other_emevd_source)
        else:
            if isinstance(other_emevd_source, EMEVD):
                raise TypeError("EMEVD game class of `other_emevd_source` is not compatible with this one.")
            raise TypeError(f"Invalid `other_emevd_source` type: {type(other_emevd_source).__name__}")

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
