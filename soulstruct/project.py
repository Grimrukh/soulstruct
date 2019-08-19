from __future__ import annotations
import datetime
from functools import wraps
import json
import os
import pickle
import shutil
from tkinter import Frame
from tkinter.constants import *

from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import find_steam_common_paths, traverse_path_tree, word_wrap, camel_case_to_spaces
from soulstruct.utilities.window import BaseWindow

__all__ = ['SoulstructProject', 'SoulstructError', 'SoulstructProjectError']


# TODO: SoulstructProject needs to wrap BaseWindow, not subclass it, to keep the namespace clear for interactive mode.
# TODO: Inspect PTD directory for lack of unpacking.


class SoulstructError(Exception):
    def __init__(self, msg=None):
        super().__init__(word_wrap(msg, 60) if msg else msg)


class SoulstructProjectError(SoulstructError):
    pass


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


# TODO: Separate Frame subclasses for each tab, so they can be launched independently.
class _TextEditor(Frame):

    def __init__(self, *args, soulstruct_project, **kwargs):
        super().__init__(*args, **kwargs)
        self._project = soulstruct_project  # Will need whole project for resolving references.


class _TextEditBox(BaseWindow):
    """Small pop-up widget that allows you to modify longer text more freely, with newlines and all."""

    WIDTH = 50  # characters
    HEIGHT = 10  # lines

    def __init__(self, master: _SoulstructProjectWindow, text_category: str, text_id: int, initial_text: str):
        super().__init__(window_title=f"Editing {camel_case_to_spaces(text_category)} [{text_id}]", master=master)

        self.initial_text = initial_text
        self.output = None

        self.start_auto_rows()
        self._text = self.Text(padx=20, pady=20, width=self.WIDTH, height=self.HEIGHT)
        self._text.insert(END, initial_text)
        with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={'padx': 10}):
            self.Button(text="Confirm changes", command=lambda: self.done(True), **master.DEFAULT_BUTTON_KWARGS['YES'])
            self.Button(text="Cancel changes", command=lambda: self.done(False), **master.DEFAULT_BUTTON_KWARGS['NO'])

        self.protocol('WM_DELETE_WINDOW', lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3))

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            new_text = self._text.get('1.0', END + '-1c')
            if new_text == self.initial_text:
                self.output = None
            else:
                self.output = self._text.get('1.0', END + '-1c')
        self.quit()


