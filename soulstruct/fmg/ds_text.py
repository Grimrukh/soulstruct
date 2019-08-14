from copy import deepcopy
import os
from soulstruct.bnd import BND
from soulstruct.fmg.core import FMG


class DarkSoulsText(object):

    ArmorDescriptions: dict
    ArmorNames: dict
    ArmorSummaries: dict
    BloodMessages: dict
    ContextualHelp: dict
    Conversations: dict
    DebugTags_Win32: dict
    EventTexts: dict
    FeatureDescriptions: dict
    FeatureNames: dict
    FeatureSummaries: dict
    IngameMenus: dict
    ItemDescriptions: dict
    ItemNames: dict
    ItemSummaries: dict
    KeyGuide: dict
    MenuDialogs: dict
    MenuHelpSnippets: dict
    MenuText_Common: dict
    MenuText_Other: dict
    MovieSubtitles: dict
    NPCNames: dict
    PlaceNames: dict
    RingDescriptions: dict
    RingNames: dict
    RingSummaries: dict
    MagicDescriptions: dict
    MagicNames: dict
    MagicSummaries: dict
    SystemMessages_Win32: dict
    TextTagPlaceholders: dict
    WeaponDescriptions: dict
    WeaponNames: dict
    WeaponSummaries: dict

    def __init__(self, msg_directory=None):
        """ Point this to the directory containing 'item.msgbnd' and 'menu.msgbnd' (should be PTD_DOA_DATA/msg). You can then
        access and modify the `entries` attribute of the FMG data contained inside using the names of the FMGs (which
        are converted to the standardized list below). The source (item/menu) of the FMG and its type (standard/Patch)
        are handled internally.

        Note that only PTD uses Patch resources for the text data added in the DLC; in DSR, these have all been merged into
        the base resources.
        """

        if msg_directory is None:
            msg_directory = default_path('msg/ENGLISH')

        self._bnd_dir = ''
        self._directory = msg_directory
        self._original_names = {}  # The actual within-BND FMG names are completely up to us. My names are nicer.
        self._is_menu = {}  # Records whether each FMG belongs in 'item' or 'menu' MSGBND.
        self._data = {}

        # Patch and non-Patch resources get put into the same attribute here so they can be edited together.
        # This set contains tuple pairs (fmg_name, entry_index) that came from Patch resources.
        self._is_patch = set()

        try:
            self.item_msgbnd = BND(os.path.join(msg_directory, 'item.msgbnd.dcx'))
        except FileNotFoundError:
            self.item_msgbnd = BND(os.path.join(msg_directory, 'item.msgbnd'))
            self._item_dcx = False
        else:
            self._item_dcx = True
            if os.path.isfile(os.path.join(msg_directory, 'item.msgbnd')):
                print("# WARNING: Both DCX and non-DCX 'item.msgbnd' resources were found. Reading only the DCX file, "
                      "and will compress with DCX by default when `.write()` is called.")

        try:
            self.menu_msgbnd = BND(os.path.join(msg_directory, 'menu.msgbnd.dcx'))
        except FileNotFoundError:
            self.menu_msgbnd = BND(os.path.join(msg_directory, 'menu.msgbnd'))
            self._menu_dcx = False
        else:
            self._menu_dcx = True
            if os.path.isfile(os.path.join(msg_directory, 'menu.msgbnd')):
                print("# WARNING: Both DCX and non-DCX 'menu.msgbnd' resources were found. Reading only the DCX file, "
                      "and will compress with DCX by default when `.write()` is called.")

        self.load_fmg_entries_from_bnd(self.item_msgbnd, is_menu=False)
        self.load_fmg_entries_from_bnd(self.menu_msgbnd, is_menu=True)

        for key, fmg_dict in self._data.items():
            setattr(self, key, fmg_dict)

    def load_fmg_entries_from_bnd(self, msgbnd: BND, is_menu: bool):

        # remastered = False if 'win32' in msgbnd[0].path else True

        for entry in msgbnd:
            try:
                new_name = MSGBND_NAMES[entry.id]
            except KeyError:
                raise ValueError(f"BND entry '{entry.path}' has unexpected index {entry.id} in its msgbnd.")

            original_name = os.path.basename(entry.path)

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

    def write(self, msg_directory=None, description_word_wrap_limit=50, separate_patch=False, use_original_names=False,
              double_space_to_double_newline=True, dcx=None):
        """ Export FMGs and repack BND, then write it as packed. Should really just be 'write' and 'pack' methods. """

        new_item_msgbnd = deepcopy(self.item_msgbnd)
        new_menu_msgbnd = deepcopy(self.menu_msgbnd)

        if msg_directory is None:
            msg_directory = self._directory
        item_dcx = self._item_dcx if dcx is None else dcx
        menu_dcx = self._menu_dcx if dcx is None else dcx

        if not separate_patch:
            # Patch indices will all be merged into main resources, so remove any Patch entries from the BND.
            for fmg_name, fmg_entries in self._data.items():
                try:
                    bnd_index = [key for key in MSGBND_NAMES.keys() if MSGBND_NAMES[key] == fmg_name + 'Patch'][0]
                except IndexError:
                    # No Patch version of this FMG.
                    pass
                else:
                    if bnd_index >= 100 and self._is_menu.get(fmg_name + 'Patch', False):
                        self.menu_msgbnd.remove_entry(bnd_index)

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
                    fmg = FMG(fmg_entries_patch)
                    fmg.version = 1
                    fmg.unknown = 0
                    fmg_patch_data = FMG.new_ds1(fmg_entries_patch).pack(
                        word_wrap_limit=word_wrap, double_space_to_double_newline=double_space_to_double_newline)
                    original_name = self._original_names[fmg_name + 'Patch']
                    patch_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name + 'Patch'] else new_item_msgbnd
                    try:
                        bnd_entry_id = [k for k, v in MSGBND_NAMES.items() if v == fmg_name][0]
                    except IndexError:
                        raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
                    bnd_entry = patch_msgbnd.entries_by_id[bnd_entry_id]
                    bnd_entry.data = fmg_patch_data
                    if not use_original_names:
                        # Note that original path is kept.
                        bnd_entry.path = bnd_entry.path.replace(original_name, fmg_name + 'Patch.fmg')

            fmg_main_data = FMG.new_ds1(fmg_entries_main).pack(
                word_wrap_limit=word_wrap, double_space_to_double_newline=double_space_to_double_newline)
            original_name = self._original_names[fmg_name]
            msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            try:
                bnd_entry_id = [k for k, v in MSGBND_NAMES.items() if v == fmg_name][0]
            except IndexError:
                raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
            bnd_entry = msgbnd.entries_by_id[bnd_entry_id]
            bnd_entry.data = fmg_main_data
            if not use_original_names:
                # Note that original path is kept.
                bnd_entry.path = bnd_entry.path.replace(original_name, fmg_name + '.fmg')

        # Write BNDs (to original directory by default).
        new_item_msgbnd.write(os.path.join(msg_directory, 'item.msgbnd' + ('.dcx' if item_dcx else '')))
        new_menu_msgbnd.write(os.path.join(msg_directory, 'menu.msgbnd' + ('.dcx' if menu_dcx else '')))

        # Update BNDs after successful write.
        self.item_msgbnd = new_item_msgbnd
        self.menu_msgbnd = new_menu_msgbnd

    def change_item_text(self, text_dict, index=None, item_type=None):
        if index is None:
            index = text_dict['index']
        if not isinstance(index, (list, tuple)):
            index = (index,)
        if item_type is None:
            item_type = text_dict['item_type']
        item_fmg = self.resolve_item_type(item_type)
        Patch = ''
        for i in index:
            if i not in self[item_fmg + 'Names']:
                print(f"NEW ENTRY: {item_fmg} with index {i} has been added "
                      f"({text_dict.get('name', 'unknown name')})")
            if 'name' in text_dict:
                self[item_fmg + 'Names' + Patch][i] = text_dict['name']
            if 'summary' in text_dict:
                self[item_fmg + 'Summaries' + Patch][i] = text_dict['summary']
            if 'description' in text_dict:
                self[item_fmg + 'Descriptions' + Patch][i] = text_dict['description']

    def search_all(self, search_string, fmg=None, replace_with=None, exclude_conversations=True):
        if fmg is None:
            dicts_to_search = [(fmg_name, fmg_dict) for fmg_name, fmg_dict in self._data.items()
                               if fmg_name != 'Conversations'] if exclude_conversations else self._data.items()
        else:
            dicts_to_search = (fmg, self[fmg]),

        for fmg_name, fmg_dict in dicts_to_search:
            for index, text in fmg_dict.items():
                if search_string in text:
                    print(f"\n~~~ {fmg_name}[{index}]:\n{text}")
                    if replace_with is not None:
                        fmg_dict[index] = text.replace(search_string, replace_with)
                        print(f"-> {fmg_dict[index]}")

    @property
    def fmg_names(self):
        return list(self._data.keys())

    def __iter__(self):
        return iter(self._data.items())

    def __getitem__(self, fmg_name):
        try:
            return self._data[fmg_name]
        except KeyError:
            raise AttributeError(f"Non-existent FMG name: '{fmg_name}'")

    @staticmethod
    def resolve_item_type(item_type):
        if item_type.lower() in ('good', 'item', 'consumable'):
            return 'Item'
        elif item_type.lower() in ('ring', 'accessory'):
            return 'Ring'
        elif item_type.lower() in ('weapon', 'shield'):
            return 'Weapon'
        elif item_type.lower() in ('armour', 'armor', 'protector'):
            return 'Armor'
        elif item_type.lower() == 'equipment':
            raise ValueError("'Equipment' is ambiguous. Did you mean 'weapon', 'armor', or 'ring'?")
        else:
            raise ValueError(f"Unrecognized item type: '{item_type}'")


