from __future__ import annotations

__all__ = ["MapsEditor"]

from soulstruct.base.project.editors.maps import MapsEditor as BaseMapsEditor
from soulstruct.bloodborne import game_types
from soulstruct.bloodborne.game_types import ObjActParam, PlaceName
from soulstruct.darksouls1ptde.maps.parts import MSBPart


class MapsEditor(BaseMapsEditor):

    GAME_TYPES_MODULE = game_types
    GROUP_BIT_COUNT = MSBPart.GROUP_BIT_COUNT

    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        if field_type == ObjActParam and field_value == -1:
            # Link to ObjActParam with the object's model ID.
            obj_act_part = self.get_selected_field_dict()["obj_act_part"]  # type: MSBPart
            field_value = int(obj_act_part.model.name[1:5])

        if valid_null_values is None:
            if field_type == PlaceName:
                valid_null_values = {-1: "Default Map Name + Force Banner"}
            else:
                valid_null_values = {0: "Default/None", -1: "Default/None"}

        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