class _SoulstructProjectWindow(BaseWindow):
    DEFAULT_BUTTON_KWARGS = {
        'OK': {
            'fg': '#FFFFFF', 'bg': '#442222', 'width': 20,
        },
        'YES': {
            'fg': '#FFFFFF', 'bg': '#772222', 'width': 20,
        },
        'NO': {
            'fg': '#FFFFFF', 'bg': '#444444', 'width': 20,
        },
    }

    TEXT_CANVAS_BG = '#111'
    TEXT_CATEGORY_BOX_WIDTH = 250
    TEXT_SELECTED_CATEGORY = '#555'
    TEXT_BOX_WIDTH = 800
    TEXT_DISPLAY_COUNT = 50
    TEXT_ALTERNATING_BG = ('#222', '#333')
    TEXT_SPACE_ONLY_ALTERNATING_BG = ('#332', '#443')
    TEXT_EMPTY_ALTERNATING_BG = ('#422', '#533')
    TEXT_SELECTED_BG = '#445'

    def __init__(self, soulstruct_project: SoulstructProject, master=None):
        """TODO: Build window.

        I'm thinking: main tabs up top (Text, Params, Lighting) in large text.

        In Text:
            You can freely edit both IDs and names, but when confirming the edit, it will complain if the ID matches an
            existing ID and refuse to make the change.

            Empty entries are highlighted in red. These will be removed when you next save (a warning will pop up when
                you save, which you can set to never appear again).
            Buttons to delete entries and insert a new empty one below the current selection (auto-numbered).

            LATER: Undo/redo button. It takes about 30 ms to make an entire copy of the Text dictionary, so it's easy
                to save stacks of states.

            LATER: You can find all usages of a given text entry. They pop up in a separate window with hyperlinks to
                each occurrence.

        In Params:


        """
        self.project = soulstruct_project
        super().__init__("Soulstruct", master=master)

        self.file_types = None

        self.text_category_canvas = None
        self.f_text_categories = None
        self.show_all_categories = self.BooleanVar()
        self.category_boxes = {}
        self.selected_text_category = 'PlaceNames'
        self.fmg_canvas = None
        self.f_fmg_entries = None
        self.previous_range_button = None
        self.next_range_button = None
        self.text_boxes = {}
        self.selected_text_id = None
        self.text_entry = None
        self.editing_text = False
        self.text_start_index = 0

    def build(self):

        self.file_types = self.Notebook()

        text_tab = self.Frame(frame=self.file_types)
        self.file_types.add(text_tab, text='  Text  ')
        self.build_text_tab(text_tab)

        # TODO: Params and lighting. Events. Etc.
        self.resizable(False, False)
        self.set_geometry()

    def populate_text_categories(self):
        for box, label in self.category_boxes.values():
            box.destroy()
            label.destroy()
        self.category_boxes = {}
        with self.set_master(self.f_text_categories):
            names = 'all_fmg_names' if self.show_all_categories.get() else 'useful_fmg_names'
            categories = getattr(self.project.Text, names)
            if self.selected_text_category not in categories:
                self.select_text_category(None)
            for row, category in enumerate(categories):
                box = self.Frame(row=row, width=self.TEXT_CATEGORY_BOX_WIDTH, height=30, highlightthickness=1)
                label_text = camel_case_to_spaces(category).replace(' _', ':')
                label = self.Label(text=label_text, sticky=EW, row=row)
                label.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                box.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                if category == self.selected_text_category:
                    label['bg'] = self.TEXT_SELECTED_CATEGORY
                    box['bg'] = self.TEXT_SELECTED_CATEGORY
                self.link_to_scrollable(self.text_category_canvas, box, label)
                self.category_boxes[category] = (box, label)

    def build_text_tab(self, text_tab):
        with self.set_master(text_tab, auto_columns=0):
            with self.set_master(auto_rows=0):
                with self.set_master():
                    self.text_category_canvas = self.Canvas(
                        scrollbar=True, width=self.TEXT_CATEGORY_BOX_WIDTH, height=575, padx=40, pady=40,
                        highlightthickness=0)
                    self.f_text_categories = self.Frame(width=self.TEXT_CATEGORY_BOX_WIDTH, height=575, sticky=EW)
                    self.link_to_scrollable(self.text_category_canvas, self.f_text_categories)
                    self.text_category_canvas.create_window(
                        self.TEXT_CATEGORY_BOX_WIDTH / 2, 300, window=self.f_text_categories, anchor=NW)
                    self.f_text_categories.bind(
                        "<Configure>", lambda e, c=self.text_category_canvas: self.reset_canvas_scroll_region(c))

                    self.populate_text_categories()

                self.show_all_categories = self.Checkbutton(label='Show internal categories ', initial_state=False,
                                                            command=self.populate_text_categories, pady=20).var

            # TODO: Field to add brand new text entries (ID and text).
            # TODO: Field to navigate straight to entry (ID).
            # TODO: Field to search for text in this category (text). Can click repeatedly to go to next (loops around).
            # TODO: Detect if sequential entries are +1 to ID and add '+N' to text string, and collapse them. They can
            #  be edited by editing the first one, or you can manually un-collapse them with right click.

            with self.set_master():
                self.previous_range_button = self.Button(
                    text=f"Previous {self.TEXT_DISPLAY_COUNT}", bg='#722', width=30, command=self.previous_text_range,
                    padx=10, pady=20, row=0)

                with self.set_master(row=1):
                    self.fmg_canvas = self.Canvas(scrollbar=True, width=self.TEXT_BOX_WIDTH, height=500,
                                                  highlightthickness=1, padx=40, pady=40, bg=self.TEXT_CANVAS_BG)
                    self.f_fmg_entries = self.Frame(frame=self.fmg_canvas, width=self.TEXT_BOX_WIDTH, sticky=EW)
                    self.fmg_canvas.create_window(self.TEXT_BOX_WIDTH / 2, 250, window=self.f_fmg_entries, anchor=NW)
                    self.f_fmg_entries.bind(
                        "<Configure>", lambda e, c=self.fmg_canvas: self.reset_canvas_scroll_region(c))
                self.next_range_button = self.Button(
                    text=f"Next {self.TEXT_DISPLAY_COUNT}", bg='#722', width=30, command=self.next_text_range,
                    padx=10, pady=20, row=2)

                self.populate_text()

    def select_text_category(self, selected):
        if selected == self.selected_text_category:
            return  # No change.

        self.cancel_text_edit(self.selected_text_id)
        self.text_start_index = 0

        if selected is None:
            self.selected_text_category = None
            for widgets in self.text_boxes.values():
                for w in widgets.values():
                    w.destroy()
            return

        self.selected_text_category = selected
        for category, (box, label) in self.category_boxes.items():
            if selected == category:
                box['bg'] = self.TEXT_SELECTED_CATEGORY
                label['bg'] = self.TEXT_SELECTED_CATEGORY
                self.populate_text()
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']

        self.update()
        self.fmg_canvas.yview_moveto(0)
        self.previous_range_button['state'] = DISABLED

        if self.text_start_index == min(max(
                len(self.project.Text[self.selected_text_category]) - self.TEXT_DISPLAY_COUNT, 0),
                self.text_start_index + self.TEXT_DISPLAY_COUNT):
            self.next_range_button['state'] = DISABLED
        else:
            self.next_range_button['state'] = NORMAL

    def populate_text(self):
        for widgets in self.text_boxes.values():
            for w in widgets.values():
                w.destroy()
        self.text_boxes = {}

        with self.set_master(self.f_fmg_entries):
            for row, (text_id, text) in enumerate(
                    self.project.Text.get_range(self.selected_text_category, self.text_start_index,
                                                self.text_start_index + self.TEXT_DISPLAY_COUNT)):
                bg = self.TEXT_ALTERNATING_BG[row % 2] if text else self.TEXT_EMPTY_ALTERNATING_BG[row % 2]
                if text == ' ':
                    text_bg = self.TEXT_SPACE_ONLY_ALTERNATING_BG[row % 2]
                elif not text:
                    text_bg = self.TEXT_EMPTY_ALTERNATING_BG[row % 2]
                else:
                    text_bg = bg
                row_box = self.Frame(width=self.TEXT_BOX_WIDTH, height=30, row=row, columnspan=2, sticky=NSEW, bg=bg)
                self._bind_text_events(row_box, text_id)

                id_label = self.Label(text=str(text_id), width=15, row=row, column=0, bg=bg, sticky=E)
                self._bind_text_events(id_label, text_id)

                text_box = self.Frame(row=row, column=1, bg=bg, sticky=EW)
                self._bind_text_events(text_box, text_id)

                text_label = self.Label(text_box, text=text, bg=text_bg, sticky=SW, justify=LEFT)
                self._bind_text_events(text_label, text_id)

                context_menu = self.Menu()
                context_menu.add_command(
                    label="Edit in Floating Box (shift + click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self.floating_edit_text(i))
                context_menu.add_command(
                    label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self._add_relative_entry(self.selected_text_category, i, offset=1))
                context_menu.add_command(
                    label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self._delete_entry(self.selected_text_category, i))

                self.text_boxes[text_id] = {'row_box': row_box, 'id_label': id_label, 'text_box': text_box,
                                            'text_label': text_label, 'context_menu': context_menu}
                row += 1

        self.f_fmg_entries.grid_columnconfigure(1, weight=1)

    def _right_click_text_entry(self, event, text_id):
        self.select_text(text_id, edit_if_already_selected=False)
        self.text_boxes[text_id]['context_menu'].tk_popup(event.x_root, event.y_root)

    def _add_relative_entry(self, category, text_id, offset=1, new_text=None):
        if offset == 0:
            raise ValueError("Offset for adding relative entry cannot be zero.")
        if text_id + offset < 0:
            raise ValueError(f"Offset from entry cannot be negative (offset {offset} from text ID {text_id}).")
        if text_id + offset in self.project.Text[category]:
            self.dialog("Existing Text Error", f"Text entry {text_id + offset} already exists for category {category}.",
                        button_names='OK', button_kwargs='OK')
            return
        if new_text is None:
            new_text = self.project.Text[category][text_id]
        self.cancel_text_edit(self.selected_text_id)
        self.project.Text[category][text_id + offset] = new_text
        if category == self.selected_text_category:
            self.populate_text()
            # TODO: Is full refresh necessary? What's the best way to adjust displayed range?

    def _delete_entry(self, category, text_id):
        self.cancel_text_edit(self.selected_text_id)
        self.project.Text[category].pop(text_id)
        if category == self.selected_text_category:
            self.populate_text()
            # TODO: Is full refresh necessary? What's the best way to adjust displayed range?

    def _bind_text_events(self, widget, text_id):
        widget.bind('<Button-1>', lambda e, i=text_id: self.select_text(i))
        widget.bind('<Shift-Button-1>', lambda e, i=text_id: self.floating_edit_text(i))
        widget.bind('<Prior>', lambda e: self.previous_text_range())
        widget.bind('<Next>', lambda e: self.next_text_range())
        widget.bind('<Button-3>', lambda e, i=text_id: self._right_click_text_entry(e, i))

    def previous_text_range(self):
        if self.selected_text_category is None:
            return
        target_start = max(self.text_start_index - self.TEXT_DISPLAY_COUNT, 0)
        if target_start == self.text_start_index:
            self.previous_range_button['state'] = DISABLED
            return
        self.previous_range_button['state'] = NORMAL
        self.text_start_index = target_start
        self.cancel_text_edit(self.selected_text_id)
        self.populate_text()
        first_text_id = list(self.text_boxes)[0]
        if self.selected_text_id != first_text_id:
            self.select_text(first_text_id)
        self.geometry()
        self.fmg_canvas.yview_moveto(0)

        if self.text_start_index == max(self.text_start_index - self.TEXT_DISPLAY_COUNT, 0):
            self.previous_range_button['state'] = DISABLED

        if self.text_start_index != min(max(len(self.project.Text[self.selected_text_category])
                                            - self.TEXT_DISPLAY_COUNT, 0),
                                        self.text_start_index + self.TEXT_DISPLAY_COUNT):
            self.next_range_button['state'] = NORMAL

    def next_text_range(self):
        if self.selected_text_category is None:
            return
        target_start = min(max(len(self.project.Text[self.selected_text_category]) - self.TEXT_DISPLAY_COUNT, 0),
                           self.text_start_index + self.TEXT_DISPLAY_COUNT)
        if target_start == self.text_start_index:
            self.next_range_button['state'] = DISABLED
            return  # TODO: Check if button should be disabled more often (whenever a new category is loaded).
        self.next_range_button['state'] = NORMAL
        self.text_start_index = target_start
        self.cancel_text_edit(self.selected_text_id)
        self.populate_text()
        first_text_id = list(self.text_boxes)[0]
        if self.selected_text_id != first_text_id:
            self.select_text(first_text_id)
        self.geometry()
        self.fmg_canvas.yview_moveto(0)

        if self.text_start_index != max(self.text_start_index - self.TEXT_DISPLAY_COUNT, 0):
            self.previous_range_button['state'] = NORMAL

        if self.text_start_index == min(max(len(self.project.Text[self.selected_text_category])
                                            - self.TEXT_DISPLAY_COUNT, 0),
                                        self.text_start_index + self.TEXT_DISPLAY_COUNT):
            self.next_range_button['state'] = DISABLED

    def start_text_edit(self, edited_text_id):
        if not self.editing_text:
            widgets = self.text_boxes[edited_text_id]
            text_box = widgets['text_box']
            label = widgets['text_label']
            if '\n' in label.var.get():
                return self.floating_edit_text(edited_text_id)
            label.grid_remove()
            self.text_entry = self.Entry(text_box, initial_text=label.var.get(), sticky=EW, font=('Roboto', 12),
                                         width=60)
            self.text_entry.bind('<Return>', lambda e, i=edited_text_id: self.confirm_text_edit(i))
            self.text_entry.bind('<FocusOut>', lambda e, i=edited_text_id: self.cancel_text_edit(i))
            self.text_entry.bind('<Escape>', lambda e, i=edited_text_id: self.cancel_text_edit(i))
            self.text_entry.grid()
            self.text_entry.focus_set()
            self.editing_text = True

    def floating_edit_text(self, edited_text_id):
        if not self.editing_text:
            self.editing_text = True
            label = self.text_boxes[edited_text_id]['text_label']
            floating_edit = _TextEditBox(self, self.selected_text_category, edited_text_id, label.var.get())
            new_text = floating_edit.go()
            if new_text is not None:  # Confirmed text change.
                label.var.set(new_text)
                self.project.Text[self.selected_text_category][edited_text_id] = new_text
            self.editing_text = False

    def cancel_text_edit(self, edited_text_id):
        if self.editing_text:
            widgets = self.text_boxes[edited_text_id]
            label = widgets['text_label']
            self.text_entry.destroy()
            label.grid()
            self.editing_text = False

    def confirm_text_edit(self, edited_text_id):
        if self.editing_text:
            new_text = self.text_entry.var.get()
            if self.project.Text[self.selected_text_category][edited_text_id] != new_text:
                pass  # TODO: flag unsaved change to Text. Add (category, text) tuple to an unsaved set. Red entry BG.
            self.project.Text[self.selected_text_category][edited_text_id] = new_text
            widgets = self.text_boxes[edited_text_id]
            label = widgets['text_label']
            self.text_entry.destroy()
            label.var.set(new_text)
            label.grid()
            self.editing_text = False

    def select_text(self, selected_text_id, edit_if_already_selected=True):
        if self.selected_text_id is not None and selected_text_id == self.selected_text_id:
            if edit_if_already_selected:
                return self.start_text_edit(selected_text_id)
            return

        self.selected_text_id = selected_text_id
        for row, (text_id, widgets) in enumerate(self.text_boxes.items()):
            text = widgets['text_label'].var.get()
            bg = self.TEXT_ALTERNATING_BG[row % 2] if text else self.TEXT_EMPTY_ALTERNATING_BG[row % 2]
            if text == ' ':
                text_bg = self.TEXT_SPACE_ONLY_ALTERNATING_BG[row % 2]
            elif not text:
                text_bg = self.TEXT_EMPTY_ALTERNATING_BG[row % 2]
            else:
                text_bg = bg
            if text_id == selected_text_id:
                widgets['row_box']['bg'] = widgets['id_label']['bg'] = self.TEXT_SELECTED_BG
                widgets['text_box']['bg'] = widgets['text_label']['bg'] = self.TEXT_SELECTED_BG
                widgets['text_label'].focus_set()
            else:
                widgets['row_box']['bg'] = widgets['id_label']['bg'] = bg
                widgets['text_box']['bg'] = bg
                widgets['text_label']['bg'] = text_bg

    def dialog(self, *args, **kwargs):
        button_kwargs = kwargs.get('button_kwargs', None)
        if button_kwargs is not None:
            if button_kwargs in self.DEFAULT_BUTTON_KWARGS:
                button_kwargs = self.DEFAULT_BUTTON_KWARGS[button_kwargs]
            else:
                for b in button_kwargs:
                    if b in self.DEFAULT_BUTTON_KWARGS:
                        button_kwargs[b] = self.DEFAULT_BUTTON_KWARGS[b]
            kwargs['button_kwargs'] = button_kwargs
        return self.custom_dialog(*args, **kwargs)


class SoulstructProject(object):
    """Manages a directory of files that can be modded and 'pushed' into the appropriate game directory at will.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.
    TODO:
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save decorators that operate at ten minute intervals on write methods.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'

    def __init__(self, project_directory: str = ''):

        self._window = _SoulstructProjectWindow(soulstruct_project=self, master=None)
        # self._window.withdraw()

        self.game_name = ''
        self.game_dir = ''
        self.last_pull_time = ''
        self.last_push_time = ''
        # TODO: Record last edit time for each file/structure.

        self.Text = DarkSoulsText(None)
        self.Params = DarkSoulsGameParameters(None)
        self.Lighting = DarkSoulsLightingParameters(None)

        try:
            self.project_dir = self._validate_project_directory(project_directory, self._DEFAULT_PROJECT_ROOT)
            self.load_config()
            try:
                self.unpickle_all()
            except FileNotFoundError:
                # TODO: Should try to unpickle all, then prompt you to pull missing files.
                self.load_project()
                self.pickle_all()
        except SoulstructProjectError as e:
            self.dialog(title="Project Error", message=str(e), button_kwargs='OK')
            raise
        except Exception as e:
            msg = "Internal Python Error:\n\n" + str(e)
            self.dialog(title="Unknown Error", message=msg, button_kwargs='OK')
            raise

        self._window.build()
        self._window.wait_window()

    def load_project(self):
        """Load project structures (params, text, etc.) into dictionary as attributes.

        TODO: Will eventually look for entire pickled project file first.
        """
        self.Text = DarkSoulsText(self.project_path('msg/ENGLISH'))
        self.Params = DarkSoulsGameParameters(self.project_path('param/GameParam/GameParam.parambnd'))
        self.Lighting = DarkSoulsLightingParameters(self.project_path('param/DrawParam'))

    def export_project(self, export_directory: str = None):
        if export_directory is None:
            export_directory = self.project_path(f'export/{self._get_timestamp(for_path=True)}')

        text_path = os.path.join(export_directory, 'msg/ENGLISH/')
        os.makedirs(text_path, exist_ok=True)
        self.Text.write(text_path)

        params_path = os.path.join(export_directory, 'param/GameParam/GameParam.parambnd')
        os.makedirs(params_path, exist_ok=True)
        self.Params.save(params_path)

        # TODO
        # lighting_path = os.path.join(export_directory, 'param/DrawParam/')
        # os.makedirs(lighting_path, exist_ok=True)
        # self.Lighting.write(lighting_path)

    def pickle_all(self):
        with open(self.project_path('Text.dstext'), 'wb') as f:
            pickle.dump(self.Text, f)
        with open(self.project_path('Params.dstext'), 'wb') as f:
            pickle.dump(self.Params, f)
        with open(self.project_path('Lighting.dstext'), 'wb') as f:
            pickle.dump(self.Lighting, f)

    def unpickle_all(self):
        try:
            with open(self.project_path('Text.dstext'), 'rb') as f:
                self.Text = pickle.load(f)
            with open(self.project_path('Params.dstext'), 'rb') as f:
                self.Params = pickle.load(f)
            with open(self.project_path('Lighting.dstext'), 'rb') as f:
                self.Lighting = pickle.load(f)
        except FileNotFoundError:
            self.dialog(title="Project Error", message="(TODO) Could not unpickle files. Will try to pull.",
                        button_kwargs='OK')
            raise

    def load_config(self):
        try:
            with open(os.path.join(self.project_dir, 'config.json'), 'r') as f:
                try:
                    config = json.load(f)
                except json.JSONDecodeError:
                    raise SoulstructProjectError(
                        "Could not interpret 'config.json' file. Check it for errors, or "
                        "delete it to have Soulstruct create a fresh copy on next load."
                    )
                else:
                    try:
                        self.game_name = config['GameName']
                        self.game_dir = config['GameDirectory']
                        self.last_pull_time = config.get('LastPullTime', None)
                        self.last_push_time = config['LastPushTime']
                    except KeyError:
                        raise SoulstructProjectError(
                            "Project config file does not contain necessary settings. "
                            "Delete it and load the project directory again to create "
                            "a fresh copy."
                        )
        except FileNotFoundError:
            # Create project config file.
            try:
                self.game_dir, self.game_name = self._get_live_game_directory()
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            if self.dialog(title="Initial project pull",
                           message="Pull game files from game directory into project directory now?",
                           button_names=("Yes, pull the files", "No, I'll do it later"),
                           button_kwargs=('YES', 'NO'),
                           cancel_output=1, default_output=1) == 0:
                self.pull()

    @_with_config_write
    def pull(self):
        print("# Pulling game files into project...")  # TODO: log
        for path_sequence in traverse_path_tree(MODIFIABLE_FILES[self.game_name]):
            game_file = os.path.join(self.game_dir, *path_sequence)
            project_file = os.path.join(self.project_dir, *path_sequence)
            try:
                os.makedirs(os.path.dirname(project_file), exist_ok=True)
                shutil.copy2(game_file, project_file)
            except FileNotFoundError:
                raise SoulstructProjectError(f"Could not find expected game file: {repr(game_file)}")
        self.last_pull_time = self._get_timestamp()

    @_with_config_write
    def push(self):
        print("# Pushing project files to game...")  # TODO: log
        for path_sequence in traverse_path_tree(MODIFIABLE_FILES[self.game_name]):
            project_file = os.path.join(self.project_dir, *path_sequence)
            game_file = os.path.join(self.game_dir, *path_sequence)
            shutil.copy2(project_file, game_file)
        self.last_push_time = self._get_timestamp()

    def game_path(self, *relative_parts):
        return os.path.abspath(os.path.join(self.game_dir, *relative_parts))

    def project_path(self, *relative_parts):
        return os.path.abspath(os.path.join(self.project_dir, *relative_parts))

    @staticmethod
    def _get_timestamp(for_path=False):
        if for_path:
            return datetime.datetime.now().strftime('%Y %B %d %H.%M.%S')
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _build_config_dict(self):
        return {
            'GameName': self.game_name,
            'GameDirectory': self.game_dir,
            'LastPullTime': self.last_pull_time,
            'LastPushTime': self.last_push_time,
        }

    def _write_config(self):
        try:
            with open(os.path.join(self.project_dir, 'config.json'), 'w') as f:
                json.dump(self._build_config_dict(), f, indent=4)
        except PermissionError:
            raise SoulstructProjectError("No write access to 'config.json' in project directory.")

    def _validate_project_directory(self, project_dir, default_root):
        if not project_dir:
            self.dialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it."
                    "The name of the directory will be the name of the project.", 50),
                button_names='OK', button_kwargs='OK')
            project_dir = self._window.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=os.path.expanduser('~/Documents'))
            if not project_dir:
                raise SoulstructProjectError(word_wrap("No directory chosen. Quitting Soulstruct.", 50))
        if not os.path.isabs(project_dir):
            project_dir = os.path.abspath(os.path.join(default_root, project_dir))
        if os.path.isfile(project_dir):
            raise SoulstructProjectError("You must specify a project *directory*, not a file.")

        if not os.path.isdir(project_dir):
            try:
                os.makedirs(project_dir, exist_ok=True)
            except NotADirectoryError:
                raise SoulstructProjectError(f"Invalid directory path: {repr(project_dir)}.")
            except PermissionError:
                raise SoulstructProjectError(f"No write access to create directory: {repr(project_dir)}.")

        return project_dir

    def _get_live_game_directory(self):
        for common_path in find_steam_common_paths():
            dsr_path = os.path.join(common_path, 'DARK SOULS REMASTERED')
            if os.path.isdir(dsr_path):
                initial_dir = dsr_path
                break
            ptd_path = os.path.join(common_path, 'Dark Souls Prepare to Die Edition/DATA')
            if os.path.isdir(ptd_path):
                initial_dir = ptd_path
                break
        else:
            initial_dir = None

        message = ("Navigate to the game executable for this project.\n"
                   "This can normally be found in:\n\n"
                   ""
                   "Prepare to Die Edition:\n"
                   "C:/Program Files/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/DARKSOULS.exe\n\n"
                   ""
                   "Remastered:\n"
                   "C:/Program Files/Steam/steamapps/common/DARK SOULS REMASTERED/DarkSoulsRemastered.exe\n\n"
                   ""
                   "Otherwise, you can use Steam to find your Steam directory.")
        self.dialog(title="Select game for project", message=message, font_size=14,
                    button_names='OK', button_kwargs='OK')
        live_dir = self._window.FileDialog.askopenfilename(
            title="Choose your game executable", initialdir=initial_dir, filetypes=[('Game executable', '.exe')])
        if not live_dir:
            raise SoulstructProjectError("No game directory selected.")
        if os.path.isfile(os.path.join(live_dir, 'DarkSoulsRemastered.exe')):
            return live_dir, 'Dark Souls Remastered'
        elif os.path.isfile(os.path.join(live_dir, 'DARKSOULS.exe')):
            return live_dir, 'Dark Souls Prepare to Die Edition'
        else:
            raise SoulstructProjectError("Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                                         "but your selected executable was not a version of Dark Souls.")

    def dialog(self, title, message, *args, **kwargs):
        message = word_wrap(message, 50)
        return self._window.dialog(title, message, *args, **kwargs)


MODIFIABLE_FILES = {
    'Dark Souls Prepare to Die Edition': {
        'event': [
            "common.emevd",
            "m10_00_00_00.emevd",
            "m10_01_00_00.emevd",
            "m10_02_00_00.emevd",
            "m11_00_00_00.emevd",
            "m12_00_00_00.emevd",
            "m12_01_00_00.emevd",
            "m13_00_00_00.emevd",
            "m13_01_00_00.emevd",
            "m13_02_00_00.emevd",
            "m14_00_00_00.emevd",
            "m14_01_00_00.emevd",
            "m15_00_00_00.emevd",
            "m15_01_00_00.emevd",
            "m16_00_00_00.emevd",
            "m17_00_00_00.emevd",
            "m18_00_00_00.emevd",
            "m18_01_00_00.emevd",
        ],
        'msg': {
            'ENGLISH': [
                'item.msgbnd',
                'menu.msgbnd',
            ],
        },
        'param': {
            'GameParam': [
                'GameParam.parambnd',
            ],
            'DrawParam': [
                "a10_DrawParam.parambnd",
                "a11_DrawParam.parambnd",
                "a12_DrawParam.parambnd",
                "a13_DrawParam.parambnd",
                "a14_DrawParam.parambnd",
                "a15_DrawParam.parambnd",
                "a16_DrawParam.parambnd",
                "a17_DrawParam.parambnd",
                "a18_DrawParam.parambnd",
                "a99_DrawParam.parambnd",
                "default_DrawParam.parambnd",
            ],
        },
    },
    'Dark Souls Remastered': {
        'event': [
            "common.emevd.dcx",
            "m10_00_00_00.emevd.dcx",
            "m10_01_00_00.emevd.dcx",
            "m10_02_00_00.emevd.dcx",
            "m11_00_00_00.emevd.dcx",
            "m12_00_00_00.emevd.dcx",
            "m12_01_00_00.emevd.dcx",
            "m13_00_00_00.emevd.dcx",
            "m13_01_00_00.emevd.dcx",
            "m13_02_00_00.emevd.dcx",
            "m14_00_00_00.emevd.dcx",
            "m14_01_00_00.emevd.dcx",
            "m15_00_00_00.emevd.dcx",
            "m15_01_00_00.emevd.dcx",
            "m16_00_00_00.emevd.dcx",
            "m17_00_00_00.emevd.dcx",
            "m18_00_00_00.emevd.dcx",
            "m18_01_00_00.emevd.dcx",
        ],
        'msg': {
            'ENGLISH': [
                'item.msgbnd.dcx',
                'menu.msgbnd.dcx',
            ],
        },
        'param': {
            'GameParam': [
                'GameParam.parambnd.dcx'
            ],
            'DrawParam': [
                "a10_DrawParam.parambnd.dcx",
                "a11_DrawParam.parambnd.dcx",
                "a12_DrawParam.parambnd.dcx",
                "a13_DrawParam.parambnd.dcx",
                "a14_DrawParam.parambnd.dcx",
                "a15_DrawParam.parambnd.dcx",
                "a16_DrawParam.parambnd.dcx",
                "a17_DrawParam.parambnd.dcx",
                "a18_DrawParam.parambnd.dcx",
                "a99_DrawParam.parambnd.dcx",
                "default_DrawParam.parambnd.dcx",
            ],
        },
    },
}
