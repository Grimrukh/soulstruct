from __future__ import annotations

__all__ = ["ESD"]

import abc
import ast
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import *

from .exceptions import ESDTypeError
from .command import Command
from .condition import Condition
from .state import State
from .esp_compiler import ESPCompiler
from .ezl_parser import SET_INTERNAL_SYMBOLS

try:
    Self = tp.Self
except AttributeError:
    Self = "ESD"

if tp.TYPE_CHECKING:
    from soulstruct.containers.dcx import DCXType

_LOGGER = logging.getLogger(__name__)

# TODO: (signature, version, internal_header_size, state_machine_header_size, state_size, condition_size, command_size,
#  command_arg_size)
#  Assign to each subclass and use to assert.
EXTERNAL_HEADER_INFO = ()


@dataclass(slots=True)
class ESDExternalHeaderStruct(NewBinaryStruct):
    """All offsets are relative to the END of this struct.

    The only difference between games thus far) is in the actual values of these `size` fields, and the case of the
    very first `signature`.

    Unlike the rest of the file, this header always uses 32-bit ints, even for the couple of offset fields it has.
    """
    signature: bytes = field(**Binary(length=4, asserted=[b"fSSL", b"fsSL"]))
    _one: int = field(**Binary(asserted=1))  # TODO: probably for indicating endianness
    game_version: tuple[int, int] = field(**Binary(asserted=[(1, 1), (2, 2), (3, 3)]))
    _table_size_offset: int = field(**Binary(asserted=84))
    internal_data_size: int  # excludes this header (i.e. EOF minus this header size)
    unk: int = field(**Binary(asserted=6))  # TODO: possibly 'table count'?
    internal_header_size: int  # post-asserted based on varint_size
    internal_header_count: int = field(**Binary(asserted=1))
    state_machine_header_size: int  # post-asserted based on varint_size
    state_machine_count: int
    state_size: int  # post-asserted based on varint_size
    state_count: int
    condition_size: int  # post-asserted based on varint_size
    condition_count: int
    command_size: int  # post-asserted based on varint_size
    command_count: int
    command_arg_size: int  # post-asserted based on varint_size
    command_arg_count: int
    condition_pointers_offset: int
    condition_pointers_count: int
    esd_name_offset_minus_1: int  # unclear why this is 1 less (internal header has accurate offset)
    esd_name_length: int
    unk_offset_1: int
    unk_size_1: int = field(**Binary(asserted=0))
    unk_offset_2: int
    unk_size_2: int = field(**Binary(asserted=0))


# Fields (table sizes) that vary depending on varint size, which is detected with `signature`.
EXTERNAL_HEADER_VARINT_ASSERTED = {
    4: {
        "signature": b"fSSL",
        "internal_header_size": 44,
        "state_machine_header_size": 16,
        "state_size": 36,
        "condition_size": 28,
        "command_size": 16,
        "command_arg_size": 8,
    },
    8: {
        "signature": b"fsSL",
        "internal_header_size": 72,
        "state_machine_header_size": 32,
        "state_size": 72,
        "condition_size": 56,
        "command_size": 24,
        "command_arg_size": 16,
    }
}

INTERNAL_HEADER_VARINT_ASSERTED = {
    4: {"state_machine_headers_offset": 44},
    8: {"state_machine_headers_offset": 72}
}


@dataclass(slots=True)
class ESDInternalHeaderStruct(NewBinaryStruct):
    _one: int = field(**Binary(asserted=1))
    magic: tuple[int, int, int, int]  # TODO: check if this is constant per game
    _pad1: bytes = field(**BinaryPad(4, skip_callback=lambda varint_size, _: varint_size == 4))
    state_machine_headers_offset: varint  # 44 or 72
    state_machine_count: varint  # same as external header
    esd_name_offset: varint  # accurate, unlike external header
    esd_name_length: varint
    _footer: tuple[varint, varint] = field(**Binary(asserted=[(-1, -1)]))


@dataclass(slots=True)
class StateMachineHeaderStruct(NewBinaryStruct):
    index: varint
    offset: varint
    state_count: varint
    offset_2: varint  # duplicate


