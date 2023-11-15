__all__ = ["FLVER"]

from dataclasses import dataclass

from soulstruct.base.models.flver import FLVER as BaseFLVER, Version


@dataclass(slots=True)
class FLVER(BaseFLVER):

    version: Version = Version.Bloodborne_DS3_A
