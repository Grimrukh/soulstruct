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
from .condition import Condition
from .state import State
from .esp_compiler import ESPCompiler
from .ezl_parser import SET_INTERNAL_SYMBOLS

try:
    Self = tp.Self
except AttributeError:
    Self = "ESD"

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class ESDExternalHeaderStruct(BinaryStruct):
    """All offsets are relative to the END of this struct.

    The only difference between games thus far) is in the actual values of these `size` fields, and the case of the
    very first `signature`.

    Unlike the rest of the file, this header always uses 32-bit ints, even for the couple of offset fields it has.
    """
    signature: bytes = field(**BinaryString(4, asserted=[b"fSSL", b"fsSL"]))
    _one: int = field(**Binary(asserted=1))  # TODO: probably for indicating endianness
    game_version: list[int] = field(**BinaryArray(2, asserted=([1, 1], [2, 2], [3, 3])))
    _table_size_offset: int = field(**Binary(asserted=84))
    internal_data_size: int  # excludes this header (i.e. EOF minus this header size)
    unk: int = field(**Binary(asserted=6))  # TODO: possibly 'table count'?
    internal_header_size: int  # post-asserted based on varint size
    internal_header_count: int = field(**Binary(asserted=1))
    state_machine_header_size: int  # post-asserted based on varint size
    state_machine_count: int
    state_size: int  # post-asserted based on varint size
    state_count: int
    condition_size: int  # post-asserted based on varint size
    condition_count: int
    command_size: int  # post-asserted based on varint size
    command_count: int
    command_arg_size: int  # post-asserted based on varint size
    command_arg_count: int
    condition_pointers_offset: int
    condition_pointers_count: int
    tail_offset: int  # points to just before actual name
    esd_name_length: int
    unk_offset_1: int
    unk_size_1: int = field(**Binary(asserted=0))
    unk_offset_2: int
    unk_size_2: int = field(**Binary(asserted=0))


# Fields (table sizes) that vary depending on varint size, which is detected with `signature`.
EXTERNAL_HEADER_VARINT_ASSERTED = {
    False: {
        "signature": b"fSSL",
        "internal_header_size": 44,
        "state_machine_header_size": 16,
        "state_size": 36,
        "condition_size": 28,
        "command_size": 16,
        "command_arg_size": 8,
    },
    True: {
        "signature": b"fsSL",
        "internal_header_size": 72,
        "state_machine_header_size": 32,
        "state_size": 72,
        "condition_size": 56,
        "command_size": 24,
        "command_arg_size": 16,
    }
}


@dataclass(slots=True)
class ESDInternalHeaderStruct(BinaryStruct):
    _one: int = field(**Binary(asserted=1))
    magic: list[int] = field(**BinaryArray(4))  # TODO: check if this is constant per game
    _pad1: bytes = field(**BinaryPad(4, should_skip_func=lambda long_varints, _: not long_varints))
    state_machine_headers_offset: varint  # 44 or 72
    state_machine_count: varint  # same as external header
    esd_name_offset: varint  # accurate, unlike external header
    esd_name_length: varint  # same as value in external header
    footer: list[varint] = field(**BinaryArray(2, asserted=([0, 0], [-1, -1])))  # [0, 0] in PTDE/DSR only


INTERNAL_HEADER_VARINT_ASSERTED = {
    # NOTE: We can't assert `footer` here as it depends on `game_version`, not `long_varints`.
    False: {"state_machine_headers_offset": 44},
    True: {"state_machine_headers_offset": 72},
}


@dataclass(slots=True)
class StateMachineHeaderStruct(BinaryStruct):
    index: varint
    states_offset: varint
    state_count: varint
    states_offset_2: varint  # duplicate


