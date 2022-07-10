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
    RegisterGrace(grace_flag=76306, obj=1040531950, unknown=5.0)
    Event_1040532800()
    Event_1040532810()
    Event_1040532849()
    Unknown_2005_18(obj_1=1040531201, obj_2=1040531200, unk_8_12=151)
    Event_1040532650()
    Event_1040532660()
    Event_1040532665()
    Event_1040532670()
    Event_1040532680()
    Event_1040532685()
    Event_1040532690()
    RunCommonEvent(0, 90005300, args=(1040530500, 1040530500, 40320, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1040530400, 1040532400, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530401, 1040532400, 7.0, 0.4000000059604645, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530404, 1040532404, 7.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530404, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1040530402, 1040532402, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(1040530430, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530431, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530432, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530433, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530434, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530435, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530436, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530437, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530438, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530439, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530440, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530441, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530442, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530443, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530444, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530445, 1040532430, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530451, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530452, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530453, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530454, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530455, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530456, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530457, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530458, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530461, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530462, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530463, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530464, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040530465, 1040532452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1040530450, 30000, 20000, 1040532450, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(1040530250, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1040530260, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1040530212, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1040530267, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1040530263, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(1040530207, 30004, 20004, 1040532207, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1040530261, 30010, 20010, 1040532207, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1040530262, 30010, 20010, 1040532207, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(1040530405, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1040530460, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1040530357, 1040532357, 0.0, 3000), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1040530357, 2.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1040530353, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1040530363, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1040530364, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1040530365, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1040530351, 10.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(1040530390, 30001, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(
        0,
        90005200,
        args=(1040530300, 30000, 20000, 1040532405, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1040530301, 30000, 20000, 1040532405, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(1040530302, 30000, 20000, 1040532405, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(1040530303, 30000, 20000, 1040532405, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )


@RestartOnRest(1040532800)
def Event_1040532800():
    """Event 1040532800"""
    EndIfFlagEnabled(1040530800)
    IfHealthValueLessThanOrEqual(MAIN, 1040530800, value=0)
    Wait(4.0)
    PlaySoundEffect(1040530800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1040530800)
    KillBossAndDisplayBanner(character=1040530800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(1040531560, obj_act_id=1110064)
    EnableFlag(1040530800)


@RestartOnRest(1040532810)
def Event_1040532810():
    """Event 1040532810"""
    GotoIfFlagDisabled(Label.L0, flag=1040530800)
    DisableCharacter(1040530800)
    DisableAnimations(1040530800)
    Kill(1040530800)
    EnableObjectActivation(1040531560, obj_act_id=1110064)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1040530800)
    ForceAnimation(1040530800, 30000, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 1040532805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1040532800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(1040530800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(1040530800, 20000, unknown2=1.0)
    EnableAI(1040530800)
    Wait(2.799999952316284)
    EnableBossHealthBar(1040530800, name=903550540)
    DisableObjectActivation(1040531560, obj_act_id=1110064)


@RestartOnRest(1040532849)
def Event_1040532849():
    """Event 1040532849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1040530800, 1040531800, 1040532800, 1040532805, 1040535800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1040530800, 1040531800, 1040532800, 1040532805, 1040532806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1040530800, 1040531800, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1040530800, 920900, 1040532805, 1040532806, 0, 1040532802, 0, 0),
        arg_types="IiIIIIii",
    )
    RunCommonEvent(0, 9005812, args=(1040530800, 1040531801, 3, 0, 0), arg_types="IIiIi")


@RestartOnRest(1040532650)
def Event_1040532650():
    """Event 1040532650"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableObject(1040531650)
    DeleteVFX(1040532650, erase_root_only=False)
    IfFlagEnabled(MAIN, 1039530505)
    EnableObject(1040531650)
    CreateVFX(1040532650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1040531650)
    DeleteVFX(1040532650, erase_root_only=False)
    End()


@RestartOnRest(1040532660)
def Event_1040532660():
    """Event 1040532660"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1040530655)
    IfFlagEnabled(AND_1, 1039530505)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1040532651)
    IfActionButtonParamActivated(AND_1, action_button_id=9521, entity=1040531650)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1040530655)
    DisableObject(1040531650)
    DisableMapPiece(map_piece_id=1040532651)
    RotateToFaceEntity(PLAYER, 1040531650, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532665)
def Event_1040532665():
    """Event 1040532665"""
    IfFlagEnabled(MAIN, 1040530655)
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532670)
def Event_1040532670():
    """Event 1040532670"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableObject(1040531651)
    IfFlagEnabled(MAIN, 1039530505)
    EnableObject(1040531651)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1040531651)
    End()


@RestartOnRest(1040532680)
def Event_1040532680():
    """Event 1040532680"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=1040531651, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1040530680)
    End()


@RestartOnRest(1040532685)
def Event_1040532685():
    """Event 1040532685"""
    IfFlagEnabled(MAIN, 1040530680)
    ForceAnimation(1040531651, 1, wait_for_completion=True, unknown2=1.0)
    DisableObject(1040531651)
    End()


@RestartOnRest(1040532690)
def Event_1040532690():
    """Event 1040532690"""
    IfFlagEnabled(AND_15, 1040530655)
    GotoIfConditionTrue(Label.L2, input_condition=AND_15)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)

    # --- Label 2 --- #
    DefineLabel(2)
    Kill(1040530610, award_souls=True)
    EndIfConditionTrue(input_condition=AND_15)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1040533610)
    GotoIfFlagEnabled(Label.L1, flag=1040532701)
    DisableSpawner(entity=1040533610)
    IfFlagEnabled(AND_1, 1039530505)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1040532610)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=1040533610)
    ClearTargetList(1040530610)
    MakeEnemyAppear(character=1040533610)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterDead(AND_2, 1040530610)
    SkipLinesIfConditionFalse(4, AND_2)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=10.0)
    EnableSpawner(entity=1040533610)
    ClearTargetList(1040530610)
    MakeEnemyAppear(character=1040533610)
    SkipLinesIfFlagDisabled(1, 1040530655)
    Wait(5.0)
    DisableSpawner(entity=1040533610)
    EnableFlag(1040532701)
    Restart()
