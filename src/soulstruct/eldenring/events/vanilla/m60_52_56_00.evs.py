"""
Northeast Mountaintops (SW) (SW)

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
from .enums.m60_52_56_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052560000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76520,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=5,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    CommonFunc_90005860(
        0,
        flag=1052560800,
        left=0,
        character=Characters.ErdtreeAvatar0,
        left_1=0,
        item_lot=30525,
        seconds=0.0,
    )
    Event_1052562815(0, character=Characters.ErdtreeAvatar0, name=904810601, npc_threat_level=18)
    CommonFunc_90005872(0, character=Characters.ErdtreeAvatar0, npc_threat_level=18, right=0)
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeAvatar0,
        animation_id=30000,
        animation_id_1=20000,
        region=1052562800,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Scarab1,
        animation_id=30001,
        animation_id_1=20001,
        region=0,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1052562820()
    Event_1052562821()
    Event_1052562830(
        0,
        character=Characters.ErdtreeAvatar1,
        animation_id=30001,
        animation_id_1=20020,
        region=0,
        seconds=0.0,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy1, flag=1052562700)


@ContinueOnRest(1052562815)
def Event_1052562815(_, character: Character | int, name: NPCName | int, npc_threat_level: uint):
    """Event 1052562815"""
    DisableNetworkSync()
    OR_15.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_15.Add(HasAIStatus(Characters.ErdtreeAvatar1, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_15)
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(Characters.ErdtreeAvatar3, name=name)
    OR_14.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_14.Add(HasAIStatus(Characters.ErdtreeAvatar1, ai_status=AIStatusType.Battle))
    AND_2.Add(OR_14)
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(Characters.ErdtreeAvatar3, name=name)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(Characters.ErdtreeAvatar3, name=name, bar_slot=1)
    OR_11.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_11.Add(HasAIStatus(Characters.ErdtreeAvatar1, ai_status=AIStatusType.Battle))
    AND_12.Add(OR_11)
    AND_12.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_12.Add(not AND_12)
    OR_12.Add(CharacterDead(character))
    OR_12.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_12)
    
    OR_13.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(Characters.ErdtreeAvatar3, name=name, bar_slot=1)
    DisableFlag(9291)
    Restart()


@RestartOnRest(1052562820)
def Event_1052562820():
    """Event 1052562820"""
    AddSpecialEffect(Characters.ErdtreeAvatar0, 17320)
    AddSpecialEffect(Characters.ErdtreeAvatar1, 17321)
    AddSpecialEffect(Characters.ErdtreeAvatar2, 17322)
    DisableHealthBar(Characters.ErdtreeAvatar0)
    DisableHealthBar(Characters.ErdtreeAvatar1)
    DisableHealthBar(Characters.ErdtreeAvatar2)
    DisableHealthBar(Characters.ErdtreeAvatar3)
    DisableGravity(Characters.ErdtreeAvatar3)
    DisableAnimations(Characters.ErdtreeAvatar3)
    ReferDamageToEntity(Characters.ErdtreeAvatar0, target_entity=Characters.ErdtreeAvatar3)
    ReferDamageToEntity(Characters.ErdtreeAvatar1, target_entity=Characters.ErdtreeAvatar3)
    ReferDamageToEntity(Characters.ErdtreeAvatar2, target_entity=Characters.ErdtreeAvatar3)


@RestartOnRest(1052562821)
def Event_1052562821():
    """Event 1052562821"""
    GotoIfFlagDisabled(Label.L0, flag=1052560800)
    DisableAnimations(Characters.ErdtreeAvatar0)
    DisableAnimations(Characters.ErdtreeAvatar1)
    DisableAnimations(Characters.ErdtreeAvatar2)
    DisableAnimations(Characters.ErdtreeAvatar3)
    Kill(Characters.ErdtreeAvatar0)
    Kill(Characters.ErdtreeAvatar1)
    Kill(Characters.ErdtreeAvatar2)
    Kill(Characters.ErdtreeAvatar3)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(HealthValue(Characters.ErdtreeAvatar0) == 0)
    OR_1.Add(HealthValue(Characters.ErdtreeAvatar1) == 0)
    OR_1.Add(HealthValue(Characters.ErdtreeAvatar2) == 0)
    OR_1.Add(HealthValue(Characters.ErdtreeAvatar3) == 0)
    
    MAIN.Await(OR_1)
    
    Kill(Characters.ErdtreeAvatar0)
    Kill(Characters.ErdtreeAvatar1)
    Kill(Characters.ErdtreeAvatar2)
    Kill(Characters.ErdtreeAvatar3)


@RestartOnRest(1052562830)
def Event_1052562830(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    seconds_1: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1052562830"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(CharacterHasSpecialEffect(Characters.ErdtreeAvatar0, 17325))
    OR_3.Add(CharacterHasSpecialEffect(Characters.ErdtreeAvatar1, 17326))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    Wait(seconds_1)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    EnableAI(character)
    Move(
        character,
        destination=Characters.ErdtreeAvatar0,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=Characters.ErdtreeAvatar0,
    )
    ForceAnimation(character, animation_id_1, loop=True)
    Wait(5.0)
    AddSpecialEffect(Characters.ErdtreeAvatar0, 17327)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    Wait(5.0)
    AddSpecialEffect(Characters.ErdtreeAvatar0, 17327)
    End()
    Wait(seconds)
