import logging
import re
import sys
import threading
import time
from pathlib import Path
from typing import Optional

from soulstruct.bnd import BND
from soulstruct.constants.darksouls1.maps import get_map
from soulstruct.utilities import word_wrap
from soulstruct.utilities.window import SmartFrame

from .core import SoulstructProject
from .ai import SoulstructAIEditor
from .entities import SoulstructEntityEditor
from .events import SoulstructEventEditor
from .icon import SOULSTRUCT_ICON
from .lighting import SoulstructLightingEditor
from .links import WindowLinker
from .maps import SoulstructMapEditor
from .params import SoulstructParamsEditor
from .runtime import SoulstructRuntimeManager
from .talk import SoulstructTalkEditor
from .text import SoulstructTextEditor
from .utilities import SoulstructProjectError, data_type_caps, RestoreBackupError, DATA_TYPES

_LOGGER = logging.getLogger(__name__)


class SoulstructProjectWindow(SmartFrame):
    maps_tab: Optional[SoulstructMapEditor]
    entities_tab: Optional[SoulstructEntityEditor]
    params_tab: Optional[SoulstructParamsEditor]
    lighting_tab: Optional[SoulstructLightingEditor]
    text_tab: Optional[SoulstructTextEditor]
    events_tab: Optional[SoulstructEventEditor]
    ai_tab: Optional[SoulstructAIEditor]
    talk_tab: Optional[SoulstructTalkEditor]

    TAB_ORDER = ['maps', 'entities', 'params', 'lighting', 'text', 'events', 'ai', 'talk', 'runtime']

    def __init__(self, project_path=None, master=None):
        """
        TODO:
            - Auto-save scheduled Tk functions that operate at ten minute intervals.
        """
        super().__init__(master=master, toplevel=True, icon_data=SOULSTRUCT_ICON,
                         window_title="Soulstruct Project Editor")
        self.withdraw()
        self._THREAD_EXCEPTION = None

        if not project_path:
            self.CustomDialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it. "
                    "The name of the directory will be the name of the project.", 50))
            project_path = self.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=str(Path('~/Documents').expanduser()))
            if not project_path:
                self.CustomDialog(title="Project Error", message="No directory chosen. Quitting Soulstruct.")
                raise SoulstructProjectError("No directory chosen. Quitting Soulstruct.")

        self.toplevel.title("Soulstruct Project Editor: " + str(Path(project_path)))

        try:
            self.project = SoulstructProject(project_path, with_window=self)
            _LOGGER.info(f"Opened project: {project_path}")
        except SoulstructProjectError as e:
            self.deiconify()
            msg = (f"Fatal Soulstruct project error encountered (see log for full traceback):\n\n"
                   f"{word_wrap(str(e), 50)}\n\nAbortin startup.")
            _LOGGER.exception("Fatal Soulstruct project error encountered. Aborting startup.")
            self.CustomDialog(title="Project Error", message=msg)
            raise
        except Exception as e:
            self.deiconify()
            _LOGGER.exception("Fatal internal error encountered. Aborting startup.")
            msg = (f"Fatal internal error encountered (see log for full traceback):"
                   f"\n\n{word_wrap(str(e), 50)}\n\nAborting startup.")
            self.CustomDialog(title="Internal Error", message=msg)
            raise

        self.linker = WindowLinker(self)  # TODO: Individual editors should have a lesser linker.

        with self.set_master(column_weights=[1], row_weights=[0, 1], auto_rows=0, sticky='nsew'):
            self.global_ribbon = self.Frame(row_weights=[1], column_weights=[1, 1, 1, 1], pady=(10, 5))
            self.page_tabs = self.Notebook(name="project_notebook", sticky='nsew')

        self.maps_tab = None
        self.entities_tab = None
        self.params_tab = None
        self.text_tab = None
        self.lighting_tab = None
        self.events_tab = None
        self.ai_tab = None
        self.talk_tab = None
        self.runtime_tab = None

        self.save_all_button = None
        self.save_tab_button = None
        self.export_all_button = None
        self.export_tab_button = None

        self.toplevel.minsize(700, 500)
        self.alphanumeric_word_boundaries()
        if getattr(sys, "frozen", False):
            self.toplevel.protocol("WM_DELETE_WINDOW", self.confirm_quit)
        self.build()
        self.deiconify()

    def build(self):
        self.build_top_menu()

        with self.set_master(self.global_ribbon, auto_columns=0, grid_defaults={'padx': 5}):
            self.save_all_button = self.Button(
                text="Save Entire Project", width=20, bg="#622",
                tooltip_text="Saves all project data types to local project files. (Ctrl + Shift + S)",
                command=self._save_data)
            self.save_tab_button = self.Button(
                text="Save Tab Data", width=20,
                tooltip_text="Saves just the indicated data type to local project files. (Ctrl + S)",
                command=lambda: self._save_data(self.current_data_type))
            self.export_tab_button = self.Button(
                text="Export Tab Data", width=20,
                tooltip_text="Saves and exports just the indicated data type to the game directory. (Ctrl + E)",
                command=lambda: self._export_data(self.current_data_type, self.project.game_root))
            self.export_all_button = self.Button(
                text="Export Entire Project", width=20, bg="#622",
                tooltip_text="Saves and exports all project data types to the game directory. (Ctrl + Shift + E)",
                command=lambda: self._export_data(export_directory=self.project.game_root))

        tab_frames = {tab_name: self.Frame(frame=self.page_tabs, sticky='nsew', row_weights=[1], column_weights=[1])
                      for tab_name in self.TAB_ORDER}

        self.maps_tab = self.SmartFrame(
            frame=tab_frames['maps'], smart_frame_class=SoulstructMapEditor,
            maps=self.project.Maps, global_map_choice_func=self.set_global_map_choice,
            linker=self.linker, sticky='nsew')
        self.maps_tab.bind("<Visibility>", self._update_banner)

        self.entities_tab = self.SmartFrame(
            frame=tab_frames['entities'], smart_frame_class=SoulstructEntityEditor,
            maps=self.project.Maps, evs_directory=self.project.project_root / "events",
            global_map_choice_func=self.set_global_map_choice,
            linker=self.linker, sticky='nsew')
        self.entities_tab.bind("<Visibility>", self._update_banner)

        self.params_tab = self.SmartFrame(
            frame=tab_frames['params'], smart_frame_class=SoulstructParamsEditor,
            params=self.project.Params, linker=self.linker, sticky='nsew')
        self.params_tab.bind("<Visibility>", self._update_banner)

        self.lighting_tab = self.SmartFrame(
            frame=tab_frames['lighting'], smart_frame_class=SoulstructLightingEditor,
            lighting=self.project.Lighting, linker=self.linker, sticky='nsew')
        self.lighting_tab.bind("<Visibility>", self._update_banner)

        self.text_tab = self.SmartFrame(
            frame=tab_frames['text'], smart_frame_class=SoulstructTextEditor,
            text=self.project.Text, linker=self.linker, sticky='nsew')
        self.text_tab.bind("<Visibility>", self._update_banner)

        self.events_tab = self.SmartFrame(
            frame=tab_frames['events'], smart_frame_class=SoulstructEventEditor,
            evs_directory=self.project.project_root / "events", game_root=self.project.game_root,
            global_map_choice_func=self.set_global_map_choice,
            dcx=self.project.game_name == "Dark Souls Remastered", sticky='nsew')
        self.events_tab.bind("<Visibility>", self._update_banner)

        self.ai_tab = self.SmartFrame(
            frame=tab_frames['ai'], smart_frame_class=SoulstructAIEditor,
            ai=self.project.AI, script_directory=self.project.project_root / "ai_scripts",
            game_root=self.project.game_root, allow_decompile=self.project.game_name == "Dark Souls Remastered",
            global_map_choice_func=self.set_global_map_choice,
            linker=self.linker, sticky='nsew')
        self.ai_tab.bind("<Visibility>", self._update_banner)

        self.talk_tab = self.SmartFrame(
            frame=tab_frames['talk'], smart_frame_class=SoulstructTalkEditor,
            esp_directory=self.project.project_root / "talk", game_root=self.project.game_root,
            game_name=self.project.game_name,
            global_map_choice_func=self.set_global_map_choice,
            linker=self.linker, sticky='nsew'
        )
        self.talk_tab.bind("<Visibility>", self._update_banner)

        self.runtime_tab = self.SmartFrame(
            frame=tab_frames['runtime'], smart_frame_class=SoulstructRuntimeManager,
            project=self.project, sticky='nsew')
        self.runtime_tab.bind("<Visibility>", self._update_banner)

        for tab_name, tab_frame in tab_frames.items():
            self.page_tabs.add(tab_frame, text=f'  {data_type_caps(tab_name)}  ')

        self.create_key_bindings()

        self.set_geometry()

    def build_top_menu(self):
        top_menu = self.Menu()

        file_menu = self.Menu(tearoff=0)
        save_menu = self.Menu(tearoff=0)
        save_menu.add_command(
            label=f"Save Entire Project", foreground='#FFF',
            command=self._save_data)
        save_menu.add_separator()
        for data_type in DATA_TYPES:
            save_menu.add_command(
                label=f"Save {data_type_caps(data_type)}", foreground='#FFF',
                command=lambda d=data_type: self._save_data(d))
        file_menu.add_cascade(label=f"Save", foreground='#FFF', menu=save_menu)
        file_menu.add_separator()
        for import_dir in (self.project.game_root, None):
            import_menu = self.Menu(tearoff=0)
            import_menu.add_command(
                label=f"Import Everything", foreground='#FFF',
                command=lambda i=import_dir: self._import_data(import_directory=i))
            import_menu.add_separator()
            for data_type in DATA_TYPES:
                import_menu.add_command(
                    label=f"Import {data_type_caps(data_type)}", foreground='#FFF',
                    command=lambda d=data_type, i=import_dir: self._import_data(d, import_directory=i))
            file_menu.add_cascade(label=f"Import from{' Game' if import_dir else '...'}",
                                  foreground='#FFF', menu=import_menu)
        file_menu.add_separator()
        for export_dir in (self.project.game_root, None):
            export_menu = self.Menu(tearoff=0)
            export_menu.add_command(
                label=f"Export Everything", foreground='#FFF',
                command=lambda e=export_dir: self._export_data(export_directory=e))
            export_menu.add_separator()
            for data_type in DATA_TYPES:
                export_menu.add_command(
                    label=f"Export {data_type_caps(data_type)}", foreground='#FFF',
                    command=lambda d=data_type, e=export_dir: self._export_data(d, export_directory=e))
            file_menu.add_cascade(label=f"Export to{' Game' if export_dir else '...'}",
                                  foreground='#FFF', menu=export_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Set as Default Project", foreground='#FFF',
                              command=self._set_as_default_project)
        file_menu.add_command(label="Clear Default Project", foreground='#FFF',
                              command=self._clear_default_project)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", foreground='#FFF', command=self.confirm_quit)
        top_menu.add_cascade(label="File", menu=file_menu)

        tools_menu = self.Menu(tearoff=0)
        tools_menu.add_command(label="Restore .bak File", foreground='#FFF',
                               command=lambda: self._restore_backup(full_folder=False))
        tools_menu.add_command(label="Restore .bak Files", foreground='#FFF',
                               command=lambda: self._restore_backup(full_folder=True))
        tools_menu.add_separator()
        tools_menu.add_command(label="Unpack BND", foreground='#FFF',
                               command=self._unpack_bnd)
        tools_menu.add_command(label="Repack BND", foreground='#FFF',
                               command=self._repack_bnd)
        top_menu.add_cascade(label="Tools", menu=tools_menu)

        # TODO: edit commands
        # edit_menu = self.Menu(tearoff=0)
        # edit_menu.add_command(label="Undo", foreground='#FFF', command=lambda: print("Undo"))
        # edit_menu.add_command(label="Redo", foreground='#FFF', command=lambda: print("Redo"))
        # edit_menu.add_command(label="Copy", foreground='#FFF', command=lambda: print("Copy"))
        # edit_menu.add_command(label="Cut", foreground='#FFF', command=lambda: print("Cut"))
        # edit_menu.add_command(label="Paste", foreground='#FFF', command=lambda: print("Paste"))
        # top_menu.add_cascade(label="Edit", menu=edit_menu)

        self.toplevel.config(menu=top_menu)

    def alphanumeric_word_boundaries(self):
        """See: http://www.tcl.tk/man/tcl8.5/TclCmd/library.htm#M19"""
        self.tk.call('tcl_wordBreakAfter', '', 0)
        self.tk.call('set', 'tcl_wordchars', '[a-zA-Z0-9_.]')
        self.tk.call('set', 'tcl_nonwordchars', '[^a-zA-Z0-9_.]')

    def create_key_bindings(self):
        self.bind_all("<Control-s>", lambda _: self._save_data(self.current_data_type, mimic_click=True))
        self.bind_all("<Control-S>", lambda _: self._save_data(mimic_click=True))
        self.bind_all("<Control-e>", lambda _: self._export_data(
            self.current_data_type, export_directory=self.project.game_root, mimic_click=True))
        self.bind_all("<Control-E>", lambda _: self._export_data(
            export_directory=self.project.game_root, mimic_click=True))

    def refresh_tab_data(self, data_type=None):
        if data_type is None:
            for data_type in self.TAB_ORDER:
                self.refresh_tab_data(data_type)
        data_type = data_type.lower()
        if data_type not in self.TAB_ORDER:
            raise ValueError(f"Invalid data type name: {data_type}")

        if data_type == "events":
            self.events_tab.scan_evs_files()
            self.events_tab.refresh()
        elif data_type == "talk":
            self.talk_tab.refresh()
        elif data_type == "entities":
            self.entities_tab.Maps = self.project.Maps
            self.entities_tab.refresh_entries()
        elif data_type == "runtime":
            pass
        else:
            project_data = getattr(self.project, data_type_caps(data_type))
            setattr(getattr(self, f'{data_type}_tab'), data_type_caps(data_type), project_data)
            if data_type == "params":
                self.params_tab.refresh_entries()
            elif data_type == "maps":
                self.maps_tab.refresh_entries()
            elif data_type == "lighting":
                self.lighting_tab.refresh_entries()
            elif data_type == "text":
                self.text_tab.refresh_entries()

    def confirm_quit(self):
        if self.CustomDialog(title="Quit Soulstruct?",
                             message="Quit Soulstruct? Any unsaved changes will be lost.",
                             button_names=("Yes, quit", "No, go back"),
                             button_kwargs=('YES', 'NO'),
                             cancel_output=1, default_output=1) == 0:
            self.destroy()

    def destroy(self):
        """Destruction takes a second or so, so we withdraw first to hide the awkward lag."""
        self.withdraw()
        super().destroy()

    @property
    def current_data_type(self):
        data_type = self.TAB_ORDER[self.page_tabs.index(self.page_tabs.select())]
        if data_type == "entities":
            return "maps"
        return data_type

    def set_global_map_choice(self, map_id, ignore_tabs=()):
        game_map = get_map(map_id)
        if "maps" not in ignore_tabs:
            try:
                self.maps_tab.map_choice.var.set(
                    f"{game_map.msb_file_stem} [{game_map.verbose_name}]")
            except KeyError:
                pass
        if "entities" not in ignore_tabs:
            try:
                self.entities_tab.map_choice.var.set(
                    f"{game_map.msb_file_stem} [{game_map.verbose_name}]")
            except KeyError:
                pass
        if "events" not in ignore_tabs:
            try:
                self.events_tab.map_choice.var.set(
                    f"{game_map.emevd_file_stem} [{game_map.verbose_name})")
            except KeyError:
                pass
        if "ai" not in ignore_tabs:
            try:
                self.ai_tab.bnd_choice.var.set(
                    f"{game_map.ai_file_stem} [{game_map.verbose_name}]")
            except KeyError:
                pass
        if "talk" not in ignore_tabs:
            try:
                self.talk_tab.map_choice.var.set(
                    f"{game_map.esd_file_stem} [{game_map.verbose_name}]")
            except KeyError:
                pass

    def _import_data(self, data_type=None, import_directory=None):
        if import_directory is None:
            import_directory = self._choose_directory()
            if import_directory is None:
                return  # Abort import.

        def _threaded_import():
            try:
                self.project.import_data(data_type, import_directory)
            except Exception as e:
                self._THREAD_EXCEPTION = e
                raise

        loading = self.LoadingDialog(
            title="Importing...", message=f"Importing {data_type if data_type is not None else 'all files'}...",
            maximum=20)
        import_thread = threading.Thread(target=_threaded_import)
        import_thread.start()
        loading.update()
        loading.progress.start()
        while import_thread.is_alive():
            loading.update()
            time.sleep(1 / 60)
        loading.progress.stop()
        loading.destroy()

        if self._THREAD_EXCEPTION:
            message = (f"Error occurred while importing data:\n\n{str(self._THREAD_EXCEPTION)}\n\n"
                       f"Import operation may have only partially completed.")
            self._THREAD_EXCEPTION = None
            return self.CustomDialog(title="Import Error", message=message)

        self.refresh_tab_data(data_type)

    def _save_data(self, data_type=None, mimic_click=False):
        if data_type == "runtime":
            return  # nothing to save
        elif data_type == "events":
            self.events_tab.save_selected_evs()
            if mimic_click:
                self.mimic_click(self.save_tab_button)
            return
        elif data_type == "talk":
            self.talk_tab.save_selected_esp()
            if mimic_click:
                self.mimic_click(self.save_tab_button)
            return
        elif data_type == "ai" and self.ai_tab.confirm_button["state"] == "normal":
            self.ai_tab.confirm_selected(mimic_click=mimic_click)
            # doesn't return here
        if mimic_click:
            if data_type is None:
                self.mimic_click(self.save_all_button)
            else:
                self.mimic_click(self.save_tab_button)
        self.project.save(data_type)  # doesn't save events
        if data_type is None:
            self.events_tab.save_all_evs()  # saves EVS files to project subdirectory
        self.flash_bg(self)

    def _export_data(self, data_type=None, export_directory=None, mimic_click=False):
        if export_directory is None:
            export_directory = self._choose_directory()
            if export_directory is None:
                return  # Abort export.
        if data_type == "events":
            # Specifying 'events' here means the selected script only.
            self.events_tab.save_selected_evs()
            self.mimic_click(self.save_tab_button)
            self.events_tab.export_selected_evs(export_directory)
            if mimic_click:
                self.mimic_click(self.export_tab_button)
            return
        elif data_type == "talk":
            # All talk scripts in selected map are exported.
            if self.talk_tab.active_row_index is not None:
                self.talk_tab.save_selected_esp()
                self.mimic_click(self.save_tab_button)
            self.talk_tab.export_all_in_map(export_directory)
            if mimic_click:
                self.mimic_click(self.export_tab_button)
            return

        if mimic_click:
            if data_type is None:
                self.mimic_click(self.export_all_button)
            else:
                self.mimic_click(self.export_tab_button)

        def _threaded_export():
            try:
                self.project.export_data(data_type, export_directory)
            except Exception as e:
                self._THREAD_EXCEPTION = e
                raise

        loading = self.LoadingDialog(
            title="Exporting...", message=f"Exporting {data_type if data_type is not None else 'all files'}...",
            maximum=20)
        export_thread = threading.Thread(target=_threaded_export)
        export_thread.start()
        loading.update()
        loading.progress.start()
        while export_thread.is_alive():
            loading.update()
            time.sleep(1 / 60)
        loading.progress.stop()
        loading.destroy()

        if self._THREAD_EXCEPTION:
            message = (f"Error occurred while exporting data:\n\n{str(self._THREAD_EXCEPTION)}\n\n"
                       f"Export operation may have only partially completed.")
            self._THREAD_EXCEPTION = None
            return self.CustomDialog(title="Export Error", message=message)

    def _restore_backup(self, target=None, full_folder=False):
        if target is None:
            if full_folder:
                target = self.FileDialog.askdirectory(
                    title="Choose Folder to Restore Backups", initialdir=str(self.project.game_root))
            else:
                target = self.FileDialog.askopenfilename(
                    title="Choose File to Restore Backup", initialdir=str(self.project.game_root),
                    filetypes=[("Bak file", ".bak")])
            if not target:
                return
        try:
            count = self.project.restore_backup(target=target)
        except RestoreBackupError as e:
            return self.CustomDialog(title="Restore Backup Error", message=str(e))
        if count:
            return self.CustomDialog(
                title="Restore Successful",
                message=f"{count} '.bak' files restored in folder\n'{str(target)}'.")
        return self.CustomDialog("Restore Successful", f"Backup file '{str(target)}' restored.")

    def _unpack_bnd(self):
        target = self.FileDialog.askopenfilename(
            title="Choose BND File to Unpack", initialdir=str(self.project.game_root))
        if target is None:
            return
        if not re.match(r".*\.[a-z]*bnd(\.dcx)?$", target):
            return self.CustomDialog(
                title="Invalid BND File",
                message=f"A valid BND file (with or without DCX) must be selected.")
        BND(target).write_unpacked_dir()

    def _repack_bnd(self):
        target = self.FileDialog.askdirectory(
            title="Choose Unpacked BND Directory to Repack", initialdir=str(self.project.game_root))
        if target is None:
            return
        if not re.match(r".*\.[a-z]*bnd", target):
            return self.CustomDialog(
                title="Invalid Directory",
                message=f"A valid unpacked BND directory (with a 'bnd_manifest.txt' file) must be selected.")
        BND(target).write()

    def _set_as_default_project(self):
        """Set this project directory as the Soulstruct default in `config.py`."""
        from soulstruct._config import SET_CONFIG
        SET_CONFIG(default_project_path=str(self.project.project_root))

    @staticmethod
    def _clear_default_project():
        from soulstruct._config import SET_CONFIG
        SET_CONFIG(default_project_path='')

    def _choose_directory(self, initial_dir=None, **kwargs):
        if initial_dir is None:
            initial_dir = str(self.project.project_root)
        directory = self.FileDialog.askdirectory(initialdir=initial_dir, **kwargs)
        if directory is None:
            return None
        return Path(directory)

    def _update_banner(self, event):
        try:
            data_name = event.widget.DATA_NAME
        except AttributeError:
            raise AttributeError(f"No `DATA_NAME` for widget: {type(event.widget)}")
        if data_name is None:
            self.save_tab_button.var.set(f"Save")
            self.export_tab_button.var.set(f"Export")
            self.save_tab_button["state"] = "disabled"
            self.export_tab_button["state"] = "disabled"
        else:
            self.save_all_button["state"] = "normal"
            self.save_tab_button["state"] = "normal"
            self.export_all_button["state"] = "normal"
            self.export_tab_button["state"] = "normal"
            if data_name == "Events":
                self.save_tab_button.var.set(f"Save Event Script")
                self.export_tab_button.var.set(f"Export Event Script")
            elif data_name == "AI":
                self.save_tab_button.var.set(f"Save All AI")
                self.export_tab_button.var.set(f"Export All AI")
            elif data_name == "Talk":
                self.save_tab_button.var.set(f"Save Talk Script")
                self.export_tab_button.var.set(f"Export All Talk in Map")
            else:
                self.save_tab_button.var.set(f"Save {data_name}")
                self.export_tab_button.var.set(f"Export {data_name}")
