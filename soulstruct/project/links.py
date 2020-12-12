from __future__ import annotations

__all__ = ["WindowLinker", "LinkError"]

import typing as tp

from soulstruct.bnd.core import BND
from soulstruct.game_types import *
from soulstruct.maps.enums import MSBModelSubtype
from soulstruct.maps.base.models import MSBModelList
from soulstruct.models.darksouls1 import CHARACTER_MODELS
from soulstruct.core import SoulstructError
from soulstruct.project.utilities import ItemTextEditBox

if tp.TYPE_CHECKING:
    from soulstruct.project import SoulstructProjectWindow
    from soulstruct.project.base.field_editor import SoulstructBaseFieldEditor
    from soulstruct.maps import MSB


class LinkError(SoulstructError):
    pass


class WindowLinker:
    """Interface that generates links (go-to commands) between arbitrary parts of the Soulstruct unified window."""

    def __init__(self, window: SoulstructProjectWindow):
        self.window = window
        self.project = window.project

    def get_tab_index(self, tab_name):
        return self.window.TAB_ORDER.index(tab_name.lower())

    def jump(self, tab_name, category, entry_id, field_name=None, choice_func=None):
        data_tab = getattr(self.window, f"{tab_name}_tab")  # type: SoulstructBaseFieldEditor
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
    ) -> tp.List[BaseLink]:
        """Some field types are `GameObject` subclasses, which means that the field values are IDs to look up.

        Currently, only `MapEntry`, `Text`, and `BaseParam` field types are supported here. In the future, `Texture`,
        `Animation`, `AIScriptBase` etc. will also be supported.
        """

        if valid_null_values is None:
            valid_null_values = {}

        name_extension = ""

        if issubclass(field_type, MapEntry):
            entry_name = field_value
            if not entry_name:  # No link expected (None or empty string)
                return [BaseLink(self, name="None")]
            entry_type_name, entry_subtype_name = field_type.get_msb_entry_type_subtype()
            active_msb = self.window.maps_tab.get_selected_msb()  # type: MSB
            entry_list = active_msb[entry_type_name]
            try:
                entry = entry_list[entry_name]
            except KeyError:
                # Entry name is missing.
                return [BaseLink()]
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
                return [BaseLink()]

        # This is the right time to check for null values.
        if field_value in valid_null_values:
            return [BaseLink(self, name=valid_null_values[field_value])]

        if issubclass(field_type, Text):
            text_category_name = field_type.get_text_category()
            text_table = self.project.Text[text_category_name]
            if field_value not in text_table:
                return [BaseLink()]
            text = text_table[field_value]
            return [TextLink(self, text_type_name=text_category_name, text_id=field_value, name=text)]

        if issubclass(field_type, BaseGameParam):
            if field_type in {AttackParam, BehaviorParam}:
                # Try to determine Player vs. Non Player table.
                param_nickname = ""
                if field_type == AttackParam:
                    if self.window.params_tab.active_category == "PlayerBehaviors":
                        param_nickname = "PlayerAttacks"
                    elif self.window.params_tab.active_category == "NonPlayerBehaviors":
                        param_nickname = "NonPlayerAttacks"
                elif field_type == BehaviorParam:
                    if self.window.params_tab.active_category == "Players":
                        param_nickname = "PlayerBehaviors"
                if not param_nickname:
                    # Could be Player or Non Player. Provide both links.
                    param_nickname = "Attacks" if field_type == AttackParam else "Behaviors"
                    player_table = self.project.Params[f"Player{param_nickname}"]
                    non_player_table = self.project.Params[f"NonPlayer{param_nickname}"]
                    links = []
                    if field_value in player_table:
                        links.append(
                            ParamsLink(
                                self,
                                param_name=f"Player{param_nickname}",
                                param_entry_id=field_value,
                                name=player_table[field_value].name,
                            )
                        )
                    if field_value in non_player_table:
                        links.append(
                            ParamsLink(
                                self,
                                param_name=f"NonPlayer{param_nickname}",
                                param_entry_id=field_value,
                                name=non_player_table[field_value].name,
                            )
                        )
                    if links:
                        return links
                    return [BaseLink()]

            elif field_type in {ArmorParam, WeaponParam}:
                param_nickname = field_type.get_param_nickname()
                true_param_id = (
                    self.check_armor_id(field_value) if field_type == ArmorParam else self.check_weapon_id(field_value)
                )
                if true_param_id is None:
                    return [BaseLink()]  # Invalid weapon/armor ID, even considering reinforcement.
                if field_value != true_param_id:
                    name_extension = "+" + str(field_value - true_param_id)
                field_value = true_param_id

            else:
                param_nickname = field_type.get_param_nickname()

            param_table = self.project.Params[param_nickname]
            try:
                name = param_table[field_value].name + name_extension
            except KeyError:
                return [BaseLink()]
            else:
                return [ParamsLink(self, param_name=param_nickname, param_entry_id=field_value, name=name)]

        if issubclass(field_type, BaseLightingParam):
            # Always uses slot 0. You can easily jump to other slots from there (entry names should be the same).
            # Looks up map from Maps tab, since nothing else links there right now.
            param_nickname = field_type.get_param_nickname()
            map_area_name = map_override[:3] if map_override else f"m{self.window.maps_tab.get_map().area_id}"
            param_table = self.project.Lighting[map_area_name][param_nickname][0]
            try:
                name = param_table[field_value].name + name_extension
            except KeyError:
                return [BaseLink()]
            else:
                return [LightingLink(
                    self,
                    param_name=param_nickname,
                    map_area_name=map_area_name,
                    param_entry_id=field_value,
                    slot=0,
                    name=name,
                )]

        return []  # No other data types (Flag, Texture, Map, Animation, etc.) supported yet.

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
                        names[i] += f"  {{{CHARACTER_MODELS.get(model_id, 'UNKNOWN')}}}"
                return names
            else:
                return entry_list.get_entry_names()

    def param_entry_text_link(self, entry_id):
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
            if text_ids[text_category] not in self.project.Text[prefix + text_category]:
                links.append(BaseLink())
            else:
                links.append(
                    TextLink(
                        self,
                        text_type_name=prefix + text_category,
                        text_id=text_id,
                        name=self.project.Text[prefix + text_category][text_id],
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
            origin = self.project.Params["Armor"][base_armor][origin_field]
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
            origin = self.project.Params["Weapons"][base_weapon][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_weapon

    def text_link(self, text_type_name, text_id):
        self.window.page_tabs.select(self.get_tab_index("text"))
        # TODO: Create entry if missing.
        self.window.text_tab.select_category(text_type_name)
        self.window.text_tab.select_entry_id(text_id, edit_if_already_selected=False)
        self.window.text_tab.update_idletasks()

    def maps_link(self, entry_list_name, entry_type_name, entry_local_index):
        self.window.maps_tab.select_displayed_field_row(None)
        self.window.page_tabs.select(self.get_tab_index("maps"))
        self.window.maps_tab.refresh_categories()  # TODO: why do I need to call this?
        category = f"{entry_list_name}: {entry_type_name}"
        self.window.maps_tab.select_category(category, auto_scroll=True)
        self.window.maps_tab.select_entry_id(entry_local_index, edit_if_already_selected=False)
        self.window.maps_tab.update_idletasks()

    def validate_model_subtype(self, model_subtype, name, map_id):
        """Check appropriate game model files to confirm the given model name is valid.

        Note that Character and Object models don't actually need `map_id` to validate them.
        """
        model_subtype = MSBModelList.resolve_entry_subtype(model_subtype)

        dcx = ".dcx" if self.project.game_name == "Dark Souls Remastered" else ""

        if model_subtype == MSBModelSubtype.Character:
            if (self.project.game_root / f"chr/{name}.chrbnd{dcx}").is_file():
                return True
        elif model_subtype == MSBModelSubtype.Object:
            if (self.project.game_root / f"obj/{name}.objbnd{dcx}").is_file():
                return True
        elif model_subtype == MSBModelSubtype.MapPiece:
            if (self.project.game_root / f"map/{map_id}/{name}A{map_id[1:3]}.flver{dcx}").is_file():
                return True
        elif model_subtype == MSBModelSubtype.Collision:
            # TODO: Rough BHD string scan until I have that file format.
            hkxbhd_path = self.project.game_root / f"map/{map_id}/h{map_id}.hkxbhd"
            if hkxbhd_path.is_file():
                with hkxbhd_path.open("r") as f:
                    if name + "A10.hkx" in f.read():
                        return True
        elif model_subtype == MSBModelSubtype.Navmesh:
            nvmbnd_path = self.project.game_root / f"map/{map_id}/{map_id}.nvmbnd{dcx}"
            if nvmbnd_path.is_file():
                navmesh_bnd = BND(nvmbnd_path)
                if name + "A10.nvm" in navmesh_bnd.entries_by_basename.keys():
                    return True

        return False

    def params_link(self, param_name, param_entry_id, field_name=None):
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

    def lighting_link(self, param_name, map_area_name, param_entry_id, lighting_slot=0, field_name=None):
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

    def runtime_hook(self):
        return self.window.runtime_tab.hook_into_game()

    @property
    def is_hooked(self):
        return self.window.runtime_tab.is_hooked

    def get_game_value(self, value_name):
        """Try to retrieve given game value (e.g. 'player_x') from runtime memory hook."""
        return self.window.runtime_tab.get_game_value(value_name)

    def edit_all_item_text(self, item_type, item_id):
        """Edit name, summary, and description of item (weapon, armor, ring, good, or spell) simultaneously.

        Name must be specified. If summary and/or description are left empty, they will NOT be modified or created.

        Note that for new Armor entries, the default summary text is a single blank space rather than empty text. For
        new Weapon entries, the default summary text is 'WeaponType', to remind you to specify it.
        """
        name = getattr(self.project.Text, item_type + "Names").get(item_id, "")
        summary = getattr(self.project.Text, item_type + "Summaries").get(item_id, "")
        if not summary:
            if item_type == "Weapon":
                summary = "WeaponType"  # reminder to specify weapon type as summary
            elif item_type == "Armor":
                summary = " "  # Armor summary defaults to a single blank space.
        description = getattr(self.project.Text, item_type + "Descriptions").get(item_id, "")
        name, summary, description = ItemTextEditBox(
            self.window, name, summary, description, f"Editing {item_type}[{item_id}]"
        ).go()
        if not name:
            raise ValueError("Item name cannot be empty.")
        getattr(self.project.Text, item_type + "Names")[item_id] = name
        if summary:
            getattr(self.project.Text, item_type + "Summaries")[item_id] = summary
        if description:
            getattr(self.project.Text, item_type + "Descriptions")[item_id] = description


class BaseLink:
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
        super().__init__(linker, name="None/Default", menu_text="")

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
        self.linker.maps_link(self.entry_list_name, self.entry_type_name, self.entry_local_index)


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
        self.linker.params_link(self.param_name, self.param_entry_id)


class TextLink(BaseLink):
    def __init__(self, linker, text_type_name, text_id, name=None):
        super().__init__(linker, name=name, menu_text=f"Go to Text.{text_type_name}[{text_id}]")
        self.text_type_name = text_type_name
        self.text_id = text_id

    def __call__(self):
        self.linker.text_link(self.text_type_name, self.text_id)


class LightingLink(BaseLink):
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
        self.linker.lighting_link(self.param_name, self.map_area_name, self.param_entry_id, self.lighting_slot)
