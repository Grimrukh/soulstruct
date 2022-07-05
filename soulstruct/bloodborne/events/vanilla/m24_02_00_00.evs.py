"""
linked:
180

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス戦_撃破時間
58: ボス_撃破
70: PC情報_ボス撃破_月の落とし子
104: ボス_戦闘開始
120: PC情報_ボス撃破_月からの使者
154: PC情報_聖堂街C到達時
180: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=20, args=(2420950, 2421950, 999, 12427800))
    RunEvent(7000, slot=21, args=(2420951, 2421951, 12421800, 12427820))
    RunEvent(7000, slot=22, args=(2420952, 2421952, 12421700, 12427840))
    RunEvent(7100, slot=20, args=(72420200, 2421950))
    RunEvent(7100, slot=21, args=(72420201, 2421951))
    RunEvent(7100, slot=22, args=(72420202, 2421952))
    RunEvent(7200, slot=20, args=(72420100, 2421950, 2102950))
    RunEvent(7200, slot=21, args=(72420101, 2421951, 2102950))
    RunEvent(7200, slot=22, args=(72420102, 2421952, 2102950))
    RunEvent(7300, slot=20, args=(72102420, 2421950))
    RunEvent(7300, slot=21, args=(72102421, 2421951))
    RunEvent(7300, slot=22, args=(72102422, 2421952))
    DeleteVFX(2423910, erase_root_only=False)
    Event_12424400(0, flag=12424440, vfx_id=2423910, flag_1=12424420, flag_2=12424430, flag_3=12421800, flag_4=6001)
    Event_12424410(
        0,
        sign_type=0,
        character=2420910,
        region=2422910,
        summon_flag=12424420,
        dismissal_flag=12424430,
        flag=12424440,
        flag_1=12421800,
        action_button_id=10566
    )
    Event_12424450(0, character=2420910, region=2422911, flag=12424420, flag_1=12424430, flag_2=12424800)
    Event_12424460(
        0,
        character=2420910,
        region=2422911,
        region_1=2422800,
        region_2=2422801,
        animation=101130,
        flag=12424450,
        region_3=2422801
    )
    RunEvent(9200, slot=4, args=(2423900,))
    RunEvent(9220, slot=4, args=(2420710, 12424220, 12424221, 2420, 24, 2), arg_types="iiiiBB")
    RunEvent(9240, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types="iiiiBB")
    RunEvent(9260, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types="iiiiBB")
    RunEvent(9280, slot=4, args=(2420710, 12424220, 12424221, 2420, 12424700, 24, 2), arg_types="iiiiiBB")
    StartPlayLogMeasurement(measurement_id=2420000, name=0, overwrite=True)
    StartPlayLogMeasurement(measurement_id=2420001, name=18, overwrite=True)
    Event_12420990()
    Event_12420400()
    RunEvent(7600, slot=40, args=(2421999, 2423999))
    RunEvent(7600, slot=41, args=(2421998, 2423998))
    CreateHazard(
        obj_flag=12420020,
        obj=2421230,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    Event_12420123()
    Event_12420124()
    Event_12420140()
    Event_12420150()
    Event_12420151()
    Event_12420152()
    Event_12420153()
    Event_12420156()
    Event_12420850(0, 2427020, 2427021, 2427022, 12420130, 12420102, 2.0, 2427000, 920200)
    Event_12420850(1, 2427025, 2427026, 2427027, 12420132, 12420110, 3.0, 2427017, 920202)
    Event_12420850(2, 2427028, 2427029, 2427030, 12420131, 12420111, 3.0, 2427016, 920203)
    Event_12420853()
    Event_12420854()
    Event_12420280(0, region=2422500)
    Event_12420280(1, region=2422501)
    Event_12420285(0, region=2422502, flag=12420032)
    Event_12420285(1, region=2422503, flag=12420033)
    Event_12420000(0, obj=2421201, animation_id=1, obj_act_id=2420020, obj_act_id_1=12420120)
    Event_12420000(1, obj=2421223, animation_id=1, obj_act_id=2420030, obj_act_id_1=12420121)
    Event_12420030(0, obj_act_id=12420120)
    Event_12420030(2, obj_act_id=12420126)
    Event_12420030(3, obj_act_id=12420127)
    Event_12420050(0, obj=2421100, obj_act_id=12421000, obj_act_id_1=9942)
    Event_12420050(1, obj=2421101, obj_act_id=12421001, obj_act_id_1=9942)
    DisableSoundEvent(sound_id=2423802)
    DisableSoundEvent(sound_id=2423803)
    DisableSoundEvent(sound_id=2423812)
    DisableSoundEvent(sound_id=2423813)
    CreateProjectileOwner(entity=2420801)
    Event_12424812()
    Event_12424813()
    Event_12421800()
    Event_12421801()
    Event_12421802()
    Event_12424810()
    Event_12424811()
    Event_12424802()
    Event_12424803()
    Event_12424804()
    Event_12424805()
    Event_12424980()
    Event_12424990()
    Event_12421803()
    Event_12424870(
        0,
        npc_part_id=2420,
        npc_part_id_1=2420,
        part_index=5,
        part_health=200,
        special_effect_id=480,
        special_effect_id_1=490,
        animation_id=8040
    )
    Event_12424871(
        0,
        npc_part_id=2421,
        npc_part_id_1=2421,
        part_index=1,
        part_health=200,
        special_effect_id=481,
        special_effect_id_1=491,
        animation_id=8010
    )
    Event_12424871(
        1,
        npc_part_id=2422,
        npc_part_id_1=2422,
        part_index=2,
        part_health=200,
        special_effect_id=482,
        special_effect_id_1=492,
        animation_id=8000
    )
    Event_12424871(
        2,
        npc_part_id=2423,
        npc_part_id_1=2423,
        part_index=3,
        part_health=200,
        special_effect_id=483,
        special_effect_id_1=493,
        animation_id=8030
    )
    Event_12424871(
        3,
        npc_part_id=2424,
        npc_part_id_1=2424,
        part_index=4,
        part_health=200,
        special_effect_id=484,
        special_effect_id_1=494,
        animation_id=8020
    )
    Event_12424712()
    Event_12424713()
    Event_12421700()
    Event_12421701()
    Event_12421702()
    Event_12424710()
    Event_12424711()
    Event_12424702()
    Event_12424703()
    Event_12424704()
    Event_12424705()
    Event_12424790()
    Event_12424780()
    Event_12424791()
    Event_12424792(0, character=2420750)
    Event_12424792(1, character=2420751)
    Event_12421703()
    Event_12424785(0, character=2420810, region=2422816, command_id=10, flag=12424702)
    Event_12424785(1, character=2420811, region=2422817, command_id=20, flag=12424790)
    Event_12424784()
    Event_12424787(0, character=2420711, region=2422816, command_id=10, flag=12424702, character_1=2420810)
    Event_12424787(1, character=2420712, region=2422816, command_id=10, flag=12424702, character_1=2420810)
    Event_12424795()
    Event_12424770(0, character=2423711, character_1=2420711)
    Event_12424770(1, character=2423712, character_1=2420712)
    Event_12424770(2, character=2423713, character_1=2420713)
    Event_12424770(5, character=2423716, character_1=2420716)
    Event_12424770(6, character=2423717, character_1=2420717)
    Event_12424770(8, character=2423719, character_1=2420719)
    Event_12424770(9, character=2423720, character_1=2420720)
    Event_12424770(12, character=2423720, character_1=2420810)

    # --- 1 --- #
    DefineLabel(1)
    Event_12420300()
    Event_12420320()
    Event_12420310()
    Event_12425200(0, character=2420262)
    Event_12425210(0, character=2420250)
    Event_12425210(1, character=2420258)
    Event_12425210(2, character=2420267)
    Event_12425225()
    Event_12425221(0, character=2420256)
    Event_12425250(0, 2420252, 1.5, 2422659, 9.0, 2422252, 20, 1, 1)
    Event_12425245()
    DisableFlag(12425246)
    Event_12425300(0, character=2420451)
    Event_12425305(0, character=2420452)
    Event_12425310(0, character=2420352)
    Event_12425310(1, character=2420375)
    Event_12425310(2, character=2420376)
    Event_12425310(3, character=2420387)
    Event_12425310(4, character=2420388)
    Event_12425320(0, character=2420380, animation_id=7012, animation_id_1=7013, region=2422380)
    Event_12425320(1, character=2420381, animation_id=7012, animation_id_1=7013, region=2422381)
    Event_12425320(2, character=2420382, animation_id=7012, animation_id_1=7013, region=2422382)
    Event_12425320(3, character=2420383, animation_id=7012, animation_id_1=7013, region=2422383)
    Event_12425320(4, character=2420384, animation_id=7012, animation_id_1=7013, region=2422384)
    Event_12425320(5, character=2420350, animation_id=7012, animation_id_1=7013, region=2422350)
    Event_12425320(6, character=2420351, animation_id=7012, animation_id_1=7013, region=2422351)
    Event_12425320(7, character=2420377, animation_id=7012, animation_id_1=7013, region=2422377)
    Event_12425320(8, character=2420357, animation_id=7012, animation_id_1=7013, region=2422357)
    Event_12425320(9, character=2420358, animation_id=7012, animation_id_1=7013, region=2422358)
    Event_12425320(10, character=2420359, animation_id=7012, animation_id_1=7013, region=2422359)
    Event_12425320(11, character=2420363, animation_id=7012, animation_id_1=7013, region=2422363)
    Event_12425320(12, character=2420364, animation_id=7012, animation_id_1=7013, region=2422364)
    Event_12425320(13, character=2420385, animation_id=7012, animation_id_1=7013, region=2422385)
    Event_12425320(14, character=2420386, animation_id=7012, animation_id_1=7013, region=2422386)
    SetNetworkUpdateRate(2420811, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Event_12425500(0, 2420357, 5.0, 1, 2422650, 0.0)
    Event_12425500(1, 2420358, 5.0, 1, 2422650, 0.0)
    Event_12425500(2, 2420359, 5.0, 1, 2422650, 0.0)
    Event_12425500(3, 2420363, 5.0, 1, 2422650, 0.0)
    Event_12425500(4, 2420364, 5.0, 1, 2422650, 0.0)
    Event_12425500(5, 2420251, 5.0, 1, 2422251, 0.0)
    Event_12425500(6, 2420255, 3.0, 1, 2422254, 0.0)
    Event_12425500(7, 2420255, 3.0, 1, 2422255, 0.0)
    Event_12425500(8, 2420256, 5.0, 1, 2422256, 0.0)
    Event_12425500(9, 2420377, 5.0, 1, 2422656, 0.0)
    Event_12425500(10, 2420351, 5.0, 1, 2422656, 0.0)
    Event_12425500(11, 2420385, 5.0, 1, 2422650, 0.0)
    Event_12425500(12, 2420386, 5.0, 1, 2422650, 0.0)
    Event_12425500(13, 2420259, 5.0, 1, 2422259, 0.0)
    Event_12425500(14, 2420350, 5.0, 1, 2422654, 0.0)
    Event_12425500(15, 2420380, 5.0, 1, 2422654, 0.0)
    Event_12425500(16, 2420381, 5.0, 1, 2422654, 0.0)
    Event_12425500(17, 2420382, 5.0, 1, 2422654, 0.0)
    Event_12425500(18, 2420383, 5.0, 1, 2422654, 0.0)
    Event_12425500(19, 2420384, 5.0, 1, 2422654, 0.0)
    Event_12425500(20, 2420203, 5.0, 1, 2422653, 0.0)
    Event_12425500(21, 2420264, 2.0, 1, 2422264, 0.0)
    Event_12425500(22, 2420400, 5.0, 1, 2422256, 0.0)
    Event_12425500(23, 2420450, 5.0, 1, 2422300, 0.0)
    Event_12425500(24, 2420451, 5.0, 1, 2422300, 0.0)
    Event_12425600()
    Event_12425601()
    Event_12425602()
    Event_12425603()
    Event_12425350(0, character=2420350, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(1, character=2420351, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(2, character=2420377, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(3, character=2420380, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(4, character=2420381, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(5, character=2420382, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(6, character=2420383, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425350(7, character=2420384, ai_param_id=252002, ai_param_id_1=252000)
    Event_12425400(0, attacked_entity=2420263, region=2422265, animation_id=3000)
    Event_12425400(1, attacked_entity=2420392, region=2422686, animation_id=3004)
    Event_12420100()
    RegisterLadder(start_climbing_flag=12420600, stop_climbing_flag=12420601, obj=2421600)
    Event_12420500()
    Event_12420700()
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6648)
    EnableFlag(12421999)
    SkipLinesIfFlagEnabled(5, 12421999)
    EnableObject(2421102)
    DisableObject(2421103)
    EnableTreasure(obj=2421102)
    DisableTreasure(obj=2421103)
    SkipLines(4)
    DisableObject(2421102)
    EnableObject(2421103)
    DisableTreasure(obj=2421102)
    EnableTreasure(obj=2421103)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6313)
    EnableFlag(12421998)
    SkipLinesIfFlagEnabled(5, 12421998)
    EnableObject(2421500)
    DisableObject(2421501)
    EnableTreasure(obj=2421500)
    DisableTreasure(obj=2421501)
    SkipLines(4)
    DisableObject(2421500)
    EnableObject(2421501)
    DisableTreasure(obj=2421500)
    EnableTreasure(obj=2421501)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2423950)
    DisableGravity(2423950)
    DisableCharacterCollision(2423950)
    DisableAnimations(2423951)
    DisableGravity(2423951)
    DisableCharacterCollision(2423951)
    DisableAnimations(2423952)
    DisableGravity(2423952)
    DisableCharacterCollision(2423952)
    Event_12425290()


@RestartOnRest(12420700)
def Event_12420700():
    """Event 12420700"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(0, 2420268)
    AwardItemLot(2420900, host_only=False)


