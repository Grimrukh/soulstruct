from __future__ import annotations

__all__ = ["MapsEditor"]

import logging
import math
import typing as tp

from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.base.game_types import BaseGameObject, GameObjectSequence
from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.base.maps.msb.enums import BaseMSBModelSubtype, BaseMSBRegionSubtype
from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.base.project.utilities import (
    bind_events,
    NameSelectionBox,
    EntryTextEditBox,
    SequenceNameEditBox,
    GroupBitSetEditBox,
)
from soulstruct.base.project.editors.base_editor import EntryRow
from soulstruct.base.project.editors.field_editor import BaseFieldEditor, FieldRow
from soulstruct.utilities.conversion import int_group_to_bit_set
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.memory import MemoryHookCallError

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.map_studio_directory import MapStudioDirectory
    from soulstruct.base.maps.msb import MSB, MSBEntryList, MSBEntry

_LOGGER = logging.getLogger(__name__)

# TODO: Models are handled automatically. Model entries are auto-generated from all used model names.
#  - Validation is done by checking the model files for that map (only need to inspect the names inside the BND).
#  - Validation/SIB path depends on game version.

ENTRY_LIST_FG_COLORS = {
    "Parts": "#DDF",
    "Regions": "#FDD",
    "Events": "#DFD",
    "Models": "#FFC",
}


class MapEntryRow(EntryRow):
    """Entry rows for Maps have no ID (`entry_id` is a list index in that MSB category).

    They also display their Entity ID field if they have a non-default value.
    """

    master: MapsEditor

    ENTRY_ID_WIDTH = 5
    EDIT_ENTRY_ID = False

    def __init__(self, editor: MapsEditor, row_index: int, main_bindings: dict = None):
        super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

    def update_entry(self, entry_index: int, entry_text: str, entry_description: str = ""):
        self.entry_id = entry_index
        entry_data = self.master.get_category_data()[entry_index]
        if hasattr(entry_data, "entity_id"):
            text_tail = f"  {{ID: {entry_data.entity_id}}}" if entry_data.entity_id not in {-1, 0} else ""
        elif isinstance(entry_data, BaseMSBModel) and entry_data.SUBTYPE_ENUM.name in {"Character", "Player"}:
            try:
                model_id = int(entry_text.lstrip("c"))
            except ValueError:
                text_tail = ""
            else:
                try:
                    text_tail = f"  {{{self.master.character_models[model_id]}}}"
                except KeyError:
                    text_tail = "  {UNKNOWN}"
        else:
            text_tail = ""

        if entry_description:
            self.tool_tip.text = entry_description
        else:
            self.tool_tip.text = None
        self._entry_text = entry_text
        self.text_label.var.set(entry_text + text_tail)
        self.build_entry_context_menu()
        self.unhide()

    def build_entry_context_menu(self):
        self.context_menu.delete(0, "end")
        self.context_menu.add_command(
            label="Edit in Floating Box (Shift + Click)",
            command=lambda: self.master.popout_entry_text_edit(self.row_index),
        )
        self.context_menu.add_command(
            label="Translate Japanese Text",
            command=lambda: self.master.translate_entry_text(self.row_index),
        )
        self.context_menu.add_command(
            label="Duplicate Entry to Next Index",
            command=lambda: self.master.add_relative_entry(self.entry_id),
        )
        msb_type, msb_subtype = self.master.active_category.split(": ")
        if msb_type == "Regions" or (msb_type == "Parts" and msb_subtype in {"Characters", "Objects", "PlayerStarts"}):
            copy_fields = ("translate", "rotate")
            if msb_subtype in {"Characters", "Objects"}:
                copy_fields += ("draw_parent_name",)
        self.context_menu.add_command(
            label="Duplicate Entry to Next Index + Copy Player Transform",
            command=lambda: self.master.add_relative_entry_and_copy_player_transform(
                self.entry_id, **{f: True for f in copy_fields}
            ),
        )
        self.context_menu.add_command(
            label="Create New Entry at Next Index",
            command=lambda: self.master.add_new_default_entry(self.entry_id + 1),
        )
        self.context_menu.add_command(
            label="Create New Entry at Last Index",
            command=lambda: self.master.add_new_default_entry(),
        )
        self.context_menu.add_command(
            label="Delete Entry",
            command=lambda: self.master.delete_entry(self.row_index),
        )

        # For converting to Python scripting.
        self.context_menu.add_command(
            label="Copy as Python Instance",
            command=lambda: self.master.copy_python_instance_text(self.row_index),
        )


