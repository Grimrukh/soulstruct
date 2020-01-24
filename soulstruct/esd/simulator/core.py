"""ESD Simulator

Simulate an ESD state machine by manipulating flags, spoofing controller inputs, and changing relevant parts of the
game state. The simulator will report commands that are run, such as spoken dialogue, flag changes, and presented
dialogs and menus. Use this to test if the state machine behaves as expected without needing to open the game.

Currently works only for DS1 'talk' ESD files (both PTDE and DSR).
"""
import soulstruct.enums.darksouls1 as enums
from soulstruct.esd.ds1ptde import ESD as ESD_PTDE
from soulstruct.esd.ds1r import ESD as ESD_DSR
from soulstruct.esd.ezl_parser import decompile
from soulstruct.esd.functions import COMMANDS
from soulstruct.utilities.core import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame


class GameState(object):
    def __init__(self):
        self.one_line_help_message = None
        self.talk_list = None
        self.menus_open = []
        self.disable_talk_period_elapsed = False
        self.conversation = None
        self.level_up_menu_open = None
        # TODO: other menus with specific launch commands


class EntityState(object):
    def __init__(self):
        self.update_distance = 0  # TODO: unclear default
        self.bonfire_level = {0: 0}
        self.bonfire_state = 0  # TODO: both 0 and 1 are used as arguments. I think 0 is enabled and 1 is disabled.
        self.is_dead = False
        self.is_disabled = False
        self.enemies_nearby = False
        self.hp_percent = 100


class PlayerState(object):
    def __init__(self):
        self.is_dead = False
        self.is_client = False
        self.distance = 20  # seems like a sensible starting default
        self.y_distance = 0  # seems like a sensible starting default
        self.facing_angle = 0
        self.talking_to_entity = False
        self.talking_to_other = False
        self.character_type = enums.CharacterType.Hollow  # seems like a sensible default
        self.has_equipment = []
        self.wearing_equipment = []

    def build(self, window: SmartFrame):
        window.is_dead = self._create_button(window, "is_dead", "Is Dead")
        window.is_client = self._create_button(window, "is_client", "Is Client")
        window.talking_to_entity = self._create_button(window, "talking_to_entity", "Talking to Entity")
        window.talking_to_other = self._create_button(window, "talking_to_other", "Talking to Other")
        window.character_type = self._create_combobox(window, "character_type", "Character Type", enums.CharacterType)
        window.distance = self._create_entry(window, "distance", "Distance")
        window.y_distance = self._create_entry(window, "y_distance", "Y Distance")

    def _create_button(self, window, field, verbose):
        button = window.Button(
            text="{verbose}: {value}".format(verbose=verbose, value=getattr(self, field)),
            command=lambda: self._toggle_button(window, field))
        button.verbose_fmt = verbose
        return button

    def _toggle_button(self, window, field):
        setattr(self, field, not field)
        getattr(window, field)["text"] = "{verbose}: {value}".format(verbose=getattr(window, field).verbose_fmt,
                                                                     value=getattr(self, field))

    def _create_combobox(self, window, field, verbose, enum):
        values = [e.value for e in enum]
        combobox = window.Combobox(
            label=verbose, values=values, initial_value=getattr(self, field),
            on_select_function=lambda e: self._set_combobox(e, field))
        combobox.enum = enum
        return combobox

    def _set_combobox(self, event, field):
        combobox = event.widget
        enum = getattr(combobox.enum, combobox.var.get().replace(' ', ''))
        setattr(self, field, enum)

    def _create_entry(self, window, field, verbose):
        entry = window.Entry(label=verbose, initial_text=getattr(self, field))
        entry.bind("<Return>", self._update_entry)

    def _update_entry(self, event):
        entry = event.widget
        new_text = entry.var.get()
        try:
            new_value = float(new_text)
        except ValueError:
            if not entry.flashing:
                old_bg = entry["bg"]
                entry["bg"] = "#422"
                entry.after(100, lambda: self._stop_flash(entry, old_bg))

    @staticmethod
    def _stop_flash(widget, old_bg):
        widget.flashing = False
        widget["bg"] = old_bg


class InputEvents(object):
    def __init__(self):
        self.press_action_button = None
        self.selected_talk_list_entry = None
        self.player_attacked = None

    def reset(self):
        self.press_action_button = None
        self.selected_talk_list_entry = None
        self.player_attacked = None


