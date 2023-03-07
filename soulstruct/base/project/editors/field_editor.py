from __future__ import annotations

__all__ = ["BaseFieldEditor", "FieldRow"]

import abc
import logging
import typing as tp
from ast import literal_eval
from enum import IntEnum

from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.base.game_types import GAME_TYPE, GameObject, GameObjectSequence, MapEntry, BaseParam
from soulstruct.base.project.editors.base_editor import BaseEditor
from soulstruct.base.project.links import WindowLinker
from soulstruct.base.project.utilities import bind_events, NumberEditBox
from soulstruct.utilities.text import camel_case_to_spaces
from soulstruct.utilities.window import ToolTip

if tp.TYPE_CHECKING:
    from soulstruct.base.project.core import GameDirectoryProject

_LOGGER = logging.getLogger(__name__)


FieldTypeTyping = tp.Union[GAME_TYPE, tp.Type[GameObjectSequence], type, tp.Iterable]


class FieldRow:
    """Container/manager for widgets in a single field row in the Editor.

    These are only created once, and their contents are refreshed when needed (e.g. when a new entry is selected).
    Unlike entries, field value widgets may be Labels (which turn into Entries for editing), Checkbuttons, or
    Comboboxes. Each of these widgets is created for each row, so they can be hidden/dispalyed when needed by a
    given field type, rather than dynamically creating and destroying them every time a new entry/category is
    selected.
    """

    CAMEL_CASE_NICKNAMES = True

    def __init__(self, editor: BaseFieldEditor, row_index: int, main_bindings: dict = None):
        self.master = editor
        self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

        self.row_index = row_index
        self._active = False
        self._link_missing = False
        self.field_name = ""
        self.field_type = type  # type: FieldTypeTyping
        self.field_nickname = ""
        self.field_docstring = ""
        self.field_links = []
        self.link_missing = False

        bg_color = self._get_color()

        self.row_box = editor.Frame(
            width=editor.FIELD_BOX_WIDTH,
            height=editor.FIELD_ROW_HEIGHT,
            bg=bg_color,
            row=row_index,
            columnspan=2,
            sticky="nsew",
        )
        bind_events(self.row_box, main_bindings)

        self.field_name_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky="w")
        bind_events(self.field_name_box, main_bindings)

        self.field_name_label = editor.Label(
            self.field_name_box,
            text="",
            fg=editor.FIELD_NAME_FG,
            width=editor.FIELD_NAME_WIDTH,
            bg=bg_color,
            anchor="w",
            padx=(5, 0),
        )
        bind_events(self.field_name_label, main_bindings)

        self.value_box = editor.Frame(
            width=editor.FIELD_VALUE_BOX_WIDTH, row=row_index, column=1, bg=bg_color, sticky="ew"
        )
        bind_events(self.value_box, main_bindings)

        # VALUE WIDGETS

        self.value_label = editor.Label(
            self.value_box, text="", bg=bg_color, width=editor.FIELD_VALUE_WIDTH, anchor="w"
        )
        bind_events(self.value_label, main_bindings)

        self.value_checkbutton = editor.Checkbutton(
            self.value_box,
            label=None,
            bg=bg_color,
            no_grid=True,
            selectcolor="#000",
            command=self._checkbutton_toggle,
        )
        # Main focus bindings are not bound to Checkbutton.

        self.value_combobox = editor.Combobox(
            self.value_box,
            values=None,
            width=editor.FIELD_VALUE_WIDTH,
            no_grid=True,
            font=self.master.CONFIG.REGULAR_FONT,
            on_select_function=self._combobox_choice,
        )
        self.value_combobox.bind("<MouseWheel>", lambda _: "break")  # prevent scrolling on collapsed Combobox
        # Main focus bindings are not bound to Combobox.

        # TODO: BEHAVIOR_REF_TYPE combobox should also force a refresh, as it may change field names.
        #  (Class will need access to ParamEntry for this, which is fine.)

        self.context_menu = editor.Menu(self.row_box)
        self.tooltip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

        self.active_value_widget = self.value_label
        self.hide()

    def _combobox_choice(self, _=None):
        """Updates field value with integer value from Combobox enum or unknown integer.

        Note that the Combobox's appearance needs no further updating.
        """
        combobox_string = self.value_combobox.var.get()
        if combobox_string.startswith("Unknown: "):
            value = int(combobox_string[len("Unknown: "):])
        else:
            value = int(self.value_combobox.var.get().split(" ")[0])
        self.master.change_field_value(self.field_name, value)

    def _activate_value_widget(self, widget):
        if id(self.active_value_widget) != id(widget):
            self.active_value_widget.grid_remove()
        self.active_value_widget = widget

    def _checkbutton_toggle(self):
        """Modify appearance of Checkbutton when toggled."""
        new_value = self.value_checkbutton.var.get()
        if self.master.change_field_value(self.field_name, new_value):
            self.value_checkbutton.config(fg="#3F3" if new_value else "#F33", text="ON" if new_value else "OFF")
        else:
            self.value_checkbutton.var.set(not new_value)

    def update_field(
        self,
        name,
        nickname,
        value: tp.Any,
        field_type: type,
        docstring="",
    ):
        """Update widgets with given field information.

        The `entry` argument is not used by this base class, but may be used by child methods.
        """
        self.field_name = name
        self.field_type = field_type
        self.field_nickname = camel_case_to_spaces(nickname) if self.CAMEL_CASE_NICKNAMES else nickname
        self.field_docstring = docstring if docstring else "DOC-TODO"
        self.field_links = []

        if self.field_name_label.var.get() != self.field_nickname:
            self.field_name_label.var.set(self.field_nickname)

        self.update_field_value_display(value)

        self.tooltip.text = f"{self.field_nickname}: {self.field_docstring}"
        self.unhide()

    def _update_field_GameObjectSequence(self, value):
        if self.field_type.count != len(value):
            raise ValueError(
                f"Length of value {value} does not match number of objects in `GameObjectSequence` for field "
                f"{self.field_name}."
            )
        self.field_links = []
        for value_i in value:
            if value_i is not None:
                self.field_links += self.master.get_field_links(self.field_type.game_object_type, value_i)
        valid_count = sum(v is not None for v in value)
        self._set_linked_value_label(f"<{valid_count} entries>", multiple_hint="{MULTIPLE}")

    def _update_field_GameObject(self, value):
        self.field_links = self.master.get_field_links(self.field_type, value)
        self._update_field_int(value)

    def _update_field_IntEnum(self, value):
        self.value_combobox["values"] = [f"{e.value} {camel_case_to_spaces(e.name)}" for e in self.field_type]
        try:
            enum_name = getattr(self.field_type(value), "name")
        except ValueError:
            value_text = f"Unknown: {value}"
        else:
            value_text = f"{value} {camel_case_to_spaces(enum_name)}"
        self.value_combobox.var.set(value_text)
        self._activate_value_widget(self.value_combobox)

    def _update_field_int(self, value):
        self._set_linked_value_label(str(value))

    def _update_field_float(self, value):
        self._set_linked_value_label(f"{value:.3f}")

    def _update_field_bool(self, value):
        if value not in {0, 1}:
            raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
        self.value_checkbutton.var.set(value)
        self.value_checkbutton.config(fg="#3F3" if value else "#F33", text="ON" if value else "OFF")
        self._activate_value_widget(self.value_checkbutton)

    def _update_field_list(self, value):
        """Actual list of values (e.g. draw groups)."""
        # Convert sets (e.g. draw/display/navmesh groups) to sorted lists so empty sets appear pretty.
        value_text = repr(sorted(value)) if not isinstance(value, list) else repr(value)
        self.value_label.var.set(value_text)
        self._activate_value_widget(self.value_label)

    @property
    def field_update_method(self) -> tp.Callable:
        """Returns the appropriate update method for the current field type."""

        # First, look for a method defined for this specific type.
        try:
            field_type_name = self.field_type.__name__
        except AttributeError:
            raise AttributeError(f"Could not detect name of field type {self.field_type}.")
        try:
            return getattr(self, f"_update_field_{field_type_name}")
        except AttributeError:
            pass

        # Try a super-type method.
        if issubclass(self.field_type, str):
            return self._set_linked_value_label
        if issubclass(self.field_type, GameObjectSequence):
            return self._update_field_GameObjectSequence
        if issubclass(self.field_type, GameObject):
            return self._update_field_GameObject
        if issubclass(self.field_type, IntEnum):
            return self._update_field_IntEnum

        raise AttributeError(
            f"Could not find field update method '_update_field_{field_type_name}' or a superclass."
            f"    Field: {self.field_name}")

    def _set_linked_value_label(self, value_text, multiple_hint="{AMBIGUOUS}"):
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

    def _set_field_fg(self, value):
        """Color field text ('fg') depending on whether value is some default that shouldn't draw attention."""
        if issubclass(self.field_type, GameObject):
            self.field_name_label["fg"] = self.master.FIELD_NAME_FG
            self.value_label["fg"] = self.master.FIELD_NAME_FG_GAME_TYPE
        elif self._is_default(self.field_type, value, self.field_nickname):
            self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
            self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
        else:
            self.field_name_label["fg"] = self.master.FIELD_NAME_FG
            self.value_label["fg"] = self.master.FIELD_VALUE_FG

    def hide(self):
        """Called when this row has no field to display (e.g. for smaller ParamTables or unselected entry)."""
        self.row_box.grid_remove()
        self.field_name_box.grid_remove()
        self.field_name_label.grid_remove()
        self.value_box.grid_remove()
        self.active_value_widget.grid_remove()

    def unhide(self):
        self.row_box.grid()
        self.field_name_box.grid()
        self.field_name_label.grid()
        self.value_box.grid()
        self.active_value_widget.grid()

    def build_field_context_menu(self):
        self.context_menu.delete(0, "end")

        if self.field_links:
            for field_link in self.field_links:
                field_link.add_to_context_menu(self.context_menu)

        # Users can enter their own custom integer values for IntEnums.
        if issubclass(self.field_type, IntEnum):
            self.context_menu.add_command(label="Set custom integer value", command=self._set_custom_intenum_value)

    @property
    def editable(self):
        return self.active_value_widget is self.value_label

    def _string_to_GameObjectSequence(self, string):
        try:
            new_value = literal_eval(string)
            if isinstance(new_value, tuple):
                new_value = list(new_value)
            elif not isinstance(new_value, list):
                raise SyntaxError
        except SyntaxError:
            raise ValueError(f"Value of field {self.field_nickname} should be a list of strings or numbers.")
        game_object_type = self.field_type.game_object_type
        for new_value_i in new_value:
            if new_value_i is None:
                continue  # None is valid for any type.
            if issubclass(game_object_type, BaseParam) and not isinstance(new_value_i, int):
                raise ValueError(f"Found non-integer {game_object_type} value in sequence: {new_value_i}")
            elif issubclass(game_object_type, MapEntry) and not isinstance(new_value_i, str):
                raise ValueError(f"Found non-string {game_object_type} name in sequence: {new_value_i}")
        return new_value

    def _string_to_GameObject(self, string):
        # Assume all non-`MapEntry` fields use integers (e.g. `BaseParam`, `Text`).
        if issubclass(self.field_type, MapEntry):
            return string
        else:
            try:
                return int(string)
            except ValueError:
                raise InvalidFieldValueError(
                    f"Value of field {self.field_nickname} must be an integer ({self.field_type})."
                )

    def _string_to_int(self, string):
        if not string.strip("-"):
            return None  # no change
        try:
            return int(string)
        except ValueError:
            raise InvalidFieldValueError(f"Value of field {self.field_nickname} must be an integer.")

    def _string_to_float(self, string):
        if not string.strip("-"):
            return None  # no change
        try:
            return float(string)
        except ValueError:
            raise InvalidFieldValueError(f"Value of field {self.field_nickname} must be a float.")

    def _string_to_list(self, string):
        """At the moment, all elements of `list`-type fields must be integers."""
        try:
            new_value = literal_eval(string)
            if isinstance(new_value, tuple):
                new_value = list(new_value)
            elif not isinstance(new_value, list):
                raise SyntaxError
            if not all(isinstance(i, int) for i in new_value):
                raise SyntaxError
        except (SyntaxError, ValueError):
            raise InvalidFieldValueError(
                f"Value of field {self.field_nickname} must be a list of integers, e.g. [1, 2, 3, ...]"
            )
        return new_value

    @property
    def string_conversion_method(self) -> tp.Callable:
        """Returns the appropriate update method for the current field type."""

        # First, look for a method defined for this specific type.
        try:
            field_type_name = self.field_type.__name__
        except AttributeError:
            raise AttributeError(f"Could not detect name of field type {self.field_type}.")
        try:
            return getattr(self, f"_string_to_{field_type_name}")
        except AttributeError:
            pass

        # Try a super-type method.
        if issubclass(self.field_type, str):
            return lambda value: value
        if issubclass(self.field_type, GameObjectSequence):
            return self._string_to_GameObjectSequence
        if issubclass(self.field_type, GameObject):
            return self._string_to_GameObject
        if issubclass(self.field_type, IntEnum):
            raise NotImplementedError

        raise AttributeError(f"Could not find field update method '_string_to_{field_type_name}' or a superclass.")

    def update_field_value_display(self, new_value):
        """Updates field value and display/option properties related to it."""
        self.field_update_method(new_value)
        self._set_field_fg(new_value)
        self.link_missing = self.field_links and not any(link.name for link in self.field_links)
        self.build_field_context_menu()

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        if not self._active and value:
            self._active = True
        elif self._active and not value:
            self._active = False
        else:
            return  # No change to active state.

        # All widget backgrounds need updating (except Combobox).
        self._update_colors()

    @property
    def link_missing(self):
        return self._link_missing

    @link_missing.setter
    def link_missing(self, value: bool):
        if value and not self._link_missing:
            self._link_missing = True
            self._update_colors()
        elif not value and self._link_missing:
            self._link_missing = False
            self._update_colors()

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (
            self.row_box,
            self.field_name_box,
            self.field_name_label,
            self.value_box,
            self.value_label,
            self.value_checkbutton,
        ):
            widget["bg"] = bg_color

    def _get_color(self):
        """Inspects field name/data and returns an RGB string."""
        base_bg = int(self.STYLE_DEFAULTS["bg"].lstrip("#"))  # dark grey
        if self.link_missing:
            base_bg += 100
        if self._active:
            base_bg += 123
        if self.row_index % 2:
            base_bg += 111
        return f"#{base_bg}"

    def _set_custom_intenum_value(self):
        new_value = NumberEditBox(
            self.master, window_title=f"New value for {self.field_nickname}", integers_only=True,
        ).go()
        if new_value is None:
            return
        field_changed = self.master.change_field_value(self.field_name, new_value)
        if field_changed:
            self.update_field_value_display(new_value)

    def _is_default(self, field_type, value, field_nickname=""):
        return False


