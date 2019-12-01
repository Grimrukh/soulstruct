from copy import deepcopy
from pathlib import Path
from soulstruct.bnd import BND, BaseBND
from soulstruct.text.fmg import FMG


class DarkSoulsText(object):

    ArmorDescriptions: dict
    ArmorNames: dict
    ArmorSummaries: dict
    ContextualHelp: dict
    Conversations: dict
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
    main_categories = main_fmg_names = [
        'NPCNames', 'PlaceNames', 'EventText', 'SoapstoneMessages',
        'WeaponNames', 'WeaponSummaries', 'WeaponDescriptions',
        'ArmorNames', 'ArmorSummaries', 'ArmorDescriptions',
        'RingNames', 'RingSummaries', 'RingDescriptions',
        'GoodNames', 'GoodSummaries', 'GoodDescriptions',
        'SpellNames', 'SpellSummaries', 'SpellDescriptions',
        'Conversations',
    ]

    # These are text categories you are unlikely to change, whether it's for pragmatic
    # reasons (like Conversations) or because they contain low-level menu/system text.
    internal_categories = internal_fmg_names = [
        'ContextualHelp', 'DebugTags_Win32',
        'FeatureNames', 'FeatureSummaries', 'FeatureDescriptions',
        'IngameMenus', 'KeyGuide', 'MenuDialogs', 'MenuHelpSnippets',
        'MenuText_Common', 'MenuText_Other', 'OpeningSubtitles',
        'SystemMessages_Win32', 'TextTagPlaceholders',
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
        self._bnd_dir = ''
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
            self.item_msgbnd = BND(self._directory / 'item.msgbnd.dcx', optional_dcx=False)
        except FileNotFoundError:
            self.item_msgbnd = BND(self._directory / 'item.msgbnd', optional_dcx=False)
            self._dcx = False
        else:
            self._dcx = True
            if (self._directory / 'item.msgbnd').is_file():
                print("# WARNING: Both DCX and non-DCX 'item.msgbnd' resources were found. Reading only the DCX file, "
                      "and will compress with DCX by default when `.write()` is called.")

        try:
            self.menu_msgbnd = BND(self._directory / 'menu.msgbnd.dcx', optional_dcx=False)
        except FileNotFoundError:
            self.menu_msgbnd = BND(self._directory / 'menu.msgbnd', optional_dcx=False)
            if self._dcx:
                raise ValueError("Found DCX-compressed 'item.msgbnd.dcx', but not 'menu.msgbnd.dcx'.")
        else:
            if not self._dcx:
                raise ValueError("Found DCX-compressed 'menu.msgbnd.dcx', but not 'item.msgbnd.dcx'.")
            if (self._directory / 'menu.msgbnd').is_file():
                print("# WARNING: Both DCX and non-DCX 'menu.msgbnd' resources were found. Reading only the DCX file, "
                      "and will compress with DCX by default when `.write()` is called.")

        self.load_fmg_entries_from_bnd(self.item_msgbnd, is_menu=False)
        self.load_fmg_entries_from_bnd(self.menu_msgbnd, is_menu=True)

        for key, fmg_dict in self._data.items():
            setattr(self, key, fmg_dict)

    def load_fmg_entries_from_bnd(self, msgbnd: BaseBND, is_menu: bool):

        # remastered = False if 'win32' in msgbnd[0].path else True

        for entry in msgbnd:
            try:
                new_name = _MSGBND_INDEX_TO_SS[entry.id]
            except KeyError:
                raise ValueError(f"BND entry '{entry.path}' has unexpected index {entry.id} in its msgbnd.")

            original_name = entry.name

            self._original_names[new_name] = original_name
            self._is_menu[new_name] = is_menu
            fmg = FMG(entry.data)

            if new_name.endswith('Patch'):
                # Patch FMGs are merged with the originals here. Their origin is tracked in `_is_patch` in order to
                # separate them again when writing the BNDs (though this is technically optional).
                new_name = new_name[:-5]
                for index in fmg.entries:
                    self._is_patch.add((new_name, index))

            self._data.setdefault(new_name, {}).update(fmg.entries)

    def get_all_item_text(self, index, item_type='good'):
        """ Get name, summary, and description of goods, weapons, armor, or rings. """
        item_fmg = self.resolve_item_type(item_type)
        if index not in self._data[item_fmg + 'Names']:
            return None
        return {'name': self._data[item_fmg + 'Names'][index],
                'summary': self._data[item_fmg + 'Summaries'][index],
                'description': self._data[item_fmg + 'Descriptions'][index]}

    def add_item_text(self, index, item_type, name, summary, description):
        item_fmg = self.resolve_item_type(item_type)
        if index in self._data[item_fmg + 'Names']:
            raise ValueError(f"Item with index {index} already exists in {item_fmg}Names: "
                             f"{self._data[item_fmg + 'Names'][index]}")
        self._data[item_fmg + 'Names'][index] = name
        self._data[item_fmg + 'Summaries'][index] = summary
        self._data[item_fmg + 'Descriptions'][index] = description

    def delete_item_text(self, index, item_fmg='good'):
        """ Remove entries for item name, summary, and description. """
        item_fmg = self.resolve_item_type(item_fmg)
        if index not in self._data[item_fmg + 'Names']:
            raise ValueError(f"There is no {item_fmg} with index {index} to delete.")
        self._data[item_fmg + 'Names'][index] = ''
        self._data[item_fmg + 'Summaries'][index] = ''
        self._data[item_fmg + 'Descriptions'][index] = ''

    def save(self, msg_directory=None, description_word_wrap_limit=50, separate_patch=False, use_original_names=False,
             pipe_to_newline=True, dcx=None):
        """ Export FMGs and repack BND, then write it as packed. Should really just be 'write' and 'pack' methods. """

        new_item_msgbnd = deepcopy(self.item_msgbnd)  # type: BaseBND
        new_menu_msgbnd = deepcopy(self.menu_msgbnd)  # type: BaseBND

        msg_directory = self._directory if msg_directory is None else Path(msg_directory)
        if dcx is None:
            dcx = self._dcx

        if not separate_patch:
            # Patch indices will all be merged into main resources, so remove any Patch entries from the BND.
            for fmg_name, fmg_entries in self._data.items():
                try:
                    bnd_index = [key for key in _MSGBND_INDEX_TO_SS.keys()
                                 if _MSGBND_INDEX_TO_SS[key] == fmg_name + 'Patch'][0]
                except IndexError:
                    # No Patch version of this FMG.
                    print('-- No patch version of', fmg_name)
                    pass
                else:
                    if bnd_index >= 100 and self._is_menu.get(fmg_name + 'Patch', False):
                        new_menu_msgbnd.remove_entry(bnd_index)
                        print('Removed patch FMG:', fmg_name + 'Patch', bnd_index)

        for fmg_name, fmg_entries in self._data.items():
            word_wrap = description_word_wrap_limit if 'Descriptions' in fmg_name else None
            fmg_entries_main = fmg_entries.copy()
            fmg_entries_patch = {}

            if separate_patch:
                # Separate Patch indices out into Patch dictionary.
                for index in fmg_entries.keys():
                    if (fmg_name, index) in self._is_patch:
                        patch_text = fmg_entries_main.pop(index)
                        if patch_text:
                            # Don't bother adding if empty.
                            fmg_entries_patch[index] = patch_text
                if fmg_entries_patch:
                    fmg = FMG(fmg_entries_patch, version='ds1')
                    fmg.unknown = 0
                    fmg_patch_data = FMG(fmg_entries_patch, version='ds1').pack(
                        word_wrap_limit=word_wrap, pipe_to_newline=pipe_to_newline)
                    original_name = self._original_names[fmg_name + 'Patch']
                    patch_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name + 'Patch'] else new_item_msgbnd
                    try:
                        bnd_entry_id = [k for k, v in _MSGBND_INDEX_TO_SS.items() if v == fmg_name + 'Patch'][0]
                    except IndexError:
                        raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
                    bnd_entry = patch_msgbnd.entries_by_id[bnd_entry_id]
                    bnd_entry.data = fmg_patch_data
                    if not use_original_names:
                        # Note that original path is kept.
                        bnd_entry.path = bnd_entry.path.replace(original_name, fmg_name + 'Patch.text')

            fmg_main_data = FMG(fmg_entries_main, version='ds1').pack(
                word_wrap_limit=word_wrap, pipe_to_newline=pipe_to_newline)
            original_name = self._original_names[fmg_name]
            msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            try:
                bnd_entry_id = [k for k, v in _MSGBND_INDEX_TO_SS.items() if v == fmg_name][0]
            except IndexError:
                raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
            bnd_entry = msgbnd.entries_by_id[bnd_entry_id]
            bnd_entry.data = fmg_main_data
            if not use_original_names:
                # Note that original path is kept.
                bnd_entry.path = bnd_entry.path.replace(original_name, fmg_name + '.text')

        # Write BNDs (to original directory by default).
        new_item_msgbnd.write(msg_directory / ('item.msgbnd' + ('.dcx' if dcx else '')))
        new_menu_msgbnd.write(msg_directory / ('menu.msgbnd' + ('.dcx' if dcx else '')))

        # Update BNDs after successful write.
        self.item_msgbnd = new_item_msgbnd
        self.menu_msgbnd = new_menu_msgbnd

        print("# Dark Souls text ('item.msgbnd[.dcx]' and 'menu.msgbnd[.dcx]') saved successfully.")

    def change_item_text(self, text_dict, index=None, item_type=None, patch=False):
        if index is None:
            index = text_dict['index']
        if not isinstance(index, (list, tuple)):
            index = (index,)
        if item_type is None:
            item_type = text_dict['item_type']
        item_fmg = self.resolve_item_type(item_type)
        patch = 'Patch' if patch else ''
        for i in index:
            if i not in self[item_fmg + 'Names']:
                print(f"NEW ENTRY: {item_fmg} with index {i} has been added "
                      f"({text_dict.get('name', 'unknown name')})")
            if 'name' in text_dict:
                self[item_fmg + 'Names' + patch][i] = text_dict['name']
            if 'summary' in text_dict:
                self[item_fmg + 'Summaries' + patch][i] = text_dict['summary']
            if 'description' in text_dict:
                self[item_fmg + 'Descriptions' + patch][i] = text_dict['description']

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
            dicts_to_search = [(fmg_name, fmg_dict) for fmg_name, fmg_dict in self._data.items()
                               if fmg_name != 'Conversations'] if exclude_conversations else self._data.items()
        else:
            dicts_to_search = (text_category, self[text_category]),

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
        if item_type.lower() in ('good', 'consumable'):
            return 'Good'
        elif item_type.lower() in ('ring', 'accessory'):
            return 'Ring'
        elif item_type.lower() in ('weapon', 'shield'):
            return 'Weapon'
        elif item_type.lower() in ('armour', 'armor', 'protector'):
            return 'Armor'
        elif item_type.lower() == 'equipment':
            raise ValueError("'Equipment' is ambiguous. Did you mean 'weapon', 'armor', or 'ring'?")
        elif item_type.lower() == 'item':
            raise ValueError("'Item' is ambiguous; it's the term used to describe everything in your inventory.\n"
                             "Did you mean 'weapon', 'armor', 'ring', or 'good'?")
        else:
            raise ValueError(f"Unrecognized item type: '{item_type}'")


