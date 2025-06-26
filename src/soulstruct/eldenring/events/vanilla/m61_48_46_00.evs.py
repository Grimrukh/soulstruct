"""
Land of Shadow 12-11 NW SW

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005250(0, character=2048460200, region=2048462200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2048460201, region=2048462200, seconds=0.0, animation_id=-1)
    CommonFunc_90005301(0, flag=2048460301, character=2048460301, item_lot__unk1=2048460710, seconds=0.0, unk1=0)
    CommonFunc_90005301(0, flag=2048460390, character=2048460390, item_lot__unk1=40904, seconds=0.0, unk1=0)
    Event_2048462490()


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    Event_2248462300(0, character=2248460291, patrol_information_id=2248463291, region=2248462291, flag=2248462292)
    CommonFunc_90005250(0, character=2248460291, region=2248462290, seconds=0.0, animation_id=-1)
    CommonFunc_90005301(0, flag=2248460291, character=2248460291, item_lot__unk1=2048460700, seconds=4.0, unk1=0)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005430(0, character=2248460291)
    CommonFunc_90005432(0, character=2248460291, flag=2248462291)
    CommonFunc_90005435(
        0,
        character=2248460291,
        flag=2248462292,
        flag_1=2248462293,
        flag_2=2248462294,
        flag_3=2248462295,
    )
    CommonFunc_90005433(0, character=2248460291, flag=2248462296, flag_1=2248462297, flag_2=2248462298)
    CommonFunc_90005434(0, character=2248460291, flag=2248462296, flag_1=2248462297, flag_2=2248462298)
    CommonFunc_90005437(0, character=2248460291, flag=2248462299, flag_1=2248463200)


@RestartOnRest(2048462490)
def Event_2048462490():
    """Event 2048462490"""
    if FlagEnabled(4927):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2048462490))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(4927)
    AddSpecialEffect(PLAYER, 20004230)


@RestartOnRest(2248462300)
def Event_2248462300(
    _,
    character: Character | int,
    patrol_information_id: uint,
    region: Region | int,
    flag: Flag | int,
):
    """Event 2248462300"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
