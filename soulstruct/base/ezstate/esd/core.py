from __future__ import annotations

__all__ = ["ESD"]

import abc
import ast
import logging
import re
import typing as tp
from pathlib import Path

from .exceptions import ESDTypeError
from soulstruct.base.game_file import GameFile, InvalidGameFileTypeError
from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .state import State
from .esp_compiler import ESPCompiler
from .ezl_parser import SET_INTERNAL_SYMBOLS

if tp.TYPE_CHECKING:
    from soulstruct.containers.dcx import DCXType
    from .command import Command
    from .condition import Condition

_LOGGER = logging.getLogger(__name__)


class ESD(GameFile, abc.ABC):
    """An EzState state machine that controls character/bonfire interactions (TALK) or character animations (CHR)."""

    EXT = ".esd"
    EXTERNAL_HEADER_STRUCT: BinaryStruct = None
    INTERNAL_HEADER_STRUCT: BinaryStruct = None
    STATE_MACHINE_HEADER_STRUCT: BinaryStruct = None
    DCX_TYPE: DCXType = None
    ESD_TYPE: ESDType = None

    State: tp.Type[State] = None

    def __init__(self, esd_source, dcx_type=None, esd_name=""):
        """ Source can be one of:
            - file path of a '.esd[.dcx]' file.
            - raw binary data (e.g. from a BND entry).
            - '.esp' file (must a single state machine with index 1, and `esd_name` must also be given).
            - '.esp' directory with a file `ESD_Header.esp.py` and separate state machine files `StateMachine_i.esp.py`
              (or `StateMachine_xi.esp.py` for callable state machines).
        """
        self.magic = ()
        self.file_tail = b""
        self.state_machines = {}  # type: dict[int, dict[int, State]]
        super().__init__(esd_source, dcx_type)
        if esd_name:  # override any auto-detected name
            self.esd_name = esd_name

    def _handle_other_source_types(self, file_source, **kwargs) -> tp.Optional[BinaryReader]:
        if isinstance(file_source, (Path, str)):
            file_source = Path(file_source)

            if file_source.is_dir():
                self.path = file_source
                self.compile_from_esp_dir(file_source)
                return None

            for ext in (".esp.py", ".esp", ".py"):
                if file_source.name.endswith(ext):
                    self.esd_name = file_source.name[len(ext)]
                    self.path = file_source.parent / self.esd_name
                    try:
                        self.compile_from_esp_single_file(file_source)
                    except Exception as ex:
                        raise ValueError(f"Error encountered while parsing '{file_source}': {ex}")
                    return None

        raise InvalidGameFileTypeError("`esd_source` is not a `.esp[.py]` file or directory.")

    def unpack(self, esd_reader: BinaryReader, **kwargs):

        header = esd_reader.unpack_struct(self.EXTERNAL_HEADER_STRUCT)
        # Internal offsets start here, so we reset the buffer.
        esd_reader = BinaryReader(esd_reader.read())

        internal_header = esd_reader.unpack_struct(self.INTERNAL_HEADER_STRUCT)
        self.magic = internal_header["magic"]
        state_machine_headers = esd_reader.unpack_structs(
            self.STATE_MACHINE_HEADER_STRUCT, count=header["state_machine_count"]
        )

        for state_machine_header in state_machine_headers:
            states = self.State.unpack(
                esd_reader,
                state_machine_header["state_machine_offset"],
                count=state_machine_header["state_count"],
            )
            self.state_machines[state_machine_header["state_machine_index"]] = states

        if internal_header["esd_name_length"] > 0:
            esd_name_offset = internal_header["esd_name_offset"]
            esd_name_length = internal_header["esd_name_length"]
            # Note the given length is the length of the final string. The actual UTF-16 encoded bytes are twice that.
            self.esd_name = esd_reader.unpack_string(
                offset=esd_name_offset, length=2 * esd_name_length, encoding="utf-16le"
            )
            esd_reader.seek(esd_name_offset + 2 * esd_name_length)
            self.file_tail = esd_reader.read()
        else:
            self.esd_name = ""
            esd_reader.seek(header["unk_offset_1"])  # after packed EZL
            self.file_tail = esd_reader.read()

    def compile_from_esp_dir(self, esp_dir):
        esp_dir = Path(esp_dir)

        header_path = list(esp_dir.glob("ESD_Header*"))
        if not header_path:
            raise FileNotFoundError("Could not find 'ESD_Header file in directory.")
        self.read_esp_header(header_path[0])

        self.state_machines = {}
        for esp_path in esp_dir.glob("StateMachine_*"):
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
            compiler = ESPCompiler(esp_path, self)
            self.state_machines[state_machine_index] = compiler.states

    def compile_from_esp_single_file(self, esp_file):
        esp_file = Path(esp_file)
        self.magic = (0, 0, 0, 0)
        _LOGGER.debug(f"Compiling single-file ESD state machine: {esp_file.name}")
        compiler = ESPCompiler(esp_file, self)
        self.state_machines = {1: compiler.states}

    def read_esp_header(self, header_path: Path):
        with header_path.open("r") as f:
            for line in f:
                line = line.strip(" \r\n")
                if not line:
                    continue
                if line.startswith("ESD_NAME = "):
                    self.esd_name = ast.literal_eval(line[len("ESD_NAME = "):])
                elif line.startswith("ESD_TYPE = "):
                    esd_type = ESDType(ast.literal_eval(line[len("ESD_TYPE = "):]))
                    if esd_type != self.ESD_TYPE:
                        raise ESDTypeError(
                            f"ESP file ESD_TYPE is {esd_type}. Cannot load with {self.__class__.__name__}."
                        )
                elif line.startswith("MAGIC = "):
                    magic = line[len("MAGIC = "):]
                    try:
                        self.magic = tuple(ast.literal_eval(magic))
                    except ValueError:
                        raise ValueError(f"Could not read MAGIC value from ESD_Header: {magic}")
                else:
                    raise ValueError(f"Invalid ESD Header line: {line}")
        if len(self.magic) != 4:
            raise ValueError(f"MAGIC should be a four-element sequence.")

    def pack(self):
        """Packs tables and computes new byte offsets for them."""
        # TODO: is 'existing commands' a thing for enemyCommon.esd? Probably, but only for efficiency.
        tables = _ESDPacker(self)

        external_header = self.EXTERNAL_HEADER_STRUCT.pack(tables.external_header)
        packed = b""
        packed += self.INTERNAL_HEADER_STRUCT.pack(tables.internal_header)
        for sm_i, sm in tables.state_machine_headers.items():
            assert len(packed) == tables.offsets["state_machine_headers"][sm_i]
            packed += self.STATE_MACHINE_HEADER_STRUCT.pack(sm)
        for sm_i, sm in tables.state_machines.items():
            assert len(packed) == tables.offsets["state_machines"][sm_i]
            packed += self.State.STRUCT.pack_multiple(sm)
        assert len(packed) == tables.offsets["conditions"]
        packed += self.State.Condition.STRUCT.pack_multiple(tables.conditions)
        assert len(packed) == tables.offsets["commands"]
        packed += self.State.Command.STRUCT.pack_multiple(tables.commands)
        assert len(packed) == tables.offsets["command_args"]
        packed += self.State.Command.ARG_STRUCT.pack_multiple(tables.command_args)
        assert len(packed) == tables.offsets["condition_pointers"]
        packed += self.State.Condition.POINTER_STRUCT.pack_multiple(tables.condition_pointers)
        assert len(packed) == tables.offsets["ezl"]
        packed += tables.ezl
        assert len(packed) == tables.offsets["esd_name"]
        packed += tables.esd_name
        assert len(packed) == tables.offsets["file_tail"]
        packed += tables.file_tail

        return external_header + packed

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
        s = f"from soulstruct.{self.GAME.submodule_name}.ezstate.esd import *\n\n"
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

    def __init__(self, esd: ESD):
        self.__updated = False
        self.esd = esd

        # Various constants.
        self.magic = esd.magic
        self.esd_name = esd.esd_name.encode("utf-16le")
        if self.esd_name:
            self.esd_name += b"\0"
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
