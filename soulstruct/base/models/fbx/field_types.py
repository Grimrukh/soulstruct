import abc

from soulstruct.utilities.maths import Vector3


class BaseFieldType(abc.ABC):

    def __str__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"


class Time(BaseFieldType, int):
    """Epoch time."""


class KTime(BaseFieldType, int):
    """Epoch time, also?."""


class DateTime(BaseFieldType, str):
    """Full datetime string."""


class FieldOfView(BaseFieldType, float):
    """Field of view X."""


class FieldOfViewX(BaseFieldType, float):
    """Field of view X."""


class FieldOfViewY(BaseFieldType, float):
    """Field of view Y."""


class OpticalCenterX(BaseFieldType, float):
    """Optical center X."""


class OpticalCenterY(BaseFieldType, float):
    """Optical center Y."""


class Visibility(BaseFieldType, float):
    """Visibility."""


class VisibilityInheritance(BaseFieldType, int):
    """Visibility inheritance. TODO: Probably actually a bool."""


class LclTranslation(Vector3):
    """Local translation of a model."""
    REPR_PRECISION = 6


class LclRotation(Vector3):
    """Local rotation of a model."""
    REPR_PRECISION = 6


class LclScaling(Vector3):
    """Local scaling of a model."""
    REPR_PRECISION = 6
