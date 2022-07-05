"""UPPER CATHEDRAL WARD

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
from .common_entities import *
from .m24_02_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=20, args=(2420950, 2421950, 999, 12427800))
    RunEvent(7000, slot=21, args=(2420951, 2421951, Flags.EbrietasDead, 12427820))
    RunEvent(7000, slot=22, args=(2420952, 2421952, Flags.CelestialEmissaryDead, 12427840))
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
    RunEvent(12424400, slot=0, args=(12424440, 2423910, 12424420, 12424430, Flags.EbrietasDead, 6001))
    RunEvent(12424410, slot=0, args=(0, 2420910, 2422910, 12424420, 12424430, 12424440, Flags.EbrietasDead, 10566))
    RunEvent(12424450, slot=0, args=(2420910, 2422911, 12424420, 12424430, Flags.EbrietasFogEntered))
    RunEvent(12424460, slot=0, args=(2420910, 2422911, 2422800, 2422801, 101130, 12424450, 2422801))
    RunEvent(9200, slot=4, args=(2423900,))
    RunEvent(9220, slot=4, args=(2420710, 12424220, 12424221, 2420, 24, 2), arg_types="iiiiBB")
    RunEvent(9240, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types="iiiiBB")
    RunEvent(9260, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types="iiiiBB")
    RunEvent(9280, slot=4, args=(2420710, 12424220, 12424221, 2420, Flags.CelestialEmissaryFogEntered, 24, 2),
             arg_types="iiiiiBB")
    StartPlayLogMeasurement(2420000, 0, overwrite=True)
    StartPlayLogMeasurement(2420001, 18, overwrite=True)
    Event12420990()
    Event12420400()
    RunEvent(7600, slot=40, args=(2421999, 2423999))
    RunEvent(7600, slot=41, args=(2421998, 2423998))
    CreateHazard(
        12420020,
        2421230,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    Event12420123()
    Event12420124()
    Event12420140()
    Event12420150()
    Event12420151()
    Event12420152()
    Event12420153()
    Event12420156()
    RunEvent(
        12420850,
        slot=0,
        args=(2427020, 2427021, 2427022, 12420130, 12420102, 2.0, 2427000, 920200),
        arg_types="iiiiifii",
    )
    RunEvent(
        12420850,
        slot=1,
        args=(2427025, 2427026, 2427027, 12420132, 12420110, 3.0, 2427017, 920202),
        arg_types="iiiiifii",
    )
    RunEvent(
        12420850,
        slot=2,
        args=(2427028, 2427029, 2427030, 12420131, 12420111, 3.0, 2427016, 920203),
        arg_types="iiiiifii",
    )
    Event12420853()
    Event12420854()
    RunEvent(12420280, slot=0, args=(2422500,))
    RunEvent(12420280, slot=1, args=(2422501,))
    RunEvent(12420285, slot=0, args=(2422502, 12420032))
    RunEvent(12420285, slot=1, args=(2422503, 12420033))
    RunEvent(12420000, slot=0, args=(2421201, 1, 2420020, 12420120))
    RunEvent(12420000, slot=1, args=(2421223, 1, 2420030, 12420121))
    RunEvent(12420030, slot=0, args=(12420120,))
    RunEvent(12420030, slot=2, args=(12420126,))
    RunEvent(12420030, slot=3, args=(12420127,))
    RunEvent(12420050, slot=0, args=(2421100, 12421000, 9942))
    RunEvent(12420050, slot=1, args=(2421101, 12421001, 9942))
    DisableSoundEvent(2423802)
    DisableSoundEvent(2423803)
    DisableSoundEvent(2423812)
    DisableSoundEvent(2423813)
    CreateProjectileOwner(2420801)

    # EBRIETAS, DAUGHTER OF THE COSMOS
    Event12424812()
    Event12424813()
    EbrietasDies()
    Event12421801()
    EbrietasFirstTime()
    EnterEbrietasFog()
    EnterEbrietasFogAsSummon()
    StartEbrietasBattle()
    ControlEbrietasMusic()
    ControlEbrietasCamera()
    StopEbrietasMusic()
    EbrietasPhaseTwoTrigger()
    DismissEbrietasStarsOnDeath()
    SummonStartEbrietasBattle()
    EbrietasHeadDamage(0, 2420, 2420, 5, 200, 480, 490, 8040)
    EbrietasLimbDamage(0, 2421, 2421, 1, 200, 481, 491, 8010)
    EbrietasLimbDamage(1, 2422, 2422, 2, 200, 482, 492, 8000)
    EbrietasLimbDamage(2, 2423, 2423, 3, 200, 483, 493, 8030)
    EbrietasLimbDamage(3, 2424, 2424, 4, 200, 484, 494, 8020)

    # CELESTIAL EMISSARY
    Event12424712()
    Event12424713()
    CelestialEmissaryDies()
    PlayCelestialEmissaryDeathSound()
    CelestialEmissaryFirstTime()
    EnterCelestialEmissaryFog()
    EnterCelestialEmissaryFogAsSummon()
    StartCelestialEmissaryBattle()
    ControlCelestialEmissaryMusic()
    ControlCelestialEmissaryCamera()
    StopCelestialEmissaryMusic()
    CelestialEmissaryPhaseTwoTrigger()
    ApplyCelestialEmissaryAura()
    ControlCelestialEmissaryTendrils()
    CelestialEmissaryTendrilAttack(0, 2420750)
    CelestialEmissaryTendrilAttack(1, 2420751)
    SummonStartCelestialEmissaryBattle()
    # Haven't translated the rest of these Celestial Emissary events yet. Mostly character control.
    RunEvent(12424785, slot=0, args=(Characters.CelestialEmissarySmall, 2422816, 10, Flags.CelestialEmissaryBattleStarted))
    RunEvent(12424785, slot=1, args=(Characters.CelestialEmissaryGiant, 2422817, 20, Flags.CelestialEmissaryPhaseTwo))
    Event12424784()
    RunEvent(12424787, slot=0, args=(Characters.CelestialMinion1, 2422816, 10, Flags.CelestialEmissaryBattleStarted, Characters.CelestialEmissarySmall))
    RunEvent(12424787, slot=1, args=(Characters.CelestialMinion2, 2422816, 10, Flags.CelestialEmissaryBattleStarted, Characters.CelestialEmissarySmall))
    Event12424795()
    RunEvent(12424770, slot=0, args=(2423711, Characters.CelestialMinion1))
    RunEvent(12424770, slot=1, args=(2423712, Characters.CelestialMinion2))
    RunEvent(12424770, slot=2, args=(2423713, Characters.CelestialMinion3))
    RunEvent(12424770, slot=5, args=(2423716, Characters.CelestialMinion4))
    RunEvent(12424770, slot=6, args=(2423717, Characters.CelestialMinion5))
    RunEvent(12424770, slot=8, args=(2423719, Characters.CelestialMinion6))
    RunEvent(12424770, slot=9, args=(2423720, Characters.CelestialMinion7))
    RunEvent(12424770, slot=12, args=(2423720, Characters.CelestialEmissarySmall))

    # --- 1 --- #
    DefineLabel(1)
    Event12420300()
    Event12420320()
    Event12420310()
    RunEvent(12425200, slot=0, args=(2420262,))
    RunEvent(12425210, slot=0, args=(2420250,))
    RunEvent(12425210, slot=1, args=(2420258,))
    RunEvent(12425210, slot=2, args=(2420267,))
    Event12425225()
    RunEvent(12425221, slot=0, args=(2420256,))
    RunEvent(12425250, slot=0, args=(2420252, 1.5, 2422659, 9.0, 2422252, 20, 1, 1), arg_types="ififiiiB")
    Event12425245()
    DisableFlag(12425246)
    RunEvent(12425300, slot=0, args=(2420451,))
    RunEvent(12425305, slot=0, args=(2420452,))
    RunEvent(12425310, slot=0, args=(2420352,))
    RunEvent(12425310, slot=1, args=(2420375,))
    RunEvent(12425310, slot=2, args=(2420376,))
    RunEvent(12425310, slot=3, args=(2420387,))
    RunEvent(12425310, slot=4, args=(2420388,))
    RunEvent(12425320, slot=0, args=(2420380, 7012, 7013, 2422380))
    RunEvent(12425320, slot=1, args=(2420381, 7012, 7013, 2422381))
    RunEvent(12425320, slot=2, args=(2420382, 7012, 7013, 2422382))
    RunEvent(12425320, slot=3, args=(2420383, 7012, 7013, 2422383))
    RunEvent(12425320, slot=4, args=(2420384, 7012, 7013, 2422384))
    RunEvent(12425320, slot=5, args=(2420350, 7012, 7013, 2422350))
    RunEvent(12425320, slot=6, args=(2420351, 7012, 7013, 2422351))
    RunEvent(12425320, slot=7, args=(2420377, 7012, 7013, 2422377))
    RunEvent(12425320, slot=8, args=(2420357, 7012, 7013, 2422357))
    RunEvent(12425320, slot=9, args=(2420358, 7012, 7013, 2422358))
    RunEvent(12425320, slot=10, args=(2420359, 7012, 7013, 2422359))
    RunEvent(12425320, slot=11, args=(2420363, 7012, 7013, 2422363))
    RunEvent(12425320, slot=12, args=(2420364, 7012, 7013, 2422364))
    RunEvent(12425320, slot=13, args=(2420385, 7012, 7013, 2422385))
    RunEvent(12425320, slot=14, args=(2420386, 7012, 7013, 2422386))
    SetNetworkUpdateRate(Characters.CelestialEmissaryGiant, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RunEvent(12425500, slot=0, args=(2420357, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=1, args=(2420358, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=2, args=(2420359, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=3, args=(2420363, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=4, args=(2420364, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=5, args=(2420251, 5.0, 1, 2422251, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=6, args=(2420255, 3.0, 1, 2422254, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=7, args=(2420255, 3.0, 1, 2422255, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=8, args=(2420256, 5.0, 1, 2422256, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=9, args=(2420377, 5.0, 1, 2422656, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=10, args=(2420351, 5.0, 1, 2422656, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=11, args=(2420385, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=12, args=(2420386, 5.0, 1, 2422650, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=13, args=(2420259, 5.0, 1, 2422259, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=14, args=(2420350, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=15, args=(2420380, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=16, args=(2420381, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=17, args=(2420382, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=18, args=(2420383, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=19, args=(2420384, 5.0, 1, 2422654, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=20, args=(2420203, 5.0, 1, 2422653, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=21, args=(2420264, 2.0, 1, 2422264, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=22, args=(2420400, 5.0, 1, 2422256, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=23, args=(2420450, 5.0, 1, 2422300, 0.0), arg_types="ifiif")
    RunEvent(12425500, slot=24, args=(2420451, 5.0, 1, 2422300, 0.0), arg_types="ifiif")
    Event12425600()
    Event12425601()
    Event12425602()
    Event12425603()
    RunEvent(12425350, slot=0, args=(2420350, 252002, 252000))
    RunEvent(12425350, slot=1, args=(2420351, 252002, 252000))
    RunEvent(12425350, slot=2, args=(2420377, 252002, 252000))
    RunEvent(12425350, slot=3, args=(2420380, 252002, 252000))
    RunEvent(12425350, slot=4, args=(2420381, 252002, 252000))
    RunEvent(12425350, slot=5, args=(2420382, 252002, 252000))
    RunEvent(12425350, slot=6, args=(2420383, 252002, 252000))
    RunEvent(12425350, slot=7, args=(2420384, 252002, 252000))
    RunEvent(12425400, slot=0, args=(2420263, 2422265, 3000))
    RunEvent(12425400, slot=1, args=(2420392, 2422686, 3004))
    Event12420100()
    RegisterLadder(start_climbing_flag=12420600, stop_climbing_flag=12420601, obj=2421600)
    Event12420500()
    Event12420700()
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6648)
    EnableFlag(12421999)
    SkipLinesIfFlagEnabled(5, 12421999)
    EnableObject(2421102)
    DisableObject(2421103)
    EnableTreasure(2421102)
    DisableTreasure(2421103)
    SkipLines(4)
    DisableObject(2421102)
    EnableObject(2421103)
    DisableTreasure(2421102)
    EnableTreasure(2421103)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6313)
    EnableFlag(12421998)
    SkipLinesIfFlagEnabled(5, 12421998)
    EnableObject(2421500)
    DisableObject(2421501)
    EnableTreasure(2421500)
    DisableTreasure(2421501)
    SkipLines(4)
    DisableObject(2421500)
    EnableObject(2421501)
    DisableTreasure(2421500)
    EnableTreasure(2421501)


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2423950)
    DisableGravity(2423950)
    DisableCharacterCollision(2423950)
    DisableAnimations(2423951)
    DisableGravity(2423951)
    DisableCharacterCollision(2423951)
    DisableAnimations(2423952)
    DisableGravity(2423952)
    DisableCharacterCollision(2423952)
    Event12425290()


@RestartOnRest
def Event12420700():
    """ 12420700: Event 12420700 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(0, 2420268)
    AwardItemLot(2420900, host_only=False)


