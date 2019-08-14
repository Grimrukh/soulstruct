from enum import IntEnum
from typing import Union

from soulstruct.emevd.shared import instructions as instr
from soulstruct.enums.shared import ButtonType, NumberButtons, PLAYER
from soulstruct.game_types.basic_types import GameObject
from soulstruct.game_types.msb_types import CoordEntityInt

__all__ = ['Text', 'EventText', 'StringOffset', 'EventTextInt', 'StringOffsetInt']


class Text(GameObject, IntEnum):
    """Base class for a text ID from an FMG.

    Note that only the EventText subclass can be used in any EMEVD instructions.
    """
    pass


class EventText(Text):
    """Text ID from the EventText FMG.

    Call the 'as_dialog' or 'as_status' methods in EMEVD to display this text in-game.
    """

    def as_dialog(self, anchor_entity: CoordEntityInt = PLAYER, display_distance: float = 3.0,
                  button_type: ButtonType = ButtonType.OK_or_Cancel,
                  number_buttons: NumberButtons = NumberButtons.NoButton):
        """Display single line of text in a small dialog box at the bottom of the game window."""
        instr.DisplayDialog(self.value, anchor_entity=anchor_entity, display_distance=display_distance,
                            button_type=button_type, number_buttons=number_buttons)

    def as_status(self, pad_enabled: bool = True):
        """Display text in a large status message that appears at the top of the screen.

        If 'pad_enabled' is False, the player will not be able to get rid of the message by pressing any buttons, but
        will instead have to wait for it to time out.

        Note that this text can have two lines. In the vanilla game, it appears when you are cursed for the first time,
        when you first arrive in Lordran, when you obtain the Lordvessel, when you approach a golden fog gate, etc.
        """
        instr.DisplayStatus(self.value, pad_enabled=pad_enabled)


# I haven't yet bothered with classes for other text types, as they will have no methods (relevant to EMEVD at least).


class StringOffset(GameObject, IntEnum):
    """Simple enum for string offsets to be passed to certain EMEVD instructions in later games.

    You are very unlikely to use those instructions, and hence this type.
    """
    pass


TextInt = Union[Text, int]
EventTextInt = Union[EventText, int]
StringOffsetInt = Union[StringOffset, int]