@dataclass(slots=True)
class ESD(GameFile, abc.ABC):
    """An EzState state machine that controls character/bonfire interactions (TALK) or character animations (CHR)."""

    EXT: tp.ClassVar[str] = ".esd"
    ESD_TYPE: tp.ClassVar[ESDType]
    VERSION: tp.ClassVar[int]  # used to assert binary `game_version` and a few other connected fields
    LONG_VARINTS: tp.ClassVar[bool]

    magic: list[int] = field(default_factory=lambda: [0] * 4)
    esd_name: str = ""
    # Maps state machine IDs to dictionaries mapping state IDs to `State` instances.
    # NOTE: Called `StateGroups` in SoulsFormats.
    state_machines: dict[int, dict[int, State]] = field(default_factory=dict)

    @classmethod
    def from_auto_detect_source_type(cls, esd_source: Path | str | bytes | BinaryReader) -> tuple[ESD, str]:
        if isinstance(esd_source, (Path, str)):
            esd_source = Path(esd_source)
            if esd_source.is_dir():
                try:
                    esd = cls.from_esp_directory(esd_source)
                except Exception as ex:
                    raise ValueError(f"Error while parsing '{esd_source}' as ESP directory: {ex}")
                return esd, "esp_directory"
            for ext in (".esp.py", ".esp", ".py"):
                if esd_source.is_file() and esd_source.name.endswith(ext):
                    try:
                        esd = cls.from_esp_file(esd_source)
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
        reader.long_varints = cls.LONG_VARINTS

        header = ESDExternalHeaderStruct.from_bytes(reader)
        header.assert_field_values(
            game_version=[cls.VERSION, cls.VERSION],
            **EXTERNAL_HEADER_VARINT_ASSERTED[cls.LONG_VARINTS],
        )

        # Internal offsets start here, so we reset the reader to make these offsets naturally correct.
        reader = BinaryReader(reader.read(), default_byte_order=ByteOrder.LittleEndian, long_varints=cls.LONG_VARINTS)

        internal_header = ESDInternalHeaderStruct.from_bytes(reader)
        internal_header.assert_field_values(
            footer=[0, 0] if cls.VERSION == 1 else [-1, -1],
            **INTERNAL_HEADER_VARINT_ASSERTED[cls.LONG_VARINTS]
        )
        state_machine_header_structs = [
            StateMachineHeaderStruct.from_bytes(reader)
            for _ in range(header.state_machine_count)
        ]

        state_machines = {}
        for state_machine_header in state_machine_header_structs:
            if state_machine_header.index in state_machines:
                raise ValueError(f"State machine with index {state_machine_header.index} appeared more than once.")
            reader.seek(state_machine_header.states_offset)
            states = {}
            for _ in range(state_machine_header.state_count):
                # State construction will recursively unpack all other data (Conditions, Commands, etc.) as they appear.
                # NOTE: State machines with more than one State have a completely identical copy of the first state at
                # the end of the machine. This contributes to `total_state_count` in the file, but not the state machine
                # header itself, and will therefore not be unpacked (or even asserted) here.
                state = State.from_esd_reader(reader)
                if state.state_id in states:
                    # First state (index 0) repeats at the end, for some reason, but other states should not.
                    if state.state_id != list(states.keys())[0]:
                        _LOGGER.warning(
                            f"State {state.state_id} in {state_machine_header.index} appeared multiple times. "
                            f"Using first only."
                        )
                    # Otherwise, ignore duplicate first state.
                else:
                    states[state.state_id] = state
            state_machines[state_machine_header.index] = states

        if internal_header.esd_name_length > 0:
            # Note the given length is the number of characters in the final string.
            # The actual UTF-16 encoded bytes are twice that size.
            reader.seek(internal_header.esd_name_offset)
            esd_name = reader.unpack_string(length=2 * internal_header.esd_name_length, encoding="utf-16-le")
        else:
            esd_name = ""

        return cls(magic=internal_header.magic, esd_name=esd_name, state_machines=state_machines)

    @classmethod
    def from_esp_directory(cls, esp_directory: Path | str) -> Self:
        """Load `ESD` instance from a directory of ESP scripts (one per state machine) with an `ESD_Header` file."""
        esp_directory = Path(esp_directory)

        header_path = list(esp_directory.glob("ESD_Header*"))
        if not header_path:
            raise FileNotFoundError("Could not find 'ESD_Header' file in directory.")
        esd_name, magic = cls.read_esp_header(header_path[0])

        state_machines = {}
        for esp_path in esp_directory.glob("StateMachine_*"):
            # TODO: Also writing state machine index to docstring. Can use that...
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

        esd = cls(magic=list(magic), esd_name=esd_name, state_machines=state_machines)
        esd.path = esp_directory.name
        return esd

    @classmethod
    def from_esp_file(cls, esp_file: Path | str) -> Self:
        """TODO: Surely I can put magic in ESP file docstring?"""
        esp_file = Path(esp_file)
        _LOGGER.debug(f"Compiling single-file ESD state machine: {esp_file.name}")
        compiler = ESPCompiler(esp_file, cls.ESD_TYPE)
        # TODO: Read state machine index from docstring. Only default to 1 (and warn) if necessary.
        esd = cls(
            magic=[0, 0, 0, 0],
            esd_name=esp_file.name.split(".")[0] + cls.EXT,  # makes sure to remove '.esp' and '.py' suffix, etc.
            state_machines={1: compiler.states},
        )
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

        # External header is constructed last, as all offsets are relative to the end of it.
        external_header_writer = ESDExternalHeaderStruct.object_to_writer(
            self,
            byte_order=ByteOrder.LittleEndian,  # big-endian versions not handled
            long_varints=self.LONG_VARINTS,
            esd_name_length=len(self.esd_name) // 2,  # number of UTF-16 characters, NOT size of encoded bytes
            state_machine_count=len(self.state_machines),  # also appears in internal header
            game_version=[self.VERSION, self.VERSION],
            **EXTERNAL_HEADER_VARINT_ASSERTED[self.LONG_VARINTS],
            # All other fields reserved.
        )

        # Pack internal header. This is the writer we use throughout, except when filling external header offsets.
        writer = ESDInternalHeaderStruct.object_to_writer(
            self,
            byte_order=ByteOrder.LittleEndian,
            long_varints=self.LONG_VARINTS,
            state_machine_count=len(self.state_machines),  # also appears in external header
            esd_name_offset=RESERVED,  # only reserved field in internal header
            esd_name_length=len(self.esd_name) // 2,  # number of UTF-16 characters, NOT size of encoded bytes
            footer=[0, 0] if self.VERSION == 1 else [-1, -1],
            **INTERNAL_HEADER_VARINT_ASSERTED[self.LONG_VARINTS],
        )

        for state_machine_index, states in self.state_machines.items():
            StateMachineHeaderStruct.object_to_writer(
                states,
                writer,
                index=state_machine_index,
                states_offset=RESERVED,
                state_count=len(states),  # does NOT include dummy state, confusingly
                states_offset_2=RESERVED,  # duplicate of `states_offset`
            )

        # For `next_state_offset` of Conditions.
        state_id_offsets = {}  # type: dict[int, int]
        all_states = []  # for ease below (includes dummy state)

        for state_machine_index, states in self.state_machines.items():
            writer.fill_with_position("states_offset", obj=states)
            writer.fill_with_position("states_offset_2", obj=states)
            for state_id, state in states.items():
                state_id_offsets[state.state_id] = writer.position
                state.to_esd_writer(writer)
                all_states.append(state)
            if len(states) > 1:
                # Create and pack a duplicate of the first state. It will have its own condition pointers and arg data,
                # so needs proper creation rather than just duplicating the State struct.
                dummy_state = list(states.values())[0].copy()  # needs a new ID for reserving
                dummy_state.to_esd_writer(writer)
                all_states.append(dummy_state)
                # NOTE: NOT added to `state_id_offsets`. Any Condition pointing to the first state uses the real one.

        # Total state count in header includes dummy states.
        external_header_writer.fill("state_count", len(all_states), obj=self)

        # Offsets of existing Conditions, which can be re-used across States if they are identical.
        all_condition_offsets = {}  # type: dict[Condition, int]

        # Pack Conditions. These are the real `Condition` instances, which may be shared by multiple `State`s. States
        # do not reference these offsets directly, but instead go through 'condition pointer' offsets packed near the
        # end of the file. (Every condition of every State has a unique condition pointer, but multiple pointers may
        # point to the same `Condition` instance up here.)
        state_fresh_conditions = []
        for state in all_states:
            fresh_conditions = state.pack_conditions(writer, state_id_offsets, all_condition_offsets)
            state_fresh_conditions.append(fresh_conditions)
        external_header_writer.fill("condition_count", len(all_condition_offsets), obj=self)

        # Pack Commands.
        command_count = 0
        for state, fresh_conditions in zip(all_states, state_fresh_conditions):
            command_count += state.pack_commands(writer, fresh_conditions)
        external_header_writer.fill("command_count", command_count, obj=self)

        # Pack Command arg offsets.
        command_arg_count = 0
        for state, fresh_conditions in zip(all_states, state_fresh_conditions):
            command_arg_count += state.pack_command_args(writer, fresh_conditions)
        external_header_writer.fill("command_arg_count", command_arg_count, obj=self)

        # Pack Condition pointers.
        condition_pointers_count = 0
        recurred_conditions = set()
        external_header_writer.fill("condition_pointers_offset", writer.position, obj=self)
        for state in all_states:
            condition_pointers_count += state.pack_condition_pointers(
                writer, all_condition_offsets, recurred_conditions
            )
        external_header_writer.fill("condition_pointers_count", condition_pointers_count, obj=self)

        # Pack Condition test EZL data.
        for state, fresh_conditions in zip(all_states, state_fresh_conditions):
            state.pack_condition_test_data(writer, fresh_conditions)

        # Pack Command arg EZL data.
        for state, fresh_conditions in zip(all_states, state_fresh_conditions):
            state.pack_command_arg_data(writer, fresh_conditions)

        external_header_writer.fill("tail_offset", writer.position, obj=self)

        if self.esd_name:
            # writer.pad(2)  # TODO: TKGP does this in SF. Not correct for DSR, but maybe later games?
            writer.fill_with_position("esd_name_offset", obj=self)
            writer.append(self.esd_name.encode("utf-16-le") + b"\0\0")
        else:
            writer.fill("esd_name_offset", -1, obj=self)

        # Otherwise, EOF file offset written to both below.

        external_header_writer.fill("unk_offset_1", writer.position, obj=self)
        external_header_writer.fill("unk_offset_2", writer.position, obj=self)
        external_header_writer.fill("internal_data_size", writer.position, obj=self)

        # Combine writers.
        external_header_writer.append(bytes(writer))
        return external_header_writer

    def get_next_states(self, condition: Condition):
        next_states = []
        for subcondition in condition.subconditions:
            next_states += self.get_next_states(subcondition)
        if condition.next_state_id != -1:
            next_states.append(condition.next_state_id)
        return next_states

    def to_esp(self, esd_type: ESDType, state_machine_index=1) -> str:
        """Writes a single state machine to a single Python module."""

        # Scan each state to build 'from' lists.
        from_states = {}
        for i, state in self.state_machines[state_machine_index].items():
            for condition in state.conditions:
                for next_state in self.get_next_states(condition):
                    from_states.setdefault(next_state, set()).add(i)
        s = f"\"\"\"{esd_type.name} ESD STATE MACHINE {state_machine_index}\"\"\"\n"
        s += f"from soulstruct.{self.get_game().submodule_name}.ezstate.esd import *\n\n"
        for i, state in self.state_machines[state_machine_index].items():
            s += state.to_esp(esd_type, from_states=from_states.get(i, None))
        s = s.strip("\n") + "\n"  # End with just one newline.
        return s

    def write_esp_file(self, esp_path: Path | str = None, esd_type=ESDType.TALK):
        """Write ESP language script to a single file. Only works for single state machine Talk ESD.

        NOTE: This ESP format discards the four 'magic' integers, which will default to zeroes when this file is read.
        This shouldn't matter in-game. The ESD internal name will be inferred from the file stem (and this also doesn't
        matter in-game).
        """
        if len(self.state_machines) > 1:
            raise ValueError(
                f"Cannot write an `ESD` instance with {len(self.state_machines)} state machines to a single ESP file. "
                f"Use `write_esp_directory()`."
            )
        if esd_type != ESDType.TALK:
            raise TypeError("Can currently only write single-file ESP for 'TALK'. Use `write_esp_directory()`.")

        if esp_path is None:
            if self.path is None:
                raise ValueError("Cannot auto-detect ESP file path (no previous `path` set).")
            esp_path = self.path.with_suffix(".esp.py")
        else:
            esp_path = Path(esp_path)

        # Write single 'talk' state machine to a single ESP file.
        esp_path.parent.mkdir(parents=True, exist_ok=True)
        state_machine_py = self.to_esp(esd_type, next(iter(self.state_machines)))
        esp_path.write_text(state_machine_py, encoding="utf-8")

    def write_esp_directory(self, directory=None, esd_type=ESDType.TALK):
        """Write ESD to a collection of Python-like 'ESP' scripts (one per state machine) in the specified folder.

        Header information about the ESD file (internal name, ESD type, and four unknown 'magic' integers) is written to
        a file called 'ESD_Header.esp.py' in the directory. The state machine indices are written into the script names,
        and both the ESD type and state machine indices are also written into each script's docstring.

        NOTE: Neither the internal ESD name nor the four 'magic' integers seems to matter in-game (i.e. the file works
        normally if the name is empty and the 'magic' is just [0, 0, 0, 0]).
        """
        if directory is None:
            directory = self.path
            if not directory.suffix == ".esp":
                directory = directory.with_suffix(directory.suffix + ".esp")
        else:
            directory = Path(directory)

        directory.mkdir(parents=True, exist_ok=True)
        for i, state_machine in self.state_machines.items():
            if i >= 0x70000000:
                # 'Callable' state machine.
                state_machine_path = directory / f"StateMachine_x{0x80000000 - i}.esp.py"
            else:
                # Primary state machine.
                state_machine_path = directory / f"StateMachine_{i}.esp.py"
            with state_machine_path.open(mode="w", encoding="utf-8") as state_machine_file:
                state_machine_py = self.to_esp(esd_type, i)
                state_machine_file.write(state_machine_py)

        header = (
            f"ESD_NAME = {repr(self.esd_name)}\n"
            f"ESD_TYPE = {repr(self.ESD_TYPE.name)}\n"
            f"MAGIC = {repr(self.magic)}\n"
        )
        with (directory / "ESD_Header.esp.py").open(mode="w", encoding="utf-8") as header_file:
            header_file.write(header)

    def to_html(self, esd_type: ESDType):

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
                html += state.to_html(esd_type)

        SET_INTERNAL_SYMBOLS(False)

        return html + "</body></html>"

    def write_html(self, html_path=None, /, esd_type=ESDType.TALK):
        if html_path is None:
            html_path = self.path.with_suffix(self.path.suffix + ".html")
        else:
            html_path = Path(html_path)
        with html_path.open(mode="w", encoding="shift_jis_2004") as output_file:
            output_file.write(self.to_html(esd_type))
