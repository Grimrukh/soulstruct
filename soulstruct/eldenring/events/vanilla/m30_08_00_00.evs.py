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
    RunCommonEvent(
        0,
        90005646,
        args=(30080800, 30082840, 30082841, 30081840, 30082840, 30, 8, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=73008, obj=30081950, unknown=5.0)
    RunCommonEvent(
        0,
        90005620,
        args=(30080575, 30081575, 30081576, 0, 30082575, 30082576, 30082577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30080575, 30081578), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(30080565, 30081565, 30081566, 0, 30082565, 30082566, 30082567),
        arg_types="IIIIIIi",
    )
    Event_30082564(0, flag=30080565, obj=30081568)
    Event_30082400(0, character=30080300)
    Event_30082400(1, character=30080301)
    Event_30082400(2, character=30080302)
    RunCommonEvent(0, 90005261, args=(30080300, 30082312, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(30080301, 30002, 20002, 30082210, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(30080303, 30082303, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30080304, 30082303, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(30080305, 30082303, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(30080306, 30082303, 2.0, 0.0, 0), arg_types="IIffi")
    Event_30082400(4, character=30080303)
    Event_30082400(5, character=30080304)
    Event_30082400(6, character=30080305)
    Event_30082400(7, character=30080306)
    RunCommonEvent(0, 90005261, args=(30080307, 30082307, 2.0, 0.800000011920929, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30080308, 30082307, 2.0, 6.300000190734863, -1), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(30080309, 30082307, 2.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(30080310, 30082307, 2.0, 4.300000190734863, -1), arg_types="IIffi")
    Event_30082400(8, character=30080307)
    Event_30082400(9, character=30080308)
    Event_30082400(10, character=30080309)
    Event_30082400(11, character=30080310)
    Event_30082400(12, character=30080450)
    RunCommonEvent(0, 90005300, args=(30080450, 30080450, 0, 3.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005250, args=(30080403, 30082403, 0.0, 3022), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30080404, 30082403, 0.8999999761581421, 3022), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(30080405, 30082403, 0.5, 3022), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(30080406, 4.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(30080400, 30082400, 0.0, 3022), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(30080409, 30082409, 10.0, 0.0, 3022), arg_types="IIffi")
    RunCommonEvent(1, 90005250, args=(30080410, 30082410, 0.0, 3022), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(30080412, 30082412, 5.0, 0.0, -1), arg_types="IIffi")
    Event_30082300(0, character=30080412)
    RunCommonEvent(0, 90005261, args=(30080200, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30080201, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(30080202, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(30080203, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(4, 90005261, args=(30080204, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(5, 90005261, args=(30080205, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(6, 90005261, args=(30080206, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(7, 90005261, args=(30080207, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(8, 90005261, args=(30080208, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(9, 90005261, args=(30080209, 30082200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30080220, 30082220, 5.0, 0.0, 3035), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30080221, 30082220, 5.0, 1.0, 3035), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(30080213, 2.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(30080214, 2.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(30080225, 30082225, 5.0, 0.0, 3035), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(30080414, 7.0, 0.0, 0), arg_types="Iffi")
    Event_30082550()
    Event_30082501()
    RunCommonEvent(
        0,
        90005200,
        args=(30080461, 30000, 20000, 30082461, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30080462, 30000, 20000, 30082462, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005652, args=(30080540, 30081540, 30080400), arg_types="III")
    RunCommonEvent(0, 90005651, args=(30080540, 30081540), arg_types="II")
    Event_30082401()
    Event_30082500()
    RunCommonEvent(
        0,
        90005501,
        args=(30080510, 30081510, 3, 30081510, 30081511, 30081512, 30080511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005513, args=(30080542, 30081542, 30081543, 30083543, 27115, 0, 0), arg_types="IIIIiii")
    Event_30082510()
    Event_30082580()
    Event_30080520()
    RunCommonEvent(0, 90005525, args=(30080570, 30081570), arg_types="II")
    Event_30080790(0, obj=30081520, flag=30080800)
    Event_30082800()
    Event_30082810()
    Event_30082849()
    Event_30082811()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30080519()


@RestartOnRest(30082300)
def Event_30082300(_, character: uint):
    """Event 30082300"""
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 3009, loop=True, skip_transition=True, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character, 3012, loop=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(30082400)
def Event_30082400(_, character: uint):
    """Event 30082400"""
    IfCharacterDead(OR_2, character)
    IfThisEventSlotFlagEnabled(OR_2)
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4320)
    DisableAnimations(character)
    IfCharacterInsideRegion(OR_1, character=character, region=30082300)
    IfCharacterInsideRegion(OR_1, character=character, region=30082301)
    IfCharacterInsideRegion(OR_1, character=character, region=30082302)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableThisSlotFlag()
    AddSpecialEffect(character, 5881)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5882)
    CancelSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()


@RestartOnRest(30082401)
def Event_30082401():
    """Event 30082401"""
    EndIfFlagEnabled(30080400)
    IfCharacterDead(MAIN, 30080450)
    EnableFlag(30080400)
    End()


@NeverRestart(30082500)
def Event_30082500():
    """Event 30082500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203070, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203060, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203050, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203040, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203030, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203020, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203010, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082500, 30083500, 30081500, 30082500, 801203000, 4.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203070, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203060, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203050, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203040, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203030, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203020, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203010, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082501, 30083501, 30081501, 30082500, 801203000, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203070, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203060, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203050, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203040, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203030, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203020, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203010, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082502, 30083502, 30081502, 30082500, 801203000, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203070, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203060, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203050, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203040, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203030, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203020, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203010, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082503, 30083503, 30081503, 30082500, 801203000, 4.5, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203070, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203060, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203050, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203040, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203030, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203020, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203010, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082504, 30083504, 30081504, 30082500, 801203000, 2.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203070, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203060, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203050, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203040, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203030, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203020, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203010, 0.0, 1), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30082505, 30083505, 30081505, 30082500, 801203000, 0.0, 1), arg_types="IIIIifi")


@NeverRestart(30082510)
def Event_30082510():
    """Event 30082510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30080510,
            30081510,
            3,
            30081510,
            30081511,
            30083511,
            30081512,
            30083512,
            30082511,
            30082512,
            30080511,
            30082512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30080519)
def Event_30080519():
    """Event 30080519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30080510)


@RestartOnRest(30080520)
def Event_30080520():
    """Event 30080520"""
    EnableObjectInvulnerability(30081508)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30082508)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableObjectInvulnerability(30081508)
    End()


@NeverRestart(30082564)
def Event_30082564(_, flag: uint, obj: uint):
    """Event 30082564"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806043)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@NeverRestart(30082580)
def Event_30082580():
    """Event 30082580"""
    RegisterLadder(start_climbing_flag=30080580, stop_climbing_flag=30080581, obj=30081580)


@RestartOnRest(30082550)
def Event_30082550():
    """Event 30082550"""
    EndIfFlagEnabled(30082500)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30082460)
    IfCharacterBackreadEnabled(AND_1, 30080460)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(30082550)
    End()


@RestartOnRest(30082501)
def Event_30082501():
    """Event 30082501"""
    GotoIfFlagEnabled(Label.L0, flag=30082501)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30082450)
    IfCharacterBackreadEnabled(AND_1, 30080460)
    IfFlagEnabled(AND_1, 30082550)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(30082501)
    Wait(0.0)

    # --- Label 0 --- #
    DefineLabel(0)
    MakeEnemyAppear(character=30083460)
    EnableAI(30080460)
    End()


@RestartOnRest(30080790)
def Event_30080790(_, obj: uint, flag: uint):
    """Event 30080790"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfThisEventSlotFlagDisabled(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    EnableObjectActivation(obj, obj_act_id=-1)
    End()


@RestartOnRest(30082800)
def Event_30082800():
    """Event 30082800"""
    EndIfFlagEnabled(30080800)
    IfHealthValueLessThanOrEqual(MAIN, 30080800, value=0)
    Wait(4.0)
    PlaySoundEffect(30080800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30080800)
    KillBossAndDisplayBanner(character=30080800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30080800)
    EnableFlag(9208)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61208)


@RestartOnRest(30082810)
def Event_30082810():
    """Event 30082810"""
    GotoIfFlagDisabled(Label.L0, flag=30080800)
    DisableCharacter(30080800)
    DisableAnimations(30080800)
    Kill(30080800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30080800)
    IfFlagEnabled(AND_2, 30082805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30082800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30080800)
    SetNetworkUpdateRate(30080800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30080800, name=907100300)


@RestartOnRest(30082811)
def Event_30082811():
    """Event 30082811"""
    EndIfFlagEnabled(30080800)
    IfHealthLessThanOrEqual(AND_1, 30080800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30082802)


@RestartOnRest(30082849)
def Event_30082849():
    """Event 30082849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30080800, 30081800, 30082800, 30082805, 30085800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30080800, 30081800, 30082800, 30082805, 30082806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30080800, 30081800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30080800, 920200, 30082805, 30082806, 0, 30082802, 0, 0), arg_types="IiIIIIii")