def EbrietasDies():
    """ 12421800: Ebrietas, Daughter of the Cosmos is defeated. """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2423802)
    DisableSoundEvent(2423803)
    DisableCharacter(Characters.Ebrietas)
    Kill(Characters.Ebrietas, award_souls=False)
    DisableObject(Objects.EbrietasFog)
    DeleteVFX(VFX.EbrietasFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.Ebrietas)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.EbrietasFog)
    DeleteVFX(VFX.EbrietasFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.Ebrietas)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    AwardAchievement(28)
    AwardItemLot(80000300, host_only=False)
    EnableFlag(2421)
    EnableFlag(9459)
    StartPlayLogMeasurement(2420000, 0, overwrite=False)
    StartPlayLogMeasurement(2420001, 18, overwrite=False)
    StartPlayLogMeasurement(2420010, 40, overwrite=False)
    CreatePlayLog(58)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 70, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event12421801():
    """ 12421801: Event 12421801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    IfFlagEnabled(1, Flags.EbrietasDead)
    IfCharacterBackreadDisabled(2, Characters.Ebrietas)
    IfHealthLessThanOrEqual(2, Characters.Ebrietas, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2422800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


def EbrietasFirstTime():
    """ 12421802: Event 12421802 """
    EndIfFlagEnabled(Flags.EbrietasDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    Move(Characters.Ebrietas, destination=2422800, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(Characters.Ebrietas, 2422804, animation=-1, wait_for_completion=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.Ebrietas, 7001, loop=True)
    EnableImmortality(Characters.Ebrietas)
    AddSpecialEffect(Characters.Ebrietas, 5647, affect_npc_part_hp=False)
    IfFlagDisabled(1, Flags.EbrietasDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=Characters.Ebrietas, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.Ebrietas, 7000, wait_for_completion=True)
    DisableImmortality(Characters.Ebrietas)
    CancelSpecialEffect(Characters.Ebrietas, 5647)
    EnableFlag(Flags.EbrietasFogEntered)
    EndIfFlagEnabled(9304)
    RunEvent(9350, 0, args=(3,))
    EnableFlag(9304)


def SummonStartEbrietasBattle():
    """ 12421803: Event 12421803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.EbrietasFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(Flags.EbrietasFogEntered)
    EnableFlag(Flags.EbrietasFirstTimeDone)


