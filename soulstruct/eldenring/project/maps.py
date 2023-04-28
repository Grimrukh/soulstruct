from __future__ import annotations

__all__ = ["MapsEditor"]

from soulstruct.base.project.editors import MapsEditor as BaseMapsEditor
from soulstruct.eldenring import game_types
from soulstruct.eldenring.maps.parts import MSBPart


class MapsEditor(BaseMapsEditor):

    GAME_TYPES_MODULE = game_types
    GROUP_BIT_COUNT = MSBPart.GROUP_BIT_COUNT
