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
    RegisterGrace(grace_flag=1043370000, obj=1043371950, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1043370210, 1043370210, 40108, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1043370800, 1043370341, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1043370340, 1043370341), arg_types="II")
    RunCommonEvent(0, 90005477)
    Event_1043372340(0, character=1043370340, character_1=1043370341)
    RunCommonEvent(0, 90005860, args=(1043370800, 0, 1043370340, 0, 1043370400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005871, args=(1043370340, 903150600, 10, 1043370341), arg_types="IiII")
    RunCommonEvent(0, 90005872, args=(1043370340, 10, 0), arg_types="III")
    Event_1043373700(0, character=1043370700, character_1=1043370701, character_2=1043370702, obj=1043376700)
    Event_1043373703(0, character=1043370700)
    Event_1043373705(0, character=1043370700)
    RunCommonEvent(0, 90005703, args=(1043370700, 4701, 4702, 1043379249, 4701, 4700, 4703, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1043370700, 4701, 4700, 1043379249, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1043370700, 4703, 4700, 4703), arg_types="IIII")
    RunCommonEvent(
        0,
        90005703,
        args=(1043370701, 1043379246, 1043379246, 1043379247, 1043379246, 1043379246, 1043379246, 0),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1043370701, 1043379246, 1043379246, 1043379247, 3), arg_types="IIIIi")
    RunCommonEvent(0, 1043373706, args=(1043370700, 1043370701), arg_types="II")
    Event_1043373707(
        0,
        character=1043370700,
        first_flag=4700,
        flag=4701,
        flag_1=4702,
        last_flag=4703,
        character_1=1043370701,
        flag_2=1043379246
    )
    Event_1043373701()
    Event_1043373710(0, character=1043370730)
    Event_1043373711()
    Event_1043373722(
        0,
        character__unk_0_4=1043370740,
        region=1043372709,
        region_1=1043372711,
        region_2=1043372701,
        region_3=1043382700
    )
    Event_1043373726(0, character=1043370740)
    RunCommonEvent(0, 90005791, args=(1043379262, 1043372715, 1043372716, 1043370740), arg_types="IIII")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1043379262, 1043372715, 1043372716, 1043370740, 21, 1043382710, 1043372709, 0.0, 1043372740, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1043379262, 1043372715, 1043372716, 1043370740, 21, 1043372712, 1043372711, 0.0, 1043372741, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005774, args=(1043379262, 1042370700, 1042377700), arg_types="IiI")
    RunCommonEvent(0, 90005704, args=(1043370750, 3941, 3940, 1043379351, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1043370750, 3941, 3942, 1043379351, 3941, 3940, 3944, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1043370750, 3943, 3940, 3944), arg_types="IIII")
    Event_1043373730(0, character=1043370750, obj=1043371700)
    Event_1043373731(0, 13.0, 13.0, 25.0)
    Event_1043373732(0, character=1043370750, obj=1043371700)
    Event_1043373733(0, character=1043370750)
    Event_1043373734(0, entity=1043370750)
    RunCommonEvent(0, 90005630, args=(61433700, 1043371500, 127), arg_types="IIi")
    RunCommonEvent(0, 90005460, args=(1043370200,))
    RunCommonEvent(0, 90005461, args=(1043370200,))
    RunCommonEvent(0, 90005462, args=(1043370200,))
    RunCommonEvent(0, 900005610, args=(1043371680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005631, args=(1043371640, 61010), arg_types="Ii")
    Event_1043372650(0, 1520, 710520, 1770, 710770, 69090, 69370)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043370711)
    DisableBackread(1043370720)
    DisableBackread(1043370740)
    DisableBackread(1043370750)
    RunCommonEvent(0, 90005200, args=(1043370240, 30019, 20019, 1043372240, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043370241, 30019, 20019, 1043372240, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043370242, 30019, 20019, 1043372240, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043370243, 30019, 20019, 1043372240, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043370244, 30019, 20019, 1043372240, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1043370210, 1043372210, 3.0, 0.0, -1), arg_types="IIffi")


