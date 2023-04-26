__all__ = ["MSGDirectory"]

import typing as tp

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory, FMG, fmg_property
from .msgbnd import MSGBND


class MSGDirectory(_BaseMSGDirectory):

    FILE_CLASS: tp.ClassVar[tp.Type[MSGBND]] = MSGBND

    DEFAULT_ENTRY_STEMS = {
        ("item", 10): "アイテム名",
        ("item", 11): "武器名",
        ("item", 12): "防具名",
        ("item", 13): "アクセサリ名",
        ("item", 14): "魔法名",
        ("item", 15): "特徴名",
        ("item", 16): "特徴説明",
        ("item", 17): "特徴うんちく",
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

        ("menu", 1): "会話",
        ("menu", 2): "血文字",
        ("menu", 3): "ムービー字幕",
        ("menu", 30): "イベントテキスト",
        ("menu", 70): "インゲームメニュー",
        ("menu", 76): "メニュー共通テキスト",
        ("menu", 77): "メニューその他",
        ("menu", 78): "ダイアログ",
        ("menu", 79): "キーガイド",
        ("menu", 80): "一行ヘルプ",
        ("menu", 81): "項目ヘルプ",
        ("menu", 90): "テキスト表示用タグ一覧",
        ("menu", 91): "機種別タグ_win32",
        ("menu", 92): "システムメッセージ_win32",
        # NOTE: In PTDE, the item 'patch' (DLC) FMGs are in `menu.msgbnd`. In DSR, they are in `item.msgbnd.dcx`.
        ("menu", 100): "アイテムうんちくパッチ",
        ("menu", 101): "イベントテキストパッチ",
        ("menu", 102): "ダイアログパッチ",
        ("menu", 103): "システムメッセージ_win32パッチ",
        ("menu", 104): "会話パッチ",
        ("menu", 105): "魔法うんちくパッチ",
        ("menu", 106): "武器うんちくパッチ",
        ("menu", 107): "血文字パッチ",
        ("menu", 108): "防具うんちくパッチ",
        ("menu", 109): "アクセサリうんちくパッチ",
        ("menu", 110): "アイテム説明パッチ",
        ("menu", 111): "アイテム名パッチ",
        ("menu", 112): "アクセサリ説明パッチ",
        ("menu", 113): "アクセサリ名パッチ",
        ("menu", 114): "武器説明パッチ",
        ("menu", 115): "武器名パッチ",
        ("menu", 116): "防具説明パッチ",
        ("menu", 117): "防具名パッチ",
        ("menu", 118): "魔法名パッチ",
        ("menu", 119): "NPC名パッチ",
        ("menu", 120): "地名パッチ",
        ("menu", 121): "一行ヘルプパッチ",
        ("menu", 122): "キーガイドパッチ",
        ("menu", 123): "メニューその他パッチ",
        ("menu", 124): "メニュー共通テキストパッチ",
    }

    BASE_PATCH_FMGS = {
        ("item", 10): ("menu", 111),
        ("item", 11): ("menu", 115),
        ("item", 12): ("menu", 117),
        ("item", 13): ("menu", 113),
        ("item", 14): ("menu", 118),
        ("item", 18): ("menu", 119),
        ("item", 19): ("menu", 120),
        ("item", 20): ("menu", 110),
        ("item", 21): ("menu", 114),
        ("item", 22): ("menu", 116),
        ("item", 23): ("menu", 112),
        ("item", 24): ("menu", 100),
        ("item", 25): ("menu", 106),
        ("item", 26): ("menu", 108),
        ("item", 27): ("menu", 109),
        ("item", 29): ("menu", 105),
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
    ArmorDescriptionsPatch = fmg_property("menu", 108)  # type: FMG
    ArmorNames = fmg_property("item", 12)  # type: FMG
    ArmorNamesPatch = fmg_property("menu", 117)  # type: FMG
    ArmorSummaries = fmg_property("item", 22)  # type: FMG
    ArmorSummariesPatch = fmg_property("menu", 116)  # type: FMG
    ContextualHelp = fmg_property("menu", 81)  # type: FMG
    DebugTags_Win32 = fmg_property("menu", 91)  # type: FMG
    EventText = fmg_property("menu", 30)  # type: FMG
    EventTextPatch = fmg_property("menu", 101)  # type: FMG
    FeatureDescriptions = fmg_property("item", 17)  # type: FMG
    FeatureNames = fmg_property("item", 15)  # type: FMG
    FeatureSummaries = fmg_property("item", 16)  # type: FMG
    GoodDescriptions = fmg_property("item", 24)  # type: FMG
    GoodDescriptionsPatch = fmg_property("menu", 100)  # type: FMG
    GoodNames = fmg_property("item", 10)  # type: FMG
    GoodNamesPatch = fmg_property("menu", 111)  # type: FMG
    GoodSummaries = fmg_property("item", 20)  # type: FMG
    GoodSummariesPatch = fmg_property("menu", 110)  # type: FMG
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
    NPCNamesPatch = fmg_property("menu", 119)  # type: FMG
    OpeningSubtitles = fmg_property("menu", 3)  # type: FMG
    PlaceNames = fmg_property("item", 19)  # type: FMG
    PlaceNamesPatch = fmg_property("menu", 120)  # type: FMG
    RingDescriptions = fmg_property("item", 27)  # type: FMG
    RingDescriptionsPatch = fmg_property("menu", 109)  # type: FMG
    RingNames = fmg_property("item", 13)  # type: FMG
    RingNamesPatch = fmg_property("menu", 113)  # type: FMG
    RingSummaries = fmg_property("item", 23)  # type: FMG
    RingSummariesPatch = fmg_property("menu", 112)  # type: FMG
    SoapstoneMessages = fmg_property("menu", 2)  # type: FMG
    SoapstoneMessagesPatch = fmg_property("menu", 107)  # type: FMG
    SpellDescriptions = fmg_property("item", 29)  # type: FMG
    SpellDescriptionsPatch = fmg_property("menu", 105)  # type: FMG
    SpellNames = fmg_property("item", 14)  # type: FMG
    SpellNamesPatch = fmg_property("menu", 118)  # type: FMG
    SpellSummaries = fmg_property("item", 28)  # type: FMG  # NOTE: No patch.
    Subtitles = fmg_property("menu", 1)  # type: FMG
    SubtitlesPatch = fmg_property("menu", 104)  # type: FMG
    SystemMessages_Win32 = fmg_property("menu", 92)  # type: FMG
    SystemMessages_Win32Patch = fmg_property("menu", 103)  # type: FMG
    TextTagPlaceholders = fmg_property("menu", 90)  # type: FMG
    WeaponDescriptions = fmg_property("item", 25)  # type: FMG
    WeaponDescriptionsPatch = fmg_property("menu", 106)  # type: FMG
    WeaponNames = fmg_property("item", 11)  # type: FMG
    WeaponNamesPatch = fmg_property("menu", 115)  # type: FMG
    WeaponSummaries = fmg_property("item", 21)  # type: FMG
    WeaponSummariesPatch = fmg_property("menu", 114)  # type: FMG
