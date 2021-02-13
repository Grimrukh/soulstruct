"""ESD Simulator

Simulate an ESD state machine by manipulating flags, spoofing controller inputs, and changing relevant parts of the
game state. The simulator will report commands that are run, such as spoken dialogue, flag changes, and presented
dialogs and menus. Use this to test if the state machine behaves as expected without needing to open the game.

Currently works only for DS1 'talk' ESD files (both PTDE and DSR).
"""
import logging
from queue import Queue

from soulstruct.darksouls1r.events import enums
from soulstruct.game_types.internal_types import ESDType
from soulstruct.darksouls1ptde.ezstate import TalkESD as TalkESDPTDE
from soulstruct.darksouls1r.ezstate import TalkESD as TalkESDDSR
from soulstruct.base.ezstate.esd.ezl_parser import decompile
from soulstruct.base.ezstate.esd.functions import COMMANDS
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.utilities.core import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame

_LOGGER = logging.getLogger(__name__)


class BaseState:
    name = ""

    def _create_button(self, window: SmartFrame, field, verbose, is_boolean=True):
        button = window.Button(
            text=f"{verbose}: {getattr(self, field)}",
            fg="#8F8" if getattr(self, field) else "#F88",
            width=20,
            command=lambda: self._toggle_button(window, field),
        )
        button.verbose_fmt = verbose
        button.is_boolean = is_boolean
        return button

    def _toggle_button(self, window, field):
        button = getattr(window, self.name)[field]
        if button.is_boolean:
            setattr(self, field, not getattr(self, field))
        else:
            # Only other type of button right now is 0 - 1.
            setattr(self, field, int(not getattr(self, field)))
        button["fg"] = "#8F8" if getattr(self, field) else "#F88"
        button.var.set(f"{button.verbose_fmt}: {getattr(self, field)}")

    def _create_combobox(self, window, field, verbose, enum):
        values = [camel_case_to_spaces(e.name) for e in enum]
        combobox = window.Combobox(
            label=verbose,
            values=values,
            initial_value=camel_case_to_spaces(getattr(self, field).name),
            on_select_function=lambda e: self._set_combobox(e, field),
        )
        combobox.enum = enum
        return combobox

    def _set_combobox(self, event, field):
        combobox = event.widget
        enum = getattr(combobox.enum, combobox.var.get().replace(" ", ""))
        setattr(self, field, enum)

    def _create_entry(self, window, field, verbose):
        entry = window.Entry(label=verbose + ":", initial_text=getattr(self, field), width=6, sticky="e")
        entry.bind("<Return>", lambda e: self._update_entry(e, field))
        entry.flashing = False
        return entry

    def _update_entry(self, event, field):
        entry = event.widget
        new_text = entry.var.get()
        try:
            new_value = float(new_text)
        except ValueError:
            if not entry.flashing:
                old_bg = entry["bg"]
                entry["bg"] = "#422"
                entry.after(100, lambda: self._stop_flash(entry, old_bg))
        else:
            setattr(self, field, new_value)
            if not entry.flashing:
                old_bg = entry["bg"]
                entry["bg"] = "#242"
                entry.after(100, lambda: self._stop_flash(entry, old_bg))

    @staticmethod
    def _stop_flash(widget, old_bg):
        widget.flashing = False
        widget["bg"] = old_bg


