import struct

from soulstruct.maps.base.msb import MSB as BaseMSB

from .models import MSBModelList
from .events import MSBEventList
from .regions import MSBRegionList
from .parts import MSBPartList


class MSB(BaseMSB):
    """Handles MSB ('MapStudio') data for Dark Souls. Both versions of the game have identical formats."""

    HEADER = struct.pack("4sII??bb", b"MSB ", 1, 16, False, False, 1, 255)

    MODEL_LIST_CLASS = MSBModelList
    EVENT_LIST_CLASS = MSBEventList
    REGION_LIST_CLASS = MSBRegionList
    PART_LIST_CLASS = MSBPartList

    models: MSBModelList
    events: MSBEventList
    regions: MSBRegionList
    parts: MSBPartList
