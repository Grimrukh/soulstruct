"""
Coastal Cave

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
from .enums.m31_15_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31150000, asset=Assets.AEG099_060_9000)
    CommonFunc_AITrigger_RegionOrHurt(0, character=31155800, region=31152500, seconds=0.0, animation_id=0)
    Event_31152800()
    Event_31152810()
    Event_31152820(0, character=Characters.DemiHumanBeastman0)
    Event_31152820(1, character=Characters.DemiHumanBeastman1)
    Event_31152849()
    Event_31152816()
    Event_31152830(0, flag=31150815, character=Characters.TalkDummy0)
    Event_31152811()
    CommonFunc_90005780(
        0,
        flag=31150800,
        summon_flag=31152160,
        dismissal_flag=31152161,
        character=Characters.OldKnightIstvan,
        sign_type=20,
        region=31152701,
        right=31159250,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=31150800, flag_1=31152160, flag_2=31152161, character=Characters.OldKnightIstvan)
    Event_31152825(
        0,
        flag=31152160,
        region=31152805,
        character=Characters.OldKnightIstvan,
        target_entity=31152500,
        region_1=31152809,
        animation=0,
    )
    CommonFunc_90005646(
        0,
        flag=31150800,
        left_flag=31152840,
        cancel_flag__right_flag=31152841,
        asset=Assets.AEG099_065_9000,
        player_start=31152840,
        area_id=31,
        block_id=15,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_31153700(0, character=Characters.DemiHumanShaman)
    Event_31153701(0, seconds=30.0)
    Event_31153710()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DemiHumanShaman)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.DemiHumanBeastman0, region=31152800, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.DemiHumanBeastman1, region=31152800, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.DemiHuman0, radius=7.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman8,
        animation_id=30000,
        animation_id_1=20000,
        region=31152217,
        radius=2.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LargeDemiHuman,
        animation_id=30001,
        animation_id_1=20001,
        region=31152217,
        radius=2.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.DemiHuman9, region=31152219, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.DemiHuman10, region=31152219, radius=2.0, seconds=0.0, animation_id=0)
    Event_31152570()


@RestartOnRest(31152570)
def Event_31152570():
    """Event 31152570"""
    WaitFramesAfterCutscene(frames=1)
    if FlagEnabled(31152570):
        return
    DisableAsset(Assets.AEG027_114_9000)
    DeleteAssetVFX(Assets.AEG027_114_9000)
    if FlagEnabled(3946):
        EnableAsset(Assets.AEG027_114_9000)


@RestartOnRest(31152650)
def Event_31152650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31152650"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(700690):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(700690))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    EnableFlag(700690)


@RestartOnRest(31152800)
def Event_31152800():
    """Event 31152800"""
    if FlagEnabled(31150800):
        return
    AND_2.Add(CharacterDead(Characters.DemiHumanBeastman0))
    AND_2.Add(CharacterDead(Characters.DemiHumanBeastman1))
    
    MAIN.Await(AND_2)
    
    Wait(2.0)
    PlaySoundEffect(Characters.DemiHumanBeastman0, 888880000, sound_type=SoundType.s_SFX)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=31152810, unk_8_12=1)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=31152811, unk_8_12=1)
    KillBossAndDisplayBanner(character=Characters.DemiHumanBeastman0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31150800)
    EnableFlag(9234)
    if PlayerInOwnWorld():
        EnableFlag(61234)
    Wait(5.0)
    AwardItemLot(20340, host_only=True)
    End()


@RestartOnRest(31152810)
def Event_31152810():
    """Event 31152810"""
    GotoIfFlagDisabled(Label.L0, flag=31150800)
    DisableCharacter(Characters.DemiHumanBeastman0)
    DisableAnimations(Characters.DemiHumanBeastman0)
    Kill(Characters.DemiHumanBeastman0)
    Kill(31155800)
    DisableCharacter(Characters.DemiHumanBeastman1)
    DisableAnimations(Characters.DemiHumanBeastman1)
    Kill(Characters.DemiHumanBeastman1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31150815)
    DisableCharacter(Characters.DemiHumanBeastman0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31152800))
    AND_1.Add(CharacterAlive(Characters.DemiHumanBeastman0))
    AND_1.Add(CharacterBackreadEnabled(Characters.DemiHumanBeastman0))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31152800))
    AND_2.Add(CharacterAlive(Characters.DemiHumanBeastman1))
    AND_2.Add(CharacterBackreadEnabled(Characters.DemiHumanBeastman1))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHumanBeastman0, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHumanBeastman1, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(31150815)
    EnableCharacter(Characters.DemiHumanBeastman0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(31152805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31152800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHumanBeastman0, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(Characters.DemiHumanBeastman0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanBeastman0, name=904120310)
    SetNetworkUpdateRate(Characters.DemiHumanBeastman1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanBeastman1, name=904120311, bar_slot=1)
    EnableFlag(31152815)
    EnableNetworkFlag(31152805)
    BanishInvaders(unknown=0)
    RemoveSpecialEffect(31155200, 8081)


@RestartOnRest(31152816)
def Event_31152816():
    """Event 31152816"""
    OR_1.Add(FlagEnabled(31150815))
    OR_1.Add(FlagEnabled(31150800))
    if OR_1:
        return
    OR_2.Add(HasAIStatus(Characters.DemiHumanBeastman1, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DemiHumanBeastman0, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(Characters.DemiHumanBeastman0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanBeastman0, name=904120310)
    SetNetworkUpdateRate(Characters.DemiHumanBeastman1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanBeastman1, name=904120311, bar_slot=1)
    EnableFlag(31152815)
    RemoveSpecialEffect(31155200, 8081)
    SetAIParamID(0, ai_param_id=0)


@RestartOnRest(31152811)
def Event_31152811():
    """Event 31152811"""
    if FlagEnabled(31150800):
        return
    OR_15.Add(CharacterDead(Characters.DemiHumanBeastman0))
    OR_15.Add(CharacterDead(Characters.DemiHumanBeastman1))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31152842)


@RestartOnRest(31152820)
def Event_31152820(_, character: uint):
    """Event 31152820"""
    if FlagEnabled(31150800):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 4306))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 4305)


@ContinueOnRest(31152825)
def Event_31152825(_, flag: uint, region: uint, character: uint, target_entity: uint, region_1: uint, animation: int):
    """Event 31152825"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(region))
    
    MAIN.Await(AND_1)
    
    DisableMapCollision(collision=31151835)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    OR_15.Add(TimeElapsed(seconds=4.0))
    OR_14.Add(OR_15)
    OR_14.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_14)
    
    RestartIfLastConditionResultTrue(input_condition=OR_15)
    if ValueNotEqual(left=animation, right=0):
        FaceEntity(character, target_entity, animation=animation, wait_for_completion=True)
    else:
        FaceEntity(character, target_entity, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_5)
    
    RestartIfLastConditionResultTrue(input_condition=OR_4)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    EnableMapCollision(collision=31151835)


