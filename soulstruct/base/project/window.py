from __future__ import annotations

__all__ = ["ImportSettings", "ProjectCreatorWizard", "ProjectWindow"]

import abc
import logging
import re
import subprocess
import sys
import threading
import time
import tkinter
import typing as tp
from pathlib import Path
from queue import Queue

from soulstruct.containers import Binder
from soulstruct.utilities.text import word_wrap
from soulstruct.utilities.window import SmartFrame

from . import editor_config

from .editors import (
    AIEditor,
    EnumsEditor,
    EventsEditor,
    LightingEditor,
    MapsEditor,
    ParamsEditor,
    TalkEditor,
    TextEditor,
)
from .core import GameDirectoryProject, ProjectDataType
from .exceptions import SoulstructProjectError, RestoreBackupError
from .icon import SOULSTRUCT_ICON
from .links import WindowLinker  # TODO: Move to base, with game subclasses

if tp.TYPE_CHECKING:
    from .runtime import RuntimeManager

_LOGGER = logging.getLogger(__name__)


# Maps tab name to editor window class. Also determines tab order.
# (Runtime dab is always last, followed by any game-specific extras.)
TAB_EDITORS = {
    ProjectDataType.Maps: MapsEditor,
    ProjectDataType.Enums: EnumsEditor,
    ProjectDataType.Params: ParamsEditor,
    ProjectDataType.Lighting: LightingEditor,
    ProjectDataType.Text: TextEditor,
    ProjectDataType.Events: EventsEditor,
    ProjectDataType.AI: AIEditor,
    ProjectDataType.Talk: TalkEditor,
}  # also specifies tab order ("runtime" always comes last, followed by any other game-specific extras)


class ImportSettings(tp.NamedTuple):
    """Constructed from `ProjectCreatorWizard.done()`."""
    import_data_types: list[ProjectDataType]
    data_type_settings: dict[ProjectDataType, dict[str, bool]]
    extra_settings: dict[str, bool]


class ProjectCreatorWizard(SmartFrame):
    """Provides a bunch of checkbuttons for creating a new project."""
    # TODO: Can probably fold the Game Selector into this too?

    import_data_type_bool_vars: dict[ProjectDataType, tkinter.BooleanVar]
    data_type_settings_bool_vars: dict[ProjectDataType, dict[str, tkinter.BooleanVar]]
    extra_bool_vars: dict[str, tkinter.BooleanVar]

    output: ImportSettings | None

    def __init__(
        self,
        master,
        game_name: str,
        supported_data_types: tp.Sequence[ProjectDataType],
        data_type_settings: dict[ProjectDataType, dict[str, tuple[str, bool, str | None]]] = None,
        extra_settings: dict[str, tuple[str, bool, str | None]] = None,
    ):
        super().__init__(master=master, toplevel=True, icon_data=SOULSTRUCT_ICON, window_title="Project Creator Wizard")
        self.import_data_type_bool_vars = {}
        self.data_type_settings_bool_vars = {}
        self.extra_bool_vars = {}
        self.output = None

        # TODO: Game-specific options:
        #  - DS1:
        #     - Rename Japanese regions/events referenced in vanilla EMEVD?
        #     - Remove glitched, unused Duke's Archives regions?

        with self.set_master(column_weights=[1], row_weights=[0, 1, 0], auto_rows=0, sticky="nsew", padx=20, pady=20):
            self.Label(text=game_name, font=24)
            self.build_data_type_settings(supported_data_types, data_type_settings, extra_settings)
            self.Button(
                text="Create Project",
                font=editor_config.HEADING_FONT,
                width=30,
                bg="#622",
                tooltip_text="Import project with selected settings",
                command=lambda: self.done(True),
            )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=False):
        if confirm:
            import_data_types = [
                data_type for data_type, bool_var in self.import_data_type_bool_vars.items() if bool_var.get()
            ]
            data_type_settings = {}
            for data_type, data_type_bool_vars in self.data_type_settings_bool_vars.items():
                if data_type not in import_data_types:
                    continue  # ignore
                data_type_settings[data_type] = {
                    key: bool_var.get() for key, bool_var in data_type_bool_vars.items()
                }
            extra_settings = {key: bool_var.get() for key, bool_var in self.extra_bool_vars.items()}

            self.output = ImportSettings(import_data_types, data_type_settings, extra_settings)

        self.quit()

    def build_data_type_settings(
        self,
        supported_data_type: tp.Sequence[ProjectDataType],
        data_type_settings: dict[ProjectDataType, dict[str, tuple[str, bool, str | None]]] = None,
        extra_settings: dict[str, tuple[str, bool, str | None]] = None,
    ):
        self.import_data_type_bool_vars = {}
        self.data_type_settings_bool_vars = {}
        self.extra_bool_vars = {}

        with self.set_master(column_weights=[1], auto_rows=0, sticky="nsew", padx=20, pady=20):
            for data_type in supported_data_type:
                settings = data_type_settings.get(data_type, {}) if data_type_settings else {}
                with self.set_master(
                    column_weights=[1], row_weights=[1] * (len(settings) + 1), auto_rows=0, sticky="nsew", pady=0
                ):
                    import_check = self.Checkbutton(
                        label=f"Import {data_type.name}",
                        label_position="right",
                        initial_state=True,
                        label_font=editor_config.BOLD_FONT,
                        pady=5,
                        sticky="w",
                    )
                    self.import_data_type_bool_vars[data_type] = import_check.var

                    self.data_type_settings_bool_vars[data_type] = {}
                    for setting_name, (label, initial_state, tooltip) in settings.items():
                        check = self.Checkbutton(
                            label=label,
                            label_position="right",
                            initial_state=initial_state,
                            tooltip_text=tooltip,
                            label_font=editor_config.SMALL_FONT,
                            pady=5,
                            padx=(20, 0),
                            sticky="w",
                        )
                        self.data_type_settings_bool_vars[data_type][setting_name] = check.var

                    if data_type != supported_data_type[-1]:
                        self.Separator(sticky="ew")

            if not extra_settings:
                return

            with self.set_master(
                column_weights=[1], row_weights=[1] * len(extra_settings), auto_rows=0, sticky="nsew", pady=20
            ):
                for bool_key, (bool_label, initial_state, tooltip) in extra_settings.items():
                    check = self.Checkbutton(
                        label=bool_label,
                        initial_state=initial_state,
                        tooltip_text=tooltip,
                        label_font=editor_config.SMALL_FONT,
                        pady=10,
                        anchor="e",
                    )
                    self.extra_bool_vars[bool_key] = check.var


