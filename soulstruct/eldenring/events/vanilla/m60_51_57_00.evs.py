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
    RegisterGrace(grace_flag=1051570000, obj=1051571950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76524, 76521, 1051571980, 77510, 0, 78510, 78511, 78512, 78513, 78514, 78515, 78516, 78517, 78518, 78519),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1051570001, obj=1051571951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76524, 76522, 1051571981, 77510, 1, 78510, 78511, 78512, 78513, 78514, 78515, 78516, 78517, 78518, 78519),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1051570002, obj=1051571952, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(1051570800, 1051570003, 1051570953, 1051571953, 5.0), arg_types="IIIIf")
    Event_1051572580()
    RunCommonEvent(0, 90005511, args=(1051570560, 1051571560, 1051573560, 30000, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1051570560, 1051572560, 1051572561), arg_types="III")
    Event_1051572350()
    Event_1051572350(slot=1)
    Event_1051572510()
    RunCommonEvent(
        0,
        90005501,
        args=(1051570510, 1051570511, 0, 1051571510, 1051571511, 1051571512, 1051570512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005502, args=(1051570514, 1051571512, 1051572511), arg_types="III")
    RunCommonEvent(0, 900005610, args=(1051571600, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005632, args=(580030, 1051571550, 80030), arg_types="IIi")
    Event_1051572849()
    Event_1051572800()
    Event_1051572810()
    Event_1051572811()
    Event_1051572812()
    Event_1051572820(0, character=1051570800, character_1=1051575801, special_effect=11130, animation_id=20015)
    Event_1051572821(0, character=1051570800, character_1=1051575801, special_effect=11136, animation_id=20016)
    Event_1051572822(0, character=1051570800, character_1=1051570801, character_2=1051570802, special_effect_id=11135)
    Event_1051572828(0, region=1051572829)
    Event_1051572829(0, region=1051572829)
    RunCommonEvent(
        0,
        90005211,
        args=(1051570200, 30001, 20001, 1051572200, 5.0, 1.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570201, 30000, 20000, 1051572201, 5.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570202, 30000, 20000, 1051572202, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570203, 30000, 20000, 1051572203, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570204, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(1051570205, 1051572205, 3.0, 0.699999988079071, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1051570206, 1051572206, 3.0, 0.30000001192092896, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570207, 30001, 20001, 1051572207, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570208, 30000, 20000, 1051572208, 0.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570210, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570211, 30000, 20000, 1051572211, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570212, 30000, 20000, 1051572212, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570213, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570214, 30001, 20001, 1051572214, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570216, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570217, 30000, 20000, 1051572214, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570218, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570219, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570220, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570221, 30001, 20001, 1051572200, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570222, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570223, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570224, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570225, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570226, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570227, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570228, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570229, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570240, 30002, 20011, 1051572240, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1051570241, 30002, 20011, 1051572241, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1051570242, 1051572242, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1051570243, 1051572242, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1051570244, 1051572242, 0.5, 0.0, 0), arg_types="IIffi")
    Event_1051572250(0, 1051570272, 30010, 20010, 0, 1.0, 0.0, 0, 0, 0, 0, 1051570240)
    Event_1051572250(5, 1051570215, 30001, 20001, 0, 2.5, 0.0, 0, 0, 0, 0, 1051570241)
    Event_1051572250(6, 1051570209, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0, 1051570241)
    Event_1051572250(7, 1051570250, 30001, 20001, 0, 2.5, 0.0, 0, 0, 0, 0, 1051570241)
    Event_1051572250(8, 1051570255, 30000, 20000, 0, 4.5, 0.0, 0, 0, 0, 0, 1051570241)
    RunCommonEvent(
        0,
        90005211,
        args=(1051570251, 30001, 20001, 1051572251, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570252, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570253, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570254, 30001, 20001, 1051572254, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570256, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570257, 30001, 20001, 1051572257, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1051570258, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570259, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570270, 30011, 20011, 1051572270, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1051570271, 1051572271, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(1051570273, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_1051572274(0, 1051570274, 30011, 20011, 1051572274, 5.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005211, args=(1051570276, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570277, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570278, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570279, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570280, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570281, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570282, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570283, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570284, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570285, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570286, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570287, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570288, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570289, 30010, 20010, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(1051570395, 1051572275, 3.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1051570315, 1051572315, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(1051570315, 1051570315, 40508, 0.0, 0), arg_types="IIifi")
    Event_1051572310(0, 1051570311, 30000, 20000, 1051572310, 5.0, 0.0, 0, 0, 0, 0)
    Event_1051572311(0, character=1051570311, special_effect_id=13360)
    RunCommonEvent(0, 90005300, args=(1051570310, 1051570310, 1051570800, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1051570311, 1051570311, 1051570810, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(1051570370, 1051572370, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570372, 30000, 20000, 1051572372, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1051570374, 1051572370, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(1051570381, 30000, 20000, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051570383, 30000, 20000, 0, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(1051570385, 1051572385, 5.0, 0.0, 0), arg_types="IIffi")
    Event_1051572450(0, character=1051570430, special_effect_id=5021)
    Event_1051572430(0, character=1051570430, region=1051572430, flag=1051572440)
    Event_1051572430(1, character=1051570431, region=1051572430, flag=1051572441)
    Event_1051572430(2, character=1051570432, region=1051572430, flag=1051572442)
    Event_1051572430(3, character=1051570433, region=1051572430, flag=1051572443)
    Event_1051572430(6, character=1051570436, region=1051572430, flag=1051572446)
    Event_1051572430(7, character=1051570437, region=1051572430, flag=1051572447)
    RunCommonEvent(0, 90005211, args=(1051570430, 30000, 20000, 0, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005300, args=(1051570421, 1051570421, 1051570720, 0.0, 0), arg_types="IIifi")
    Event_1051572460(0, character=1051570421, character_1=1051570430, special_effect=15335)
    Event_1051572460(1, character=1051570421, character_1=1051570431, special_effect=15335)
    Event_1051572460(2, character=1051570421, character_1=1051570432, special_effect=15335)
    Event_1051572460(3, character=1051570421, character_1=1051570433, special_effect=15335)
    Event_1051572460(6, character=1051570421, character_1=1051570436, special_effect=15335)
    Event_1051572460(7, character=1051570421, character_1=1051570437, special_effect=15335)
    Event_1051572460(9, character=1051570421, character_1=1050570320, special_effect=15335)
    RunCommonEvent(0, 90005616, args=(1051577720, 1051572700), arg_types="II")
    RunCommonEvent(
        0,
        90005211,
        args=(1051570368, 30000, 20000, 1051572368, 0.0, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005706, args=(1051570710, 930025, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1051570700)
    DisableBackread(1051570710)
    Event_1051570519()


@NeverRestart(1051572510)
def Event_1051572510():
    """Event 1051572510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1051570510,
            1051570511,
            0,
            1051571510,
            1051571511,
            1051573511,
            1051571512,
            1051573512,
            1051572511,
            1051572512,
            1051570512,
            1051570513,
            1051570514,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1051570519)
def Event_1051570519():
    """Event 1051570519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(1051570510)
    DisableThisSlotFlag()


@RestartOnRest(1051572430)
def Event_1051572430(_, character: uint, region: uint, flag: uint):
    """Event 1051572430"""
    IfCharacterAlive(AND_15, character)
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    IfCharacterBackreadEnabled(AND_14, character)
    AwaitConditionTrue(AND_14)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterType(AND_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfAllPlayersOutsideRegion(AND_2, region=region)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    AddSpecialEffect(character, 15338)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterType(AND_5, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_5, PLAYER, 3710)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfCharacterHuman(OR_5, PLAYER)
    IfCharacterHollow(OR_5, PLAYER)
    IfCharacterWhitePhantom(OR_5, PLAYER)
    IfConditionTrue(AND_6, input_condition=OR_5)
    IfCharacterInsideRegion(AND_6, character=PLAYER, region=region)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfFlagDisabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    DisableNetworkFlag(flag)
    AddSpecialEffect(character, 15339)
    Wait(3.0)
    Restart()


@RestartOnRest(1051572450)
def Event_1051572450(_, character: uint, special_effect_id: int):
    """Event 1051572450"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1051572460)
def Event_1051572460(_, character: uint, character_1: uint, special_effect: int):
    """Event 1051572460"""
    GotoIfFlagDisabled(Label.L0, flag=1051570421)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueEqual(MAIN, character, value=0)
    IfCharacterHasSpecialEffect(AND_1, character_1, special_effect)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Kill(character_1, award_souls=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Kill(character_1, award_souls=True)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1051572250)
def Event_1051572250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    seconds_1: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    character_1: uint,
):
    """Event 1051572250"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfCharacterHasSpecialEffect(OR_3, character_1, 17126)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds_1)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()
    Wait(seconds)


@RestartOnRest(1051572274)
def Event_1051572274(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1051572274"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfHealthLessThanOrEqual(AND_1, 1051570272, value=0.4000000059604645)
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
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1051572310)
def Event_1051572310(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1051572310"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfHealthLessThanOrEqual(OR_3, 1051570310, value=0.5)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1051572311)
def Event_1051572311(_, character: uint, special_effect_id: int):
    """Event 1051572311"""
    EndIfThisEventSlotFlagEnabled()
    DisableHealthBar(character)
    AddSpecialEffect(character, special_effect_id)
    Wait(0.10000000149011612)
    EnableHealthBar(character)
    End()


@RestartOnRest(1051572350)
def Event_1051572350():
    """Event 1051572350"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1051570350)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1051572350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1051570350,
        source_entity=1051572351,
        model_point=900,
        behavior_id=802105070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1051572580)
def Event_1051572580():
    """Event 1051572580"""
    RegisterLadder(start_climbing_flag=1051570580, stop_climbing_flag=1051570581, obj=1051571580)
    RegisterLadder(start_climbing_flag=1051570582, stop_climbing_flag=1051570583, obj=1051571582)
    RegisterLadder(start_climbing_flag=1051570584, stop_climbing_flag=1051570585, obj=1051571584)
    RegisterLadder(start_climbing_flag=1051570590, stop_climbing_flag=1051570591, obj=1051571590)
    RegisterLadder(start_climbing_flag=1051570592, stop_climbing_flag=1051570593, obj=1051571592)
    RegisterLadder(start_climbing_flag=1051570594, stop_climbing_flag=1051570595, obj=1051571594)


@NeverRestart(1051572800)
def Event_1051572800():
    """Event 1051572800"""
    EndIfFlagEnabled(1051570800)
    IfHealthLessThanOrEqual(MAIN, 1051570800, value=0.0)
    IfCharacterDead(MAIN, 1051570800)
    KillBossAndDisplayBanner(character=1051570800, banner_type=BannerType.Unknown)
    EnableFlag(1051570800)
    EnableFlag(9184)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61184)


@RestartOnRest(1051572810)
def Event_1051572810():
    """Event 1051572810"""
    GotoIfFlagDisabled(Label.L0, flag=1051570800)
    DisableCharacter(1051570800)
    DisableAnimations(1051570800)
    Kill(1051570800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1051570800)
    GotoIfFlagEnabled(Label.L1, flag=1051570801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1051572801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=1051570800, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=1051570800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1051570800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1051570800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1051570800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=1051570800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(1051570801)
    ForceAnimation(1051570800, 20010, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 1051572805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1051572800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(1051570800, 20010, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1051570800)
    SetNetworkUpdateRate(1051575800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1051570800, name=903050500)


@RestartOnRest(1051572811)
def Event_1051572811():
    """Event 1051572811"""
    EndIfFlagEnabled(1051570800)
    IfCharacterHasSpecialEffect(AND_1, 1051570800, 11155)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1051572802)


@RestartOnRest(1051572812)
def Event_1051572812():
    """Event 1051572812"""
    DisableNetworkSync()
    EndIfFlagEnabled(1051570800)
    IfFlagDisabled(AND_1, 1051570800)
    IfHealthValueNotEqual(AND_1, 1051570800, value=0)
    IfCharacterHasSpecialEffect(AND_1, 1051570800, 11135)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 1051570800, 11135)
    IfConditionTrue(MAIN, input_condition=AND_2)
    IfHealthValueEqual(OR_15, 1051570800, value=0)
    EndIfConditionTrue(input_condition=OR_15)
    Restart()


@RestartOnRest(1051572820)
def Event_1051572820(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1051572820"""
    GotoIfFlagDisabled(Label.L0, flag=1051570800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character_1)
    DisableCharacter(character_1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    ForceAnimation(character_1, animation_id, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(1051572821)
def Event_1051572821(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1051572821"""
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(OR_1, character, special_effect)
    IfCharacterDead(OR_1, character)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(character_1, animation_id, skip_transition=True, unknown2=1.0)
    WaitFrames(frames=300)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()


@RestartOnRest(1051572822)
def Event_1051572822(_, character: uint, character_1: uint, character_2: uint, special_effect_id: int):
    """Event 1051572822"""
    EndIfFlagEnabled(character)
    IfCharacterDead(AND_1, character_1)
    IfCharacterDead(AND_1, character_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1051572828)
def Event_1051572828(_, region: uint):
    """Event 1051572828"""
    EndIfFlagEnabled(1051570800)
    IfCharacterInsideRegion(AND_2, character=35000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(35000, 10859)


@RestartOnRest(1051572829)
def Event_1051572829(_, region: uint):
    """Event 1051572829"""
    EndIfFlagEnabled(1051570800)
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(20000, 10859)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_3, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 10859)
    Restart()


@NeverRestart(1051572849)
def Event_1051572849():
    """Event 1051572849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1051570800, 1051571800, 1051572800, 1051572805, 1051575800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1051570800, 1051571800, 1051572800, 1051572805, 1051572806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1051570800, 1051571800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1051570800, 1051571801, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1051570800, 950000, 1051572805, 1051572806, 0, 1051572802, 0, 0),
        arg_types="IiIIIIii",
    )


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunEvent(1051572581, slot=0, args=(0,))
    RunCommonEvent(0, 90005451, args=(1251570400, 1251576420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1251570400, 1251570400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1251570400, 1251572400, 1251570400), arg_types="III")
    RunCommonEvent(0, 90005458, args=(1251570400, 1251571401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571420, 101, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1251570400, 1251571421, 102, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571422, 103, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571423, 104, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571424, 105, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571425, 106, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571426, 107, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571427, 108, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571428, 109, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571429, 110, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571430, 111, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571436, 117, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571437, 118, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571438, 119, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571439, 120, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571440, 121, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571441, 122, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571442, 123, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571443, 124, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571444, 125, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571445, 126, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571446, 127, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571447, 128, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571452, 133, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571453, 134, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571454, 135, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571455, 136, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571456, 137, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571457, 138, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571458, 139, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571459, 140, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571460, 141, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571461, 142, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571468, 149, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571469, 150, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571470, 151, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571471, 152, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571472, 153, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571473, 154, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571474, 155, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571475, 156, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571476, 157, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571477, 158, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1251570400, 1251571478, 159, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005456, args=(1251570400, 1251571410, 1251571418, 1251570400), arg_types="IIII")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1251570400, 1251571400, 1251571410, 1251571418), arg_types="IIII")
