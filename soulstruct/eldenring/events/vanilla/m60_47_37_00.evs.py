"""
East Limgrave (SE) (NE)

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
from .entities.m60_47_37_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1047372200(
        0,
        flag=1047370350,
        flag_1=1047372350,
        anchor_entity=Characters.WanderingNoble,
        character=Characters.Troll,
        left=1,
        item_lot=1047370100,
    )
    CommonFunc_90005391(
        0,
        flag=1047370350,
        flag_1=1047372350,
        character=Characters.WanderingNoble,
        character_1=Characters.Troll,
        left=1,
    )
    CommonFunc_90005251(0, character=Characters.WanderingNoble, radius=10.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1047372200)
def Event_1047372200(_, flag: uint, flag_1: uint, anchor_entity: uint, character: uint, left: int, item_lot: int):
    """Event 1047372200"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(6.0)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if ValueNotEqual(left=item_lot, right=0):
        AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)