def EnterEbrietasFog():
    """ 12424810: Event 12424810 """
    EndIfFlagEnabled(Flags.EbrietasDead)
    GotoIfFlagEnabled(Label.L0, Flags.EbrietasFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.EbrietasFog)
    DeleteVFX(VFX.EbrietasFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.EbrietasDead)
    IfFlagEnabled(1, Flags.EbrietasFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.EbrietasFog)
    CreateVFX(VFX.EbrietasFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.EbrietasDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2420800, entity=Objects.EbrietasFog)
    IfFlagEnabled(3, Flags.EbrietasDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.EbrietasFogEntered)
    Restart()


def EnterEbrietasFogAsSummon():
    """ 12424811: Event 12424811 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    IfFlagDisabled(1, Flags.EbrietasDead)
    IfFlagEnabled(1, Flags.EbrietasFirstTimeDone)
    IfFlagEnabled(1, Flags.EbrietasFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2420800, entity=Objects.EbrietasFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2422801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12424801)
    Restart()


def Event12424812():
    """ 12424812: Event 12424812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.EbrietasFog, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12424813():
    """ 12424813: Event 12424813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.EbrietasFog, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.EbrietasFog, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartEbrietasBattle():
    """ 12424802: Event 12424802 """
    EndIfFlagEnabled(Flags.EbrietasDead)
    DisableAI(Characters.Ebrietas)
    DisableHealthBar(Characters.Ebrietas)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.EbrietasFogEntered)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.Ebrietas, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.EbrietasFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.Ebrietas, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Ebrietas)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.Ebrietas, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Ebrietas)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.Ebrietas)
    EnableBossHealthBar(Characters.Ebrietas, name=251000, slot=0)
    CreatePlayLog(104)
    StartPlayLogMeasurement(2420010, 40, overwrite=True)


def ControlEbrietasMusic():
    """ 12424803: Event 12424803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2423802)
    DisableSoundEvent(2423803)
    IfFlagDisabled(1, Flags.EbrietasDead)
    IfFlagEnabled(1, Flags.EbrietasBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12424801)
    IfCharacterInsideRegion(1, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2423802)
    EnableFlag(12425246)
    IfCharacterHasTAEEvent(2, Characters.Ebrietas, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.EbrietasDead)
    IfFlagEnabled(2, Flags.EbrietasBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12424801)
    IfCharacterInsideRegion(2, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2423802)
    EnableFlag(12425246)
    WaitFrames(0)
    EnableBossMusic(2423803)


def ControlEbrietasCamera():
    """ 12424804: Event 12424804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    IfCharacterHasTAEEvent(0, Characters.Ebrietas, tae_event_id=10)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfCharacterHasTAEEvent(0, Characters.Ebrietas, tae_event_id=20)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


def StopEbrietasMusic():
    """ 12424805: Event 12424805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    IfFlagEnabled(0, Flags.EbrietasDead)
    DisableBossMusic(2423802)
    DisableBossMusic(2423803)
    DisableBossMusic(-1)
    DisableFlag(12425246)


