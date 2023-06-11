__all__ = ["MSGDirectory"]

import typing as tp

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory, FMG, fmg_property
from .msgbnd import MSGBND


class MSGDirectory(_BaseMSGDirectory):

    FILE_CLASS: tp.ClassVar[tp.Type[MSGBND]] = MSGBND

    # NOTE: The 'patch' entries have the exact same Binder paths as non-patch entries, which is (a) one
    # of the VERY few times this has been seen in Binders, and (b) probably QLOC's oversight.
    DEFAULT_ENTRY_STEMS = {
        ("item", 10): "Item_name_",
        ("item", 11): "Weapon_name_",
        ("item", 12): "Armor_name_",
        ("item", 13): "Accessory_name_",
        ("item", 14): "Magic_name_",
        ("item", 15): "Feature_name_",
        ("item", 16): "Feature_description_",
        ("item", 17): "Feature_long_desc_",
        ("item", 18): "NPC_name_",
        ("item", 19): "Place_name_",
        ("item", 20): "Item_description_",
        ("item", 21): "Weapon_description_",
        ("item", 22): "Armor_description_",
        ("item", 23): "Accessory_description_",
        ("item", 24): "Item_long_desc_",
        ("item", 25): "Weapon_long_desc_",
        ("item", 26): "Armor_long_desc_",
        ("item", 27): "Accessory_long_desc_",
        ("item", 28): "Magic_description_",  # NOTE: No patch.
        ("item", 29): "Magic_long_desc_",
        # NOTE: The item 'patch' FMGs are in `item.msgbnd.dcx` rather than `menu` (as in PTDE).
        # The entry IDs are exactly the same, though.
        ("item", 100): "Item_long_desc_",
        ("item", 105): "Magic_long_desc_",
        ("item", 106): "Weapon_long_desc_",
        ("item", 108): "Armor_long_desc_",
        ("item", 109): "Accessory_long_desc_",
        ("item", 110): "Item_description_",
        ("item", 111): "Item_name_",
        ("item", 112): "Accessory_description_",
        ("item", 113): "Accessory_name_",
        ("item", 114): "Weapon_description_",
        ("item", 115): "Weapon_name_",
        ("item", 116): "Armor_description_",
        ("item", 117): "Armor_name_",
        ("item", 118): "Magic_name_",
        ("item", 119): "NPC_name_",
        ("item", 120): "Place_name_",

        ("menu", 1): "Conversation_",
        ("menu", 2): "Blood_writing_",
        ("menu", 3): "Movie_subtitles_",
        ("menu", 30): "Event_text_",
        ("menu", 70): "Ingame_menu_",
        ("menu", 76): "Menu_general_text_",
        ("menu", 77): "Menu_others_",
        ("menu", 78): "Dialogue_",
        ("menu", 79): "Key_guide_",
        ("menu", 80): "Single_line_help_",
        ("menu", 81): "Item_help_",
        ("menu", 90): "Text_display_tag_list_",
        ("menu", 91): "System_specific_tags_win32_",
        ("menu", 92): "System_message_win32_",
        ("menu", 101): "Event_text_",
        ("menu", 102): "Dialogue_",
        ("menu", 103): "System_message_win32_",
        ("menu", 104): "Conversation_",
        ("menu", 107): "Blood_writing_",
        ("menu", 121): "Single_line_help_",
        ("menu", 122): "Key_guide_",
        ("menu", 123): "Menu_others_",
        ("menu", 124): "Menu_general_text_",
    }

    BASE_PATCH_FMGS = {
        # NOTE: Identical to PTDE, except the `item` patches are still in `item`.
        ("item", 10): ("item", 111),
        ("item", 11): ("item", 115),
        ("item", 12): ("item", 117),
        ("item", 13): ("item", 113),
        ("item", 14): ("item", 118),
        ("item", 18): ("item", 119),
        ("item", 19): ("item", 120),
        ("item", 20): ("item", 110),
        ("item", 21): ("item", 114),
        ("item", 22): ("item", 116),
        ("item", 23): ("item", 112),
        ("item", 24): ("item", 100),
        ("item", 25): ("item", 106),
        ("item", 26): ("item", 108),
        ("item", 27): ("item", 109),
        ("item", 29): ("item", 105),
        ("menu", 1): ("menu", 104),
        ("menu", 2): ("menu", 107),
        ("menu", 30): ("menu", 101),
        ("menu", 76): ("menu", 124),
        ("menu", 77): ("menu", 123),
        ("menu", 78): ("menu", 102),
        ("menu", 79): ("menu", 122),
        ("menu", 80): ("menu", 121),
        ("menu", 92): ("menu", 103),
    }

    # NOTE: This is for the GUI, which will always sync Patch categories, so those aren't needed.
    MAIN_CATEGORIES = (
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
    )

    INTERNAL_CATEGORIES = (
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
    )

    ArmorDescriptions = fmg_property("item", 26)  # type: FMG
    ArmorDescriptionsPatch = fmg_property("item", 108)  # type: FMG
    ArmorNames = fmg_property("item", 12)  # type: FMG
    ArmorNamesPatch = fmg_property("item", 117)  # type: FMG
    ArmorSummaries = fmg_property("item", 22)  # type: FMG
    ArmorSummariesPatch = fmg_property("item", 116)  # type: FMG
    ContextualHelp = fmg_property("menu", 81)  # type: FMG
    DebugTags_Win32 = fmg_property("menu", 91)  # type: FMG
    EventText = fmg_property("menu", 30)  # type: FMG
    EventTextPatch = fmg_property("menu", 101)  # type: FMG
    FeatureDescriptions = fmg_property("item", 17)  # type: FMG
    FeatureNames = fmg_property("item", 15)  # type: FMG
    FeatureSummaries = fmg_property("item", 16)  # type: FMG
    GoodDescriptions = fmg_property("item", 24)  # type: FMG
    GoodDescriptionsPatch = fmg_property("item", 100)  # type: FMG
    GoodNames = fmg_property("item", 10)  # type: FMG
    GoodNamesPatch = fmg_property("item", 111)  # type: FMG
    GoodSummaries = fmg_property("item", 20)  # type: FMG
    GoodSummariesPatch = fmg_property("item", 110)  # type: FMG
    IngameMenus = fmg_property("menu", 70)  # type: FMG
    KeyGuide = fmg_property("menu", 79)  # type: FMG
    KeyGuidePatch = fmg_property("menu", 122)  # type: FMG
    MenuDialogs = fmg_property("menu", 78)  # type: FMG
    MenuDialogsPatch = fmg_property("menu", 102)  # type: FMG
    MenuHelpSnippets = fmg_property("menu", 80)  # type: FMG
    MenuHelpSnippetsPatch = fmg_property("menu", 121)  # type: FMG
    MenuText_Common = fmg_property("menu", 76)  # type: FMG
    MenuText_CommonPatch = fmg_property("menu", 124)  # type: FMG
    MenuText_Other = fmg_property("menu", 77)  # type: FMG
    MenuText_OtherPatch = fmg_property("menu", 123)  # type: FMG
    NPCNames = fmg_property("item", 18)  # type: FMG
    NPCNamesPatch = fmg_property("item", 119)  # type: FMG
    OpeningSubtitles = fmg_property("menu", 3)  # type: FMG
    PlaceNames = fmg_property("item", 19)  # type: FMG
    PlaceNamesPatch = fmg_property("item", 120)  # type: FMG
    RingDescriptions = fmg_property("item", 27)  # type: FMG
    RingDescriptionsPatch = fmg_property("item", 109)  # type: FMG
    RingNames = fmg_property("item", 13)  # type: FMG
    RingNamesPatch = fmg_property("item", 113)  # type: FMG
    RingSummaries = fmg_property("item", 23)  # type: FMG
    RingSummariesPatch = fmg_property("item", 112)  # type: FMG
    SoapstoneMessages = fmg_property("menu", 2)  # type: FMG
    SoapstoneMessagesPatch = fmg_property("menu", 107)  # type: FMG
    SpellDescriptions = fmg_property("item", 29)  # type: FMG
    SpellDescriptionsPatch = fmg_property("item", 105)  # type: FMG
    SpellNames = fmg_property("item", 14)  # type: FMG
    SpellNamesPatch = fmg_property("item", 118)  # type: FMG
    SpellSummaries = fmg_property("item", 28)  # type: FMG  # NOTE: No patch.
    Subtitles = fmg_property("menu", 1)  # type: FMG
    SubtitlesPatch = fmg_property("menu", 104)  # type: FMG
    SystemMessages_Win32 = fmg_property("menu", 92)  # type: FMG
    SystemMessages_Win32Patch = fmg_property("menu", 103)  # type: FMG
    TextTagPlaceholders = fmg_property("menu", 90)  # type: FMG
    WeaponDescriptions = fmg_property("item", 25)  # type: FMG
    WeaponDescriptionsPatch = fmg_property("item", 106)  # type: FMG
    WeaponNames = fmg_property("item", 11)  # type: FMG
    WeaponNamesPatch = fmg_property("item", 115)  # type: FMG
    WeaponSummaries = fmg_property("item", 21)  # type: FMG
    WeaponSummariesPatch = fmg_property("item", 114)  # type: FMG

    @classmethod
    def repair_dsr_patch_fmgs(cls, item_bnd_path, menu_bnd_path):
        """Open given DSR text BNDs, rename FMGs to their vanilla names, and duplicate base entry data to any Patch
        (DLC) binder entries (creating them if needed).

        Useful for repairing well-meaning attempts to do away with the 'patch' FMGs in DSR in old Soulstruct versions.
        """
        from soulstruct.containers import Binder

        item = Binder.from_path(item_bnd_path)
        menu = Binder.from_path(menu_bnd_path)

        # Rename item FMGs.
        for (file, entry_id), stem in cls.DEFAULT_ENTRY_STEMS.items():
            binder = item if file == "item" else menu
            try:
                base_entry = binder.entries_by_id[entry_id]
            except KeyError:
                if (file, entry_id) in cls.BASE_PATCH_FMGS.values():
                    continue  # missing DLC entry will be created when base entry is found
                raise ValueError(f"Base entry not found for {file} {entry_id}.")
            if (file, entry_id) in cls.BASE_PATCH_FMGS:
                _, dlc_entry_id = cls.BASE_PATCH_FMGS[(file, entry_id)]
                base_entry.set_path_name(stem + ".fmg")
                # Copy to DLC entry if it doesn't already exist.
                try:
                    patch_entry = binder.entries_by_id[dlc_entry_id]
                except KeyError:
                    patch_entry = base_entry.copy()
                    patch_entry.id = dlc_entry_id
                    binder.add_entry(patch_entry)
                else:
                    # Make sure patch entry has same data as base entry and same stem.
                    patch_entry.data = base_entry.data
                    patch_entry.set_path_name(stem + ".fmg")
            else:
                # Just fix stem.
                base_entry.set_path_name(stem + ".fmg")

        item.write()
        menu.write()