@NeverRestart(12421800)
def Event_12421800():
    """Event 12421800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2423802)
    DisableSoundEvent(sound_id=2423803)
    DisableCharacter(2420800)
    Kill(2420800)
    DisableObject(2421800)
    DeleteVFX(2423800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2420800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2421800)
    DeleteVFX(2423800)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2420800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=28)
    AwardItemLot(80000300, host_only=False)
    EnableFlag(2421)
    EnableFlag(9459)
    StartPlayLogMeasurement(measurement_id=2420000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2420001, name=18, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2420010, name=40, overwrite=False)
    CreatePlayLog(name=58)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=70,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=70,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=70,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=70,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12421801)
def Event_12421801():
    """Event 12421801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    IfFlagEnabled(1, 12421800)
    IfCharacterBackreadDisabled(2, 2420800)
    IfHealthLessThanOrEqual(2, 2420800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2422800, 500099999, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12421802)
def Event_12421802():
    """Event 12421802"""
    EndIfFlagEnabled(12421800)
    GotoIfThisEventFlagDisabled(Label.L0)
    Move(2420800, destination=2422800, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(2420800, 2422804)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2420800, 7001, loop=True)
    EnableImmortality(2420800)
    AddSpecialEffect(2420800, 5647)
    IfFlagDisabled(1, 12421800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=2420800, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2420800, 7000, wait_for_completion=True)
    DisableImmortality(2420800)
    CancelSpecialEffect(2420800, 5647)
    EnableFlag(12424800)
    EndIfFlagEnabled(9304)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(9304)


