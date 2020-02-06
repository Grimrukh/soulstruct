from __future__ import annotations

import re
from typing import TYPE_CHECKING

from soulstruct.project.editor import SoulstructBaseEditor

if TYPE_CHECKING:
    from soulstruct.text import DarkSoulsText


class SoulstructTextEditor(SoulstructBaseEditor):
    DATA_NAME = "Text"
    TAB_NAME = "text"
    CATEGORY_BOX_WIDTH = 165
    CATEGORY_BOX_HEIGHT = 400
    ENTRY_BOX_WIDTH = 870
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 100

    class EntryRow(SoulstructBaseEditor.EntryRow):
        _MATCH_ITEM = re.compile(r'^(Weapon|Armor|Ring|Good|Spell)(Names|Summaries|Descriptions)$')

        def build_entry_context_menu(self):
            super().build_entry_context_menu()
            text_id = self.entry_id

            item_match = self._MATCH_ITEM.match(self.master.active_category)
            if item_match:
                item_type, text_type = item_match.group(1, 2)

                # Category shortcuts.
                separator_added = False
                text_categories = ('Names', 'Summaries', 'Descriptions')
                linked_id = ((text_id // 100) * 100) if item_type != 'Ring' else text_id
                for link_category in text_categories:
                    if text_type != link_category and linked_id in self.master.Text[item_type + link_category]:
                        if not separator_added:
                            self.context_menu.add_separator()
                            separator_added = True
                        self.context_menu.add_command(
                            label=f"Go to Text.{item_type}{link_category}[{linked_id}]",
                            foreground=self.STYLE_DEFAULTS['text_fg'],
                            command=lambda it=item_type, lc=link_category, i=linked_id: self.master.linker.text_link(
                                it + lc, i))

                # Param shortcut.
                self.context_menu.add_separator()
                param_category = item_type + ('s' if item_type != 'Armor' else '')
                self.context_menu.add_command(
                    label=f"Go to Params.{param_category}[{linked_id}]",
                    foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=param_category, i=linked_id: self.master.linker.params_link(c, i))

                # Automatic upgrade text generation.
                if item_type == 'Weapon' and text_type == 'Names' and text_id % 100 == 0:
                    self.context_menu.add_separator()
                    for count in (5, 10, 15):
                        self.context_menu.add_command(
                            label=f"Create weapon upgrade names (+{count})", foreground=self.STYLE_DEFAULTS['text_fg'],
                            command=lambda i=text_id: self.master.create_upgrade_entries(i, count=count))
                elif item_type == 'Armor' and text_type == 'Names' and text_id % 100 == 0:
                    self.context_menu.add_separator()
                    for count in (5, 10):
                        self.context_menu.add_command(
                            label=f"Create armor upgrade names (+{count})", foreground=self.STYLE_DEFAULTS['text_fg'],
                            command=lambda i=text_id: self.master.create_upgrade_entries(i, count=count))

    def __init__(self, text: DarkSoulsText, linker, master=None, toplevel=False):
        self.Text = text
        self.show_all_categories = None
        self.find_text_id_entry = None
        self.find_text_string_entry = None
        self.replace_text_string_entry = None
        super().__init__(linker, master, toplevel, window_title="Soulstruct Text Editor")

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[0, 1, 1, 1], auto_columns=0):

                self.show_all_categories = self.Checkbutton(
                    label='Show internal categories ', initial_state=False, command=self.refresh_categories,
                    padx=10).var

                self.find_text_id_entry = self.Entry(
                    label="Find ID:", label_position='left', width=10, padx=10)
                self.current_frame.columnconfigure(1, minsize=150)
                self.find_text_id_entry.bind('<Return>', self.find_text_id)
                self.find_text_string_entry = self.Entry(
                    label="Find Text:", label_position='left', width=18, padx=10, sticky='e')
                self.find_text_string_entry.bind('<Return>', lambda e: self.find_text_string())
                self.replace_text_string_entry = self.Entry(
                    label="Replace With:", label_position='left', width=18, padx=10, sticky='e')
                self.replace_text_string_entry.bind('<Return>', lambda e: self.find_text_string(replace=True))

            super().build()

    def create_upgrade_entries(self, base_text_id, count, category=None):
        if category is None:
            category = self.active_category

        text_dict = self.Text[category]
        if base_text_id % 100 != 0:
            self.CustomDialog(
                title="Invalid Base ID for Upgrades",
                message=f"The base text ID for weapons or armor should be a multiple of 100.")
            return
        if any(base_text_id + i in text_dict for i in range(1, count + 1)):
            if self.CustomDialog(
                    title="Upgrade IDs already exist",
                    message=f"Overwrite all existing entries in ID range "
                            f"{base_text_id + 1} to {base_text_id + count}?",
                    button_names=('Yes, overwrite them', 'No, go back'),
                    button_kwargs=('YES', 'NO'),
                    cancel_output=1, default_output=1) == 1:
                return
        base_text = text_dict[base_text_id]
        undo_bulk = []
        redo_bulk = []
        for i in range(1, count + 1):
            new_text = f'{base_text}+{i}'
            if base_text_id + i in text_dict:
                old_text = text_dict[base_text_id + i]
                undo_bulk.append((category, base_text_id + i, old_text, 'change'))
                redo_bulk.append((category, base_text_id + i, new_text, 'change'))
            else:
                undo_bulk.append((category, base_text_id + i, None, 'delete'))
                redo_bulk.append((category, base_text_id + i, new_text, 'add'))
            text_dict[base_text_id + i] = new_text

        # TODO: History action manager. Will need linker access.
        # self.action_history.record_action(
        #     undo=partial(self.bulk_action, *undo_bulk, jump_to_category=category, jump_to_text_id=base_text_id),
        #     redo=partial(self.bulk_action, *redo_bulk, jump_to_category=category, jump_to_text_id=base_text_id),
        # )

        self.refresh_entries()

    def find_text_id(self, _=None):
        try:
            id_to_find = int(self.find_text_id_entry.var.get())
            if id_to_find < 0:
                raise ValueError
        except ValueError:
            self.CustomDialog(
                title="Value Error",
                message=f"Invalid text ID: {self.find_text_id_entry.var.get()}.\n\n"
                        f"The ID must be an integer (zero or greater).")
            return
        if self.active_category and id_to_find in self.Text[self.active_category]:
            row_index = self._update_first_entry_display_index(self.get_entry_index(id_to_find))
            self.refresh_entries()
            self.select_entry_row_index(row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(0)
        else:
            self.flash_bg(self.find_text_id_entry)

    def find_text_string(self, replace=False):
        text = self.find_text_string_entry.var.get()
        text_id_list = sorted(self.get_category_data())
        if not text_id_list:
            self.flash_bg(self.replace_text_string_entry if replace else self.find_text_string_entry)
            return
        text_id_selected = self.get_entry_id(self.active_row_index) if self.active_row_index is not None else -1
        first_index = None
        for i, text_id in enumerate(text_id_list):
            if text in self.get_entry_text(text_id):
                if text_id > text_id_selected:  # also works if text_id_selected == -1
                    next_index = i
                    break
                elif text_id != text_id_selected and first_index is None:
                    first_index = i
        else:
            next_index = first_index

        if text_id_selected >= 0 and replace and text in self.get_entry_text(text_id_selected):
            to_replace = self.replace_text_string_entry.var.get()
            new_text = self.active_category[text_id_selected].replace(text, to_replace)
            self.change_entry_text(text_id_selected, new_text)

        if next_index is not None:
            row_index = self._update_first_entry_display_index(next_index)
            self.refresh_entries()
            self.select_entry_row_index(row_index, set_focus_to_text=False, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(0)
        else:
            self.flash_bg(self.replace_text_string_entry if replace else self.find_text_string_entry)

    def _get_display_categories(self):
        return self.Text.all_categories if self.show_all_categories.get() else self.Text.main_categories

    def get_category_data(self, category=None) -> dict:
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        return self.Text[category]

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.Text.get_range(category, self.first_display_index, self.first_display_index + self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in text category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No text category selected.")
        if entry_id not in self.Text[category]:
            raise ValueError(f"Text ID {entry_id} does not appear in category {category}.")
        return sorted(self.Text[category]).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No text category selected.")
        return self.Text[category][entry_id]

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        entry_text = self.Text[category].pop(entry_id)
        self.Text[category][new_id] = entry_text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(new_id, entry_text)

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No text category selected.")
        self.Text[category][entry_id] = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text)
