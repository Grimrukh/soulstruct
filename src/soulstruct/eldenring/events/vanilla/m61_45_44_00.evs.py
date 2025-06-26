"""
Land of Shadow 11-11 SW SE

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
    Event_2045442811(
        0,
        character=2045440800,
        animation_id=30002,
        animation_id_1=20002,
        flag=2045440820,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=2045440800, name=905860600, npc_threat_level=22)
    CommonFunc_90005860(0, flag=2045440800, left=0, character=2045440800, left_1=1, item_lot=30860, seconds=0.0)
    Event_2045442812()
    CommonFunc_90005200(
        0,
        character=2045440200,
        animation_id=30001,
        animation_id_1=20001,
        region=2045442200,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2045440201,
        animation_id=30001,
        animation_id_1=20001,
        region=2045442200,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2045440202,
        animation_id=30001,
        animation_id_1=20001,
        region=2045442200,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(2045442810)
def Event_2045442810(_, character: Character | int, name: NPCName | int, npc_threat_level: uint):
    """Event 2045442810"""
    DisableNetworkSync()
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=224, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=225, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=226, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
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
    DisableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=224, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=225, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=226, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_12.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
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
    DisableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9291)
    Restart()


@RestartOnRest(2045442811)
def Event_2045442811(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    flag: Flag | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 2045442811"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if FlagEnabled(flag):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    SetLockOnPoint(character=character, lock_on_dummy_id=224, state=False)
    SetLockOnPoint(character=character, lock_on_dummy_id=225, state=False)
    SetLockOnPoint(character=character, lock_on_dummy_id=226, state=False)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableNetworkFlag(flag)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=224, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=225, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=226, state=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@ContinueOnRest(2045442812)
def Event_2045442812():
    """Event 2045442812"""
    if FlagEnabled(2045440820):
        return
    AddSpecialEffect(2045440100, 9531)
    AwaitFlagEnabled(flag=2045440820)
    AddSpecialEffect(2045440100, 9532)
