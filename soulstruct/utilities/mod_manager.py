import logging
import os
import shutil
from pathlib import Path

from soulstruct.config import DSR_PATH
from soulstruct.darksouls1r.utilities.file_list import DSR_FILE_LIST
from soulstruct.utilities.files import read_json, write_json
from soulstruct.utilities.window import SmartFrame

_LOGGER = logging.getLogger("visionaut.mod_manager")


class ModManagerWindow(SmartFrame):
    """Simple GUI for managing mod installations and easily recording/restoring vanilla files.

    Currently for Dark Souls: Remastered only.
    """

    DEFAULT_VANILLA_BACKUP = "vanilla-backup"  # inside `game_path`

    def __init__(self, game_path=None, vanilla_backup=None):
        super().__init__(toplevel=True, window_title="Dark Souls Mod Manager")
        if not game_path:
            game_path = Path(DSR_PATH)
        game_path = Path(game_path)
        if game_path.is_file() and game_path.name == "DarkSoulsRemastered.exe":
            self._game_path = game_path.parent
        elif game_path.is_dir() and (game_path / "DarkSoulsRemastered.exe").is_file():
            self._game_path = game_path
        else:
            raise ValueError(f"`game_path` should point to DARK SOULS REMASTERED folder or the executable within.")

        self.backup_path = self._game_path / self.DEFAULT_VANILLA_BACKUP if not vanilla_backup else Path(vanilla_backup)

        if self._manager_json_path.is_file():
            self.mods = read_json(self._manager_json_path)
        else:
            self.mods = []

        with self.set_master(padx=20, pady=20, auto_rows=0):
            self.Label(text="Mod Manager", font=("Segoe UI", 25), pady=(5, 10))
            with self.set_master(auto_columns=0, grid_defaults={"padx": 10}):
                with self.set_master(width=20, auto_rows=0):
                    self.Label(text="Mod List:")
                    self.mod_list = self.Listbox(font=16, height=10, width=20, sticky="ew")
                    with self.set_master(auto_columns=0, pady=5, grid_defaults={"padx": 5}):
                        self.Button(text="Forget Mod", width=20, command=self._delete_mod)
                        self.Button(text="Show Mod Path", width=20, command=self._show_selected_paths)
                with self.set_master(auto_rows=0, grid_defaults={"pady": 5}):
                    self.mod_nickname = self.Entry(width=40, label="Mod Nickname:", sticky="e")
                    self.mod_path = self.Entry(width=40, label="Mod Root Directory:", sticky="e")
                    with self.set_master(auto_columns=0, pady=10, grid_defaults={"padx": 5}):
                        self.Button(text="Browse to Mod Root", width=20, command=self._browse_to_mod)
                        self.Button(text="Add to Mod List", width=20, command=self._add_mod)

                    self.Button(text="Add Root to Selected Mod", width=30, command=self._add_root_to_selected)

                    self.Button(text="Install Mod", width=40, command=self._install_mod, pady=20, bg="#622")

                    self.Button(text="Create Vanilla Backup", width=40, command=self._create_vanilla_backup)
                    self.Button(
                        text="Restore Vanilla Backup", width=40, command=self._restore_vanilla_backup, bg="#226"
                    )
                    self.Button(text="Delete Bak Files", width=40, command=self._delete_bak_files, bg="#226")

        for mod_info in self.mods:
            self.mod_list.insert("end", mod_info["nickname"])

        self.set_geometry()

    def _browse_to_mod(self):
        directory = str(self._choose_directory())
        if directory:
            self.mod_path.var.set(directory)

    def _add_mod(self):
        mod_nickname = self.mod_nickname.var.get()
        mod_path = self.mod_path.var.get()
        if mod_nickname and mod_path:
            if not Path(mod_path).is_dir():
                self.CustomDialog("Invalid Mod Directory", f"Directory {mod_path} does not exist.")
                return
            mod_info = {"nickname": mod_nickname, "root_paths": [mod_path]}
            if any(info == mod_info for info in self.mods):
                self.CustomDialog(
                    "Mod Already Added", f"A mod named {mod_nickname} with that path is already in the list."
                )
                return
            self.mod_list.insert("end", mod_nickname)
            self.mods.append(mod_info)
            self._write_manager_json()
        else:
            if not mod_nickname:
                self.flash_bg(self.mod_nickname, "#622")
            if not mod_path:
                self.flash_bg(self.mod_path, "#622")

    def _delete_mod(self):
        try:
            selected = self.mod_list.curselection()[0]
        except IndexError:
            self.CustomDialog("No Mod Selected", "You must select a mod to delete.")
            return
        self.mods.pop(selected)
        self.mod_list.delete(selected)
        self._write_manager_json()

    def _add_root_to_selected(self):
        try:
            selected = self.mod_list.curselection()[0]
        except IndexError:
            self.CustomDialog("No Mod Selected", "You must select a mod to add the root to.")
            return
        mod_path = self.mod_path.var.get()
        if not mod_path:
            self.CustomDialog("No Mod Path", "No mod path was given.")
        if not Path(mod_path).is_dir():
            self.CustomDialog("Invalid Mod Directory", f"Directory {mod_path} does not exist.")
            return
        if self.mod_nickname.var.get():
            self.CustomDialog("Nickname Given", "The nickname box must be empty to add the root to the selected mod.")
            return
        mod_info = self.mods[selected]
        mod_info["root_paths"].append(mod_path)
        self._write_manager_json()

    def _install_mod(self, ignore_unrecognized=False):
        try:
            selected = self.mod_list.curselection()[0]
        except IndexError:
            self.CustomDialog("No Mod Selected", "You must select a mod to install.")
            return
        mod_info = self.mods[selected]
        self._restore_vanilla_backup(get_confirmation=False)
        mod_root_paths = [Path(p) for p in mod_info["root_paths"]]

        # Validate mod paths.
        for mod_root_path in mod_root_paths:
            if not mod_root_path.is_dir():
                self.CustomDialog("Mod Path Error", f"Could not find mod root path: {mod_root_path}.")
                return
            if not ignore_unrecognized:
                unrecognized_files = []
                for mod_file in mod_root_path.rglob("*"):
                    if mod_file.is_file():
                        relative_mod_file = str(mod_file.relative_to(mod_root_path).as_posix())  # with forward slashes
                        if relative_mod_file not in DSR_FILE_LIST:
                            unrecognized_files.append(relative_mod_file)
                if unrecognized_files:
                    if len(unrecognized_files) > 10:
                        unrecognized_files = unrecognized_files[:9] + [f"...{len(unrecognized_files) - 10} more files"]
                    file_str = "\n".join(unrecognized_files)
                    confirm = self.yesno_dialog(
                        "Ignore Unrecognized Files?",
                        "Mod folder contains non-game files:\n\n"
                        + file_str
                        + "\n\n" "Continue with installation anyway?",
                    )
                    if not confirm:
                        return

        # Install
        file_count = 0
        for mod_root_path in mod_root_paths:
            for mod_file in mod_root_path.rglob("*"):
                if mod_file.is_file():
                    relative_mod_file = str(mod_file.relative_to(mod_root_path).as_posix())  # with forward slashes
                    if relative_mod_file not in DSR_FILE_LIST:
                        continue
                    dest_file = str(Path(DSR_PATH) / relative_mod_file)
                    shutil.copy2(str(mod_file), dest_file)
                    file_count += 1

        _LOGGER.info(f"Installed {mod_info['nickname']} successfully ({file_count} files).")
        self.CustomDialog("Success", "Mod installed successfully.")

    def _create_vanilla_backup(self):
        confirm = self.yesno_dialog(
            "Confirm Vanilla Backup Creation",
            "Are you sure you want to create a backup of all vanilla game files? This "
            "may take several minutes.\n\n"
            f"The backup will be created in '{self.backup_path}' in your game directory. "
            "Existing backup files will only be replaced if they have a different size or "
            "last-modified time.",
        )
        if not confirm:
            return
        backup_count = 0
        for dsr_file in DSR_FILE_LIST:
            source_path = self._game_path / dsr_file
            dest_path = self.backup_path / dsr_file
            if dest_path.is_file():
                source_path_stat = source_path.stat()
                dest_path_stat = dest_path.stat()
                if (
                    source_path_stat.st_mtime == dest_path_stat.st_mtime
                    and source_path_stat.st_size == dest_path_stat.st_size
                ):
                    continue  # vanilla file with same size and modified time already exists
            elif not dest_path.is_file():
                dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(source_path), str(dest_path))
            backup_count += 1

        _LOGGER.info(f"Backed up vanilla files with Mod Manager ({backup_count} files).")
        self.CustomDialog("Success", "Vanilla backup files created successfully.")

    def _restore_vanilla_backup(self, get_confirmation=True):
        if get_confirmation:
            confirm = self.yesno_dialog(
                "Confirm Vanilla Restoration",
                "Are you sure you want to restore vanilla game files? Note that this is "
                "also done automatically before installing any mod.\n\n"
                "Files will only be restored if their size or last-modified time "
                f"have changed from the file in '{self.backup_path}'.",
            )
            if not confirm:
                return
        restore_count = 0
        for dsr_file in DSR_FILE_LIST:
            source_path = self.backup_path / dsr_file
            dest_path = self._game_path / dsr_file
            if dest_path.is_file():
                source_path_stat = source_path.stat()
                dest_path_stat = dest_path.stat()
                if (
                    source_path_stat.st_mtime == dest_path_stat.st_mtime
                    and source_path_stat.st_size == dest_path_stat.st_size
                ):
                    continue  # vanilla file with same size and modified time already exists
            elif not dest_path.is_file():
                dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(source_path), str(dest_path))
            restore_count += 1
        _LOGGER.info(f"Restored {restore_count} vanilla files with Mod Manager.")
        if get_confirmation:
            self.CustomDialog("Success", f"Restored {restore_count} vanilla files successfully.")

    def _delete_bak_files(self, get_confirmation=True):
        """Delete all files with a suffix ending in 'bak' (e.g. '.bak', '.smbak')."""
        if get_confirmation:
            confirm = self.yesno_dialog(
                "Confirm Bak Deletion",
                "Are you sure you want to delete all files whose name ends in 'bak'?",
            )
            if not confirm:
                return
        deletion_count = 0
        for bak_path in self._game_path.glob("**/*bak"):
            os.remove(bak_path)
            deletion_count += 1
        _LOGGER.info(f"Deleted {deletion_count} 'bak' files with Mod Manager.")
        if get_confirmation:
            self.CustomDialog("Success", f"Deleted {deletion_count} 'bak' files successfully.")

    def _show_selected_paths(self):
        try:
            selected = self.mod_list.curselection()[0]
        except IndexError:
            self.CustomDialog("Mod Root Paths", "No mod selected.")
        else:
            self.CustomDialog("Mod Root Paths", "\n".join(self.mods[selected]["root_paths"]), font_type="Consolas")

    def _write_manager_json(self):
        write_json(self._manager_json_path, self.mods)

    @property
    def _manager_json_path(self):
        return self._game_path / "SoulstructModManager.json"

    def _choose_directory(self, initial_dir=None, **kwargs):
        if initial_dir is None:
            initial_dir = DSR_PATH
        directory = self.FileDialog.askdirectory(initialdir=initial_dir, **kwargs)
        if not directory:
            return None
        return Path(directory)


if __name__ == "__main__":
    ModManagerWindow().wait_window()