class GameState(BaseState):
    def __init__(self):
        """These are display only and can't be modified directly, unlike entity and player state."""
        self._one_line_help_message = None
        self._talk_list = None
        self._conversation = None
        self._disable_talk_period_elapsed = True  # internal timer that delays sequential talk prompts

        # TODO
        self._menus_open = []
        self._level_up_menu_open = None
        # TODO: other menus with specific launch commands

        self._window = None

    def build(self, window: SmartFrame):
        window.game = {
            "one_line_help_message": window.Label(label="One Line Help:", label_position="above", text="<None>"),
            "talk_list": window.Listbox(label="Menu Options:", label_position="above"),
            "conversation": window.Label(label="Conversation:", label_position="above", text="<None>"),
            "disable_talk_period_elapsed": window.Label(
                label="Talk Disabled Period Elapsed:", label_position="above", text="True"
            ),
        }
        self._window = window

    @property
    def one_line_help_message(self):
        return self._one_line_help_message

    @one_line_help_message.setter
    def one_line_help_message(self, text):
        self._one_line_help_message = text
        if self._window:
            self._window.game["one_line_help_message"].var.set("<None>" if text is None else text)

    def set_talk_list(self, talk_list):
        self._talk_list = talk_list
        if self._window:
            listbox = self._window.talk_list
            listbox.delete(0, "end")
            for item in self._talk_list:
                if not isinstance(item, str):
                    raise ValueError("Only text strings should be added to talk list (text IDs are looked up).")
                listbox.insert("end", item)

    def append_talk_list(self, item: str):
        if isinstance(self._talk_list, list):
            self._talk_list.append(item)
        else:
            raise TypeError("Talk list has not been initialized. Cannot add item to it.")
        if self._window:
            self._window.talk_list.insert("end", item)

    @property
    def conversation(self):
        return self._conversation

    @conversation.setter
    def conversation(self, text):
        self._conversation = text
        if self._window:
            self._window.conversation.var.set("<None>" if text is None else text)

    @property
    def disable_talk_period_elapsed(self):
        return self._disable_talk_period_elapsed

    @disable_talk_period_elapsed.setter
    def disable_talk_period_elapsed(self, text):
        self._disable_talk_period_elapsed = text
        # if self._window:  # TODO
        #     self._window.disable_talk_period_elapsed.var.set(f"Talks Disabled: {self._disable_talk_period_elapsed}")


class EntityState(BaseState):
    name = "entity"

    def __init__(self):
        self.update_distance = 0  # TODO: unclear default
        self.bonfire_level = 0  # TODO: currently bonfire '0' only
        self.bonfire_state = 1  # 1 is unlit, 0 is lit
        self.is_dead = False
        self.is_disabled = False
        self.enemies_nearby = False
        self.hp_percent = 100

    def build(self, window: SmartFrame):
        window.entity = {
            "is_dead": self._create_button(window, "is_dead", "Is Dead"),
            "is_disabled": self._create_button(window, "is_disabled", "Is Disabled"),
            "enemies_nearby": self._create_button(window, "enemies_nearby", "Enemies Nearby"),
            "hp_percent": self._create_entry(window, "hp_percent", "HP Percent"),
            "update_distance": self._create_entry(window, "update_distance", "Update Distance"),
            "bonfire_level": self._create_entry(window, "bonfire_level", "Bonfire Level (0)"),
            "bonfire_state": self._create_button(window, "bonfire_state", "Bonfire State", is_boolean=False),
        }


class PlayerState(BaseState):
    name = "player"

    def __init__(self):
        self.is_dead = False
        self.is_client = False
        self.talking_to_entity = False
        self.talking_to_other = False
        self.character_type = enums.CharacterType.Hollow  # seems like a sensible default
        self.distance = 20  # seems like a sensible starting default
        self.y_distance = 0  # seems like a sensible starting default
        self.facing_angle = 0
        self.has_equipment = []  # TODO
        self.wearing_equipment = []  # TODO

    def build(self, window: SmartFrame):
        window.player = {
            "is_dead": self._create_button(window, "is_dead", "Is Dead"),
            "is_client": self._create_button(window, "is_client", "Is Client"),
            "talking_to_entity": self._create_button(window, "talking_to_entity", "Talking to Entity"),
            "talking_to_other": self._create_button(window, "talking_to_other", "Talking to Other"),
            "character_type": self._create_combobox(window, "character_type", "Character Type", enums.CharacterType),
            "distance": self._create_entry(window, "distance", "Distance"),
            "y_distance": self._create_entry(window, "y_distance", "Y Distance"),
            "facing_angle": self._create_entry(window, "facing_angle", "Facing Angle"),
        }


class InputEvents:
    def __init__(self):
        self.press_action_button = None
        self.selected_talk_list_entry = None
        self.player_attacked = None

    def reset(self):
        self.press_action_button = None
        self.selected_talk_list_entry = None
        self.player_attacked = None


