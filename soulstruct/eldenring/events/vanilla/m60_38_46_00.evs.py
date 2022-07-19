"""
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
from .entities.m60_38_46_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038460000, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005511(0, flag=1038460560, asset=1038461550, obj_act_id=1038463560, obj_act_id_1=257018, left=0)
    CommonFunc_90005512(0, flag=1038460560, region=1038462550, region_1=1038462551)
    CommonFunc_90005640(0, flag=1038460540, asset=Assets.AEG239_001_2000)
    Event_1038462200(0, character=Characters.Commoner0)
    Event_1038462200(1, character=Characters.Commoner1)
    Event_1038462200(2, character=Characters.ThornSorcerer)
    CommonFunc_90005300(
        0,
        flag=1038460340,
        character=Characters.GuardianGolem,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    Event_1038460510()
    CommonFunc_90005501(0, 1038460650, 1038460651, 0, 1038461650, 1038461651, 1038461652, 1038460652)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1038460519()
    Event_1038462340()


@RestartOnRest(1038462200)
def Event_1038462200(_, character: uint):
    """Event 1038462200"""
    Kill(character)


@RestartOnRest(1038462210)
def Event_1038462210(_, character: uint):
    """Event 1038462210"""
    DisableCharacter(character)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1038462210))
    
    CreateAssetVFX(1038461210, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    Wait(2.0)
    DeleteAssetVFX(1038461210)
    ForceAnimation(character, 20001, wait_for_completion=True)
    End()


@RestartOnRest(1038462340)
def Event_1038462340():
    """Event 1038462340"""
    if FlagEnabled(1038460340):
        return
    DisableHealthBar(Characters.GuardianGolem)
    AddSpecialEffect(Characters.GuardianGolem, 12189)
    Wait(3.0)
    RemoveSpecialEffect(Characters.GuardianGolem, 12189)
    EnableHealthBar(Characters.GuardianGolem)


@NeverRestart(1038460510)
def Event_1038460510():
    """Event 1038460510"""
    CommonFunc_90005500(
        0,
        1038460650,
        1038460651,
        0,
        1038461650,
        1038461651,
        1038463651,
        1038461652,
        1038463652,
        1038462651,
        1038462652,
        1038460652,
        1038462653,
        0,
    )


@NeverRestart(1038460519)
def Event_1038460519():
    """Event 1038460519"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(OutsideMap(game_map=AINSEL_RIVER))
    
    EnableFlag(1038460650)