MSGBND_NAMES = {
    1: 'Conversations',
    2: 'BloodMessages',
    3: 'MovieSubtitles',
    10: 'ItemNames',
    11: 'WeaponNames',
    12: 'ArmorNames',
    13: 'RingNames',
    14: 'MagicNames',
    15: 'FeatureNames',
    16: 'FeatureSummaries',
    17: 'FeatureDescriptions',
    18: 'NPCNames',
    19: 'PlaceNames',
    20: 'ItemSummaries',
    21: 'WeaponSummaries',
    22: 'ArmorSummaries',
    23: 'RingSummaries',
    24: 'ItemDescriptions',
    25: 'WeaponDescriptions',
    26: 'ArmorDescriptions',
    27: 'RingDescriptions',
    28: 'MagicSummaries',
    29: 'MagicDescriptions',
    30: 'EventTexts',
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
    100: 'ItemDescriptionsPatch',
    101: 'EventTextsPatch',
    102: 'MenuDialogsPatch',
    103: 'SystemMessages_Win32Patch',
    104: 'ConversationsPatch',
    105: 'MagicDescriptionsPatch',
    106: 'WeaponDescriptionsPatch',
    107: 'BloodMessagesPatch',
    108: 'ArmorDescriptionsPatch',
    109: 'RingDescriptionsPatch',
    110: 'ItemSummariesPatch',
    111: 'ItemNamesPatch',
    112: 'RingSummariesPatch',
    113: 'RingNamesPatch',
    114: 'WeaponSummariesPatch',
    115: 'WeaponNamesPatch',
    116: 'ArmorSummariesPatch',
    117: 'ArmorNamesPatch',
    118: 'MagicNamesPatch',
    119: 'NPCNamesPatch',
    120: 'PlaceNamesPatch',
    121: 'MenuHelpSnippetsPatch',
    122: 'KeyGuidePatch',
    123: 'MenuText_OtherPatch',
    124: 'MenuText_CommonPatch',
}

