__all__ = ["InstructionDecompiler"]

from typing import Union

from soulstruct.base.events.emevd.decompiler import parse_parameters
from soulstruct.darksouls1ptde.events.emevd.decompiler import InstructionDecompiler as _BaseDecompiler
from soulstruct.darksouls1r.maps.constants import get_map
from soulstruct.game_types.msb_types import *
from .enums import *
from . import enums


class InstructionDecompiler(_BaseDecompiler):
    """Subclass of DS1PTDE decompiler."""

    ENUMS = enums
    GET_MAP = staticmethod(get_map)

    @parse_parameters("Unknown_3_23")
    def _3_23(self, condition, arg1, arg2):
        pass

    @parse_parameters("IfMultiplayerCount", no_name_count=1)
    def _3_24(self, condition, arg1, arg2):
        pass

    @parse_parameters("Unknown_4_15", no_name_count=1)
    def _4_15(self, condition, arg1):
        pass

    @parse_parameters("Unknown_4_16", no_name_count=1)
    def _4_16(self, condition, arg1, arg2, arg3):
        pass

    @parse_parameters("IfArenaMatchmaking", no_name_count=1)
    def _4_17(self, condition):
        pass

    @parse_parameters("Unknown_2000_06")
    def _2000_06(self, arg1):
        pass

    @parse_parameters
    def _2002_06(self, cutscene_id, cutscene_type: CutsceneType, first_region, last_region, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return (
            f"PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1({cutscene_id}, {cutscene_type}, {first_region=}, "
            f"{last_region=}, {game_map=})"
        )

    @parse_parameters
    def _2002_07(self, cutscene_id, cutscene_type: CutsceneType, first_region, last_region, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return (
            f"PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2({cutscene_id}, {cutscene_type}, {first_region=}, "
            f"{last_region=}, {game_map=})"
        )

    @parse_parameters("CopyEventValue")
    def _2003_42(self, source_flag, destination_flag, bit_count):
        pass

    @parse_parameters("Unknown_2003_43")
    def _2003_43(self, flag, bit_count, arg1, arg2):
        pass

    @parse_parameters("ForceAnimation_WithUnknownEffect1", no_name_count=1)
    def _2003_44(
        self,
        entity: Union[Character, Object],
        animation,
        loop: bool,
        wait_for_completion: bool,
        skip_transition: bool,
        arg1,
    ):
        """Does not use default arguments because last argument `arg` is always shown."""
        pass

    @parse_parameters("ForceAnimation_WithUnknownEffect2", no_name_count=1)
    def _2003_46(
        self,
        entity: Union[Character, Object],
        animation,
        loop: bool,
        wait_for_completion: bool,
        skip_transition: bool,
        arg1,
    ):
        """Does not use default arguments because last argument `arg` is always shown."""
        pass

    @parse_parameters("Unknown_2003_47")
    def _2003_47(self):
        pass

    @parse_parameters("Unknown_2003_48")
    def _2003_48(
        self,
        entity: Union[Character, Object],
        arg1,
        model_point,
        magic_id,
        shoot_angle_x,
        shoot_angle_y,
        shoot_angle_z,
    ):
        pass

    @parse_parameters("EraseNPCSummonSign")
    def _2003_49(self, summoned_character: Character):
        pass

    @parse_parameters("FadeOutCharacter", no_name_count=1)
    def _2004_48(self, character: Character, duration):
        pass

    @parse_parameters("FadeInCharacter", no_name_count=1)
    def _2004_49(self, character: Character, duration):
        pass

    @parse_parameters("Unknown_2004_50")
    def _2004_50(self):
        pass

    @parse_parameters("Unknown_2004_51")
    def _2004_51(self, arg1):
        pass

    @parse_parameters("Unknown_2004_52")
    def _2004_52(self):
        pass

    @parse_parameters("ArenaSetNametag5", no_name_count=1)
    def _2007_10(self, player_id: PlayerEntity):
        pass

    @parse_parameters("ArenaSetNametag6", no_name_count=1)
    def _2007_11(self, player_id: PlayerEntity):
        pass

    @parse_parameters("DisplayConcatenatedMessage")
    def _2007_12(self, message_id, pad_enabled: bool, concatenator_base_flag, bit_count):
        pass

    @parse_parameters("Unknown_2007_13")
    def _2007_13(self, arg1):
        pass

    @parse_parameters("Unknown_2008_04")
    def _2008_04(self):
        pass
