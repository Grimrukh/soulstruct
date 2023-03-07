__all__ = ["MSGDirectory"]

import typing as tp

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory, fmg_property
from soulstruct.base.text.fmg import FMG
from .msgbnd import MSGBND


class MSGDirectory(_BaseMSGDirectory):

    FILE_CLASS: tp.ClassVar[tp.Type[MSGBND]] = MSGBND

    DEFAULT_ENTRY_STEMS = {
        # ITEM
        ("item", 10): "アイテム名",
        ("item", 11): "武器名",
        ("item", 12): "防具名",
        ("item", 13): "アクセサリ名",
        ("item", 14): "魔法名",
        ("item", 18): "NPC名",
        ("item", 19): "地名",
        ("item", 20): "アイテム説明",
        ("item", 21): "武器説明",
        ("item", 22): "防具説明",
        ("item", 23): "アクセサリ説明",
        ("item", 24): "アイテムうんちく",
        ("item", 25): "武器うんちく",
        ("item", 26): "防具うんちく",
        ("item", 27): "アクセサリうんちく",
        ("item", 28): "魔法説明",
        ("item", 29): "魔法うんちく",
        # MENU
        ("menu", 1): "会話",
        ("menu", 2): "血文字",
        ("menu", 3): "ムービー字幕",
        ("menu", 4): "死因",
        ("menu", 30): "イベントテキスト",
        ("menu", 31): "魔石名",
        ("menu", 32): "魔石説明",
        ("menu", 33): "魔石うんちく",
        ("menu", 34): "魔石接頭語",
        ("menu", 35): "魔石効果",
        ("menu", 70): "インゲームメニュー",
        ("menu", 76): "メニュー共通テキスト",
        ("menu", 77): "メニューその他",
        ("menu", 78): "ダイアログ",
        ("menu", 79): "キーガイド",
        ("menu", 80): "一行ヘルプ",
        ("menu", 90): "テキスト表示用タグ一覧",
        ("menu", 91): "機種別タグ_win64",
        ("menu", 92): "システムメッセージ_win64",
        ("menu", 200): "SP_メニューテキスト",
        ("menu", 201): "SP_一行ヘルプ",
        ("menu", 202): "SP_キーガイド",
        ("menu", 203): "SP_システムメッセージ_win64",
        ("menu", 204): "SP_ダイアログ",
    }

    BASE_PATCH_FMGS = {}  # no patches

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
        "AccessoryNames",
        "AccessorySummaries",
        "AccessoryDescriptions",
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

    ArmorDescriptions = fmg_property("item", 26)  # type: FMG
    ArmorNames = fmg_property("item", 12)  # type: FMG
    ArmorSummaries = fmg_property("item", 22)  # type: FMG
    BloodGemDescriptions = fmg_property("menu", 33)  # type: FMG
    BloodGemEffects = fmg_property("menu", 35)  # type: FMG
    BloodGemNames = fmg_property("menu", 31)  # type: FMG
    BloodGemPrefixes = fmg_property("menu", 34)  # type: FMG
    BloodGemSummaries = fmg_property("menu", 32)  # type: FMG
    CausesOfDeath = fmg_property("menu", 4)  # type: FMG
    Subtitles = fmg_property("menu", 1)  # type: FMG
    DebugTags_Win64 = fmg_property("menu", 91)  # type: FMG
    EventText = fmg_property("menu", 30)  # type: FMG
    IngameMenus = fmg_property("menu", 70)  # type: FMG
    GoodDescriptions = fmg_property("item", 24)  # type: FMG
    GoodNames = fmg_property("item", 10)  # type: FMG
    GoodSummaries = fmg_property("item", 20)  # type: FMG
    KeyGuide = fmg_property("menu", 79)  # type: FMG
    KeyGuide_SP = fmg_property("menu", 202)  # type: FMG
    SpellDescriptions = fmg_property("item", 27)  # type: FMG
    SpellNames = fmg_property("item", 14)  # type: FMG
    SpellSummaries = fmg_property("item", 28)  # type: FMG
    MenuDialogs = fmg_property("menu", 78)  # type: FMG
    MenuDialogs_SP = fmg_property("menu", 204)  # type: FMG
    MenuHelpSnippets = fmg_property("menu", 80)  # type: FMG
    MenuHelpSnippets_SP = fmg_property("menu", 201)  # type: FMG
    MenuText_Common = fmg_property("menu", 76)  # type: FMG
    MenuText_Other = fmg_property("menu", 77)  # type: FMG
    MenuText_SP = fmg_property("menu", 200)  # type: FMG
    NPCNames = fmg_property("item", 18)  # type: FMG
    OpeningSubtitles = fmg_property("menu", 3)  # type: FMG
    PlaceNames = fmg_property("item", 19)  # type: FMG
    AccessoryDescriptions = fmg_property("item", 27)  # type: FMG
    AccessoryNames = fmg_property("item", 13)  # type: FMG
    AccessorySummaries = fmg_property("item", 23)  # type: FMG
    SoapstoneMessages = fmg_property("menu", 2)  # type: FMG
    SystemMessages_Win64 = fmg_property("menu", 92)  # type: FMG
    SystemMessages_Win64_SP = fmg_property("menu", 203)  # type: FMG
    TextTagPlaceholders = fmg_property("menu", 90)  # type: FMG
    WeaponDescriptions = fmg_property("item", 25)  # type: FMG
    WeaponNames = fmg_property("item", 11)  # type: FMG
    WeaponSummaries = fmg_property("item", 21)  # type: FMG