_MSGBND_INDEX_TO_SS = {
    1: 'Conversations',
    2: 'SoapstoneMessages',
    3: 'OpeningSubtitles',
    10: 'GoodNames',
    11: 'WeaponNames',
    12: 'ArmorNames',
    13: 'RingNames',
    14: 'SpellNames',
    15: 'FeatureNames',
    16: 'FeatureSummaries',
    17: 'FeatureDescriptions',
    18: 'NPCNames',
    19: 'PlaceNames',
    20: 'GoodSummaries',
    21: 'WeaponSummaries',
    22: 'ArmorSummaries',
    23: 'RingSummaries',
    24: 'GoodDescriptions',
    25: 'WeaponDescriptions',
    26: 'ArmorDescriptions',
    27: 'RingDescriptions',
    28: 'SpellSummaries',
    29: 'SpellDescriptions',
    30: 'EventText',
    70: 'IngameMenus',
    76: 'MenuText_Common',
    77: 'MenuText_Other',
    78: 'MenuDialogs',
    79: 'KeyGuide',
    80: 'MenuHelpSnippets',
    81: 'ContextualHelp',
    90: 'TextTagPlaceholders',
    91: 'DebugTags_Win32',
    92: 'SystemMessages_Win32',
    # Patch resources (all in menu.msgbnd in PTD; put with their main resources in DSR).
    100: 'GoodDescriptionsPatch',
    101: 'EventTextPatch',
    102: 'MenuDialogsPatch',
    103: 'SystemMessages_Win32Patch',
    104: 'ConversationsPatch',
    105: 'SpellDescriptionsPatch',
    106: 'WeaponDescriptionsPatch',
    107: 'SoapstoneMessagesPatch',
    108: 'ArmorDescriptionsPatch',
    109: 'RingDescriptionsPatch',
    110: 'GoodSummariesPatch',
    111: 'GoodNamesPatch',
    112: 'RingSummariesPatch',
    113: 'RingNamesPatch',
    114: 'WeaponSummariesPatch',
    115: 'WeaponNamesPatch',
    116: 'ArmorSummariesPatch',
    117: 'ArmorNamesPatch',
    118: 'SpellNamesPatch',
    119: 'NPCNamesPatch',
    120: 'PlaceNamesPatch',
    121: 'MenuHelpSnippetsPatch',
    122: 'KeyGuidePatch',
    123: 'MenuText_OtherPatch',
    124: 'MenuText_CommonPatch',
}

