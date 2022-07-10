"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044330000, obj=1044331950, unknown=5.0)
    RegisterGrace(grace_flag=1044330001, obj=1044331951, unknown=5.0)
    RegisterGrace(grace_flag=1044330002, obj=1044331952, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76161, 76151, 1044331980, 77110, 2, 78110, 78111, 78112, 78113, 78114, 78115, 78116, 78117, 78118, 78119),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1044330290, 1044330290, 40140, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005550, args=(1044330500, 1044331500, 44333500), arg_types="III")
    RunCommonEvent(0, 90005510, args=(1044330540, 1044331540, 1044333540, -1, 10010851, 0), arg_types="IIIiiI")
    RunCommonEvent(0, 90005461, args=(1044330200,))
    RunCommonEvent(1, 90005462, args=(1044330200,))
    RunCommonEvent(0, 90005460, args=(1044330200,))
    Event_1044332230(0, character=1044330970)
    Event_1044332230(1, character=1044330240)
    Event_1044332230(2, character=1044330241)
    Event_1044332230(3, character=1044330242)
    Event_1044332230(4, character=1044330243)
    Event_1044332230(5, character=1044330244)
    Event_1044332230(6, character=1044330245)
    Event_1044332230(7, character=1044330246)
    Event_1044332230(18, character=1044330247)
    Event_1044332230(19, character=1044330248)
    Event_1044332230(20, character=1044330249)
    Event_1044332230(8, character=1044330304)
    Event_1044332230(9, character=1044330305)
    Event_1044332230(10, character=1044330306)
    Event_1044332230(11, character=1044330307)
    Event_1044332230(12, character=1044330308)
    Event_1044332230(13, character=1044330309)
    Event_1044332230(14, character=1044330310)
    Event_1044332230(15, character=1044330311)
    Event_1044332230(16, character=1044330312)
    Event_1044332230(17, character=1044330313)
    Event_1044332230(21, character=1044330300)
    Event_1044332230(22, character=1044330301)
    Event_1044332230(15, character=1044330250)
    Event_1044332230(16, character=1044330251)
    Event_1044332230(17, character=1044330252)
    Event_1044332230(18, character=1044330253)
    Event_1044332230(19, character=1044330254)
    Event_1044332230(20, character=1044330255)
    Event_1044332230(21, character=1044330256)
    Event_1044332280(0, character=1044330280, obj=1044331280, region=1044332280)
    Event_1044332280(1, character=1044330281, obj=1044331281, region=1044332280)
    RunCommonEvent(0, 90005400, args=(1044330250, 0, 0.0, 0.0, 0), arg_types="IiffI")
    RunCommonEvent(0, 90005401, args=(98103, 1044330250), arg_types="II")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005695, args=(1044331600, 1044331600, 200, 0, 802001200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    Event_1044333700(0, character=1044330700)
    RunCommonEvent(
        0,
        90005725,
        args=(4735, 4736, 4738, 1044339205, 1044330705, 1044330706, 1044336700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1044330705, 4736, 4737, 1044339206, 4736, 4735, 4739, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1044330705, 4736, 4735, 1044339206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1044330705, 4738, 4735, 4739), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1044330706, 4736, 4737, 1044339207, 4736, 4735, 4739, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1044330706, 4736, 4735, 1044339207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1044330706, 1044332706, 1044332707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4736, 1044330705, 1044330706, 4735, 4738), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044330700)
    DisableBackread(1044330705)
    DisableBackread(1044330706)
    RunCommonEvent(0, 90005251, args=(1044330232, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044330234, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1044330270, 1044332233, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044330271, 1044332233, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044330272, 1044332231, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044330273, 1044332231, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044330274, 1044332231, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1044330340, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1044330260, 1044332260, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330261, 1044332260, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330262, 1044332260, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330263, 1044332260, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1044330200, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044330201, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044330202, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044330203, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044330204, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(2, 90005251, args=(1044330206, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1044330200, 30006, 20006, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044330201, 30004, 20004, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044330202, 30004, 20004, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044330203, 30006, 20006, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044330204, 30004, 20004, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044330206, 30004, 20004, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(1044330214, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330215, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330216, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330217, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330218, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330220, 1044332220, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330200, 1044332200, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044330201, 1044332200, 1.0, 0.0, -1), arg_types="IIffi")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1044332240()


@RestartOnRest(1044332230)
def Event_1044332230(_, character: uint):
    """Event 1044332230"""
    Kill(character)
    End()


@RestartOnRest(1044332240)
def Event_1044332240():
    """Event 1044332240"""
    EndOfAnimation(obj=1044331610, animation_id=2)


@RestartOnRest(1044332280)
def Event_1044332280(_, character: uint, obj: uint, region: uint):
    """Event 1044332280"""
    DisableCharacter(character)
    DisableObject(obj)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    EnableObject(obj)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableObject(obj)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044332300)
def Event_1044332300():
    """Event 1044332300"""
    AddSpecialEffect(1044330220, 8810)
    DisableCharacter(1044330210)
    DisableAnimations(1044330210)
    DisableCharacter(1044335240)
    DisableAnimations(1044335240)
    ForceAnimation(1044330210, 30005, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1044332351)
    IfFlagDisabled(AND_1, 1044330321)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(1044330210)
    EnableAnimations(1044330210)
    ForceAnimation(1044330210, 30005, loop=True, unknown2=1.0)
    EnableFlag(1044330300)
    EnableFlag(1044332320)


@RestartOnRest(1044332301)
def Event_1044332301():
    """Event 1044332301"""
    GotoIfFlagEnabled(Label.L0, flag=1044330321)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1044332332)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangePatrolBehavior(1044330210, patrol_information_id=1044333351)
    Wait(10.0)
    DisableFlag(1044332320)
    EnableFlag(1044330321)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(1044330210)
    DisableAnimations(1044330210)
    DisableCharacter(1044335240)
    DisableAnimations(1044335240)


@RestartOnRest(1044332302)
def Event_1044332302():
    """Event 1044332302"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1044332320)
    IfFlagDisabled(AND_1, 1044330321)
    IfFlagDisabled(AND_1, 1044332322)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1044332350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(1044335240)
    EnableAnimations(1044335240)
    AddSpecialEffect(1044335240, 10270)
    CancelSpecialEffect(1044335240, 8552)
    EnableFlag(1044332322)
    ForceAnimation(1044330210, 20021, wait_for_completion=True, unknown2=1.0)
    ChangePatrolBehavior(1044330210, patrol_information_id=1044333350)
    AddSpecialEffect(1044330210, 5000)
    EnableFlag(1044332330)


@RestartOnRest(1044332303)
def Event_1044332303():
    """Event 1044332303"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1044332320)
    IfCharacterDead(AND_1, 1044330225)
    IfCharacterDead(AND_1, 1044330226)
    IfCharacterDead(AND_1, 1044330227)
    IfCharacterDead(AND_1, 1044330228)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1044332331)
    CancelSpecialEffect(1044330210, 5000)


@RestartOnRest(1044332304)
def Event_1044332304():
    """Event 1044332304"""
    DisableFlag(1044332330)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1044330390)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1044332330)


@RestartOnRest(1044333700)
def Event_1044333700(_, character: uint):
    """Event 1044333700"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    ForceAnimation(character, 20022, unknown2=1.0)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()