@dataclass(slots=True)
class ESD(GameFile, abc.ABC):
    """An EzState state machine that controls character/bonfire interactions (TALK) or character animations (CHR)."""

    EXT = ".esd"
    DCX_TYPE: tp.ClassVar[DCXType]
    ESD_TYPE: tp.ClassVar[ESDType]

    magic: tuple[int, int, int, int] = ()
    file_tail: bytes = b"\0"  # default for files loaded from ESP, etc.
    esd_name: str = ""
    varint_size: int = 8

    # Maps state machine IDs to dictionaries mapping state IDs to `State` instances.
    # NOTE: Called `StateGroups` in SoulsFormats.
    state_machines: dict[int, dict[int, State]] = field(default_factory=dict)

    @classmethod
    def from_auto_detect_source_type(cls, esd_source: Path | str | bytes | BinaryReader) -> tuple[ESD, str]:
        if isinstance(esd_source, (Path, str)):
            esd_source = Path(esd_source)
            if esd_source.is_dir():
                try:
                    esd = cls.compile_from_esp_directory(esd_source)
                except Exception as ex:
                    raise ValueError(f"Error while parsing '{esd_source}' as ESP directory: {ex}")
                return esd, "esp_directory"
            for ext in (".esp.py", ".esp", ".py"):
                if esd_source.is_file() and esd_source.name.endswith(ext):
                    try:
                        esd = cls.compile_from_esp_single_file(esd_source)
                    except Exception as ex:
                        raise ValueError(f"Error encountered while parsing '{esd_source}' as single ESP file: {ex}")
                    return esd, "esp_file"
            # Otherwise, try ESD binary file.
            try:
                esd = cls.from_path(esd_source)
            except Exception as ex:
                raise ValueError(f"Error encountered while parsing '{esd_source}' as binary ESD file: {ex}")
            return esd, "esd"

        try:
            if isinstance(esd_source, BinaryReader):
                esd = cls.from_reader(esd_source)
                return esd, "esd"
            if isinstance(esd_source, bytes):
                esd = cls.from_bytes(esd_source)
                return esd, "esd"
        except Exception as ex:
            raise TypeError(f"Could not load binary `esd_source` as an ESD: {ex}")

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:

        # We need to consume the entire reader to handle the offsets (non-painfully), so this class does NOT support
        # the very rare usage case of reading it from some kind of conjoined data.
        # TODO: Could add some kind of persistent 'seek_offset' to `BinaryReader` to modify 'seek()` calls.
        if reader.position != 0:
            raise ValueError("Cannot read `ESD` from a reader that did not start at position 0.")

        # NOTE: big-endian not supported (or encountered). Consoles probably use it and `one` in external header is
        # probably a safe test for it.
        reader.default_byte_order = ByteOrder.LittleEndian

        # NOTE: We don't need to set `varint_size` for the brief existence of `reader` as the external header is 32-bit.
        signature = reader.peek(4)
        if signature == b"fSSL":
            varint_size = 4
        elif signature == b"fsSL":
            varint_size = 8
        else:
            raise ValueError(f"Invalid ESD file first four bytes: {signature}")

        header = ESDExternalHeaderStruct.from_bytes(reader)
        header.assert_field_values(**EXTERNAL_HEADER_VARINT_ASSERTED[varint_size])
        # Internal offsets start here, so we reset the reader to make these offsets naturally correct.
        reader = BinaryReader(reader.read(), default_byte_order=ByteOrder.LittleEndian, varint_size=varint_size)
        internal_header = ESDInternalHeaderStruct.from_bytes(reader)
        internal_header.assert_field_values(**INTERNAL_HEADER_VARINT_ASSERTED[varint_size])

        state_machine_header_structs = [
            StateMachineHeaderStruct.from_bytes(reader)
            for _ in range(header.state_machine_count)
        ]

        # NOTE: We do not care about maintaining reader offset beyond this point, so `seek()` is used frequently, both
        # here and in all the component class `from_esd_reader()` constructors.

        state_machines = {}
        for state_machine_header in state_machine_header_structs:
            if state_machine_header.index in state_machines:
                raise ValueError(f"State machine with index {state_machine_header.index} appeared more than once.")
            reader.seek(state_machine_header.offset)
            states = {}
            for _ in range(state_machine_header.state_count):
                # State construction will recursively unpack all other data (Conditions, Commands, etc.) as they apepar.
                state = State.from_esd_reader(reader)
                if state.index in states and state.index != 0:
                    # State 0 repeats at the end of the table, for some reason, but other states should not.
                    _LOGGER.warning(
                        f"State {state.index} in {state_machine_header.index} appeared multiple times. Using first "
                        f"only."
                    )
                else:
                    states[state.index] = state
            state_machines[state_machine_header.index] = states

        if internal_header.esd_name_length > 0:
            # Note the given length is the number of characters in the final string.
            # The actual UTF-16 encoded bytes are twice that size.
            reader.seek(internal_header.esd_name_offset)
            esd_name = reader.unpack_string(length=2 * internal_header.esd_name_length, encoding="utf-16-le")
            file_tail = reader.read()  # remainder of file
        else:
            esd_name = ""
            reader.seek(header.unk_offset_1)  # after packed EZL
            file_tail = reader.read()  # remainder of file

        return cls(internal_header.magic, file_tail, esd_name, varint_size, state_machines)

    @classmethod
    def compile_from_esp_directory(cls, esp_directory: Path | str) -> Self:
        esp_directory = Path(esp_directory)

        header_path = list(esp_directory.glob("ESD_Header*"))
        if not header_path:
            raise FileNotFoundError("Could not find 'ESD_Header' file in directory.")
        esd_name, magic = cls.read_esp_header(header_path[0])

        state_machines = {}
        for esp_path in esp_directory.glob("StateMachine_*"):
            _LOGGER.info(f"Compiling ESD state machine: {esp_path.name}")
            esp_match = re.match(r"StateMachine_(x?)(\d*)(\.esp)?(\.py)?", esp_path.name)
            if esp_match is None:
                raise ValueError(
                    f"State machine resources should all be in format 'StateMachine_i.esp.py' for main "
                    f"machines or 'StateMachine_xi.esp.py' for callable machines, not '{esp_path.name}'."
                )
            if esp_match.group(1) == "x":
                state_machine_index = 0x80000000 - int(esp_match.group(2))
            else:
                state_machine_index = int(esp_match.group(2))
            compiler = ESPCompiler(esp_path, cls.ESD_TYPE)
            state_machines[state_machine_index] = compiler.states

        esd = cls(magic, esd_name=esd_name, state_machines=state_machines)
        esd.path = esp_directory.name
        return esd

    @classmethod
    def compile_from_esp_single_file(cls, esp_file) -> Self:
        """TODO: Surely I can put magic in ESP file docstring?"""
        esp_file = Path(esp_file)
        _LOGGER.debug(f"Compiling single-file ESD state machine: {esp_file.name}")
        compiler = ESPCompiler(esp_file, cls.ESD_TYPE)
        esd = cls(magic=(0, 0, 0, 0), esd_name=esp_file.stem + cls.EXT, state_machines={1: compiler.states})
        esd.path = esp_file.parent / esd.esd_name
        return esd

    @classmethod
    def read_esp_header(cls, header_path: Path) -> tuple[str, tuple[int, int, int, int]]:
        with header_path.open("r") as f:
            for line in f:
                line = line.strip(" \r\n")
                if not line:
                    continue
                if line.startswith("ESD_NAME = "):
                    esd_name = ast.literal_eval(line[len("ESD_NAME = "):])
                elif line.startswith("ESD_TYPE = "):
                    esd_type = ESDType(ast.literal_eval(line[len("ESD_TYPE = "):]))
                    if esd_type != cls.ESD_TYPE:
                        raise ESDTypeError(
                            f"ESP file ESD_TYPE is {esd_type}. Cannot load with {cls.__name__}."
                        )
                elif line.startswith("MAGIC = "):
                    magic_str = line[len("MAGIC = "):]
                    try:
                        magic = tuple(ast.literal_eval(magic_str))
                    except ValueError:
                        raise ValueError(f"Could not read MAGIC value from ESD_Header: {magic_str}")
                else:
                    raise ValueError(f"Invalid ESD Header line: {line}")
        if len(magic) != 4:
            raise ValueError(f"MAGIC should be a four-element sequence.")

        return esd_name, magic

    def to_writer(self) -> BinaryWriter:
        """Packs tables and computes new byte offsets for them."""
        # TODO: is 'existing commands' a thing for enemyCommon.esd? Probably, but only for efficiency.

        # TODO:
        """
        - Pack external header.
        - Pack internal header.
        
        - Pack state machine headers.
        
        
        - Pack State headers.
            - Reserve offsets for `condition_pointers`, `enter/exit/ongoing_commands`.
            
        - Create 'existing condition' dictionary that maps Condition instances to writer offsets.
        
        - Pack Condition headers by:
            - Iterate over States and pack all Conditions in each. 
            - If a Condition is already in 'existing conditions', just use that for state 'condition pointers'.
            - Otherwise, pack condition:
                - Reserve offsets for 
        """

        # External header is constructed last, as all offsets are relative to the end of it.
        external_header_writer = ESDExternalHeaderStruct.object_to_writer(
            self,
            esd_name_length=len(self.esd_name) * 2,  # size of UTF-16 encoded bytes
            state_machine_count=len(self.state_machines),  # also appears in internal header
            # Other counts reserved.
            **EXTERNAL_HEADER_VARINT_ASSERTED[self.varint_size],
        )

        # Pack internal header. This is the writer we use throughout, except when filling external header offsets.
        writer = ESDInternalHeaderStruct.object_to_writer(
            self,
            byte_order=ByteOrder.LittleEndian,
            varint_size=self.varint_size,
            state_machine_count=len(self.state_machines),  # also appears in external header
            esd_name_length=len(self.esd_name) * 2,  # size of UTF-16 encoded bytes
            **INTERNAL_HEADER_VARINT_ASSERTED[self.varint_size],
        )

        for state_machine_index, states in self.state_machines.items():
            StateMachineHeaderStruct.object_to_writer(
                self,
                writer,
                index=state_machine_index,
                offset=RESERVED,
                state_count=len(states),
                offset_2=RESERVED,  # same as `offset`
            )

        # For `next_state_offset` of Conditions.
        state_index_offsets = {}  # type: dict[int, int]

        all_states = []  # for ease below
        for states in self.state_machines.values():
            for state_index, state in states.items():
                state_index_offsets[state.index] = writer.position
                state.to_esd_writer(writer)
                all_states.append(state)
        external_header_writer.fill("state_count", len(all_states), self)

        # Offsets of existing Conditions, which can be re-used across States if they are identical.
        all_condition_offsets = {}  # type: dict[Condition, int]

        # Pack Conditions.
        for state in all_states:
            state.pack_conditions(writer, state_index_offsets, all_condition_offsets)
        external_header_writer.fill("condition_count", len(all_condition_offsets), self)
        # Pack Commands.
        command_count = 0
        for state in all_states:
            command_count += state.pack_commands(writer)
        external_header_writer.fill("command_count", command_count, self)
        # Pack Command arg offsets.
        command_arg_count = 0
        for state in all_states:
            command_arg_count += state.pack_command_args(writer)
        external_header_writer.fill("command_arg_count", command_count, self)
        # Pack Condition pointers.
        condition_pointers_count = 0
        external_header_writer.fill("condition_pointers_offset", writer.position, self)
        for state in all_states:
            condition_pointers_count += state.pack_condition_pointers(writer, all_condition_offsets)
        external_header_writer.fill("condition_pointers_count", command_count, self)
        # Pack Condition test EZL data.
        for state in all_states:
            state.pack_condition_test_data(writer)
        # Pack Command arg EZL data.
        for state in all_states:
            state.pack_command_arg_data(writer)

        if self.esd_name:
            external_header_writer.fill("esd_name_offset_minus_1", writer.position - 1, self)
            writer.fill_with_position("esd_name_offset", self)
            writer.fill_with_position("unk_offset_1", self)
            writer.append(self.esd_name.encode("utf-16-le"))
        # Otherwise, EOF file offset written to both below.

        writer.fill_with_position("unk_offset_2", self)
        if not self.file_tail:
            writer.append(b"\0")  # MUST have at least one null byte after name (e.g. for SoulsFormats)
        writer.append(self.file_tail)

        external_header_writer.fill("internal_data_size", writer.position, self)
        if not self.esd_name:
            external_header_writer.fill("esd_name_offset_minus_1", writer.position, self)
            writer.fill_with_position("esd_name_offset", self)

        # TODO: Old -- only kept until new tested.
        # tables = _ESDPacker(self)
        # external_header = self.EXTERNAL_HEADER_STRUCT.pack(tables.external_header)
        # packed = b""
        # packed += self.INTERNAL_HEADER_STRUCT.pack(tables.internal_header)
        # for sm_i, sm in tables.state_machine_headers.items():
        #     assert len(packed) == tables.offsets["state_machine_headers"][sm_i]
        #     packed += self.STATE_MACHINE_HEADER_STRUCT.pack(sm)
        # for sm_i, sm in tables.state_machines.items():
        #     assert len(packed) == tables.offsets["state_machines"][sm_i]
        #     packed += self.State.STRUCT.pack_multiple(sm)
        # assert len(packed) == tables.offsets["conditions"]
        # packed += self.State.Condition.STRUCT.pack_multiple(tables.conditions)
        # assert len(packed) == tables.offsets["commands"]
        # packed += self.State.Command.STRUCT.pack_multiple(tables.commands)
        # assert len(packed) == tables.offsets["command_args"]
        # packed += self.State.Command.ARG_STRUCT.pack_multiple(tables.command_args)
        # assert len(packed) == tables.offsets["condition_pointers"]
        # packed += self.State.Condition.POINTER_STRUCT.pack_multiple(tables.condition_pointers)
        # assert len(packed) == tables.offsets["ezl"]
        # packed += tables.ezl
        # assert len(packed) == tables.offsets["esd_name"]
        # packed += tables.esd_name
        # assert len(packed) == tables.offsets["file_tail"]
        # packed += tables.file_tail
        # return external_header + packed

        return writer

    def get_next_states(self, condition: Condition):
        next_states = []
        for subcondition in condition.subconditions:
            next_states += self.get_next_states(subcondition)
        if condition.next_state_index != -1:
            next_states.append(condition.next_state_index)
        return next_states

    def to_esp(self, state_machine_index=1):
        """Writes each state machine to a separate script."""
        # Scan each state to build 'from' lists.
        from_states = {}
        for i, state in self.state_machines[state_machine_index].items():
            for condition in state.conditions:
                for next_state in self.get_next_states(condition):
                    from_states.setdefault(next_state, set()).add(i)
        s = f"from soulstruct.{self.get_game().submodule_name}.ezstate.esd import *\n\n"
        for i, state in self.state_machines[state_machine_index].items():
            s += state.to_esp(from_states=from_states.get(i, None))
        s = s.strip("\n") + "\n"  # End with just one newline.
        return s

    def write_esp(self, esp_directory=None, force_folder=False):
        """Write ESD to a collection of Python-like 'ESP' scripts (one per state machine) in the specified folder.

        If only one state machine is present and `esd_type` is 'talk', it will be written to a single file in the given
        directory named after the internal name (discarding any junk at the end of it), with the unknown 'magic' bytes
        discarded (neither the internal name nor magic matters in-game). You can disable this behavior and force an ESP
        folder to be written even in this case by setting `force_folder=True`.
        """
        if esp_directory is None:
            esp_directory = self.path
            if not esp_directory.suffix == ".esp":
                esp_directory = esp_directory.with_suffix(esp_directory.suffix + ".esp")
        else:
            esp_directory = Path(esp_directory)

        single_file = (
            len(self.state_machines) == 1
            and 1 in self.state_machines
            and self.ESD_TYPE == ESDType.TALK
            and not esp_directory.is_dir()
            and not force_folder
        )

        # TODO: read from single file

        if single_file:
            # Write single 'talk' state machine to a single ESP file.
            if esp_directory.suffix != ".py":
                esp_directory = esp_directory.with_suffix(esp_directory.suffix + ".py")
            esp_directory.parent.mkdir(parents=True, exist_ok=True)
            with esp_directory.open(mode="w", encoding="utf-8") as esp_file:
                state_machine_py = self.to_esp(1)
                esp_file.write(state_machine_py)
            return

        esp_directory.mkdir(parents=True, exist_ok=True)
        for i, state_machine in self.state_machines.items():
            if i >= 0x70000000:
                # 'Callable' state machine.
                state_machine_path = esp_directory / f"StateMachine_x{0x80000000 - i}.esp.py"
            else:
                # Primary state machine.
                state_machine_path = esp_directory / f"StateMachine_{i}.esp.py"
            with state_machine_path.open(mode="w", encoding="utf-8") as state_machine_file:
                state_machine_py = self.to_esp(i)
                state_machine_file.write(state_machine_py)
        header = (
            f"ESD_NAME = {repr(self.esd_name)}\n"
            f"ESD_TYPE = {repr(self.ESD_TYPE.name)}\n"
            f"MAGIC = {repr(self.magic)}\n"
        )
        with (esp_directory / "ESD_Header.esp.py").open(mode="w", encoding="utf-8") as header_file:
            header_file.write(header)

    def to_html(self):

        SET_INTERNAL_SYMBOLS(True)

        html = (
            "<html><head></head><body>"
            '<meta charset="shift_jis_2004"><br>'
            "NOTES:<br>"
            "  <b>&</b>: this expression has been evaluated in a previous condition of this state, and loaded<br>"
            "  here from one of eight registers. (We currently believe this is only used for function calls,<br>"
            "  so if you see it used with any other type of expression, please show us!)<br>"
            "  <b>...</b>: interpreter should continue even if the previous value is false. (This seems to be<br>"
            "  the default behavior anyway, so this symbol seems useless, and I haven't been able to detect<br>"
            "  a pattern for when it's actually used.)<br>"
            "  <b>!</b>: interpreter should stop if the previous value is false. (Optimizes 'and' operations,<br>"
            "  but not if there's a register save to be done later in the test script.)<br>"
        )

        for state_machine in self.state_machines.values():
            for state in state_machine.values():
                html += state.to_html()

        SET_INTERNAL_SYMBOLS(False)

        return html + "</body></html>"

    def write_html(self, html_path=None):
        if html_path is None:
            html_path = self.path.with_suffix(self.path.suffix + ".html")
        else:
            html_path = Path(html_path)
        with html_path.open(mode="w", encoding="shift_jis_2004") as output_file:
            output_file.write(self.to_html())


