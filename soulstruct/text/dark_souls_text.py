import logging
from copy import deepcopy
from pathlib import Path

from soulstruct.bnd import BND, BaseBND
from soulstruct.text.fmg import FMG
from soulstruct.utilities.core import BiDict

__all__ = ["DarkSoulsText"]
_LOGGER = logging.getLogger(__name__)


class DarkSoulsText:

    ArmorDescriptions: dict
    ArmorNames: dict
    ArmorSummaries: dict
    ContextualHelp: dict
    Subtitles: dict
    DebugTags_Win32: dict
    EventText: dict
    FeatureDescriptions: dict
    FeatureNames: dict
    FeatureSummaries: dict
    IngameMenus: dict
    GoodDescriptions: dict
    GoodNames: dict
    GoodSummaries: dict
    KeyGuide: dict
    SpellDescriptions: dict
    SpellNames: dict
    SpellSummaries: dict
    MenuDialogs: dict
    MenuHelpSnippets: dict
    MenuText_Common: dict
    MenuText_Other: dict
    NPCNames: dict
    OpeningSubtitles: dict
    PlaceNames: dict
    RingDescriptions: dict
    RingNames: dict
    RingSummaries: dict
    SoapstoneMessages: dict
    SystemMessages_Win32: dict
    TextTagPlaceholders: dict
    WeaponDescriptions: dict
    WeaponNames: dict
    WeaponSummaries: dict

    # These are text categories you are likely to want to change in mod projects.
    main_categories = [
        "NPCNames",
        "PlaceNames",
        "EventText",
        "SoapstoneMessages",
        "WeaponNames",
        "WeaponSummaries",
        "WeaponDescriptions",
        "ArmorNames",
        "ArmorSummaries",
        "ArmorDescriptions",
        "RingNames",
        "RingSummaries",
        "RingDescriptions",
        "GoodNames",
        "GoodSummaries",
        "GoodDescriptions",
        "SpellNames",
        "SpellSummaries",
        "SpellDescriptions",
        "Subtitles",
    ]

    # These are text categories you are unlikely to change, whether it's for pragmatic
    # reasons or because they contain low-level menu/system text.
    internal_categories = [
        "ContextualHelp",
        "DebugTags_Win32",
        "FeatureNames",
        "FeatureSummaries",
        "FeatureDescriptions",
        "IngameMenus",
        "KeyGuide",
        "MenuDialogs",
        "MenuHelpSnippets",
        "MenuText_Common",
        "MenuText_Other",
        "OpeningSubtitles",
        "SystemMessages_Win32",
        "TextTagPlaceholders",
    ]

    all_categories = all_fmg_names = main_categories + internal_categories

    def __init__(self, msg_directory=None):
        """Unpack all Dark Souls 1 text data (from both 'item' and 'menu' MSGBND files) into one unified structure.

        You can access and modify the `entries` attributes of each loaded `FMG` instance using the names of the FMGs,
        which I have translated into a standard list (see above attribute hints). The source (item/menu) of the FMG and
        its type (standard/Patch) are handled internally, though the latter does not matter in either version of DS1
        (and neither do the names of the FMG files in the MSGBND archives).

        Args:
            msg_directory: Directory containing 'item.msgbnd[.dcx]' and 'menu.msgbnd[.dcx]', in any of the language
                folders within the 'msg' directory in the Dark Souls data files.
        """
        self._bnd_dir = ""
        self._directory = None
        self._original_names = {}  # The actual within-BND FMG names are completely up to us. My names are nicer.
        self._is_menu = {}  # Records whether each FMG belongs in 'item' or 'menu' MSGBND.
        self._data = {}
        self._dcx = False

        # Patch and non-Patch resources get put into the same attribute here so they can be edited together.
        # This set contains tuple pairs (fmg_name, entry_index) that came from Patch resources.
        self._is_patch = set()

        if msg_directory is None:
            self.item_msgbnd = None
            self.menu_msgbnd = None
            return

        self._directory = Path(msg_directory)

        try:
            self.item_msgbnd = BND(self._directory / "item.msgbnd.dcx", optional_dcx=False)
        except FileNotFoundError:
            self.item_msgbnd = BND(self._directory / "item.msgbnd", optional_dcx=False)
            self._dcx = False
        else:
            self._dcx = True
            if (self._directory / "item.msgbnd").is_file():
                _LOGGER.warning(
                    "Both DCX and non-DCX 'item.msgbnd' resources were found. Reading only the DCX file, "
                    "and will compress with DCX by default when `.write()` is called."
                )

        try:
            self.menu_msgbnd = BND(self._directory / "menu.msgbnd.dcx", optional_dcx=False)
        except FileNotFoundError:
            self.menu_msgbnd = BND(self._directory / "menu.msgbnd", optional_dcx=False)
            if self._dcx:
                raise ValueError("Found DCX-compressed 'item.msgbnd.dcx', but not 'menu.msgbnd.dcx'.")
        else:
            if not self._dcx:
                raise ValueError("Found DCX-compressed 'menu.msgbnd.dcx', but not 'item.msgbnd.dcx'.")
            if (self._directory / "menu.msgbnd").is_file():
                _LOGGER.warning(
                    "Both DCX and non-DCX 'menu.msgbnd' resources were found. Reading only the DCX file, "
                    "and will compress with DCX by default when `.write()` is called."
                )

        self.load_fmg_entries_from_bnd(self.item_msgbnd, is_menu=False)
        self.load_fmg_entries_from_bnd(self.menu_msgbnd, is_menu=True)

        for key, fmg_dict in self._data.items():
            setattr(self, key, fmg_dict)

    def load_fmg_entries_from_bnd(self, msgbnd: BaseBND, is_menu: bool):

        # remastered = False if 'win32' in msgbnd[0].path else True

        for entry in msgbnd:
            try:
                new_name = _MSGBND_INDEX_to_SS_NAME_[entry.id]
            except KeyError:
                raise ValueError(f"BND entry '{entry.path}' has unexpected index {entry.id} in its msgbnd.")

            original_name = entry.name

            self._original_names[new_name] = original_name
            self._is_menu[new_name] = is_menu
            fmg = FMG(entry.data)

            if new_name.endswith("Patch"):
                # Patch FMGs are merged with the originals here. Their origin is tracked in `_is_patch` in order to
                # separate them again when writing the BNDs (though this is technically optional).
                new_name = new_name[:-5]
                for index in fmg.entries:
                    self._is_patch.add((new_name, index))

            self._data.setdefault(new_name, {}).update(fmg.entries)

    def get_all_item_text(self, index, item_type="good"):
        """ Get name, summary, and description of goods, weapons, armor, or rings. """
        item_fmg = self.resolve_item_type(item_type)
        if index not in self._data[item_fmg + "Names"]:
            return None
        return {
            "name": self._data[item_fmg + "Names"][index],
            "summary": self._data[item_fmg + "Summaries"][index],
            "description": self._data[item_fmg + "Descriptions"][index],
        }

    def add_item_text(self, index, item_type, name, summary, description):
        item_fmg = self.resolve_item_type(item_type)
        if index in self._data[item_fmg + "Names"]:
            raise ValueError(
                f"Item with index {index} already exists in {item_fmg}Names: "
                f"{self._data[item_fmg + 'Names'][index]}"
            )
        self._data[item_fmg + "Names"][index] = name
        self._data[item_fmg + "Summaries"][index] = summary
        self._data[item_fmg + "Descriptions"][index] = description

    def delete_item_text(self, index, item_fmg="good"):
        """ Remove entries for item name, summary, and description. """
        item_fmg = self.resolve_item_type(item_fmg)
        if index not in self._data[item_fmg + "Names"]:
            raise ValueError(f"There is no {item_fmg} with index {index} to delete.")
        self._data[item_fmg + "Names"][index] = ""
        self._data[item_fmg + "Summaries"][index] = ""
        self._data[item_fmg + "Descriptions"][index] = ""

    def update_msgbnd_entry(
        self, msgbnd, fmg_name, fmg_entries: dict, word_wrap_limit=None, pipe_to_newline=False, use_original_names=True
    ):
        fmg_patch_data = FMG(fmg_entries, version="ds1").pack(
            word_wrap_limit=word_wrap_limit, pipe_to_newline=pipe_to_newline
        )
        try:
            bnd_entry_id = _MSGBND_INDEX_to_SS_NAME_[fmg_name]
        except IndexError:
            raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
        bnd_entry = msgbnd.entries_by_id[bnd_entry_id]
        bnd_entry.data = fmg_patch_data
        if not use_original_names:
            bnd_entry.path = bnd_entry.path.replace(self._original_names[fmg_name], fmg_name + ".fmg")

    def save(
        self,
        msg_directory=None,
        description_word_wrap_limit=None,
        separate_patch=False,
        use_original_names=True,
        pipe_to_newline=True,
        dcx=None,
    ):
        """Export FMGs and repack BND, then write it as packed. Should really just be 'write' and 'pack' methods."""
        new_item_msgbnd = deepcopy(self.item_msgbnd)  # type: BaseBND
        new_menu_msgbnd = deepcopy(self.menu_msgbnd)  # type: BaseBND

        msg_directory = self._directory if msg_directory is None else Path(msg_directory)
        if dcx is None:
            dcx = self._dcx

        if not separate_patch:
            # Select Patch indices will be merged into non-Patch FMG, so remove those Patch entries from the BND now.
            for patch_fmg_name in _CAN_MERGE_PATCH:
                if patch_fmg_name in self._is_menu:
                    bnd_index = _MSGBND_INDEX_to_SS_NAME_[patch_fmg_name]
                    msgbnd = new_menu_msgbnd if self._is_menu[patch_fmg_name] else new_item_msgbnd
                    if bnd_index in msgbnd.entries_by_id:
                        msgbnd.remove_entry(bnd_index)

        for fmg_name, fmg_entries in self._data.items():
            word_wrap = description_word_wrap_limit if "Descriptions" in fmg_name else None
            fmg_entries_main = fmg_entries.copy()
            fmg_entries_patch = {}

            if separate_patch:
                # Separate Patch indices out into Patch dictionary.
                for index in fmg_entries.keys():
                    if (fmg_name, index) in self._is_patch:
                        patch_text = fmg_entries_main.pop(index)
                        if patch_text:
                            fmg_entries_patch[index] = patch_text  # Don't bother adding if empty.
                if fmg_entries_patch:
                    patch_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name + "Patch"] else new_item_msgbnd
                    self.update_msgbnd_entry(
                        patch_msgbnd,
                        fmg_name + "Patch",
                        fmg_entries_patch,
                        word_wrap_limit=word_wrap,
                        pipe_to_newline=pipe_to_newline,
                        use_original_names=use_original_names,
                    )

            main_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            self.update_msgbnd_entry(
                main_msgbnd,
                fmg_name,
                fmg_entries,
                word_wrap_limit=word_wrap,
                pipe_to_newline=pipe_to_newline,
                use_original_names=use_original_names,
            )

        # Write BNDs (to original directory by default).
        new_item_msgbnd.write(msg_directory / ("item.msgbnd" + (".dcx" if dcx else "")))
        new_menu_msgbnd.write(msg_directory / ("menu.msgbnd" + (".dcx" if dcx else "")))

        # Update BNDs after successful write.
        self.item_msgbnd = new_item_msgbnd
        self.menu_msgbnd = new_menu_msgbnd

        _LOGGER.info("Dark Souls text files (MsgBND) written successfully.")

    def change_item_text(self, text_dict, index=None, item_type=None, patch=False):
        if index is None:
            index = text_dict["index"]
        if not isinstance(index, (list, tuple)):
            index = (index,)
        if item_type is None:
            item_type = text_dict["item_type"]
        item_fmg = self.resolve_item_type(item_type)
        patch = "Patch" if patch else ""
        for i in index:
            if i not in self[item_fmg + "Names"]:
                _LOGGER.info(
                    f"NEW ENTRY: {item_fmg} with index {i} has been added ({text_dict.get('name', 'unknown name')})"
                )
            if "name" in text_dict:
                self[item_fmg + "Names" + patch][i] = text_dict["name"]
            if "summary" in text_dict:
                self[item_fmg + "Summaries" + patch][i] = text_dict["summary"]
            if "description" in text_dict:
                self[item_fmg + "Descriptions" + patch][i] = text_dict["description"]

    def find(self, search_string, replace_with=None, text_category=None, exclude_conversations=True):
        """Search for the given text in the entire game.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            replace_with: String to replace the given text with in any results. (Default: None)
            text_category: Name of text category (FMG) to search. If no category is given, all categories will be
                searched (except perhaps Conversations; see below). (Default: None)
            exclude_conversations: If True, the Conversations text category will not be searched when all categories are
                searched. (This category contains a lot of text, and you are unlikely to want to modify it, given how it
                lines up with the audio.) (Default: True)
        """
        if text_category is None:
            dicts_to_search = (
                [(fmg_name, fmg_dict) for fmg_name, fmg_dict in self._data.items() if fmg_name != "Conversations"]
                if exclude_conversations
                else self._data.items()
            )
        else:
            dicts_to_search = ((text_category, self[text_category]),)

        found_something = False
        for fmg_name, fmg_dict in dicts_to_search:
            for index, text in fmg_dict.items():
                if search_string in text:
                    found_something = True
                    print(f"\n~~~ {fmg_name}[{index}]:\n{text}")
                    if replace_with is not None:
                        fmg_dict[index] = text.replace(search_string, replace_with)
                        print(f"-> {fmg_dict[index]}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def __iter__(self):
        return iter(self._data.items())

    def __getitem__(self, text_category):
        try:
            return self._data[text_category]
        except KeyError:
            raise AttributeError(f"Non-existent text category (FMG): '{text_category}'")

    def get_range(self, category, start, end):
        """Get a list of (id, text) pairs from a certain range inside the ID-sorted text dictionary."""
        return [(text_id, self._data[category][text_id]) for text_id in sorted(self._data[category])[start:end]]

    @staticmethod
    def resolve_item_type(item_type):
        if item_type.lower() in ("good", "consumable"):
            return "Good"
        elif item_type.lower() in ("ring", "accessory"):
            return "Ring"
        elif item_type.lower() in ("weapon", "shield"):
            return "Weapon"
        elif item_type.lower() in ("armour", "armor", "protector"):
            return "Armor"
        elif item_type.lower() == "equipment":
            raise ValueError("'Equipment' is ambiguous. Did you mean 'weapon', 'armor', 'ring', or 'good'?")
        elif item_type.lower() == "item":
            raise ValueError(
                "'Item' is ambiguous; it's the term used to describe everything in your inventory.\n"
                "Did you mean 'weapon', 'armor', 'ring', or 'good'?"
            )
        else:
            raise ValueError(f"Unrecognized item type: '{item_type}'")


_CAN_MERGE_PATCH = {
    "WeaponNamesPatch",
    "WeaponSummariesPatch",
    "WeaponDescriptionsPatch",
    "ArmorNamesPatch",
    "ArmorSummariesPatch",
    "ArmorDescriptionsPatch",
    "RingNamesPatch",
    "RingSummariesPatch",
    "RingDescriptionsPatch",
    "GoodNamesPatch",
    "GoodSummariesPatch",
    "GoodDescriptionsPatch",
    "SpellNamesPatch",
    "SpellDescriptionsPatch",
    "NPCNamesPatch",
    "PlaceNamesPatch",
}
_DO_NOT_MERGE_PATCH = {
    "EventText",
    "MenuDialogs",
    "SystemMessages_Win32",
    "Conversations",
    "SoapstoneMessages",
    "MenuHelpSnippets",
    "KeyGuide",
    "MenuText_Other",
    "MenuText_Common",
}


_MSGBND_INDEX_to_SS_NAME_ = BiDict(
    (1, "Conversations"),
    (2, "SoapstoneMessages"),
    (3, "OpeningSubtitles"),
    (10, "GoodNames"),
    (11, "WeaponNames"),
    (12, "ArmorNames"),
    (13, "RingNames"),
    (14, "SpellNames"),
    (15, "FeatureNames"),
    (16, "FeatureSummaries"),
    (17, "FeatureDescriptions"),
    (18, "NPCNames"),
    (19, "PlaceNames"),
    (20, "GoodSummaries"),
    (21, "WeaponSummaries"),
    (22, "ArmorSummaries"),
    (23, "RingSummaries"),
    (24, "GoodDescriptions"),
    (25, "WeaponDescriptions"),
    (26, "ArmorDescriptions"),
    (27, "RingDescriptions"),
    (28, "SpellSummaries"),
    (29, "SpellDescriptions"),
    (30, "EventText"),
    (70, "IngameMenus"),
    (76, "MenuText_Common"),
    (77, "MenuText_Other"),
    (78, "MenuDialogs"),
    (79, "KeyGuide"),
    (80, "MenuHelpSnippets"),
    (81, "ContextualHelp"),
    (90, "TextTagPlaceholders"),
    (91, "DebugTags_Win32"),
    (92, "SystemMessages_Win32"),
    # Patch resources (all in menu.msgbnd in PTDE, but some in item.msgbnd in DSR).
    (100, "GoodDescriptionsPatch"),
    (101, "EventTextPatch"),
    (102, "MenuDialogsPatch"),
    (103, "SystemMessages_Win32Patch"),
    (104, "ConversationsPatch"),
    (105, "SpellDescriptionsPatch"),
    (106, "WeaponDescriptionsPatch"),
    (107, "SoapstoneMessagesPatch"),
    (108, "ArmorDescriptionsPatch"),
    (109, "RingDescriptionsPatch"),
    (110, "GoodSummariesPatch"),
    (111, "GoodNamesPatch"),
    (112, "RingSummariesPatch"),
    (113, "RingNamesPatch"),
    (114, "WeaponSummariesPatch"),
    (115, "WeaponNamesPatch"),
    (116, "ArmorSummariesPatch"),
    (117, "ArmorNamesPatch"),
    (118, "SpellNamesPatch"),
    (119, "NPCNamesPatch"),
    (120, "PlaceNamesPatch"),
    (121, "MenuHelpSnippetsPatch"),
    (122, "KeyGuidePatch"),
    (123, "MenuText_OtherPatch"),
    (124, "MenuText_CommonPatch"),
)


# TODO: Unused; using BND index instead.
_DSR_TO_SS = {
    # item.msgbnd
    "Accessory_long_desc_.fmg": "RingDescriptions",
    "Accessory_name_.fmg": "RingNames",
    "Accessory_description_.fmg": "RingSummaries",
    "Armor_long_desc_.fmg": "ArmorDescriptions",
    "Armor_name_.fmg": "ArmorNames",
    "Armor_description_.fmg": "ArmorSummaries",
    "Feature_long_desc_.fmg": "FeatureDescriptions",
    "Feature_name_.fmg": "FeatureNames",
    "Feature_description_.fmg": "FeatureSummaries",
    "Item_long_desc_.fmg": "GoodDescriptions",
    "Item_name_.fmg": "GoodNames",
    "Item_description_.fmg": "GoodSummaries",
    "Magic_long_desc_.fmg": "SpellDescriptions",
    "Magic_name_.fmg": "SpellNames",
    "Magic_description_.fmg": "SpellSummaries",
    "NPC_name_.fmg": "NPCNames",
    "Place_name_.fmg": "PlaceNames",
    "Weapon_long_desc_.fmg": "WeaponDescriptions",
    "Weapon_name_.fmg": "WeaponNames",
    "Weapon_description_.fmg": "WeaponSummaries",
    # menu.msgbnd
    "Blood_writing_.fmg": "SoapstoneMessages",
    "Conversation_.fmg": "Conversations",
    "Dialogue_.fmg": "MenuDialogs",
    "Event_text_.fmg": "EventText",
    "Ingame_menu.fmg": "IngameMenus",
    "Item_help_.fmg": "ContextualHelp",
    "Key_guide_.fmg": "KeyGuide",
    "Menu_general_text_.fmg": "MenuText_Common",
    "Menu_others_.fmg": "MenuText_Other",
    "Movie_subtitles_.fmg": "OpeningSubtitles",
    "Single_line_help_.fmg": "MenuHelpSnippets",
    "System_message_win32_.fmg": "SystemMessages_Win32",
    "System_specific_tags_win32_.fmg": "DebugTags_Win32",
    "Text_display_tag_list_.fmg": "TextTagPlaceholders",
}


# TODO: Unused; using BND index instead.
_PTD_TO_SS = {
    # item.msgbnd (including patch)
    "防具うんちく.fmg": "ArmorDescriptions",
    "防具うんちくパッチ.fmg": "ArmorDescriptionsPatch",
    "防具名.fmg": "ArmorNames",
    "防具名パッチ.fmg": "ArmorNamesPatch",
    "防具説明.fmg": "ArmorSummaries",
    "防具説明パッチ.fmg": "ArmorSummariesPatch",
    "特徴うんちく.fmg": "FeatureDescriptions",
    "特徴名.fmg": "FeatureNames",
    "特徴説明.fmg": "FeatureSummaries",
    "アイテムうんちく.fmg": "GoodDescriptions",
    "アイテムうんちくパッチ.fmg": "GoodDescriptionsPatch",
    "アイテム名.fmg": "GoodNames",
    "アイテム名パッチ.fmg": "GoodNamesPatch",
    "アイテム説明.fmg": "GoodSummaries",
    "アイテム説明パッチ.fmg": "GoodSummariesPatch",
    "NPC名.fmg": "NPCNames",
    "NPC名パッチ.fmg": "NPCNamesPatch",
    "地名.fmg": "PlaceNames",
    "地名パッチ.fmg": "PlaceNamesPatch",
    "アクセサリうんちく.fmg": "RingDescriptions",
    "アクセサリうんちくパッチ.fmg": "RingDescriptionsPatch",
    "アクセサリ名.fmg": "RingNames",
    "アクセサリ名パッチ.fmg": "RingNamesPatch",
    "アクセサリ説明.fmg": "RingSummaries",
    "アクセサリ説明パッチ.fmg": "RingSummariesPatch",
    "魔法うんちく.fmg": "SpellDescriptions",
    "魔法うんちくパッチ.fmg": "SpellDescriptionsPatch",
    "魔法名.fmg": "SpellNames",
    "魔法名パッチ.fmg": "SpellNamesPatch",
    "魔法説明.fmg": "SpellSummaries",
    "武器うんちく.fmg": "WeaponDescriptions",
    "武器うんちくパッチ.fmg": "WeaponDescriptionsPatch",
    "武器名.fmg": "WeaponNames",
    "武器名パッチ.fmg": "WeaponNamesPatch",
    "武器説明.fmg": "WeaponSummaries",
    "武器説明パッチ.fmg": "WeaponSummariesPatch",
    # menu.msgbnd
    "項目ヘルプ.fmg": "ContextualHelp",
    "会話.fmg": "Conversations",
    "会話パッチ.fmg": "ConversationsPatch",
    "機種別タグ_win32.fmg": "DebugTags_Win32",
    "イベントテキスト.fmg": "EventText",
    "イベントテキストパッチ.fmg": "EventTextPatch",
    "インゲームメニュー.fmg": "IngameMenus",
    "キーガイド.fmg": "KeyGuide",
    "キーガイドパッチ.fmg": "KeyGuidePatch",
    "ダイアログ.fmg": "MenuDialogs",
    "ダイアログパッチ.fmg": "MenuDialogsPatch",
    "一行ヘルプ.fmg": "MenuHelpSnippets",
    "一行ヘルプパッチ.fmg": "MenuHelpSnippetsPatch",
    "メニュー共通テキスト.fmg": "MenuText_Common",
    "メニュー共通テキストパッチ.fmg": "MenuText_CommonPatch",
    "メニューその他.fmg": "MenuText_Other",
    "メニューその他パッチ.fmg": "MenuText_OtherPatch",
    "ムービー字幕.fmg": "OpeningSubtitles",
    "血文字.fmg": "SoapstoneMessages",
    "血文字パッチ.fmg": "SoapstoneMessagesPatch",
    "システムメッセージ_win32.fmg": "SystemMessages_Win32",
    "システムメッセージ_win32パッチ.fmg": "SystemMessages_Win32Patch",
    "テキスト表示用タグ一覧.fmg": "TextTagPlaceholders",
}