class TalkSimulatorWindow(SmartFrame):
    def __init__(self, esd_source, game_version, text_source):
        super().__init__(window_title="DS1 Talk Simulator")

        self.sim = TalkSimulator(esd_source, game_version, text_source)

        with self.set_master(auto_columns=0, padx=10, pady=10):
            with self.set_master(auto_rows=0):

                self.current_state = self.Label(text="State: None", font_size=20, pady=10)

                self.current_conditions = self.Listbox(
                    label="Conditions:",
                    label_position="above",
                    label_bg="#111",
                    font=("Consolas", 8),
                    width=100,
                    height=10,
                    padx=10,
                    pady=10,
                    bg="#333",
                )

                # Log  # TODO: in canvas
                self.output_log = self.TextBox(
                    width=50, height=10, vertical_scrollbar=True, padx=15, pady=15, bg="#333"
                )

                # Buttons
                with self.set_master(auto_columns=0):
                    self.Button(text="Update", command=self.update, width=20, bg="#622")

            # Panel
            with self.set_master():
                self.Label(text="Game State", font_size=14, row=0, column=0)
                with self.set_master(row=1, column=0, auto_rows=0, grid_defaults={"pady": 5}, padx=20):
                    self.sim.game_state.build(self)
                self.Label(text="Entity State", font_size=14, row=0, column=1)
                with self.set_master(row=1, column=1, auto_rows=0, grid_defaults={"pady": 5}, padx=20):
                    self.sim.entity_state.build(self)
                self.Label(text="Player State", font_size=14, row=0, column=2)
                with self.set_master(row=1, column=2, auto_rows=0, grid_defaults={"pady": 5}, padx=20):
                    self.sim.player_state.build(self)

        self.set_geometry()

    def update(self):
        self.sim.update()
        self.current_state.var.set(f"State: {self.sim.current_state}")
        self.current_conditions.delete(0, "end")
        for condition in self.sim.get_state_object().conditions:
            test_string = decompile(condition.test_ezl, ESDType.TALK)
            condition_string = f"{self.sim.current_state} -> {condition.next_state_index}: {test_string}"
            self.current_conditions.insert("end", condition_string)
        while not self.sim.unprocessed_commands.empty():
            command = self.sim.unprocessed_commands.get()
            self.output_log.insert("end", "\n" + command)