class MapFieldRow(FieldRow):

    CAMEL_CASE_NICKNAMES = False  # field nicknames already properly formatted for display

    master: MapsEditor

    def __init__(self, editor: MapsEditor, row_index: int, main_bindings: dict = None):
        super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

        bg_color = self._get_color()

        self.value_vector_frame = editor.Frame(
            self.value_box,
            bg=bg_color,
            width=editor.FIELD_VALUE_WIDTH,
            height=editor.FIELD_ROW_HEIGHT,
            no_grid=True,
        )
        bind_events(self.value_vector_frame, main_bindings)
        self.value_vector_x = editor.Label(
            self.value_vector_frame, text="", bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6, column=0, anchor="w"
        )
        self.value_vector_y = editor.Label(
            self.value_vector_frame, text="", bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6, column=1, anchor="w"
        )
        self.value_vector_z = editor.Label(
            self.value_vector_frame, text="", bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6, column=2, anchor="w"
        )

        for coord, label in zip("xyz", (self.value_vector_x, self.value_vector_y, self.value_vector_z)):
            vector_bindings = main_bindings.copy()
            vector_bindings.update(
                {"<Button-1>": lambda _, c=coord: editor.select_displayed_field_row(row_index, coord=c)}
            )
            bind_events(label, vector_bindings)

        self.unhide()

    def update_field_value_display(self, new_value):
        """Updates field value and display/option properties related to it."""
        if issubclass(self.field_type, Vector3) and self.master.e_coord is not None:
            # A single coordinate is being edited.
            self._set_linked_value_label(f"{self.master.e_coord}: {new_value:.3f}")
        else:
            try:
                self.field_update_method(new_value)
            except TypeError:
                raise TypeError(
                    f"Could not update field {self.field_name} (type {self.field_type}) with value {new_value}."
                )
        self._set_field_fg(new_value)
        self.link_missing = self.field_links and not any(link.name for link in self.field_links)
        self.build_field_context_menu()

    def _update_field_GameObject(self, value):
        """Adds any recognized `GameObject` names as hints."""
        try:
            self.field_links = self.master.get_field_links(self.field_type, value)
        except ValueError:
            _LOGGER.warning(
                f"Could not generate link for value {repr(value)} of field '{self.field_name}'.\n"
                f"Value type does not match expected field type ({self.field_type})."
            )
            self.value_label.var.set(str(value) + "  {LINK ERROR}")
            self._activate_value_widget(self.value_label)

        if issubclass(self.field_type, MapEntry):
            # `value` is the name of another MSB entry, or an empty string to reset to `None`.
            if not value:
                self.value_label.var.set("None")
            else:
                msb_entry_name = str(value)
                if self.field_type == CharacterModel:
                    # Auto-display DS1 character model names for convenience.
                    if self.field_links[0].name is None:
                        msb_entry_name += "  {BROKEN LINK}"
                    else:
                        model_id = int(msb_entry_name[1:])  # ignore 'c' prefix
                        try:
                            msb_entry_name += f"  {{{self.master.character_models[model_id]}}}"
                        except KeyError:
                            msb_entry_name += "  {UNKNOWN}"
                self.value_label.var.set(msb_entry_name)
            self._activate_value_widget(self.value_label)
            return

        self._update_field_int(value)

    def _update_field_Vector3(self, value: Vector3):
        """Update field with a `Vector3` value. (No chance of a link.)"""
        self.value_vector_x.var.set(f"x: {value.x:.3f}")
        self.value_vector_y.var.set(f"y: {value.y:.3f}")
        self.value_vector_z.var.set(f"z: {value.z:.3f}")
        self._activate_value_widget(self.value_vector_frame)

    def _update_field_Map(self, value: Map):
        """Update field with a valid 'Map' specification. (No chance of a link.)

        Note that the basic EMEVD-style map string is displayed, rather than the vanilla map name, as the original names
        may not make sense in your project.
        """
        self.value_label.var.set(value.emevd_file_stem)
        self._activate_value_widget(self.value_label)

    def _set_linked_value_label(self, value_text, multiple_hint="{AMBIGUOUS}"):
        if self.master.e_coord is not None:
            coord_label = getattr(self, f"value_vector_{self.master.e_coord}")
            coord_label.var.set(value_text)
            self._activate_value_widget(self.value_vector_frame)
            return

        if self.field_links:
            if len(self.field_links) > 1:
                value_text += f"    {multiple_hint}"
            if any(link.name is None for link in self.field_links):
                value_text += "    {BROKEN LINK}"
            else:
                value_text += f"    {{{self.field_links[0].name}}}"
        if self.value_label.var.get() != value_text:
            self.value_label.var.set(value_text)  # TODO: probably redundant in terms of update efficiency
        self._activate_value_widget(self.value_label)

    def _add_copy_option(self, menu, translate=False, rotate=False, draw_parent_name=False, y_offset=0.0):
        text = []
        if translate:
            text.append(f"translate ({y_offset} Y)" if y_offset != 0.0 else "translate")
        if rotate:
            text.append("rotate")
        if draw_parent_name:
            text.append("draw parent")
        label = f"Copy player {' + '.join(text)}"
        menu.add_command(
            label=label,
            command=lambda: self.master.copy_player_position(
                translate=translate, rotate=rotate, draw_parent_name=draw_parent_name, y_offset=y_offset,
            )
        )

    def build_field_context_menu(self):
        """For linked fields, adds an option to select an entry name from the linked table."""
        self.context_menu.delete(0, "end")
        if issubclass(self.field_type, BaseGameObject):
            for field_link in self.field_links:
                field_link.add_to_context_menu(self.context_menu)
            if issubclass(self.field_type, MapEntry):
                self.context_menu.add_command(
                    label="Select linked entry name from list", command=self.choose_linked_map_entry
                )
            if self.field_type == CharacterModel:
                self.context_menu.add_command(
                    label="Select model from complete list", command=self.choose_character_model
                )

        # Users can open a dialog of checkbuttons.
        if self.field_type == list and self.field_name.endswith("_groups"):
            self.context_menu.add_command(label="Show checkbuttons", command=self._set_group_checkbuttons)

        msb_type, msb_subtype = self.master.active_category.split(": ")
        if msb_type == "Regions" or msb_subtype in {"Characters", "Objects", "PlayerStarts"}:
            copy_fields = ("translate", "rotate")
            if msb_subtype in {"Characters", "Objects"}:
                copy_fields += ("draw_parent_name",)
            if self.field_name in copy_fields:
                copy_menu = self.master.Menu(tearoff=0)
                if len(copy_fields) == 3:
                    # Triple option.
                    kwargs = {f: True for f in copy_fields}
                    self._add_copy_option(copy_menu, **kwargs)
                    if self.master.active_category.endswith("Boxes"):
                        self._add_copy_option(copy_menu, **kwargs, y_offset=-0.1)
                if len(copy_fields) >= 2:
                    # Double options (iterate over OTHER copy fields).
                    for copy_field in (f for f in copy_fields if f != self.field_name):
                        kwargs = {f: f in {self.field_name, copy_field} for f in copy_fields}
                        self._add_copy_option(copy_menu, **kwargs)
                        if kwargs.get("translate", False) and self.master.active_category.endswith("Boxes"):
                            self._add_copy_option(copy_menu, **kwargs, y_offset=-0.1)
                # Single option (this field only).
                kwargs = {self.field_name: True}
                self._add_copy_option(copy_menu, **kwargs)
                if self.field_name == "translate" and self.master.active_category.endswith("Boxes"):
                    self._add_copy_option(copy_menu, **kwargs, y_offset=-0.1)
                self.context_menu.add_cascade(label="Copy from hook...", foreground="#FFF", menu=copy_menu)

        if issubclass(self.field_type, GameObjectSequence):
            self.context_menu.add_command(
                label=f"Edit sequence names in popout box",
                command=lambda: self.master.popout_sequence_name_edit(
                    self.field_name, self.field_nickname, self.field_type.game_object_type
                ),
            )
            if self.field_type.game_object_type is Region:
                # Option to add a point to a list of Points, based on current player translate/rotate.
                # NOTE: Assumes that Points are sufficient, which I think is true for all sequence fields I've seen.
                self.context_menu.add_command(
                    label=f"Add new Point from player translate + rotate",
                    command=lambda: self.master.add_point_from_player_position(self.field_name, self.field_nickname),
                )

    def choose_linked_map_entry(self):
        if not issubclass(self.field_type, MapEntry):
            return  # option shouldn't even appear
        names = self.master.linker.get_map_entry_type_names(self.field_type)  # adds suffix for Characters
        selected_name = NameSelectionBox(self.master, names).go()
        if selected_name is not None:
            selected_name = selected_name.split("  {")[0]  # remove suffix
            self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
            if not self.field_links[0].name:
                display_name = selected_name + "  {BROKEN LINK}"
                self.link_missing = True
                self.master.CustomDialog(
                    title="Map Link Error",
                    message="Map link was broken after selecting map entry from list. This should not happen; "
                    "please try restarting Soulstruct, and inform Grimrukh if the problem persists.",
                )
            else:
                if self.field_type in (CharacterModel, PlayerModel):
                    model_id = int(selected_name[1:])  # ignore 'c' prefix
                    try:
                        display_name = selected_name + f"  {{{self.master.character_models[model_id]}}}"
                    except KeyError:
                        display_name = selected_name + "  {UNKNOWN}"
                else:
                    display_name = selected_name
                self.link_missing = False

            self.master.change_field_value(self.field_name, selected_name)
            self.value_label.var.set(display_name)
            self.build_field_context_menu()

    def choose_character_model(self):
        if not issubclass(self.field_type, CharacterModel):
            return  # option shouldn't even appear
        names = [f"c{model_id:04d}  {{{model_name}}}" for model_id, model_name in self.master.character_models.items()]
        selected_name = NameSelectionBox(self.master, names).go()
        if selected_name is not None:
            selected_name = selected_name.split("  {")[0]  # remove suffix
            self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
            if not self.field_links[0].name:
                self.master.add_models(self.field_type, selected_name)
                self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
            if self.field_links[0].name:
                model_id = int(selected_name[1:])  # ignore 'c' prefix
                try:
                    display_name = selected_name + f"  {{{self.master.character_models[model_id]}}}"
                except KeyError:
                    display_name = selected_name + "  {UNKNOWN}"
                if self.link_missing:
                    self.link_missing = False
                    self._update_colors()
            else:
                display_name = selected_name + "  {BROKEN LINK}"
                if not self.link_missing:
                    self.link_missing = True
                    self._update_colors()

            self.master.change_field_value(self.field_name, selected_name)
            self.value_label.var.set(display_name)
            self.build_field_context_menu()

    def _set_group_checkbuttons(self):
        new_bit_set = GroupBitSetEditBox(
            self.master,
            initial_bit_set=self.master.get_selected_field_dict()[self.field_name],
            window_title=f"Modify {self.field_nickname}",
        ).go()
        if new_bit_set is None:
            return
        field_changed = self.master.change_field_value(self.field_name, new_bit_set)
        if field_changed:
            self.update_field_value_display(new_bit_set)

    @property
    def editable(self):
        return id(self.active_value_widget) in {id(self.value_label), id(self.value_vector_frame)}

    def _string_to_Vector3(self, string):
        return self._string_to_float(string)

    def _string_to_Map(self, string):
        try:
            return self.master.maps.GET_MAP(string)
        except (KeyError, ValueError):
            raise InvalidFieldValueError(
                f"Could not interpret input as a Map specifier for field {self.field_nickname}. Try a string like "
                f"'m10_02_00_00'."
            )

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (
            self.row_box,
            self.field_name_box,
            self.field_name_label,
            self.value_box,
            self.value_label,
            self.value_vector_frame,
            self.value_vector_x,
            self.value_vector_y,
            self.value_vector_z,
            self.value_checkbutton,
        ):
            widget["bg"] = bg_color


