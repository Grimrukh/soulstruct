__all__ = ["MSBModel", "MSBModelList"]

from soulstruct.maps.base.models import (
    MSBModel as BaseMSBModel,
    MSBModelList as BaseMSBModelList,
)
from soulstruct.maps.enums import MSBModelSubtype
from soulstruct.utilities import BinaryStruct


class MSBModel(BaseMSBModel):
    """MSB model entry in Dark Souls."""

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("__model_type", "I"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "i"),
        ("_instance_count", "i"),
        "12x",
    )

    ENCODING = "shift_jis_2004"
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0" * 6


class MSBModelList(BaseMSBModelList):

    ENTRY_CLASS = MSBModel


for _entry_subtype in MSBModelSubtype:
    setattr(
        MSBModelList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