@NeverRestart(12421803)
def Event_12421803():
    """Event 12421803"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12424800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12424800)
    EnableFlag(12421802)


@NeverRestart(12424810)
def Event_12424810():
    """Event 12424810"""
    EndIfFlagEnabled(12421800)
    GotoIfFlagEnabled(Label.L0, flag=12421802)
    SkipLinesIfClient(2)
    DisableObject(2421800)
    DeleteVFX(2423800, erase_root_only=False)
    IfFlagDisabled(1, 12421800)
    IfFlagEnabled(1, 12421802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2421800)
    CreateVFX(2423800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12421800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2420800, entity=2421800)
    IfFlagEnabled(3, 12421800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12424800)
    Restart()


@NeverRestart(12424811)
def Event_12424811():
    """Event 12424811"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    IfFlagDisabled(1, 12421800)
    IfFlagEnabled(1, 12421802)
    IfFlagEnabled(1, 12424800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2420800, entity=2421800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2422801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12424801)
    Restart()


@NeverRestart(12424812)
def Event_12424812():
    """Event 12424812"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2421800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12424813)
def Event_12424813():
    """Event 12424813"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2421800, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2421800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12424802)
def Event_12424802():
    """Event 12424802"""
    EndIfFlagEnabled(12421800)
    DisableAI(2420800)
    DisableHealthBar(2420800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12424800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2420800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12424800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2420800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2420800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2420800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2420800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2420800)
    EnableBossHealthBar(2420800, name=251000)
    CreatePlayLog(name=104)
    StartPlayLogMeasurement(measurement_id=2420010, name=40, overwrite=True)


@NeverRestart(12424803)
def Event_12424803():
    """Event 12424803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2423802)
    DisableSoundEvent(sound_id=2423803)
    IfFlagDisabled(1, 12421800)
    IfFlagEnabled(1, 12424802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12424801)
    IfCharacterInsideRegion(1, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2423802)
    EnableFlag(12425246)
    IfCharacterHasTAEEvent(2, 2420800, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12421800)
    IfFlagEnabled(2, 12424802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12424801)
    IfCharacterInsideRegion(2, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2423802)
    EnableFlag(12425246)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2423803)


@NeverRestart(12424804)
def Event_12424804():
    """Event 12424804"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    IfCharacterHasTAEEvent(0, 2420800, tae_event_id=10)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfCharacterHasTAEEvent(0, 2420800, tae_event_id=20)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart(12424805)
def Event_12424805():
    """Event 12424805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    IfFlagEnabled(0, 12421800)
    DisableBossMusic(sound_id=2423802)
    DisableBossMusic(sound_id=2423803)
    DisableBossMusic(sound_id=-1)
    DisableFlag(12425246)


@RestartOnRest(12424870)
def Event_12424870(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12424870"""
    CreateNPCPart(
        2420800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        body_damage_correction=2.0,
    )
    SetNPCPartEffects(2420800, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, 2420800, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, 2420800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        2420800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=2.5,
    )
    SetNPCPartEffects(2420800, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    ResetAnimation(2420800)
    ForceAnimation(2420800, animation_id)
    AddSpecialEffect(2420800, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, special_effect_id_1)
    ReplanAI(2420800)
    IfCharacterHasTAEEvent(0, 2420800, tae_event_id=100)
    SetNPCPartHealth(2420800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2420800, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, special_effect_id)
    AICommand(2420800, command_id=-1, command_slot=0)
    ReplanAI(2420800)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12424871)
