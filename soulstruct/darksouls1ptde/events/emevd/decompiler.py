__all__ = ["InstructionDecompiler"]

from typing import Union

from soulstruct.base.events.emevd.decompiler import InstructionDecompiler as _BaseDecompiler, parse_parameters
from soulstruct.darksouls1ptde.maps.constants import get_map
from soulstruct.game_types.msb_types import *
from . import enums


class InstructionDecompiler(_BaseDecompiler):

    ENUMS = enums
    GET_MAP = staticmethod(get_map)

    @parse_parameters
    def _2003_41(self, area_id, block_id, y_threshold, target_model_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return f"ActivateKillplaneForModel({game_map=}, {y_threshold=}, {target_model_id=})"

    @parse_parameters("AddSpecialEffect", no_name_count=2)
    def _2004_08(self, character: Character, special_effect_id):
        pass

    @parse_parameters("RotateToFaceEntity", no_name_count=2)
    def _2004_14(self, character: Character, target_entity_id: Union[Character, Object, Region]):
        pass
