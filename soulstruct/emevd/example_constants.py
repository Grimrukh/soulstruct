
from soulstruct.emevd.ds_types import Character, Flag, ItemLot, Object, Text


class FLAGS(Flag):
    PaintedWorldVisited = 11002000


class CHARACTERS(Character):
    DepthsChanneler = 1000300


class ITEMLOT(ItemLot):
    # It's good practice to name item lots after their location/context, not the items they may happen to contain in
    # the Item Lot Params.
    InDepthsDoor = 1660


class OBJECTS(Object):
    DepthsDoor = 1001200


class TEXT(Text):
    Open = 10010400
    SomethingInDoor = 10010631
    RemoveItemFromDoor = 10010632