class ProjectWindow(SmartFrame, abc.ABC):

    PROJECT_CLASS: tp.Type[GameDirectoryProject] = None
    LINKER_CLASS: tp.Type[WindowLinker] = WindowLinker
    MAPS_EDITOR_CLASS: tp.Type[MapsEditor] = MapsEditor
    ENUMS_EDITOR_CLASS: tp.Type[EnumsEditor] = EnumsEditor
    PARAMS_EDITOR_CLASS: tp.Type[ParamsEditor] = ParamsEditor
    LIGHTING_EDITOR_CLASS: tp.Type[LightingEditor] = LightingEditor
    TEXT_EDITOR_CLASS: tp.Type[TextEditor] = TextEditor
    EVENT_EDITOR_CLASS: tp.Type[EventsEditor] = EventsEditor
    AI_EDITOR_CLASS: tp.Type[AIEditor] = AIEditor
    TALK_EDITOR_CLASS: tp.Type[TalkEditor] = TalkEditor
    RUNTIME_MANAGER_CLASS: tp.Type[RuntimeManager] = None

    EXTRA_TAB_CLASSES = {}  # maps tab names to classes (they should take `project` argument)
    # TODO: Random specific info to have here. Probably combine into a more general class (when more is actually here).
    CHARACTER_MODELS = {}  # optional game-specific dictionary

    maps_tab: MapsEditor | None
    enums_tab: EnumsEditor | None
    params_tab: ParamsEditor | None
    lighting_tab: LightingEditor | None
    text_tab: TextEditor | None
    events_tab: EventsEditor | None
    ai_tab: AIEditor | None
    talk_tab: TalkEditor | None
    runtime_tab: RuntimeManager | None

    def __init__(self, project_path="", game_root=None, master=None):
        super().__init__(
            master=master,
            toplevel=True,
            icon_data=SOULSTRUCT_ICON,
            window_title=f"{self.PROJECT_CLASS.get_game().name} Project Editor",
        )
        self.withdraw()

        if not project_path:
            # User must select project path.
            self.CustomDialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n"
                + word_wrap(
                    "If you want to create a new project, create an empty directory and select it. "
                    "The name of the directory will be the name of the project.",
                    50,
                ),
            )
            project_path = self.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=str(Path("~/Documents").expanduser())
            )
            if not project_path:
                self.CustomDialog(title="Project Error", message="No directory chosen. Quitting Soulstruct.")
                raise SoulstructProjectError("No directory chosen. Quitting Soulstruct.")

        self.toplevel.title(f"{self.PROJECT_CLASS.get_game().name} Project Editor: {Path(project_path)}")

        try:
            self.project = self.PROJECT_CLASS(project_path, with_window=self, game_root=game_root)
            _LOGGER.info(f"Opened project: {project_path}")
        except SoulstructProjectError as ex:
            self.deiconify()
            msg = (
                f"Fatal Soulstruct project error encountered (see log for full traceback):\n\n"
                f"{word_wrap(str(ex), 50)}\n\nAborting startup."
            )
            _LOGGER.exception("Fatal Soulstruct project error encountered. Aborting startup.")
            self.CustomDialog(title="Project Error", message=msg)
            raise
        except Exception as ex:
            self.deiconify()
            _LOGGER.exception("Fatal internal error encountered. Aborting startup.")
            msg = (
                f"Fatal internal error encountered (see log for full traceback):"
                f"\n\n{word_wrap(str(ex), 50)}\n\nAborting startup."
            )
            self.CustomDialog(title="Internal Error", message=msg)
            raise

        if self.project.is_empty:
            self.destroy()
            _LOGGER.warning("Soulstruct project is empty. Destroying window.")
            return

        self.linker = self.LINKER_CLASS(self)  # TODO: Individual editors should have a lesser linker.

        with self.set_master(column_weights=[1], row_weights=[0, 1], auto_rows=0, sticky="nsew"):
            self.global_ribbon = self.Frame(row_weights=[1], column_weights=[1, 1, 1, 1], pady=(10, 5))
            self.page_tabs = self.Notebook(name="project_notebook", sticky="nsew")

        self.maps_tab = None
        self.enums_tab = None
        self.params_tab = None
        self.text_tab = None
        self.lighting_tab = None
        self.events_tab = None
        self.ai_tab = None
        self.talk_tab = None
        self.runtime_tab = None
        self.tab_frames = {}
        self.extra_tabs = []

        self.save_all_button = None
        self.save_tab_button = None
        self.export_all_button = None
        self.export_tab_button = None

        self.toplevel.minsize(900, 800)
        self.alphanumeric_word_boundaries()
        if getattr(sys, "frozen", False):
            self.toplevel.protocol("WM_DELETE_WINDOW", self.confirm_quit)
        self.build()
        self.deiconify()

        if self.maps_tab:
            self.maps_tab.check_for_repeated_entity_ids()

    def build(self):
        self.build_top_menu()

        with self.set_master(self.global_ribbon, auto_columns=0, grid_defaults={"padx": 5}):
            button_width = 30
            font = editor_config.BOLD_FONT
            self.save_all_button = self.Button(
                text="SAVE FULL PROJECT",
                width=button_width,
                font=font,
                bg="#622",
                tooltip_text="Saves all project data types to local project files. (Ctrl + Shift + S)",
                command=self._save_all,
            )
            self.save_tab_button = self.Button(
                text="SAVE TAB DATA",
                width=button_width,
                font=font,
                tooltip_text="Saves just the indicated data type to local project files. (Ctrl + S)",
                command=lambda: self._save_data(self.current_data_type),
            )
            self.export_tab_button = self.Button(
                text="EXPORT TAB DATA",
                width=button_width,
                font=font,
                tooltip_text=(
                    "Saves and exports just the indicated data type to the game directory. For Events/Talk, exports "
                    "ONLY the currently selected script. (Ctrl + E)"
                ),
                command=lambda: self._export_data(
                    self.current_data_type,
                    self.project.game_root,
                    single_script_only=True,
                ),
            )
            self.export_all_button = self.Button(
                text="EXPORT ALL DATA",
                width=button_width,
                font=font,
                bg="#622",
                tooltip_text="Saves and exports ALL project data files to the game directory. (Ctrl + Shift + E)",
                command=lambda: self._export_all(export_directory=self.project.game_root),
            )

        self.tab_frames = {
            tab_name: self.Frame(frame=self.page_tabs, sticky="nsew", row_weights=[1], column_weights=[1])
            for tab_name in self.ordered_tabs
        }
        for tab_name in self.EXTRA_TAB_CLASSES:
            self.tab_frames[tab_name] = self.Frame(
                frame=self.page_tabs, sticky="nsew", row_weights=[1], column_weights=[1]
            )

        if "maps" in self.tab_frames:
            if self.project.maps:
                self.create_Maps_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Maps, self.project.import_Maps)

        if "enums" in self.tab_frames:
            if self.project.enums_directory.is_dir():
                self.create_Enums_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Enums, self.project.import_Enums)

        if "params" in self.tab_frames:
            if self.project.params:
                self.create_Params_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Params, self.project.import_Params)

        if "lighting" in self.tab_frames:
            if self.project.lighting:
                self.create_Lighting_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Lighting, self.project.import_Lighting)

        if "text" in self.tab_frames:
            if self.project.text:
                self.create_Text_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Text, self.project.import_Text)

        if "events" in self.tab_frames:
            if self.project.events_directory.is_dir():
                self.create_Events_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Events, self.project.import_Events)

        if "ai" in self.tab_frames:
            if self.project.ai:
                self.create_AI_tab()
            else:
                self.create_dummy_tab(ProjectDataType.AI, self.project.import_AI)

        if "talk" in self.tab_frames:
            if self.project.talk_directory.is_dir():
                self.create_Talk_tab()
            else:
                self.create_dummy_tab(ProjectDataType.Talk, self.project.import_Talk)

        # Created now or never.
        if "runtime" in self.tab_frames:
            self.runtime_tab = self.SmartFrame(
                frame=self.tab_frames["runtime"],
                smart_frame_class=self.RUNTIME_MANAGER_CLASS,
                project=self.project,
                sticky="nsew",
            )
            self.runtime_tab.bind("<Visibility>", self._update_banner)

        for tab_name, smart_frame_class in self.EXTRA_TAB_CLASSES.items():
            # `smart_frame_class` just needs to accept `project` argument.
            extra_tab = self.SmartFrame(
                frame=self.tab_frames[tab_name],
                smart_frame_class=smart_frame_class,
                project=self.project,
                sticky="nsew",
            )
            extra_tab.bind("<Visibility>", self._update_banner)
            self.extra_tabs.append(extra_tab)

        for tab_name, tab_frame in self.tab_frames.items():
            self.page_tabs.add(tab_frame, text=f"  {data_type_caps(tab_name)}  ")

        self.create_key_bindings()

        # Default window dimensions are 75% of screen width/height.
        dimensions = (0.75 * self.toplevel.winfo_screenwidth(), 0.75 * self.toplevel.winfo_screenheight())
        self.set_geometry(dimensions=dimensions)

    # region Tab Creators

    def create_Maps_tab(self):
        self.maps_tab = self.SmartFrame(
            frame=self.tab_frames["maps"],
            smart_frame_class=self.MAPS_EDITOR_CLASS,
            project=self.project,
            character_models=self.CHARACTER_MODELS,
            global_map_choice_func=self.set_global_map_choice,
            linker=self.linker,
            sticky="nsew",
        )
        self.maps_tab.bind("<Visibility>", self._update_banner)

    def create_Enums_tab(self):
        self.enums_tab = self.SmartFrame(
            frame=self.tab_frames["enums"],
            smart_frame_class=self.ENUMS_EDITOR_CLASS,
            project=self.project,
            enums_directory=self.project.enums_directory,
            global_map_choice_func=self.set_global_map_choice,
            linker=self.linker,
            sticky="nsew",
        )
        self.enums_tab.bind("<Visibility>", self._update_banner)

    def create_Params_tab(self):
        self.params_tab = self.SmartFrame(
            frame=self.tab_frames["params"],
            smart_frame_class=self.PARAMS_EDITOR_CLASS,
            project=self.project,
            linker=self.linker,
            sticky="nsew",
        )
        self.params_tab.bind("<Visibility>", self._update_banner)

    def create_Lighting_tab(self):
        self.lighting_tab = self.SmartFrame(
            frame=self.tab_frames["lighting"],
            smart_frame_class=self.LIGHTING_EDITOR_CLASS,
            project=self.project,
            linker=self.linker,
            sticky="nsew",
        )
        self.lighting_tab.bind("<Visibility>", self._update_banner)

    def create_Text_tab(self):
        self.text_tab = self.SmartFrame(
            frame=self.tab_frames["text"],
            smart_frame_class=self.TEXT_EDITOR_CLASS,
            project=self.project,
            linker=self.linker,
            sticky="nsew",
        )
        self.text_tab.bind("<Visibility>", self._update_banner)

    def create_Events_tab(self):
        self.events_tab = self.SmartFrame(
            frame=self.tab_frames["events"],
            smart_frame_class=self.EVENT_EDITOR_CLASS,
            project=self.project,
            evs_directory=self.project.project_root / "events",
            game_root=self.project.game_root,
            global_map_choice_func=self.set_global_map_choice,
            text_font_size=self.project.text_editor_font_size,
            sticky="nsew",
        )
        self.events_tab.bind("<Visibility>", self._update_banner)

    def create_AI_tab(self):
        self.ai_tab = self.SmartFrame(
            frame=self.tab_frames["ai"],
            smart_frame_class=self.AI_EDITOR_CLASS,
            project=self.project,
            script_directory=self.project.project_root / "ai_scripts",
            allow_decompile=self.project.get_game().name == "Dark Souls Remastered",
            global_map_choice_func=self.set_global_map_choice,
            text_font_size=self.project.text_editor_font_size,
            linker=self.linker,
            sticky="nsew",
        )
        self.ai_tab.bind("<Visibility>", self._update_banner)

    def create_Talk_tab(self):
        self.talk_tab = self.SmartFrame(
            frame=self.tab_frames["talk"],
            smart_frame_class=self.TALK_EDITOR_CLASS,
            project=self.project,
            esp_directory=self.project.project_root / "talk",
            global_map_choice_func=self.set_global_map_choice,
            text_font_size=self.project.text_editor_font_size,
            linker=self.linker,
            sticky="nsew",
        )
        self.talk_tab.bind("<Visibility>", self._update_banner)

    def create_dummy_tab(self, data_type: ProjectDataType, import_func: tp.Callable):
        """Create a tab that just has a big 'Import' button for this data type."""
        tab = self.Frame(
            frame=self.tab_frames[data_type.value.lower()],
            sticky="nsew",
        )

        def _import_and_create_tab():
            import_func(self.project.game_root)
            tab.destroy()
            getattr(self, f"create_{data_type.name}_tab")()

        with self.set_master(tab):
            self.Button(
                text=f"Import {data_type_caps(data_type.value)}",
                command=_import_and_create_tab,
                font=editor_config.HEADING_FONT,
                bg="#622",
                width=30,
            )

        # Center button.
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        setattr(self, f"{data_type.lower()}_tab", tab)  # will be replaced by real tab when button is clicked
        tab.bind("<Visibility>", self._update_banner)

    # endregion

    def build_top_menu(self):
        top_menu = self.Menu()

        file_menu = self.Menu()
        self._build_file_menu(file_menu)
        top_menu.add_cascade(label="File", menu=file_menu)

        # TODO: edit commands
        # edit_menu = self.Menu()
        # edit_menu.add_command(label="Undo", foreground='#FFF', command=lambda: print("Undo"))
        # edit_menu.add_command(label="Redo", foreground='#FFF', command=lambda: print("Redo"))
        # edit_menu.add_command(label="Copy", foreground='#FFF', command=lambda: print("Copy"))
        # edit_menu.add_command(label="Cut", foreground='#FFF', command=lambda: print("Cut"))
        # edit_menu.add_command(label="Paste", foreground='#FFF', command=lambda: print("Paste"))
        # top_menu.add_cascade(label="Edit", menu=edit_menu)

        tools_menu = self.Menu()
        self._build_tools_menu(tools_menu)
        top_menu.add_cascade(label="Tools", menu=tools_menu)

        scripts_menu = self.Menu()
        self._build_scripts_menu(scripts_menu)
        top_menu.add_cascade(label="Scripts", menu=scripts_menu)

        self.toplevel.config(menu=top_menu)

    def _build_file_menu(self, file_menu):
        save_submenu = self.Menu()
        self._build_save_submenu(save_submenu)
        file_menu.add_cascade(label="Save", foreground="#FFF", menu=save_submenu)

        file_menu.add_separator()

        reload_submenu = self.Menu()
        self._build_reload_submenu(reload_submenu)
        file_menu.add_cascade(label="Reload", foreground="#FFF", menu=reload_submenu)

        file_menu.add_separator()

        import_from_game_submenu = self.Menu()
        self._build_import_submenu(import_from_game_submenu, self.project.game_root)
        file_menu.add_cascade(label="Import from Game", foreground="#FFF", menu=import_from_game_submenu)

        import_from_submenu = self.Menu()
        self._build_import_submenu(import_from_submenu, None)
        file_menu.add_cascade(label="Import from...", foreground="#FFF", menu=import_from_submenu)

        file_menu.add_separator()

        export_to_game_submenu = self.Menu()
        self._build_export_submenu(export_to_game_submenu, self.project.game_root)
        file_menu.add_cascade(label="Export to Game", foreground="#FFF", menu=export_to_game_submenu)

        export_to_submenu = self.Menu()
        self._build_export_submenu(export_to_submenu, None)
        file_menu.add_cascade(label="Export to...", foreground="#FFF", menu=export_to_submenu)

        file_menu.add_separator()

        file_menu.add_command(label="Set as Default Project", foreground="#FFF", command=self._set_as_default_project)
        file_menu.add_command(label="Clear Default Project", foreground="#FFF", command=self._clear_default_project)

        file_menu.add_separator()

        file_menu.add_command(label="Quit", foreground="#FFF", command=self.confirm_quit)

    def _build_save_submenu(self, save_menu):
        save_menu.add_command(label="Save Entire Project", foreground="#FFF", command=self._save_all)
        save_menu.add_separator()
        for data_type in self.data_types:
            save_menu.add_command(
                label=f"Save {data_type_caps(data_type)}",
                foreground="#FFF",
                command=lambda d=data_type: self._save_data(d),
            )

    def _build_reload_submenu(self, reload_menu):
        reload_menu.add_command(label="Reload Entire Project", foreground="#FFF", command=self._reload_data)
        reload_menu.add_separator()
        for data_type in self.data_types:
            reload_menu.add_command(
                label=f"Reload {data_type_caps(data_type)}",
                foreground="#FFF",
                command=lambda d=data_type: self._reload_data(d),
            )

    def _build_import_submenu(self, import_menu, import_dir):
        import_menu.add_command(
            label=f"Import Everything",
            foreground="#FFF",
            command=lambda i=import_dir: self._import_all(import_directory=i),
        )
        import_menu.add_separator()
        for data_type in self.data_types:
            import_menu.add_command(
                label=f"Import {data_type_caps(data_type)}",
                foreground="#FFF",
                command=lambda d=data_type, i=import_dir: self._import_data_type(d, import_directory=i),
            )

    def _build_export_submenu(self, export_menu, export_dir):
        export_menu.add_command(
            label=f"Export Everything",
            foreground="#FFF",
            command=lambda e=export_dir: self._export_all(export_directory=e),
        )
        export_menu.add_separator()
        for data_type in self.data_types:
            export_menu.add_command(
                label=f"Export {data_type_caps(data_type)}",
                foreground="#FFF",
                command=lambda d=data_type, e=export_dir: self._export_data(d, export_directory=e),
            )

    def _build_tools_menu(self, tools_menu):
        tools_menu.add_command(label="Create Game Backup", foreground="#FFF", command=self._create_game_backup)
        tools_menu.add_command(label="Restore Game Backup", foreground="#FFF", command=self._restore_game_backup)
        tools_menu.add_separator()
        tools_menu.add_command(
            label="Restore .bak File", foreground="#FFF", command=lambda: self._restore_backup(full_folder=False)
        )
        tools_menu.add_command(
            label="Restore .bak Files", foreground="#FFF", command=lambda: self._restore_backup(full_folder=True)
        )
        tools_menu.add_separator()
        tools_menu.add_command(label="Unpack BND", foreground="#FFF", command=self._unpack_binder)
        tools_menu.add_command(label="Repack BND", foreground="#FFF", command=self._repack_binder)
        return tools_menu

    def _build_scripts_menu(self, scripts_menu):
        for script in self.project.python_script_directory.rglob("*.py"):
            if script.name.startswith("_"):
                continue  # skipped
            scripts_menu.add_command(label=script.stem, foreground="#FFF", command=lambda s=script: self._run_script(s))
        scripts_menu.add_separator()
        scripts_menu.add_command(label="Open Console", foreground="#FFF", command=self._open_console)

    def _run_script(self, script_path: Path):
        """Run given Python script `script_path` in a subprocess and wait for it to return."""
        completed_process = self.project.run_python_script(script_path.absolute())  # same stdout and stderr
        if completed_process.returncode != 0:
            self.CustomDialog(
                title="Script Error",
                message=f"Script '{script_path.name}' encountered an error. It may have only partially completed.",
            )
            return
        self.CustomDialog(
            title="Script Successful",
            message=f"Script '{script_path.name}' ran successfully.",
        )

    def _open_console(self):
        try:
            # noinspection PyPackageRequirements
            import IPython
        except ImportError:
            self.CustomDialog(
                title="Console Error",
                message="Interactive console requires the `ipython` package to be installed\n"
                        "in your Python environment.",
            )
            _LOGGER.info(f"Interactive console aborted. `ipython` package is not installed.")
            return

        _LOGGER.info("Starting interactive console in new window. Note that it will load the LAST SAVED project data.")
        result = subprocess.run(
            [sys.executable, "-m", "soulstruct", "--console", str(self.project.project_root)],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        if result.returncode not in {0, 3221225786}:  # second code is for window close
            self.CustomDialog(
                title="Console Error",
                message="Interactive console encountered an error and terminated.\n\n"
                        "Project data has not been reloaded, as it may have been corrupted.\n"
                        "If you believe the console may have written malformed data, make\n"
                        "sure to save your project files again from the GUI before closing it\n."
                        "Otherwise, use File > Reload to load any new data written by the console.\n",
            )
            _LOGGER.info(f"Interactive console exited with an unexpected return code: {result.returncode}")
            return
        _LOGGER.info("Interactive console exited properly.")
        if (
            self.CustomDialog(
                title="Reload Project Data?",
                message="Reload maps, params, lighting, and text data to acquire any changes made in the console?",
                button_names=("Yes, reload data", "No, do nothing"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
        ) == 0:
            for data_type in self.project.DATA_TYPES:
                if data_type not in {"maps", "params", "lighting", "text"}:
                    continue
                self.project.load(data_type)  # TODO: fix

    def alphanumeric_word_boundaries(self):
        """See: http://www.tcl.tk/man/tcl8.5/TclCmd/library.htm#M19"""
        self.tk.call("tcl_wordBreakAfter", "", 0)
        self.tk.call("set", "tcl_wordchars", "[a-zA-Z0-9_.]")
        self.tk.call("set", "tcl_nonwordchars", "[^a-zA-Z0-9_.]")

    def create_key_bindings(self):
        self.bind_all("<Control-s>", lambda _: self._save_data(self.current_data_type, mimic_click=True))
        self.bind_all("<Control-S>", lambda _: self._save_all(mimic_click=True))
        self.bind_all(
            "<Control-e>",
            lambda _: self._export_data(
                self.current_data_type, export_directory=self.project.game_root, mimic_click=True
            ),
        )
        self.bind_all(
            "<Control-E>", lambda _: self._export_all(export_directory=self.project.game_root, mimic_click=True)
        )

    def refresh_tab_data(self, data_type: ProjectDataType = None):
        if data_type is None:
            for data_type in self.data_types:
                self.refresh_tab_data(data_type)
        if data_type not in self.data_types:
            raise ValueError(f"Invalid data type name: {data_type}")

        # TODO: Can't refresh AI tab?
        if data_type == ProjectDataType.Events and self.events_tab:
            self.events_tab.scan_evs_files()
            self.events_tab.refresh()
        elif data_type == ProjectDataType.Talk and self.talk_tab:
            self.talk_tab.refresh()
        elif data_type == ProjectDataType.Enums and self.enums_tab:
            self.enums_tab.maps = self.project.maps
            self.enums_tab.refresh_entries()
        elif data_type == ProjectDataType.Params and self.params_tab:
            self.params_tab.refresh_entries()
        elif data_type == ProjectDataType.Maps and self.maps_tab:
            self.maps_tab.refresh_entries()
            self.maps_tab.check_for_repeated_entity_ids()
        elif data_type == ProjectDataType.Lighting and self.lighting_tab:
            self.lighting_tab.refresh_entries()
        elif data_type == ProjectDataType.Text and self.text_tab:
            self.text_tab.refresh_entries()

    def confirm_quit(self):
        if self.CustomDialog(
            title="Quit Soulstruct?",
            message="Quit Soulstruct? Any unsaved changes will be lost.",
            button_names=("Yes, quit", "No, go back"),
            button_kwargs=("YES", "NO"),
            cancel_output=1,
            default_output=1,
        ) == 0:
            self.destroy()

    def destroy(self):
        """Destruction takes a second or so, so we withdraw first to hide the awkward lag."""
        self.withdraw()
        super().destroy()

    def run_creator_wizard(
        self,
        game_name: str,
        supported_data_types: tp.Sequence[ProjectDataType],
        data_type_settings: dict[ProjectDataType, dict[str, tuple[str, bool, str]]],
    ) -> ImportSettings | None:
        """Launch Project Creator Wizard window and block until it returns its boolean dictionary."""
        wizard = ProjectCreatorWizard(
            master=self,
            game_name=game_name,
            supported_data_types=supported_data_types,
            data_type_settings=data_type_settings,
        )
        return wizard.go()

    @property
    def current_data_type(self) -> ProjectDataType | None:
        """Return name of current tab's data type (or None if not data type is connected to the active tab)."""
        tab_index = self.page_tabs.index(self.page_tabs.select())
        tab_name = self.ordered_tabs[tab_index]
        if tab_name == "runtime":
            return None
        if tab_name == "enums":
            return ProjectDataType.Enums
        return ProjectDataType.Maps

    def set_global_map_choice(self, map_id, ignore_tabs=()):
        data_types = self.data_types
        if "maps" not in data_types:
            # Cannot get map to set it globally.
            return
        # noinspection PyUnresolvedReferences
        game_map = self.project.DATA_TYPES[ProjectDataType.Maps].GET_MAP(map_id)
        if "maps" not in ignore_tabs and self.maps_tab:
            if game_map.msb_file_stem is not None:
                self.maps_tab.map_choice.var.set(f"{game_map.msb_file_stem} [{game_map.verbose_name}]")
                self.maps_tab.on_map_choice()
        if "enums" not in ignore_tabs and self.enums_tab:
            if game_map.msb_file_stem is not None:
                self.enums_tab.map_choice.var.set(f"{game_map.msb_file_stem} [{game_map.verbose_name}]")
                self.enums_tab.on_map_choice()
        if ProjectDataType.Events in data_types and self.events_tab and "events" not in ignore_tabs:
            if game_map.emevd_file_stem is not None:
                self.events_tab.map_choice.var.set(f"{game_map.emevd_file_stem} [{game_map.verbose_name})")
                self.events_tab.on_map_choice()
        if ProjectDataType.AI in data_types and self.ai_tab and "ai" not in ignore_tabs:
            if game_map.ai_file_stem is not None:
                self.ai_tab.map_choice.var.set(f"{game_map.ai_file_stem} [{game_map.verbose_name}]")
                self.ai_tab.on_map_choice()
        if ProjectDataType.Talk in data_types and self.talk_tab and "talk" not in ignore_tabs:
            if game_map.esd_file_stem is not None:
                self.talk_tab.map_choice.var.set(f"{game_map.esd_file_stem} [{game_map.verbose_name}]")
                self.talk_tab.on_map_choice()

    def _import_all(self, import_directory: Path = None):
        if import_directory is None:
            import_directory = self._choose_directory()
            if not import_directory:
                return  # Abort import.

        try:
            self._thread_with_loading_dialog(
                "Importing",
                "Importing all data types...",
                self.project.import_all,
                import_directory,
            )
        except Exception as ex:
            message = (
                f"Error occurred while importing data:\n\n{ex}\n\n"
                f"Import operation may have only partially completed."
            )
            return self.CustomDialog(title="Import Error", message=message)

        self.refresh_tab_data()

    def _import_data_type(self, data_type: ProjectDataType, import_directory: Path = None):
        if import_directory is None:
            import_directory = self._choose_directory()
            if not import_directory:
                return  # Abort import.

        # TODO: No options.
        import_func = getattr(self.project, f"import_{data_type.name}")

        try:
            self._thread_with_loading_dialog(
                "Importing",
                f"Importing {data_type.name}...",
                import_func,
                import_directory,
            )
        except Exception as ex:
            message = (
                f"Error occurred while importing data:\n\n{ex}\n\n"
                f"Import operation may have only partially completed."
            )
            return self.CustomDialog(title="Import Error", message=message)

        self.refresh_tab_data(data_type)

    def _save_all(self, mimic_click=False):
        self.events_tab.save_all_evs()
        self.talk_tab.save_selected_esp()  # TODO: not exactly 'save all'
        self.ai_tab.confirm_selected(mimic_click=mimic_click)
        if mimic_click:
            self.mimic_click(self.save_all_button)
        self.project.save_all()

    def _save_data(self, data_type: ProjectDataType, mimic_click=False, single_script_only=False):
        if data_type == ProjectDataType.Events:
            # Saves '.evs.py' file(s) to project 'events' directory.
            self.events_tab.save_selected_evs() if single_script_only else self.events_tab.save_all_evs()
            if mimic_click:
                self.mimic_click(self.save_tab_button)
            return
        elif data_type == ProjectDataType.Talk:
            self.talk_tab.save_selected_esp()
            if mimic_click:
                self.mimic_click(self.save_tab_button)
            return
        elif data_type == ProjectDataType.AI and self.ai_tab.confirm_button["state"] == "normal":
            self.ai_tab.confirm_selected(mimic_click=mimic_click)
            # doesn't return here

        if mimic_click:
            self.mimic_click(self.save_tab_button)

        save_func = getattr(self.project, f"save_{data_type.name}")
        save_func()
        self.flash_bg(self)

    def _reload_data(self, data_type: ProjectDataType):
        if self.CustomDialog(
            title="Reload Project Data?",
            message=f"Are you sure you want to reload project {data_type} data? Any unsaved changes will be lost.",
            button_names=("Yes, reload data", "No, do nothing"),
            button_kwargs=("YES", "NO"),
            cancel_output=1,
            default_output=1,
        ) != 0:
            return

        if data_type == ProjectDataType.Events:
            # No need to reload `EventDirectory` instance.
            self.events_tab.scan_evs_files()
            self.events_tab.refresh()
            return
        elif data_type == ProjectDataType.Talk:
            # No need to reload `TalkDirectory` instance.
            self.talk_tab.refresh()
            return

        load_func = getattr(self.project, f"load_{data_type.name}")
        load_func()
        self.flash_bg(self)

    def _export_all(self,  export_directory=None, mimic_click=False):
        if export_directory is None:
            export_directory = self._choose_directory()
            if not export_directory:
                return  # Abort export.

        # Save active Events and Talk scripts.
        self.events_tab.save_selected_evs()
        if self.talk_tab.active_row_index is not None:
            self.talk_tab.save_selected_esp()

        if mimic_click:
            self.mimic_click(self.export_all_button)

        try:
            self._thread_with_loading_dialog(
                "Exporting",
                f"Exporting all data...",
                self.project.export_all,
                export_directory,
            )
        except Exception as ex:
            _LOGGER.error(f"Error occurred while exporting data.", exc_info=ex)
            message = (
                f"Error occurred while exporting data:\n\n{str(ex)}\n\n"
                f"See full traceback in log. Export operation may have only partially completed."
            )
            return self.CustomDialog(title="Export Error", message=message)

    def _export_data(
        self, data_type: ProjectDataType, export_directory=None, mimic_click=False, single_script_only=False
    ):
        if export_directory is None:
            export_directory = self._choose_directory()
            if not export_directory:
                return  # Abort export.

        if single_script_only:
            if data_type == ProjectDataType.Events:
                # Specifying 'events' here means the selected script only.
                self.events_tab.save_selected_evs()
                self.mimic_click(self.save_tab_button)
                self.events_tab.export_selected_evs(export_directory)
                if mimic_click:
                    self.mimic_click(self.export_tab_button)
                return
            elif data_type == ProjectDataType.Talk:
                # All talk scripts in selected map are exported.
                if self.talk_tab.active_row_index is not None:
                    self.talk_tab.save_selected_esp()
                    self.mimic_click(self.save_tab_button)
                self.talk_tab.export_all_in_map(export_directory)
                if mimic_click:
                    self.mimic_click(self.export_tab_button)
                return
            # Otherwise, ignore `single_script_only` argument.

        if mimic_click:
            self.mimic_click(self.export_tab_button)

        export_func = getattr(self.project, f"export_{data_type.name}")

        try:
            self._thread_with_loading_dialog(
                "Exporting",
                f"Exporting {data_type.name}...",
                export_func,
                export_directory,
            )
        except Exception as ex:
            _LOGGER.error(f"Error occurred while exporting {data_type.name} data.", exc_info=ex)
            message = (
                f"Error occurred while exporting {data_type.name} data:\n\n{str(ex)}\n\n"
                f"See full traceback in log. Export operation may have only partially completed."
            )
            return self.CustomDialog(title="Export Error", message=message)

    def _restore_backup(self, target=None, full_folder=False):
        if target is None:
            if full_folder:
                target = self.FileDialog.askdirectory(
                    title="Choose Folder to Restore Backups", initialdir=str(self.project.game_root)
                )
            else:
                target = self.FileDialog.askopenfilename(
                    title="Choose File to Restore Backup",
                    initialdir=str(self.project.game_root),
                    filetypes=[("Bak file", ".bak")],
                )
            if not target:
                return
        try:
            count = self.project.restore_backup(target=target)
        except RestoreBackupError as e:
            return self.CustomDialog(title="Restore Backup Error", message=str(e))
        if count:
            return self.CustomDialog(
                title="Restore Successful", message=f"{count} '.bak' files restored in folder\n'{str(target)}'."
            )
        return self.CustomDialog("Restore Successful", f"Backup file '{str(target)}' restored.")

    def _unpack_binder(self):
        target = self.FileDialog.askopenfilename(
            title="Choose BND/BHD/BDT File to Unpack", initialdir=str(self.project.game_root)
        )
        if target is None:
            return
        if not re.match(r".*\.[a-z]*(bnd|bhd|bdt)(\.dcx)?$", target):
            return self.CustomDialog(
                title="Invalid BND/BHD/BDT File",
                message=f"A BND/BHD/BDT file (with or without DCX) must be selected.",
            )
        Binder(target).write_unpacked_directory()

    def _repack_binder(self):
        target = self.FileDialog.askdirectory(
            title="Choose Unpacked BND/BHD/BDT Directory to Repack", initialdir=str(self.project.game_root)
        )
        if target is None:
            return
        if not re.match(r".*\.[a-z]*(bnd|bhd|bdt).*", target):
            return self.CustomDialog(
                title="Invalid Directory",
                message=f"An unpacked BND/BHD/BDT directory (with a 'binder_manifest.json' file) must be selected.",
            )
        Binder(target).write()

    def _set_as_default_project(self):
        """Set this project directory as the Soulstruct default in `config.py`."""
        from soulstruct.config import SET_CONFIG

        SET_CONFIG(DEFAULT_PROJECT_PATH=str(self.project.project_root))

    @staticmethod
    def _clear_default_project():
        from soulstruct.config import SET_CONFIG

        SET_CONFIG(DEFAULT_PROJECT_PATH="")

    def _create_game_backup(self):
        backup_path = self.project.game_root / "soulstruct-backup"
        if backup_path.is_dir():
            if (
                self.CustomDialog(
                    title="Confirm Backup Overwrite",
                    message="Backup directory `soulstruct-backup` in game directory already exists. Overwrite?",
                    button_names=("Yes, overwrite", "No, go back"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=1,
                )
                == 1
            ):
                return
        try:
            self.project.create_game_backup(backup_path)
        except Exception as e:
            self.CustomDialog(
                "Backup Error",
                f"Error while creating game file backup:\n\n"
                f"{e}\n\n"
                f"Backup may have only been partially completed.",
            )
            _LOGGER.error(f"Error while creating game file backup: {e}", exc_info=True)
        else:
            self.CustomDialog("Backup Creation Successful", "Backup files created successfully.")

    def _restore_game_backup(self):
        backup_path = self.project.game_root / "soulstruct-backup"
        if not backup_path.is_dir():
            self.CustomDialog(
                "No Backup Created", "Backup folder `soulstruct-backup` has not yet been created in game directory."
            )
            return
        if (
            self.CustomDialog(
                title="Confirm Backup Restore",
                message="Are you sure you want to restore backup Dark Souls files?",
                button_names=("Yes, continue", "No, go back"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
            == 1
        ):
            return
        try:
            self.project.restore_game_backup(backup_path)
        except Exception as e:
            self.CustomDialog(
                "Backup Error",
                f"Error while restoring game file backup:\n\n"
                f"{e}\n\n"
                f"Backup files may have been only partially restored.",
            )
            _LOGGER.error(f"Error while restoring game file backup: {e}", exc_info=True)
        else:
            self.CustomDialog("Backup Restore Successful", "All backup files restored successfully.")

    def _choose_directory(self, initial_dir=None, **kwargs):
        if initial_dir is None:
            initial_dir = str(self.project.project_root)
        directory = self.FileDialog.askdirectory(initialdir=initial_dir, **kwargs)
        if not directory:
            return None
        return Path(directory)

    def _update_banner(self, event):
        try:
            data_name = event.widget.DATA_NAME
        except AttributeError:
            # Dummy tab with no associated data.
            data_name = None
        if data_name is None:
            self.save_tab_button.var.set("SAVE")
            self.export_tab_button.var.set("EXPORT")
            self.save_tab_button["state"] = "disabled"
            self.export_tab_button["state"] = "disabled"
        else:
            self.save_all_button["state"] = "normal"
            self.save_tab_button["state"] = "normal"
            self.export_all_button["state"] = "normal"
            self.export_tab_button["state"] = "normal"
            if data_name == "Events":
                self.save_tab_button.var.set(f"SAVE EVENT SCRIPT")
                self.export_tab_button.var.set(f"EXPORT EVENT SCRIPT")
            elif data_name == "AI":
                self.save_tab_button.var.set(f"SAVE MAP AI")
                self.export_tab_button.var.set(f"EXPORT MAP AI")
            elif data_name == "Talk":
                self.save_tab_button.var.set(f"SAVE TALK SCRIPT")
                self.export_tab_button.var.set(f"EXPORT MAP TALK")
            else:
                self.save_tab_button.var.set(f"SAVE {data_name.upper()}")
                self.export_tab_button.var.set(f"EXPORT {data_name.upper()}")

    def _thread_with_loading_dialog(self, dialog_title: str, dialog_message: str, func: tp.Callable, *args, **kwargs):
        """Run `func(*args, **kwargs)` in another thread while displaying an animated loading dialog in the main thread.

        Returns or raises anything returned or raised by the threaded function.
        """

        output = Queue()
        errors = Queue()

        def _threaded_func():
            try:
                result = func(*args, **kwargs)
            except Exception as thread_ex:
                errors.put(thread_ex)
            else:
                output.put(result)

        loading_dialog = self.LoadingDialog(title=dialog_title, message=dialog_message, maximum=20)
        import_thread = threading.Thread(target=_threaded_func)
        import_thread.start()
        loading_dialog.update()
        loading_dialog.progress.start()
        while import_thread.is_alive():
            loading_dialog.update()
            time.sleep(1 / 60)
        loading_dialog.progress.stop()
        loading_dialog.destroy()

        if not errors.empty():
            raise errors.get()
        return output.get()

    @property
    def data_types(self) -> tuple[ProjectDataType]:
        return tuple(self.PROJECT_CLASS.DATA_TYPES)

    @property
    def ordered_tabs(self) -> list[str]:
        """NOTE: Tab names/keys are just strings, not `ProjectDataType`s."""
        editor_tabs = [
            tab_name.value for tab_name in TAB_EDITORS
            if tab_name in self.PROJECT_CLASS.DATA_TYPES or tab_name == "enums"
        ]
        if self.RUNTIME_MANAGER_CLASS:
            return editor_tabs + ["runtime"]
        return editor_tabs


def data_type_caps(data_type: str):
    return "AI" if data_type.lower() == "ai" else data_type.capitalize()
