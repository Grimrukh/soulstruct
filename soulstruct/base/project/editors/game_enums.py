from __future__ import annotations

__all__ = ["EnumsEditor"]

import inspect
import logging
import re
import sys
import types
import typing as tp
from pathlib import Path

from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.base.project.editors.base_editor import BaseEditor, EntryRow
from soulstruct.base.project.utilities import bind_events
from soulstruct.utilities.files import import_arbitrary_file
from soulstruct.utilities.text import word_wrap

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.map_studio_directory import MapStudioDirectory
    from soulstruct.base.maps.msb import MSB, MSBEntry, MSBEntryList

_LOGGER = logging.getLogger(__name__)

ENTRY_LIST_FG_COLORS = {
    "Parts": "#DDF",
    "Regions": "#FDD",
    "Events": "#DFD",
}

ENTITY_GAME_TYPES = (
    MapPiece,
    Object,
    Character,
    PlayerStart,
    Collision,
    SoundEvent,
    VFXEvent,
    SpawnerEvent,
    MessageEvent,
    SpawnPointEvent,
    NavigationEvent,
    RegionPoint,
    RegionSphere,
    RegionCylinder,
    RegionBox,
)

_RE_ENUM_CLASS = re.compile(r"^class (\w+)\(\w+\): *$")
_RE_ENUM_MEMBER = re.compile(r"^ +([\w_]+) *= *(\d+) *#(.*)$")


