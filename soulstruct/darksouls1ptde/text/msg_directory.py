__all__ = ["MSGDirectory", "NEW_FMG_NAMES"]

from soulstruct.base.text.msg_directory import MSGDirectory as _BaseMSGDirectory
from soulstruct.utilities.core import BiDict

from .fmg import FMG


class MSGDirectory(_BaseMSGDirectory):
    IS_DCX = False

    FMG_CLASS = FMG

    _MSGBND_INDEX_NAMES = BiDict(
        (1, "Subtitles"),
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
        (104, "SubtitlesPatch"),
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

    ALL_CATEGORIES = ALL_FMG_NAMES = MAIN_CATEGORIES + INTERNAL_CATEGORIES

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


# Unused; using BND index instead.
NEW_FMG_NAMES = {
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
    "会話.fmg": "Subtitles",
    "会話パッチ.fmg": "SubtitlesPatch",
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
