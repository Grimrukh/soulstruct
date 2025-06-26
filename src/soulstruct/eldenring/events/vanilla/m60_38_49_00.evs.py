"""
Liurnia to Altus Plateau (SE) (NW)

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
from .enums.m60_38_49_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1038492300()
    Event_1038492301()
    Event_1038492306()
    Event_1038492400()
    Event_1038492401()
    Event_1038492304()
    Event_1038492320()
    Event_1038492580()
    CommonFunc_90005250(0, character=Characters.Rat0, region=1038492302, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat1, region=1038492313, seconds=0.0, animation_id=-1)
    CommonFunc_90005706(0, character=Characters.Commoner0, animation_id=930018, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner0)
    Event_1038492310(0, character=Characters.BulletDummy)
    Event_1038492305()


@RestartOnRest(1038492300)
def Event_1038492300():
    """Event 1038492300"""
    GotoIfFlagEnabled(Label.L3, flag=1038490201)
    GotoIfFlagEnabled(Label.L0, flag=1038492207)
    GotoIfFlagEnabled(Label.L0, flag=1038492208)
    GotoIfFlagDisabled(Label.L1, flag=1038492207)
    GotoIfFlagDisabled(Label.L1, flag=1038492208)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(1038492212)
    if FlagEnabled(1038492210):
        DisableCharacter(Characters.BulletDummy)
    SetNetworkUpdateRate(Characters.BulletDummy, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    if FlagDisabled(1038492210):
        EnableCharacter(Characters.BulletDummy)
        SetNetworkUpdateRate(Characters.BulletDummy, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(1038492212)
    if FlagDisabled(1038492209):
        CreateAssetVFX(Assets.AEG099_090_9000, dummy_id=100, vfx_id=806740)
        EnableFlag(1038492209)
    OR_1.Add(FlagDisabled(1038492207))
    OR_1.Add(FlagDisabled(1038492208))
    AND_1.Add(FlagDisabled(1038492210))
    AND_1.Add(FlagDisabled(1038492212))
    OR_1.Add(AND_1)
    AND_2.Add(FlagEnabled(1038492210))
    AND_2.Add(FlagEnabled(1038492212))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(Characters.BulletDummy)
    SetNetworkUpdateRate(Characters.BulletDummy, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    DisableFlag(1038492209)
    OR_2.Add(FlagEnabled(1038492207))
    OR_2.Add(FlagEnabled(1038492208))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(Characters.BulletDummy)
    SetNetworkUpdateRate(Characters.BulletDummy, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    DisableNetworkFlag(1038492207)
    DisableNetworkFlag(1038492208)


@RestartOnRest(1038492301)
def Event_1038492301():
    """Event 1038492301"""
    EnableNetworkSync()
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_2.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown7))
    if OR_2:
        return
    if FlagEnabled(1038490201):
        return
    OR_1.Add(FlagDisabled(1038492206))
    OR_1.Add(EntityBeyondDistance(entity=Characters.BulletDummy, other_entity=PLAYER, radius=150.0))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_1.Add(FlagEnabled(1038492206))
    AND_1.Add(EntityWithinDistance(entity=Characters.BulletDummy, other_entity=PLAYER, radius=150.0))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Wait(1.0)
    
    MAIN.Await(FlagDisabled(1038492206))
    
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableNetworkFlag(1038492207)
    if PlayerNotInOwnWorld():
        DisableNetworkFlag(1038492208)
    Wait(1.0)
    
    MAIN.Await(FlagEnabled(1038492206))
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(1038492207)
    if PlayerNotInOwnWorld():
        EnableNetworkFlag(1038492208)
    
    MAIN.Await(FlagDisabled(1038492206))
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1038492304)
def Event_1038492304():
    """Event 1038492304"""
    EnableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=1038490201)
    DisableCharacter(Characters.Commoner1)
    DisableAnimations(Characters.Commoner1)
    Kill(Characters.Commoner1)
    DisableCharacter(Characters.Commoner2)
    DisableAnimations(Characters.Commoner2)
    Kill(Characters.Commoner2)
    DisableCharacter(Characters.Commoner3)
    DisableAnimations(Characters.Commoner3)
    Kill(Characters.Commoner3)
    DisableCharacter(Characters.Commoner4)
    DisableAnimations(Characters.Commoner4)
    Kill(Characters.Commoner4)
    DisableCharacter(Characters.Commoner5)
    DisableAnimations(Characters.Commoner5)
    Kill(Characters.Commoner5)
    DisableCharacter(Characters.Commoner6)
    DisableAnimations(Characters.Commoner6)
    Kill(Characters.Commoner6)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1038490201):
        return
    AND_1.Add(CharacterDead(Characters.Commoner1))
    AND_1.Add(CharacterDead(Characters.Commoner2))
    AND_1.Add(CharacterDead(Characters.Commoner3))
    AND_1.Add(CharacterDead(Characters.Commoner4))
    AND_1.Add(CharacterDead(Characters.Commoner5))
    AND_1.Add(CharacterDead(Characters.Commoner6))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1038490201)


@RestartOnRest(1038492305)
def Event_1038492305():
    """Event 1038492305"""
    if FlagEnabled(1038490201):
        return
    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(1038492206)
    DisableNetworkFlag(1038492207)
    DisableNetworkFlag(1038492208)
    DisableNetworkFlag(1038492209)
    DisableNetworkFlag(1038492210)
    DisableNetworkFlag(1038492211)


@RestartOnRest(1038492306)
def Event_1038492306():
    """Event 1038492306"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if FlagEnabled(1038490201):
        return
    Wait(7.0)
    DisableNetworkFlag(1038492206)
    DisableNetworkFlag(1038492208)
    Wait(5.0)
    EnableNetworkFlag(1038492206)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1038492310)