@RestartOnRest
def EbrietasHeadDamage(
    _, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12424870: Event 12424870 """
    CreateNPCPart(
        Characters.Ebrietas,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=2.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.Ebrietas, npc_part_id=arg_4_7, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.Ebrietas, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, Characters.Ebrietas, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        Characters.Ebrietas,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=2.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.Ebrietas, npc_part_id=arg_4_7, material_sfx_id=75, material_vfx_id=75)
    ResetAnimation(Characters.Ebrietas, disable_interpolation=False)
    ForceAnimation(Characters.Ebrietas, arg_24_27)
    AddSpecialEffect(Characters.Ebrietas, arg_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.Ebrietas, arg_20_23)
    ReplanAI(Characters.Ebrietas)
    IfCharacterHasTAEEvent(0, Characters.Ebrietas, tae_event_id=100)
    SetNPCPartHealth(Characters.Ebrietas, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.Ebrietas, arg_20_23, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.Ebrietas, arg_16_19)
    AICommand(Characters.Ebrietas, command_id=-1, slot=0)
    ReplanAI(Characters.Ebrietas)
    WaitFrames(10)
    Restart()


@RestartOnRest
def EbrietasLimbDamage(
    _, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12424871: Event 12424871 """
    CreateNPCPart(
        Characters.Ebrietas,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.Ebrietas, npc_part_id=arg_4_7, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.Ebrietas, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, Characters.Ebrietas, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        Characters.Ebrietas,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.Ebrietas, npc_part_id=arg_4_7, material_sfx_id=74, material_vfx_id=74)
    ResetAnimation(Characters.Ebrietas, disable_interpolation=False)
    ForceAnimation(Characters.Ebrietas, arg_24_27)
    AddSpecialEffect(Characters.Ebrietas, arg_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.Ebrietas, arg_20_23)
    ReplanAI(Characters.Ebrietas)
    IfCharacterHasTAEEvent(0, Characters.Ebrietas, tae_event_id=100)
    SetNPCPartHealth(Characters.Ebrietas, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.Ebrietas, arg_20_23, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.Ebrietas, arg_16_19)
    AICommand(Characters.Ebrietas, command_id=-1, slot=0)
    ReplanAI(Characters.Ebrietas)
    WaitFrames(10)
    Restart()


def EbrietasPhaseTwoTrigger():
    """ 12424980: Event 12424980 """
    WaitFrames(1)
    IfCharacterDead(1, Characters.Ebrietas)
    EndIfConditionTrue(1)
    IfFlagEnabled(2, Flags.EbrietasFogEntered)
    IfHealthLessThan(2, Characters.Ebrietas, 0.5)
    IfConditionTrue(0, input_condition=2)
    AICommand(Characters.Ebrietas, command_id=100, slot=0)
    ReplanAI(Characters.Ebrietas)
    IfCharacterHasTAEEvent(0, Characters.Ebrietas, tae_event_id=500)
    AICommand(Characters.Ebrietas, command_id=-1, slot=0)
    ReplanAI(Characters.Ebrietas)


def DismissEbrietasStarsOnDeath():
    """ 12424990: Event 12424990 """
    IfCharacterHasSpecialEffect(1, Characters.Ebrietas, Effects.EbrietasStarsActive)
    IfHealthValueLessThan(1, Characters.Ebrietas, 0)
    IfConditionTrue(0, input_condition=1)
    ShootProjectile(
        owner_entity=2420801,
        projectile_id=Characters.Ebrietas,
        model_point=6,
        behavior_id=225100310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    Restart()


def CelestialEmissaryDies():
    """ 12421700: Event 12421700 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2423812)
    DisableSoundEvent(2423813)
    DisableCharacter(Characters.CelestialEmissarySmall)
    Kill(Characters.CelestialEmissarySmall, award_souls=False)
    DisableCharacter(Characters.CelestialMinion1)
    DisableCharacter(Characters.CelestialMinion2)
    DisableCharacter(Characters.CelestialMinion3)
    DisableCharacter(Characters.CelestialMinion4)
    DisableCharacter(Characters.CelestialMinion5)
    DisableCharacter(Characters.CelestialMinion6)
    DisableCharacter(Characters.CelestialMinion7)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    DisableAI(Characters.CelestialMinion1)
    DisableAI(Characters.CelestialMinion2)
    DisableAI(Characters.CelestialMinion3)
    DisableAI(Characters.CelestialMinion4)
    DisableAI(Characters.CelestialMinion5)
    DisableAI(Characters.CelestialMinion6)
    DisableAI(Characters.CelestialMinion7)
    DisableObject(Objects.CelestialEmissaryFog)
    DisableObject(Objects.CelestialEmissaryExitFog)
    DeleteVFX(VFX.CelestialEmissaryEntranceFog, erase_root_only=False)
    DeleteVFX(VFX.CelestialEmissaryExitFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.CelestialEmissaryGiant)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.CelestialEmissaryFog)
    DisableObject(Objects.CelestialEmissaryExitFog)
    DeleteVFX(VFX.CelestialEmissaryEntranceFog, erase_root_only=True)
    DeleteVFX(VFX.CelestialEmissaryExitFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    Wait(3.0)
    KillBoss(Characters.CelestialEmissaryGiant)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(2,))
    AwardAchievement(27)
    SkipLinesIfFlagEnabled(2, 6332)
    AwardItemLot(25700000, host_only=False)
    SkipLines(1)
    AwardItemLot(25700005, host_only=False)
    EnableFlag(2420)
    EnableFlag(9458)
    StartPlayLogMeasurement(2420000, 0, overwrite=False)
    StartPlayLogMeasurement(2420001, 18, overwrite=False)
    StartPlayLogMeasurement(2420010, 40, overwrite=False)
    CreatePlayLog(58)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 120, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayCelestialEmissaryDeathSound():
    """ 12421701: Event 12421701 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.EbrietasDead)
    IfFlagEnabled(1, Flags.EbrietasDead)
    IfCharacterBackreadDisabled(2, Characters.Ebrietas)
    IfHealthLessThanOrEqual(2, Characters.Ebrietas, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2422800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


def CelestialEmissaryFirstTime():
    """ 12421702: Event 12421702 """
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    EndIfThisEventFlagEnabled()
    DisableCharacter(Characters.CelestialEmissarySmall)
    DisableCharacter(Characters.CelestialMinion1)
    DisableCharacter(Characters.CelestialMinion2)
    DisableCharacter(Characters.CelestialMinion3)
    DisableCharacter(Characters.CelestialMinion4)
    DisableCharacter(Characters.CelestialMinion5)
    DisableCharacter(Characters.CelestialMinion6)
    DisableCharacter(Characters.CelestialMinion7)
    IfFlagDisabled(1, Flags.CelestialEmissaryDead)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2422815)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(Flags.CelestialEmissaryFogEntered)
    EnableFlag(Flags.CelestialEmissaryFirstTimeDone)
    EnableCharacter(Characters.CelestialMinion4)
    EnableAI(Characters.CelestialMinion4)
    ForceAnimation(Characters.CelestialMinion4, 6200)
    EnableCharacter(Characters.CelestialMinion5)
    EnableAI(Characters.CelestialMinion5)
    ForceAnimation(Characters.CelestialMinion5, 6200)
    EnableCharacter(Characters.CelestialMinion7)
    EnableAI(Characters.CelestialMinion7)
    ForceAnimation(Characters.CelestialMinion7, 6200)
    Wait(2.0)
    EnableCharacter(Characters.CelestialEmissarySmall)
    EnableAI(Characters.CelestialEmissarySmall)
    ForceAnimation(Characters.CelestialEmissarySmall, 6200)
    EnableCharacter(Characters.CelestialMinion1)
    EnableAI(Characters.CelestialMinion1)
    ForceAnimation(Characters.CelestialMinion1, 6200)
    EnableCharacter(Characters.CelestialMinion3)
    EnableAI(Characters.CelestialMinion3)
    ForceAnimation(Characters.CelestialMinion3, 6200)
    Wait(2.5)
    EnableCharacter(Characters.CelestialMinion2)
    EnableAI(Characters.CelestialMinion2)
    ForceAnimation(Characters.CelestialMinion2, 6200)
    EnableCharacter(Characters.CelestialMinion6)
    EnableAI(Characters.CelestialMinion6)
    ForceAnimation(Characters.CelestialMinion6, 6200)


def SummonStartCelestialEmissaryBattle():
    """ 12421703: Event 12421703 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.CelestialEmissaryFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(Flags.CelestialEmissaryFogEntered)
    EnableFlag(Flags.CelestialEmissaryFirstTimeDone)
    EnableCharacter(Characters.CelestialMinion4)
    EnableAI(Characters.CelestialMinion4)
    ForceAnimation(Characters.CelestialMinion4, 6200)
    EnableCharacter(Characters.CelestialMinion5)
    EnableAI(Characters.CelestialMinion5)
    ForceAnimation(Characters.CelestialMinion5, 6200)
    EnableCharacter(Characters.CelestialMinion7)
    EnableAI(Characters.CelestialMinion7)
    ForceAnimation(Characters.CelestialMinion7, 6200)
    Wait(2.0)
    EnableCharacter(Characters.CelestialEmissarySmall)
    EnableAI(Characters.CelestialEmissarySmall)
    ForceAnimation(Characters.CelestialEmissarySmall, 6200)
    EnableCharacter(Characters.CelestialMinion1)
    EnableAI(Characters.CelestialMinion1)
    ForceAnimation(Characters.CelestialMinion1, 6200)
    EnableCharacter(Characters.CelestialMinion3)
    EnableAI(Characters.CelestialMinion3)
    ForceAnimation(Characters.CelestialMinion3, 6200)
    Wait(2.5)
    EnableCharacter(Characters.CelestialMinion2)
    EnableAI(Characters.CelestialMinion2)
    ForceAnimation(Characters.CelestialMinion2, 6200)
    EnableCharacter(Characters.CelestialMinion6)
    EnableAI(Characters.CelestialMinion6)
    ForceAnimation(Characters.CelestialMinion6, 6200)


def EnterCelestialEmissaryFog():
    """ 12424710: Event 12424710 """
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    GotoIfFlagEnabled(Label.L0, Flags.CelestialEmissaryFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.CelestialEmissaryEntranceFog)
    DeleteVFX(VFX.CelestialEmissaryEntranceFog, erase_root_only=False)
    DisableObject(Objects.CelestialEmissaryExitFog)
    DeleteVFX(VFX.CelestialEmissaryExitFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.CelestialEmissaryDead)
    IfFlagEnabled(1, Flags.CelestialEmissaryFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.CelestialEmissaryEntranceFog)
    EnableObject(Objects.CelestialEmissaryExitFog)
    CreateVFX(VFX.CelestialEmissaryEntranceFog)
    CreateVFX(VFX.CelestialEmissaryExitFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(1, Flags.CelestialEmissaryDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2420700, entity=Objects.CelestialEmissaryEntranceFog)
    IfFlagEnabled(3, Flags.CelestialEmissaryDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.CelestialEmissaryFogEntered)
    Restart()


def EnterCelestialEmissaryFogAsSummon():
    """ 12424711: Event 12424711 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    IfFlagDisabled(1, Flags.CelestialEmissaryDead)
    IfFlagEnabled(1, Flags.CelestialEmissaryFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2420700, entity=Objects.CelestialEmissaryEntranceFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2422811)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12424701)
    Restart()


