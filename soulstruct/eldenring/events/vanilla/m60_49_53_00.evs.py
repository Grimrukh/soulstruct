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
from .entities.m60_49_53_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049530000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76501,
        asset=Assets.AEG099_090_9004,
        source_flag=77500,
        value=1,
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
    RegisterGrace(grace_flag=1049530001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005261(0, character=Characters.Springhare0, region=1049532260, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare1, region=1049532261, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare2, region=1049532262, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare3, region=1049532263, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_900005610(0, asset=1049531600, vfx_id=100, model_point=800, right=0)
    Event_1049532200(0, character=1049535200)
    CommonFunc_90005704(0, attacked_entity=Characters.Shabriri, flag=3621, flag_1=3620, flag_2=1049539201, right=3)
    CommonFunc_90005703(0, 1049530700, 3621, 3622, 1049539201, 3621, 3620, 3624, -1)
    CommonFunc_90005702(0, character=Characters.Shabriri, flag=3623, first_flag=3620, last_flag=3624)
    Event_1049533700(0, character=Characters.Shabriri)
    Event_1049533701()
    Event_1049533702()
    Event_1049533703(0, character=Characters.Shabriri)
    CommonFunc_90005705(0, character=Characters.FingerReader)
    Event_1049533705()
    Event_1049533710(0, 1049532710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Shabriri)
    DisableBackread(Characters.FingerReader)


@RestartOnRest(1049532200)
def Event_1049532200(_, character: uint):
    """Event 1049532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1049533700)
def Event_1049533700(_, character: uint):
    """Event 1049533700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3620):
        DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3631)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3631))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3631))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1049533701)
def Event_1049533701():
    """Event 1049533701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1049539210):
        return
    EnableFlag(1049539210)
    if FlagEnabled(3621):
        DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
        EnableNetworkFlag(3620)
    OR_1.Add(FlagEnabled(1043359259))
    OR_1.Add(FlagEnabled(1044389209))
    OR_1.Add(FlagEnabled(1035469209))
    OR_1.Add(FlagEnabled(1039529209))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    if FlagEnabled(3626):
        EnableFlag(1043359259)
        Goto(Label.L1)
    if FlagEnabled(3625):
        EnableFlag(1044389209)
        Goto(Label.L1)
    if FlagEnabled(3627):
        EnableFlag(1035469209)
        Goto(Label.L1)
    if FlagEnabled(3630):
        EnableFlag(1039529209)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    EnableFlag(3638)
    End()


@RestartOnRest(1049533702)
def Event_1049533702():
    """Event 1049533702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3623))
    AND_1.Add(FlagEnabled(3631))
    if AND_1:
        return
    
    MAIN.Await(FlagEnabled(3631))
    
    if FlagDisabled(35000500):
        return
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()


@RestartOnRest(1049533703)
def Event_1049533703(_, character: uint):
    """Event 1049533703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3623):
        return
    AND_1.Add(CharacterDead(character))
    AND_1.Add(FlagDisabled(3623))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1049539212)
    SetBackreadStateAlternate(character, True)
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(character, 9600))
    OR_1.Add(TimeElapsed(seconds=60.0))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(1049533705)
def Event_1049533705():
    """Event 1049533705"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109561):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1049532500))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109561)
    End()


@RestartOnRest(1049533710)
def Event_1049533710(_, flag: uint):
    """Event 1049533710"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    DisableFlag(flag)
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(not OR_2)
    
    Restart()
