from __future__ import annotations

__all__ = ["MapsEditor"]

import abc
import ast
import logging
import math
import typing as tp
from enum import IntEnum
from types import ModuleType

from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.base.game_types import GAME_TYPE, GAME_INT_TYPE, GameObjectInt, GameObjectIntSequence
from soulstruct.base.game_types.map_types import *
from soulstruct.base.maps.msb.enums import MSBSupertype, BaseMSBModelSubtype, BaseMSBRegionSubtype
from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.base.maps.msb.utils import GroupBitSet, GroupBitSet128, GroupBitSet256
from soulstruct.base.project.utilities import (
    bind_events,
    NameSelectionBox,
    CategorizedNameSelectionBox,
    TextEditBox,
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
    from ..links import MapsLink

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

    def update_entry(self, entry_index: int, entry_text: str, entry_tooltip: str = ""):
        """Update the data currently presented in this `MapEntryRow`."""
        self.entry_id = entry_index
        entry_data = self.master.get_category_data()[entry_index]  # type: MSBEntry
        text_label_fg = "#FFF"  # white
        if hasattr(entry_data, "entity_id"):
            text_tail = f"  {{ID: {entry_data.entity_id}}}" if entry_data.entity_id not in {-1, 0} else ""
            if text_tail:
                text_label_fg = "#FDA"  # orange
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

        if entry_tooltip:
            self.tooltip.text = entry_tooltip
        else:
            self.tooltip.text = None
        self._entry_text = entry_text
        self.text_label.var.set(entry_text + text_tail)
        self.text_label["fg"] = text_label_fg
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
                copy_fields += ("draw_parent",)
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
            label="Copy Python Constructor",
            command=lambda: self.master.copy_python_constructor_text(self.row_index),
        )


