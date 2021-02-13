from soulstruct.base.maps.msb import MSB as _BaseMSB

from .models import MSBModelList
from .events import MSBEventList
from .regions import MSBRegionList
from .parts import MSBPartList


class MSB(_BaseMSB):
    """Handles MSB ('MapStudio') data for Dark Souls. Both versions of the game have identical formats."""

    MODEL_LIST_CLASS = MSBModelList
    EVENT_LIST_CLASS = MSBEventList
    REGION_LIST_CLASS = MSBRegionList
    PART_LIST_CLASS = MSBPartList

    models: MSBModelList
    events: MSBEventList
    regions: MSBRegionList
    parts: MSBPartList
