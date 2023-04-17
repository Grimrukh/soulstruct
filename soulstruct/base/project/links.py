from __future__ import annotations

__all__ = [
    "WindowLinker",
    "LinkError",
    "BaseLink",
    "BrokenLink",
    "NullLink",
    "MapsLink",
    "ParamsLink",
    "TextLink",
    "LightingLink",
]

import abc
import typing as tp

from soulstruct.exceptions import SoulstructError
from soulstruct.base.game_types import *

from .utilities import ItemTextEditBox

if tp.TYPE_CHECKING:
    from soulstruct.base.project.window import ProjectWindow
    from soulstruct.base.project.editors.field_editor import BaseFieldEditor
    from soulstruct.base.maps.msb import MSB, MSBEntry


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
        self, field_type: GAME_TYPE, field_value, valid_null_values: dict = None, map_override=None,
    ) -> list[BaseLink]:
        """Some field types are `GameObjectInt` subclasses, which means that the field values are IDs to look up.

        Currently, only `MapEntry`, `Text`, and `BaseGameParam` field types are supported here. In the future,
        `Texture`, `Animation`, `AIScriptBase` etc. will also be supported.
        """
        if valid_null_values is None:
            valid_null_values = {}

        if issubclass(field_type, MapEntry):
            field_value: MSBEntry
            return self.map_entry_link(field_type, entry=field_value)

        # This is the right time to check for null values.
        if field_value in valid_null_values:
            return [NullLink(self, name=valid_null_values[field_value])]

        if issubclass(field_type, Text):
            return self.text_link(field_type, field_value)

        if issubclass(field_type, BaseGameParam):
            return self.game_param_link(field_type, field_value)

        # No other cross-game base data types (Texture, Map, Animation, etc.) supported yet.

        return self.check_other_link_types(field_type, field_value, valid_null_values, map_override)

    def map_entry_link(self, entry_game_type: tp.Type[MapEntry], entry: MSBEntry | None):
        if not entry:  # no link expected (reference is `None`)
            return [NullLink(self, name="None")]
        entry_supertype_name, entry_subtype_name = entry_game_type.get_msb_entry_supertype_subtype()
        active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB

        try:
            entry_list = active_msb.get_list_of_entry(entry)
        except ValueError:
            # Entry name is missing.
            return [BrokenLink()]

        if entry_subtype_name is not None:
            # Technically, map links only care about entry list type, (except for the collision field of Map
            # Connections and the Environment field of Collisions), but I'm sometimes adding some additional subtype
            # enforcement (e.g. model types).
            if entry.name == "c0000" and entry_subtype_name in ("CharacterModel", "PlayerModel"):
                # c0000 model can have Character or Player subtype.
                pass
            elif entry.SUBTYPE_ENUM.name == "UnusedObject" and entry_subtype_name in {"Object", "Asset"}:
                pass
            elif entry.SUBTYPE_ENUM.name == "UnusedCharacter" and entry_subtype_name == "Character":
                pass
            elif entry.SUBTYPE_ENUM.name != entry_subtype_name:
                raise ValueError(
                    f"Type of entry name in field ({entry.SUBTYPE_ENUM.name}) "
                    f"does not match enforced type of field ({entry_subtype_name})."
                )
        try:
            entry_subtype_index = entry_list.index_entry(entry)
            pluralized_name = entry.SUBTYPE_ENUM.pluralized_name
            if pluralized_name in {"CharacterModels", "PlayerModels"} and entry.name == "c0000":
                # Check if map has `c0000` model (as every map should).
                if not active_msb.has_c0000_model():
                    raise LinkError(f"Could not find player model c0000 in Character or Player model lists.")
            return [
                MapsLink(
                    self,
                    entry=entry,
                    entry_supertype_name=entry_supertype_name,
                    entry_subtype_name=pluralized_name,
                    entry_subtype_index=entry_subtype_index,
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

    def game_param_link(self, field_type: tp.Type[BaseGameParam], field_value: int):
        param_nickname = field_type.get_param_nickname()
        param = self.project.params.get_param(param_nickname)
        try:
            name = param[field_value].Name
        except KeyError:
            return [BrokenLink()]
        else:
            return [ParamsLink(self, param_name=param_nickname, param_entry_id=field_value, name=name)]

    def check_other_link_types(self, field_type, field_value, valid_null_values: dict, map_override) -> list[BaseLink]:
        """Override this to check other game-specific types for links."""
        return []

    def get_map_entry_subtype_list(self, entry_game_type: GAME_TYPE) -> list[MSBEntry]:
        """Retrieves a list of MSB entries of the given type."""
        if not issubclass(entry_game_type, MapEntry):
            raise TypeError(f"Invalid field type. Must be a `MapEntry` subtype, not: {entry_game_type.__name__}")

        entry_supertype_name, entry_subtype_name = entry_game_type.get_msb_entry_supertype_subtype()
        active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
        if entry_subtype_name:
            # Handle annoying special case: `c0000` model can appear as a Character or Player model.
            if entry_supertype_name == "Models" and entry_subtype_name in {"CharacterModel", "PlayerModel"}:
                return list(active_msb["CharacterModel"]) + list(active_msb["PlayerModel"])
            return list(active_msb[entry_subtype_name])
        return active_msb.get_supertype_list(entry_supertype_name)

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
            if text_ids[text_category] not in self.project.text[prefix + text_category].entries:
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
    def validate_model_subtype(self, model_game_type: tp.Type[MapModel], model_name: str, map_stem: str):
        """Check appropriate game model files to confirm the given model name is valid."""
        ...

    # region Link Execution
    def execute_text_link(self, text_type_name, text_id):
        self.window.page_tabs.select(self.get_tab_index("text"))
        # TODO: Create entry if missing.
        self.window.text_tab.select_category(text_type_name)
        self.window.text_tab.select_entry_id(text_id, edit_if_already_selected=False)
        self.window.text_tab.update_idletasks()

    def execute_maps_link(self, entry_supertype_name, entry_subtype_name, entry_subtype_index):
        self.window.maps_tab.select_displayed_field_row(None)
        self.window.page_tabs.select(self.get_tab_index("maps"))
        self.window.maps_tab.refresh_categories()  # TODO: why do I need to call this?
        category = f"{entry_supertype_name}: {entry_subtype_name}"
        self.window.maps_tab.select_category(category, auto_scroll=True)
        self.window.maps_tab.select_entry_id(entry_subtype_index, edit_if_already_selected=False)
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
    # TODO: Supertype name may no longer be needed. (I think it's used to get the dropdown category name.)
    def __init__(self, linker, entry, entry_supertype_name, entry_subtype_index, entry_subtype_name):
        super().__init__(
            linker,
            name=entry.name,
            menu_text=f"Go to Maps.{entry_supertype_name}"
            f"{'.' + entry_subtype_name if entry_subtype_name is not None else ''}[{entry_subtype_index}]"
            f" {{{entry.name}}}",
        )
        self.entry = entry
        self.entry_supertype_name = entry_supertype_name
        self.entry_subtype_name = entry_subtype_name
        self.entry_subtype_index = entry_subtype_index

    def __call__(self):
        self.linker.execute_maps_link(self.entry_supertype_name, self.entry_subtype_name, self.entry_subtype_index)


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