class EnumEntryRow(EntryRow):
    """Entry rows for Maps have no ID, and also display their Entity ID field if they have a non-default value."""

    master: EnumsEditor

    ENTRY_ID_WIDTH = 15
    SHOW_ENTRY_ID = True
    EDIT_ENTRY_ID = True
    ENTRY_TEXT_WIDTH = 40
    ENTRY_DESCRIPTION_WIDTH = 110

    # noinspection PyMissingConstructor
    def __init__(self, editor: EnumsEditor, row_index: int, main_bindings: dict = None):
        self.master = editor
        self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

        self.row_index = row_index
        self._entry_id = None
        self._entry_text = None
        self._entry_description = None
        self._active = False
        self.maps_link = None

        bg_color = self._get_color()

        self.row_box = editor.Frame(
            width=self.ENTRY_ID_WIDTH + self.ENTRY_TEXT_WIDTH + self.ENTRY_DESCRIPTION_WIDTH,
            height=self.ENTRY_ROW_HEIGHT,
            bg=bg_color,
            row=row_index,
            columnspan=2,
            sticky="nsew",
        )
        bind_events(self.row_box, main_bindings)

        self.id_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky="ew")
        self.id_label = editor.Label(
            self.id_box,
            text="",
            width=self.ENTRY_ID_WIDTH,
            bg=bg_color,
            fg=self.ENTRY_ID_FG,
            sticky="e",
        )
        if self.EDIT_ENTRY_ID:
            id_bindings = main_bindings.copy()
            id_bindings["<Button-1>"] = lambda _, i=row_index: self.master.select_entry_row_index(
                i, id_clicked=True
            )
            # id_bindings["<Shift-Button-1>"] = lambda _, i=row_index: self.master.popout_entry_id_edit(i)
        else:
            id_bindings = main_bindings
        bind_events(self.id_box, id_bindings)
        bind_events(self.id_label, id_bindings)

        self.text_box = editor.Frame(row=row_index, column=1, bg=bg_color, sticky="ew")
        self.text_label = editor.Label(
            self.text_box,
            text="",
            bg=bg_color,
            fg=self.ENTRY_TEXT_FG,
            anchor="w",
            justify="left",
            width=self.ENTRY_TEXT_WIDTH,
        )
        bind_events(self.text_box, main_bindings)
        bind_events(self.text_label, main_bindings)

        self.description_box = editor.Frame(row=row_index, column=2, bg=bg_color, sticky="nsew")
        self.description_label = editor.Label(
            self.description_box,
            text="",
            bg=bg_color,
            fg=self.ENTRY_TEXT_FG,
            anchor="w",
            justify="left",
            width=self.ENTRY_DESCRIPTION_WIDTH,
        )
        desc_bindings = main_bindings.copy()
        desc_bindings.pop("<Shift-Button-1", None)
        desc_bindings["<Button-1>"] = lambda _, i=row_index: self.master.select_entry_row_index(
            i, description_clicked=True
        )
        bind_events(self.description_box, desc_bindings)
        bind_events(self.description_label, desc_bindings)

        self.context_menu = editor.Menu(self.row_box)

        self.tool_tip = None

    def update_entry(self, entry_id: int, entry_text: str, entry: MSBEntry = None):
        if entry is None:
            raise ValueError("`entry` required for `EnumsEditor.update_entry()` (for Maps link).")
        self.entry_id = entry_id
        self._entry_text = entry_text
        self.text_label.var.set(entry_text)
        self.description_label.var.set(entry.description if entry.description else "<No Description>")

        for entry_game_type in ENTITY_GAME_TYPES:
            supertype, subtype = entry_game_type.get_msb_entry_supertype_subtype(pluralized_subtype=True)
            if f"{supertype}: {subtype}" == self.master.active_category:
                self.maps_link = self.master.linker.soulstruct_link(entry_game_type, entry)[0]
                break

        self.build_entry_context_menu()
        self.unhide()

    def build_entry_context_menu(self):
        self.context_menu.delete(0, "end")
        if self.maps_link:
            self.maps_link.add_to_context_menu(self.context_menu)
        self.context_menu.add_command(
            label="Edit in Floating Box (Shift + Click)",
            command=lambda: self.master.popout_entry_text_edit(self.row_index),
        )
        self.context_menu.add_command(
            label="Translate Japanese Text",
            command=lambda: self.master.translate_entry_text(self.row_index),
        )

    def hide(self):
        """Called when this row has no entry to display."""
        self.row_box.grid_remove()
        if self.SHOW_ENTRY_ID:
            self.id_box.grid_remove()
            self.id_label.grid_remove()
        self.text_box.grid_remove()
        self.text_label.grid_remove()
        self.description_box.grid_remove()
        self.description_label.grid_remove()

    def unhide(self):
        self.row_box.grid()
        if self.SHOW_ENTRY_ID:
            self.id_box.grid()
            self.id_label.grid()
        self.text_box.grid()
        self.text_label.grid()
        self.description_box.grid()
        self.description_label.grid()

    @property
    def _colored_widgets(self):
        return (
            self.row_box, self.id_box, self.id_label, self.text_box, self.text_label,
            self.description_box, self.description_label
        )


