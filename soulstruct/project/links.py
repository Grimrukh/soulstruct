from __future__ import annotations
import re
from typing import TYPE_CHECKING

from soulstruct.maps import MAP_ENTRY_TYPES

if TYPE_CHECKING:
    from soulstruct.project.core import SoulstructProjectWindow
    from soulstruct.maps import MSB


class WindowLinker(object):
    """Interface that generates links (go-to commands) between arbitrary parts of the Soulstruct unified window."""
    _MATCH_LINK = re.compile(r'<(.*)>')

    def __init__(self, window: SoulstructProjectWindow):
        self.window = window
        self.project = window.project

    def get_tab_index(self, tab_name):
        return self.window.TAB_ORDER.index(tab_name.lower())

    def soulstruct_link(self, field_type, field_value, valid_null_values: dict = None):
        """Some field values are IDs to look up from other parameters or other types of game files (texture IDs,
        animation IDs, AI script IDs, etc.). These are coded as tags in the field information dictionary, and
        resolved here."""

        if valid_null_values is None:
            valid_null_values = {}

        match_link = self._MATCH_LINK.match(field_type)
        if not match_link:
            raise ValueError(f"Invalid link: {field_type}")

        name_extension = ''
        link_text = match_link.group(1)

        if ':' not in link_text:
            return []  # TODO: haven't supported certain simple IDs yet (e.g. Flag, Animation, ...)

        link_pieces = link_text.split(':')
        table_type = link_pieces[0]

        if table_type == 'MapsList':
            links = []
            field_type = f'<Maps:{":".join(link_pieces[1:])}>'
            for entry_name in field_value:
                if not entry_name:
                    continue
                links += self.soulstruct_link(field_type, entry_name)
            return links

        if table_type == 'Maps':
            entry_name = field_value
            if not entry_name:  # None or empty string
                return [BaseLink(self, name='None')]
            active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
            entry_list_name = link_pieces[1]
            if entry_list_name not in MAP_ENTRY_TYPES:
                raise ValueError(f"Invalid map entry list: {entry_list_name}")
            entry_list = active_msb[entry_list_name]

            try:
                entry_local_index = entry_list.get_entry_type_index(entry_name)

                if len(link_pieces) == 3:
                    # Technically, map links only care about entry list type, but I'm sometimes adding some additional
                    # enforcement (like parts.characters[i].model_index linking to models.characters only).
                    entry_types = [MAP_ENTRY_TYPES[entry_list_name][entry_type].name
                                   for entry_type in link_pieces[2].split('|')]
                    if entry_list[entry_name].ENTRY_TYPE.name not in entry_types:
                        raise ValueError("Type of entry name in field does not match enforced type of field.")

                # Need plural form of entry type.
                entry_type_name = [key for key in MAP_ENTRY_TYPES[entry_list_name]
                                   if MAP_ENTRY_TYPES[entry_list_name][key] == entry_list[entry_name].ENTRY_TYPE][0]

            except ValueError:
                # Entry name is missing (or is not of the enforced entry type).
                return []

            return [MapsLink(
                self, name=field_value, entry_list_name=entry_list_name, entry_type_name=entry_type_name,
                entry_local_index=entry_local_index)]

        if field_value in valid_null_values:
            return [BaseLink(self, name=valid_null_values[field_value])]

        category = link_pieces[1]

        if table_type == 'Text':
            text_table = self.project.Text[category]
            if field_value not in text_table:
                return [BaseLink()]
            return [TextLink(self, category=category, text_id=field_value, name=text_table[field_value])]

        if table_type == 'Params':
            if category in {'Attacks', 'Behaviors'}:
                # Try to determine Player vs. Non Player table.
                if category == 'Attacks':
                    if self.window.params_tab.active_category == 'PlayerBehaviors':
                        category = 'PlayerAttacks'
                    elif self.window.params_tab.active_category == 'NonPlayerBehaviors':
                        category = 'NonPlayerAttacks'
                elif category == 'Behaviors':
                    if self.window.params_tab.active_category == 'Players':
                        category = 'PlayerBehaviors'
                if category in {'Attacks', 'Behaviors'}:
                    # Could be Player or Non Player. Provide both links.
                    player_table = self.project.Params['Player' + category]
                    non_player_table = self.project.Params['NonPlayer' + category]
                    if field_value not in player_table and field_value not in non_player_table:
                        return [BaseLink()]
                    links = []
                    if field_value in player_table:
                        links.append(ParamsLink(
                            self, category='Player' + category, param_entry_id=field_value,
                            name=player_table[field_value]))
                    if field_value in player_table:
                        links.append(ParamsLink(
                            self, category='NonPlayer' + category, param_entry_id=field_value,
                            name=player_table[field_value]))
                    if links:
                        return links
                    return [BaseLink()]

            if category in {'Armor', 'Weapons'}:
                true_param_id = (self.check_armor_id(field_value) if category == 'Armor'
                                 else self.check_weapon_id(field_value))
                if true_param_id is None:
                    return [BaseLink()]  # Invalid weapon/armor ID, even considering reinforcement.
                if field_value != true_param_id:
                    name_extension = '+' + str(field_value - true_param_id)
                field_value = true_param_id

            param_table = self.project.Params[category]
            try:
                name = param_table[field_value].name + name_extension
            except KeyError:
                return [BaseLink()]
            else:
                return [ParamsLink(self, category=category, param_entry_id=field_value, name=name)]

        return []  # No other table types supported yet.

    def get_map_entry_type_names(self, field_type):
        match_link = self._MATCH_LINK.match(field_type)
        if not match_link:
            raise ValueError(f"Invalid link: {field_type}")

        link_text = match_link.group(1)

        if ':' not in link_text:
            return []  # TODO: haven't supported certain simple IDs yet (e.g. Flag, Animation, ...)

        link_pieces = link_text.split(':')
        table_type = link_pieces[0]

        if table_type == 'Maps':
            active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
            entry_list_name = link_pieces[1]
            if entry_list_name not in MAP_ENTRY_TYPES:
                raise ValueError(f"Invalid map entry list: {entry_list_name}")
            entry_list = active_msb[entry_list_name]

            if len(link_pieces) == 3:
                # Technically, map links only care about entry list type, but I'm sometimes adding some additional
                # enforcement (like parts.characters[i].model_index linking to models.characters only).
                names = []
                for name in link_pieces[2].split('|'):
                    names += entry_list.get_entry_names(entry_type=name)
                return names
            else:
                return entry_list.get_entry_names()

    def param_entry_text_link(self, entry_id):
        """Return three (name, link) pairs for entries in item categories (Name, Summary, and Description).

        Returns empty list if no link is appropriate, and returns an empty tuple if text *should* exist but cannot be
        found.
        """
        param_category = self.window.params_tab.active_category
        if param_category not in {'Weapons', 'Armor', 'Rings', 'Goods', 'Spells'}:
            return []
        text_ids = {'Names': entry_id, 'Summaries': entry_id, 'Descriptions': entry_id}
        links = []

        prefix = param_category.rstrip('s')

        if param_category == 'Weapons':
            base_weapon_id = self.check_weapon_id(entry_id)
            if base_weapon_id is not None:
                text_ids['Summaries'] = base_weapon_id
                text_ids['Descriptions'] = base_weapon_id
        elif param_category == 'Armor':
            base_armor_id = self.check_armor_id(entry_id)
            if base_armor_id is not None:
                text_ids['Summaries'] = base_armor_id
                text_ids['Descriptions'] = base_armor_id
        for text_category, text_id in text_ids.items():
            if text_ids[text_category] not in self.project.Text[prefix + text_category]:
                links.append(BaseLink())
            else:
                links.append(TextLink(
                    self, category=prefix + text_category, text_id=text_id,
                    name=self.project.Text[prefix + text_category][text_id]))

        return links

    def check_armor_id(self, armor_id):
        """Checks if the given armor ID (which may include a reinforcement offset) is valid by inspecting the
        Weapons table, then returns the base armor ID (with no reinforcement) or None if invalid."""
        level = armor_id % 100
        if level > 10:
            return None
        if level == 0:
            return armor_id
        base_armor = armor_id - level
        origin_field = 'originEquipPro' + ('' if level == 0 else str(level))
        try:
            origin = self.project.Params['Armor'][base_armor][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_armor

    def check_weapon_id(self, weapon_id):
        """Checks if the given weapon ID (which may include a reinforcement offset) is valid by inspecting the
        Weapons table, then returns the base weapon ID (with no reinforcement) or None if invalid."""
        level = weapon_id % 100
        if level > 15:
            return None
        if level == 0:
            return weapon_id
        base_weapon = weapon_id - level
        origin_field = 'originEquipWep' + ('' if level == 0 else str(level))
        try:
            origin = self.project.Params['Weapons'][base_weapon][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_weapon

    def text_link(self, category, text_id):
        self.window.page_tabs.select(self.get_tab_index('text'))
        # TODO: Create entry if missing.
        self.window.text_tab.select_category(category)
        self.window.text_tab.select_entry_id(text_id)
        self.window.text_tab.update_idletasks()

    def maps_link(self, entry_list_name, entry_type_name, entry_local_index):
        self.window.maps_tab.select_displayed_field_row(None)
        self.window.page_tabs.select(self.get_tab_index('maps'))
        self.window.maps_tab.refresh_categories()
        category = f'{entry_list_name}:{entry_type_name}'
        self.window.maps_tab.select_category(category)
        view_ratio = self.window.maps_tab.get_category_position_ratio(category)
        self.window.maps_tab.category_canvas.yview_moveto(view_ratio)
        self.window.maps_tab.select_entry_id(entry_local_index, edit_if_already_selected=False)
        self.window.maps_tab.update_idletasks()

    def params_link(self, category, param_entry_id, field_name=None):
        # TODO: Create if missing.
        if param_entry_id not in self.window.params_tab.get_category_dict(category).entries:
            self.window.dialog("Param ID Missing", f"Param ID {param_entry_id} is missing from Params.{category}.")
            return
        self.window.page_tabs.select(self.get_tab_index('params'))
        self.window.params_tab.select_category(category)
        self.window.params_tab.select_entry_id(param_entry_id)
        if field_name is not None:
            self.window.params_tab.select_field_name(field_name)
        self.window.params_tab.update_idletasks()


class BaseLink(object):
    def __init__(self, linker: WindowLinker = None, name=None, menu_text=None):
        """Bundles right-click context menu text with a GUI-jumping link callback, with an optional name.

        Args:
            name: Name that will appear in curly braces {} next to ID. If None, no name will appear.
            menu_text: Text that will appear in right-click menu. Usually "Go to [type]". If None (default), no right
                click option will be given.
        """
        self.linker = linker
        self.name = name
        self.menu_text = menu_text

    def add_to_context_menu(self, context_menu, **kwargs):
        if self.menu_text:
            context_menu.add_command(label=self.menu_text, command=self, **kwargs)

    def __call__(self):
        raise NotImplementedError


class NullLink(BaseLink):
    """Dummy link for a normally-linked field has a null value, usually 0 or -1, which means the field is unused or set
    to a default. Simply displays '{None/Default}' next to name."""
    def __init__(self, linker: WindowLinker):
        super().__init__(linker, name='None/Default', menu_text='')

    def __call__(self):
        raise AttributeError("Null link cannot be called.")


class ParamsLink(BaseLink):
    def __init__(self, linker, category, param_entry_id, name=None):
        super().__init__(
            linker, name=name,
            menu_text=f"Go to Params.{category}[{param_entry_id}]" + f"  {{{name}}}" if name is not None else "")
        self.category = category
        self.param_entry_id = param_entry_id

    def __call__(self):
        self.linker.params_link(self.category, self.param_entry_id)


class TextLink(BaseLink):
    def __init__(self, linker, category, text_id, name=None):
        super().__init__(linker, name=name, menu_text=f"Go to Text.{category}[{text_id}]")
        self.category = category
        self.text_id = text_id

    def __call__(self):
        self.linker.text_link(self.category, self.text_id)


class MapsLink(BaseLink):
    def __init__(self, linker, entry_list_name, entry_local_index, entry_type_name, name=None):
        super().__init__(
            linker, name=name,
            menu_text=f"Go to Maps.{entry_list_name}"
                      f"{'.' + entry_type_name if entry_type_name is not None else ''}[{entry_local_index}]"
                      f" {{{name}}}")
        self.entry_list_name = entry_list_name
        self.entry_type_name = entry_type_name
        self.entry_local_index = entry_local_index

    def __call__(self):
        self.linker.maps_link(self.entry_list_name, self.entry_type_name, self.entry_local_index)
