from __future__ import annotations

__all__ = [
    "Text",
    "NPCName",
    "PlaceName",
    "EventText",
    "SoapstoneMessage",
    "WeaponName",
    "WeaponSummary",
    "WeaponDescription",
    "ArmorName",
    "ArmorSummary",
    "ArmorDescription",
    "AccessoryName",
    "AccessorySummary",
    "AccessoryDescription",
    "GoodName",
    "GoodSummary",
    "GoodDescription",
    "SpellName",
    "SpellSummary",
    "SpellDescription",
    "Subtitle",
    "StringOffset",
    "EventTextTyping",
    "NPCNameTyping",
    "SubtitleTyping",
    "StringOffsetTyping",
]

import typing as tp

from soulstruct.base.game_types import GameObjectInt, Text


class NPCName(Text):
    """NPC name ID."""
    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_text_category(cls):
        return "NPCNames"


class PlaceName(Text):
    """Place name ID."""
    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_text_category(cls):
        return "PlaceNames"


class EventText(Text):
    """Text ID from the EventText FMG.

    Call the 'as_dialog' or 'as_status' methods in EMEVD to display this text in-game.
    """

    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_text_category(cls):
        return "EventText"


class SoapstoneMessage(Text):
    """Soapstone message ID."""
    @classmethod
    def get_text_category(cls):
        return "SoapstoneMessages"


class WeaponName(Text):
    """Weapon name ID."""
    @classmethod
    def get_text_category(cls):
        return "WeaponNames"


class WeaponSummary(Text):
    """Weapon summary ID."""
    @classmethod
    def get_text_category(cls):
        return "WeaponSummaries"


class WeaponDescription(Text):
    """Weapon description ID."""
    @classmethod
    def get_text_category(cls):
        return "WeaponDescriptions"


class ArmorName(Text):
    """Armor name ID."""
    @classmethod
    def get_text_category(cls):
        return "ArmorNames"


class ArmorSummary(Text):
    """Armor summary ID."""
    @classmethod
    def get_text_category(cls):
        return "ArmorSummaries"


class ArmorDescription(Text):
    """Armor description ID."""
    @classmethod
    def get_text_category(cls):
        return "ArmorDescriptions"


class AccessoryName(Text):
    """Accessory name ID."""
    @classmethod
    def get_text_category(cls):
        return "AccessoryNames"


class AccessorySummary(Text):
    """Accessory summary ID."""
    @classmethod
    def get_text_category(cls):
        return "AccessorySummaries"


class AccessoryDescription(Text):
    """Accessory description ID."""
    @classmethod
    def get_text_category(cls):
        return "AccessoryDescriptions"


class GoodName(Text):
    """Good name ID."""
    @classmethod
    def get_text_category(cls):
        return "GoodNames"


class GoodSummary(Text):
    """Good summary ID."""
    @classmethod
    def get_text_category(cls):
        return "GoodSummaries"


class GoodDescription(Text):
    """Good description ID."""
    @classmethod
    def get_text_category(cls):
        return "GoodDescriptions"


class SpellName(Text):
    """Spell name ID."""
    @classmethod
    def get_text_category(cls):
        return "SpellNames"


class SpellSummary(Text):
    """Spell summary ID."""
    @classmethod
    def get_text_category(cls):
        return "SpellSummaries"


class SpellDescription(Text):
    """Spell description ID."""
    @classmethod
    def get_text_category(cls):
        return "SpellDescriptions"


class Subtitle(Text):
    """Text ID from the Subtitles FMG, which contains dialogue subtitles."""
    @classmethod
    def get_text_category(cls):
        return "Subtitles"


# TODO: I haven't yet bothered with classes for internal text types.


class StringOffset(GameObjectInt):
    """Simple enum for string offsets to be passed to certain EMEVD instructions in later games.

    You are very unlikely to use those instructions, and hence this type.
    """


TextTyping = tp.Union[Text, int]
EventTextTyping = tp.Union[EventText, int]
NPCNameTyping = tp.Union[NPCName, int]
SubtitleTyping = tp.Union[Subtitle, int]
StringOffsetTyping = tp.Union[StringOffset, int]
