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
from .entities.m31_03_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=310300, asset=Assets.AEG099_060_9000)
    Event_31032800()
    Event_31032810()
    Event_31032811()
    Event_31032849()
    CommonFunc_90005646(0, 31030800, 31032840, 31032841, 31031840, 31032840, 31, 3, 0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Wolf2, region=31032202, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Wolf3,
        animation_id=30000,
        animation_id_1=20000,
        region=31032210,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf4,
        animation_id=30005,
        animation_id_1=20005,
        region=31032210,
        radius=8.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(0, 31030216, 30001, 20001, 31032216, 2.0, 0.0, 0, 0, 0, 0)


@RestartOnRest(31032650)
def Event_31032650(_, tutorial_param_id: int, flag: uint):
    """Event 31032650"""
    if Multiplayer():
        return
    AND_5.Add(PlayerHasGood(250, including_storage=True))
    if AND_5:
        return
    AND_1.Add(PlayerHasGood(250, including_storage=True))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9115, flag=flag, bit_count=1)


@RestartOnRest(31032651)
def Event_31032651(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31032651"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)


@RestartOnRest(31032800)
def Event_31032800():
    """Event 31032800"""
    if FlagEnabled(31030800):
        return
    
    MAIN.Await(HealthValue(Characters.BeastmanofFarumAzula) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BeastmanofFarumAzula, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.BeastmanofFarumAzula))
    
    KillBossAndDisplayBanner(character=Characters.BeastmanofFarumAzula, banner_type=BannerType.EnemyFelled)
    EnableFlag(31030800)
    EnableFlag(9233)
    if PlayerInOwnWorld():
        EnableFlag(61233)
    Wait(5.0)
    AwardItemLot(20330, host_only=True)
    End()


@RestartOnRest(31032810)
def Event_31032810():
    """Event 31032810"""
    GotoIfFlagDisabled(Label.L0, flag=31030800)
    DisableCharacter(Characters.BeastmanofFarumAzula)
    DisableAnimations(Characters.BeastmanofFarumAzula)
    Kill(Characters.BeastmanofFarumAzula)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BeastmanofFarumAzula)
    DisableAnimations(Characters.BeastmanofFarumAzula)
    ForceAnimation(Characters.BeastmanofFarumAzula, 30003)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31032800))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(31030801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.BeastmanofFarumAzula)
    EnableAnimations(Characters.BeastmanofFarumAzula)
    SetNetworkUpdateRate(Characters.BeastmanofFarumAzula, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BeastmanofFarumAzula, name=903970310)
    Wait(1.0)
    ForceAnimation(Characters.BeastmanofFarumAzula, 20003)


@RestartOnRest(31032811)
def Event_31032811():
    """Event 31032811"""
    if FlagEnabled(31030800):
        return
    AND_1.Add(HealthRatio(Characters.BeastmanofFarumAzula) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31032802)


@RestartOnRest(31032849)
def Event_31032849():
    """Event 31032849"""
    CommonFunc_9005800(
        0,
        flag=31030800,
        entity=Assets.AEG099_001_9000,
        region=31032800,
        flag_1=31032805,
        character=31035800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31030800,
        entity=Assets.AEG099_001_9000,
        region=31032800,
        flag_1=31032805,
        flag_2=31032806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31030800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 31030800, 931000, 31032805, 31032806, 0, 31032802, 0, 0)
