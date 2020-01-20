import subprocess
import sys

from soulstruct.utilities.window import SmartFrame

from .utilities import error_as_dialog

try:
    import psutil
except ImportError:
    psutil = None


class SoulstructRuntimeManager(SmartFrame):
    DATA_NAME = None

    def __init__(self, project, master=None, toplevel=False):
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Runtime Manager")
        self.project = project
        self.game_save_entry = None
        self.game_save_list = None
        self.install_psutil_button = None

        self.build()

    def build(self):
        """
        TODO:
            - Option to connect to running game and extract current player XYZ coordinates into an MSB entry?
        """
        with self.set_master(padx=10, pady=10, row_weights=[1, 1, 1], column_weights=[1], auto_rows=0):

            if psutil is None:
                with self.set_master(padx=10, pady=10):
                    self.Label(
                        text="Cannot use launcher tools without Python package psutil.\n"
                             "Click below to install it, then restart Soulstruct.",
                        font_size=14, pady=10, row=0)
                    self.install_psutil_button = self.Button(
                        text="Install psutil", command=self._install_psutil, bg="#422", width=30,
                        font_size=16, row=1)
            else:
                with self.set_master(padx=10, pady=10, row_weights=[1, 1], column_weights=[1, 1]):
                    button_kwargs = {'width': 30, 'sticky': 'nsew', 'padx': 10, 'pady': 10, 'font_size': 14}
                    self.Button(text="Launch Game", command=self._error_as_dialog(self.project.launch_game),
                                bg="#222", row=0, column=0, **button_kwargs)
                    debug_launch = self.Button(
                        text="Launch Game (Debug)",
                        command=self._error_as_dialog(lambda: self.project.launch_game(debug=True)),
                        bg="#222", row=0, column=1, **button_kwargs)
                    if self.project.game_name != "Dark Souls Prepare to Die Edition":
                        debug_launch['state'] = 'disabled'
                        debug_launch.var.set("No Debug for DSR")
                    self.Button(text="Launch DS Gadget", bg="#222",
                                command=self._error_as_dialog(self.project.launch_gadget),
                                row=1, column=0, **button_kwargs)
                    self.Button(text="Close Game", bg="#422",
                                command=self._error_as_dialog(lambda: self.project.force_quit_game(
                                    including_debug=self.project.game_name == "Dark Souls Prepare to Die Edition")),
                                row=1, column=1, **button_kwargs)

            with self.set_master(padx=10, pady=20, row_weights=[1, 1], column_weights=[1, 1, 1]):
                game_saves = self.project.get_game_saves()
                self.game_save_list = self.Combobox(
                    values=game_saves, initial_value=game_saves[0] if game_saves else "", width=40,
                    label_font_size=10, label="Available Saves:", label_position='left', font=("Segoe UI", 10),
                    row=0, column=0)
                self.Button(
                    text="Load Save", font_size=10, bg="#222", padx=10, width=15,
                    command=self._error_as_dialog(self.load_game_save), row=0, column=1)
                delete_button = self.Button(
                    text="Delete (Shift + Click)", font_size=10, bg="#422", padx=20, width=20, command=None,
                    row=0, column=2)
                delete_button.bind("<Shift-Button-1>", self._error_as_dialog(lambda _: self.delete_game_save()))

                self.game_save_entry = self.Entry(
                    width=43, label="New Save Name:", label_position='left', row=1, column=0).var
                create_save_button = self.Button(
                    text="Create Save", font_size=10, bg="#222", padx=10, pady=(10, 0), width=15,
                    command=None, row=1, column=1)
                self.Label(text="Shift + Click to Overwrite", font_size=8, row=2, column=1)
                create_save_button.bind(
                    "<Button-1>",
                    self._error_as_dialog(lambda _: self.create_game_save(overwrite=False)))
                create_save_button.bind(
                    "<Shift-Button-1>",
                    self._error_as_dialog(lambda _: self.create_game_save(overwrite=True)))

    def load_game_save(self):
        selected_game_save = self.game_save_list.get()
        if not selected_game_save:
            return
        self.project.load_game_save(selected_game_save)

    def delete_game_save(self):
        selected_game_save = self.game_save_list.get()
        if not selected_game_save:
            return
        self.project.delete_game_save(selected_game_save)
        self.game_save_list['values'] = self.project.get_game_saves()
        self.game_save_list.set("")

    def create_game_save(self, overwrite=False):
        game_save_name = self.game_save_entry.get()
        self.project.create_game_save(game_save_name, overwrite=overwrite)
        self.game_save_list['values'] = self.project.get_game_saves()

    def _install_psutil(self):
        self.install_psutil_button.var.set("Installing...")
        self.update_idletasks()
        subprocess.run(f"{sys.executable} -m pip install psutil")
        self.install_psutil_button.var.set("Installation successful.")
        self.install_psutil_button['state'] = "disabled"
        self.update_idletasks()
        self.bell()
        self.CustomDialog(
            title="Installation complete", message="psutil installed successfully.\n\nPlease restart Soulstruct.")

    def _error_as_dialog(self, func):
        return error_as_dialog(self, func)