def Event12424712():
    """ 12424712: Event 12424712 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.CelestialEmissaryEntranceFog, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12424713():
    """ 12424713: Event 12424713 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.CelestialEmissaryEntranceFog, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, Objects.CelestialEmissaryEntranceFog, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartCelestialEmissaryBattle():
    """ 12424702: Event 12424702 """
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    DisableAI(Characters.CelestialEmissarySmall)
    DisableAI(Characters.CelestialMinion1)
    DisableAI(Characters.CelestialMinion2)
    DisableAI(Characters.CelestialMinion3)
    DisableAI(Characters.CelestialMinion4)
    DisableAI(Characters.CelestialMinion5)
    DisableAI(Characters.CelestialMinion6)
    DisableAI(Characters.CelestialMinion7)
    EnableImmortality(Characters.CelestialEmissarySmall)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.CelestialEmissaryFogEntered)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2800810, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800811, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.CelestialEmissaryFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2800800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(2800803)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2800800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(2800803)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableBossHealthBar(Characters.CelestialEmissarySmall, name=257000, slot=0)
    CreatePlayLog(104)
    StartPlayLogMeasurement(2800010, 40, overwrite=True)
    EndIfFlagDisabled(Flags.CelestialEmissaryFirstTimeDone)
    IfCharacterInsideRegion(-1, PLAYER, region=2422817)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialEmissarySmall, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion1, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion2, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion3, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion4, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion5, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion6, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.CelestialMinion7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.CelestialEmissarySmall)
    EnableAI(Characters.CelestialMinion1)
    EnableAI(Characters.CelestialMinion2)
    EnableAI(Characters.CelestialMinion3)
    EnableAI(Characters.CelestialMinion4)
    EnableAI(Characters.CelestialMinion5)
    EnableAI(Characters.CelestialMinion6)
    EnableAI(Characters.CelestialMinion7)


def ControlCelestialEmissaryMusic():
    """ 12424703: Event 12424703 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2703802)
    DisableSoundEvent(2703803)
    IfFlagDisabled(1, Flags.CelestialEmissaryDead)
    IfFlagEnabled(1, Flags.CelestialEmissaryBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12424701)
    IfCharacterInsideRegion(1, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2423812)
    EnableFlag(12425246)
    IfFlagEnabled(0, Flags.CelestialEmissaryPhaseTwo)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.CelestialEmissaryDead)
    IfFlagEnabled(2, Flags.CelestialEmissaryBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12424701)
    IfCharacterInsideRegion(2, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2423812)
    EnableFlag(12425246)
    WaitFrames(0)
    EnableBossMusic(2423813)


def ControlCelestialEmissaryCamera():
    """ 12424704: Event 12424704 """
    DisableNetworkSync()
    IfHealthGreaterThan(1, Characters.CelestialEmissaryGiant, 0.0)
    IfHealthLessThanOrEqual(1, Characters.CelestialEmissaryGiant, 0.6000000238418579)
    IfEntityWithinDistance(1, PLAYER, Characters.CelestialEmissaryGiant, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, Characters.CelestialEmissaryGiant, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.CelestialEmissaryGiant, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


def StopCelestialEmissaryMusic():
    """ 12424705: Event 12424705 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.CelestialEmissaryDead)
    IfFlagEnabled(0, Flags.CelestialEmissaryDead)
    DisableBossMusic(2423812)
    DisableBossMusic(2423813)
    DisableBossMusic(-1)
    DisableFlag(12425246)


@RestartOnRest
def Event12424770(_, arg_0_3: int, arg_4_7: int):
    """ 12424770: Event 12424770 """
    IfCharacterDead(1, Characters.CelestialEmissaryGiant)
    IfCharacterAlive(2, arg_0_3)
    IfCharacterDead(3, arg_0_3)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableImmortality(arg_4_7)
    DisableSpawner(arg_0_3)
    Kill(arg_4_7, award_souls=True)
    SkipLinesIfFinishedConditionTrue(1, 2)
    DisableCharacter(arg_0_3)
    IfCharacterAlive(0, arg_4_7)
    Restart()