class MapsEditor(BaseFieldEditor):
    DATA_NAME = "Maps"
    TAB_NAME = "maps"
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 42  # highest count found so far (Parts.Collisions in Bloodborne)
    FIELD_NAME_WIDTH = 20
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 60

    ENTRY_ROW_CLASS = MapEntryRow
    FIELD_ROW_CLASS = MapFieldRow

    entry_rows: list[MapEntryRow]
    field_rows: list[MapFieldRow]

    def __init__(
        self,
        project,
        global_map_choice_func,
        linker,
        master=None,
        toplevel=False,
        character_models: dict[int, str] = None,
    ):
        self.global_map_choice_func = global_map_choice_func
        self.character_models = {} if character_models is None else character_models
        self.e_coord = None
        self.map_choice = None
        self.entry_canvas_context_menu = None
        super().__init__(project, linker, master=master, toplevel=toplevel, window_title="Soulstruct Map Data Editor")

    @property
    def maps(self) -> MapStudioDirectory:
        return self._project.maps

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):
            with self.set_master(pady=10, sticky="w", row_weights=[1], column_weights=[1], auto_columns=0):
                map_display_names = [
                    f"{game_map.msb_file_stem} [{game_map.verbose_name}]"
                    for game_map in self.maps.ALL_MAPS
                    if game_map.msb_file_stem
                ]
                self.map_choice = self.Combobox(
                    values=map_display_names,
                    label="Map:",
                    label_font_size=12,
                    label_position="left",
                    width=35,
                    font=("Segoe UI", 12),
                    on_select_function=self.on_map_choice,
                    sticky="w",
                    padx=10,
                )

            super().build()

        self.entry_canvas_context_menu = self.Menu(self.entry_canvas)
        self.entry_canvas_context_menu.add_command(label="Create New Entry", command=self.add_new_default_entry)
        self.entry_canvas.bind("<Button-3>", self.right_click_entry_canvas)

    def check_for_repeated_entity_ids(self):
        # Check for duplicate entity IDs.
        repeat_warning = ""
        for map_name, msb in self.maps.items():
            repeats = msb.get_repeated_entity_ids()
            if repeats["Regions"]:
                regions = "\n".join(f"{e.entity_id}: {e.name}" for e in repeats["Regions"])
                region_ids = ", ".join(str(e.entity_id) for e in repeats["Regions"])
                repeat_warning += f"{map_name}:\n{regions}\n"
                _LOGGER.warning(f"Found repeated region entity IDs in {map_name}: {region_ids}")
        if repeat_warning:
            self.CustomDialog(
                "Repeated Region Entity IDs Found",
                "Found repeated region entity IDs in map files.\n"
                "Any regions that appear after these in the map\n"
                "will not function properly in event scripts.\n"
                "(If you're seeing four IDs in the Duke's Archives,\n"
                "this is indeed a vanilla bug - you can just delete\n"
                "the offending four repeated regions, as they are\n"
                "not used.)\n\n" + repeat_warning,
            )

    def right_click_entry_canvas(self, event):
        if self.active_category is not None:
            self.entry_canvas_context_menu.tk_popup(event.x_root, event.y_root)

    def refresh_entries(self, reset_field_display=False):
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range(
            first_index=self.first_display_index, last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id, _ in entries_to_display:
            self.entry_rows[row].update_entry(
                entry_id, self.get_entry_text(entry_id), self.get_entry_description(entry_id)
            )
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

        self.refresh_fields(reset_display=reset_field_display)

    def on_map_choice(self, event=None):
        if self.global_map_choice_func and event is not None:
            self.global_map_choice_func(self.map_choice_stem, ignore_tabs=("maps",))
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    @staticmethod
    def _get_category_text_fg(category: str):
        return ENTRY_LIST_FG_COLORS.get(category.split(":")[0], "#FFF")

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

    def _add_entry(self, subtype_index: int, text: str, category=None, new_field_dict: MSBEntry = None):
        """Active category is required."""
        subtype_list = self._get_category_subtype_list(category)
        self._cancel_entry_text_edit()
        new_field_dict.name = text
        subtype_list.insert(subtype_index, new_field_dict)
        self.select_entry_id(subtype_index, set_focus_to_text=True, edit_if_already_selected=False)
        # TODO: ActionHistory stuff?
        return True

    def add_relative_entry(self, subtype_index: int, offset=1, text=None):
        """Duplicate entry at `subtype_index` to index `subtype_index + offset`."""
        subtype_list = self._get_category_subtype_list()
        source_msb_entry = subtype_list[subtype_index]
        msb_entry = source_msb_entry.copy()
        msb_entry.name = text if text is None else source_msb_entry.name + " <COPY>"
        return self._add_entry(subtype_index + offset, text=msb_entry.name, new_field_dict=msb_entry)

    def add_relative_entry_and_copy_player_transform(
        self, entry_index, translate=False, rotate=False, draw_parent_name=False
    ):
        self.add_relative_entry(entry_index)
        # Duplicated entry is selected, so we can apply player transform now.
        self.copy_player_position(translate=translate, rotate=rotate, draw_parent_name=draw_parent_name)

    def add_new_default_entry(self, entry_index=-1):
        """Add a new `MSBEntry` instance of the appropriate subtype to the end of the list, with all default values."""
        subtype_list = self._get_category_subtype_list()
        msb_entry = subtype_list.default_entry()
        return self._add_entry(entry_index, text=msb_entry.name, new_field_dict=msb_entry)

    def delete_entry(self, row_index: int, category=None) -> MSBEntry | None:
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        if row_index is None:
            self.bell()
            return

        subtype_list = self._get_category_subtype_list(category)
        self._cancel_entry_text_edit()
        # Row index and subtype index may be different if displayed row range does not start at zero.
        entry_subtype_index = self.get_entry_id(row_index)
        deleted_entry = subtype_list.pop(entry_subtype_index)
        self.select_entry_row_index(None)
        self.refresh_entries()
        return deleted_entry

    def copy_python_instance_text(self, row_index: int, category=None):
        """Copies valid string representation of given entry to clipboard."""
        if row_index is None:
            self.bell()
            return

        subtype_list = self._get_category_subtype_list(category)
        entry = subtype_list[row_index]
        self.clipboard_clear()
        self.clipboard_append(repr(entry))
        self.update()

    def popout_entry_text_edit(self, row_index):
        """Can actually change both ID and text."""
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_text(entry_id, self.active_category)
            popout_editor = EntryTextEditBox(
                self,
                self.active_category,
                category_data=self.get_category_data(),
                entry_id=entry_id,
                initial_text=initial_text,
                edit_entry_id=False,
            )
            try:
                _, new_text = popout_editor.go()
            except Exception as e:
                _LOGGER.error(e, exc_info=True)
                return self.CustomDialog("Entry Text Error", f"Error occurred while setting entry text:\n\n{e}")
            if new_text is not None:
                self.change_entry_text(row_index, new_text)

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True, coord=None):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index, coord=coord)
                return
        else:
            self._cancel_field_value_edit()

        self.selected_field_row_index = row_index

        if old_row_index is not None:
            self.field_rows[old_row_index].active = False
        if row_index is not None:
            self.field_rows[row_index].active = True
            if set_focus_to_value:
                self.field_rows[row_index].active_value_widget.focus_set()

    # TODO: how does field_press react if a coord is being edited? Should go to next coord, probably.

    def _get_field_edit_widget(self, row_index):
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.active_row_index))[field_row.field_name]

        if issubclass(field_type, Vector3):
            if self.e_coord is None:
                return None  # Exact coordinate not clicked.
            return self.Entry(
                field_row.value_vector_frame,
                initial_text=getattr(field_value, self.e_coord),
                numbers_only=True,
                sticky="ew",
                width=5,
                column="xyz".index(self.e_coord),
            )

        return super()._get_field_edit_widget(row_index)

    def _start_field_value_edit(self, row_index, coord=None):
        if self.e_field_value_edit and self.e_coord and coord and coord != self.e_coord:
            # Finish up previous coord edit.
            self._confirm_field_value_edit(row_index)
        self.e_coord = coord
        super()._start_field_value_edit(row_index)

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None
            self.e_coord = None

    def _confirm_field_value_edit(self, row_index):
        if self.e_field_value_edit:
            row = self.field_rows[row_index]
            if not row.editable:
                raise TypeError(f"Cannot edit field {row.field_name}. This shouldn't happen; please tell Grimrukh!")
            new_text = self.e_field_value_edit.var.get()
            try:
                new_value = row.string_conversion_method(new_text)
            except InvalidFieldValueError as e:
                _LOGGER.error(f"Invalid input {new_text} for field {row.field_nickname}. Error: {str(e)}")
                self.bell()
                self.CustomDialog("Invalid Field Value", f"Invalid field value. Error:\n\n{str(e)}")
                return
            field_changed = self.change_field_value(row.field_name, new_value)
            if field_changed:
                row.update_field_value_display(new_value)
            self._cancel_field_value_edit()

            if issubclass(row.field_type, (CharacterModel, ObjectModel)) and row.field_links[0].name is None:
                # Offer to create models (after checking if they're valid) then update field display again if done.
                if self.add_models(row.field_type, new_value):
                    row.update_field_value_display(new_value)

    def change_field_value(self, field_name: str, new_value):
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if self.e_coord:
            old_value = getattr(old_value, self.e_coord)
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            if self.e_coord:
                setattr(field_dict[field_name], self.e_coord, new_value)
            else:
                field_dict[field_name] = new_value
        except InvalidFieldValueError as e:
            self.bell()
            self.CustomDialog(title="Field Value Error", message=str(e))
            return False
        return True

    def _field_press_up(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new_row = self.e_field_value_edit is not None
            new_coord = ""
            if self.e_coord is not None:
                if self.e_coord == "y":
                    new_coord = "x"
                    edit_new_row = False
                elif self.e_coord == "z":
                    new_coord = "y"
                    edit_new_row = False
            self._confirm_field_value_edit(self.selected_field_row_index)
            if new_coord in {"x", "y"}:
                self._start_field_value_edit(self.selected_field_row_index, coord=new_coord)
            else:
                self._shift_selected_field(-1)
            if edit_new_row and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[1] != 1.0 or self.selected_field_row_index < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, "units")

    def _field_press_down(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new_row = self.e_field_value_edit is not None or self.e_coord
            new_coord = ""
            if self.e_coord is not None:
                if self.e_coord == "x":
                    new_coord = "y"
                    edit_new_row = False
                elif self.e_coord == "y":
                    new_coord = "z"
                    edit_new_row = False
            self._confirm_field_value_edit(self.selected_field_row_index)
            if new_coord in {"y", "z"}:
                self._start_field_value_edit(self.selected_field_row_index, coord=new_coord)
            else:
                self._shift_selected_field(+1)
            if edit_new_row and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[0] != 0.0 or self.selected_field_row_index > 5:
                self.field_canvas.yview_scroll(1, "units")

    def _get_display_categories(self):
        """ALl combinations of MSB entry list names and their subtypes, properly formatted."""
        categories = []
        for msb_type, subtypes in self.maps.MSB_CLASS.get_display_type_dict().items():
            for msb_subtype in subtypes:
                if isinstance(msb_subtype, BaseMSBRegionSubtype) and msb_subtype.name in {"Circle", "Rect"}:
                    continue  # These useless 2D region types are hidden.
                if isinstance(msb_subtype, BaseMSBModelSubtype) and msb_subtype.name in {"Items"}:
                    continue  # Unused 'item' model type hidden.
                categories.append(f"{msb_type}: {msb_subtype.pluralized_name}")
        return categories

    def get_selected_msb(self) -> MSB:
        map_name = self.maps.GET_MAP(self.map_choice_stem).name
        return self.maps[map_name]

    def get_category_data(self, category=None) -> list[MSBEntry]:
        """Gets entry data from map choice, entry list choice, and entry type choice (active category).

        For Maps, this actually returns a *list*, not a dict, and not the real `MSBEntryList`. Entry IDs are equivalent
        to entry/row indices in this list, so all parent methods still function as expected.
        """
        return list(self._get_category_subtype_list(category))

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns a `zip()` generator for parent method."""
        entry_list = self.get_category_data(category)
        return zip(range(first_index, last_index), entry_list[first_index:last_index])

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Entry index and entry ID are equivalent in Maps.

        Note that `.get_entry_id()` is still necessary to get the true entry index from the displayed row index.
        """
        return entry_id

    def get_entry_text(self, entry_index: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_index].name

    def get_entry_description(self, entry_index: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_index].description

    def _set_entry_text(self, entry_index: int, text: str, category=None, update_row_index=None):

        subtype_list = self._get_category_subtype_list(category)
        subtype_list[entry_index].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_index, text, subtype_list[entry_index].description)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Not implemented for Map Editor."""
        raise TypeError("Cannot set entry IDs in Maps Editor (entries are just a list).")

    def get_field_dict(self, entry_index: int, category=None) -> MSBEntry:
        """Uses entry index instad of entry ID."""
        return self.get_category_data(category)[entry_index]

    def get_field_display_info(self, field_dict, field_name):
        field = field_dict.FIELD_INFO[field_name]
        return field.nickname, field_name in field_dict.field_names, field.display_type, field.description

    def get_field_names(self, field_dict):
        return field_dict.all_field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        """Game subclasses can override this to support more link types."""
        if valid_null_values is None:
            valid_null_values = {0: "Default/None", -1: "Default/None"}
        return self.linker.soulstruct_link(
            field_type, field_value, valid_null_values=valid_null_values, map_override=None,
        )

    def add_models(self, model_game_type: tp.Type[MapModel], model_name):
        map_stem = self.map_choice_stem
        _, model_subtype_name = model_game_type.get_msb_entry_type_subtype()
        if self.linker.validate_model_subtype(model_game_type, model_name, map_stem=map_stem):
            result = self.CustomDialog(
                title=f"Add {model_subtype_name} Model",
                message=f"Add {model_subtype_name} model {model_name} to map?",
                button_names=("Yes, add it", "No, leave as missing"),
                button_kwargs=("YES", "NO"),
                return_output=0,
                default_output=0,
                cancel_output=1,
            )
            if result == 0:
                self.get_selected_msb().new_model(model_subtype_name, name=model_name, map_stem=map_stem)
                return True
        else:
            self.CustomDialog(
                title=f"Invalid {model_subtype_name} Model",
                message=f"{model_subtype_name} model {model_name} does not have any data in the game files.\n"
                f"This will likely cause severe problems in your game!",
            )

        return False

    def copy_player_position(self, translate=False, rotate=False, draw_parent_name=False, y_offset=0.0):
        if not translate and not rotate and not draw_parent_name:
            raise ValueError("At least one of `translate`, `rotate`, and `draw_parent_name` should be True.")
        new_translate = None
        new_rotate_y = None
        new_collision = None
        if not self.linker.hook_created:
            if (
                self.CustomDialog(
                    title="Cannot Read Memory",
                    message="Game has not been hooked. Would you like to try hooking into the game now?",
                    default_output=0,
                    cancel_output=1,
                    return_output=0,
                    button_names=("Yes, hook in", "No, forget it"),
                    button_kwargs=("YES", "NO"),
                )
                == 1
            ):
                return
            if self.linker.runtime_hook():
                # Call this function again.
                return self.copy_player_position(
                    translate=translate, rotate=rotate, draw_parent_name=draw_parent_name, y_offset=y_offset,
                )
            return
        try:
            if translate:
                player_x = self.linker.get_game_value("player_x")
                player_y = self.linker.get_game_value("player_y") + y_offset
                player_z = self.linker.get_game_value("player_z")
                new_translate = Vector3([player_x, player_y, player_z])
            if rotate:
                new_rotate_y = math.degrees(self.linker.get_game_value("player_angle"))
            if draw_parent_name:
                map_prefix = self.map_choice_stem[:6]  # e.g. "m10_02"
                display_group_ints = self.linker.get_game_value(f"{map_prefix}_display_groups")
                display_groups = int_group_to_bit_set(display_group_ints, assert_size=4)  # TODO: Other game sizes.
                if not display_groups:
                    self.CustomDialog(
                        title="No Collision Found",
                        message=f"No display groups in {self.map_choice_stem} are currently active.\n"
                                f"Are you sure the player is currently standing in this map? (No changes made.)",
                    )
                    return
                # NOTE: `.collisions` subtype is always present, but still not defined in base class.
                search = [
                    col for col in self.get_selected_msb()["collisions"]
                    if col.display_groups == display_groups
                ]
                if len(search) > 1:
                    # Find lowest-index collision.
                    new_collision = min(search, key=lambda c: int(c.model_name[1:5]))
                elif search:
                    new_collision = search[0]
                else:
                    self.CustomDialog(
                        title="No Collision Found",
                        message=f"Could not find any collisions that match current player display groups: "
                                f"{display_groups}. No changes made.",
                    )
                    return
        except MemoryHookCallError as e:
            _LOGGER.error(str(e), exc_info=True)
            self.CustomDialog(
                title="Cannot Read Memory",
                message=f"An error occurred when trying to copy player position (see log for full traceback):\n\n"
                f"{str(e)}\n\n"
                f"If this error doesn't seem like it can be solved (e.g. did you close the game after\n"
                f"hooking into it?) please inform Grimrukh.",
            )
            return
        field_dict = self.get_selected_field_dict()
        if translate:
            field_dict["translate"] = new_translate
        if rotate:
            field_dict["rotate"].y = new_rotate_y
        if draw_parent_name:
            field_dict["draw_parent_name"] = new_collision.name
        self.refresh_fields()

    def popout_sequence_name_edit(self, field_name: str, field_nickname: str, game_object_type: tp.Type):
        msb_entry = self.get_selected_field_dict()
        valid_names = [
            name for name in self.linker.get_map_entry_type_names(game_object_type)
            if not name.startswith("_EnvironmentEvent")  # exclude all these
        ]
        popout_editor = SequenceNameEditBox(
            self,
            initial_names=msb_entry[field_name],
            valid_names=valid_names,
            window_title=f"Editing {field_nickname}",
        )
        try:
            new_names = popout_editor.go()
        except Exception as ex:
            _LOGGER.error(ex, exc_info=True)
            return self.CustomDialog("Sequence Name Error", f"Error occurred while setting sequence names:\n\n{ex}")
        if new_names is not None:
            msb_entry[field_name] = new_names
            self.refresh_fields()

    def add_point_from_player_position(self, sequence_field: str, field_nickname: str):
        if not self.linker.hook_created:
            if (
                self.CustomDialog(
                    title="Cannot Read Memory",
                    message="Game has not been hooked. Would you like to try hooking into the game now?",
                    default_output=0,
                    cancel_output=1,
                    return_output=0,
                    button_names=("Yes, hook in", "No, forget it"),
                    button_kwargs=("YES", "NO"),
                )
                == 1
            ):
                return
            if self.linker.runtime_hook():
                # Call this function again.
                return self.add_point_from_player_position(sequence_field, field_nickname)
            return

        field_dict = self.get_selected_field_dict()
        sequence = field_dict[sequence_field]
        i = -1
        for i, existing_region_name in enumerate(sequence):
            if existing_region_name is None:
                break
        if i == -1:
            # Sequence is full.
            self.CustomDialog(
                title="Cannot Add New Point",
                message=f"Field '{sequence_field}' of entry '{field_dict.name}' cannot hold any more Points.",
            )
            return
        point_name = f"{field_dict.name} {field_nickname} {i}"

        try:
            player_x = self.linker.get_game_value("player_x")
            player_y = self.linker.get_game_value("player_y")
            player_z = self.linker.get_game_value("player_z")
            new_translate = Vector3([player_x, player_y, player_z])
            new_rotate_y = math.degrees(self.linker.get_game_value("player_angle"))
        except MemoryHookCallError as e:
            _LOGGER.error(str(e), exc_info=True)
            self.CustomDialog(
                title="Cannot Read Memory",
                message=f"An error occurred when trying to copy player position (see log for full traceback):\n\n"
                f"{str(e)}\n\n"
                f"If this error doesn't seem like it can be solved (e.g. did you close the game after\n"
                f"hooking into it?) please inform Grimrukh.",
            )
            return

        self.get_selected_msb()["points"].new(
            name=point_name,
            translate=new_translate,
            rotate=Vector3([0, new_rotate_y, 0]),
        )
        sequence[i] = point_name
        self.refresh_fields()