@RestartOnRest(1043372250)
def Event_1043372250(_, character: uint, region: uint, owner_entity: uint):
    """Event 1043372250"""
    EndIfFlagEnabled(1041382200)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableFlag(1041382200)
    IfCharacterDead(AND_5, character)
    EndIfConditionTrue(input_condition=AND_5)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    IfCharacterOutsideRegion(AND_7, character=PLAYER, region=region)
    EndIfConditionTrue(input_condition=AND_7)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    EnableCharacter(character)
    ForceAnimation(character, 20011, unknown2=1.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    CancelSpecialEffect(character, 8090)


@RestartOnRest(1043372340)
def Event_1043372340(_, character: uint, character_1: uint):
    """Event 1043372340"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1043372650)
def Event_1043372650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1043372650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_NE)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1043373700)
def Event_1043373700(_, character: uint, character_1: uint, character_2: uint, obj: uint):
    """Event 1043373700"""
    WaitFrames(frames=1)
    DisableFlag(1043379200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_1, 4700)
    IfFlagEnabled(AND_1, 1043379248)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379248)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    IfFlagEnabled(OR_1, 4705)
    IfFlagEnabled(OR_1, 4706)
    IfFlagEnabled(OR_1, 4707)
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(1, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(2, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
    DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 1043379200)
    Restart()


@RestartOnRest(1043373701)
def Event_1043373701():
    """Event 1043373701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043379229)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1043370700, radius=7.5)
    EnableNetworkFlag(1043379229)
    End()


@NeverRestart(1043373703)
def Event_1043373703(_, character: uint):
    """Event 1043373703"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4705)
    IfFlagEnabled(OR_1, 4706)
    IfFlagEnabled(OR_1, 4707)
    IfFlagEnabled(OR_2, 4700)
    IfFlagEnabled(OR_2, 4701)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(OR_5, character, 9601)
    IfCharacterHasSpecialEffect(OR_5, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityWithinDistance(OR_6, entity=20000, other_entity=character, radius=4.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_6, character, 9601)
    IfConditionTrue(MAIN, input_condition=OR_6)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9601)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    IfEntityBeyondDistance(OR_7, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_7, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_7)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20010, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterHasSpecialEffect(OR_10, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_10)
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    IfEntityBeyondDistance(OR_11, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_11, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_11)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=9603)
    ForceAnimation(character, 20011, unknown2=1.0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1043373705)
def Event_1043373705(_, character: uint):
    """Event 1043373705"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4705)
    IfFlagEnabled(OR_1, 4706)
    IfFlagEnabled(OR_1, 4707)
    IfFlagEnabled(OR_2, 4700)
    IfFlagEnabled(OR_2, 4701)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9602)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    IfCharacterHasSpecialEffect(MAIN, character, 9602)
    Restart()


@RestartOnRest(1043373706)
def Event_1043373706(_, character: uint, attacked_entity: uint):
    """Event 1043373706"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 1043372709)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1043372708)
    EndIfFlagEnabled(4701)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9602)
    ForceAnimation(character, 20006, unknown2=1.0)


@NeverRestart(1043373707)
def Event_1043373707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1043373707"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, 3000)
    EndIfFlagDisabled(first_flag)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    IfHealthValueLessThan(AND_1, character, value=1)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_3, flag_2)
    IfAttackedWithDamageType(AND_3, attacked_entity=character_1, attacker=20000)
    IfHealthValueLessThan(AND_3, character_1, value=1)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(MAIN, flag_2)
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1043373710)
def Event_1043373710(_, character: uint):
    """Event 1043373710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023, unknown2=1.0)


@RestartOnRest(1043373711)
def Event_1043373711():
    """Event 1043373711"""
    IfFlagDisabled(AND_1, 1043379305)
    IfFlagDisabled(AND_1, 1043379306)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1043370730, radius=8.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1043372722)


@RestartOnRest(1043373721)
def Event_1043373721(_, character: uint, flag: uint, distance: float):
    """Event 1043373721"""
    EndIfPlayerNotInOwnWorld()
    DisableBackread(character)
    EndIfFlagDisabled(3620)
    IfFlagDisabled(AND_1, 3625)
    IfFlagDisabled(AND_1, 3626)
    EndIfConditionTrue(input_condition=AND_1)
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfFlagDisabled(AND_2, 1043372713)
    IfFlagEnabled(AND_2, 1043372717)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableBackread(character)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(1043373722)
