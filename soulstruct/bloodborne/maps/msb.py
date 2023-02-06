
from soulstruct.base.maps.msb import MSB as _BaseMSB

class MSB(_BaseMSB, BloodborneType):
    """Handles MSB ('MapStudio') data for Dark Souls. Both versions of the game have identical formats."""
    # TODO: subtype lists