DSR_TO_SS = {
    # item.msgbnd
    'Accessory_long_desc_.fmg': 'RingDescriptions',
    'Accessory_name_.fmg': 'RingNames',
    'Accessory_description_.fmg': 'RingSummaries',
    'Armor_long_desc_.fmg': 'ArmorDescriptions',
    'Armor_name_.fmg': 'ArmorNames',
    'Armor_description_.fmg': 'ArmorSummaries',
    'Feature_long_desc_.fmg': 'FeatureDescriptions',
    'Feature_name_.fmg': 'FeatureNames',
    'Feature_description_.fmg': 'FeatureSummaries',
    'Item_long_desc_.fmg': 'ItemDescriptions',
    'Item_name_.fmg': 'ItemNames',
    'Item_description_.fmg': 'ItemSummaries',
    'Magic_long_desc_.fmg': 'MagicDescriptions',
    'Magic_name_.fmg': 'MagicNames',
    'Magic_description_.fmg': 'MagicSummaries',
    'NPC_name_.fmg': 'NPCNames',
    'Place_name_.fmg': 'PlaceNames',
    'Weapon_long_desc_.fmg': 'WeaponDescriptions',
    'Weapon_name_.fmg': 'WeaponNames',
    'Weapon_description_.fmg': 'WeaponSummaries',

    # menu.msgbnd
    'Blood_writing_.fmg': 'BloodMessages',
    'Conversation_.fmg': 'Conversations',
    'Dialogue_.fmg': 'MenuDialogs',
    'Event_text_.fmg': 'EventTexts',
    'Ingame_menu.fmg': 'IngameMenus',
    'Item_help_.fmg': 'ContextualHelp',
    'Key_guide_.fmg': 'KeyGuide',
    'Menu_general_text_.fmg': 'MenuText_Common',
    'Menu_others_.fmg': 'MenuText_Other',
    'Movie_subtitles_.fmg': 'MovieSubtitles',
    'Single_line_help_.fmg': 'MenuHelpSnippets',
    'System_message_win32_.fmg': 'SystemMessages_Win32',
    'System_specific_tags_win32_.fmg': 'DebugTags_Win32',
    'Text_display_tag_list_.fmg': 'TextTagPlaceholders',
}


