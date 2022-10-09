from __future__ import annotations

__all__ = ["WindowLinker", "LinkError"]

import abc
import typing as tp

from soulstruct.exceptions import SoulstructError
from soulstruct.base.game_types import *
from soulstruct.base.maps.msb.enums import BaseMSBModelSubtype

from .utilities import ItemTextEditBox

if tp.TYPE_CHECKING:
    from soulstruct.base.project.window import ProjectWindow
    from soulstruct.base.project.editors.field_editor import BaseFieldEditor
    from soulstruct.base.maps.msb import MSB


class LinkError(SoulstructError):
    pass


class WindowLinker:
    """Interface that generates links (go-to commands) between arbitrary parts of the Soulstruct unified window."""

    def __init__(self, window: ProjectWindow):
        self.window = window
        self.project = window.project

    def get_tab_index(self, tab_name):
        return self.window.ordered_tabs.index(tab_name.lower())

    def jump(self, tab_name, category, entry_id, field_name=None, choice_func=None):
        data_tab = getattr(self.window, f"{tab_name}_tab")  # type: BaseFieldEditor
        self.window.page_tabs.select(self.get_tab_index(tab_name))
        try:
            if choice_func is not None:
                choice_func()  # e.g. changing map choice combobox
            data_tab.select_category(category, auto_scroll=True)
            data_tab.select_entry_id(entry_id, edit_if_already_selected=False)
            if field_name is not None:
                data_tab.select_field_name(field_name)
        except (IndexError, KeyError):
            return False  # Jump failed.
        return True  # Jump succeeded.

    def soulstruct_link(
        self, field_type, field_value, valid_null_values: dict = None, map_override=None,
    ) -> list[BaseLink]:
        """Some field types are `GameObject` subclasses, which means that the field values are IDs to look up.

        Currently, only `MapEntry`, `Text`, and `BaseGameParam` field types are supported here. In the future,
        `Texture`, `Animation`, `AIScriptBase` etc. will also be supported.
        """
        if valid_null_values is None:
            valid_null_values = {}

        if issubclass(field_type, MapEntry):
            return self.map_entry_link(field_type, field_value)

        # This is the right time to check for null values.
        if field_value in valid_null_values:
            return [NullLink(self, name=valid_null_values[field_value])]

        if issubclass(field_type, Text):
            return self.text_link(field_type, field_value)

        if issubclass(field_type, BaseGameParam):
            return self.game_param_link(field_type, field_value)

        # No other cross-game base data types (Texture, Map, Animation, etc.) supported yet.

        return self.check_other_link_types(field_type, field_value, valid_null_values, map_override)

    def map_entry_link(self, field_type, field_value):
        entry_name = field_value
        if not entry_name:  # no link expected (None or empty string)
            return [NullLink(self, name="None")]
        entry_type_name, entry_subtype_name = field_type.get_msb_entry_type_subtype()
        active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
        entry_list = active_msb[entry_type_name]
        try:
            entry = entry_list[entry_name]
        except KeyError:
            # Entry name is missing.
            return [BrokenLink()]
        if entry_subtype_name is not None:
            # Technically, map links only care about entry list type (except for the collision field of Map
            # Connections) but I'm sometimes adding some additional subtype enforcement (e.g. model types).
            if (
                entry.ENTRY_SUBTYPE.name == "Player" and entry_subtype_name == "Character"
                and entry_name == "c0000"
            ):
                # c0000 model happens to be in "Player" category for this map.
                pass
            elif entry.ENTRY_SUBTYPE.name == "UnusedObject" and entry_subtype_name == "Object":
                pass
            elif entry.ENTRY_SUBTYPE.name == "UnusedCharacter" and entry_subtype_name == "Character":
                pass
            elif entry.ENTRY_SUBTYPE.name != entry_subtype_name:
                raise ValueError(
                    f"Type of entry name in field ({entry.ENTRY_SUBTYPE.name}) "
                    f"does not match enforced type of field ({entry_subtype_name})."
                )
        try:
            entry_local_index = entry_list.get_entry_subtype_index(entry_name)
            entry_subtype = entry.ENTRY_SUBTYPE
            pluralized_name = entry_subtype.pluralized_name
            if pluralized_name == "Characters" and field_value == "c0000":
                if not [model for model in getattr(entry_list, "Characters") if model.name == "c0000"]:
                    if not [model for model in getattr(entry_list, "Players") if model.name == "c0000"]:
                        raise LinkError(f"Could not find player model c0000 in Character or Player model lists.")
                    pluralized_name = "Players"  # redirect c0000 to 'Player' models
            return [
                MapsLink(
                    self,
                    name=field_value,
                    entry_type_name=entry_type_name,
                    entry_subtype_name=pluralized_name,
                    entry_local_index=entry_local_index,
                )
            ]
        except (KeyError, ValueError):
            # Entry name is missing (or is not of the enforced entry type).
            return [BrokenLink()]

    def text_link(self, field_type, field_value):
        text_category_name = field_type.get_text_category()
        text_table = self.project.text[text_category_name]
        if field_value not in text_table:
            return [BrokenLink()]
        text = text_table[field_value]
        return [TextLink(self, text_type_name=text_category_name, text_id=field_value, name=text)]

    def game_param_link(self, field_type, field_value):
        param_nickname = field_type.get_param_nickname()
        param_table = self.project.params.get_param(param_nickname)
        try:
            name = param_table[field_value].name
        except KeyError:
            return [BrokenLink()]
        else:
            return [ParamsLink(self, param_name=param_nickname, param_entry_id=field_value, name=name)]

    def check_other_link_types(self, field_type, field_value, valid_null_values: dict, map_override) -> list[BaseLink]:
        """Override this to check other game-specific types for links."""
        return []

    def get_map_entry_type_names(self, field_type: type):
        """Retrieves a list of names of the given type, sometimes with hint suffixes.

        Currently only supports `MapEntry` fields.
        """
        if issubclass(field_type, MapEntry):
            entry_type_name, entry_subtype_name = field_type.get_msb_entry_type_subtype()
            active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
            entry_list = active_msb[entry_type_name]
            if entry_subtype_name is not None:
                # Technically, map links only care about entry list type (except for the collision field of Map
                # Connections) but I'm sometimes adding some additional subtype enforcement (e.g. model types).
                names = entry_list.get_entry_names(entry_subtype=entry_subtype_name)
                if entry_type_name == "Models" and entry_subtype_name in {"Character", "Player"}:
                    # Add model names as suffixes.
                    for i, name in enumerate(names):
                        model_id = int(name.lstrip("c"))
                        names[i] += f"  {{{self.window.CHARACTER_MODELS.get(model_id, 'UNKNOWN')}}}"
                return names
            else:
                return entry_list.get_entry_names()
        # TODO: raise type error?

    def get_param_entry_text_links(self, entry_id):
        """Return three (name, link) pairs for entries in item categories (Name, Summary, and Description).

        Returns empty list if no link is appropriate, and returns an empty tuple if text *should* exist but cannot be
        found.
        """
        param_category = self.window.params_tab.active_category
        if param_category not in {"Weapons", "Armor", "Rings", "Goods", "Spells"}:
            return []
        text_ids = {"Names": entry_id, "Summaries": entry_id, "Descriptions": entry_id}
        links = []

        prefix = param_category.rstrip("s")

        if param_category == "Weapons":
            base_weapon_id = self.check_weapon_id(entry_id)
            if base_weapon_id is not None:
                text_ids["Summaries"] = base_weapon_id
                text_ids["Descriptions"] = base_weapon_id
        elif param_category == "Armor":
            base_armor_id = self.check_armor_id(entry_id)
            if base_armor_id is not None:
                text_ids["Summaries"] = base_armor_id
                text_ids["Descriptions"] = base_armor_id
        for text_category, text_id in text_ids.items():
            if text_ids[text_category] not in self.project.text[prefix + text_category]:
                links.append(BrokenLink())
            else:
                links.append(
                    TextLink(
                        self,
                        text_type_name=prefix + text_category,
                        text_id=text_id,
                        name=self.project.text[prefix + text_category][text_id],
                    )
                )

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
        origin_field = "originEquipPro" + ("" if level == 0 else str(level))
        try:
            origin = self.project.params.get_param("Armor")[base_armor][origin_field]
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
        origin_field = "originEquipWep" + ("" if level == 0 else str(level))
        try:
            origin = self.project.params.get_param("Weapons")[base_weapon][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_weapon

    @abc.abstractmethod
    def validate_model_subtype(self, model_subtype: BaseMSBModelSubtype, name: str, map_id: str):
        """Check appropriate game model files to confirm the given model name is valid."""
        ...

    # region Link Execution
    def execute_text_link(self, text_type_name, text_id):
        self.window.page_tabs.select(self.get_tab_index("text"))
        # TODO: Create entry if missing.
        self.window.text_tab.select_category(text_type_name)
        self.window.text_tab.select_entry_id(text_id, edit_if_already_selected=False)
        self.window.text_tab.update_idletasks()

    def execute_maps_link(self, entry_list_name, entry_type_name, entry_local_index):
        self.window.maps_tab.select_displayed_field_row(None)
        self.window.page_tabs.select(self.get_tab_index("maps"))
        self.window.maps_tab.refresh_categories()  # TODO: why do I need to call this?
        category = f"{entry_list_name}: {entry_type_name}"
        self.window.maps_tab.select_category(category, auto_scroll=True)
        self.window.maps_tab.select_entry_id(entry_local_index, edit_if_already_selected=False)
        self.window.maps_tab.update_idletasks()

    def execute_params_link(self, param_name, param_entry_id, field_name=None):
        # TODO: Create if missing.
        if param_entry_id not in self.window.params_tab.get_category_data(param_name):
            self.window.CustomDialog(
                title="Param ID Missing", message=f"Param ID {param_entry_id} is missing from Params.{param_name}."
            )
            return
        self.window.page_tabs.select(self.get_tab_index("params"))
        self.window.params_tab.select_category(param_name)
        self.window.params_tab.select_entry_id(param_entry_id)
        if field_name is not None:
            self.window.params_tab.select_field_name(field_name)
        self.window.params_tab.update_idletasks()

    def execute_lighting_link(self, param_name, map_area_name, param_entry_id, lighting_slot=0, field_name=None):
        # TODO: Create if missing.
        if param_entry_id not in self.window.lighting_tab.get_category_data(param_name):
            self.window.CustomDialog(
                title="Lighting ID Missing",
                message=f"Lighting ID {param_entry_id} is missing from Lighting.{param_name}.",
            )
            return
        self.window.page_tabs.select(self.get_tab_index("lighting"))
        self.window.lighting_tab.select_category(param_name)
        self.window.lighting_tab.go_to_area_and_slot(map_area_name, lighting_slot)
        self.window.lighting_tab.select_entry_id(param_entry_id)
        if field_name is not None:
            self.window.lighting_tab.select_field_name(field_name)
        self.window.lighting_tab.update_idletasks()
    # endregion

    def runtime_hook(self):
        return self.window.runtime_tab.hook_into_game()

    @property
    def hook_created(self):
        return self.window.runtime_tab.hook_created

    def get_game_value(self, value_name):
        """Try to retrieve given game value (e.g. 'player_x') from runtime memory hook."""
        return self.window.runtime_tab.get_game_value(value_name)

    def edit_all_item_text(self, item_type, item_id):
        """Edit name, summary, and description of item (weapon, armor, ring, good, or spell) simultaneously.

        Name must be specified. If summary and/or description are left empty, they will NOT be modified or created.

        Note that for new Armor entries, the default summary text is a single blank space rather than empty text. For
        new Weapon entries, the default summary text is 'WeaponType', to remind you to specify it.
        """
        name = getattr(self.project.text, item_type + "Names").get(item_id, "")
        summary = getattr(self.project.text, item_type + "Summaries").get(item_id, "")
        if not summary:
            if item_type == "Weapon":
                summary = "[weapon type goes here]"  # reminder to user to specify weapon type as summary
            elif item_type == "Armor":
                summary = " "  # Armor summary defaults to a single blank space.
        description = getattr(self.project.text, item_type + "Descriptions").get(item_id, "")
        name, summary, description = ItemTextEditBox(
            self.window, name, summary, description, f"Editing {item_type}[{item_id}]"
        ).go()
        if not name:
            raise ValueError("Item name cannot be empty.")
        getattr(self.project.text, item_type + "Names")[item_id] = name
        if summary:
            getattr(self.project.text, item_type + "Summaries")[item_id] = summary
        if description:
            getattr(self.project.text, item_type + "Descriptions")[item_id] = description


class BaseLink(abc.ABC):
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

    @abc.abstractmethod
    def __call__(self):
        ...


class BrokenLink(BaseLink):
    """Link with an invalid, non-default value that cannot be found in the target table/file."""
    def __init__(self):
        super().__init__()  # all None

    def __call__(self):
        raise AttributeError("Broken link cannot be called.")


class NullLink(BaseLink):
    """Dummy link for a normally-linked field that has a null value, usually 0 or -1, which means the field is unused or
    set to a default. Will simply display `name`, eg '{Default/None}', next to field value."""

    def __init__(self, linker: WindowLinker, name="Default/None"):
        super().__init__(linker, name=name, menu_text="")

    def __call__(self):
        raise AttributeError("Null link cannot be called.")


class MapsLink(BaseLink):
    def __init__(self, linker, entry_type_name, entry_local_index, entry_subtype_name, name=None):
        super().__init__(
            linker,
            name=name,
            menu_text=f"Go to Maps.{entry_type_name}"
            f"{'.' + entry_subtype_name if entry_subtype_name is not None else ''}[{entry_local_index}]"
            f" {{{name}}}",
        )
        self.entry_list_name = entry_type_name
        self.entry_type_name = entry_subtype_name
        self.entry_local_index = entry_local_index

    def __call__(self):
        self.linker.execute_maps_link(self.entry_list_name, self.entry_type_name, self.entry_local_index)


class ParamsLink(BaseLink):
    def __init__(self, linker, param_name, param_entry_id, name=None):
        super().__init__(
            linker,
            name=name,
            menu_text=f"Go to Params.{param_name}[{param_entry_id}]" + f"  {{{name}}}" if name is not None else "",
        )
        self.param_name = param_name
        self.param_entry_id = param_entry_id

    def __call__(self):
        self.linker.execute_params_link(self.param_name, self.param_entry_id)


class TextLink(BaseLink):
    def __init__(self, linker, text_type_name, text_id, name=None):
        super().__init__(linker, name=name, menu_text=f"Go to Text.{text_type_name}[{text_id}]")
        self.text_type_name = text_type_name
        self.text_id = text_id

    def __call__(self):
        self.linker.execute_text_link(self.text_type_name, self.text_id)


class LightingLink(BaseLink):
    """TODO: If/when I implemented GParam window, this will probably change to a base class for DrawParam AND GParam."""
    def __init__(self, linker, param_name, map_area_name, param_entry_id, slot=0, name=None):
        super().__init__(
            linker,
            name=name,
            menu_text=f"Go to Lighting.{param_name}[{param_entry_id}]" + f"  {{{name}}}" if name is not None else "",
        )
        self.param_name = param_name
        self.map_area_name = map_area_name
        self.param_entry_id = param_entry_id
        self.lighting_slot = slot

    def __call__(self):
        self.linker.execute_lighting_link(self.param_name, self.map_area_name, self.param_entry_id, self.lighting_slot)
