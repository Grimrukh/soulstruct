from __future__ import annotations

import inspect
import re
import sys
from importlib import import_module
from pathlib import Path
from typing import Dict, List, TYPE_CHECKING

import soulstruct.game_types as gt
from soulstruct.maps import DARK_SOULS_MAP_NAMES
from soulstruct.maps.msb import MAP_ENTRY_ENTITY_TYPES
from soulstruct.project.editor import SoulstructBaseEditor
from soulstruct.utilities import camel_case_to_spaces

if TYPE_CHECKING:
    from soulstruct.maps import DarkSoulsMaps
    from soulstruct.maps.core import MSBEntryEntity


ENTRY_LIST_FG_COLORS = {
    'Parts': '#DDF',
    'Regions': '#FDD',
    'Events': '#DFD',
}


ENTRY_GAME_TYPES = {
    "Parts: MapPieces": gt.MapPiece,
    "Parts: Objects": gt.Object,
    "Parts: Characters": gt.Character,
    "Parts: PlayerStarts": gt.PlayerStart,
    "Parts: Collisions": gt.Collision,
    "Parts: Navmeshes": gt.Navmesh,
    "Events: Sounds": gt.SoundEvent,
    "Events: FX": gt.FXEvent,
    "Events: Spawners": gt.SpawnerEvent,
    "Events: Messages": gt.MessageEvent,
    "Events: ObjActs": gt.ObjActEvent,
    "Events: SpawnPoints": gt.SpawnPointEvent,
    "Events: Navigation": gt.NavmeshEvent,
    "Regions: Points": gt.Region,
    "Regions: Circles": gt.Region,
    "Regions: Spheres": gt.Region,
    "Regions: Cylinders": gt.Region,
    "Regions: Rectangles": gt.Region,
    "Regions: Boxes": gt.Region,
}


MODULE_CLASS_NAMES = {
    "Parts: MapPieces": "MapPieces",
    "Parts: Objects": "Objects",
    "Parts: Characters": "Characters",
    "Parts: PlayerStarts": "PlayerStarts",
    "Parts: Collisions": "Collisions",
    "Parts: Navmeshes": "Navmeshes",
    "Events: Sounds": "SoundEvents",
    "Events: FX": "FXEvents",
    "Events: Spawners": "SpawnerEvents",
    "Events: Messages": "MessageEvents",
    "Events: ObjActs": "ObjActEvents",
    "Events: SpawnPoints": "SpawnPointEvents",
    "Events: Navigation": "NavmeshEvents",
    "Regions: Points": "Points",
    "Regions: Circles": "Circles",
    "Regions: Spheres": "Spheres",
    "Regions: Cylinders": "Cylinders",
    "Regions: Rectangles": "Rectangles",
    "Regions: Boxes": "Boxes",
}


