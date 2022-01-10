__all__ = ["MSGDirectory", "NEW_FMG_NAMES"]

from soulstruct.darksouls1ptde.text.msg_directory import MSGDirectory as _BaseMSGDirectory


class MSGDirectory(_BaseMSGDirectory):
    """Mostly identical to PTDE."""
    IS_DCX = True
    _ORIGINAL_PATCH_SUFFIX = ""  # Patch FMG names are identical to non-Patch ones


# Unused; using BND index instead.
NEW_FMG_NAMES = {
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
    "Conversation_.fmg": "Subtitles",
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
