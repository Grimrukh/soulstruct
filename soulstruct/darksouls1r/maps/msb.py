__all__ = ["MSB"]

from soulstruct.darksouls1ptde.maps.msb import MSB as _BaseMSB

from .models import MSBModelList


class MSB(_BaseMSB):
    """Only difference from DS1PTDE is in the methods."""

    MODEL_LIST_CLASS = MSBModelList

    models: MSBModelList