def Event_12424871(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12424871"""
    CreateNPCPart(2420800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2420800, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, 2420800, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, 2420800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        2420800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(2420800, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    ResetAnimation(2420800)
    ForceAnimation(2420800, animation_id)
    AddSpecialEffect(2420800, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, special_effect_id_1)
    ReplanAI(2420800)
    IfCharacterHasTAEEvent(0, 2420800, tae_event_id=100)
    SetNPCPartHealth(2420800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2420800, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, special_effect_id)
    AICommand(2420800, command_id=-1, command_slot=0)
    ReplanAI(2420800)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12424980)
def Event_12424980():
    """Event 12424980"""
    WaitFrames(frames=1)
    IfCharacterDead(1, 2420800)
    EndIfConditionTrue(1)
    IfFlagEnabled(2, 12424800)
    IfHealthLessThan(2, 2420800, value=0.5)
    IfConditionTrue(0, input_condition=2)
    AICommand(2420800, command_id=100, command_slot=0)
    ReplanAI(2420800)
    IfCharacterHasTAEEvent(0, 2420800, tae_event_id=500)
    AICommand(2420800, command_id=-1, command_slot=0)
    ReplanAI(2420800)


@NeverRestart(12424990)
def Event_12424990():
    """Event 12424990"""
    IfCharacterHasSpecialEffect(1, 2420800, 5650)
    IfHealthValueLessThan(1, 2420800, value=0)
    IfConditionTrue(0, input_condition=1)
    ShootProjectile(
        owner_entity=2420801,
        source_entity=2420800,
        model_point=6,
        behavior_id=225100310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    Restart()


@NeverRestart(12421700)
def Event_12421700():
    """Event 12421700"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2423812)
    DisableSoundEvent(sound_id=2423813)
    DisableCharacter(2420810)
    Kill(2420810)
    DisableCharacter(2420711)
    DisableCharacter(2420712)
    DisableCharacter(2420713)
    DisableCharacter(2420716)
    DisableCharacter(2420717)
    DisableCharacter(2420719)
    DisableCharacter(2420720)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    DisableAI(2420711)
    DisableAI(2420712)
    DisableAI(2420713)
    DisableAI(2420716)
    DisableAI(2420717)
    DisableAI(2420719)
    DisableAI(2420720)
    DisableObject(2421700)
    DisableObject(2421701)
    DeleteVFX(2423810, erase_root_only=False)
    DeleteVFX(2423811, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2420811)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2421700)
    DisableObject(2421701)
    DeleteVFX(2423810)
    DeleteVFX(2423811)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    Wait(3.0)
    KillBoss(game_area_param_id=2420811)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=27)
    SkipLinesIfFlagEnabled(2, 6332)
    AwardItemLot(25700000, host_only=False)
    SkipLines(1)
    AwardItemLot(25700005, host_only=False)
    EnableFlag(2420)
    EnableFlag(9458)
    StartPlayLogMeasurement(measurement_id=2420000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2420001, name=18, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2420010, name=40, overwrite=False)
    CreatePlayLog(name=58)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12421701)
def Event_12421701():
    """Event 12421701"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421800)
    IfFlagEnabled(1, 12421800)
    IfCharacterBackreadDisabled(2, 2420800)
    IfHealthLessThanOrEqual(2, 2420800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2422800, 500099999, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12421702)
def Event_12421702():
    """Event 12421702"""
    EndIfFlagEnabled(12421700)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2420810)
    DisableCharacter(2420711)
    DisableCharacter(2420712)
    DisableCharacter(2420713)
    DisableCharacter(2420716)
    DisableCharacter(2420717)
    DisableCharacter(2420719)
    DisableCharacter(2420720)
    IfFlagDisabled(1, 12421700)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2422815)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12424700)
    EnableFlag(12421702)
    EnableCharacter(2420716)
    EnableAI(2420716)
    ForceAnimation(2420716, 6200)
    EnableCharacter(2420717)
    EnableAI(2420717)
    ForceAnimation(2420717, 6200)
    EnableCharacter(2420720)
    EnableAI(2420720)
    ForceAnimation(2420720, 6200)
    Wait(2.0)
    EnableCharacter(2420810)
    EnableAI(2420810)
    ForceAnimation(2420810, 6200)
    EnableCharacter(2420711)
    EnableAI(2420711)
    ForceAnimation(2420711, 6200)
    EnableCharacter(2420713)
    EnableAI(2420713)
    ForceAnimation(2420713, 6200)
    Wait(2.5)
    EnableCharacter(2420712)
    EnableAI(2420712)
    ForceAnimation(2420712, 6200)
    EnableCharacter(2420719)
    EnableAI(2420719)
    ForceAnimation(2420719, 6200)


@NeverRestart(12421703)
def Event_12421703():
    """Event 12421703"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12424700)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12424700)
    EnableFlag(12421702)
    EnableCharacter(2420716)
    EnableAI(2420716)
    ForceAnimation(2420716, 6200)
    EnableCharacter(2420717)
    EnableAI(2420717)
    ForceAnimation(2420717, 6200)
    EnableCharacter(2420720)
    EnableAI(2420720)
    ForceAnimation(2420720, 6200)
    Wait(2.0)
    EnableCharacter(2420810)
    EnableAI(2420810)
    ForceAnimation(2420810, 6200)
    EnableCharacter(2420711)
    EnableAI(2420711)
    ForceAnimation(2420711, 6200)
    EnableCharacter(2420713)
    EnableAI(2420713)
    ForceAnimation(2420713, 6200)
    Wait(2.5)
    EnableCharacter(2420712)
    EnableAI(2420712)
    ForceAnimation(2420712, 6200)
    EnableCharacter(2420719)
    EnableAI(2420719)
    ForceAnimation(2420719, 6200)


