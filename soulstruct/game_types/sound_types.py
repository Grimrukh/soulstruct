from enum import IntEnum

from soulstruct.events.shared import instructions as instr
from soulstruct.enums.shared import SoundType
from soulstruct.game_types.basic_types import GameObject
from soulstruct.game_types.msb_types import CoordEntityTyping, SoundEvent

__all__ = ["Sound", "SFXSound", "ObjectSound", "VoiceSound", "CharacterMotionSound", "SoundEvent"]


class Sound(GameObject, IntEnum):
    """Base class for a sound event that can be played transiently at a given anchor entity."""

    def play(self, anchor_entity: CoordEntityTyping):
        return instr.PlaySoundEffect(anchor_entity, self.sound_type, self.value)

    @property
    def sound_type(self):
        raise NotImplementedError("You must use a subclass of Sound.")


class SFXSound(Sound):
    """SFX-type sound effect, which is probably the most common one you will want to use."""

    @property
    def sound_type(self):
        return SoundType.s_SFX


class ObjectSound(Sound):
    """Object-type sound effect."""

    @property
    def sound_type(self):
        return SoundType.o_Object


class VoiceSound(Sound):
    """Voice-type sound effect."""

    @property
    def sound_type(self):
        return SoundType.v_Voice


class CharacterMotionSound(Sound):
    """CharacterMotion-type sound effect, which you will probably not use."""

    @property
    def sound_type(self):
        return SoundType.c_CharacterMotion


# I haven't bothered implementing the other sound types (MenuEffect, Cutscene, Armor/FloorMaterialDependent, Ghost).
