"""
North Altus Plateau (SE) (SE)

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
from .enums.m60_43_52_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1043522500(
        0,
        character=Characters.Commoner,
        character_1=Characters.Margit,
        flag=1043520505,
        region=1043522500,
        flag_1=1043522500,
    )
    Event_1043522505(
        0,
        flag=1043520505,
        character=Characters.Commoner,
        character_1=Characters.Margit,
        flag_1=1043522500,
    )
    Event_1043522510()
    Event_1043522515()
    CommonFunc_90005300(0, flag=1043520506, character=Characters.Margit, item_lot=1043520500, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1043520400, character=Characters.Scarab, item_lot=40316, seconds=0.0, left=0)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61032)
    CommonFunc_90005705(0, character=Characters.FingerReader)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043520705)
    DisableBackread(Characters.FingerReader)


@RestartOnRest(1043522500)
def Event_1043522500(_, character: uint, character_1: uint, flag: Flag | int, region: Region | int, flag_1: Flag | int):
    """Event 1043522500"""
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    if FlagEnabled(flag):
        return
    ForceAnimation(character, 30029, loop=True, skip_transition=True)
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.5)
    AND_15.Add(HealthValue(character) == 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_15)
    EnableAI(character)
    ForceAnimation(character, 20030, loop=True, skip_transition=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    AddSpecialEffect(character, 9730)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=636615, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    ForceAnimation(character, 20030, skip_transition=True)
    Move(character_1, destination=character, destination_type=CoordEntityType.Character, dummy_id=900, short_move=True)
    Wait(1.0)
    ForceAnimation(character, 20030, skip_transition=True)
    Wait(1.0)
    ForceAnimation(character, 20030, skip_transition=True)
    Wait(1.0)
    EnableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(1043522506)
    End()


@RestartOnRest(1043522505)
def Event_1043522505(_, flag: Flag | int, character: uint, character_1: uint, flag_1: Flag | int):
    """Event 1043522505"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(1043522700))
    AND_1.Add(FlagDisabled(1043522506))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableGravity(character_1)
    AddSpecialEffect(character_1, 9732)
    Kill(character)
    DisableGravity(character)
    DisableCharacter(character)
    DisableAI(character)
    Wait(0.4000000059604645)
    EnableAI(character_1)
    EnableAnimations(character_1)
    
    MAIN.Await(CharacterDead(character_1))
    
    Move(character, destination=character_1, destination_type=CoordEntityType.Character, dummy_id=900, short_move=True)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableGravity(character)
    EnableFlag(flag)
    End()


@RestartOnRest(1043522510)
def Event_1043522510():
    """Event 1043522510"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(1043522700))
    
    EnableNetworkFlag(1043522700)
    
    MAIN.Await(FlagDisabled(1043522700))
    
    DisableNetworkFlag(1043522700)
    End()


@RestartOnRest(1043522515)
def Event_1043522515():
    """Event 1043522515"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043520505):
        return
    SetCharacterTalkRange(character=Characters.Commoner, distance=150.0)
    SetCharacterTalkRange(character=Characters.Margit, distance=150.0)
    AwaitFlagEnabled(flag=1043520505)
    SetCharacterTalkRange(character=Characters.Commoner, distance=17.0)
    SetCharacterTalkRange(character=Characters.Margit, distance=17.0)
    End()
