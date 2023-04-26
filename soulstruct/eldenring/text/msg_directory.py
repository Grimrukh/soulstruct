__all__ = ["MSGDirectory"]

import typing as tp

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory, FMG, fmg_property
from .msgbnd import MSGBND


class MSGDirectory(_BaseMSGDirectory):
    FILE_CLASS: tp.ClassVar[tp.Type[MSGBND]] = MSGBND

    DEFAULT_ENTRY_STEMS = {
        # ITEM
        ("item", 10): "GoodsName",
        ("item", 11): "WeaponName",
        ("item", 12): "ProtectorName",
        ("item", 13): "AccessoryName",
        ("item", 14): "MagicName",
        ("item", 18): "NpcName",
        ("item", 19): "PlaceName",
        ("item", 20): "GoodsInfo",
        ("item", 21): "WeaponInfo",
        ("item", 22): "ProtectorInfo",
        ("item", 23): "AccessoryInfo",
        ("item", 24): "GoodsCaption",
        ("item", 25): "WeaponCaption",
        ("item", 26): "ProtectorCaption",
        ("item", 27): "AccessoryCaption",
        ("item", 28): "MagicInfo",
        ("item", 29): "MagicCaption",
        ("item", 35): "GemName",
        ("item", 36): "GemInfo",
        ("item", 37): "GemCaption",
        ("item", 41): "GoodsDialog",
        ("item", 42): "ArtsName",
        ("item", 43): "ArtsCaption",
        ("item", 44): "WeaponEffect",
        ("item", 45): "GemEffect",
        ("item", 46): "GoodsInfo2",
        # MENU
        ("menu", 1): "TalkMsg",
        ("menu", 2): "BloodMsg",
        ("menu", 3): "MovieSubtitle",
        ("menu", 31): "NetworkMessage",
        ("menu", 32): "ActionButtonText",
        ("menu", 33): "EventTextForTalk",
        ("menu", 34): "EventTextForMap",
        ("menu", 200): "GR_MenuText",
        ("menu", 201): "GR_LineHelp",
        ("menu", 202): "GR_KeyGuide",
        ("menu", 203): "GR_System_Message_win64",
        ("menu", 204): "GR_Dialogues",
        ("menu", 205): "LoadingTitle",
        ("menu", 206): "LoadingText",
        ("menu", 207): "TutorialTitle",
        ("menu", 208): "TutorialBody",
        ("menu", 209): "TextEmbedImageName_win64",
        ("menu", 210): "ToS_win64",
    }

    MAIN_CATEGORIES = (
        "AccessoryCaptions",
        "AccessoryInfo",
        "AccessoryNames",
        "ActionButtonText",
        "ArmorCaptions",
        "ArmorInfo",
        "ArmorNames",
        "ArtsCaptions",
        "ArtsNames",
        "EventTextMap",
        "EventTextTalk",
        "GemCaptions",
        "GemEffects",
        "GemInfo",
        "GemNames",
        "GoodsCaptions",
        "GoodsDialogs",
        "GoodsInfo",
        "GoodsTips",
        "GoodsNames",
        "LoadingText",
        "LoadingTitle",
        "NetworkMessages",
        "NPCNames",
        "PlaceNames",
        "SoapstoneMessages",
        "SpellCaptions",
        "SpellInfo",
        "SpellNames",
        "Subtitles",
        "SystemMessageWin64",
        "TalkMessages",
        "TutorialBody",
        "TutorialTitle",
        "WeaponCaptions",
        "WeaponEffects",
        "WeaponInfo",
        "WeaponNames",
    )

    INTERNAL_CATEGORIES = (
        "KeyGuide",
        "LineHelp",
        "MovieSubtitles",
        "SystemMessagesWin64",
        "TermsOfService",
        "TextEmbedImageNames",
    )

    ALL_CATEGORIES = ALL_FMG_NAMES = MAIN_CATEGORIES + INTERNAL_CATEGORIES

    AccessoryCaptions = fmg_property("item", 27)  # type: FMG
    AccessoryInfo = fmg_property("item", 23)  # type: FMG
    AccessoryNames = fmg_property("item", 13)  # type: FMG
    ActionButtonText = fmg_property("menu", 32)  # type: FMG
    ArmorCaptions = fmg_property("item", 26)  # type: FMG
    ArmorInfo = fmg_property("item", 22)  # type: FMG
    ArmorNames = fmg_property("item", 12)  # type: FMG
    ArtsCaptions = fmg_property("item", 43)  # type: FMG
    ArtsNames = fmg_property("item", 42)  # type: FMG
    EventTextMap = fmg_property("menu", 34)  # type: FMG
    EventTextTalk = fmg_property("menu", 33)  # type: FMG
    GemCaptions = fmg_property("item", 37)  # type: FMG
    GemEffects = fmg_property("item", 45)  # type: FMG
    GemInfo = fmg_property("item", 36)  # type: FMG
    GemNames = fmg_property("item", 35)  # type: FMG
    GoodsCaptions = fmg_property("item", 24)  # type: FMG
    GoodsDialogs = fmg_property("item", 41)  # type: FMG
    GoodsInfo = fmg_property("item", 20)  # type: FMG
    GoodsTips = fmg_property("item", 46)  # type: FMG
    GoodsNames = fmg_property("item", 10)  # type: FMG
    KeyGuide = fmg_property("menu", 202)  # type: FMG
    LineHelp = fmg_property("menu", 201)  # type: FMG
    LoadingText = fmg_property("menu", 206)  # type: FMG
    LoadingTitle = fmg_property("menu", 205)  # type: FMG
    MenuText = fmg_property("menu", 200)  # type: FMG
    MovieSubtitles = fmg_property("menu", 3)  # type: FMG
    NetworkMessages = fmg_property("menu", 31)  # type: FMG
    NPCNames = fmg_property("item", 18)  # type: FMG
    PlaceNames = fmg_property("item", 19)  # type: FMG
    SoapstoneMessages = fmg_property("menu", 2)  # type: FMG
    SpellCaptions = fmg_property("item", 29)  # type: FMG
    SpellInfo = fmg_property("item", 28)  # type: FMG
    SpellNames = fmg_property("item", 14)  # type: FMG
    Subtitles = fmg_property("menu", 204)  # type: FMG
    SystemMessageWin64 = fmg_property("menu", 203)  # type: FMG
    TalkMessages = fmg_property("menu", 1)  # type: FMG
    TermsOfService = fmg_property("menu", 210)  # type: FMG
    TextEmbedImageNames = fmg_property("menu", 209)  # type: FMG
    TutorialBody = fmg_property("menu", 208)  # type: FMG
    TutorialTitle = fmg_property("menu", 207)  # type: FMG
    WeaponCaptions = fmg_property("item", 25)  # type: FMG
    WeaponEffects = fmg_property("item", 44)  # type: FMG
    WeaponInfo = fmg_property("item", 21)  # type: FMG
    WeaponNames = fmg_property("item", 11)  # type: FMG
