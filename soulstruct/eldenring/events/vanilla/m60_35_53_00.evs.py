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
    RunCommonEvent(0, 90005600, args=(76355, 1035531950, 5.0, 0), arg_types="IIfI")
    Event_1035532200(0, attacker__character=1035535200, region=1035532200)
    Event_1035532210()
    RunCommonEvent(0, 90005251, args=(1035530250, 10.0, 0.20000000298023224, -1), arg_types="Iffi")
    RunCommonEvent(1, 90005251, args=(1035530251, 10.0, 0.30000001192092896, -1), arg_types="Iffi")
    RunCommonEvent(2, 90005251, args=(1035530252, 10.0, 0.30000001192092896, -1), arg_types="Iffi")
    RunCommonEvent(3, 90005251, args=(1035530253, 10.0, 0.4000000059604645, -1), arg_types="Iffi")
    RunCommonEvent(4, 90005251, args=(1035530254, 10.0, 0.4000000059604645, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1035530230, 1035532230, 30.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035530231, 1035532230, 30.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035530400, 1035532400, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1035530800, 30001, 20001, 1035532346, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1035530800, 1035532346, 0.5, 3004), arg_types="IIfi")
    Event_1035532300()
    RunCommonEvent(0, 90005870, args=(1035530800, 904910600, 5), arg_types="IiI")
    RunCommonEvent(0, 90005861, args=(1035530800, 1035530800, 1035530800, 1, 30390, 30062, 0.0), arg_types="IIIIiif")
    Event_1035532500()
    Event_1035532450(0, obj=1035531400)
    Event_1035532450(1, obj=1035531401)
    Event_1035532450(2, obj=1035531402)
    RunCommonEvent(0, 90005704, args=(1035530700, 3661, 3660, 1043399301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1035530700, 3661, 3662, 1043399301, 3661, 3660, 3663, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1035530700, 3663, 3660, 3663), arg_types="IIII")
    Event_1035533700(0, character=1035530700)
    Event_1035533701()
    RunCommonEvent(
        0,
        90005730,
        args=(1035532702, 40.0, 1035539206, 1051369265, 1035539205, 1035539205),
        arg_types="IfIIII",
    )


@RestartOnRest(1035532200)
def Event_1035532200(_, attacker__character: uint, region: uint):
    """Event 1035532200"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5658)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1050562200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5658)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1050562200)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5658)


@NeverRestart(1035532210)
def Event_1035532210():
    """Event 1035532210"""
    AddSpecialEffect(1035530210, 8092)
    AddSpecialEffect(1035530211, 8092)


@RestartOnRest(1035532300)
def Event_1035532300():
    """Event 1035532300"""
    IfHasAIStatus(MAIN, 1035530800, ai_status=AIStatusType.Battle)
    ForceAnimation(1035530800, 3004, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(1035532340)
def Event_1035532340(_, character: uint, region: uint, destination: uint):
    """Event 1035532340"""
    SkipLinesIfFlagDisabled(1, 1035530340)
    End()
    IfFlagDisabled(AND_1, 1035530340)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    IfFlagDisabled(AND_2, 1035530340)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20002, loop=True, unknown2=1.0)
    EnableNetworkFlag(1035530340)
    End()


@RestartOnRest(1035532450)
def Event_1035532450(_, obj: uint):
    """Event 1035532450"""
    DisableObject(obj)
    End()


@NeverRestart(1035532500)
def Event_1035532500():
    """Event 1035532500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1035532250, 1035531200, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1035532251, 1035531201, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1035532252, 1035531202, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")


@RestartOnRest(1035533700)
def Event_1035533700(_, character: uint):
    """Event 1035533700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3669)
    IfFlagEnabled(OR_1, 3670)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_2, 3669)
    IfFlagEnabled(OR_2, 3670)
    AwaitConditionTrue(OR_2)
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
    ForceAnimation(character, 930020, unknown2=1.0)
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
    IfFlagDisabled(AND_15, 3669)
    IfFlagDisabled(AND_15, 3670)
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1035533701)
def Event_1035533701():
    """Event 1035533701"""
    IfFlagDisabled(AND_1, 3669)
    IfFlagDisabled(AND_1, 3670)
    EndIfConditionTrue(input_condition=AND_1)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=1035530700, radius=90.0)
    EnableNetworkFlag(1035539204)
    AwaitFlagEnabled(flag=1035530800)
    SkipLinesIfFlagEnabled(2, 1035539207)
    EnableNetworkFlag(1035539207)
    Wait(20.0)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=1035530700, radius=90.0)
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1035539206)
    IfEntityBeyondDistance(AND_4, entity=PLAYER, other_entity=1035530700, radius=90.0)
    AwaitConditionTrue(AND_4)
    DisableNetworkFlag(1035539206)
    Restart()