@RestartOnRest
def ApplyCelestialEmissaryAura():
    """ 12424780: Minion aliens get buff from Celestial Emissary action. """
    IfCharacterHasTAEEvent(0, Characters.CelestialEmissaryGiant, tae_event_id=40)
    AddSpecialEffect(Characters.CelestialMinion1, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion2, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion3, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion4, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion5, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion6, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    AddSpecialEffect(Characters.CelestialMinion7, Effects.CelestialEmissaryAura, affect_npc_part_hp=False)
    Restart()


@RestartOnRest
def Event12424785(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12424785: Event 12424785 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterOutsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12424787(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12424787: Event 12424787 """
    IfFlagEnabled(1, arg_12_15)
    IfHealthGreaterThan(1, arg_16_19, 0.6000000238418579)
    IfCharacterOutsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12424784():
    """ 12424784: Event 12424784 """
    IfCharacterHasSpecialEffect(1, Characters.CelestialEmissaryGiant, 5609)
    IfCharacterOutsideRegion(1, Characters.CelestialEmissaryGiant, region=2422816)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.CelestialEmissaryGiant, command_id=20, slot=0)
    ReplanAI(Characters.CelestialEmissaryGiant)
    IfCharacterInsideRegion(0, Characters.CelestialEmissaryGiant, region=2422722)
    AICommand(Characters.CelestialEmissaryGiant, command_id=40, slot=0)
    ReplanAI(Characters.CelestialEmissaryGiant)
    IfCharacterInsideRegion(0, PLAYER, region=2422816)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(Characters.CelestialEmissaryGiant, command_id=-1, slot=0)
    ReplanAI(Characters.CelestialEmissaryGiant)
    Restart()


@RestartOnRest
def CelestialEmissaryPhaseTwoTrigger():
    """ 12424790: Event 12424790 """
    IfCharacterBackreadEnabled(0, Characters.CelestialEmissaryGiant)
    DisableAI(Characters.CelestialEmissaryGiant)
    DisableGravity(Characters.CelestialEmissaryGiant)
    DisableHealthBar(Characters.CelestialEmissaryGiant)
    ReferDamageToEntity(Characters.CelestialEmissarySmall, Characters.CelestialEmissaryGiant)
    DisableGravity(2420750)
    DisableGravity(2420751)
    IfHealthLessThan(1, Characters.CelestialEmissarySmall, 0.6000000238418579)
    IfHealthGreaterThan(1, Characters.CelestialEmissaryGiant, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetNest(Characters.CelestialEmissaryGiant, 2422721)
    AICommand(Characters.CelestialEmissarySmall, command_id=40, slot=1)
    ReplanAI(Characters.CelestialEmissarySmall)
    IfCharacterHasTAEEvent(0, Characters.CelestialEmissarySmall, tae_event_id=30)
    DisableBossHealthBar(Characters.CelestialEmissarySmall, name=257000, slot=0)
    WaitFrames(5)
    DisableCharacter(Characters.CelestialEmissarySmall)
    Move(
        Characters.CelestialEmissaryGiant,
        destination=Characters.CelestialEmissarySmall,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=Characters.CelestialEmissarySmall,
    )
    EnableGravity(Characters.CelestialEmissaryGiant)
    EnableAI(Characters.CelestialEmissaryGiant)
    ForceAnimation(Characters.CelestialEmissaryGiant, 3025, wait_for_completion=True)
    EnableBossHealthBar(Characters.CelestialEmissaryGiant, name=257000, slot=0)


@RestartOnRest
def ControlCelestialEmissaryTendrils():
    """ 12424791: Event 12424791 """
    IfHealthLessThanOrEqual(0, Characters.CelestialEmissaryGiant, 0.30000001192092896)
    SkipLinesIfThisEventFlagEnabled(1)
    WaitFrames(135)
    Move(
        2420750,
        destination=Characters.CelestialEmissaryGiant,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=Characters.CelestialEmissaryGiant,
    )
    Move(
        2420751,
        destination=Characters.CelestialEmissaryGiant,
        destination_type=CoordEntityType.Character,
        model_point=41,
        copy_draw_parent=Characters.CelestialEmissaryGiant,
    )
    Restart()


@RestartOnRest
def CelestialEmissaryTendrilAttack(_, tendrils: int):
    """ 12424792: Event 12424792 """
    IfHealthLessThanOrEqual(0, Characters.CelestialEmissaryGiant, 0.30000001192092896)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    WaitFrames(145)
    ForceAnimation(tendrils, 3000)
    IfCharacterHasSpecialEffect(0, Characters.CelestialEmissaryGiant, 5402)
    ForceAnimation(tendrils, 3000)
    Wait(3.5)
    DisableCharacter(tendrils)
    IfCharacterHasSpecialEffect(0, Characters.CelestialEmissaryGiant, 5400)
    Wait(1.5)
    EnableCharacter(tendrils)
    ForceAnimation(tendrils, 3000)
    Restart()


@RestartOnRest
def Event12424795():
    """ 12424795: Event 12424795 """
    IfCharacterHasSpecialEffect(1, Characters.CelestialEmissaryGiant, 5531)
    IfAttackedWithDamageType(1, attacked_entity=Characters.CelestialEmissaryGiant, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.CelestialEmissaryGiant, 3030)
    WaitFrames(59)
    ForceAnimation(Characters.CelestialEmissaryGiant, 7000, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(150)
    ForceAnimation(Characters.CelestialEmissaryGiant, 3000, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()


def Event12420000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12420000: Event 12420000 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_12_15)
    Wait(0.0)


def Event12420030(_, arg_0_3: int):
    """ 12420030: Event 12420030 """
    DisableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(0.0)


def Event12420050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12420050: Event 12420050 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event12420100():
    """ 12420100: Event 12420100 """
    SkipLinesIfThisEventFlagDisabled(2)
    PostDestruction(2421850)
    End()
    IfObjectDestroyed(0, 2421850)
    EnableFlag(12420100)


def Event12420123():
    """ 12420123: Event 12420123 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2421200, 1)
    DisableObjectActivation(2421270, obj_act_id=2420000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12420122)
    ForceAnimation(2421200, 1)
    CreateObjectVFX(920204, obj=2421200, model_point=200)
    CreateObjectVFX(920205, obj=2421200, model_point=201)


def Event12420124():
    """ 12420124: Event 12420124 """
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
    EndIfFinishedConditionTrue(3)
    EndIfFinishedConditionTrue(4)
    DisplayDialog(
        10010160,
        anchor_entity=2421200,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(0.0)
    Restart()


def Event12420130(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12420130: Event 12420130 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_8_11)
    Wait(0.0)


def Event12420140():
    """ 12420140: Event 12420140 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12420123)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421270)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(0.0)
    Restart()


def Event12420150():
    """ 12420150: Event 12420150 """
    IfFlagEnabled(1, 12420154)
    IfFlagDisabled(2, 12420154)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2421250, 0)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    SkipLines(3)
    EndOfAnimation(2421250, 8)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    DisableObjectActivation(2421252, obj_act_id=2420000)


def Event12420151():
    """ 12420151: Event 12420151 """
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
    WaitFrames(250)
    IfAllPlayersOutsideRegion(0, region=2422652)
    DisableObjectActivation(2421252, obj_act_id=2420000)
    ForceAnimation(2421250, 9)
    WaitFrames(10)
    EnableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    Restart()


def Event12420152():
    """ 12420152: Event 12420152 """
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
    WaitFrames(250)
    IfAllPlayersOutsideRegion(0, region=2422651)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    ForceAnimation(2421250, 7)
    WaitFrames(10)
    DisableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    Restart()


def Event12420153():
    """ 12420153: Event 12420153 """
    DisableNetworkSync()
    IfFlagDisabled(-1, 12420154)
    IfFlagEnabled(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421251)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12420156():
    """ 12420156: Event 12420156 """
    DisableNetworkSync()
    IfFlagEnabled(-1, 12420154)
    IfFlagEnabled(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2421252)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12420280(_, arg_0_3: int):
    """ 12420280: Event 12420280 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event12420285(_, arg_0_3: int, arg_4_7: int):
    """ 12420285: Event 12420285 """
    IfFlagEnabled(0, arg_4_7)
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event12420300():
    """ 12420300: Event 12420300 """
    DisableNetworkSync()
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=2422681)
    PlaySoundEffect(anchor_entity=2422680, sound_type=SoundType.a_Ambient, sound_id=20011001)
    EnableFlag(12420301)


@RestartOnRest
def Event12420310():
    """ 12420310: Event 12420310 """
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
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 52420170)
    IfCharacterInsideRegion(1, PLAYER, region=2422660)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=2421121, sound_type=SoundType.a_Ambient, sound_id=20011004)
    EnableCharacter(2420205)
    ForceAnimation(2420205, 7004)
    WaitFrames(10)
    DestroyObject(2421210)
    EnableGravity(2420205)
    EnableCharacterCollision(2420205)
    EnableAI(2420205)


