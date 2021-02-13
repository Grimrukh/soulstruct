__all__ = ["MSGDirectory"]

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory
from soulstruct.utilities.core import BiDict

from .fmg import FMG


class MSGDirectory(_BaseMSGDirectory):
    FMG_CLASS = FMG

    _MSGBND_INDEX_NAMES = BiDict(
        (1, "Subtitles"),
        (2, "SoapstoneMessages"),
        (3, "OpeningSubtitles"),
        (4, "CausesOfDeath"),
        (10, "GoodNames"),
        (11, "WeaponNames"),
        (12, "ArmorNames"),
        (13, "RingNames"),
        (14, "SpellNames"),
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
        (31, "BloodGemNames"),
        (32, "BloodGemSummaries"),
        (33, "BloodGemDescriptions"),
        (34, "BloodGemPrefixes"),
        (35, "BloodGemEffects"),
        (70, "IngameMenus"),
        (76, "MenuText_Common"),
        (77, "MenuText_Other"),
        (78, "MenuDialogs"),
        (79, "KeyGuide"),
        (80, "MenuHelpSnippets"),
        (90, "TextTagPlaceholders"),
        (91, "DebugTags_Win64"),
        (92, "SystemMessages_Win64"),
        # Old playtest categories.
        (200, "MenuText_SP"),
        (201, "MenuHelpSnippets_SP"),
        (202, "KeyGuide_SP"),
        (203, "SystemMessages_Win64_SP"),
        (204, "MenuDialogs_SP"),
        # NOTE: No Patch categories.
    )

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
        "BloodGemNames",
        "BloodGemSummaries",
        "BloodGemDescriptions",
        "BloodGemEffects",
        "Subtitles",
    )

    INTERNAL_CATEGORIES = (
        "BloodGemPrefixes",
        "CausesOfDeath",
        "ContextualHelp",
        "DebugTags_Win64",
        "FeatureNames",
        "FeatureSummaries",
        "FeatureDescriptions",
        "IngameMenus",
        "KeyGuide",
        "KeyGuide_SP",
        "MenuDialogs",
        "MenuDialogs_SP",
        "MenuHelpSnippets",
        "MenuHelpSnippets_SP",
        "MenuText_Common",
        "MenuText_Other",
        "MenuText_SP",
        "OpeningSubtitles",
        "SystemMessages_Win64",
        "SystemMessages_Win64_SP",
        "TextTagPlaceholders",
    )

    ALL_CATEGORIES = ALL_FMG_NAMES = MAIN_CATEGORIES + INTERNAL_CATEGORIES

    ArmorDescriptions: dict
    ArmorNames: dict
    ArmorSummaries: dict
    BloodGemDescriptions: dict
    BloodGemEffects: dict
    BloodGemNames: dict
    BloodGemPrefixes: dict
    BloodGemSummaries: dict
    CausesOfDeath: dict
    ContextualHelp: dict
    Subtitles: dict
    DebugTags_Win64: dict
    EventText: dict
    FeatureDescriptions: dict
    FeatureNames: dict
    FeatureSummaries: dict
    IngameMenus: dict
    GoodDescriptions: dict
    GoodNames: dict
    GoodSummaries: dict
    KeyGuide: dict
    KeyGuide_SP: dict
    SpellDescriptions: dict
    SpellNames: dict
    SpellSummaries: dict
    MenuDialogs: dict
    MenuDialogs_SP: dict
    MenuHelpSnippets: dict
    MenuHelpSnippets_SP: dict
    MenuText_Common: dict
    MenuText_Other: dict
    MenuText_SP: dict
    NPCNames: dict
    OpeningSubtitles: dict
    PlaceNames: dict
    RingDescriptions: dict
    RingNames: dict
    RingSummaries: dict
    SoapstoneMessages: dict
    SystemMessages_Win64: dict
    SystemMessages_Win64_SP: dict
    TextTagPlaceholders: dict
    WeaponDescriptions: dict
    WeaponNames: dict
    WeaponSummaries: dict