_DSR_TO_SS = {
    # item.msgbnd
    'Accessory_long_desc_.text': 'RingDescriptions',
    'Accessory_name_.text': 'RingNames',
    'Accessory_description_.text': 'RingSummaries',
    'Armor_long_desc_.text': 'ArmorDescriptions',
    'Armor_name_.text': 'ArmorNames',
    'Armor_description_.text': 'ArmorSummaries',
    'Feature_long_desc_.text': 'FeatureDescriptions',
    'Feature_name_.text': 'FeatureNames',
    'Feature_description_.text': 'FeatureSummaries',
    'Item_long_desc_.text': 'GoodDescriptions',
    'Item_name_.text': 'GoodNames',
    'Item_description_.text': 'GoodSummaries',
    'Magic_long_desc_.text': 'SpellDescriptions',
    'Magic_name_.text': 'SpellNames',
    'Magic_description_.text': 'SpellSummaries',
    'NPC_name_.text': 'NPCNames',
    'Place_name_.text': 'PlaceNames',
    'Weapon_long_desc_.text': 'WeaponDescriptions',
    'Weapon_name_.text': 'WeaponNames',
    'Weapon_description_.text': 'WeaponSummaries',

    # menu.msgbnd
    'Blood_writing_.text': 'SoapstoneMessages',
    'Conversation_.text': 'Conversations',
    'Dialogue_.text': 'MenuDialogs',
    'Event_text_.text': 'EventText',
    'Ingame_menu.text': 'IngameMenus',
    'Item_help_.text': 'ContextualHelp',
    'Key_guide_.text': 'KeyGuide',
    'Menu_general_text_.text': 'MenuText_Common',
    'Menu_others_.text': 'MenuText_Other',
    'Movie_subtitles_.text': 'OpeningSubtitles',
    'Single_line_help_.text': 'MenuHelpSnippets',
    'System_message_win32_.text': 'SystemMessages_Win32',
    'System_specific_tags_win32_.text': 'DebugTags_Win32',
    'Text_display_tag_list_.text': 'TextTagPlaceholders',
}