@RestartOnRest
def Event12420320():
    """ 12420320: Event 12420320 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableObject(2421300)
    Move(2420200, destination=2422200, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    Move(2420201, destination=2422201, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    Move(2420202, destination=2422202, destination_type=CoordEntityType.Region, set_draw_parent=2420203)
    SetNest(2420200, 2422200)
    SetNest(2420201, 2422201)
    SetNest(2420202, 2422202)
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
    CreateObjectVFX(924500, obj=2421300, model_point=100)
    CreateObjectVFX(924500, obj=2421300, model_point=101)
    CreateObjectVFX(924500, obj=2421300, model_point=102)
    CreateObjectVFX(924500, obj=2421300, model_point=103)
    CreateObjectVFX(924500, obj=2421300, model_point=104)
    CreateObjectVFX(924500, obj=2421300, model_point=105)
    CreateObjectVFX(924500, obj=2421300, model_point=106)
    CreateObjectVFX(924500, obj=2421300, model_point=107)
    CreateObjectVFX(924500, obj=2421300, model_point=108)
    CreateObjectVFX(924500, obj=2421300, model_point=109)
    CreateObjectVFX(924500, obj=2421300, model_point=110)
    CreateObjectVFX(924500, obj=2421300, model_point=111)
    CreateObjectVFX(924500, obj=2421300, model_point=112)
    CreateObjectVFX(924500, obj=2421300, model_point=113)
    CreateObjectVFX(924500, obj=2421300, model_point=114)
    CreateObjectVFX(924500, obj=2421300, model_point=115)
    CreateObjectVFX(924500, obj=2421300, model_point=116)
    CreateObjectVFX(924500, obj=2421300, model_point=117)
    CreateObjectVFX(924500, obj=2421300, model_point=118)
    CreateObjectVFX(924500, obj=2421300, model_point=119)
    CreateObjectVFX(924500, obj=2421300, model_point=120)
    CreateObjectVFX(924500, obj=2421300, model_point=121)
    CreateObjectVFX(924500, obj=2421300, model_point=122)
    CreateObjectVFX(924500, obj=2421300, model_point=123)
    CreateObjectVFX(924500, obj=2421300, model_point=124)
    CreateObjectVFX(924500, obj=2421300, model_point=125)
    CreateObjectVFX(924500, obj=2421300, model_point=126)
    CreateObjectVFX(924500, obj=2421300, model_point=127)
    CreateObjectVFX(924500, obj=2421300, model_point=128)
    CreateObjectVFX(924500, obj=2421300, model_point=129)
    CreateObjectVFX(924500, obj=2421300, model_point=130)
    CreateObjectVFX(924500, obj=2421300, model_point=131)
    CreateObjectVFX(924500, obj=2421300, model_point=132)
    CreateObjectVFX(924500, obj=2421300, model_point=133)
    CreateObjectVFX(924500, obj=2421300, model_point=134)
    CreateObjectVFX(924500, obj=2421300, model_point=135)
    CreateObjectVFX(924500, obj=2421300, model_point=136)
    CreateObjectVFX(924500, obj=2421300, model_point=137)
    CreateObjectVFX(924500, obj=2421300, model_point=138)
    CreateObjectVFX(924500, obj=2421300, model_point=139)
    CreateObjectVFX(924501, obj=2421300, model_point=201)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=2422653)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2420200)
    ForceAnimation(2420200, 7007)
    ForceAnimation(2420201, 7008)
    ForceAnimation(2420202, 7009)
    ForceAnimation(2421300, 1)
    WaitFrames(81)
    DeleteObjectVFX(2421300, erase_root=False)
    CreateObjectVFX(924502, obj=2421300, model_point=201)
    WaitFrames(32)
    CreateObjectVFX(924503, obj=2421300, model_point=201)
    DisableObject(2421300)
    EnableObject(2421301)
    DestroyObject(2421301)
    EnableAI(2420200)
    EnableGravity(2420200)
    SetNest(2420200, 2422200)
    EnableAI(2420201)
    EnableGravity(2420201)
    SetNest(2420201, 2422201)
    EnableAI(2420202)
    EnableGravity(2420202)
    SetNest(2420202, 2422202)
    Wait(10.0)
    SetAIParamID(2420200, 100000)
    SetAIParamID(2420201, 100000)
    SetAIParamID(2420202, 100000)


def Event12420400():
    """ 12420400: Event 12420400 """
    GotoIfFlagEnabled(Label.L3, 9802)
    GotoIfFlagEnabled(Label.L2, 9801)
    GotoIfFlagEnabled(Label.L1, 9800)
    GotoIfFlagDisabled(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)
    EnableMapPiece(2424000)
    DisableMapPiece(2424010)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableMapPiece(2424000)
    EnableMapPiece(2424010)


def Event12420500():
    """ 12420500: Event 12420500 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72500326)
    IfFlagEnabled(0, 72500326)
    DisableFlagRange((72500304, 72500309))
    EnableFlag(72500328)
    RemoveGoodFromPlayer(4305, quantity=1)
    PlayCutscene(24020000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(10)
    DisableFlag(72500339)
    SaveRequest()
    Restart()


@RestartOnRest
def Event12420850(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12420850: Event 12420850 """
    DeleteVFX(arg_0_3, erase_root_only=False)
    DeleteVFX(arg_4_7, erase_root_only=False)
    DeleteVFX(arg_8_11, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, arg_12_15)
    CreateVFX(arg_4_7)
    CreateVFX(arg_8_11)
    End()
    IfObjectActivated(0, obj_act_id=arg_16_19)
    Wait(arg_20_23)
    CreateVFX(arg_0_3)
    CreateTemporaryVFX(arg_28_31, anchor_entity=arg_24_27, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    CreateVFX(arg_4_7)
    CreateVFX(arg_8_11)


@RestartOnRest
def Event12420853():
    """ 12420853: Event 12420853 """
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
    CreateTemporaryVFX(920206, anchor_entity=2421204, anchor_type=CoordEntityType.Object, model_point=200)
    CreateTemporaryVFX(920207, anchor_entity=2421204, anchor_type=CoordEntityType.Object, model_point=242)
    Wait(4.0)
    CreateVFX(2427032)
    CreateVFX(2427033)


@RestartOnRest
def Event12420854():
    """ 12420854: Event 12420854 """
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


@RestartOnRest
def Event12425200(_, arg_0_3: int):
    """ 12425200: Event 12425200 """
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=2.0)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(3, PLAYER, region=2422661)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 3)
    ForceAnimation(arg_0_3, 7001)
    ReplanAI(arg_0_3)
    End()
    ForceAnimation(arg_0_3, 7001)
    AICommand(arg_0_3, command_id=10, slot=0)
    SetNest(arg_0_3, 2422262)
    ReplanAI(arg_0_3)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-3, arg_0_3, region=2422262)
    IfConditionTrue(0, input_condition=-3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425210(_, arg_0_3: int):
    """ 12425210: Event 12425210 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7001)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425221(_, arg_0_3: int):
    """ 12425221: Event 12425221 """
    IfCharacterInsideRegion(0, arg_0_3, region=2422655)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=2423210)


