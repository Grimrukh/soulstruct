"""
West Weeping Peninsula (SW) (NE)

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
from .entities.m60_41_33_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1041330000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005251(0, 1041330233, 8.0, 1.0, -1)
    CommonFunc_90005251(0, 1041330234, 8.0, 0.5, -1)
    CommonFunc_90005251(0, 1041330235, 8.0, 1.100000023841858, -1)
    CommonFunc_90005251(0, 1041330236, 8.0, 0.0, -1)
    CommonFunc_90005251(0, 1041330237, 8.0, 0.5, -1)
    CommonFunc_90005251(0, 1041330238, 8.0, 0.0, -1)
    CommonFunc_90005251(0, 1041330239, 8.0, 1.0, -1)
    CommonFunc_90005251(0, 1041330240, 8.0, 0.0, -1)
    CommonFunc_90005251(0, 1041330241, 8.0, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.GravenSchool,
        animation_id=30000,
        animation_id_1=20000,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005920(0, flag=1041330900, asset=1041331900, obj_act_id=1041333900)
    CommonFunc_90005703(0, 1041330700, 3461, 3462, 1044369204, 3461, 3460, 3464, -1)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SorceressSellen0,
        flag=3461,
        flag_1=3460,
        flag_2=1044369204,
        right=3,
    )
    Event_1041333700(0, character=Characters.SorceressSellen0, character_1=Characters.SorceressSellen1)
    CommonFunc_90005740(
        0,
        1044362702,
        1044362703,
        1044362704,
        1041330700,
        704,
        1041331700,
        704,
        0.20000000298023224,
        90204,
        -1,
        -1,
        1.2000000476837158,
    )
    CommonFunc_90005741(0, 1044362708, 1044362709, 1044362704, 1041330700, 90201, 0, -1, -1, 0.5)
    Event_1041333705(0, character=Characters.WitchHunterJerren)
    CommonFunc_90005703(0, 1041330710, 3361, 3362, 1041339251, 3361, 3360, 3363, -1)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.WitchHunterJerren,
        flag=3361,
        flag_1=3360,
        flag_2=1041339251,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.WitchHunterJerren, flag=3363, first_flag=3360, last_flag=3363)
    CommonFunc_90005706(0, 1041330720, 930023, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SorceressSellen0)
    DisableBackread(Characters.SorceressSellen1)
    DisableBackread(Characters.WitchHunterJerren)
    DisableBackread(Characters.WanderingNoble)


@RestartOnRest(1041332800)
def Event_1041332800():
    """Event 1041332800"""
    if FlagEnabled(1041330800):
        return
    
    MAIN.Await(HealthValue(1041330800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(1041330800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(1041330800))
    
    KillBossAndDisplayBanner(character=1041330800, banner_type=BannerType.GreatEnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_1003, obj_act_id=-1)
    EnableFlag(1041330800)


@RestartOnRest(1041332810)
def Event_1041332810():
    """Event 1041332810"""
    GotoIfFlagDisabled(Label.L0, flag=1041330800)
    DisableCharacter(1041330800)
    DisableAnimations(1041330800)
    Kill(1041330800)
    EnableAssetActivation(Assets.AEG004_970_1003, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1041330800)
    AND_2.Add(FlagEnabled(1041332805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1041332800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1041330800)
    SetNetworkUpdateRate(1041330800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1041330800, name=904133540)
    DisableAssetActivation(Assets.AEG004_970_1003, obj_act_id=-1)


@RestartOnRest(1041332849)
def Event_1041332849():
    """Event 1041332849"""
    CommonFunc_9005800(
        0,
        flag=1041330800,
        entity=1041331800,
        region=1041332800,
        flag_1=1041332805,
        character=1041335800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1041330800,
        entity=1041331800,
        region=1041332800,
        flag_1=1041332805,
        flag_2=1041332806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1041330800, asset=1041331800, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1041330800,
        bgm_boss_conv_param_id=0,
        flag_1=1041332805,
        flag_2=1041332806,
        right=0,
        flag_3=1041332802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, 1041330800, 1041331801, 3, 0, 0)


@RestartOnRest(1041333700)
def Event_1041333700(_, character: uint, character_1: uint):
    """Event 1041333700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3460):
        DisableFlag(1034509253)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3465))
    OR_1.Add(FlagEnabled(3466))
    OR_1.Add(FlagEnabled(3467))
    OR_1.Add(FlagEnabled(3468))
    OR_1.Add(FlagEnabled(3469))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(Assets.AEG099_413_9000)
    OR_2.Add(FlagEnabled(3465))
    OR_2.Add(FlagEnabled(3466))
    OR_2.Add(FlagEnabled(3467))
    OR_2.Add(FlagEnabled(3468))
    OR_2.Add(FlagEnabled(3469))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L4, flag=1041339259)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    DisableAsset(Assets.AEG099_413_9000)
    ForceAnimation(character, 90101)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableAsset(Assets.AEG099_413_9000)
    ForceAnimation(character, 90101)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 90102)
    if FlagDisabled(1041339259):
        DisableAsset(Assets.AEG099_413_9000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3465))
    AND_15.Add(FlagDisabled(3466))
    AND_15.Add(FlagDisabled(3467))
    AND_15.Add(FlagDisabled(3468))
    AND_15.Add(FlagDisabled(3469))
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1041333705)
def Event_1041333705(_, character: uint):
    """Event 1041333705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3360):
        DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3369)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3369))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
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
    
    MAIN.Await(FlagDisabled(3369))
    
    Restart()