_PTD_TO_SS = {
    # item.msgbnd (including patch)
    '防具うんちく.text': 'ArmorDescriptions',
    '防具うんちくパッチ.text': 'ArmorDescriptionsPatch',
    '防具名.text': 'ArmorNames',
    '防具名パッチ.text': 'ArmorNamesPatch',
    '防具説明.text': 'ArmorSummaries',
    '防具説明パッチ.text': 'ArmorSummariesPatch',
    '特徴うんちく.text': 'FeatureDescriptions',
    '特徴名.text': 'FeatureNames',
    '特徴説明.text': 'FeatureSummaries',
    'アイテムうんちく.text': 'GoodDescriptions',
    'アイテムうんちくパッチ.text': 'GoodDescriptionsPatch',
    'アイテム名.text': 'GoodNames',
    'アイテム名パッチ.text': 'GoodNamesPatch',
    'アイテム説明.text': 'GoodSummaries',
    'アイテム説明パッチ.text': 'GoodSummariesPatch',
    'NPC名.text': 'NPCNames',
    'NPC名パッチ.text': 'NPCNamesPatch',
    '地名.text': 'PlaceNames',
    '地名パッチ.text': 'PlaceNamesPatch',
    'アクセサリうんちく.text': 'RingDescriptions',
    'アクセサリうんちくパッチ.text': 'RingDescriptionsPatch',
    'アクセサリ名.text': 'RingNames',
    'アクセサリ名パッチ.text': 'RingNamesPatch',
    'アクセサリ説明.text': 'RingSummaries',
    'アクセサリ説明パッチ.text': 'RingSummariesPatch',
    '魔法うんちく.text': 'SpellDescriptions',
    '魔法うんちくパッチ.text': 'SpellDescriptionsPatch',
    '魔法名.text': 'SpellNames',
    '魔法名パッチ.text': 'SpellNamesPatch',
    '魔法説明.text': 'SpellSummaries',
    '武器うんちく.text': 'WeaponDescriptions',
    '武器うんちくパッチ.text': 'WeaponDescriptionsPatch',
    '武器名.text': 'WeaponNames',
    '武器名パッチ.text': 'WeaponNamesPatch',
    '武器説明.text': 'WeaponSummaries',
    '武器説明パッチ.text': 'WeaponSummariesPatch',

    # menu.msgbnd
    '項目ヘルプ.text': 'ContextualHelp',
    '会話.text': 'Conversations',
    '会話パッチ.text': 'ConversationsPatch',
    '機種別タグ_win32.text': 'DebugTags_Win32',
    'イベントテキスト.text': 'EventText',
    'イベントテキストパッチ.text': 'EventTextPatch',
    'インゲームメニュー.text': 'IngameMenus',
    'キーガイド.text': 'KeyGuide',
    'キーガイドパッチ.text': 'KeyGuidePatch',
    'ダイアログ.text': 'MenuDialogs',
    'ダイアログパッチ.text': 'MenuDialogsPatch',
    '一行ヘルプ.text': 'MenuHelpSnippets',
    '一行ヘルプパッチ.text': 'MenuHelpSnippetsPatch',
    'メニュー共通テキスト.text': 'MenuText_Common',
    'メニュー共通テキストパッチ.text': 'MenuText_CommonPatch',
    'メニューその他.text': 'MenuText_Other',
    'メニューその他パッチ.text': 'MenuText_OtherPatch',
    'ムービー字幕.text': 'OpeningSubtitles',
    '血文字.text': 'SoapstoneMessages',
    '血文字パッチ.text': 'SoapstoneMessagesPatch',
    'システムメッセージ_win32.text': 'SystemMessages_Win32',
    'システムメッセージ_win32パッチ.text': 'SystemMessages_Win32Patch',
    'テキスト表示用タグ一覧.text': 'TextTagPlaceholders',
}