def Event_1043373722(_, character__unk_0_4: uint, region: uint, region_1: uint, region_2: uint, region_3: uint):
    """Event 1043373722"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    GotoIfFlagDisabled(Label.L1, flag=1043372714)
    GotoIfFlagEnabled(Label.L2, flag=1043372714)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_1)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfCharacterInsideRegion(Label.L5, character=PLAYER, region=region)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(1043372740)
    DisableFlag(1043372741)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(1043372741)
    DisableFlag(1043372740)
    Goto(Label.L7)

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1043372714)
    SetNetworkUpdateAuthority(character__unk_0_4, authority_level=UpdateAuthority.Unknown8192)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_2)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_3)
    IfCharacterDead(OR_2, character__unk_0_4)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableFlag(1043372714)
    DisableFlag(1043372740)
    DisableFlag(1043372741)
    EnableFlag(1043379263)
    IfCharacterDead(AND_2, character__unk_0_4)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(1043379262)
    WaitFrames(frames=1)
    EnableFlag(3638)
    DisableFlag(1043369200)
    EndIfFlagEnabled(1043379262)
    Unknown_2003_79(unk_0_4=character__unk_0_4)
    End()


@RestartOnRest(1043373726)
def Event_1043373726(_, character: uint):
    """Event 1043373726"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfCharacterHasSpecialEffect(MAIN, character, 9760)
    Wait(5.0)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    End()


@RestartOnRest(1043373730)
def Event_1043373730(_, character: uint, obj: uint):
    """Event 1043373730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3940)
    IfFlagEnabled(AND_1, 1043379353)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_1, 3945)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3945)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L5, flag=1043379357)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    SetCharacterTalkRange(character=character, distance=70.0)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableObject(obj)
    DisableAnimations(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930010, unknown2=1.0)
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
    IfFlagEnabled(OR_15, 3945)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1043373731)
def Event_1043373731(_, seconds: float, seconds_1: float, seconds_2: float):
    """Event 1043373731"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3945)
    EndIfFlagEnabled(1043379357)
    EnableFlag(1043372732)
    IfFlagEnabled(MAIN, 1043372733)
    Wait(seconds)
    EnableFlag(1043372734)
    IfFlagEnabled(MAIN, 1043372735)
    Wait(seconds_1)
    EnableFlag(1043372736)
    IfFlagEnabled(MAIN, 1043372737)
    Wait(seconds_2)
    DisableFlag(1043372732)
    DisableFlag(1043372733)
    DisableFlag(1043372734)
    DisableFlag(1043372735)
    DisableFlag(1043372736)
    DisableFlag(1043372737)
    Restart()


@RestartOnRest(1043373732)
def Event_1043373732(_, character: uint, obj: uint):
    """Event 1043373732"""
    GotoIfPlayerNotInOwnWorld(Label.L0)
    EndIfFlagEnabled(1044342300)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1043379357)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagEnabled(flag=1043379357)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableObject(obj)
    Wait(0.30000001192092896)
    EnableCharacter(character)
    EnableAnimations(character)
    End()


@RestartOnRest(1043373733)
def Event_1043373733(_, character: uint):
    """Event 1043373733"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    SetBackreadStateAlternate(character, False)
    EndIfFlagDisabled(3945)
    EndIfFlagEnabled(1043379357)
    IfFlagDisabled(AND_1, 1043379357)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=15.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character, True)
    IfFlagDisabled(AND_2, 1043379357)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=15.0)
    IfConditionFalse(MAIN, input_condition=AND_2)
    SetBackreadStateAlternate(character, False)
    Restart()


@RestartOnRest(1043373734)
def Event_1043373734(_, entity: uint):
    """Event 1043373734"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3945)
    EndIfFlagDisabled(3940)
    IfFlagEnabled(MAIN, 3941)
    ForceAnimation(entity, 20043, unknown2=1.0)
    Restart()