class EnumsEditor(BaseEditor):
    DATA_NAME = "Maps"
    TAB_NAME = "enums"
    CATEGORY_BOX_WIDTH = 400
    ENTRY_BOX_WIDTH = 870
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 100  # More are added dynamically as needed.

    ENTRY_ROW_CLASS = EnumEntryRow
    entry_rows: list[EnumEntryRow]

    def __init__(
        self,
        project,
        enums_directory,
        global_map_choice_func,
        linker,
        master=None,
        toplevel=False,
    ):
        self.map_choice = None
        self.global_map_choice_func = global_map_choice_func
        self.enums_directory = Path(enums_directory)
        self._e_entry_description_edit = None
        super().__init__(project, linker, master=master, toplevel=toplevel, window_title="Soulstruct Map Data Editor")

    @property
    def maps(self) -> MapStudioDirectory:
        return self._project.maps

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):

            # HEADER BUTTONS
            with self.set_master(pady=10, sticky="w", row_weights=[1], column_weights=[1, 1, 1, 1], auto_columns=0):
                map_display_names = [
                    f"{game_map.msb_file_stem} [{game_map.verbose_name}]"
                    for game_map in self.maps.ALL_MAPS
                    if game_map.msb_file_stem
                ]
                self.map_choice = self.Combobox(
                    values=map_display_names,
                    label="Map:",
                    label_position="left",
                    width=55,
                    font=self.CONFIG.REGULAR_FONT,
                    on_select_function=self.on_map_choice,
                    sticky="w",
                    padx=10,
                )
                self.Button(
                    text="Import Entity IDs",
                    width=17,
                    padx=10,
                    command=lambda: self._import_enums_module(import_names=False),
                    tooltip_text="Import all entity IDs and descriptions, based on matching entity names, from an "
                    "existing Python module using Soulstruct game type enums (i.e. the format auto-generated).",
                )
                self.Button(
                    text="Import Entity Names",
                    width=20,
                    padx=10,
                    command=lambda: self._import_enums_module(import_names=True),
                    tooltip_text="Import all entity names and descriptions, based on matching entity IDs, from an "
                    "existing Python module using Soulstruct game type enums (i.e. the format auto-generated).",
                )
                self.Button(
                    text="Write Enums",
                    width=15,
                    padx=10,
                    command=self._write_enums_module,
                    tooltip_text="Create or replace the Python enums module that can be imported into "
                    "this map's EVS script. If you have changed any existing names and want to "
                    "update the names in the EVS script, make sure to restore the IDs before "
                    "regenerating this file.",
                )

            # MAIN BOXES
            with self.set_master(sticky="nsew", row_weights=[1], column_weights=[0, 1], auto_columns=0):
                self.build_category_canvas()
                with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1], auto_rows=0):
                    self.build_entry_frame()

    def select_entry_row_index(
        self,
        row_index,
        set_focus_to_text=True,
        edit_if_already_selected=True,
        id_clicked=False,
        description_clicked=False,
    ):
        """Select entry from row index, based on currently displayed category and ID range."""
        old_row_index = self.active_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected:
                    if id_clicked:
                        return self._start_entry_id_edit(row_index)
                    elif description_clicked:
                        return self._start_entry_description_edit(row_index)
                    else:
                        return self._start_entry_text_edit(row_index)
                return
        else:
            self._cancel_entry_id_edit()
            self._cancel_entry_text_edit()

        self.active_row_index = row_index

        if old_row_index is not None:
            self.entry_rows[old_row_index].active = False
        if row_index is not None:
            self.entry_rows[row_index].active = True
            if set_focus_to_text:
                self.entry_rows[row_index].text_label.focus_set()

    def refresh_entries(self):
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range() if self.active_category else []

        row = 0
        for entry_id, entry in entries_to_display:
            try:
                self.entry_rows[row].update_entry(entry_id, entry.name, entry)
            except IndexError:
                # Create new rows as needed.
                with self.set_master(self.entry_i_frame):
                    self.entry_rows.append(
                        self.ENTRY_ROW_CLASS(
                            self,
                            row_index=row,
                            main_bindings={
                                "<Button-1>": lambda _, i=row: self.select_entry_row_index(i),
                                "<Shift-Button-1>": lambda e, i=row: self.popout_entry_text_edit(i),
                                "<Button-3>": lambda e, i=row: self._right_click_entry(e, i),
                                "<Up>": self._entry_press_up,
                                "<Down>": self._entry_press_down,
                                "<Prior>": lambda e: self._go_to_previous_entry_range(),
                                "<Next>": lambda e: self._go_to_next_entry_range(),
                            },
                        )
                    )
                self.entry_rows[row].update_entry(entry_id, entry.name, entry)
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, len(self.entry_rows)):
            self.entry_rows[remaining_row].hide()

        self.entry_i_frame.columnconfigure(0, weight=1)
        self.entry_i_frame.columnconfigure(1, weight=1)
        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_range_buttons()

    def _start_entry_description_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit and not self._e_entry_description_edit:
            entry_id = self.get_entry_id(row_index)
            initial_desc = self.get_entry_description(entry_id)
            self._e_entry_description_edit = self.Entry(
                self.entry_rows[row_index].description_box, initial_text=initial_desc, sticky="ew", width=5
            )
            self._e_entry_description_edit.bind(
                "<Return>", lambda e, i=row_index: self._confirm_entry_description_edit(i)
            )
            self._e_entry_description_edit.bind("<Up>", self._entry_press_up)  # confirms edit
            self._e_entry_description_edit.bind("<Down>", self._entry_press_down)  # confirms edit
            self._e_entry_description_edit.bind(
                "<FocusOut>", lambda e, i=row_index: self._confirm_entry_description_edit(i)
            )
            self._e_entry_description_edit.bind("<Escape>", lambda e: self._cancel_entry_description_edit())
            self._e_entry_description_edit.focus_set()
            self._e_entry_description_edit.select_range(0, "end")

    def _cancel_entry_description_edit(self):
        if self._e_entry_description_edit:
            self._e_entry_description_edit.destroy()
            self._e_entry_description_edit = None

    def _confirm_entry_description_edit(self, row_index):
        if self._e_entry_description_edit:
            new_description = self._e_entry_description_edit.var.get()
            self._change_entry_description(row_index, new_description)
            self._cancel_entry_description_edit()

    def _change_entry_description(self, row_index, new_description, category=None):
        """Set text of given entry index in the displayed category (if different from current)."""
        if category is None:
            category = self.active_category
        entry_id = self.get_entry_id(row_index)
        current_desc = self.get_entry_description(entry_id, category=category)
        if current_desc == new_description:
            return False  # Nothing to change.
        self._set_entry_description(entry_id, new_description, category=category, update_row_index=row_index)
        return True

    def _entry_press_up(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            edit_new_description = self._e_entry_description_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._confirm_entry_description_edit(self.active_row_index)
            self._shift_selected_entry(-1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            elif edit_new_description:
                self._start_entry_description_edit(self.active_row_index)
            if self.entry_canvas.yview()[1] != 1.0 or self.active_row_index < self.displayed_entry_count - 5:
                self.entry_canvas.yview_scroll(-1, "units")

    def _entry_press_down(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            edit_new_description = self._e_entry_description_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._confirm_entry_description_edit(self.active_row_index)
            self._shift_selected_entry(+1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            elif edit_new_description:
                self._start_entry_description_edit(self.active_row_index)
            if self.entry_canvas.yview()[0] != 0.0 or self.active_row_index > 5:
                self.entry_canvas.yview_scroll(1, "units")

    def on_map_choice(self, event=None):
        if self.global_map_choice_func and event is not None:
            self.global_map_choice_func(self.map_choice_stem, ignore_tabs=("enums",))
        self.select_entry_row_index(None)
        self.refresh_entries()

    def _get_map(self) -> Map:
        return self.maps.GET_MAP(self.map_choice_stem)

    def _import_enums_module(self, import_names=False):
        """Reads '{map_id}_enums.py' file and updates either:
            - entry ENTITY IDs based on matching entity names, if `import_names=False` (default)
            - entry NAMES based on matching entity IDs, if `import_names=True`

        Either way, also tries to read descriptions from inline comments with regex. (Messing too much with unusual
        formatting in the module file may interfere with this.)
        """
        game_map = self.maps.GET_MAP(self.map_choice_stem)
        module_path = self.enums_directory / f"{game_map.emevd_file_stem}_enums.py"
        if not module_path.is_file():
            return self.error_dialog("No Entity Module", "Entity module not yet created in project 'events' folder.")
        evs_path = self.enums_directory / f"{game_map.emevd_file_stem}.evs.py"
        if not evs_path.is_file():
            return self.error_dialog("No EVS Script", "EVS script not yet imported into project 'events' folder.")
        sys.path.append(str(module_path.parent))

        try:
            entity_module = import_arbitrary_file(module_path)
        except Exception as ex:
            return self.error_dialog("Import Error", f"Could not import {module_path.name}. Error:\n\n{str(ex)}")

        if import_names:
            self._update_names_from_import(entity_module, module_path)
        else:
            self._update_entity_ids_from_import(entity_module, module_path)

    def _update_names_from_import(self, entity_module: tp.Union[str, Path, types.ModuleType], module_path: Path):
        if isinstance(entity_module, (str, Path)):
            try:
                entity_module = import_arbitrary_file(module_path)
            except Exception as ex:
                return self.error_dialog("Import Error", f"Could not import {module_path.name}. Error:\n\n{str(ex)}")

        msb = self.get_selected_msb()
        entries_by_entity_enum = {}
        found_map_entry_class_names = []

        not_found = []  # type: list[int]
        for attr_name, attr in [
            m[0:2]
            for m in inspect.getmembers(entity_module, inspect.isclass)
            if m[1].__module__ == entity_module.__name__  # ignore nested imports
        ]:
            for entry_game_type in ENTITY_GAME_TYPES:
                if entry_game_type in attr.__bases__:
                    break
            else:
                continue  # ignore this class
            found_map_entry_class_names.append(attr_name)
            for entity_enum in attr:
                try:
                    entry = msb.find_entry_by_entity_id(entity_enum.value, allow_multiple=False)
                except ValueError:
                    return self.error_dialog(
                        "Duplicate Entity IDs",
                        f"MSB contains multiple entries with entity ID {entity_enum.value}. Cannot import names from "
                        f"enums module until this is fixed.",
                    )
                except KeyError:
                    not_found.append(entity_enum.value)
                    continue
                entry_type_name = entry.SUBTYPE_ENUM.get_plural_supertype_name()
                entry_subtype_name = entry.SUBTYPE_ENUM.name
                if entry_game_type.get_msb_entry_supertype_subtype() != (entry_type_name, entry_subtype_name):
                    return self.error_dialog(
                        "Entity Type Mismatch",
                        f"Entity ID {entity_enum.value} in Python module '{module_path.stem}' has type "
                        f"'{attr_name}', but has different type '{entry_type_name}.{entry_subtype_name} in MSB. Cannot "
                        f"import names from enums module until this is fixed.",
                    )
                entries_by_entity_enum[entity_enum] = entry

        if not entries_by_entity_enum:
            return self.CustomDialog(
                "No IDs to Update",
                "No IDs in the imported enums module are present in the MSB.",
            )

        if not_found:
            not_found_string = word_wrap(", ".join(str(i) for i in not_found), 50)
            if (
                self.CustomDialog(
                    title="Allow Missing IDs?",
                    message=f"These entity IDs in the Python module could not be found in the MSB:"
                    f"\n\n{not_found_string}"
                    f"\n\nContinue updating names of {len(entries_by_entity_enum)} other entries?",
                    button_kwargs=("YES", "NO"),
                    button_names=("Yes, continue", "No, abort import"),
                    default_output=0,
                    cancel_output=1,
                )
                == 1
            ):
                return

        # Find descriptions with regular expressions.
        current_attr_name = ""
        descriptions_by_attr_and_id = {}
        with module_path.open("r", encoding="utf-8") as module:
            for line in module:
                class_match = _RE_ENUM_CLASS.match(line)
                if class_match:
                    attr_name = class_match.group(1)
                    if attr_name in found_map_entry_class_names:
                        current_attr_name = attr_name
                    continue
                if current_attr_name:
                    member_match = _RE_ENUM_MEMBER.match(line)
                    if member_match:
                        entity_id, description = member_match.group(2, 3)
                        if entity_id not in not_found:
                            descriptions_by_attr_and_id[current_attr_name, int(entity_id)] = description.strip()

        for entity_enum, entry in entries_by_entity_enum.items():
            entry.name = entity_enum.name
        for (attr_name, entity_id), description in descriptions_by_attr_and_id.items():
            # attr_name not actually used, as entity ID uniqueness should have already been resolved
            try:
                entry = msb.find_entry_by_entity_id(entity_id, allow_multiple=False)
            except KeyError:
                continue  # shouldn't happen (as missing entity ID should be skipped) but just in case
            entry.description = description

        self.refresh_entries()

        self.CustomDialog("Import Successful", "Entity names and descriptions imported successfully.")

    def _update_entity_ids_from_import(self, entity_module: types.ModuleType, module_path: Path):

        msb = self.get_selected_msb()
        entries_by_entity_enum = {}
        found_map_entry_class_names = []

        not_found = []  # type: list[str]
        for attr_name, attr in [
            m[0:2]
            for m in inspect.getmembers(entity_module, inspect.isclass)
            if m[1].__module__ == entity_module.__name__  # ignore nested imports
        ]:
            for entry_game_type in ENTITY_GAME_TYPES:
                if entry_game_type in attr.__bases__:
                    break  # found matching type
            else:
                if RegionVolume in attr.__bases__:  # if unique, Volume enums are valid as Boxes/Spheres/Cylinders
                    entry_game_type = RegionVolume
                else:
                    continue  # ignore this class
            found_map_entry_class_names.append(attr_name)
            for entity_enum in attr:
                try:
                    entry = msb.find_entry_by_entity_id(entity_enum.name, allow_multiple=False)
                except ValueError:
                    return self.error_dialog(
                        "Duplicate Entity Names",
                        f"MSB contains multiple entries with name {entity_enum.name}. Cannot import entity IDs from "
                        f"enums module until this is fixed.",
                    )
                except KeyError:
                    not_found.append(entity_enum.name)
                    continue
                supertype_name = entry.SUBTYPE_ENUM.get_plural_supertype_name()
                entry_subtype_name = entry.SUBTYPE_ENUM.name
                if entry_game_type is RegionVolume:
                    if supertype_name != "Regions" or entry_subtype_name not in {"Sphere", "Cylinder", "Box"}:
                        return self.error_dialog(
                            "Entity Type Mismatch",
                            f"Entity name {entity_enum.name} in Python module '{module_path.stem}' has type "
                            f"`RegionVolume`, but is not a Sphere, Cylinder, or Box in the MSB. Cannot "
                            f"import entity IDs from enums module until this is fixed.",
                        )
                    entries_by_entity_enum[entity_enum] = entry
                elif entry_game_type.get_msb_entry_supertype_subtype() != (supertype_name, entry_subtype_name):
                    return self.error_dialog(
                        "Entity Type Mismatch",
                        f"Entity name {entity_enum.name} in Python module '{module_path.stem}' has type "
                        f"`{attr_name}`, but has different type '{supertype_name}.{entry_subtype_name}` in MSB. "
                        f"Cannot import entity IDs from enums module until this is fixed.",
                    )
                entries_by_entity_enum[entity_enum] = entry

        if not entries_by_entity_enum:
            return self.CustomDialog(
                "No Names to Update",
                "No names in the imported enums module are present in the MSB.",
            )

        if not_found:
            not_found_string = word_wrap(", ".join(not_found), 50)
            if (
                self.CustomDialog(
                    title="Allow Missing Names?",
                    message=f"These entity names in the Python module could not be found in the MSB:"
                            f"\n\n{not_found_string}"
                            f"\n\nContinue updating entity IDs of {len(entries_by_entity_enum)} other entries?",
                    button_kwargs=("YES", "NO"),
                    button_names=("Yes, continue", "No, abort import"),
                    default_output=0,
                    cancel_output=1,
                )
                == 1
            ):
                return

        # Find descriptions with regular expressions.
        current_attr_name = ""
        descriptions_by_attr_and_id = {}
        with module_path.open("r", encoding="utf-8") as module:
            for line in module:
                class_match = _RE_ENUM_CLASS.match(line)
                if class_match:
                    attr_name = class_match.group(1)
                    if attr_name in found_map_entry_class_names:
                        current_attr_name = attr_name
                    continue
                if current_attr_name:
                    member_match = _RE_ENUM_MEMBER.match(line)
                    if member_match:
                        name, description = member_match.group(1, 3)
                        if name not in not_found:
                            descriptions_by_attr_and_id[current_attr_name, name] = description.strip()

        for entity_enum, entry in entries_by_entity_enum.items():
            entry.entity_id = entity_enum.value
        for (attr_name, name), description in descriptions_by_attr_and_id.items():
            # attr_name not actually used, as name uniqueness should have already been resolved
            try:
                entry = msb.find_entry_name(name)
            except KeyError:
                continue  # shouldn't happen (as missing entity ID should be skipped) but just in case
            entry.description = description

        self.refresh_entries()

        self.CustomDialog("Import Successful", "Entity IDs and descriptions imported successfully.")

    def _write_enums_module(self):
        """Generates a '{mXX_YY}_enums.py' file with entity IDs for import into EVS script."""
        game_map = self._get_map()
        module_path = self.enums_directory / f"{game_map.emevd_file_stem}_enums.py"

        msb = self.get_selected_msb()
        try:
            msb.write_entities_module(module_path, area_id=game_map.area_id, block_id=game_map.block_id)
        except Exception as ex:
            self.CustomDialog(
                "Write Failed", f"An error occurred while writing '{{project}}/events/{module_path.name}':\n{ex}"
            )
        else:
            self.CustomDialog(
                "Write Successful", f"'{{project}}/events/{module_path.name}'\ncreated or overwritten successfully."
            )

    @staticmethod
    def _get_category_text_fg(category: str):
        return ENTRY_LIST_FG_COLORS.get(category.split(":")[0], "#FFF")

    def _get_display_categories(self):
        """ALl combinations of MSB entry list names (except Model) and their subtypes, properly formatted."""
        categories = []
        for entry_game_type in ENTITY_GAME_TYPES:
            supertype, subtype = entry_game_type.get_msb_entry_supertype_subtype(pluralized_subtype=True)
            categories.append(f"{supertype}: {subtype}")
        return categories

    def get_selected_msb(self) -> MSB:
        map_name = self.maps.GET_MAP(self.map_choice_stem).name
        return self.maps[map_name]

    def _get_category_subtype_list(self, category: str = None) -> MSBEntryList:
        """Get the selected category's subtype name and return its `MSB` entry list."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot get MSB subtype entry list without `category` if `active_category` is None.")
        try:
            supertype_name, subtype_name = self.active_category.split(": ")
        except ValueError:
            raise ValueError(f"MSB category name was not in '[supertype]: [subtype]' format: {self.active_category}")
        return self.get_selected_msb()[subtype_name]

    def get_category_data(self, category=None) -> dict[int, MSBEntry]:
        """Gets entry data from map choice, entry list choice, and entry type choice (active category).

        Entity dictionary is generated from `MSB.get_entity_id_dict()` every time and is sorted by entity ID.
        """
        subtype_list = self._get_category_subtype_list(category)
        return subtype_list.get_entity_id_dict(sort_by_entity_id=True)

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns entire dictionary (no previous/next range buttons here)."""
        return list(self.get_category_data(category).items())

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Returns index of given entry ID (entity ID) in dictionary keys."""
        return list(self.get_category_data(category)).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_id].name

    def get_entry_description(self, entry_id: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_id].description

    def _set_entry_text(self, entry_index: int, text: str, category=None, update_row_index=None):
        entry_list = self.get_category_data(category)
        entry = entry_list[entry_index]
        entry.name = text  # Will update Maps tab as well (once refreshed).
        self.linker.window.maps_tab.refresh_entries()
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_index, text, entry)

    def _set_entry_description(self, entry_index: int, description: str, category=None, update_row_index=None):
        entry_list = self.get_category_data(category)
        entry = entry_list[entry_index]
        entry.description = description  # Will update Maps tab tooltip as well.
        entry_text = self.entry_rows[update_row_index].entry_text  # keep same text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_index, entry_text, entry)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Changes 'entity_id' field of MSB entry."""
        entry_list = self.get_category_data(category)
        entry_list[entry_id].set_entity_id(new_id)
        self.linker.window.maps_tab.refresh_entries()
        entry_list[new_id] = entry = entry_list.pop(entry_id)
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(new_id, entry.name, entry)
        return True
