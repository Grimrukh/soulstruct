from enum import IntEnum

from soulstruct.darksouls1ptde.game_types.map_types import SoundEvent

__all__ = ["Sound", "MusicSound", "SFXSound", "ObjectSound", "VoiceSound", "CharacterMotionSound", "SoundEvent"]


class Sound(IntEnum):
    """Base class for a sound event that can be played transiently at a given anchor entity."""

    @classmethod
    def get_sound_enum(cls):
        raise NotImplementedError("You must use a subclass of Sound.")


class MusicSound(Sound):
    """Music-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        from ..events.enums import SoundType
        return SoundType.m_Music


class SFXSound(Sound):
    """SFX-type sound effect, which is probably the most common one you will want to use."""

    @classmethod
    def get_sound_enum(cls):
        from ..events.enums import SoundType
        return SoundType.s_SFX


class ObjectSound(Sound):
    """Object-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        from ..events.enums import SoundType
        return SoundType.o_Object


class VoiceSound(Sound):
    """Voice-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        from ..events.enums import SoundType
        return SoundType.v_Voice


class CharacterMotionSound(Sound):
    """CharacterMotion-type sound effect, which you will probably not use."""

    @classmethod
    def get_sound_enum(cls):
        from ..events.enums import SoundType
        return SoundType.c_CharacterMotion


# I haven't bothered implementing the other sound types (MenuEffect, Cutscene, Armor/FloorMaterialDependent, Ghost).