@NeverRestart(12424710)
def Event_12424710():
    """Event 12424710"""
    EndIfFlagEnabled(12421700)
    GotoIfFlagEnabled(Label.L0, flag=12421702)
    SkipLinesIfClient(2)
    DisableObject(2421700)
    DeleteVFX(2423810, erase_root_only=False)
    DisableObject(2421701)
    DeleteVFX(2423811, erase_root_only=False)
    IfFlagDisabled(1, 12421700)
    IfFlagEnabled(1, 12421702)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2421700)
    EnableObject(2421701)
    CreateVFX(2423810)
    CreateVFX(2423811)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(1, 12421700)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2420700, entity=2421700)
    IfFlagEnabled(3, 12421700)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12424700)
    Restart()


@NeverRestart(12424711)
def Event_12424711():
    """Event 12424711"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421700)
    IfFlagDisabled(1, 12421700)
    IfFlagEnabled(1, 12424700)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2420700, entity=2421700)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2422811)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12424701)
    Restart()


@NeverRestart(12424712)
def Event_12424712():
    """Event 12424712"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2421700, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12424713)
def Event_12424713():
    """Event 12424713"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2421700, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2421700, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12424702)
def Event_12424702():
    """Event 12424702"""
    EndIfFlagEnabled(12421700)
    DisableAI(2420810)
    DisableAI(2420711)
    DisableAI(2420712)
    DisableAI(2420713)
    DisableAI(2420716)
    DisableAI(2420717)
    DisableAI(2420719)
    DisableAI(2420720)
    EnableImmortality(2420810)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12424700)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2800810, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800811, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12424700)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2800800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800803)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2800800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800803)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableBossHealthBar(2420810, name=257000)
    CreatePlayLog(name=104)
    StartPlayLogMeasurement(measurement_id=2800010, name=40, overwrite=True)
    EndIfFlagDisabled(12421702)
    IfCharacterInsideRegion(-1, PLAYER, region=2422817)
    IfAttackedWithDamageType(-1, attacked_entity=2420810, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420711, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420712, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420713, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420716, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420717, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420719, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=2420720, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2420810)
    EnableAI(2420711)
    EnableAI(2420712)
    EnableAI(2420713)
    EnableAI(2420716)
    EnableAI(2420717)
    EnableAI(2420719)
    EnableAI(2420720)


@NeverRestart(12424703)
def Event_12424703():
    """Event 12424703"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421700)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2703802)
    DisableSoundEvent(sound_id=2703803)
    IfFlagDisabled(1, 12421700)
    IfFlagEnabled(1, 12424702)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12424701)
    IfCharacterInsideRegion(1, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2423812)
    EnableFlag(12425246)
    IfFlagEnabled(0, 12424790)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12421700)
    IfFlagEnabled(2, 12424702)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12424701)
    IfCharacterInsideRegion(2, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2423812)
    EnableFlag(12425246)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2423813)


@NeverRestart(12424704)
def Event_12424704():
    """Event 12424704"""
    DisableNetworkSync()
    IfHealthGreaterThan(1, 2420811, value=0.0)
    IfHealthLessThanOrEqual(1, 2420811, value=0.6000000238418579)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2420811, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, 2420811, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=2420811, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart(12424705)
def Event_12424705():
    """Event 12424705"""
    DisableNetworkSync()
    EndIfFlagEnabled(12421700)
    IfFlagEnabled(0, 12421700)
    DisableBossMusic(sound_id=2423812)
    DisableBossMusic(sound_id=2423813)
    DisableBossMusic(sound_id=-1)
    DisableFlag(12425246)


@RestartOnRest(12424770)
def Event_12424770(_, character: int, character_1: int):
    """Event 12424770"""
    IfCharacterDead(1, 2420811)
    IfCharacterAlive(2, character)
    IfCharacterDead(3, character)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableImmortality(character_1)
    DisableSpawner(entity=character)
    Kill(character_1, award_souls=True)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    DisableCharacter(character)
    IfCharacterAlive(0, character_1)
    Restart()


@RestartOnRest(12424780)
def Event_12424780():
    """Event 12424780"""
    IfCharacterHasTAEEvent(0, 2420811, tae_event_id=40)
    AddSpecialEffect(2420711, 5530)
    AddSpecialEffect(2420712, 5530)
    AddSpecialEffect(2420713, 5530)
    AddSpecialEffect(2420716, 5530)
    AddSpecialEffect(2420717, 5530)
    AddSpecialEffect(2420719, 5530)
    AddSpecialEffect(2420720, 5530)
    Restart()


@RestartOnRest(12424785)
def Event_12424785(_, character: int, region: int, command_id: int, flag: int):
    """Event 12424785"""
    IfFlagEnabled(1, flag)
    IfCharacterOutsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12424787)
def Event_12424787(_, character: int, region: int, command_id: int, flag: int, character_1: int):
    """Event 12424787"""
    IfFlagEnabled(1, flag)
    IfHealthGreaterThan(1, character_1, value=0.6000000238418579)
    IfCharacterOutsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12424784)
def Event_12424784():
    """Event 12424784"""
    IfCharacterHasSpecialEffect(1, 2420811, 5609)
    IfCharacterOutsideRegion(1, 2420811, region=2422816)
    IfConditionTrue(0, input_condition=1)
    AICommand(2420811, command_id=20, command_slot=0)
    ReplanAI(2420811)
    IfCharacterInsideRegion(0, 2420811, region=2422722)
    AICommand(2420811, command_id=40, command_slot=0)
    ReplanAI(2420811)
    IfCharacterInsideRegion(0, PLAYER, region=2422816)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(2420811, command_id=-1, command_slot=0)
    ReplanAI(2420811)
    Restart()


@RestartOnRest(12424790)
def Event_12424790():
    """Event 12424790"""
    IfCharacterBackreadEnabled(0, 2420811)
    DisableAI(2420811)
    DisableGravity(2420811)
    DisableHealthBar(2420811)
    ReferDamageToEntity(2420810, target_entity=2420811)
    DisableGravity(2420750)
    DisableGravity(2420751)
    IfHealthLessThan(1, 2420810, value=0.6000000238418579)
    IfHealthGreaterThan(1, 2420811, value=0.0)
    IfConditionTrue(0, input_condition=1)
    SetNest(2420811, region=2422721)
    AICommand(2420810, command_id=40, command_slot=1)
    ReplanAI(2420810)
    IfCharacterHasTAEEvent(0, 2420810, tae_event_id=30)
    DisableBossHealthBar(2420810, name=257000)
    WaitFrames(frames=5)
    DisableCharacter(2420810)
    Move(
        2420811,
        destination=2420810,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=2420810,
    )
    EnableGravity(2420811)
    EnableAI(2420811)
    ForceAnimation(2420811, 3025, wait_for_completion=True)
    EnableBossHealthBar(2420811, name=257000)