PTD_TO_SS = {
    # item.msgbnd
    '防具うんちく.fmg': 'ArmorDescriptions',
    '防具うんちくパッチ.fmg': 'ArmorDescriptionsPatch',
    '防具名.fmg': 'ArmorNames',
    '防具名パッチ.fmg': 'ArmorNamesPatch',
    '防具説明.fmg': 'ArmorSummaries',
    '防具説明パッチ.fmg': 'ArmorSummariesPatch',
    '特徴うんちく.fmg': 'FeatureDescriptions',
    '特徴名.fmg': 'FeatureNames',
    '特徴説明.fmg': 'FeatureSummaries',
    'アイテムうんちく.fmg': 'ItemDescriptions',
    'アイテムうんちくパッチ.fmg': 'ItemDescriptionsPatch',
    'アイテム名.fmg': 'ItemNames',
    'アイテム名パッチ.fmg': 'ItemNamesPatch',
    'アイテム説明.fmg': 'ItemSummaries',
    'アイテム説明パッチ.fmg': 'ItemSummariesPatch',
    'NPC名.fmg': 'NPCNames',
    'NPC名パッチ.fmg': 'NPCNamesPatch',
    '地名.fmg': 'PlaceNames',
    '地名パッチ.fmg': 'PlaceNamesPatch',
    'アクセサリうんちく.fmg': 'RingDescriptions',
    'アクセサリうんちくパッチ.fmg': 'RingDescriptionsPatch',
    'アクセサリ名.fmg': 'RingNames',
    'アクセサリ名パッチ.fmg': 'RingNamesPatch',
    'アクセサリ説明.fmg': 'RingSummaries',
    'アクセサリ説明パッチ.fmg': 'RingSummariesPatch',
    '魔法うんちく.fmg': 'MagicDescriptions',
    '魔法うんちくパッチ.fmg': 'MagicDescriptionsPatch',
    '魔法名.fmg': 'MagicNames',
    '魔法名パッチ.fmg': 'MagicNamesPatch',
    '魔法説明.fmg': 'MagicSummaries',
    '武器うんちく.fmg': 'WeaponDescriptions',
    '武器うんちくパッチ.fmg': 'WeaponDescriptionsPatch',
    '武器名.fmg': 'WeaponNames',
    '武器名パッチ.fmg': 'WeaponNamesPatch',
    '武器説明.fmg': 'WeaponSummaries',
    '武器説明パッチ.fmg': 'WeaponSummariesPatch',

    # menu.msgbnd
    '血文字.fmg': 'BloodMessages',
    '血文字パッチ.fmg': 'BloodMessagesPatch',
    '項目ヘルプ.fmg': 'ContextualHelp',
    '会話.fmg': 'Conversations',
    '会話パッチ.fmg': 'ConversationsPatch',
    '機種別タグ_win32.fmg': 'DebugTags_Win32',
    'イベントテキスト.fmg': 'EventTexts',
    'イベントテキストパッチ.fmg': 'EventTextsPatch',
    'インゲームメニュー.fmg': 'IngameMenus',
    'キーガイド.fmg': 'KeyGuide',
    'キーガイドパッチ.fmg': 'KeyGuidePatch',
    'ダイアログ.fmg': 'MenuDialogs',
    'ダイアログパッチ.fmg': 'MenuDialogsPatch',
    '一行ヘルプ.fmg': 'MenuHelpSnippets',
    '一行ヘルプパッチ.fmg': 'MenuHelpSnippetsPatch',
    'メニュー共通テキスト.fmg': 'MenuText_Common',
    'メニュー共通テキストパッチ.fmg': 'MenuText_CommonPatch',
    'メニューその他.fmg': 'MenuText_Other',
    'メニューその他パッチ.fmg': 'MenuText_OtherPatch',
    'ムービー字幕.fmg': 'MovieSubtitles',
    'システムメッセージ_win32.fmg': 'SystemMessages_Win32',
    'システムメッセージ_win32パッチ.fmg': 'SystemMessages_Win32Patch',
    'テキスト表示用タグ一覧.fmg': 'TextTagPlaceholders',
}


if __name__ == '__main__':
    text_ptd = DarkSoulsText(r"G:\Steam\steamapps\common\Dark Souls Prepare to Die Edition\DATA\msg\ENGLISH")
    text_dsr = DarkSoulsText(r"G:\Steam\steamapps\common\DARK SOULS REMASTERED\msg\ENGLISH")
