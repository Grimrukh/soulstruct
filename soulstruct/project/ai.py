from __future__ import annotations

import re
import tkinter as tk
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List

from soulstruct.ai import DARK_SOULS_AI_BND_NAMES
from soulstruct.ai.core import LuaError
from soulstruct.project.editor import SoulstructBaseEditor
from soulstruct.project.utilities import bind_events
from soulstruct.utilities import camel_case_to_spaces

if TYPE_CHECKING:
    from soulstruct.ai import DarkSoulsAIScripts, LuaBND, LuaGoal


class AIScriptTextEditor(tk.Text):

    SYNTAX_RE = {
        "restart_type": (r"^@[\w_]+", (0, 0)),
        "event_def": (r"^def [\w\d_]+", (0, 0)),
        "docstring": (r"^[ ]+\"\"\" [\w\d :]+ \"\"\"", (0, 0)),
        "instruction": (r"^[ ]+[\w\d_]+", (0, 0)),
        "low_level_test": (r"^[ ]+(If|Skip|Goto)[\w\d_]+", (0, 0)),
        "named_arg": (r"[(,=][ ]*(?!False)(?!True)[A-z][\w\d.]*[ ]*[,)]", (1, 1)),
        "func_arg_name": (r"[\w\d_]+[ ]*(?=\=)", (0, 0)),
    }

    re.compile(r"(?<=[,(])[ ]+\w[\w\d.]+[ ]+(?=[,)])")

    def __init__(self, *args, **kwargs):
        """Text widget that generates a "<CursorChange>" event when appropriate for event bindings and can highlight
        arbitrary text patterns.

        See:
            https://stackoverflow.com/a/23574537
            https://stackoverflow.com/a/3781773
        """
        super().__init__(*args, **kwargs)
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        # self.tag_configure("restart_type", foreground='#FFFFAA')
        # self.tag_configure("event_def", foreground='#FFAAAA')
        # self.tag_configure("docstring", foreground='#BBBBBB')
        # self.tag_configure("instruction", foreground='#AAAAFF')
        # self.tag_configure("low_level_test", foreground='#AAFFAA')  # starts with 'If', 'Skip', or 'Goto'
        # self.tag_configure("named_arg", foreground='#AAFFFF')
        # self.tag_configure("func_arg_name", foreground='#FFCCAA')
        # self.tag_configure("event_arg_name", foreground='#FFAAFF')
        #
        # self.tag_configure("found", background='#224433')
        # self.tag_configure("error", background='#443322')

    def _proxy(self, *args):
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)
        if args[0] in ("insert", "delete") or args[0:3] == ("mark", "set", "insert"):
            self.event_generate("<<CursorChange>>", when="tail")

        return result

    def highlight_line(self, number, tag):
        """Apply the given tag to all text in the given line. Clears tag first."""
        self.tag_remove(tag, "1.0", "end")
        self.tag_add(tag, f"{number}.0 linestart", f"{number}.0 lineend")

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False, clear=True,
                          start_offset=0, end_offset=0):
        """Apply the given tag to all text that matches the given pattern. Clears tag first by default.

        If 'regexp' is set to True, pattern will be treated as a regular expression according to Tcl's regular
        expression syntax.
        """
        if clear:
            self.tag_remove(tag, "1.0", "end")
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while 1:
            index = self.search(pattern, index="matchEnd", stopindex="searchLimit", count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", f"{index}+{start_offset}c")
            self.mark_set("matchEnd", f"{index}+{count.get() - end_offset}c")
            self.tag_add(tag, "matchStart", "matchEnd")

    def color_syntax(self):
        for tag, (pattern, offsets) in self.SYNTAX_RE.items():
            self.highlight_pattern(pattern, tag, regexp=True, clear=True,
                                   start_offset=offsets[0], end_offset=offsets[1])


class SoulstructAIEditor(SoulstructBaseEditor):
    CATEGORY_BOX_WIDTH = 0
    ENTRY_BOX_WIDTH = 150
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 200

    class EntryRow(SoulstructBaseEditor.EntryRow):
        """Container/manager for widgets of a single entry row in the Editor."""
        ENTRY_ANCHOR = 'center'
        ENTRY_ROW_HEIGHT = 30
        EDIT_ENTRY_ID = True
        ENTRY_TYPE_WIDTH = 5
        ENTRY_TYPE_FG = '#FFA'
        ENTRY_ID_WIDTH = 12
        ENTRY_ID_FG = '#CDF'
        ENTRY_TEXT_WIDTH = 40
        ENTRY_TEXT_FG = '#FFF'

        def __init__(self, editor: SoulstructAIEditor, row_index: int, main_bindings: dict = None):
            self.master = editor
            self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

            self.row_index = row_index
            self._entry_id = None
            self._entry_text = None
            self._active = False
            self._logic = False

            bg_color = self._get_color()

            self.row_box = editor.Frame(
                width=self.ENTRY_TYPE_WIDTH + self.ENTRY_ID_WIDTH + self.ENTRY_TEXT_WIDTH, height=self.ENTRY_ROW_HEIGHT,
                bg=bg_color, row=row_index, columnspan=3, sticky='nsew')
            bind_events(self.row_box, main_bindings)

            self.type_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky='ew')
            self.type_label = editor.Label(
                self.type_box, text='B', width=self.ENTRY_TYPE_WIDTH, bg=bg_color, fg="#F33", font_size=11,
                sticky='ew')
            type_bindings = main_bindings.copy()
            type_bindings['<Button-1>'] = lambda _, i=row_index: self.master.toggle_entry_logic_state(i)
            bind_events(self.type_box, type_bindings)
            bind_events(self.type_label, type_bindings)

            self.id_box = editor.Frame(row=row_index, column=1, bg=bg_color, sticky='ew')
            self.id_label = editor.Label(
                self.id_box, text='', width=self.ENTRY_ID_WIDTH, bg=bg_color, fg=self.ENTRY_ID_FG, font_size=11,
                sticky='e')
            id_bindings = main_bindings.copy()
            id_bindings['<Button-1>'] = lambda _, i=row_index: self.master.select_entry_row_index(
                i, id_clicked=True)
            id_bindings['<Shift-Button-1>'] = lambda _, i=row_index: self.master.popout_entry_id_edit(i)
            bind_events(self.id_box, id_bindings)
            bind_events(self.id_label, id_bindings)

            self.text_box = editor.Frame(row=row_index, column=2, bg=bg_color, sticky='ew')
            bind_events(self.text_box, main_bindings)

            self.text_label = editor.Label(
                self.text_box, text='', bg=bg_color, fg=self.ENTRY_TEXT_FG, anchor='w', font_size=11,
                justify='left', width=self.ENTRY_TEXT_WIDTH)
            bind_events(self.text_label, main_bindings)

            self.context_menu = editor.Menu(self.row_box)

            self.tool_tip = None

        def update_entry(self, entry_id: int, entry_text: str, logic_state: bool = None):
            self.entry_id = entry_id
            self.entry_text = entry_text
            if logic_state is None:
                raise ValueError("Logic state cannot be None (suggests design problem).")
            self.logic = logic_state
            self._update_colors()
            self.build_entry_context_menu()

        def hide(self):
            """Called when this row has no entry to display."""
            self.row_box.grid_remove()
            self.type_box.grid_remove()
            self.type_label.grid_remove()
            self.id_box.grid_remove()
            self.id_label.grid_remove()
            self.text_box.grid_remove()
            self.text_label.grid_remove()

        def unhide(self):
            self.row_box.grid()
            self.type_box.grid()
            self.type_label.grid()
            self.id_box.grid()
            self.id_label.grid()
            self.text_box.grid()
            self.text_label.grid()

        def build_entry_context_menu(self):
            self.context_menu.delete(0, 'end')
            self.context_menu.add_command(
                label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.add_relative_entry(self.entry_id, logic_state=self.logic, offset=1))
            self.context_menu.add_command(
                label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.delete_entry(self.row_index))

        def _update_colors(self):
            bg_color = self._get_color()
            for widget in (self.row_box, self.id_box, self.id_label, self.text_box, self.text_label,
                           self.type_box, self.type_label):
                widget['bg'] = bg_color

        def toggle_logic(self):
            self.logic = not self.logic

        @property
        def logic(self):
            return self.type_label.var.get() == "L"

        @logic.setter
        def logic(self, enabled: bool):
            if self.logic and not enabled:
                self.type_label.var.set("B")
                self.type_label['fg'] = '#F33'
            elif not self.logic and enabled:
                self.type_label.var.set("L")
                self.type_label['fg'] = '#3F3'

    entry_rows: List[SoulstructAIEditor.EntryRow]

    def __init__(self, ai: DarkSoulsAIScripts, linker, script_directory, game_root, master=None, toplevel=False):
        self.AI = ai
        self.script_directory = Path(script_directory)
        self.game_root = Path(game_root)
        self.e_coord = None
        self.bnd_choice = None
        self.has_battle_interrupt = None
        self.logic_interrupt = None
        self.set_logic_interrupt_button = None
        self.text_editor = None
        self.compile_button = None
        self.decompile_button = None
        super().__init__(linker=linker, master=master, toplevel=toplevel, window_title="Soulstruct AI Script Editor")

    def refresh_categories(self):
        return

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[2, 1, 0, 2, 1], auto_columns=0):
                bnd_display_names = [f"{camel_case_to_spaces(v)} ({k})" for k, v in DARK_SOULS_AI_BND_NAMES.items()]
                self.bnd_choice = self.Combobox(
                    values=bnd_display_names, label='Map:', label_font_size=12, label_position='left', width=25,
                    font=('Segoe UI', 12), on_select_function=self._on_bnd_choice, sticky='w', padx=10).var
                self.Label(text="Has Battle Interrupt", padx=(15, 0))
                self.has_battle_interrupt = self.Checkbutton(
                    command=self.set_battle_interrupt, selectcolor='#000', fg="#FFF")
                self.logic_interrupt = self.Entry(width=30, padx=(15, 0))
                self.set_logic_interrupt_button = self.Button(
                    text="Set Logic Interrupt", width=20, command=self.set_logic_interrupt_name, padx=5)

            with self.set_master(sticky='nsew', row_weights=[1], column_weights=[2, 1], auto_columns=0):
                with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1],
                                     padx=50, pady=10, auto_rows=0):
                    with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1, 1], pady=5, auto_columns=0):
                        self.compile_button = self.Button(
                            text="Compile", fg="#422", width=15, padx=5, command=self.compile_selected)
                        self.decompile_button = self.Button(
                            text="Decompile", fg="#422", width=15, padx=5, command=self.decompile_selected)
                    self.build_script_editor()

    def build_script_editor(self):
        self.script_editor_canvas = self.Canvas(
            horizontal_scrollbar=True, sticky='nsew', bg='#232323',
            borderwidth=0, highlightthickness=0, column=0, row_weights=[1], column_weights=[1])
        editor_i_frame = self.Frame(self.script_editor_canvas, sticky='nsew', row_weights=[1], column_weights=[1])
        self.script_editor_canvas.create_window(0, 0, window=editor_i_frame, anchor='nw')

        self.text_editor = self.CustomWidget(
            editor_i_frame, custom_widget_class=AIScriptTextEditor, set_style_defaults=('text', 'cursor'),
            width=300, height=50, wrap='word', bg='#232323', font=("Consolas", 10))
        vertical_scrollbar_w = self.Scrollbar(
            orient='vertical', command=self.text_editor.yview, column=1, sticky='ns')
        self.text_editor.config(bd=0, yscrollcommand=vertical_scrollbar_w.set)
        self.link_to_scrollable(self.text_editor, editor_i_frame)

        def _update_textbox_height(e):
            font_size = int(self.text_editor['font'].split()[1])
            self.text_editor['height'] = e.height // (font_size * 1.5)  # 1.5 line spacing

        self.script_editor_canvas.bind("<Configure>", lambda e: _update_textbox_height(e))

        # self.text_editor.bind("<<CursorChange>>", self._update_line_number)
        # self.text_editor.bind("<Control-f>", self._control_f_search)

    def set_battle_interrupt(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            self.get_category_dict()[entry_id, logic_state].has_battle_interrupt = self.has_battle_interrupt.var.get()

    def set_logic_interrupt_name(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            self.get_category_dict()[entry_id, logic_state].logic_interrupt_name = self.logic_interrupt.var.get()

    def toggle_entry_logic_state(self, row_index):
        entry_id = self.get_entry_id(row_index)
        old_logic_state = self.entry_rows[row_index].type_label.var.get() == "L"
        new_logic_state = not old_logic_state
        if (entry_id, new_logic_state) in self.get_category_dict():
            self.dialog("Script Type Error", f"A {'logic' if new_logic_state else 'battle'} script already exists for "
                                             f"goal ID {entry_id}.")
            return
        goal = self.get_category_dict()[entry_id, old_logic_state]
        goal.has_logic_interrupt = new_logic_state
        self.entry_rows[row_index].logic = new_logic_state
        self.logic_interrupt['state'] = 'normal' if new_logic_state else 'disabled'
        self.set_logic_interrupt_button['state'] = 'normal' if new_logic_state else 'disabled'

    def compile_selected(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
            try:
                goal.compile(x64=self.get_selected_bnd().is_lua_64)
                self.decompile_button['state'] = 'normal'
            except LuaError as e:
                self.dialog("Lua Compile Error", f"Error encountered while compiling script:\n\n{str(e)}")

    def decompile_selected(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
            if goal.script:
                if self.dialog(title="Overwrite Script?",
                               message="Overwrite existing decompiled script?",
                               button_names=("Yes, overwrite", "No, do nothing"),
                               button_kwargs=('YES', 'NO'),
                               cancel_output=1, default_output=1) == 1:
                    return
            try:
                goal.decompile()
                self.compile_button['state'] = 'normal'
            except LuaError as e:
                self.dialog("Lua Decompile Error", f"Error encountered while decompiling script:\n\n{str(e)}")

    def write_selected(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
            try:
                goal.write_decompiled(self.script_directory / goal.script_name)
            except LuaError as e:
                self.dialog("Lua Write Error", f"Error encountered while writing script:\n\n{str(e)}")

    def load_selected(self):
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
            try:
                goal.load_decompiled(self.script_directory / goal.script_name)
            except FileNotFoundError:
                self.dialog("Lua Read Error", "Decompiled script not found in '{project}/ai_scripts' directory.")

    def refresh_entries(self):
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range(
            first_index=self.first_display_index,
            last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id, logic_state in entries_to_display:
            self.entry_rows[row].update_entry(
                entry_id, self.get_entry_text(entry_id, logic_state=logic_state), logic_state=logic_state)
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].hide()

        self.entry_i_frame.columnconfigure(0, weight=1)
        self.entry_i_frame.columnconfigure(1, weight=1)
        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_buttons()

    def select_entry_id(self, entry_id, logic_state=None, set_focus_to_text=True, edit_if_already_selected=True):
        """Select entry based on ID and set the category display range to target_row_index rows before it."""
        entry_index = self.get_entry_index(entry_id, logic_state=logic_state)
        self.refresh_entries()
        self.select_entry_row_index(
            entry_index, set_focus_to_text=set_focus_to_text, edit_if_already_selected=edit_if_already_selected)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False):
        """Select entry from row index, based on currently displayed category and ID range."""
        old_row_index = self.active_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected:
                    if id_clicked:
                        return self._start_entry_id_edit(row_index)
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
            logic_state = self.get_entry_logic_state()
            goal = self.get_category_dict()[self.get_entry_id(self.active_row_index), logic_state]
            if goal.has_logic_interrupt:
                self.logic_interrupt['state'] = 'normal'
                self.logic_interrupt.var.set(goal.logic_interrupt_name)
                self.set_logic_interrupt_button['state'] = 'normal'
            else:
                self.logic_interrupt.var.set("")
                self.logic_interrupt['state'] = 'disabled'
                self.set_logic_interrupt_button['state'] = 'disabled'
            self.compile_button['state'] = 'normal' if goal.script else 'disabled'
            self.decompile_button['state'] = 'normal' if goal.bytecode else 'disabled'
            self.has_battle_interrupt['state'] = 'normal'
            self.has_battle_interrupt.var.set(goal.has_battle_interrupt)
            self.update_script_text(goal)
        else:
            # No entry is selected.
            self.has_battle_interrupt.var.set(False)
            self.has_battle_interrupt['state'] = 'disabled'
            self.logic_interrupt.var.set("")
            self.logic_interrupt['state'] = 'disabled'
            self.set_logic_interrupt_button['state'] = 'disabled'
            self.text_editor.delete(1.0, 'end')

    def update_script_text(self, goal):
        self.text_editor.delete(1.0, 'end')
        self.text_editor.insert(1.0, goal.script)
        self.text_editor.mark_set("insert", "1.0")

    def update_logic_interrupt_name(self):
        """Called when an entry is selected."""
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            logic_state = self.get_entry_logic_state(self.active_row_index)
            logic_interrupt_name = self.get_category_dict()[entry_id, logic_state].logic_interrupt_name
            self.logic_interrupt.var.set(logic_interrupt_name)

    def get_entry_logic_state(self, row_index=None):
        if row_index is None:
            row_index = self.active_row_index
        return self.entry_rows[row_index].type_label.var.get() == "L"

    def _get_bnd_choice_name(self):
        """Just removes parenthetical and returns to CamelCase."""
        return self.bnd_choice.get().split(' (')[0].replace(' ', '')

    def _on_bnd_choice(self, _=None):
        self.select_entry_row_index(None)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)

    def _add_entry(self, entry_id, text, logic_state=None, category=None, at_index=None, new_goal=None):
        if entry_id < 0:
            self.dialog("Goal ID Error", message=f"Entry ID cannot be negative.")
            return False
        if (entry_id, logic_state) in self.get_category_dict():
            self.dialog("Goal ID Error",
                        message=f"Goal ID {entry_id} ({'logic' if logic_state else 'battle'}) already exists.")
            return False

        new_goal.goal_id = entry_id
        new_goal.has_logic_interrupt = logic_state
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        if at_index:
            self.get_selected_bnd().goals.insert(at_index, new_goal)
        else:
            self.get_selected_bnd().goals.append(new_goal)

        self._set_entry_text(entry_id, text, logic_state)
        self.select_entry_id(entry_id, logic_state=logic_state, set_focus_to_text=True, edit_if_already_selected=False)

    def add_relative_entry(self, entry_id, logic_state=None, offset=1, text=None):
        if text is None:
            text = self.get_entry_text(entry_id, logic_state=logic_state)  # Copies name of origin entry by default.
        goal = self.get_selected_bnd().get_goal(entry_id, logic_state).copy()
        goal_index = self.get_selected_bnd().get_goal_index(entry_id, logic_state) + 1
        self._add_entry(entry_id=entry_id + offset, logic_state=logic_state, text=text,
                        at_index=goal_index, new_goal=goal)

    def delete_entry(self, row_index, category=None):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        entry_id = self.get_entry_id(row_index)
        logic_state = self.get_entry_logic_state(row_index)
        goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
        self.get_selected_bnd().goals.remove(goal)
        self.refresh_entries()

    def get_selected_bnd(self) -> LuaBND:
        return self.AI[self._get_bnd_choice_name()]

    def get_category_dict(self, category=None) -> Dict[(int, bool), LuaGoal]:
        """Gets dictionary of goals in LuaInfo from LuaBND. Category does nothing."""
        return self.get_selected_bnd().get_goal_dict()

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Always returns full dict (no previous/next buttons)."""
        return list(self.get_selected_bnd().get_goal_dict().keys())

    def get_entry_index(self, entry_id: int, logic_state=None, category=None) -> int:
        """Get index of entry. Ignores current display range."""
        if logic_state is None:
            raise ValueError(f"Logic state cannot be none (entry {entry_id}).")
        if (entry_id, logic_state) not in self.get_category_dict():
            raise ValueError(f"Goal ID {entry_id} with type '{'logic' if logic_state else 'battle'}' does not exist.")
        goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
        return self.get_selected_bnd().goals.index(goal)

    def get_entry_text(self, entry_id: int, category=None, logic_state=None) -> str:
        return self.get_selected_bnd().get_goal(entry_id, logic_state).goal_name

    def _set_entry_text(self, entry_id: int, text: str, logic_state: bool = None, category=None, update_row_index=None):
        goal = self.get_selected_bnd().get_goal(entry_id, logic_state)
        goal.goal_name = text
        if update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text, logic_state)

    def _change_entry_text(self, row_index, new_text, category=None):
        """Set text of given entry index in the displayed category (if different from current)."""
        entry_id = self.get_entry_id(row_index)
        logic_state = self.get_entry_logic_state(row_index)
        current_text = self.get_entry_text(entry_id, logic_state=logic_state)
        if current_text == new_text:
            return False  # Nothing to change.
        self._set_entry_text(entry_id, new_text, logic_state=logic_state, category=category, update_row_index=row_index)
        return True

    def _start_entry_text_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            logic_state = self.get_entry_logic_state(row_index)
            initial_text = self.get_entry_text(entry_id, logic_state=logic_state)
            if '\n' in initial_text:
                return self.popout_entry_text_edit(row_index)
            self._e_entry_text_edit = self.Entry(
                self.entry_rows[row_index].text_box, initial_text=initial_text, sticky='ew',
                width=5)
            self._e_entry_text_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_text_edit(i))
            self._e_entry_text_edit.bind('<Up>', self._entry_press_up)
            self._e_entry_text_edit.bind('<Down>', self._entry_press_down)
            self._e_entry_text_edit.bind('<FocusOut>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.bind('<Escape>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.focus_set()
            self._e_entry_text_edit.select_range(0, 'end')

    def _change_entry_id(self, row_index, new_id, category=None):
        current_id = self.get_entry_id(row_index)
        if current_id == new_id:
            return False
        logic_state = self.get_entry_logic_state(row_index)
        goal_dict = self.get_category_dict()
        if (new_id, logic_state) in goal_dict:
            self.dialog("Entry ID Clash", f"Goal ID {new_id} with type {'logic' if logic_state else 'battle'} already "
                                          f"exists. You must change or delete it first.")
            return False
        goal = goal_dict[current_id, logic_state]
        goal.goal_id = new_id
        self.entry_rows[row_index].update_entry(new_id, goal.goal_name, goal.has_logic_interrupt)
        return True

    def _get_display_categories(self):
        """Unused."""
        return []