class TalkSimulator:
    def __init__(self, esd_source, game_version, text_source):
        self.game_version = game_version
        if self.game_version == "ptde":
            self.esd_class = TalkESDPTDE
        if self.game_version == "dsr":
            self.esd_class = TalkESDDSR
        else:
            raise ValueError(f"`game_version` must be 'ptde' or 'dsr', not '{game_version}'.")

        try:
            self.text = MSGDirectory(text_source)
        except Exception:
            _LOGGER.error("Invalid text source for TalkSimulator. Should be 'msg/ENGLISH' directory.")
            raise

        if isinstance(esd_source, (TalkESDPTDE, TalkESDDSR)):
            self.esd = esd_source
        else:
            self.esd = self.esd_class(esd_source)
        self.sm = 1  # only supported SM at the moment
        self.current_state = None

        self.enabled_flags = {}
        self.disabled_flags = {}
        self.game_state = GameState()
        self.entity_state = EntityState()
        self.player_state = PlayerState()
        self.input_events = InputEvents()

        self.unprocessed_commands = Queue()

        self.reset(reset_flags=True)

    def reset(self, reset_flags=False):
        """Doesn't change flags."""
        self.current_state = None
        if reset_flags:
            # TODO: scan ESD for flags values in tests and commands. separate 'checked' from 'manipulated'.
            self.enabled_flags = {}
            self.disabled_flags = {}

        self.game_state = GameState()
        self.entity_state = EntityState()
        self.player_state = PlayerState()
        self.input_events = InputEvents()

        self.change_state(0)

    def update(self):
        """Checks all test conditions in the current state and initiates a change in state if appropriate."""
        # TODO: call automatically if some relevant input is changed (if set up to do so, which is the default).
        # TODO: call ongoing commands (before or after tests?)
        conditions = self.esd.state_machines[self.sm][self.current_state].conditions
        for condition in conditions:
            test_string = decompile(condition.test_ezl, ESDType.TALK, func_prefix="self.")
            try:
                test_result = eval(test_string, {"self": self})
            except AttributeError as e:
                attr_name = str(e).split("has no attribute '")[1][-1]
                raise AttributeError(f"\ndef {attr_name}:\n    return ...")
            if test_result:
                self.change_state(condition.next_state_index)
        print(f"# UPDATED (State {self.current_state})")

    def change_state(self, new_state):
        if self.current_state is not None:
            self.run_commands("exit")
        self.current_state = new_state
        self.run_commands("enter")

    def get_state_object(self, state_index=None):
        if state_index is None:
            state_index = self.current_state
        return self.esd.state_machines[self.sm][state_index]

    def run_commands(self, command_type, state=None):
        state_instance = self.get_state_object(state)
        if command_type == "enter":
            commands = state_instance.enter_commands
        elif command_type == "ongoing":
            commands = state_instance.ongoing_commands
        elif command_type == "exit":
            commands = state_instance.exit_commands
        else:
            raise ValueError(f"`command_type` should be 'enter', 'ongoing', or 'exit', not {command_type}")

        for command in commands:
            try:
                command_name, arg_names, arg_types = COMMANDS[ESDType.TALK][command.bank][command.index]
            except KeyError:
                if command.bank == 6:
                    raise ValueError("Child state machines cannot yet be simulated.")
                command_name = f"Command_{ESDType.TALK.name}_{command.bank}_{command.index}"
                arg_names = ()
            if len(arg_names) != len(command.args):
                arguments = ", ".join([f"{decompile(arg, ESDType.TALK)}" for arg in command.args])
            else:
                arguments = ", ".join(
                    [f"{arg_name}={decompile(arg, ESDType.TALK)}" for arg_name, arg in zip(arg_names, command.args)]
                )
            command_string = f"{command_name}({arguments})"
            print("Command String: self." + command_string)
            try:
                eval("self." + command_string, {"self": self})
            except AttributeError:
                raise
            #     self.unprocessed_commands.put(f"{command_type.capitalize()}: {command_string}")
            # else:
            #     print("Evaluated successfully:", command_string)

    # COMMANDS

    def DisplayOneLineHelp(self, text_id):
        self.game_state.one_line_help_message = self.text.EventText[text_id]

    # TESTS

    def DebugEvent(self, message):
        self.unprocessed_commands.put(f"DEBUG MESSAGE: {message}")

    def GetOneLineHelpStatus(self):
        return self.game_state.one_line_help_message is not None and self.input_events.press_action_button

    def HasDisableTalkPeriodElapsed(self):
        return self.game_state.disable_talk_period_elapsed

    def IsPlayerTalkingToMe(self):
        return self.player_state.talking_to_entity

    def IsTalkingToSomeoneElse(self):
        return self.player_state.talking_to_other

    def CheckSelfDeath(self):
        return self.entity_state.is_dead

    def IsCharacterDisabled(self):
        return self.entity_state.is_disabled

    def IsClientPlayer(self):
        return self.player_state.is_client

    def GetDistanceToPlayer(self):
        return self.player_state.distance

    def GetPlayerYDistance(self):
        return self.player_state.y_distance

    def GetRelativeAngleBetweenPlayerAndSelf(self):
        return self.player_state.facing_angle

    def CompareBonfireLevel(self, required_level, bonfire):
        """Currently accepts `bonfire=0` only."""
        if bonfire != 0:
            raise ValueError("Not implemented: checking bonfire level of non-zero bonfire index.")
        return self.entity_state.bonfire_level == required_level

    def CompareBonfireState(self, required_state):
        return self.entity_state.bonfire_state == required_state


if __name__ == "__main__":
    from soulstruct import DSR_PATH

    ts = TalkSimulatorWindow(
        DSR_PATH + "/script/talk/m10_00_00_00.talkesdbnd.dcx.unpacked/t100000.esd",
        game_version="dsr",
        text_source=DSR_PATH + "/msg/ENGLISH",
    )
    # while input("Press any key to update SM. Press Q to exit.").lower() != "q":
    #     ts.update()

    ts.wait_window()

    print("\nFinished.")
