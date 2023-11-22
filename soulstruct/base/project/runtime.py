from __future__ import annotations

__all__ = ["RuntimeManager"]

import abc
import subprocess
import sys
import threading
import time
import typing as tp

from soulstruct.utilities.window import SmartFrame

from . import editor_config
from .exceptions import SoulstructProjectError
from .utilities import error_as_dialog

if tp.TYPE_CHECKING:
    from soulstruct.utilities.memory import MemoryHook
    from .core import GameDirectoryProject

try:
    # noinspection PyPackageRequirements
    import psutil
except ImportError:
    psutil = None


class RuntimeManager(SmartFrame, abc.ABC):
    DATA_NAME = None
    _THREADED_HOOK = False

    HOOK_CLASS = None  # type: type[MemoryHook]

    def __init__(self, project: GameDirectoryProject, master=None, toplevel=False):
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Runtime Manager")
        self.project = project
        self.game_save_entry = None
        self.game_save_list = None
        self.install_psutil_button = None
        self.flag_id = None
        self.flag_enabled = None
        self._hook = None  # type: tp.Optional[MemoryHook]
        self._THREAD_EXCEPTION = None

        self.build()

    def build(self):
        with self.set_master(padx=10, pady=10, row_weights=[1, 1, 1], column_weights=[1], auto_rows=0):

            if psutil is None:
                with self.set_master(padx=10, pady=10):
                    self.Label(
                        text="Cannot use runtime tools without Python package psutil.\n"
                        "Click below to install it, then restart Soulstruct.",
                        pady=10,
                        row=0,
                    )
                    self.install_psutil_button = self.Button(
                        text="Install psutil",
                        command=self._install_psutil,
                        bg="#422",
                        width=30,
                        font=self.FONT_DEFAULTS["heading"],
                        row=1,
                        tooltip_text="Install the Python package `psutil` into your Python distribution, which will "
                        "enable runtime tools.",
                    )
            else:
                with self.set_master(
                    auto_columns=0, padx=10, pady=10, row_weights=[1], column_weights=[1, 1, 1, 1, 1], sticky="n"
                ):
                    button_kwargs = {"width": 20, "sticky": "nsew", "padx": 10, "pady": 10}
                    self.Button(
                        text="Launch Game",
                        command=self._error_as_dialog(self.project.launch_game),
                        bg="#222",
                        **button_kwargs,
                    )
                    gadget = self.project.get_game().gadget_name
                    self.Button(
                        text=f"Run {gadget[:-4]}" if gadget else "No Gadget",
                        bg="#222",
                        command=self._error_as_dialog(self.project.launch_gadget),
                        tooltip_text=f"Launch '{gadget}' if it exists next to the game executable." if gadget else None,
                        state="normal" if gadget else "disabled",
                        **button_kwargs,
                    )
                    self.Button(
                        text="Hook Game",
                        bg="#222",
                        command=self.hook_into_game,
                        tooltip_text="Hook into running game memory to unlock more features.",
                        state="normal" if self.HOOK_CLASS else "disabled",
                        **button_kwargs,
                    )
                    self.Button(
                        text="Close Game",
                        bg="#422",
                        command=self._error_as_dialog(self.project.force_quit_game),
                        tooltip_text="Force quit game if it is running.",
                        **button_kwargs,
                    )

            with self.set_master(padx=10, pady=20, row_weights=[1, 1], column_weights=[1, 1, 1]):
                try:
                    game_saves = self.project.save_manager.get_game_saves()
                except SoulstructProjectError:
                    self.Label(
                        text="Could not find game saves.\n\nTry setting 'SaveDirectory' to your save directory "
                        "manually in 'project_config.json' in your project folder, then restart Soulstruct.",
                        row=0,
                        column=0,
                    )
                else:
                    self.game_save_list = self.Combobox(
                        values=game_saves,
                        initial_value=game_saves[0] if game_saves else "",
                        width=40,
                        label="Available Saves:",
                        label_position="left",
                        font=editor_config.SMALL_FONT,
                        row=0,
                        column=0,
                    )
                    self.Button(
                        text="Load Save",
                        bg="#222",
                        padx=10,
                        width=15,
                        command=self._error_as_dialog(self.load_game_save),
                        row=0,
                        column=1,
                    )
                    delete_button = self.Button(
                        text="Delete (Shift + Click)",
                        bg="#422",
                        padx=20,
                        width=20,
                        command=None,
                        row=0,
                        column=2,
                    )
                    delete_button.bind("<Shift-Button-1>", self._error_as_dialog(lambda _: self.delete_game_save()))

                    self.game_save_entry = self.Entry(
                        width=43, label="New Save Name:", label_position="left", row=1, column=0
                    ).var
                    create_save_button = self.Button(
                        text="Create Save",
                        bg="#222",
                        padx=10,
                        pady=(10, 0),
                        width=15,
                        command=None,
                        row=1,
                        column=1,
                    )
                    self.Label(text="Shift + Click to Overwrite", row=2, column=1)
                    create_save_button.bind(
                        "<Button-1>", self._error_as_dialog(lambda _: self.create_game_save(overwrite=False))
                    )
                    create_save_button.bind(
                        "<Shift-Button-1>", self._error_as_dialog(lambda _: self.create_game_save(overwrite=True))
                    )

            if self.HOOK_CLASS.EVENT_FLAG_OFFSETS:
                with self.set_master(padx=20, pady=20, column_weights=[1, 1, 1, 1], auto_columns=0):
                    self.flag_id = self.Entry(
                        label="Event Flag ID:",
                        label_position="left",
                        width=15,
                        integers_only=True,
                    ).var
                    self.flag_enabled = self.Checkbutton(
                        initial_state=False,
                        label="State:",
                        label_position="left",
                        selectcolor="#000",
                        padx=20,
                    )
                    self.Button(
                        text="Read Flag",
                        bg="#222",
                        padx=10,
                        pady=(10, 0),
                        width=15,
                        command=self._read_flag_checkbutton,
                    )
                    self.Button(
                        text="Write Flag",
                        bg="#422",
                        padx=10,
                        pady=(10, 0),
                        width=15,
                        command=self._write_flag_checkbutton,
                    )

            else:
                with self.set_master(padx=10, pady=20):
                    self.Label(
                        text="Event flag read/write not supported for this game.",
                        pady=10,
                        row=0,
                    )

    def _read_flag_checkbutton(self):
        """Set flag Checkbutton state to flag ID state."""
        try:
            flag_id = int(self.flag_id.get())
        except ValueError:
            self.CustomDialog("Invalid Event Flag", "Event flag must be an integer.")
            return
        flag_state = self.get_flag(flag_id)
        if flag_state is None:
            return
        self.flag_enabled.var.set(flag_state)
        self.flag_enabled.config(fg="#4F4" if flag_state else "#555")

    def _write_flag_checkbutton(self):
        """Write flag ID state from flag Checkbutton state."""
        try:
            flag_id = int(self.flag_id.get())
        except ValueError:
            self.CustomDialog("Invalid Event Flag", "Event flag must be an integer.")
            return
        flag_state = self.flag_enabled.var.get()
        self.set_flag(flag_id, flag_state)

    def get_flag(self, flag_id: int) -> tp.Optional[bool]:
        if not self._hook:
            self.CustomDialog("Game Not Hooked", "You must hook into the game before reading an event flag.")
            return None
        if not self._hook.EVENT_FLAG_OFFSETS:
            self.CustomDialog("Cannot Read Flags", "Soulstruct cannot read event flags for this game.")
            return None
        try:
            flag_state = self._hook.read_event_flag(flag_id)
        except Exception as ex:
            self.CustomDialog("Flag Read Error", f"An error occurred while reading event flag ID {flag_id}:\n{ex}")
            return None
        return flag_state

    def set_flag(self, flag_id: int, state: bool):
        """Enable given flag ID."""
        if not self._hook:
            self.CustomDialog("Game Not Hooked", "You must hook into the game before writing an event flag.")
            return
        if not self._hook.EVENT_FLAG_OFFSETS:
            self.CustomDialog("Cannot Write Flags", "Soulstruct cannot write event flags for this game.")
            return
        try:
            self._hook.write_event_flag(flag_id, state)
        except Exception as ex:
            self.CustomDialog("Flag Write Error", f"An error occurred while writing event flag ID {flag_id}:\n{ex}")
            return

    def enable_flag(self, flag_id: int):
        self.set_flag(flag_id, True)

    def disable_flag(self, flag_id: int):
        self.set_flag(flag_id, False)

    def load_game_save(self):
        selected_game_save = self.game_save_list.get()
        if not selected_game_save:
            return
        self.project.save_manager.load_game_save(selected_game_save)

    def delete_game_save(self):
        selected_game_save = self.game_save_list.get()
        if not selected_game_save:
            return
        self.project.save_manager.delete_game_save(selected_game_save)
        self.game_save_list["values"] = self.project.save_manager.get_game_saves()
        self.game_save_list.set("")

    def create_game_save(self, overwrite=False):
        game_save_name = self.game_save_entry.get()
        self.project.save_manager.create_game_save(game_save_name, overwrite=overwrite)
        self.game_save_list["values"] = self.project.save_manager.get_game_saves()

    def hook_into_game(self):
        """Returns True if hook was successful, and False if not."""
        if self._THREADED_HOOK:
            self._do_threaded_hook()
        else:
            # Window will not respond while the hook loads.
            self._hook = self.HOOK_CLASS()

        self.CustomDialog(
            title="Hook Successful",
            message=f"Hooked into {self.project.get_game().name} successfully.\n\n"
            "You may now use features such as assigning current player coordinates to map entities.\n\n"
            "For more useful runtime features, use DS/DSR Gadget by TKGP.",
        )
        return True

    def _do_threaded_hook(self):
        """Hooks in a separate thread while displaying a loading dialogue.

        Only needed if hooking takes forever because of the need to scan for base pointers.
        """

        def _threaded_hook():
            try:
                self._hook = self.HOOK_CLASS()
            except Exception as e:
                self._THREAD_EXCEPTION = e
                raise

        loading = self.LoadingDialog(
            title="Hooking game...",
            message=f"Hooking into {self.project.get_game().name}...",
            maximum=20,
        )
        hook_thread = threading.Thread(target=_threaded_hook)
        hook_thread.start()
        loading.update()
        loading.progress.start()
        while hook_thread.is_alive():
            loading.update()
            time.sleep(1 / 60)
        loading.progress.stop()
        loading.destroy()

        if self._THREAD_EXCEPTION:
            message = (
                f"Error occurred while hooking into game:\n\n{str(self._THREAD_EXCEPTION)}\n\n"
                f"Import operation may have only partially completed."
            )
            self._THREAD_EXCEPTION = None
            return self.CustomDialog(title="Import Error", message=message)

    def get_game_value(self, value_name):
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")
        return self._hook.get(value_name)

    @property
    def hook_created(self):
        return self._hook is not None

    def _install_psutil(self):
        self.install_psutil_button.var.set("Installing...")
        self.update_idletasks()
        subprocess.run(f"{sys.executable} -m pip install psutil")
        self.install_psutil_button.var.set("Installation successful.")
        self.install_psutil_button["state"] = "disabled"
        self.update_idletasks()
        self.bell()
        self.CustomDialog(
            title="Installation complete", message="`psutil` installed successfully.\n\nPlease restart Soulstruct."
        )

    def _error_as_dialog(self, func):
        return error_as_dialog(self, func)