class MapFieldRow(FieldRow):

    CAMEL_CASE_NICKNAMES = False  # field nicknames already properly formatted for display

    master: MapsEditor

    def __init__(self, editor: MapsEditor, row_index: int, main_bindings: dict = None):
        """Represents, at any given time, the name and value (string representation) of an `MSBEntry` field."""
        super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

        bg_color = self._get_color()

        # Main difference of Maps tab is the ability to support three separate `Vector3` fields.
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

    def update_field_value_display(self, new_value: tp.Any):
        """Updates field value display.

        This handles `Vector3` field types separately (`self.master.e_coord` is the string name of the component).
        Otherwise, it is identical to the base method, calling `field_update_method()` (which in turns looks for
        `_update_field_{type}()` methods or falls back to some basic types) and then updating links/context menu.
        """
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

    # region Value Update Methods

    def _update_field_GameObjectInt(self, value):
        """Adds any recognized `GameObjectInt` names as hints."""
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
            # `value` is an `MSBEntry` or `None`.
            if not value:
                self.value_label.var.set("None")
            else:
                msb_entry_name = value.name
                if self.field_type == self.master.GAME_TYPES_MODULE.CharacterModel:
                    # Auto-display character model names for convenience.
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

    def _update_field_GroupBitSet128(self, value: GroupBitSet128):
        """Update `set` field with a sorted list."""
        self.value_label.var.set(repr(value.to_sorted_bit_list()))
        self._activate_value_widget(self.value_label)

    def _update_field_GroupBitSet256(self, value: GroupBitSet256):
        """Update `set` field with a sorted list."""
        self.value_label.var.set(repr(value.to_sorted_bit_list()))
        self._activate_value_widget(self.value_label)

    # endregion

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

    def _add_copy_option(self, menu, translate=False, rotate=False, draw_parent=False, y_offset=0.0):
        text = []
        if translate:
            text.append(f"translate ({y_offset} Y)" if y_offset != 0.0 else "translate")
        if rotate:
            text.append("rotate")
        if draw_parent:
            text.append("draw parent")
        label = f"Copy player {' + '.join(text)}"
        menu.add_command(
            label=label,
            command=lambda: self.master.copy_player_position(
                translate=translate, rotate=rotate, draw_parent=draw_parent, y_offset=y_offset,
            )
        )

    def build_field_context_menu(self):
        """For linked fields, adds an option to select an entry name from the linked table."""
        self.context_menu.delete(0, "end")

        has_custom_int_option = True
        if issubclass(self.field_type, GameObjectInt):
            # Add links to other game objects.
            for field_link in self.field_links:
                field_link.add_to_context_menu(self.context_menu)
            has_custom_int_option = False
        if issubclass(self.field_type, GameObjectIntSequence):
            self.context_menu.add_command(
                label="Select linked entries from list", command=self.choose_linked_map_entries
            )
            if self.field_type.game_object_type is Region or self.field_type.game_object_type is RegionPoint:
                # Option to add a point to a list of Points, based on current player translate/rotate.
                # NOTE: Assumes that Points are sufficient for any `Region` sequence, which I think is true for all
                # sequence fields I've seen.
                self.context_menu.add_command(
                    label=f"Add new Point from player translate + rotate",
                    command=lambda: self.master.add_point_from_player_position(self.field_name, self.field_nickname),
                )
        if issubclass(self.field_type, MapEntry):
            self.context_menu.add_command(
                label="Select linked entry from list", command=self.choose_linked_map_entry
            )
            has_custom_int_option = False
            if issubclass(self.field_type, MapModel):
                self.context_menu.add_command(
                    label=f"Set model by name and add if needed", command=self.choose_and_add_new_model
                )
            if self.field_type == self.master.GAME_TYPES_MODULE.CharacterModel:
                self.context_menu.add_command(
                    label="Select model from complete list", command=self.choose_character_model
                )
        if has_custom_int_option:
            # Users can enter their own custom integer values for (non-`GameObject`) IntEnums.
            if issubclass(self.field_type, IntEnum):
                self.context_menu.add_command(label="Set custom integer value", command=self._set_custom_intenum_value)

        # Users can open a dialog of checkbuttons.
        if issubclass(self.field_type, GroupBitSet):
            self.context_menu.add_command(label="Modify groups with checkbuttons", command=self._set_group_checkbuttons)

        # Add memory-copying options.
        msb_type, msb_subtype = self.master.active_category.split(": ")
        if msb_type == "Regions" or msb_subtype in {"Characters", "Objects", "PlayerStarts"}:
            copy_fields = ("translate", "rotate")
            if msb_subtype in {"Characters", "Objects"}:
                copy_fields += ("draw_parent",)
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

    def choose_linked_map_entry(self):
        """Pop-out window where user can select a map entry name from among linked category type(s)."""
        if not issubclass(self.field_type, MapEntry):
            return  # option shouldn't even appear
        entries = self.master.linker.get_map_entry_subtype_list(self.field_type)

        categories = {}  # type: dict[str, list[str]]
        for entry in entries:
            display_name = entry.name

            if self.master.character_models and entry.SUBTYPE_ENUM.name in ("CharacterModel", "PlayerModel"):
                model_id = int(entry.name.lstrip("c"))
                display_name += f"  {{{self.master.character_models.get(model_id, 'UNKNOWN')}}}"
            categories.setdefault(entry.SUBTYPE_ENUM.pluralized_name, []).append(display_name)

        # Choose initial entry subtype based on current value (if present) or a standard default otherwise.
        current_entry = self.master.get_selected_field_dict()[self.field_name]
        if current_entry is not None:
            initial_category = current_entry.SUBTYPE_ENUM.pluralized_name
            if initial_category not in categories:
                initial_category = ""  # unusual!
        elif self.field_name == "draw_parent":
            initial_category = "Collisions"
        else:
            initial_category = ""

        # Wait for user to select entry name.
        selected_category_and_name = CategorizedNameSelectionBox(self.master, categories, initial_category).go()

        if selected_category_and_name is None:
            # User cancelled.
            return
        selected_name = selected_category_and_name[1]  # don't care about category
        selected_name = selected_name.split("  {")[0]  # remove any model tail
        entry_names = [entry.name for entry in entries]
        selected_entry = entries[entry_names.index(selected_name)]
        self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_entry)
        # noinspection PyTypeChecker
        entry_link = self.field_links[0]  # type: MapsLink
        if not entry_link.entry:
            # Shouldn't be possible.
            selected_name += "  {BROKEN LINK}"
            self.link_missing = True
            self.master.CustomDialog(
                title="Map Entry Link Error",
                message="Map entry link was broken after selecting map entry from list. This should not happen; "
                "please try restarting Soulstruct, and inform Grimrukh if the problem persists.",
            )
            selected_entry = None
        else:
            self.link_missing = False
            selected_entry = entry_link.entry

        self.master.change_field_value(self.field_name, selected_entry)
        self.value_label.var.set(selected_name)  # already includes any model tail we want
        self.build_field_context_menu()

    def choose_and_add_new_model(self):
        """Pop-out window where user can enter a new model name, then create a new model of that name if needed."""
        if not issubclass(self.field_type, MapModel):
            return  # shouldn't be possible

        new_model_name = TextEditBox(self.master, allow_newlines=False, window_title="New Model Name", width=40).go()

        if new_model_name is None:
            return  # do nothing

        existing_entries = self.master.linker.get_map_entry_subtype_list(self.field_type)
        existing_entry_names = [entry.name for entry in existing_entries]
        if new_model_name in existing_entry_names:
            self.master.CustomDialog(
                title="Model Name Exists",
                message=f"Model name '{new_model_name}' already exists in MSB.\nSetting field to existing model.",
            )
        else:
            # Offer to create models (after checking if they're valid) then update field display again if done.
            new_model_created = self.master.add_models(self.field_type, new_model_name)
            if not new_model_created:
                return

        entries = self.master.linker.get_map_entry_subtype_list(self.field_type)  # should include just-added model
        entry_names = [entry.name for entry in entries]
        selected_model = entries[entry_names.index(new_model_name)]
        self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_model)
        # noinspection PyTypeChecker
        entry_link = self.field_links[0]  # type: MapsLink
        if not entry_link.entry:
            # Shouldn't be possible.
            new_model_name += "  {BROKEN LINK}"
            self.link_missing = True
            self.master.CustomDialog(
                title="Map Entry Link Error",
                message="Map entry link was broken after creating/choosing new model. This should not happen; "
                        "please try restarting Soulstruct, and inform Grimrukh if the problem persists.",
            )
            selected_model = None
        else:
            self.link_missing = False
            selected_model = entry_link.entry
            # Add new model tail for characters.
            if self.master.character_models and selected_model.SUBTYPE_ENUM.name in ("CharacterModel", "PlayerModel"):
                model_id = int(selected_model.name.lstrip("c"))
                new_model_name += f"  {{{self.master.character_models.get(model_id, 'UNKNOWN')}}}"

        self.master.change_field_value(self.field_name, selected_model)
        self.value_label.var.set(new_model_name)
        self.build_field_context_menu()

    def choose_linked_map_entries(self):
        """NOTE: Currently assumes that `game_object_type` is specifically a `MapEntry` subclass."""
        if not issubclass(self.field_type, GameObjectIntSequence):
            return  # option shouldn't even appear

        msb_entry = self.master.get_selected_field_dict()
        current_sequence = msb_entry[self.field_name]
        current_names = [e.name if e else "" for e in current_sequence]
        valid_entries = [
            entry for entry in self.master.linker.get_map_entry_subtype_list(self.field_type.game_object_type)
            if not entry.name.startswith("_EnvironmentEvent")  # exclude all these (too many)
        ]
        valid_display_names = [e.name for e in valid_entries]

        try:
            new_names = SequenceNameEditBox(
                self.master,
                initial_names=current_names,
                valid_names=valid_display_names,
                window_title=f"Editing {self.field_nickname}",
            ).go()
        except Exception as ex:
            _LOGGER.error(ex, exc_info=True)
            return self.master.CustomDialog(
                "Sequence Name Error",
                f"Error occurred while setting sequence entries:\n\n{ex}",
            )

        if new_names is None:
            # User cancelled.
            return

        selected_entries = []
        label_names = []
        for name in new_names:
            if not name:  # empty sequence entry
                selected_entries.append(None)
                label_names.append("None")
                continue

            selected_entry = valid_entries[valid_display_names.index(name)]
            self.field_links = self.master.linker.soulstruct_link(self.field_type.game_object_type, selected_entry)
            # noinspection PyTypeChecker
            entry_link = self.field_links[0]  # type: MapsLink
            if not entry_link.entry:
                # Shouldn't be possible.
                label_names.append("None")
                self.link_missing = True
                self.master.CustomDialog(
                    title="Map Link Error",
                    message="Map link was broken after selecting map entry from list. This should not happen; "
                            "please try restarting Soulstruct, and inform Grimrukh if the problem persists.",
                )
                selected_entry = None
            else:
                self.link_missing = False
                selected_entry = entry_link.entry
                label_names.append(selected_entry.name)
            selected_entries.append(selected_entry)

        self.master.change_field_value(self.field_name, selected_entries)
        self.update_field_value_display(selected_entries)
        self.build_field_context_menu()

    def choose_character_model(self):
        if not issubclass(self.field_type, self.master.GAME_TYPES_MODULE.CharacterModel):
            return  # option shouldn't even appear
        names = [f"c{model_id:04d}  {{{model_name}}}" for model_id, model_name in self.master.character_models.items()]

        new_model_name = NameSelectionBox(self.master, names, split_string="  {").go()

        if new_model_name is None:
            # User cancelled.
            return

        existing_entries = self.master.linker.get_map_entry_subtype_list(self.field_type)
        existing_entry_names = [entry.name for entry in existing_entries]
        if new_model_name in existing_entry_names:
            self.master.CustomDialog(
                title="Model Name Exists",
                message=f"Model name '{new_model_name}' already exists in MSB.\nSetting field to existing model.",
            )
        else:
            # noinspection PyTypeChecker
            new_model_created = self.master.add_models(self.field_type, new_model_name)
            if not new_model_created:
                return

        entries = self.master.linker.get_map_entry_subtype_list(self.field_type)  # should include just-added model
        entry_names = [entry.name for entry in entries]
        selected_model = entries[entry_names.index(new_model_name)]
        self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_model)
        # noinspection PyTypeChecker
        entry_link = self.field_links[0]  # type: MapsLink
        if not entry_link.entry:
            # Shouldn't be possible.
            new_model_name += "  {BROKEN LINK}"
            self.link_missing = True
            self.master.CustomDialog(
                title="Map Entry Link Error",
                message="Map entry link was broken after creating/choosing new model. This should not happen; "
                        "please try restarting Soulstruct, and inform Grimrukh if the problem persists.",
            )
            selected_model = None
        else:
            self.link_missing = False
            selected_model = entry_link.entry
            # Add new model tail for characters.
            if self.master.character_models and selected_model.SUBTYPE_ENUM.name in ("CharacterModel", "PlayerModel"):
                model_id = int(selected_model.name.lstrip("c"))
                new_model_name += f"  {{{self.master.character_models.get(model_id, 'UNKNOWN')}}}"

        self.master.change_field_value(self.field_name, selected_model)
        self.value_label.var.set(new_model_name)
        self.build_field_context_menu()

    def _set_group_checkbuttons(self):
        current_group_bit_set = self.master.get_selected_field_dict()[self.field_name]  # type: GroupBitSet
        new_bit_set = GroupBitSetEditBox(
            self.master,
            initial_bit_set=current_group_bit_set.enabled_bits,
            bit_count=current_group_bit_set.BIT_COUNT,  # class variable
            window_title=f"Modify {self.field_nickname}",
        ).go()
        if new_bit_set is None:
            return
        new_group_bit_set = current_group_bit_set.__class__(new_bit_set)
        field_changed = self.master.change_field_value(self.field_name, new_group_bit_set)
        if field_changed:
            self.update_field_value_display(new_group_bit_set)

    @property
    def editable(self):
        return id(self.active_value_widget) in {id(self.value_label), id(self.value_vector_frame)}

    def _string_to_Vector3(self, string):
        """Operates on individual vector component `float` fields."""
        return self._string_to_float(string)

    def _string_to_GroupBitSet128(self, string):
        try:
            enabled_bits_list = ast.literal_eval(string)
        except ValueError:
            raise InvalidFieldValueError(
                f"Could not interpret string as a `GroupBitSet128` for field {self.field_nickname}: {string}"
            )
        try:
            return GroupBitSet128(set(enabled_bits_list))
        except (TypeError, ValueError):
            raise InvalidFieldValueError(
                f"Could not interpret string as a `GroupBitSet128` for field {self.field_nickname}: {string}"
            )

    def _string_to_GroupBitSet256(self, string):
        try:
            enabled_bits_list = ast.literal_eval(string)
        except ValueError:
            raise InvalidFieldValueError(
                f"Could not interpret string as a `GroupBitSet256` for field {self.field_nickname}: {string}"
            )
        try:
            return GroupBitSet256(set(enabled_bits_list))
        except (TypeError, ValueError):
            raise InvalidFieldValueError(
                f"Could not interpret string as a `GroupBitSet256` for field {self.field_nickname}: {string}"
            )

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


