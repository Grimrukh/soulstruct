"""
Northwest Mountaintops (SE) (SE)

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
from .entities.m60_51_56_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1051560000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76503,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=2,
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
    CommonFunc_90005300(0, flag=1051560210, character=Characters.LargeScarab, item_lot=1051560700, seconds=0.0, left=0)
    Event_1051562200(0, character=1051565200)
    Event_1051562500()
    Event_1051562510()
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SpiritJellyfish,
        flag=3841,
        flag_1=3840,
        flag_2=1051569201,
        right=1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SpiritJellyfish,
        flag=3841,
        flag_1=3842,
        flag_2=1051569201,
        flag_3=3841,
        first_flag=3840,
        last_flag=3844,
        right=-1,
    )
    Event_1051563700(0, character=Characters.SpiritJellyfish)
    Event_1051563701(0, character=Characters.SpiritJellyfish, radius=7.0)
    Event_1051563702(0, seconds=10.0, seconds_1=12.0, seconds_2=20.0, flag=1051569206)
    Event_1051563703(0, entity=Assets.AEG099_090_9001)
    Event_1051563704(0, character=Characters.SpiritJellyfish)
    Event_1051563710(0, character=Characters.Millicent)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent, flag=4181, flag_1=4180, flag_2=1051569251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent,
        flag=4181,
        flag_1=4182,
        flag_2=1051569251,
        flag_3=4181,
        first_flag=4180,
        last_flag=4182,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent, flag=4183, first_flag=4180, last_flag=4184)
    Event_1051563715(0, character=Characters.BrotherCorhyn)
    CommonFunc_90005704(0, attacked_entity=Characters.BrotherCorhyn, flag=4201, flag_1=4200, flag_2=1040529251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.BrotherCorhyn,
        flag=4201,
        flag_1=4202,
        flag_2=1040529251,
        flag_3=4201,
        first_flag=4200,
        last_flag=4203,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.BrotherCorhyn, flag=4203, first_flag=4200, last_flag=4204)
    Event_1051563716(0, character=Characters.Goldmask)
    Event_1051563717(0, character=Characters.Goldmask)
    Event_1051563720(0, character=Characters.TalkDummy1, region=1051562700, distance=155.0)
    CommonFunc_90005725(
        0,
        flag=4795,
        flag_1=4796,
        flag_2=4798,
        flag_3=1051569405,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1051566700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4796,
        flag_1=4797,
        flag_2=1051569406,
        flag_3=4796,
        first_flag=4795,
        last_flag=4799,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4796, flag_1=4795, flag_2=1051569406, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4798, first_flag=4795, last_flag=4799)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4796,
        flag_1=4797,
        flag_2=1051569407,
        flag_3=4796,
        first_flag=4795,
        last_flag=4799,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4796, flag_1=4795, flag_2=1051569407, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1051562746, flag_1=1051562747)
    CommonFunc_90005727(
        0,
        flag=4796,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4795,
        last_flag=4798,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SpiritJellyfish)
    DisableBackread(Characters.Millicent)
    DisableBackread(Characters.Goldmask)
    DisableBackread(Characters.TalkDummy1)
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1051562200)
def Event_1051562200(_, character: uint):
    """Event 1051562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1051562500)
def Event_1051562500():
    """Event 1051562500"""
    GotoIfFlagEnabled(Label.L0, flag=1051569206)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    CreateAssetVFX(Assets.AEG099_251_9000, vfx_id=200, model_point=1520)
    AwaitFlagEnabled(flag=1051569206)
    DisplayDialog(text=30030, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG099_251_9000)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    PlaySoundEffect(Assets.AEG099_251_9000, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1051562510)
def Event_1051562510():
    """Event 1051562510"""
    DisableNetworkSync()
    if FlagEnabled(1051569206):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=Assets.AEG099_251_9000))
    OR_1.Add(FlagEnabled(1051569206))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1051569206):
        return
    DisplayDialog(text=30031, anchor_entity=Assets.AEG099_251_9000)
    Wait(1.0)
    Restart()


