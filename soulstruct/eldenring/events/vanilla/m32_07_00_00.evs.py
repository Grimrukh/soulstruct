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
    RegisterGrace(grace_flag=32070000, obj=32071950, unknown=5.0)
    RegisterGrace(grace_flag=32070001, obj=32071951, unknown=5.0)
    Event_32072810()
    Event_32072800()
    Event_32072811()
    Event_32072849()
    Event_32072200(0, 32070200, 30004, 20004, 32070310, 16576, 1.0, 0, 0, 0, 0, 32071608, 0, 0, 0)
    Event_32072200(1, 32070201, 30000, 20000, 32070310, 16572, 1.0, 0, 0, 0, 0, 32071609, 0, 0, 0)
    Event_32072200(2, 32070202, 30004, 20004, 32070310, 16576, 0.0, 0, 0, 0, 0, 32071600, 32071601, 0, 0)
    Event_32072200(3, 32070203, 30002, 20002, 32070310, 16574, 0.0, 0, 0, 0, 0, 32071602, 32071603, 32071604, 0)
    Event_32072200(4, 32070210, 30002, 20002, 32070316, 16574, 1.0, 0, 0, 0, 0, 32071610, 0, 0, 0)
    RunCommonEvent(0, 90005511, args=(32070560, 32071560, 32073560, 27043, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(32070560, 32072560, 32072561), arg_types="III")
    Event_32072580()
    RunCommonEvent(
        0,
        90005646,
        args=(32070800, 32072840, 32072841, 32071840, 32072840, 32, 7, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(32071680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(32071681, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005703, args=(32070700, 3661, 3662, 1043399301, 3661, 3660, 3663, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(32070700, 3661, 3660, 1043399301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(32070700, 3663, 3660, 3663), arg_types="IIII")
    Event_32073700(0, character=32070700)
    Event_32073701()
    Event_32073702()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32072820()
    RunCommonEvent(0, 90005250, args=(32070204, 32072204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070350, 32072306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070300, 32072300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070301, 32072300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070306, 32072306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070307, 32072306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070308, 32072308, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070309, 32072309, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070310, 32072309, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070315, 32072315, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32070316, 32072316, 0.0, -1), arg_types="IIfi")


@RestartOnRest(32072580)
def Event_32072580():
    """Event 32072580"""
    RegisterLadder(start_climbing_flag=32070530, stop_climbing_flag=32070531, obj=32071530)
    RegisterLadder(start_climbing_flag=32070532, stop_climbing_flag=32070533, obj=32071532)


@RestartOnRest(32072200)
def Event_32072200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    character_1: uint,
    special_effect_id: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
):
    """Event 32072200"""
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfObjectDestroyed(OR_10, obj)
    IfObjectDestroyed(OR_10, obj_1)
    IfObjectDestroyed(OR_10, obj_2)
    IfObjectDestroyed(OR_10, obj_3)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(AND_12, character_1, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(AND_12, PLAYER, 10004)
    IfConditionTrue(OR_2, input_condition=AND_12)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(32072800)
def Event_32072800():
    """Event 32072800"""
    EndIfFlagEnabled(32070800)
    IfHealthValueLessThanOrEqual(MAIN, 32070800, value=0)
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 32070800)
    KillBossAndDisplayBanner(character=32070800, banner_type=BannerType.Unknown)
    EnableFlag(32070800)
    EnableFlag(9266)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61266)


@RestartOnRest(32072810)
def Event_32072810():
    """Event 32072810"""
    GotoIfFlagDisabled(Label.L0, flag=32070800)
    DisableCharacter(32070800)
    DisableAnimations(32070800)
    Kill(32070800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32070800)
    GotoIfFlagEnabled(Label.L1, flag=32070801)
    ForceAnimation(32070800, 30000, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=32072801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=32070800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(32070801)
    Wait(0.30000001192092896)
    ForceAnimation(32070800, 20000, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(32070800, 30000, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32072805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32072800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.30000001192092896)
    ForceAnimation(32070800, 20000, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32070800)
    SetNetworkUpdateRate(32070800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32070800, name=904910320)


@RestartOnRest(32072811)
def Event_32072811():
    """Event 32072811"""
    EndIfFlagEnabled(32070800)
    IfHealthLessThanOrEqual(AND_1, 32070800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32072802)


@RestartOnRest(32072820)
def Event_32072820():
    """Event 32072820"""
    EndIfFlagEnabled(32070800)
    EndIfFlagEnabled(32070801)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(32078540)
    DisableFlag(32078540)


@RestartOnRest(32072849)
def Event_32072849():
    """Event 32072849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32070800, 32071800, 32072800, 32072805, 32075800, 10000, 32070801, 32072801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32070800, 32071800, 32072800, 32072805, 32072806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32070800, 32071800, 7, 32070801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32070800, 920900, 32072805, 32072806, 0, 32072802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(32073700)
def Event_32073700(_, character: uint):
    """Event 32073700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3666)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3666)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3666)
    Restart()


@RestartOnRest(32073701)
def Event_32073701():
    """Event 32073701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyEnabled(flag_range=(3666, 3671))
    IfCharacterInsideRegion(OR_1, character=20000, region=32072700)
    AwaitConditionTrue(OR_1)
    EnableFlag(32009203)
    EnableFlag(3678)
    End()


@RestartOnRest(32073702)
def Event_32073702():
    """Event 32073702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyEnabled(flag_range=(3666, 3671))
    IfCharacterInsideRegion(AND_1, character=20000, region=32072701)
    IfFlagDisabled(AND_1, 1043399305)
    IfConditionTrue(OR_1, input_condition=AND_1)
    AwaitConditionTrue(OR_1)
    EnableFlag(32009203)
    End()
