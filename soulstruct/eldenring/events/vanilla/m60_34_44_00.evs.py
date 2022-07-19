"""
West Liurnia (SE) (SW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_34_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034440000, asset=Assets.AEG099_060_9000)
    RunCommonEvent(1034442200)
    CommonFunc_90005300(0, flag=1034440220, character=Characters.Scarab, item_lot_param_id=40218, seconds=0.0, left=0)
    Event_1034440700(0, 1034440700, 930023, 3409)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_90005261(
        0,
        character=Characters.Albinauric0,
        region=1034442200,
        radius=3.0,
        seconds=2.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric0,
        animation_id=30002,
        animation_id_1=20002,
        region=1034442200,
        radius=3.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric1,
        animation_id=30002,
        animation_id_1=20002,
        region=1034442200,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Albinauric2,
        region=1034442200,
        radius=3.0,
        seconds=1.0,
        animation_id=-1,
    )
    CommonFunc_90005211(0, 1034440202, 30002, 20002, 1034442200, 3.0, 1.0, 0, 0, 0, 0)


@RestartOnRest(1034440700)
def Event_1034440700(_, character: uint, animation_id: int, flag: uint):
    """Event 1034440700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    DisableGravity(character)
    ForceAnimation(character, animation_id)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@RestartOnRest(1034442200)
def Event_1034442200():
    """Event 1034442200"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=1034442200))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1034442200, unk_8_12=1)
    End()