@RestartOnRest
def Event12425250(
    _,
    arg_0_3: int,
    arg_4_7: float,
    arg_8_11: int,
    arg_12_15: float,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_28: uchar,
):
    """ 12425250: Event 12425250 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    SetNest(arg_0_3, arg_16_19)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    Wait(arg_4_7)
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-4, PLAYER, region=arg_8_11)
    IfEntityWithinDistance(-4, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=arg_20_23, slot=0)
    ReplanAI(arg_0_3)
    SkipLinesIfNotEqual(arg_28_28, left=0, right=arg_24_27)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425225():
    """ 12425225: Event 12425225 """
    EndIfThisEventFlagEnabled()
    ForceAnimation(2420253, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=2422253)
    IfEntityWithinDistance(-2, 2420253, PLAYER, radius=2.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2420253, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2420253, 7001)
    ReplanAI(2420253)


@RestartOnRest
def Event12425245():
    """ 12425245: Event 12425245 """
    DisableNetworkSync()
    DisableSoundEvent(2423600)
    IfInsideMap(1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagDisabled(1, 12425246)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(2423600)
    IfOutsideMap(-1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagEnabled(-1, 12425246)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(2423600)
    Restart()


@RestartOnRest
def Event12425290():
    """ 12425290: Event 12425290 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountGreaterThanOrEqual(2, 10)
    EndIfConditionFalse(2)
    EnableFlag(12425291)


@RestartOnRest
def Event12425300(_, arg_0_3: int):
    """ 12425300: Event 12425300 """
    IfFlagEnabled(-1, 12425291)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    SetDisplayMask(arg_0_3, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5696, affect_npc_part_hp=False)


@RestartOnRest
def Event12425305(_, arg_0_3: int):
    """ 12425305: Event 12425305 """
    IfFlagEnabled(-1, 12425291)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_0_3, 5552, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 5553, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 5554, affect_npc_part_hp=False)


@RestartOnRest
def Event12425310(_, arg_0_3: int):
    """ 12425310: Event 12425310 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, 7018, loop=True)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(arg_0_3, 7019)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12425320: Event 12425320 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    SetNest(arg_0_3, arg_12_15)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_12_15)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Normal)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    ForceAnimation(arg_0_3, 0)
    Restart()


@RestartOnRest
def Event12425350(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12425350: Event 12425350 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetAIParamID(arg_0_3, arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    SetAIParamID(arg_0_3, arg_8_11)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425500(_, arg_0_3: int, arg_4_7: float, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 12425500: Event 12425500 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(arg_16_19)
    DisableAI(arg_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    SkipLinesIfNotEqual(3, left=1, right=arg_8_11)
    IfCharacterInsideRegion(2, PLAYER, region=arg_12_15)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12425600():
    """ 12425600: Event 12425600 """
    EndIfThisEventFlagEnabled()
    IfCharacterBackreadEnabled(1, 2420401)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    DisableAI(2420401)
    DisableAI(2420402)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfEntityWithinDistance(-3, PLAYER, 2420401, radius=5.0)
    IfEntityWithinDistance(-3, PLAYER, 2420402, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=2422685)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfAttacked(-1, 2420401, attacker=PLAYER)
    IfAttacked(-1, 2420402, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2420401)
    ReplanAI(2420401)
    Wait(3.0)
    EnableAI(2420402)
    ReplanAI(2420402)


def Event12425601():
    """ 12425601: Event 12425601 """
    DisableNetworkSync()
    IfCharacterAlive(1, 2420402)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    Move(2420731, destination=2420402, destination_type=CoordEntityType.Character, model_point=40, short_move=True)
    Restart()


@RestartOnRest
def Event12425602():
    """ 12425602: Event 12425602 """
    IfHealthLessThanOrEqual(0, 2420402, 0.0)
    Wait(1.0)
    ForceAnimation(2420731, 2200, wait_for_completion=True)
    DisableCharacter(2420731)


def Event12425603():
    """ 12425603: Event 12425603 """
    AddSpecialEffect(2420402, 5609, affect_npc_part_hp=False)
    DisableGravity(2420731)


@RestartOnRest
def Event12425400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12425400: Event 12425400 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(arg_0_3, arg_8_11)


def Event12420990():
    """ 12420990: Event 12420990 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfPlayerStandingOnCollision(0, 2423500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 154, PlayLogMultiplayerType.HostOnly)
    AwardAchievement(11)


@RestartOnRest
def Event12424450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12424450: Event 12424450 """
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12424400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12424400: Event 12424400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagDisabled(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_8_11)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12424410(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12424410: Event 12424410 """
    SkipLinesIfFlagEnabled(1, arg_12_15)
    DisableCharacter(arg_4_7)
    SkipLinesIfFlagEnabled(3, arg_16_19)
    IfClient(1)
    IfFlagEnabled(1, arg_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_4_7)
    EndIfFlagEnabled(arg_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(arg_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfFlagEnabled(2, arg_20_23)
    IfFlagDisabled(2, arg_24_27)
    IfActionButtonParamActivated(2, action_button_id=arg_28_31, entity=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(arg_0_3, arg_4_7, arg_8_11, summon_flag=arg_12_15, dismissal_flag=arg_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12424460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12424460: Event 12424460 """
    EndIfClient()
    IfFlagEnabled(1, arg_20_23)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    RotateToFaceEntity(arg_0_3, arg_8_11, animation=arg_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(arg_0_3, region=arg_8_11, reaction_range=1.0)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_24_27)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