@RestartOnRest(12424791)
def Event_12424791():
    """Event 12424791"""
    IfHealthLessThanOrEqual(0, 2420811, value=0.30000001192092896)
    SkipLinesIfThisEventFlagEnabled(1)
    WaitFrames(frames=135)
    Move(
        2420750,
        destination=2420811,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=2420811,
    )
    Move(
        2420751,
        destination=2420811,
        destination_type=CoordEntityType.Character,
        model_point=41,
        copy_draw_parent=2420811,
    )
    Restart()


@RestartOnRest(12424792)
def Event_12424792(_, character: int):
    """Event 12424792"""
    IfHealthLessThanOrEqual(0, 2420811, value=0.30000001192092896)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    WaitFrames(frames=145)
    ForceAnimation(character, 3000)
    IfCharacterHasSpecialEffect(0, 2420811, 5402)
    ForceAnimation(character, 3000)
    Wait(3.5)
    DisableCharacter(character)
    IfCharacterHasSpecialEffect(0, 2420811, 5400)
    Wait(1.5)
    EnableCharacter(character)
    ForceAnimation(character, 3000)
    Restart()


@RestartOnRest(12424795)
def Event_12424795():
    """Event 12424795"""
    IfCharacterHasSpecialEffect(1, 2420811, 5531)
    IfAttackedWithDamageType(1, attacked_entity=2420811, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2420811, 3030)
    WaitFrames(frames=59)
    ForceAnimation(2420811, 7000, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(frames=150)
    ForceAnimation(2420811, 3000, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()


@NeverRestart(12420000)
def Event_12420000(_, obj: int, animation_id: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12420000"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id_1)
    Wait(0.0)


@NeverRestart(12420030)
def Event_12420030(_, obj_act_id: int):
    """Event 12420030"""
    DisableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12420050)
def Event_12420050(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12420050"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(12420100)
def Event_12420100():
    """Event 12420100"""
    SkipLinesIfThisEventFlagDisabled(2)
    PostDestruction(2421850)
    End()
    IfObjectDestroyed(0, 2421850)
    EnableFlag(12420100)


@NeverRestart(12420123)
def Event_12420123():
    """Event 12420123"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2421200, animation_id=1)
    DisableObjectActivation(2421270, obj_act_id=2420000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12420122)
    ForceAnimation(2421200, 1)
    CreateObjectVFX(2421200, vfx_id=200, model_point=920204)
    CreateObjectVFX(2421200, vfx_id=201, model_point=920205)


@NeverRestart(12420124)
def Event_12420124():
    """Event 12420124"""
    DisableNetworkSync()
    EndIfFlagEnabled(12420123)
    IfActionButtonParamActivated(1, action_button_id=2420030, entity=2421200)
    IfActionButtonParamActivated(2, action_button_id=2420000, entity=2421200)
    IfObjectActivated(3, obj_act_id=12420122)
    IfFlagEnabled(4, 12420123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    EndIfFinishedConditionTrue(input_condition=4)
    DisplayDialog(text=10010160, anchor_entity=2421200, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()


@NeverRestart(12420130)
def Event_12420130(_, obj: int, animation_id: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12420130"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12420140)
def Event_12420140():
    """Event 12420140"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12420123)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421270)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()


@NeverRestart(12420150)
def Event_12420150():
    """Event 12420150"""
    IfFlagEnabled(1, 12420154)
    IfFlagDisabled(2, 12420154)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=2421250, animation_id=0)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    SkipLines(3)
    EndOfAnimation(obj=2421250, animation_id=8)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    DisableObjectActivation(2421252, obj_act_id=2420000)


@NeverRestart(12420151)
def Event_12420151():
    """Event 12420151"""
    IfFlagDisabled(3, 12420154)
    IfFlagEnabled(3, 12420155)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagDisabled(1, 12420154)
    IfFlagDisabled(1, 12420155)
    IfCharacterInsideRegion(1, PLAYER, region=2422651)
    IfFlagDisabled(2, 12420154)
    IfFlagDisabled(2, 12420155)
    IfObjectActivated(2, obj_act_id=12420124)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12420155)
    ForceAnimation(2421250, 1)
    ForceAnimation(2421250, 8)
    WaitFrames(frames=250)
    IfAllPlayersOutsideRegion(0, region=2422652)
    DisableObjectActivation(2421252, obj_act_id=2420000)
    ForceAnimation(2421250, 9)
    WaitFrames(frames=10)
    EnableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    Restart()


@NeverRestart(12420152)
def Event_12420152():
    """Event 12420152"""
    IfFlagEnabled(3, 12420154)
    IfFlagEnabled(3, 12420155)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(1, 12420154)
    IfFlagDisabled(1, 12420155)
    IfCharacterInsideRegion(1, PLAYER, region=2422652)
    IfFlagEnabled(2, 12420154)
    IfFlagDisabled(2, 12420155)
    IfObjectActivated(2, obj_act_id=12420123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12420155)
    ForceAnimation(2421250, 11)
    ForceAnimation(2421250, 12)
    WaitFrames(frames=250)
    IfAllPlayersOutsideRegion(0, region=2422651)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    ForceAnimation(2421250, 7)
    WaitFrames(frames=10)
    DisableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    Restart()


@NeverRestart(12420153)
def Event_12420153():
    """Event 12420153"""
    DisableNetworkSync()
    IfFlagDisabled(-1, 12420154)
    IfFlagEnabled(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421251)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12420156)
def Event_12420156():
    """Event 12420156"""
    DisableNetworkSync()
    IfFlagEnabled(-1, 12420154)
    IfFlagEnabled(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421252)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12420280)
