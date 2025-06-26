from enum import IntEnum

_all__ = [
    "SoundType",
    "Sound",
    "MusicSound",
    "SFXSound",
    "ObjectSound",
    "VoiceSound",
    "CharacterMotionSound",
    "SoundEvent",
]


class SoundType(IntEnum):
    """The initial letter is prefixed to the sound ID to find the sound file in the FEV."""
    a_Ambient = 0
    c_CharacterMotion = 1
    f_MenuEffect = 2
    o_Object = 3
    p_Cutscene = 4  # the 'p' stands for 'poly play' or 'poly-scn'.
    s_SFX = 5
    m_Music = 6
    v_Voice = 7
    x_FloorMaterialDependent = 8
    b_ArmorMaterialDependent = 9
    g_Ghost = 10
    unk_GeometrySet = 14


class Sound(IntEnum):
    """Base class for a sound event that can be played transiently at a given anchor entity."""

    @classmethod
    def get_sound_enum(cls):
        raise NotImplementedError("You must use a subclass of Sound.")


class MusicSound(Sound):
    """Music-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        return SoundType.m_Music


class SFXSound(Sound):
    """SFX-type sound effect, which is probably the most common one you will want to use."""

    @classmethod
    def get_sound_enum(cls):
        return SoundType.s_SFX


class ObjectSound(Sound):
    """Object-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        return SoundType.o_Object


class VoiceSound(Sound):
    """Voice-type sound effect."""

    @classmethod
    def get_sound_enum(cls):
        return SoundType.v_Voice


class CharacterMotionSound(Sound):
    """CharacterMotion-type sound effect, which you will probably not use."""

    @classmethod
    def get_sound_enum(cls):
        return SoundType.c_CharacterMotion


# I haven't bothered implementing the other sound types (MenuEffect, Cutscene, Armor/FloorMaterialDependent, Ghost).
