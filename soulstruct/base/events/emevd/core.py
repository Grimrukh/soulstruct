from __future__ import annotations

__all__ = ["EMEVD"]

import abc
import logging
import re
import struct
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile, InvalidGameFileTypeError
from soulstruct.containers.dcx import DCXType
from soulstruct.utilities.binary import BinaryReader

from .event import Event
from .exceptions import EMEVDError
from .numeric import build_numeric

if tp.TYPE_CHECKING:
    from soulstruct.base.events.emevd.evs import EVSParser
    from soulstruct.utilities.binary import BinaryStruct
    from .entity_enums_manager import EntityEnumsManager

_LOGGER = logging.getLogger(__name__)

_EVENT_CALL_RE = re.compile(r"( *)(Event|CommonFunc)_(\d+)\(([\d\-,. \n]+)\) *(\n|$)?")


class EMEVD(GameFile, abc.ABC):

    events: dict[int, Event]
    packed_strings: bytes
    linked_file_offset: list[int]
    map_name: str

    # For internal usage.
    all_event_arg_fmts: dict[int, str]  # maps events to their argument struct formats
    all_event_arg_names: dict[int, list[str]]  # maps events to their auto-detected argument names
    all_event_arg_types: dict[int, list[tuple[tp.Type, ...]]]  # maps events to each of their arguments' possible types

    Event: tp.Type[Event] = None
    ENTITY_ENUMS_MANAGER: tp.Type[EntityEnumsManager] = None
    EVS_PARSER: tp.Type[EVSParser] = None
    STRING_ENCODING: str = None
    DCX_TYPE: DCXType = None
    HEADER_STRUCT: BinaryStruct = None

    def __init__(
        self,
        emevd_source: GameFile.Typing,
        dcx_type=None,
        script_directory=None,
        common_func_emevd: EMEVD = None,
    ):
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

        self.events = {}
        self.packed_strings = b""
        self.linked_file_offsets = []  # offsets into packed strings
        self.map_name = ""
        self.all_event_arg_names = {}
        self.all_event_arg_fmts = {}
        self.all_event_arg_types = {}
        self.common_func_emevd = common_func_emevd

        if script_directory is None:
            if isinstance(emevd_source, Path) or (isinstance(emevd_source, str) and "\n" not in emevd_source):
                script_directory = Path(emevd_source).parent

        super().__init__(
            emevd_source, dcx_type=dcx_type, script_directory=script_directory
        )
        if dcx_type is None:
            self.dcx_type = self.DCX_TYPE  # default to standard game DCX
        if not self.map_name and self.path:
            self.map_name = self.path.name.split(".")[0]
        elif self.map_name and not self.path:
            self.path = Path(self.map_name + ".emevd")
            if self.DCX_TYPE:
                self.path = self.path.with_suffix(".emevd.dcx")

    def _handle_other_source_types(self, file_source, script_directory=None) -> tp.Optional[BinaryReader]:
        if isinstance(file_source, self.EVS_PARSER):
            # Copy data from existing `EVSParser` instance.
            self.map_name = file_source.map_name
            events, linked_file_offsets, packed_strings = build_numeric(file_source.numeric_emevd, self.Event)
            self.events.update(events)
            self.linked_file_offsets = linked_file_offsets
            self.packed_strings = packed_strings
            return None

        elif isinstance(file_source, str) and "\n" in file_source:
            # Parse EVS or numeric string format.
            parsed = self.EVS_PARSER(file_source, script_directory=script_directory)
            self.map_name = parsed.map_name
            events, self.linked_file_offsets, self.packed_strings = build_numeric(parsed.numeric_emevd, self.Event)
            self.events.update(events)
            return None

        elif isinstance(file_source, Path) or (isinstance(file_source, str) and "\n" not in file_source):
            emevd_path = Path(file_source)
            self.map_name = emevd_path.name.split(".")[0]

            if emevd_path.suffix in {".evs", ".py"}:
                if script_directory is None:
                    script_directory = emevd_path.parent
                try:
                    parsed = self.EVS_PARSER(emevd_path, script_directory=script_directory)
                except Exception as ex:
                    raise ValueError(f"Error while parsing EVS file: {emevd_path}\n  Error: {ex}")
                self.map_name = parsed.map_name
                try:
                    events, self.linked_file_offsets, self.packed_strings = build_numeric(
                        parsed.numeric_emevd, self.Event
                    )
                except Exception:
                    print("\n".join(f"{i}:   {line}" for i, line in enumerate(parsed.numeric_emevd.split("\n"))))
                    raise
                self.events.update(events)
                return None

            elif emevd_path.suffix == ".txt":
                try:
                    self.build_from_numeric_path(emevd_path)
                except Exception:
                    raise EMEVDError(
                        f"Could not interpret file '{str(emevd_path)}' as numeric-style EMEVD.\n"
                        f"(Note that you cannot use verbose-style text files as EMEVD input.)\n"
                        f"If your file is an EVS script, change the extension to '.py' or '.evs'."
                    )
                return None

        raise InvalidGameFileTypeError(
            "`emevd_source` is not an `EVSParser`, EVS or numeric string, or .evs/.py/.txt file."
        )

    def unpack(self, emevd_reader: BinaryReader, **kwargs):
        header = emevd_reader.unpack_struct(self.HEADER_STRUCT)

        emevd_reader.seek(header["event_table_offset"])
        event_dict = self.Event.unpack_event_dict(
            emevd_reader,
            header["instruction_table_offset"],
            header["base_arg_data_offset"],
            header["event_arg_table_offset"],
            header["event_layers_table_offset"],
            count=header["event_count"],
        )

        self.events.update(event_dict)

        if header["packed_strings_size"] != 0:
            emevd_reader.seek(header["packed_strings_offset"])
            self.packed_strings = emevd_reader.read(header["packed_strings_size"])

        if header["linked_files_count"] != 0:
            emevd_reader.seek(header["linked_files_table_offset"])
            # These are relative offsets into the packed string data.
            for _ in range(header["linked_files_count"]):
                self.linked_file_offsets.append(struct.unpack("<Q", emevd_reader.read(8))[0])

        # Parse event args for `RunEvent` and `RunCommonEvent` instructions.
        for event in self.events.values():
            event.update_evs_function_args(self.all_event_arg_names, self.all_event_arg_fmts, self.all_event_arg_types)
        for event in self.events.values():
            event.update_run_event_instructions(self.all_event_arg_fmts, self.common_func_emevd)

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

    def build_from_numeric_path(self, numeric_path):
        numeric_path = Path(numeric_path)
        with numeric_path.open("r", encoding="utf-8") as f:
            numeric_string = f.read()
        events, self.linked_file_offsets, self.packed_strings = build_numeric(numeric_string, self.Event)
        self.events.update(events)

    @property
    def event_count(self):
        return len(self.events)

    @property
    def instruction_count(self):
        return sum([e.instruction_count for e in self.events.values()])

    def build_event_layers_table(self):
        """Scans all Instructions for event layers and packs them into a table.

        Also sets the offset within each Instruction so that it can be packed.
        """
        packed_event_layers_table = []
        for event in self.events.values():
            for instruction in event.instructions:
                if instruction.event_layers:
                    packed_event_layers = instruction.event_layers.pack()
                    layers_header_size = self.Event.Instruction.EventLayers.HEADER_STRUCT.size
                    try:
                        existing_offset = packed_event_layers_table.index(packed_event_layers) * layers_header_size
                        instruction.event_layers_offset = existing_offset
                    except ValueError:
                        new_offset = layers_header_size * len(packed_event_layers_table)
                        packed_event_layers_table.append(packed_event_layers)
                        instruction.event_layers_offset = new_offset
                else:
                    # No event layers for this instruction.
                    instruction.event_layers_offset = -1
        return packed_event_layers_table

    @abc.abstractmethod
    def compute_base_args_size(self, existing_data_size):
        """Works different for DS1 vs. other games."""
        ...

    @abc.abstractmethod
    def pad_after_base_args(self, emevd_binary_after_base_args):
        """Works different for DS1 vs. other games."""
        ...

    @property
    def event_arg_count(self):
        return sum([e.event_arg_count for e in self.events.values()])

    def compute_table_offsets(self, event_layers_table):
        offsets = {"event": self.HEADER_STRUCT.size}
        offsets["instruction"] = offsets["event"] + self.Event.HEADER_STRUCT.size * self.event_count
        # Ignore empty unknown table.
        offsets["event_layers"] = offsets["instruction"] + (
                self.Event.Instruction.HEADER_STRUCT.size * self.instruction_count
        )
        offsets["base_arg_data"] = offsets["event_layers"] + (
                self.Event.Instruction.EventLayers.HEADER_STRUCT.size * len(event_layers_table)
        )
        offsets["event_arg"] = offsets["base_arg_data"] + self.compute_base_args_size(offsets["base_arg_data"])
        offsets["linked_files"] = offsets["event_arg"] + self.Event.EventArg.HEADER_STRUCT.size * self.event_arg_count
        offsets["packed_strings"] = offsets["linked_files"] + 8 * len(self.linked_file_offsets)
        offsets["end_of_file"] = offsets["packed_strings"] + len(self.packed_strings)
        return offsets

    def build_emevd_header(self):
        # TODO: Stop calculating offsets twice. Just calculate them during binary pack and create header last.
        event_layers_table = self.build_event_layers_table()  # TODO: Also building this twice...
        offsets = self.compute_table_offsets(event_layers_table)
        header_dict = {
            "file_size_1": offsets["end_of_file"],
            "event_count": self.event_count,
            "event_table_offset": offsets["event"],
            "instruction_count": self.instruction_count,
            "instruction_table_offset": offsets["instruction"],
            "unknown_table_offset": offsets["base_arg_data"],  # Absent.
            "event_layers_count": len(event_layers_table),
            "event_layers_table_offset": offsets["event_layers"],
            "event_arg_count": self.event_arg_count,
            "event_arg_table_offset": offsets["event_arg"],
            "linked_files_count": len(self.linked_file_offsets),
            "linked_files_table_offset": offsets["linked_files"],
            "base_arg_data_size": self.compute_base_args_size(offsets["base_arg_data"]),  # Note different table order.
            "base_arg_data_offset": offsets["base_arg_data"],
            "packed_strings_size": len(self.packed_strings),
            "packed_strings_offset": offsets["packed_strings"],
        }
        return self.HEADER_STRUCT.pack(header_dict)

    def unpack_strings(self) -> list[tuple[str, str]]:
        strings = []
        string_reader = BinaryReader(self.packed_strings)
        while string_reader.position != len(self.packed_strings):
            offset = string_reader.position
            string = string_reader.unpack_string(encoding=self.STRING_ENCODING)
            strings.append((str(offset), string))
        return strings

    def to_dict(self) -> dict:
        for event in self.events.values():
            event.process_all_event_args()

        return {
            "map_name": self.map_name,
            "linked": self.linked_file_offsets,
            "strings": self.packed_strings,
            **self.events,
        }

    def to_numeric(self):
        for event in self.events.values():
            event.process_all_event_args()

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
        is_common_func=False,
        docstring="",
    ) -> str:
        """Convert EMEVD to a Python-style EVS string.

        Currently, EMEVD instructions are line-for-line with EVS instructions; no automatic 'decompilation' into higher-
        level Python syntax (e.g. converting conditions and skips into `if` blocks) is supported.

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
        if self.common_func_emevd:
            enums_manager.all_common_event_ids = list(self.common_func_emevd.events)

        for event in self.events.values():
            event.process_all_event_args()

        docstring = self.get_evs_docstring(docstring)
        imports = f"from soulstruct.{self.GAME.submodule_name}.events import *"
        imports += f"\nfrom soulstruct.{self.GAME.submodule_name}.events.instructions import *"
        evs_events = [
            event.to_evs(
                enums_manager,
                self.all_event_arg_names,
                self.all_event_arg_fmts,
                self.all_event_arg_types,
                is_common_func=is_common_func,
            )
            for event in self.events.values()
        ]

        # Add keyword argument names to `Event_{ID}(_, x, y, z)` calls and reformat call to multiple lines if necessary.
        # TODO: Does not catch calls that are already multi-line.
        for i in range(len(evs_events)):
            evs_events[i] = self.add_event_call_keywords(evs_events[i], enums_manager)

        if self.common_func_emevd and any("CommonFunc_" in event_string for event_string in evs_events):
            # TODO: pass real path (or attach to common EMEVD).
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

    def add_event_call_keywords(self, event_string: str, enums_manager: EntityEnumsManager):
        new_event_string = event_string

        for match in _EVENT_CALL_RE.finditer(event_string):
            if match.group(4) == "":
                continue  # no arguments
            indent = match.group(1)
            call_name = match.group(2)  # 'Event' or 'CommonFunc'
            event_id = int(match.group(3))
            end = match.group(5)  # newline or empty
            if call_name == "CommonFunc" and not self.common_func_emevd:
                continue  # cannot parse common event calls
            try:
                if call_name == "CommonFunc":
                    event_arg_names = self.common_func_emevd.all_event_arg_names[event_id]
                    event_arg_py_types = self.common_func_emevd.all_event_arg_types[event_id]
                else:  # standard local "Event"
                    event_arg_names = self.all_event_arg_names[event_id]
                    event_arg_py_types = self.all_event_arg_types[event_id]
            except KeyError:
                pass  # event ID not defined in this script or in CommonFunc
            else:
                args = match.group(4).replace(" ", "").replace("\n", "").split(",")
                if args[-1] == "":
                    args = args[:-1]
                if len(args) != len(event_arg_names) + 1:
                    if call_name == "CommonFunc":
                        _LOGGER.warning(f"Mismatch in defined/called event arg count for common func event {event_id}.")
                    else:
                        _LOGGER.warning(
                            f"Mismatch in defined/called event arg count for map event {event_id}.\n"
                            f"This is likely to be a serious problem for EVS compilation!"
                        )
                    continue
                slot = args[0]
                for j in range(1, len(args)):
                    if not event_arg_py_types[j - 1]:
                        continue  # no Python type hints for this argument
                    try:
                        int_value = int(args[j])
                    except ValueError:
                        continue
                    try:
                        args[j] = f"{enums_manager.check_out_enum(int_value, *event_arg_py_types[j - 1])}"
                    except enums_manager.MissingEntityError:
                        pass
                kwargs = [f"{arg_name}={arg_value}" for arg_name, arg_value in zip(event_arg_names, args[1:])]
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

    def pack(self):
        for event in self.events.values():
            event.process_all_event_args()

        event_table_binary = b""
        instr_table_binary = b""
        argument_data_binary = b""
        arg_r_binary = b""

        current_instruction_offset = 0
        current_arg_data_offset = 0
        current_event_arg_offset = 0

        header = self.build_emevd_header()

        for e_id, e in self.events.items():

            # print(f"Event {e_id}")

            e_bin, i_bin, a_bin, p_bin = e.to_binary(
                current_instruction_offset, current_arg_data_offset, current_event_arg_offset
            )

            event_table_binary += e_bin
            instr_table_binary += i_bin
            argument_data_binary += a_bin
            arg_r_binary += p_bin

            if len(i_bin) != self.Event.Instruction.HEADER_STRUCT.size * e.instruction_count:
                raise ValueError(
                    f"Event ID: {e.event_id} returned packed instruction binary of size {len(i_bin)} but "
                    f"reports {e.instruction_count} total instructions (with expected size "
                    f"{self.Event.Instruction.HEADER_STRUCT.size * e.instruction_count})."
                )
            if len(p_bin) != self.Event.EventArg.HEADER_STRUCT.size * e.event_arg_count:
                raise ValueError(
                    f"Event ID: {e.event_id} returned packed arg replacement binary of size {len(p_bin)} "
                    f"but reports {e.event_arg_count} total replacements (with expected size "
                    f"{self.Event.EventArg.HEADER_STRUCT.size * e.event_arg_count})."
                )
            if len(a_bin) != e.total_args_size:
                raise ValueError(
                    f"Event ID: {e.event_id} returned packed argument data binary of size {len(a_bin)} "
                    f"but reports expected size to be {e.total_args_size})."
                )

            current_instruction_offset += len(i_bin)
            current_arg_data_offset += len(a_bin)
            current_event_arg_offset += len(p_bin)

        linked_file_data_binary = struct.pack("<" + "Q" * len(self.linked_file_offsets), *self.linked_file_offsets)
        event_layers_table = self.build_event_layers_table()
        event_layers_binary = b"".join(event_layers_table)

        emevd_binary = b""
        offsets = self.compute_table_offsets(event_layers_table)
        if len(header) != offsets["event"]:
            raise ValueError(f"Header was of size {len(header)} but expected size was {self.HEADER_STRUCT.size}.")
        emevd_binary += header
        if len(emevd_binary) + len(event_table_binary) != offsets["instruction"]:
            raise ValueError(
                f"Event table was of size {len(event_table_binary)} but expected size was "
                f"{offsets['instruction'] - len(emevd_binary)}."
            )
        emevd_binary += event_table_binary
        if len(emevd_binary) + len(instr_table_binary) != offsets["event_layers"]:
            raise ValueError(
                f"Instruction table was of size {len(instr_table_binary)} but expected size was "
                f"{offsets['event_layers'] - len(emevd_binary)}."
            )
        emevd_binary += instr_table_binary
        if len(emevd_binary) + len(event_layers_binary) != offsets["base_arg_data"]:
            raise ValueError(
                f"Event layers table was of size {len(event_layers_binary)} but expected size was "
                f"{offsets['base_arg_data'] - len(emevd_binary)}."
            )

        emevd_binary += event_layers_binary

        # No argument data length check due to padding.
        emevd_binary += argument_data_binary
        emevd_binary = self.pad_after_base_args(emevd_binary)

        if len(emevd_binary) + len(arg_r_binary) != offsets["linked_files"]:
            raise ValueError(
                f"Argument replacement table was of size {len(linked_file_data_binary)} but expected size "
                f"was {offsets['linked_files'] - len(emevd_binary)}."
            )
        emevd_binary += arg_r_binary
        if len(emevd_binary) + len(linked_file_data_binary) != offsets["packed_strings"]:
            raise ValueError(
                f"Linked file data was of size {len(linked_file_data_binary)} but expected size was "
                f"{offsets['packed_strings'] - len(emevd_binary)}."
            )
        emevd_binary += linked_file_data_binary
        if len(emevd_binary) + len(self.packed_strings) != offsets["end_of_file"]:
            raise ValueError(
                f"Packed string data was of size {len(linked_file_data_binary)} but expected size was "
                f"{offsets['end_of_file'] - len(emevd_binary)}."
            )
        emevd_binary += self.packed_strings
        return emevd_binary

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
        is_common_func=False,
        docstring="",
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
            is_common_func,
            docstring,
        )
        with evs_path.open("w", encoding="utf-8") as f:
            f.write(evs_string)

    def merge(
        self,
        other_emevd_source: tp.Union[EMEVD, GameFile.Typing],
        merge_events=(0, 50),
        event_id_offset=0,
    ) -> EMEVD:
        """Return a new `EMEVD` creating by emerging all events of this instance with those of `other_emevd_source`.

        Event IDs in `merge_events` will have their instruction sets merged (with this instance's instrutions appearing
        first). By default, events 0 (constructor) and 50 (preconstructor) are merged this way. Any other event IDs that
        appear in both sources will raise a `ValueError`.

        Events from `other_emevd_source` will have `event_id_offset` added to their ID before being merged (default 0,
        so no change). This is useful for, say, defining some common events that will share an ID suffix across all
        maps. You will probably want to set `merge_events=()` for this use case.

        NOTE: Currently cannot merge any events that use event arguments.
        """
        if not isinstance(other_emevd_source, self.__class__):
            other_emevd_source = self.__class__(other_emevd_source)
        combined_emevd = self.copy()
        for event_id, other_event in other_emevd_source.events.items():
            event_id += event_id_offset
            if event_id not in combined_emevd.events:
                combined_emevd.events[event_id] = other_event
            elif event_id in merge_events:
                existing_event = combined_emevd.events[event_id]
                if existing_event.event_arg_count > 0 or other_event.event_arg_count > 0:
                    raise ValueError(
                        f"Cannot merge event {event_id}, as it uses event arguments in at least one source."
                    )
                existing_event.instructions += other_event.instructions
            else:
                raise ValueError(
                    f"Event {event_id} appears in both EMEVD sources and is not in allowed `merge_events`."
                )
        return combined_emevd

    def __add__(self, other_emevd_source: tp.Union[EMEVD, GameFile.Typing]) -> EMEVD:
        """Operator shortcut for merging EMEVD sources, merging the standard pre/constructor events `(0, 50)`."""
        return self.merge(other_emevd_source)