@RestartOnRest(1051563700)
def Event_1051563700(_, character: uint):
    """Event 1051563700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3840):
        DisableFlag(1051569204)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3845)
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    OR_3.Add(FlagEnabled(3845))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3840)
    GotoIfFlagEnabled(Label.L2, flag=3841)
    GotoIfFlagEnabled(Label.L3, flag=3842)
    GotoIfFlagEnabled(Label.L4, flag=3843)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930000)
    SetCharacterTalkRange(character=character, distance=30.0)
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
    OR_4.Add(FlagEnabled(3845))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1051563701)
def Event_1051563701(_, character: uint, radius: float):
    """Event 1051563701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1051569206):
        return
    OR_1.Add(CharacterHasSpecialEffect(35000, 14200))
    OR_1.Add(CharacterHasSpecialEffect(35000, 14201))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(35000, 297000))
    AND_1.Add(FlagDisabled(3841))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=35000, radius=radius))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1051562708)
    DisableAnimations(character)
    EnableImmortality(character)
    
    MAIN.Await(FlagEnabled(1051562709))
    
    ForceAnimation(character, 20002)
    AddSpecialEffect(PLAYER, 9560)
    AddSpecialEffect(PLAYER, 236000)
    Wait(2.0)
    EnableFlag(1051569206)
    if FlagDisabled(60829):
        EnableFlag(60829)
        AwardGesture(gesture_param_id=72)
    Wait(8.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1051563702)
def Event_1051563702(_, seconds: float, seconds_1: float, seconds_2: float, flag: uint):
    """Event 1051563702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    EnableFlag(1051562702)
    
    MAIN.Await(FlagEnabled(1051562703))
    
    Wait(seconds)
    if FlagEnabled(flag):
        return
    EnableFlag(1051562704)
    
    MAIN.Await(FlagEnabled(1051562705))
    
    Wait(seconds_1)
    if FlagEnabled(flag):
        return
    EnableFlag(1051562706)
    
    MAIN.Await(FlagEnabled(1051562707))
    
    Wait(seconds_2)
    if FlagEnabled(flag):
        return
    DisableFlag(1051562702)
    DisableFlag(1051562703)
    DisableFlag(1051562704)
    DisableFlag(1051562705)
    DisableFlag(1051562706)
    DisableFlag(1051562707)
    Restart()


@RestartOnRest(1051563703)
def Event_1051563703(_, entity: uint):
    """Event 1051563703"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6590, entity=entity))
    
    DisplayDialog(text=30090, anchor_entity=0, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()


@RestartOnRest(1051563704)
def Event_1051563704(_, character: uint):
    """Event 1051563704"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkConnectedFlagRange(flag_range=(3840, 3844))
    EnableNetworkFlag(3840)
    SaveRequest()
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    AND_1.Add(FlagDisabled(3840))
    AND_2.Add(FlagEnabled(1051569206))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    AND_6.Add(CharacterHasSpecialEffect(character, 14200))
    AND_7.Add(TimeElapsed(seconds=10.0))
    OR_6.Add(AND_6)
    OR_6.Add(AND_7)
    
    MAIN.Await(OR_6)
    
    RestartIfFinishedConditionTrue(input_condition=AND_7)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 14201))
    
    Restart()


@RestartOnRest(1051563710)
def Event_1051563710(_, character: uint):
    """Event 1051563710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4189)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4189))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(4189))
    
    Restart()


@RestartOnRest(1051563715)
def Event_1051563715(_, character: uint):
    """Event 1051563715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4200):
        DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4209))
    OR_1.Add(FlagEnabled(4211))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(4209))
    OR_2.Add(FlagEnabled(4211))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90102)
    if FlagEnabled(4211):
        Move(character, destination=1051562710, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
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
    OR_15.Add(FlagEnabled(4209))
    OR_15.Add(FlagEnabled(4211))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1051563716)
def Event_1051563716(_, character: uint):
    """Event 1051563716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4209))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(4203))
    AND_2.Add(FlagDisabled(4217))
    AND_2.Add(FlagEnabled(4203))
    AND_2.Add(FlagEnabled(11009555))
    AND_2.Add(FlagDisabled(11059304))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930009)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    EnableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagEnabled(4209))
    AND_10.Add(OR_10)
    AND_10.Add(FlagDisabled(4203))
    AND_11.Add(FlagDisabled(4217))
    AND_11.Add(FlagEnabled(4203))
    AND_11.Add(FlagEnabled(11009555))
    AND_11.Add(FlagDisabled(11059304))
    OR_11.Add(AND_10)
    OR_11.Add(AND_11)
    
    MAIN.Await(not OR_11)
    
    Restart()


@RestartOnRest(1051563717)
def Event_1051563717(_, character: uint):
    """Event 1051563717"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    EnableNetworkFlag(1040542710)
    ForceAnimation(character, 20014, wait_for_completion=True, skip_transition=True)
    End()


@RestartOnRest(1051563720)
def Event_1051563720(_, character: uint, region: uint, distance: float):
    """Event 1051563720"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1051569301):
        return
    if FlagEnabled(1047589205):
        return
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    if FlagDisabled(1051562720):
        DisableFlag(1051569300)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(1051569300)
    Wait(30.0)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()