class TalkSimulatorWindow(SmartFrame):

    def __init__(self, esd_source, game_version):
        super().__init__(window_title="DS1 Talk Simulator")

        self.sim = TalkSimulator(esd_source, game_version)

        with self.set_master(auto_rows=0):
            # Panel
            with self.set_master(auto_columns=0):
                # Player State
                pass

            # Log
            output_log = self.TextBox()


class TalkSimulator(object):

    def __init__(self, esd_source, game_version):
        self.game_version = game_version
        if self.game_version == "ptde":
            self.esd_class = ESD_PTDE
        if self.game_version == "dsr":
            self.esd_class = ESD_DSR
        else:
            raise ValueError(f"`game_version` must be 'ptde' or 'dsr', not '{game_version}'.")

        if isinstance(esd_source, (ESD_PTDE, ESD_DSR)):
            self.esd = esd_source
        else:
            self.esd = self.esd_class(esd_source, "TALK")
        self.sm = 1  # only supported SM at the moment
        self.current_state = None

        self.enabled_flags = {}
        self.disabled_flags = {}
        self.game_state = GameState()
        self.entity_state = EntityState()
        self.player_state = PlayerState()
        self.input_events = InputEvents()

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
            test_string = decompile(condition.test_ezl, condition.esd_type, func_prefix="self.")
            print(f"CONDITION ({self.current_state} -> {condition.next_state_index}): {test_string}")
            try:
                test_result = eval(test_string, {"self": self})
            except AttributeError as e:
                attr_name = str(e).split("has no attribute '")[1][-1]
                raise AttributeError(f"\ndef {attr_name}:\n    return ...")
            if test_result:
                print(f"--> TEST SUCCESS: {test_string}")
                self.change_state(condition.next_state_index)
        pass

    def change_state(self, new_state):
        """TODO:
            - Run exit commands of current state (if not None)
            - Run enter commands of new state
        """
        if self.current_state is not None:
            self.exit()
        self.current_state = new_state
        self.enter()

    def enter(self, state=None):
        if state is None:
            state = self.current_state
        commands = self.esd.state_machines[self.sm][state].enter_commands
        for command in commands:
            try:
                command_name, arg_names, arg_types = COMMANDS[command.esd_type][command.bank][command.index]
            except KeyError:
                if command.bank == 6:
                    # Start a child state machine.
                    arguments = ', '.join([f'{decompile(arg, command.esd_type)}' for arg in command.args])
                    print(f"ENTER: CALL_STATE_MACHINE[{0x80000000 - command.index}]({arguments})")  # TODO: unsupported
                command_name = f'Command_{command.esd_type}_{command.bank}_{command.index}'
                arg_names = ()
            if len(arg_names) != len(command.args):
                arguments = ', '.join([f'{decompile(arg, command.esd_type)}' for arg in command.args])
            else:
                arguments = ', '.join([f'{arg_name}={decompile(arg, command.esd_type)}'
                                       for arg_name, arg in zip(arg_names, command.args)])
            print(f'ENTER: {command_name}({arguments})')

    def exit(self, state=None):
        if state is None:
            state = self.current_state
        commands = self.esd.state_machines[self.sm][state].exit_commands
        for command in commands:
            try:
                command_name, arg_names, arg_types = COMMANDS[command.esd_type][command.bank][command.index]
            except KeyError:
                if command.bank == 6:
                    # Start a child state machine.
                    arguments = ', '.join([f'{decompile(arg, command.esd_type)}' for arg in command.args])
                    print(f"EXIT: CALL_STATE_MACHINE[{0x80000000 - command.index}]({arguments})")  # TODO: unsupported
                command_name = f'Command_{command.esd_type}_{command.bank}_{command.index}'
                arg_names = ()
            if len(arg_names) != len(command.args):
                arguments = ', '.join([f'{decompile(arg, command.esd_type)}' for arg in command.args])
            else:
                arguments = ', '.join([f'{arg_name}={decompile(arg, command.esd_type)}'
                                       for arg_name, arg in zip(arg_names, command.args)])
            print(f'EXIT: {command_name}({arguments})')

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
        return self.entity_state.bonfire_level[bonfire] == required_level

    def CompareBonfireState(self, required_state):
        return self.entity_state.bonfire_state == required_state


if __name__ == '__main__':
    ts = TalkSimulator(
        "C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/script/talk/"
        "m10_00_00_00.talkesdbnd.dcx.unpacked/t100000.esd", game_version="dsr")
    while input("Press any key to update SM. Press Q to exit.").lower() != "q":
        ts.update()

    print("\nFinished.")