def Event_12420280(_, region: int):
    """Event 12420280"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(12420285)
def Event_12420285(_, region: int, flag: int):
    """Event 12420285"""
    IfFlagEnabled(0, flag)
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(12420300)
def Event_12420300():
    """Event 12420300"""
    DisableNetworkSync()
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=2422681)
    PlaySoundEffect(2422680, 20011001, sound_type=SoundType.a_Ambient)
    EnableFlag(12420301)


@RestartOnRest(12420310)
def Event_12420310():
    """Event 12420310"""
    SkipLinesIfThisEventSlotFlagDisabled(5)
    EnableCharacter(2420205)
    DisableCharacter(2420204)
    Move(2420205, destination=2422205, destination_type=CoordEntityType.Region, short_move=True)
    PostDestruction(2421210)
    End()
    DisableAI(2420205)
    DisableGravity(2420205)
    DisableCharacterCollision(2420205)
    DisableCharacter(2420205)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 52420170)
    IfCharacterInsideRegion(1, PLAYER, region=2422660)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(2421121, 20011004, sound_type=SoundType.a_Ambient)
    EnableCharacter(2420205)
    ForceAnimation(2420205, 7004)
    WaitFrames(frames=10)
    DestroyObject(2421210)
    EnableGravity(2420205)
    EnableCharacterCollision(2420205)
    EnableAI(2420205)


@RestartOnRest(12420320)
def Event_12420320():
    """Event 12420320"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableObject(2421300)
    Move(2420200, destination=2422200, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    Move(2420201, destination=2422201, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    Move(2420202, destination=2422202, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    SetNest(2420200, region=2422200)
    SetNest(2420201, region=2422201)
    SetNest(2420202, region=2422202)
    PostDestruction(2421301)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(2421301)
    DisableCharacter(2420200)
    DisableAI(2420200)
    DisableGravity(2420200)
    DisableAI(2420201)
    DisableGravity(2420201)
    ForceAnimation(2420201, 7011, loop=True)
    DisableAI(2420202)
    DisableGravity(2420202)
    ForceAnimation(2420202, 7012, loop=True)
    CreateObjectVFX(2421300, vfx_id=100, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=101, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=102, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=103, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=104, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=105, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=106, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=107, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=108, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=109, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=110, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=111, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=112, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=113, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=114, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=115, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=116, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=117, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=118, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=119, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=120, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=121, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=122, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=123, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=124, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=125, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=126, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=127, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=128, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=129, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=130, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=131, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=132, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=133, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=134, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=135, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=136, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=137, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=138, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=139, model_point=924500)
    CreateObjectVFX(2421300, vfx_id=201, model_point=924501)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2422653)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2420200)
    ForceAnimation(2420200, 7007)
    ForceAnimation(2420201, 7008)
    ForceAnimation(2420202, 7009)
    ForceAnimation(2421300, 1)
    WaitFrames(frames=81)
    DeleteObjectVFX(2421300, erase_root=False)
    CreateObjectVFX(2421300, vfx_id=201, model_point=924502)
    WaitFrames(frames=32)
    CreateObjectVFX(2421300, vfx_id=201, model_point=924503)
    DisableObject(2421300)
    EnableObject(2421301)
    DestroyObject(2421301)
    EnableAI(2420200)
    EnableGravity(2420200)
    SetNest(2420200, region=2422200)
    EnableAI(2420201)
    EnableGravity(2420201)
    SetNest(2420201, region=2422201)
    EnableAI(2420202)
    EnableGravity(2420202)
    SetNest(2420202, region=2422202)
    Wait(10.0)
    SetAIParamID(2420200, ai_param_id=100000)
    SetAIParamID(2420201, ai_param_id=100000)
    SetAIParamID(2420202, ai_param_id=100000)


@NeverRestart(12420400)
def Event_12420400():
    """Event 12420400"""
    GotoIfFlagEnabled(Label.L3, flag=9802)
    GotoIfFlagEnabled(Label.L2, flag=9801)
    GotoIfFlagEnabled(Label.L1, flag=9800)
    GotoIfFlagDisabled(Label.L0, flag=9800)

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)
    EnableMapPiece(map_piece_id=2424000)
    DisableMapPiece(map_piece_id=2424010)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableMapPiece(map_piece_id=2424000)
    EnableMapPiece(map_piece_id=2424010)


@NeverRestart(12420500)
def Event_12420500():
    """Event 12420500"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72500326)
    IfFlagEnabled(0, 72500326)
    DisableFlagRange((72500304, 72500309))
    EnableFlag(72500328)
    RemoveGoodFromPlayer(item=4305, quantity=1)
    PlayCutscene(24020000, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=10)
    DisableFlag(72500339)
    SaveRequest()
    Restart()


@RestartOnRest(12420850)
def Event_12420850(
    _,
    vfx_id: int,
    vfx_id_1: int,
    vfx_id_2: int,
    flag: int,
    obj_act_id: int,
    seconds: float,
    anchor_entity: int,
    vfx_id_3: int,
):
    """Event 12420850"""
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    DeleteVFX(vfx_id_2, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, flag)
    CreateVFX(vfx_id_1)
    CreateVFX(vfx_id_2)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(seconds)
    CreateVFX(vfx_id)
    CreateTemporaryVFX(vfx_id=vfx_id_3, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    CreateVFX(vfx_id_1)
    CreateVFX(vfx_id_2)


@RestartOnRest(12420853)
def Event_12420853():
    """Event 12420853"""
    DeleteVFX(2427031, erase_root_only=False)
    DeleteVFX(2427032, erase_root_only=False)
    DeleteVFX(2427033, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, 12420133)
    CreateVFX(2427032)
    CreateVFX(2427033)
    End()
    IfObjectActivated(0, obj_act_id=12420112)
    Wait(6.0)
    CreateVFX(2427031)
    CreateTemporaryVFX(vfx_id=920206, anchor_entity=2421204, model_point=200, anchor_type=CoordEntityType.Object)
    CreateTemporaryVFX(vfx_id=920207, anchor_entity=2421204, model_point=242, anchor_type=CoordEntityType.Object)
    Wait(4.0)
    CreateVFX(2427032)
    CreateVFX(2427033)


@RestartOnRest(12420854)
def Event_12420854():
    """Event 12420854"""
    DeleteVFX(2427023, erase_root_only=False)
    DeleteVFX(2427024, erase_root_only=False)
    SkipLinesIfFlagDisabled(2, 12420310)
    CreateVFX(2427024)
    End()
    IfFlagEnabled(0, 12420310)
    Wait(1.0)
    CreateVFX(2427023)
    Wait(4.0)
    CreateVFX(2427024)


@RestartOnRest(12425200)
def Event_12425200(_, character: int):
    """Event 12425200"""
    ForceAnimation(character, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfEntityWithinDistance(2, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(3, PLAYER, region=2422661)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, condition=3)
    ForceAnimation(character, 7001)
    ReplanAI(character)
    End()
    ForceAnimation(character, 7001)
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=2422262)
    ReplanAI(character)
    IfAttacked(-3, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(-3, character, region=2422262)
    IfConditionTrue(0, input_condition=-3)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12425210)
def Event_12425210(_, character: int):
    """Event 12425210"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7001)
    ReplanAI(character)


