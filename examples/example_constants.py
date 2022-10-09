
from soulstruct.darksouls1r.game_types import Character, Flag, Object, EventText
from soulstruct.darksouls1r.game_types.param_types import ItemLotParam


class Flags(Flag):
    PaintedWorldVisited = 11002000


class Characters(Character):
    DepthsChanneler = 1000300


class ItemLots(ItemLotParam):
    # It's good practice to name item lots after their location/context, not the items they may happen to contain in
    # the Item Lot Params.
    InDepthsDoor = 1660


class Objects(Object):
    DepthsDoor = 1001200


class EventTexts(EventText):
    Open = 10010400
    SomethingInDoor = 10010631
    RemoveItemFromDoor = 10010632