class SoulstructEntityEditor(SoulstructBaseEditor):
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 870
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 100

    class EntryRow(SoulstructBaseEditor.EntryRow):
        """Entry rows for Maps have no ID, and also display their Entity ID field if they have a non-default value."""
        master: SoulstructEntityEditor

        ENTRY_ID_WIDTH = 15
        EDIT_ENTRY_ID = True

        def __init__(self, editor: SoulstructEntityEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

        def update_entry(self, entry_index: int, entry_text: str):
            self.entry_id = entry_index
            self._entry_text = entry_text
            self.text_label.var.set(entry_text)
            self.build_entry_context_menu()
            self.unhide()

        def build_entry_context_menu(self):
            self.context_menu.delete(0, 'end')
            self.context_menu.add_command(
                label="Edit in Floating Box (Shift + Click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.popout_entry_text_edit(self.row_index))

    entry_rows: List[SoulstructEntityEditor.EntryRow]

    def __init__(self, maps: DarkSoulsMaps, evs_directory, linker, master=None, toplevel=False):
        self.Maps = maps
        self.map_choice = None
        self.evs_directory = Path(evs_directory)
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Map Data Editor")

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[1, 1], auto_columns=0):
                map_display_names = [f"{camel_case_to_spaces(v)} ({k})" for k, v in DARK_SOULS_MAP_NAMES.items()]
                self.map_choice = self.Combobox(
                    values=map_display_names, label='Map:', label_font_size=12, label_position='left', width=25,
                    font=('Segoe UI', 12), on_select_function=self._on_map_choice, sticky='w', padx=10).var
                self.Button(text="Generate EVS Constants", command=self._refresh_entities_module, width=25, padx=10)
                self.Button(text="Replace EVS IDs", command=self._replace_evs_ids, width=25, padx=10)

            with self.set_master(sticky='nsew', row_weights=[1], column_weights=[0, 1], auto_columns=0):
                self.build_category_canvas()
                with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1], auto_rows=0):
                    self.build_entry_frame()

    def _get_map_choice_name(self):
        """Just removes parenthetical and returns to CamelCase."""
        return self.map_choice.get().split(' (')[0].replace(' ', '')

    def _on_map_choice(self, _=None):
        self.select_entry_row_index(None)
        self.refresh_entries()

    def _refresh_entities_module(self):
        """Generates a '{mXX_YY}_entities.py' file with entity IDs for import into EVS script."""
        map_id = DARK_SOULS_MAP_NAMES[self._get_map_choice_name()]
        if map_id == "m12_00_00_01":
            map_id = "m12_00_00_00"  # ignore Darkroot MSB file variant index
        module_path = self.evs_directory / f"{map_id}_entities.py"
        module_text = "from soulstruct.game_types import *\n"
        for category in self._get_display_categories():
            game_type = ENTRY_GAME_TYPES[category]
            class_name = MODULE_CLASS_NAMES[category]
            class_text = ""
            requires_pass = True
            for entity_id, msb_entry in self.get_category_dict(category).items():
                name = msb_entry.name.replace(' ', '')
                try:
                    name = name.encode('utf-8').decode('ascii')
                except UnicodeDecodeError:
                    class_text += f"    # {name} = {entity_id}\n"
                else:
                    class_text += f"    {name} = {entity_id}\n"
                    requires_pass = False
            if class_text:
                class_text = f"\n\nclass {class_name}({game_type.__name__}):\n" + class_text
                if requires_pass:
                    class_text += "    pass\n"
                module_text += class_text

        with module_path.open('w', encoding='utf-8') as f:
            f.write(module_text)

    def _replace_evs_ids(self):
        map_id = DARK_SOULS_MAP_NAMES[self._get_map_choice_name()]
        if map_id == "m12_00_00_01":
            map_id = "m12_00_00_00"  # ignore Darkroot MSB file variant index
        module_path = self.evs_directory / f"{map_id}_entities.py"
        if not module_path.is_file():
            return self.error_dialog("No Entity Module", "Entity module not yet created in project 'events' folder.")
        evs_path = self.evs_directory / f"{map_id}.evs.py"
        if not evs_path.is_file():
            return self.error_dialog("No EVS Script", "EVS script not yet imported into project 'events' folder.")
        sys.path.append(str(module_path.parent))
        try:
            entity_module = import_module(module_path.stem)
        except Exception as e:
            return self.error_dialog("Import Error", f"Could not import {module_path.name}. Error:\n\n{str(e)}")
        with evs_path.open('r', encoding='utf-8') as f:
            evs = f.read()
        for attr_name, attr in [m[0:2] for m in inspect.getmembers(entity_module, inspect.isclass)
                                if m[1].__module__ == entity_module.__name__]:
            for entity in attr:
                evs = re.sub(fr"([ ,(=]){entity.value}([,)])", fr"\1{attr_name}.{entity.name}\2", evs)

        if f"from {module_path.stem} import *" not in evs:
            evs = evs.replace("from soulstruct.events.darksouls1 import *\n",
                              f"from soulstruct.events.darksouls1 import *\nfrom {module_path.stem} import *\n")
        with evs_path.open('w', encoding='utf-8') as f:
            f.write(evs)

    @staticmethod
    def _get_category_text_fg(category: str):
        return ENTRY_LIST_FG_COLORS.get(category.split(':')[0], '#FFF')

    def _get_display_categories(self):
        """ALl combinations of MSB entry list names (except Model) and their subtypes, properly formatted."""
        categories = []
        for entry_list_name, entry_type_names in MAP_ENTRY_ENTITY_TYPES.items():
            if entry_list_name == 'Models':
                continue
            for name in entry_type_names:
                categories.append(f'{entry_list_name}: {name}')
        return categories

    def get_selected_msb(self):
        return self.Maps[self._get_map_choice_name()]

    def get_category_dict(self, category=None) -> Dict[int, MSBEntryEntity]:
        """Gets entry data from map choice, entry list choice, and entry type choice (active category).

        Entity dictionary is generated from `MSB.get_entity_id_dict()` every time, and is definitively *not* sorted;
        entity IDs will appear in the order they appear in the MSB.
        """
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        map_choice = self._get_map_choice_name()
        try:
            entry_list, entry_type = category.split(': ')
        except ValueError:
            raise ValueError(f"Category name was not in [List: Type] format: {category}")
        return self.Maps[map_choice].get_entity_id_dict(entry_list, entry_type)

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns entire dictionary (no previous/next range buttons here)."""
        return list(self.get_category_dict(category).items())

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Returns index of given entry ID (entity ID) in dictionary."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No text category selected.")
        return list(self.get_category_dict(category)).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        entry_list = self.get_category_dict(category)
        return entry_list[entry_id].name

    def _set_entry_text(self, entry_index: int, text: str, category=None, update_row_index=None):
        entry_list = self.get_category_dict(category)
        entry_list[entry_index].name = text  # Will update Maps tab as well (once refreshed).
        # TODO: Might want to manually refresh corresponding Maps entry text with linker.
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_index, text)

    def _change_entry_id(self, row_index, new_id, category=None):
        """Changes 'entity_id' of MSB entry."""
        if category is None:
            category = self.active_category
        old_id = self.get_entry_id(row_index)
        if old_id == new_id:
            return False
        entry_list = self.get_category_dict(category)
        if new_id in entry_list:
            self.dialog("Entry ID Clash", f"Entry ID {new_id} already exists in Maps.{category}. You must change or "
                                          f"delete it first.")
            return False
        # Change 'entity_id' field of MSBEntry.
        entry_list[old_id].entity_id = new_id  # TODO: Might want to manually refresh corresponding Maps entry text.
        entry_list[new_id] = entry = entry_list.pop(old_id)
        if category == self.active_category and self.EntryRow.SHOW_ENTRY_ID:
            self.entry_rows[row_index].update_entry(new_id, entry.name)
        return True
