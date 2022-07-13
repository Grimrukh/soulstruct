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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 9005810, args=(12040800, 71240, 12040950, 12041950, 5.0), arg_types="IIIIf")
    Event_12042680()
    Event_12042400()
    Event_12042849()
    Event_12042800()
    Event_12042810()


@NeverRestart(12042400)
def Event_12042400():
    """Event 12042400"""
    GotoIfFlagDisabled(Label.L0, flag=114)
    DisableObject(12041400)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerInOwnWorld(1)
    Goto(Label.L10)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DeleteVFX(12041400)
    CreateObjectVFX(12041400, vfx_id=101, model_point=1507)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9506, entity=12041400)
    IfFlagEnabled(AND_2, 114)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFlagEnabled(Label.L1, flag=114)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisplayDialog(text=20006, anchor_entity=0, display_distance=5.0)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteVFX(12041400)
    DisableObject(12041400)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteVFX(12041400)
    CreateObjectVFX(12041400, vfx_id=101, model_point=1507)
    IfFlagEnabled(OR_9, 114)
    IfConditionTrue(MAIN, input_condition=OR_9)
    DeleteVFX(12041400)
    DisableObject(12041400)
    End()


@RestartOnRest(12042680)
def Event_12042680():
    """Event 12042680"""
    DisableNetworkSync()
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DeleteVFX(12043680, erase_root_only=False)
    IfOutsideMap(AND_1, game_map=ASTEL_ARENA)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12042680)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfInsideMap(AND_2, game_map=ASTEL_ARENA)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=1034412680)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CreateVFX(12043680)
    Wait(1.0)
    IfInsideMap(AND_10, game_map=ASTEL_ARENA)
    IfCharacterInsideRegion(AND_10, character=PLAYER, region=1034412680)
    IfConditionTrue(OR_10, input_condition=AND_10)
    IfOutsideMap(AND_11, game_map=ASTEL_ARENA)
    IfCharacterOutsideRegion(AND_11, character=PLAYER, region=12042680)
    IfConditionTrue(OR_10, input_condition=AND_11)
    IfConditionTrue(MAIN, input_condition=OR_10)
    DeleteVFX(12043680)
    Wait(1.0)
    Restart()


@NeverRestart(12042800)
def Event_12042800():
    """Event 12042800"""
    EndIfFlagEnabled(12040800)
    IfHealthRatioLessThanOrEqual(MAIN, 12040800, value=0.0)
    Wait(5.0)
    PlaySoundEffect(12040800, 77777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 12040800)
    KillBossAndDisplayBanner(character=12040800, banner_type=BannerType.HollowArenaWin)
    EnableFlag(12040800)
    EnableFlag(9108)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61108)


@RestartOnRest(12042810)
def Event_12042810():
    """Event 12042810"""
    GotoIfFlagDisabled(Label.L0, flag=12040800)
    DisableCharacter(12040800)
    DisableAnimations(12040800)
    Kill(12040800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12040800)
    EnableNavmeshType(navmesh_id=12044300, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=12044301, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(AND_2, 12042805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12042800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(12040800)
    SetNetworkUpdateRate(12040800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(12040800, name=904620001)
    SetCharacterEventTarget(12040800, region=12040810)


@NeverRestart(12042849)
def Event_12042849():
    """Event 12042849"""
    RunCommonEvent(0, 9005811, args=(12040800, 12041801, 8, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005800,
        args=(12040800, 12041800, 12042800, 12042805, 12045800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(12040800, 12041800, 12042800, 12042805, 12042806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12040800, 12041800, 8, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12040800, 920700, 12042805, 12042806, 0, 12042802, 0, 0), arg_types="IiIIIIii")