class _ESDPacker:
    """Utility one-shot class for packing an `ESD` instance into binary, which is a complicated process."""

    # TODO: Probably delay rework of this. Can calculate the size of the various structs for now.

    def __init__(self, esd: ESD):
        self.__updated = False
        self.esd = esd

        # Various constants.
        self.magic = esd.magic
        self.esd_name = esd.esd_name.encode("utf-16-le")
        self.file_tail = esd.file_tail

        self.state_machine_headers = {}
        self.state_machines = {}
        self.conditions = []
        self.commands = []
        self.command_args = []
        self.condition_pointers = []  # only table that is simply an integer sequence for direct packing
        self.ezl = b""  # packed byte code language for command arguments and condition tests

        self.state_indices = {}  # {state_index: state_index_in_sequence}  (in case state indices are missing)

        self.offsets = {
            "state_machine_headers": {},  # index: offset
            "state_machines": {},  # index: offset
            "conditions": 0,
            "commands": 0,
            "command_args": 0,
            "condition_pointers": 0,
            "ezl": 0,
            "esd_name": 0,
            "file_tail": 0,
            "end_of_file": 0,
        }

        # Build tables with relative within-table offsets.
        for state_machine_index, state_machine in esd.state_machines.items():
            self.current_state_machine_index = state_machine_index
            self.existing_condition_pointers = {}  # TODO: Current resetting it for every state machine.
            self.state_machines[state_machine_index] = self.build_state_machine(state_machine)
            state_count = len({sm["index"] for sm in self.state_machines[state_machine_index]})  # duplicate 0 excluded
            self.state_machine_headers[state_machine_index] = {
                "state_machine_index": state_machine_index,  # index starts at 1
                "state_machine_offset": len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size,
                "state_count": state_count,
                "state_machine_offset_2": len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size,
            }

        self.__update_offsets()

        self.__update_tables()

        self.external_header = {
            "internal_data_size": self.offsets["end_of_file"],  # excludes external header
            "state_machine_count": len(self.state_machine_headers),
            "state_count": sum([len(sm) for sm in self.state_machines.values()]),  # includes repeated state
            "condition_count": len(self.conditions),
            "command_count": len(self.commands),
            "command_arg_count": len(self.command_args),
            "condition_pointers_offset": self.offsets["condition_pointers"],
            "condition_pointers_count": len(self.condition_pointers),
            "esd_name_offset_minus_1": self.offsets["esd_name"] - 1 if self.esd_name else self.offsets["end_of_file"],
            "esd_name_length": len(self.esd_name) // 2,
            "unk_offset_1": self.offsets["esd_name"] if self.esd_name else self.offsets["end_of_file"],
            "unk_offset_2": self.offsets["file_tail"],
        }

        self.internal_header = {
            "magic": self.magic,
            "state_machine_count": len(self.state_machine_headers),
            "esd_name_offset": self.offsets["esd_name"] if self.esd_name else self.offsets["end_of_file"],
            "esd_name_length": len(self.esd_name) // 2,
        }

    def __update_offsets(self):
        state_machine_headers_offset = self.esd.INTERNAL_HEADER_STRUCT.size
        for state_machine_index in self.state_machine_headers:
            self.offsets["state_machine_headers"][state_machine_index] = (
                state_machine_headers_offset
                + len(self.offsets["state_machine_headers"]) * self.esd.STATE_MACHINE_HEADER_STRUCT.size
            )
        state_machines_offset = (
            state_machine_headers_offset + len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size
        )
        state_machine_total_size = 0
        for state_machine_index, sm in self.state_machines.items():
            self.offsets["state_machines"][state_machine_index] = state_machines_offset + state_machine_total_size
            state_machines_offset += len(sm) * self.State.STRUCT.size
        self.offsets["conditions"] = state_machines_offset + state_machine_total_size
        self.offsets["commands"] = self.offsets["conditions"] + len(self.conditions) * self.Condition.STRUCT.size
        self.offsets["command_args"] = self.offsets["commands"] + len(self.commands) * self.Command.STRUCT.size
        self.offsets["condition_pointers"] = (
            self.offsets["command_args"] + len(self.command_args) * self.Command.ARG_STRUCT.size
        )
        self.offsets["ezl"] = (
            self.offsets["condition_pointers"] + len(self.condition_pointers) * self.Condition.POINTER_STRUCT.size
        )
        self.offsets["esd_name"] = self.offsets["ezl"] + len(self.ezl)
        self.offsets["file_tail"] = self.offsets["esd_name"] + len(self.esd_name)
        self.offsets["end_of_file"] = self.offsets["file_tail"] + len(self.file_tail)

    def __update_tables(self):
        if self.__updated:
            raise ValueError("ESDPacker has already updated the tables.")
        for sm_index, header in self.state_machine_headers.items():
            header["state_machine_offset"] = header["state_machine_offset_2"] = self.offsets["state_machines"][sm_index]
        for sm in self.state_machines.values():
            states_done = set()
            for state in sm:
                if state["index"] not in states_done:
                    if state["condition_pointers_offset"] >= 0:
                        state["condition_pointers_offset"] += self.offsets["condition_pointers"]
                    if state["enter_commands_offset"] >= 0:
                        state["enter_commands_offset"] += self.offsets["commands"]
                    if state["exit_commands_offset"] >= 0:
                        state["exit_commands_offset"] += self.offsets["commands"]
                    if state["ongoing_commands_offset"] >= 0:
                        state["ongoing_commands_offset"] += self.offsets["commands"]
                    states_done.add(state["index"])
        for condition in self.conditions:
            state_machine_index = condition.pop("__state_machine_index__")
            state_machine_offset = self.offsets["state_machines"][state_machine_index]
            if condition["next_state_offset"] >= 0:
                # 'next_state_offset' is actually an absolute state index before this.
                relative_state_offset = self.state_indices[condition["next_state_offset"]] * self.State.STRUCT.size
                condition["next_state_offset"] = state_machine_offset + relative_state_offset
            if condition["pass_commands_offset"] >= 0:
                condition["pass_commands_offset"] += self.offsets["commands"]
            if condition["subcondition_pointers_offset"] >= 0:
                condition["subcondition_pointers_offset"] += self.offsets["condition_pointers"]
            if condition["test_ezl_offset"] >= 0:
                condition["test_ezl_offset"] += self.offsets["ezl"]
        for command in self.commands:
            if command["args_offset"] >= 0:
                command["args_offset"] += self.offsets["command_args"]
        for command_arg in self.command_args:
            command_arg["arg_ezl_offset"] += self.offsets["ezl"]
        for condition_pointer in self.condition_pointers:
            condition_pointer["condition_offset"] += self.offsets["conditions"]
        self.__updated = True

    def build_state_machine(self, state_machine: dict):
        built = []
        for index, state in state_machine.items():
            self.state_indices[index] = len(built)
            built_state = self.build_state(index, state)
            built.append(built_state)
        if len(built) > 1:
            built.append(built[0])  # First state (generally index 0) repeats at end of table (if not alone).
        return built

    def build_state(self, index: int, state: State):
        built = {
            "index": index,
            "condition_pointers_offset": None,
            "condition_pointers_count": None,
            "enter_commands_offset": None,
            "enter_commands_count": None,
            "exit_commands_offset": None,
            "exit_commands_count": None,
            "ongoing_commands_offset": None,
            "ongoing_commands_count": None,
        }

        condition_pointers_offset, condition_pointers_count = self.build_condition_list(state.conditions)
        built["condition_pointers_offset"] = condition_pointers_offset if condition_pointers_count > 0 else -1
        built["condition_pointers_count"] = condition_pointers_count

        enter_commands = []
        for enter_command in state.enter_commands:
            enter_commands.append(self.build_command(enter_command))
        built["enter_commands_offset"] = enter_commands[0] if enter_commands else -1
        built["enter_commands_count"] = len(enter_commands)

        exit_commands = []
        for exit_command in state.exit_commands:
            exit_commands.append(self.build_command(exit_command))
        built["exit_commands_offset"] = exit_commands[0] if exit_commands else -1
        built["exit_commands_count"] = len(exit_commands)

        ongoing_commands = []
        for ongoing_command in state.ongoing_commands:
            ongoing_commands.append(self.build_command(ongoing_command))
        built["ongoing_commands_offset"] = ongoing_commands[0] if ongoing_commands else -1
        built["ongoing_commands_count"] = len(ongoing_commands)

        return built

    def build_condition_list(self, condition_list):
        """ Ensures that adjacent conditions are built sequentially before blocks of subconditions. """
        condition_pointers = []
        subconditions_to_build = []
        for condition in condition_list:
            condition_pointer_offset, condition_dict, subconditions = self.build_condition(condition)
            condition_pointers.append(condition_pointer_offset)
            if condition_dict is not None:
                subconditions_to_build.append((condition_dict, subconditions))

        for condition_dict, subconditions in subconditions_to_build:
            offset, count = self.build_condition_list(subconditions)
            condition_dict["subcondition_pointers_offset"] = offset
            condition_dict["subcondition_pointers_count"] = count

        return (condition_pointers[0] if condition_pointers else -1), len(condition_pointers)

    def build_condition(self, condition: Condition):

        built = {
            "__state_machine_index__": self.current_state_machine_index,  # removed later
            "next_state_offset": condition.next_state_index,  # converted to offset later
            "pass_commands_offset": None,
            "pass_commands_count": None,
            "subcondition_pointers_offset": None,
            "subcondition_pointers_count": None,
            "test_ezl_offset": None,
            "test_ezl_size": None,
        }

        pass_commands = []
        for pass_command in condition.pass_commands:
            pass_commands.append(self.build_command(pass_command))
        built["pass_commands_offset"] = pass_commands[0] if pass_commands else -1
        built["pass_commands_count"] = len(pass_commands)

        # TODO: Need to pack conditions breadth-first rather than depth-first...
        subconditions_to_build = list(condition.subconditions)

        built["test_ezl_offset"] = self.build_ezl(condition.test_ezl)
        built["test_ezl_size"] = len(condition.test_ezl)

        this_pointer_offset = len(self.condition_pointers) * self.Condition.POINTER_STRUCT.size
        if condition in self.existing_condition_pointers:
            self.condition_pointers.append({"condition_offset": self.existing_condition_pointers[condition]})
            return this_pointer_offset, None, None

        this_condition_offset = len(self.conditions) * self.Condition.STRUCT.size
        self.condition_pointers.append({"condition_offset": this_condition_offset})
        self.conditions.append(built)
        self.existing_condition_pointers[condition] = this_condition_offset
        return this_pointer_offset, built, subconditions_to_build

    def build_command(self, command: Command):
        this_command_offset = len(self.commands) * self.Command.STRUCT.size
        built = {
            "bank": command.bank,
            "index": command.index,
            "args_offset": len(self.command_args) * self.Command.ARG_STRUCT.size if command.args else -1,
            "args_count": len(command.args),
        }
        for arg in command.args:
            self.command_args.append({"arg_ezl_offset": self.build_ezl(arg), "arg_ezl_size": len(arg)})
        self.commands.append(built)
        return this_command_offset

    def build_ezl(self, ezl_bytes):
        # TODO: Conditions and commands are currently intermingled (ordered by state), which is not true for the
        #  original resources (where all condition data comes before all command data), but it shouldn't matter at all.
        this_offset = len(self.ezl)
        self.ezl += ezl_bytes
        return this_offset

    @property
    def State(self):
        return self.esd.State

    @property
    def Condition(self):
        return self.esd.State.Condition

    @property
    def Command(self):
        return self.esd.State.Command
