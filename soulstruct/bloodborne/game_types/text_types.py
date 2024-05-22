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

from enum import IntEnum
import typing as tp

from soulstruct.base.game_types import GameObjectInt, Text
from .map_types import CoordEntityTyping

if tp.TYPE_CHECKING:
    from soulstruct.bloodborne.events.enums import *


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

    def as_dialog(
        self,
        anchor_entity: CoordEntityTyping = None,
        display_distance: float = 3.0,
        button_type: ButtonType = None,
        number_buttons: NumberButtons = None,
    ):
        """Display single line of text in a small dialog box at the bottom of the game window."""
        from ..events.enums import PLAYER, ButtonType, NumberButtons
        from ..events.emevd.compiler import compile_instruction
        if anchor_entity is None:
            anchor_entity = PLAYER
        if button_type is None:
            button_type = ButtonType.OK_or_Cancel
        if number_buttons is None:
            number_buttons = NumberButtons.NoButton

        return compile_instruction(
            "DisplayDialog",
            self.value,
            anchor_entity=anchor_entity,
            display_distance=display_distance,
            button_type=button_type,
            number_buttons=number_buttons,
        )

    def as_status(self, pad_enabled: bool = True):
        """Display text in a large status message that appears at the top of the screen.

        If 'pad_enabled' is False, the player will not be able to get rid of the message by pressing any buttons, but
        will instead have to wait for it to time out.

        Note that this text can have two lines. In the vanilla game, it appears when you are cursed for the first time,
        when you first arrive in Lordran, when you obtain the Lordvessel, when you approach a golden fog gate, etc.
        """
        from ..events.emevd.compiler import compile_instruction
        return compile_instruction("DisplayStatus", self.value, pad_enabled=pad_enabled)

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