class BaseFieldEditor(BaseEditor, abc.ABC):
    FIELD_CANVAS_BG = "#1d1d1d"
    FIELD_BOX_WIDTH = 450
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_HEIGHT = 50
    FIELD_NAME_WIDTH = 30
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 50
    FIELD_ROW_COUNT = 0  # must be set in child
    FIELD_NAME_FG = "#DDE"
    FIELD_NAME_FG_GAME_TYPE = "#ADA"
    FIELD_NAME_FG_DEFAULT = "#777"
    FIELD_VALUE_FG = "#FFF"
    FIELD_VALUE_FG_DEFAULT = "#777"

    FIELD_ROW_CLASS = FieldRow
    field_rows: list[FieldRow]

    def __init__(
        self,
        project: GameDirectoryProject,
        linker: WindowLinker,
        master=None,
        toplevel=False,
        window_title="Soulstruct Editor",
    ):
        if self.FIELD_ROW_COUNT == 0:
            raise AttributeError("Class attribute `FIELD_ROW_COUNT` must be set by child of SoulstructBaseFieldEditor.")
        self.show_hidden_fields = None
        self.field_canvas = None
        self.field_i_frame = None
        self.e_field_value_edit = None
        self.selected_field_row_index = None
        self.displayed_field_count = 0
        self.field_rows = []
        super().__init__(project=project, linker=linker, master=master, toplevel=toplevel, window_title=window_title)

    def build(self):
        """Builds category, entry, and field tables."""
        with self.set_master(sticky="nsew", row_weights=[1], column_weights=[0, 1], auto_columns=0):
            self.build_category_canvas()
            with self.set_master(sticky="nsew", row_weights=[0, 1, 0], column_weights=[1, 1]):
                self.build_previous_range_button(row=0, column=0)
                self.build_hidden_fields_checkbutton(row=0, column=1)
                with self.set_master(sticky="nsew", row=1, column=0, row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                with self.set_master(sticky="nsew", row=1, column=1, row_weights=[1], column_weights=[1]):
                    self.build_field_frame()
                self.build_next_range_button(row=2, column=0)

    def build_hidden_fields_checkbutton(self, **kwargs):
        self.show_hidden_fields = self.Checkbutton(
            label="Show hidden fields",
            initial_state=False,
            command=lambda: self.refresh_fields(reset_display=True),
            pady=10,
            **kwargs,
        ).var

    def build_field_frame(self):
        self.field_canvas = self.Canvas(
            yscrollincrement=self.FIELD_ROW_HEIGHT,
            vertical_scrollbar=True,
            horizontal_scrollbar=True,
            borderwidth=10,
            highlightthickness=0,
            bg=self.FIELD_CANVAS_BG,
            sticky="nsew",
            row_weights=[1],
            column_weights=[1],
        )
        self.field_i_frame = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH, sticky="nsew")
        self.field_i_frame.bind("<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))
        self.field_canvas.create_window(0, 0, window=self.field_i_frame, anchor="nw")

        with self.set_master(self.field_i_frame):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(
                    self.FIELD_ROW_CLASS(
                        self,
                        row_index=row,
                        main_bindings={
                            "<Button-1>": lambda _, i=row: self.select_displayed_field_row(i),
                            "<Button-3>": lambda e, i=row: self._right_click_field(e, i),
                            "<Up>": self._field_press_up,
                            "<Down>": self._field_press_down,
                        },
                    )
                )

    def select_category(
        self, selected_category: tp.Optional[str], first_display_index=0, auto_scroll=False, view_change=False
    ):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        """
        old_category = self.active_category

        if old_category is not None:
            selected_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.remembered_ids[old_category] = selected_entry_id

        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box["bg"] = self.CATEGORY_SELECTED_BG
                    label["bg"] = self.CATEGORY_SELECTED_BG
                    label.focus_set()
                else:
                    box["bg"] = self.CATEGORY_UNSELECTED_BG
                    label["bg"] = self.CATEGORY_UNSELECTED_BG

        if auto_scroll:
            view_ratio = list(self.category_boxes).index(self.active_category) / (len(self.category_boxes) + 1)
            self.category_canvas.yview_moveto(view_ratio)

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries(reset_field_display=True)  # TODO: this argument is the only difference. Better way?
        last_selected_entry_id = self.remembered_ids.get(self.active_category, None)
        if last_selected_entry_id is not None:
            try:
                self.select_entry_id(last_selected_entry_id, edit_if_already_selected=False)
            except ValueError:
                self.remembered_ids.pop(self.active_category)  # entry ID is invalid
                self.entry_canvas.yview_moveto(0)
        else:
            # Leave no entry selected.
            self.entry_canvas.yview_moveto(0)

        if view_change and old_category is not None:
            self.view_history.record_view_change(
                back=lambda: self.select_category(old_category), forward=lambda: self.select_category(selected_category)
            )

    def refresh_entries(self, reset_field_display=False):
        super().refresh_entries()
        self.refresh_fields(reset_display=reset_field_display)

    def select_entry_row_index(
        self, row_index, set_focus_to_text=True, edit_if_already_selected=True, id_clicked=False, view_change=False
    ):
        super().select_entry_row_index(
            row_index,
            set_focus_to_text=set_focus_to_text,
            edit_if_already_selected=edit_if_already_selected,
            id_clicked=id_clicked,
            view_change=view_change,
        )
        self.refresh_fields()

        # `refresh_fields()` seems to steal focus aggressively, so end by setting it back to entry name.
        if row_index is not None and set_focus_to_text:
            self.entry_rows[row_index].text_label.focus_set()

    def refresh_fields(self, reset_display=False):
        """Refresh all field information."""
        field_dict = self.get_selected_field_dict()

        self._cancel_field_value_edit()

        show_hidden_fields = self.show_hidden_fields.get()

        row = 0
        for field_name in self.get_field_names(field_dict):

            try:
                field_nickname, is_main, field_type, field_doc = self.get_field_display_info(field_dict, field_name)
            except ValueError as e:
                raise ValueError(f"Could not get field information for field {field_name}. Error: {str(e)}")

            if not is_main and not show_hidden_fields:
                continue  # skip hidden field

            try:
                field_value = field_dict[field_name]
            except KeyError:
                # Only some DSR-specific fields are allowed to be absent.
                if field_doc.startswith("<DSR>"):
                    continue
                raise

            if not isinstance(field_type, type):
                raise TypeError(
                    f"`field_type` of field {field_name} must be a type at this point, not: {repr(field_type)}"
                )

            self.field_rows[row].update_field(
                name=field_name, nickname=field_nickname, value=field_value, field_type=field_type, docstring=field_doc
            )
            row += 1

        self.displayed_field_count = row

        for remaining_row in range(row, len(self.field_rows)):
            self.field_rows[remaining_row].hide()

        self.field_i_frame.grid_columnconfigure(1, weight=1)

        if reset_display:
            self.select_displayed_field_row(0, edit_if_already_selected=False)
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def _add_entry(self, entry_id: int, text: str, category=None, new_field_dict=None):
        """Requires additional field_dict argument."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        if entry_id < 0:
            self.CustomDialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_data():
            self.CustomDialog(
                title="Entry ID Error",
                message=f"Entry ID {entry_id} already exists in category {camel_case_to_spaces(self.active_category)}.",
            )
            return False

        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        self.get_category_data()[entry_id] = new_field_dict  # add entry to category dictionary
        self._set_entry_text(entry_id, text)
        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

        # TODO
        # if from_history:
        #     self.jump_to_category_and_entry(category, text_id)
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._delete_entry, category, text_id),
        #         redo=partial(self._add_entry, category, text_id, text),
        #     )
        # self.unsaved_changes.add((self.active_category, text_id, 'add'))

        return True

    def add_relative_entry(self, entry_id, offset=1, text=None):
        """Copies field dict of base entry."""
        if text is None:
            text = self.get_entry_text(entry_id)  # Copies name of origin entry by default (can be overridden).
        new_field_dict = self.get_field_dict(entry_id).copy()
        self._add_entry(entry_id=entry_id + offset, text=text, new_field_dict=new_field_dict)

    def add_entry_to_next_available_id(self, entry_id, text=None):
        """Find next available entry ID after `entry_id`."""
        entry_ids = set(self.get_category_data())
        new_id = entry_id + 1
        while new_id in entry_ids:
            new_id += 1
        self.add_relative_entry(entry_id, offset=new_id - entry_id, text=text)

    def _right_click_field(self, event, field_index):
        self.select_displayed_field_row(field_index, edit_if_already_selected=False)
        self.field_rows[field_index].context_menu.tk_popup(event.x_root, event.y_root)

    def select_field_name(self, field_name, set_focus_to_value=True, edit_if_already_selected=False, auto_scroll=True):
        row_index = self.get_field_row_index_from_name(field_name)
        self.select_displayed_field_row(
            row_index, set_focus_to_value=set_focus_to_value, edit_if_already_selected=edit_if_already_selected
        )
        self.refresh_fields()

        self.field_canvas.yview_moveto(0)
        if auto_scroll:
            self.field_canvas.yview_scroll(row_index, "units")

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index)
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

    def _field_press_up(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(-1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[1] != 1.0 or self.selected_field_row_index < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, "units")

    def _field_press_down(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(+1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[0] != 0.0 or self.selected_field_row_index > 5:
                self.field_canvas.yview_scroll(1, "units")

    def _shift_selected_field(self, relative_index):
        if (
            self.selected_field_row_index is None
            or not 0 <= self.selected_field_row_index + relative_index < self.displayed_field_count
        ):
            return
        self.select_displayed_field_row(self.selected_field_row_index + relative_index)

    def _get_field_edit_widget(self, row_index):
        """Create and return `Entry` widget for editing a field value.

        Should not be called for "(select to edit)" field types (`GameObjectSequence`).
        """
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.active_row_index))[field_row.field_name]
        initial_text = repr(sorted(field_value)) if issubclass(field_type, list) else str(field_value)
        return self.Entry(
            field_row.value_box,
            initial_text=initial_text,
            integers_only=field_type == int,
            numbers_only=field_type == float,
            sticky="ew",
            width=5,
        )

    def _start_field_value_edit(self, row_index):
        if not self.e_field_value_edit:
            self.e_field_value_edit = self._get_field_edit_widget(row_index)
            if not self.e_field_value_edit:
                return  # Edit attempt was rejected.
            self.e_field_value_edit.bind("<Return>", lambda e, i=row_index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind("<Up>", self._field_press_up)  # confirms edit
            self.e_field_value_edit.bind("<Down>", self._field_press_down)  # confirms edit
            self.e_field_value_edit.bind("<FocusOut>", lambda e, i=row_index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind("<Escape>", lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.focus_set()
            self.e_field_value_edit.select_range(0, "end")

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None

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
        """New value should have already been converted to its appropriate type."""
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            field_dict[field_name] = new_value
        except InvalidFieldValueError as e:
            _LOGGER.error(f"Invalid value {new_value} for field {field_name}. Error: {str(e)}")
            self.bell()
            self.CustomDialog(title="Field Value Error", message=str(e))
            return False
        return True

    def get_field_row_index_from_name(self, field_name):
        for row in self.field_rows:
            if row.field_name == field_name:
                return row.row_index
        raise KeyError(f"Field name {field_name} does not exist in active category/entry.")

    def get_selected_field_dict(self):
        """Returns None if no field is selected."""
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            return self.get_field_dict(entry_id)
        else:
            return None

    @abc.abstractmethod
    def get_field_dict(self, entry_id: int, category=None):
        raise NotImplementedError

    @abc.abstractmethod
    def get_field_names(self, field_dict):
        raise NotImplementedError

    @abc.abstractmethod
    def get_field_display_info(self, field_dict, field_name):
        """This method should return the full field information dictionary if field_name is None."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        raise NotImplementedError