@RestartOnRest(31152830)
def Event_31152830(_, flag: uint, character: uint):
    """Event 31152830"""
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31152849)
def Event_31152849():
    """Event 31152849"""
    CommonFunc_9005800(
        0,
        flag=31150800,
        entity=Assets.AEG099_003_9000,
        region=31152804,
        flag_1=31152805,
        character=31155800,
        action_button_id=10000,
        left=31150815,
        region_1=31152500,
    )
    CommonFunc_9005801(
        0,
        flag=31150800,
        entity=Assets.AEG099_003_9000,
        region=31152804,
        flag_1=31152805,
        flag_2=31152806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31150800, asset=Assets.AEG099_003_9000, dummy_id=3, right=31150815)
    CommonFunc_9005812(
        0,
        flag=31150800,
        asset=Assets.AEG099_001_9000,
        dummy_id=3,
        right=31150815,
        dummy_id_1=806760,
    )
    CommonFunc_9005822(
        0,
        flag=31150800,
        bgm_boss_conv_param_id=931000,
        flag_1=31152805,
        flag_2=31152806,
        right=31152815,
        flag_3=31152842,
        left=0,
        left_1=0,
    )


@RestartOnRest(31153700)
def Event_31153700(_, character: uint):
    """Event 31153700"""
    WaitFrames(frames=1)
    DisableFlag(31159200)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3940))
    AND_1.Add(FlagEnabled(1043379353))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3946))
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930020)
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
    
    MAIN.Await(FlagEnabled(31159200))
    
    Restart()


@RestartOnRest(31153701)
def Event_31153701(_, seconds: float):
    """Event 31153701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3946):
        return
    if FlagEnabled(31159205):
        return
    
    MAIN.Await(FlagEnabled(31152700))
    
    Wait(seconds)
    DisableFlag(31152700)
    Restart()


@RestartOnRest(31153710)
def Event_31153710():
    """Event 31153710"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(31159250)
    if FlagEnabled(31150800):
        return
    if FlagEnabled(7602):
        return
    EnableFlag(31159250)
    End()
