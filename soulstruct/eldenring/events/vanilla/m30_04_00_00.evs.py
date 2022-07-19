"""
Murkwater Catacombs

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
from .entities.m30_04_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30040800,
        left_flag=30042840,
        cancel_flag__right_flag=30042841,
        asset=Assets.AEG099_065_9000,
        player_start=30042840,
        area_id=30,
        block_id=4,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=300400, asset=Assets.AEG099_060_9000)
    Event_30042800()
    Event_30042810()
    Event_30042849()
    Event_30042811()
    CommonFunc_90005650(
        0,
        flag=30040540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30043541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30040540, anchor_entity=Assets.AEG027_041_0500)
    Event_30042500()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.Imp0,
        animation_id=30001,
        animation_id_1=20001,
        region=30042200,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp1,
        animation_id=30002,
        animation_id_1=20002,
        region=30042201,
        seconds=1.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30042202,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp3,
        animation_id=30010,
        animation_id_1=20010,
        region=30042205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp4,
        animation_id=30010,
        animation_id_1=20010,
        region=30042205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp5, region=30042207, radius=1.0, seconds=0.0, animation_id=3004)
    CommonFunc_90005200(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30042210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp7,
        animation_id=30010,
        animation_id_1=20010,
        region=30042210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 30040212, 30003, 20003, 30042212, 0.0, 0, 0, 0, 0)


@NeverRestart(30040050)
def Event_30040050():
    """Event 30040050"""
    if ThisEventSlotFlagEnabled():
        return


@NeverRestart(30042500)
def Event_30042500():
    """Event 30042500"""
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001070,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001060,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001050,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001040,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001030,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0501,
        region=30042600,
        behavior_id=801001020,
        source_entity=30042601,
        source_entity_1=30042602,
        source_entity_2=30042603,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy2,
            entity=Assets.AEG027_044_0501,
            region=30042600,
            behavior_id=801001010,
            source_entity=30042601,
            source_entity_1=30042602,
            source_entity_2=30042603,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy2,
            entity=Assets.AEG027_044_0501,
            region=30042600,
            behavior_id=801001000,
            source_entity=30042601,
            source_entity_1=30042602,
            source_entity_2=30042603,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001070,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001060,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001050,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001040,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001030,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0500,
        region=30042605,
        behavior_id=801001020,
        source_entity=30042606,
        source_entity_1=30042607,
        source_entity_2=30042608,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy3,
            entity=Assets.AEG027_044_0500,
            region=30042605,
            behavior_id=801001010,
            source_entity=30042606,
            source_entity_1=30042607,
            source_entity_2=30042608,
        )
    else:
        CommonFunc_90005660(0, 30040605, 30041605, 30042605, 801001000, 30042606, 30042607, 30042608)


@RestartOnRest(30042650)
def Event_30042650(_, tutorial_param_id: int, flag: uint):
    """Event 30042650"""
    if Multiplayer():
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=MURKWATER_CATACOMBS))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(30042800)
def Event_30042800():
    """Event 30042800"""
    if FlagEnabled(30040800):
        return
    
    MAIN.Await(HealthValue(Characters.GraveWardenDuelist) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GraveWardenDuelist, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GraveWardenDuelist))
    
    KillBossAndDisplayBanner(character=Characters.GraveWardenDuelist, banner_type=BannerType.EnemyFelled)
    EnableFlag(30040800)
    EnableFlag(9204)
    if PlayerInOwnWorld():
        EnableFlag(61204)


@RestartOnRest(30042810)
def Event_30042810():
    """Event 30042810"""
    GotoIfFlagDisabled(Label.L0, flag=30040800)
    DisableCharacter(Characters.GraveWardenDuelist)
    DisableAnimations(Characters.GraveWardenDuelist)
    Kill(Characters.GraveWardenDuelist)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GraveWardenDuelist)
    AND_2.Add(FlagEnabled(30042805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30042800))
    
    MAIN.Await(AND_2)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(30040801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GraveWardenDuelist)
    SetNetworkUpdateRate(Characters.GraveWardenDuelist, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GraveWardenDuelist, name=903400300)


@RestartOnRest(30042811)
def Event_30042811():
    """Event 30042811"""
    if FlagEnabled(30040800):
        return
    AND_1.Add(HealthRatio(Characters.GraveWardenDuelist) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30042802)


@RestartOnRest(30042849)
def Event_30042849():
    """Event 30042849"""
    CommonFunc_9005800(
        0,
        flag=30040800,
        entity=Assets.AEG099_001_9000,
        region=30042800,
        flag_1=30042805,
        character=30045800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30040800,
        entity=Assets.AEG099_001_9000,
        region=30042800,
        flag_1=30042805,
        flag_2=30042806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30040800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30040800, 930000, 30042805, 30042806, 0, 30042802, 0, 0)


@RestartOnRest(30042900)
def Event_30042900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 30042900"""
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
