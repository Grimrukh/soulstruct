"""
Currently uses original FMG names as dictionary names, and lists all as non-internal.
"""

__all__ = ["MSGDirectory"]

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory
from soulstruct.containers.bnd import BND4
from soulstruct.utilities.misc import BiDict

from .fmg import FMG


class MSGDirectory(_BaseMSGDirectory):
    IS_DCX = True

    FMG_CLASS = FMG
    MSGBND_CLASS = BND4

    _MSGBND_INDEX_NAMES = BiDict(
        # item.msgbnd.dcx
        (10, "GoodNames"),
        (11, "WeaponNames"),
        (12, "ArmorNames"),
        (13, "TalismanNames"),
        (14, "SpellNames"),
        (18, "NPCNames"),
        (19, "PlaceNames"),
        (20, "GoodSummaries"),
        (21, "WeaponSummaries"),
        (22, "ArmorSummaries"),
        (23, "TalismanSummaries"),
        (24, "GoodDescriptions"),
        (25, "WeaponDescriptions"),
        (26, "ArmorDescriptions"),
        (27, "TalismanDescriptions"),
        (28, "SpellSummaries"),
        (29, "SpellDescriptions"),
        (35, "GemNames"),
        (36, "GemSummaries"),
        (37, "GemDescriptions"),
        (41, "GoodDialogs"),
        (42, "WeaponArtNames"),
        (43, "WeaponArtSummaries"),
        (44, "WeaponEffects"),
        (45, "GemEffects"),
        (46, "GoodTips"),

        # menu.msgbnd.dcx
        (1, "Subtitles"),
        (2, "SoapstoneMessages"),
        (3, "OpeningSubtitles"),
        (31, "NetworkMessages"),
        (32, "ActionButtonText"),
        (33, "EventTextTalk"),
        (34, "EventTextMap"),
        (200, "MenuText"),
        (201, "LineHelp"),
        (202, "KeyGuide"),
        (203, "SystemMessages"),
        (204, "Dialogues"),
        (205, "LoadingTitle"),
        (206, "LoadingText"),
        (207, "TutorialTitle"),
        (208, "TutorialBody"),
        (209, "TextEmbedImageName"),
        (210, "TermsOfService"),
    )

    MAIN_CATEGORIES = (
        "GoodNames",
        "WeaponNames",
        "ArmorNames",
        "TalismanNames",
        "SpellNames",
        "NPCNames",
        "PlaceNames",
        "GoodSummaries",
        "WeaponSummaries",
        "ArmorSummaries",
        "TalismanSummaries",
        "GoodDescriptions",
        "WeaponDescriptions",
        "ArmorDescriptions",
        "TalismanDescriptions",
        "SpellSummaries",
        "SpellDescriptions",
        "GemNames",
        "GemSummaries",
        "GemDescriptions",
        "GoodDialogs",
        "WeaponArtNames",
        "WeaponArtSummaries",
        "WeaponEffects",
        "GemEffects",
        "GoodTips",

        "Subtitles",
        "SoapstoneMessages",
        "NetworkMessages",
        "ActionButtonText",
        "EventTextTalk",
        "EventTextMap",
        "Dialogues",
        "LoadingTitle",
        "LoadingText",
        "TutorialTitle",
        "TutorialBody",
    )

    INTERNAL_CATEGORIES = (
        "OpeningSubtitles",
        "MenuText",
        "LineHelp",
        "KeyGuide",
        "SystemMessages",
        "TextEmbedImageName",
        "TermsOfService",
    )

    ALL_CATEGORIES = ALL_FMG_NAMES = MAIN_CATEGORIES + INTERNAL_CATEGORIES

    GoodNames: dict
    WeaponNames: dict
    ArmorNames: dict
    TalismanNames: dict
    SpellNames: dict
    NPCNames: dict
    PlaceNames: dict
    GoodSummaries: dict
    WeaponSummaries: dict
    ArmorSummaries: dict
    TalismanSummaries: dict
    GoodDescriptions: dict
    WeaponDescriptions: dict
    ArmorDescriptions: dict
    TalismanDescriptions: dict
    SpellSummaries: dict
    SpellDescriptions: dict
    GemNames: dict
    GemSummaries: dict
    GemDescriptions: dict
    GoodDialogs: dict
    WeaponArtNames: dict
    WeaponArtSummaries: dict
    WeaponEffects: dict
    GemEffects: dict
    GoodTips: dict

    Subtitles: dict
    SoapstoneMessages: dict
    OpeningSubtitles: dict
    NetworkMessages: dict
    ActionButtonText: dict
    EventTextTalk: dict
    EventTextMap: dict
    MenuText: dict
    LineHelp: dict
    KeyGuide: dict
    SystemMessages: dict
    Dialogues: dict
    LoadingTitle: dict
    LoadingText: dict
    TutorialTitle: dict
    TutorialBody: dict
    TextEmbedImageName: dict
    TermsOfService: dict