@RestartOnRest(12425221)
def Event_12425221(_, character: int):
    """Event 12425221"""
    IfCharacterInsideRegion(0, character, region=2422655)
    ChangePatrolBehavior(character, patrol_information_id=2423210)


@RestartOnRest(12425250)
def Event_12425250(
    _,
    character: int,
    seconds: float,
    region: int,
    radius: float,
    region_1: int,
    command_id: int,
    right: int,
    line_count: uchar,
):
    """Event 12425250"""
    IfCharacterBackreadEnabled(0, character)
    Wait(1.0)
    SetNest(character, region=region_1)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)
    Wait(seconds)
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfCharacterInsideRegion(-4, PLAYER, region=region)
    IfEntityWithinDistance(-4, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    SkipLinesIfNotEqual(line_count, left=0, right=right)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12425225)
def Event_12425225():
    """Event 12425225"""
    EndIfThisEventFlagEnabled()
    ForceAnimation(2420253, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=2422253)
    IfEntityWithinDistance(-2, entity=2420253, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2420253)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2420253, 7001)
    ReplanAI(2420253)


@RestartOnRest(12425245)
def Event_12425245():
    """Event 12425245"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=2423600)
    IfInsideMap(1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagDisabled(1, 12425246)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=2423600)
    IfOutsideMap(-1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagEnabled(-1, 12425246)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(sound_id=2423600)
    Restart()


@RestartOnRest(12425290)
def Event_12425290():
    """Event 12425290"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountGreaterThanOrEqual(2, value=10)
    EndIfConditionFalse(2)
    EnableFlag(12425291)


@RestartOnRest(12425300)
def Event_12425300(_, character: int):
    """Event 12425300"""
    IfFlagEnabled(-1, 12425291)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    SetDisplayMask(character, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, 5696)


@RestartOnRest(12425305)
def Event_12425305(_, character: int):
    """Event 12425305"""
    IfFlagEnabled(-1, 12425291)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(character, 5552)
    AddSpecialEffect(character, 5553)
    AddSpecialEffect(character, 5554)


@RestartOnRest(12425310)
def Event_12425310(_, character: int):
    """Event 12425310"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 7018, loop=True)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(character, 7019)
    ReplanAI(character)


@RestartOnRest(12425320)
def Event_12425320(_, character: int, animation_id: int, animation_id_1: int, region: int):
    """Event 12425320"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    Wait(1.0)
    SetNest(character, region=region)
    IfCharacterInsideRegion(1, character, region=region)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Normal)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    ForceAnimation(character, animation_id_1, loop=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 0)
    Restart()


@RestartOnRest(12425350)
def Event_12425350(_, character: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12425350"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ReplanAI(character)


@RestartOnRest(12425500)
def Event_12425500(_, character: int, radius: float, right: int, region: int, seconds: float):
    """Event 12425500"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    Wait(seconds)
    DisableAI(character)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    SkipLinesIfNotEqual(3, left=1, right=right)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(12425600)
def Event_12425600():
    """Event 12425600"""
    EndIfThisEventFlagEnabled()
    IfCharacterBackreadEnabled(1, 2420401)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    DisableAI(2420401)
    DisableAI(2420402)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfEntityWithinDistance(-3, entity=PLAYER, other_entity=2420401, radius=5.0)
    IfEntityWithinDistance(-3, entity=PLAYER, other_entity=2420402, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=2422685)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfAttacked(-1, attacked_entity=2420401, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=2420402, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2420401)
    ReplanAI(2420401)
    Wait(3.0)
    EnableAI(2420402)
    ReplanAI(2420402)


@NeverRestart(12425601)
def Event_12425601():
    """Event 12425601"""
    DisableNetworkSync()
    IfCharacterAlive(1, 2420402)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    Move(2420731, destination=2420402, destination_type=CoordEntityType.Character, model_point=40, short_move=True)
    Restart()


@RestartOnRest(12425602)
def Event_12425602():
    """Event 12425602"""
    IfHealthLessThanOrEqual(0, 2420402, value=0.0)
    Wait(1.0)
    ForceAnimation(2420731, 2200, wait_for_completion=True)
    DisableCharacter(2420731)


@NeverRestart(12425603)
def Event_12425603():
    """Event 12425603"""
    AddSpecialEffect(2420402, 5609)
    DisableGravity(2420731)


@RestartOnRest(12425400)
def Event_12425400(_, attacked_entity: int, region: int, animation_id: int):
    """Event 12425400"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(2, attacked_entity=attacked_entity, attacker=PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(attacked_entity, animation_id)


@NeverRestart(12420990)
def Event_12420990():
    """Event 12420990"""
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfPlayerStandingOnCollision(0, 2423500)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    AwardAchievement(achievement_id=11)


@RestartOnRest(12424450)
def Event_12424450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12424450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12424400)
def Event_12424400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12424400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12424410)
def Event_12424410(
    _,
    sign_type: int,
    character: int,
    region: int,
    summon_flag: int,
    dismissal_flag: int,
    flag: int,
    flag_1: int,
    action_button_id: int,
):
    """Event 12424410"""
    SkipLinesIfFlagEnabled(1, summon_flag)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    IfClient(1)
    IfFlagEnabled(1, summon_flag)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(character)
    EndIfFlagEnabled(flag_1)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, summon_flag)
    IfFlagDisabled(2, dismissal_flag)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest(12424460)
def Event_12424460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12424460"""
    EndIfClient()
    IfFlagEnabled(1, flag)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    IfCharacterInsideRegion(2, character, region=region_2)
    RestartIfConditionFalse(2)
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(0, character, region=region_3)
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