def Event_1038492310(_, character: Character | int):
    """Event 1038492310"""
    DisableNetworkSync()
    if FlagEnabled(1038490201):
        return
    SetBackreadStateAlternate(character, True)
    DisableGravity(character)


@RestartOnRest(1038492320)
def Event_1038492320():
    """Event 1038492320"""
    AND_1.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_1)
    AddSpecialEffect(Characters.BulletDummy, 16630)
    End()
    AND_2.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_2)
    AddSpecialEffect(Characters.BulletDummy, 16631)
    End()
    AND_3.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_3)
    AddSpecialEffect(Characters.BulletDummy, 16632)
    End()
    AND_4.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_4)
    AddSpecialEffect(Characters.BulletDummy, 16633)
    End()
    AND_5.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_5)
    AddSpecialEffect(Characters.BulletDummy, 16634)
    End()
    AND_6.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_6)
    AddSpecialEffect(Characters.BulletDummy, 16635)
    End()
    AND_7.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_7)
    AddSpecialEffect(Characters.BulletDummy, 16636)
    End()
    AND_8.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_8)
    AddSpecialEffect(Characters.BulletDummy, 16637)
    End()


@RestartOnRest(1038492400)
def Event_1038492400():
    """Event 1038492400"""
    DisableNetworkSync()
    if FlagEnabled(1038490201):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1038492300))
    
    EnableFlag(1038492210)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1038492300))
    
    DisableFlag(1038492210)
    Restart()


@RestartOnRest(1038492401)
def Event_1038492401():
    """Event 1038492401"""
    DisableNetworkSync()
    if FlagEnabled(1038490201):
        return
    if PlayerInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1038492300))
    
    EnableFlag(1038492210)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1038492300))
    
    DisableFlag(1038492210)
    Restart()


@ContinueOnRest(1038492580)
def Event_1038492580():
    """Event 1038492580"""
    RegisterLadder(start_climbing_flag=1038490580, stop_climbing_flag=1038490581, asset=Assets.AEG110_012_1003)
    RegisterLadder(start_climbing_flag=1038490582, stop_climbing_flag=1038490583, asset=Assets.AEG110_012_1004)
    RegisterLadder(start_climbing_flag=1038490584, stop_climbing_flag=1038490585, asset=Assets.AEG110_012_1005)
