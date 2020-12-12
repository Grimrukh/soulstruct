__all__ = [
    # TODO: MSB
    "MSBModel",
    "MSBSoundEvent",
    "MSBMessageEvent",
]


from soulstruct.maps.base.models import MSBModel as BaseMSBModel
from soulstruct.utilities import BinaryStruct


class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "q"),
        ("__model_type", "I"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "q"),
        ("_instance_count", "i"),
        "12x",
    )

    ENCODING = "utf-16-le"
    NULL = b"\0\0"
    # TODO: Empty sib path different? b"\0\0" * 6 maybe?