class MapsEditor(BaseFieldEditor, abc.ABC):
    DATA_NAME = "Maps"
    TAB_NAME = "maps"
    CATEGORY_BOX_WIDTH = 400
    ENTRY_BOX_WIDTH = 350
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 42  # highest count found so far (Parts.Collisions in Bloodborne)
    FIELD_NAME_WIDTH = 20
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 80

    ENTRY_ROW_CLASS = MapEntryRow
    FIELD_ROW_CLASS = MapFieldRow

    GAME_TYPES_MODULE: ModuleType

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
                    label_position="left",
                    width=55,
                    font=self.CONFIG.REGULAR_FONT,
                    on_select_function=self.on_map_choice,
                    sticky="w",
                    padx=10,
                )

            super().build()

        self.entry_canvas_context_menu = self.Menu(self.entry_canvas)
        self.entry_canvas_context_menu.add_command(label="Create New Entry", command=self.add_new_default_entry)
        self.entry_canvas.bind("<Button-3>", self.right_click_entry_canvas)

    def check_for_repeated_entity_ids(self):
        """Check for duplicate entity IDs."""
        repeat_warning = ""
        for map_name, msb in self.maps.items():
            repeats = msb.get_repeated_entity_ids()
            if repeats[MSBSupertype.REGIONS]:
                regions = "\n".join(f"{e.entity_id}: {e.name}" for e in repeats[MSBSupertype.REGIONS])
                region_ids = ", ".join(str(e.entity_id) for e in repeats[MSBSupertype.REGIONS])
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

        if self.active_category is not None:
            entries_to_display = self._get_category_name_range(
                first_index=self.first_display_index, last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
            )
        else:
            entries_to_display = []

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
        if subtype_index == -1:  # select last element in list (just added)
            subtype_index = len(subtype_list) - 1
        self.select_entry_id(subtype_index, set_focus_to_text=True, edit_if_already_selected=False)
        # TODO: ActionHistory stuff?
        return True

    def add_relative_entry(self, subtype_index: int, offset=1, text=None):
        """Duplicate entry at `subtype_index` to index `subtype_index + offset`."""
        subtype_list = self._get_category_subtype_list()
        source_msb_entry = subtype_list[subtype_index]
        msb_entry = source_msb_entry.copy()
        msb_entry.name = text if text is not None else source_msb_entry.name + " <COPY>"
        return self._add_entry(subtype_index + offset, text=msb_entry.name, new_field_dict=msb_entry)

    def add_relative_entry_and_copy_player_transform(
        self, entry_index, translate=False, rotate=False, draw_parent=False
    ):
        self.add_relative_entry(entry_index)
        # Duplicated entry is selected, so we can apply player transform now.
        self.copy_player_position(translate=translate, rotate=rotate, draw_parent=draw_parent)

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

    def copy_python_constructor_text(self, row_index: int, category=None):
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
        """Handles special cases (Vector3, GroupBitSet, MSBEntry) or goes to parent method."""
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell Grimrukh!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.active_row_index))[field_row.field_name]

        if issubclass(field_type, MapEntry):
            # Pop-out editor to choose a map entry.
            field_row.choose_linked_map_entry()
            return None

        if issubclass(field_type, GameObjectIntSequence) and issubclass(field_type.game_object_type, MapEntry):
            # Pop-out editor to choose multiple map entries.
            field_row.choose_linked_map_entries()
            return None

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

        if issubclass(field_type, GroupBitSet):
            field_value: GroupBitSet
            initial_text = repr(field_value.to_sorted_bit_list())
            return self.Entry(
                field_row.value_box,
                initial_text=initial_text,
                integers_only=field_type == int,
                numbers_only=field_type == float,
                sticky="ew",
                width=5,
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

    def _get_display_categories(self) -> list[str]:
        """ALl combinations of MSB entry list names and their subtypes, properly formatted."""
        categories = []
        for msb_supertype, subtype_enums in self.maps.FILE_CLASS.get_display_type_dict().items():
            for subtype_enum in subtype_enums:
                if isinstance(subtype_enum, BaseMSBRegionSubtype) and subtype_enum.name in {"Circle", "Rect"}:
                    continue  # These useless 2D region types are hidden.
                if isinstance(subtype_enum, BaseMSBModelSubtype) and subtype_enum.name in {"Items"}:
                    continue  # Unused 'item' model type hidden.
                categories.append(f"{msb_supertype}: {subtype_enum.pluralized_name}")
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
        return zip(range(first_index, last_index), entry_list[first_index:last_index])  # NOT strict

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

    def get_field_display_info(self, field_dict: MSBEntry, field_name: str) -> tuple[str, bool, tp.Type[tp.Any], str]:
        nickname, tooltip, display_type = field_dict.get_field_display_info(field_name, self.GAME_TYPES_MODULE)
        return nickname, field_name not in field_dict.HIDE_FIELDS, display_type, tooltip

    def get_field_names(self, field_dict: MSBEntry) -> tuple[str]:
        """NOTE: Includes hidden fields (which are filtered by caller if option set)."""
        return field_dict.get_field_names() if field_dict else ()

    def get_field_links(self, field_type: GAME_INT_TYPE, field_value, valid_null_values=None) -> list:
        """Game subclasses can override this to support more link types."""
        if valid_null_values is None:
            valid_null_values = {0: "Default/None", -1: "Default/None"}
        return self.linker.soulstruct_link(
            field_type, field_value, valid_null_values=valid_null_values, map_override=None,
        )

    def add_models(self, model_game_type: tp.Type[MapModel], model_name, auto_yes_if_valid=False):
        map_stem = self.map_choice_stem
        _, model_subtype_name = model_game_type.get_msb_entry_supertype_subtype()
        if self.linker.validate_model_subtype(model_game_type, model_name, map_stem=map_stem):
            if auto_yes_if_valid:
                result = 0
            else:
                result = self.CustomDialog(
                    title=f"Add {model_subtype_name} Model",
                    message=f"Add {model_subtype_name} {model_name} to map?",
                    button_names=("Yes, add it", "No, don't add it"),
                    button_kwargs=("YES", "NO"),
                    return_output=0,
                    default_output=0,
                    cancel_output=1,
                )
            if result == 0:
                self.get_selected_msb().get_or_create_model(model_subtype_name, name=model_name, map_stem=map_stem)
                return True
        else:
            result = self.CustomDialog(
                title=f"Add Unknown {model_subtype_name} Model",
                message=f"Game file cannot be found for {model_subtype_name} '{model_name}'.\n"
                        f"Are you sure you want to add it to the map?",
                button_names=("Yes, add it", "No, don't add it"),
                button_kwargs=("YES", "NO"),
                return_output=0,
                default_output=0,
                cancel_output=1,
            )
            if result == 0:
                self.get_selected_msb().get_or_create_model(model_subtype_name, name=model_name, map_stem=map_stem)
                return True

        return False

    def copy_player_position(self, translate=False, rotate=False, draw_parent=False, y_offset=0.0):
        if not translate and not rotate and not draw_parent:
            raise ValueError("At least one of `translate`, `rotate`, and `draw_parent` should be True.")
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
                    translate=translate, rotate=rotate, draw_parent=draw_parent, y_offset=y_offset,
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
            if draw_parent:
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
                    if col.display_groups.enabled_bits == display_groups
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
        field_dict = self.get_selected_field_dict()  # type: MSBEntry
        if translate:
            field_dict["translate"] = new_translate
        if rotate:
            field_dict["rotate"].y = new_rotate_y
        if draw_parent:
            field_dict["draw_parent"] = new_collision
        self.refresh_fields()

    def popout_sequence_name_edit(self, field_name: str, field_nickname: str, game_object_type: GAME_TYPE):
        """NOTE: Currently assumes that `game_object_type` is specifically a `MapEntry` subclass."""
        msb_entry = self.get_selected_field_dict()
        valid_entries = [
            entry for entry in self.linker.get_map_entry_subtype_list(game_object_type)
            if not entry.name.startswith("_EnvironmentEvent")  # exclude all these (too many)
        ]
        popout_editor = SequenceNameEditBox(
            self,
            initial_names=msb_entry[field_name],
            valid_names=[e.name for e in valid_entries],
            window_title=f"Editing {field_nickname}",
        )
        try:
            new_names = popout_editor.go()
        except Exception as ex:
            _LOGGER.error(ex, exc_info=True)
            return self.CustomDialog("Sequence Name Error", f"Error occurred while setting sequence names:\n\n{ex}")
        if new_names is not None:
            msb_entry[field_name] = [valid_entries[new_names.index(name)] for name in new_names]
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
