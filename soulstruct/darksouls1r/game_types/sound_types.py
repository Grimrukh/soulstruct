from enum import IntEnum

from soulstruct.darksouls1ptde.game_types.map_types import CoordEntityTyping, SoundEvent
from .emevd_types import EMEVDObject

__all__ = ["Sound", "MusicSound", "SFXSound", "ObjectSound", "VoiceSound", "CharacterMotionSound", "SoundEvent"]


class Sound(EMEVDObject, IntEnum):
    """Base class for a sound event that can be played transiently at a given anchor entity."""

    def play(self, anchor_entity: CoordEntityTyping):
        return self.compile_instruction("PlaySoundEffect", anchor_entity, self.sound_enum, self.value)

    @property
    def sound_enum(self):
        raise NotImplementedError("You must use a subclass of Sound.")


class MusicSound(Sound):
    """Music-type sound effect."""

    @property
    def sound_enum(self):
        return self.get_enum("SoundType", "m_Music")


class SFXSound(Sound):
    """SFX-type sound effect, which is probably the most common one you will want to use."""

    @property
    def sound_enum(self):
        return self.get_enum("SoundType", "s_SFX")


class ObjectSound(Sound):
    """Object-type sound effect."""

    @property
    def sound_enum(self):
        return self.get_enum("SoundType", "o_Object")


class VoiceSound(Sound):
    """Voice-type sound effect."""

    @property
    def sound_enum(self):
        return self.get_enum("SoundType", "v_Voice")


class CharacterMotionSound(Sound):
    """CharacterMotion-type sound effect, which you will probably not use."""

    @property
    def sound_enum(self):
        return self.get_enum("SoundType", "c_CharacterMotion")


# I haven't bothered implementing the other sound types (MenuEffect, Cutscene, Armor/FloorMaterialDependent, Ghost).
