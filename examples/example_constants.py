
from soulstruct.game_types import Character, Flag, Object, Text
from soulstruct.darksouls1ptde.game_types.param_types import ItemLotParam


class FLAGS(Flag):
    PaintedWorldVisited = 11002000


class CHARACTERS(Character):
    DepthsChanneler = 1000300


class ITEMLOT(ItemLotParam):
    # It's good practice to name item lots after their location/context, not the items they may happen to contain in
    # the Item Lot Params.
    InDepthsDoor = 1660


class OBJECTS(Object):
    DepthsDoor = 1001200


class TEXT(Text):
    Open = 10010400
    SomethingInDoor = 10010631
    RemoveItemFromDoor = 10010632
