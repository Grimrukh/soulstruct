"""
Land of Shadow 12-11 SE NE

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2051450000, asset=2051451950)
    Event_2051452810(0, character=2051450701)
    Event_2051452811(0, character=2051450701)
    Event_2051452812(0, character=2051450720)
    Event_2051452800(0, character=2051450720)
    Event_2051452849()
    Event_2051452311()
    Event_2051452814(0, character=2051450720)
    Event_2051452310()
    Event_2051452320(0, character=2051450300, flag=2051452300)
    Event_2051452320(1, character=2051450301, flag=2051452301)
    Event_2051452320(2, character=2051450302, flag=2051452302)
    Event_2051452320(3, character=2051450303, flag=2051452303)
    Event_2051452320(4, character=2051450304, flag=2051452304)
    Event_2051452320(5, character=2051450305, flag=2051452305)
    Event_2051452320(6, character=2051450306, flag=2051452306)
    Event_2051452320(7, character=2051450307, flag=2051452307)
    Event_2051452320(8, character=2051450308, flag=2051452308)
    Event_2051452320(9, character=2051450309, flag=2051452309)
    Event_2051452839()
    CommonFunc_90005250(0, character=2051450221, region=2051452221, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2051450222, region=2051452222, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2051450223, region=2051452223, seconds=0.0, animation_id=-1)
    Event_2051452205(
        0,
        character=2051450250,
        region=2051452250,
        region_1=2051452270,
        radius=2.0,
        character_1=2051450251,
    )
    Event_2051452200(
        0,
        character=2051450390,
        special_effect=12603,
        region=2051452399,
        region_1=2051452398,
        region_2=2051452397,
    )
    CommonFunc_90005300(0, flag=2051450390, character=2051450390, item_lot=40906, seconds=0.0, left=0)
    Event_2051452600()
    Event_2051452601()
    Event_2051452698()
    Event_2051452580()
    CommonFunc_90005515(0, flag=2051458560, anchor_entity=2051451560)
    CommonFunc_900005610(0, asset=2051451654, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2051451655, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2051451656, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2051451657, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2051450180,
        summon_flag=2051452181,
        dismissal_flag=2051452182,
        character=2051450730,
        sign_type=22,
        region=2051452730,
        region_1=2051452731,
        seconds=0.0,
        right_1=2051459739,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2051450180, flag_1=2051452181, flag_2=2051452182, character=2051450730)
    CommonFunc_90005792(
        0,
        flag=2051450180,
        flag_1=2051452181,
        flag_2=2051452182,
        character=2051450730,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2051450180,
        flag_1=2051452181,
        flag_2=2051452182,
        character=2051450730,
        other_entity=2051452730,
        region=2051452732,
        left=0,
    )
    CommonFunc_90005774(0, flag=2051450180, item_lot=106720, flag_1=400672)
    Event_2051450700(
        0,
        character=2051450700,
        flag=4320,
        flag_1=4325,
        animation_id=90100,
        flag_2=2051452730,
        flag_3=2051459722,
        flag_4=4338,
        flag_5=2051450800,
        flag_6=2051459725,
    )
    Event_2051450702(0, flag=4320, flag_1=2051452730, flag_2=4338)
    Event_2051450722(0, flag=2051459721, flag_1=2051450180)
    CommonFunc_90005734(
        0,
        flag=4325,
        flag_1=2051459739,
        region=2051452731,
        region_1=2051452731,
        flag_2=2051459739,
        right=-1,
    )
    Event_2051450704(
        0,
        character=2051450701,
        flag=4322,
        flag_1=4323,
        flag_2=4326,
        flag_3=4338,
        distance=60.0,
        flag_4=2051452706,
    )
    Event_2051450701(
        0,
        character=2051450702,
        flag=4320,
        flag_1=4326,
        animation_id=90102,
        flag_2=2051450800,
        flag_3=2051459747,
        flag_4=2051459748,
        animation_id_1=90105,
        flag_5=2051459732,
    )
    Event_2051450706(
        0,
        entity=2051451500,
        action_button_id=209523,
        flag=2051459724,
        flag_1=2051452706,
        flag_2=2051450800,
        flag_3=25000800,
    )
    Event_2051450705(0, flag=2051452709, flag_1=2051452811, flag_2=2051450800, flag_3=2051452701)
    Event_2051450721(
        0,
        character=2051450702,
        flag=2051459747,
        flag_1=2051459748,
        seconds=10.0,
        animation_id=90205,
        seconds_1=4.0,
        flag_2=2051459734,
        flag_3=2051459742,
        seconds_2=10.0,
    )
    CommonFunc_90005750(
        0,
        asset=2051451703,
        action_button_id=4350,
        item_lot=106710,
        first_flag=400671,
        last_flag=400671,
        flag=2051459742,
        vfx_id=6102,
    )
    Event_2051450707(
        0,
        flag=2051452720,
        flag_1=2051452721,
        left=2051452722,
        character=2051450702,
        dummy_id=711,
        asset=2051451702,
        dummy_id_1=711,
        radius=0.3499999940395355,
        animation=90216,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
        seconds=2.4000000953674316,
        flag_2=2051459727,
        flag_3=2051452725,
        flag_4=2051459729,
        seconds_1=0.05000000074505806,
        flag_5=2051459743,
        animation_1=90217,
        flag_6=2051459744,
    )
    Event_2051450708(
        0,
        flag=2051452723,
        flag_1=2051452724,
        left=2051452722,
        character=2051450702,
        animation__animation_id=90202,
        left_1=1,
        left_2=-1,
        special_effect=9600,
        seconds=0.0,
        flag_2=2051459743,
        animation__animation_id_1=90203,
        flag_3=2051459744,
    )
    Event_2051450709(0, flag=2051452725, flag_1=2051459728, seconds=0.05000000074505806)
    Event_2051450703(0, flag=4323, flag_1=2051452705, flag_2=4338)
    Event_2051450710(
        0,
        character=2051450710,
        flag=4500,
        flag_1=4505,
        animation_id=90100,
        flag_2=2051452719,
        flag_3=2051459725,
        flag_4=2051459223,
        flag_5=2051459214,
        flag_6=2051459215,
        flag_7=2051459209,
        flag_8=2051459225,
        animation_id_1=90101,
        distance=55.0,
        left=2051452711,
        flag_9=2051452718,
        flag_10=2051459234,
    )
    Event_2051450711(
        0,
        character=2051450720,
        flag=4506,
        flag_1=4502,
        flag_2=4503,
        flag_3=2051452709,
        distance=90.0,
        flag_4=2051452701,
    )
    Event_2051450715(
        0,
        asset=2051451500,
        animation_id=1,
        obj_act_id=464032,
        flag=2051450800,
        flag_1=2051459213,
        flag_2=2051459725,
        flag_3=25000800,
        flag_4=4506,
        flag_5=2051452719,
        flag_6=2051459230,
        obj_act_id_1=2051453570,
    )
    Event_2051450712(
        0,
        flag=4505,
        flag_1=2051459725,
        region=2051452716,
        region_1=2051452716,
        flag_2=2051452719,
        asset=2051451500,
        animation_id=1,
        obj_act_id=464032,
        flag_3=2051459217,
    )
    Event_2051450713(0, flag=2051459217, flag_1=2051452719, flag_2=2051459725)
    Event_2051450714(0, flag=2051459205, flag_1=2051452730)
    Event_2051450716(0, flag=2051459203, flag_1=2051452731, flag_2=2051452732)
    Event_2051450717(0, flag=25000800, flag_1=2051452732)
    Event_2051450718(0, flag=2051450800, flag_1=2051452731)
    Event_2051450719(0, flag=2051459206, flag_1=2050400600, flag_2=2053460600)
    CommonFunc_90005747(
        0,
        flag=2051450800,
        flag_1=4506,
        flag_2=2051452734,
        seconds=30.0,
        flag_3=2051452733,
        flag_4=0,
        seconds_1=0.0,
    )
    CommonFunc_90005734(
        0,
        flag=4505,
        flag_1=2051459238,
        region=2051452715,
        region_1=2051452715,
        flag_2=2051452714,
        right=0,
    )
    CommonFunc_90005734(
        0,
        flag=4505,
        flag_1=2051459225,
        region=2051452710,
        region_1=2051452710,
        flag_2=2051452713,
        right=0,
    )
    CommonFunc_90005734(
        0,
        flag=4505,
        flag_1=2051459216,
        region=2051452716,
        region_1=2051452716,
        flag_2=2051459216,
        right=-1,
    )
    CommonFunc_90005744(0, entity=2051450710, flag=2051459246, flag_1=2051459246, animation_id=90200)
    CommonFunc_90005744(0, entity=2051450710, flag=2051459202, flag_1=2051459202, animation_id=90204)
    CommonFunc_90005744(0, entity=2051450710, flag=2051459201, flag_1=2051459201, animation_id=90205)
    CommonFunc_90005744(0, entity=2051450710, flag=2051459249, flag_1=2051459249, animation_id=90200)
    CommonFunc_90005744(0, entity=2051450710, flag=2051459248, flag_1=2051459248, animation_id=90201)
    CommonFunc_90005702(0, character=2051450720, flag=4503, first_flag=4500, last_flag=4504)
    Event_2051450725(0, flag=2051459250, flag_1=2051452739, flag_2=2051450800)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005301(0, flag=2251450280, character=2251450280, item_lot__unk1=2051450700, seconds=4.0, unk1=0)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005431(0, character=2251450280)
    CommonFunc_90005432(0, character=2251450280, flag=2251452280)
    CommonFunc_90005435(
        0,
        character=2251450280,
        flag=2251452281,
        flag_1=2251452282,
        flag_2=2251452283,
        flag_3=2251452284,
    )
    CommonFunc_90005436(0, character=2251450280, region=2051452291, region_1=2051452292)
    CommonFunc_90005437(0, character=2251450280, flag=2251452288, flag_1=2251452289)


@ContinueOnRest(2051452200)
def Event_2051452200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 2051452200"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    DisableFlag(2051452201)
    DisableFlag(2051452202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(2051452201, 2051452202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 2051452201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 2051452201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 2051452201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(2051452205)
def Event_2051452205(
    _,
    character: uint,
    region: Region | int,
    region_1: Region | int,
    radius: float,
    character_1: uint,
):
    """Event 2051452205"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=20011469):
        AddSpecialEffect(character, 20011469)
    DisableAnimations(character_1)
    DisableGravity(character_1)
    DisableAI(character_1)
    SetLockOnPoint(character=character_1, lock_on_dummy_id=220, state=False)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_4.Add(OR_2)
    GotoIfConditionFalse(Label.L0, input_condition=OR_4)
    AddSpecialEffect(character_1, 20013351)
    ForceAnimation(character, 3020)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 20011467)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5025):
        ForceAnimation(character, 3000)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(2051452310)
def Event_2051452310():
    """Event 2051452310"""
    if FlagDisabled(2051452300):
        ForceAnimation(2051450300, 30000)
    if FlagDisabled(2051452301):
        ForceAnimation(2051450301, 30000)
    if FlagDisabled(2051452302):
        ForceAnimation(2051450302, 30000)
    if FlagDisabled(2051452303):
        ForceAnimation(2051450303, 30000)
    if FlagDisabled(2051452304):
        ForceAnimation(2051450304, 30000)
    if FlagDisabled(2051452305):
        ForceAnimation(2051450305, 30000)
    if FlagDisabled(2051452306):
        ForceAnimation(2051450306, 30000)
    if FlagDisabled(2051452307):
        ForceAnimation(2051450307, 30000)
    if FlagDisabled(2051452308):
        ForceAnimation(2051450308, 30000)
    if FlagDisabled(2051452309):
        ForceAnimation(2051450309, 30000)
    AND_1.Add(CharacterHasSpecialEffect(2051450720, 20018650))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(2051452300):
        EnableFlag(2051452300)
        SetLockOnPoint(character=2051450300, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450300)
        ForceAnimation(2051450300, 20006)
        Move(
            2051450300,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450300)
        SetNetworkUpdateRate(2051450300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452301):
        EnableFlag(2051452301)
        SetLockOnPoint(character=2051450301, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450301)
        ForceAnimation(2051450301, 20006)
        Move(
            2051450301,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450301)
        SetNetworkUpdateRate(2051450301, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452302):
        EnableFlag(2051452302)
        SetLockOnPoint(character=2051450302, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450302)
        ForceAnimation(2051450302, 20006)
        Move(
            2051450302,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450302)
        SetNetworkUpdateRate(2051450302, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452303):
        EnableFlag(2051452303)
        SetLockOnPoint(character=2051450303, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450303)
        ForceAnimation(2051450303, 20006)
        Move(
            2051450303,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450303)
        SetNetworkUpdateRate(2051450303, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452304):
        EnableFlag(2051452304)
        SetLockOnPoint(character=2051450304, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450304)
        ForceAnimation(2051450304, 20006)
        Move(
            2051450304,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450304)
        SetNetworkUpdateRate(2051450304, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452305):
        EnableFlag(2051452305)
        SetLockOnPoint(character=2051450305, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450305)
        ForceAnimation(2051450305, 20006)
        Move(
            2051450305,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450305)
        SetNetworkUpdateRate(2051450305, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452306):
        EnableFlag(2051452306)
        SetLockOnPoint(character=2051450306, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450306)
        ForceAnimation(2051450306, 20006)
        Move(
            2051450306,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450306)
        SetNetworkUpdateRate(2051450306, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452307):
        EnableFlag(2051452307)
        SetLockOnPoint(character=2051450307, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450307)
        ForceAnimation(2051450307, 20006)
        Move(
            2051450307,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450307)
        SetNetworkUpdateRate(2051450307, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452308):
        EnableFlag(2051452308)
        SetLockOnPoint(character=2051450308, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450308)
        ForceAnimation(2051450308, 20006)
        Move(
            2051450308,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450308)
        SetNetworkUpdateRate(2051450308, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)
    if FlagDisabled(2051452309):
        EnableFlag(2051452309)
        SetLockOnPoint(character=2051450309, lock_on_dummy_id=220, state=True)
        IncrementEventValue(2051452312, bit_count=5, max_value=10)
        EnableAI(2051450309)
        ForceAnimation(2051450309, 20006)
        Move(
            2051450309,
            destination=2051450720,
            destination_type=CoordEntityType.Character,
            dummy_id=615,
            short_move=True,
        )
        ActivateMultiplayerBuffs(2051450309)
        SetNetworkUpdateRate(2051450309, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(2051452311)
def Event_2051452311():
    """Event 2051452311"""
    if PlayerNotInOwnWorld():
        return
    AddSpecialEffect(2051450720, 20018693)
    RemoveSpecialEffect(2051450720, 20018711)
    
    MAIN.Await(EventValue(flag=2051452312, bit_count=5) >= 8)
    
    RemoveSpecialEffect(2051450720, 20018693)
    AddSpecialEffect(2051450720, 20018711)
    
    MAIN.Await(EventValue(flag=2051452312, bit_count=5) < 8)
    
    Restart()


@RestartOnRest(2051452320)
def Event_2051452320(_, character: uint, flag: Flag | int):
    """Event 2051452320"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterDead(character))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    ForceAnimation(character, 30000)
    Wait(3.0)
    DisableNetworkFlag(flag)
    EventValueOperation(
        source_flag=2051452312,
        source_flag_bit_count=5,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    Restart()


@RestartOnRest(2051452698)
def Event_2051452698():
    """Event 2051452698"""
    DisableNetworkSync()
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=2051452698))
    AND_1.Add(FlagDisabled(2051452820))
    AND_1.Add(FlagEnabled(2051459203))
    OR_15.Add(AND_1)
    
    MAIN.Await(OR_15)
    
    AddSpecialEffect(ALL_PLAYERS, 9621)
    Wait(0.10000000149011612)
    OR_6.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=2051452698))
    OR_6.Add(Invasion())
    OR_6.Add(FlagEnabled(2051452820))
    OR_6.Add(FlagDisabled(2051459203))
    
    MAIN.Await(OR_6)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(ALL_PLAYERS, 9621)
    Restart()


@RestartOnRest(2051452810)
def Event_2051452810(_, character: uint):
    """Event 2051452810"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(2051450800):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    WaitFrames(frames=1)
    AND_1.Add(FlagEnabled(2051452424))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    BanishInvaders(unknown=0)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableInvincibility(character)
    ForceAnimation(character, 90200, wait_for_completion=True)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.Enemy)
    SetCharacterEventTarget(character, entity=PLAYER)
    DisplayNetworkMessage(text=4080830, unk_4_5=False)
    EnableNetworkFlag(2051452820)
    End()


@RestartOnRest(2051452811)
def Event_2051452811(_, character: Character | int):
    """Event 2051452811"""
    if FlagEnabled(2051450800):
        return
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.0)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)

    # --- Label 10 --- #
    DefineLabel(10)
    Wait(5.0)
    EnableFlag(2051452811)
    DisplayNetworkMessage(text=4080832, unk_4_5=False)
    End()


@RestartOnRest(2051452812)
def Event_2051452812(_, character: uint):
    """Event 2051452812"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(2051450800):
        return
    AddSpecialEffect(character, 18677)
    EnableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    AND_1.Add(FlagEnabled(2051452709))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    EnableCharacter(character)
    EnableAnimations(character)
    AddSpecialEffect(character, 18677)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    Wait(4.0)
    RemoveSpecialEffect(character, 18677)
    EnableInvincibility(character)
    ForceAnimation(character, 90202, wait_for_completion=True)
    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(2051452813)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableBossHealthBar(character, name=142001)
    SetTeamType(character, TeamType.Enemy)
    SetCharacterEventTarget(character, entity=PLAYER)
    End()


@RestartOnRest(2051452814)
def Event_2051452814(_, character: uint):
    """Event 2051452814"""
    if FlagEnabled(2051450800):
        return
    if PlayerInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(2051452813))
    
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableBossHealthBar(character, name=142001)
    SetTeamType(character, TeamType.Enemy)


@RestartOnRest(2051452800)
def Event_2051452800(_, character: Character | int):
    """Event 2051452800"""
    if FlagEnabled(2051450800):
        return
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.0)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    Kill(2051455300)

    # --- Label 10 --- #
    DefineLabel(10)
    Wait(8.0)
    EnableFlag(2051450800)
    DisableNetworkFlag(2051452820)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    End()


@RestartOnRest(2051452839)
def Event_2051452839():
    """Event 2051452839"""
    if PlayerNotInOwnWorld():
        return
    EnableFlag(2051450839)
    if FlagEnabled(2051450800):
        return
    if FlagDisabled(25000800):
        return
    DisableFlag(2051450839)
    
    MAIN.Await(FlagEnabled(2051450800))
    
    DisableFlag(2051450839)
    End()


@RestartOnRest(2051452840)
def Event_2051452840():
    """Event 2051452840"""
    GotoIfFlagEnabled(Label.L10, flag=2051450800)
    WaitFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(2051452424))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(2051450800))
    
    MAIN.Await(OR_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    BanishInvaders(unknown=0)
    if FlagEnabled(2051450800):
        return RESTART

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2051455800, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(2051455800)
    EnableNetworkFlag(2051452805)
    if PlayerNotInOwnWorld():
        return
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    End()


@RestartOnRest(2051452841)
def Event_2051452841(_, entity: uint, region: uint):
    """Event 2051452841"""
    DisableNetworkSync()
    if FlagEnabled(2051450800):
        return
    if PlayerInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(2051452805))
    
    AND_1.Add(FlagDisabled(2051450800))
    AND_1.Add(FlagEnabled(2051452805))
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_1.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=2051452699))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterInsideRegion(Label.L5, character=PLAYER, region=2051452699)
    SuppressSoundForFogGate(duration=5.0)
    FaceEntityAndForceAnimation(PLAYER, region, animation=60060, wait_for_completion=True)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    if LastResult(OR_1):
        return RESTART

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(2051452806)
    Restart()


@RestartOnRest(2051452844)
def Event_2051452844(_, asset: Asset | int, vfx_id: int):
    """Event 2051452844"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    AND_1.Add(FlagEnabled(2051452424))
    AND_1.Add(FlagDisabled(2051450800))
    
    MAIN.Await(AND_1)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    AND_3.Add(FlagEnabled(2051452424))
    AND_3.Add(FlagEnabled(2051450800))
    
    MAIN.Await(AND_3)
    
    Restart()


@RestartOnRest(2051452849)
def Event_2051452849():
    """Event 2051452849"""
    Event_2051452840()
    Event_2051452841(0, entity=2051451800, region=2051452800)
    Event_2051452841(1, entity=2051451801, region=2051452801)
    Event_2051452841(2, entity=2051451802, region=2051452802)
    Event_2051452844(0, asset=2051451800, vfx_id=3)
    Event_2051452844(1, asset=2051451801, vfx_id=3)
    Event_2051452844(2, asset=2051451802, vfx_id=1570)


@ContinueOnRest(2051452600)
def Event_2051452600():
    """Event 2051452600"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L9, flag=9440)
    GotoIfFlagDisabled(Label.L9, flag=2051450180)
    DisableNetworkFlag(2051452602)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=2051453600))
    
    MAIN.Await(AND_1)
    
    BanishInvaders(unknown=0)
    Wait(10.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=25002600,
        dummy_id=-1,
        copy_draw_parent=25000800,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(3.0)
    EnableAssetActivation(2051451600, obj_act_id=52407)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    DisableAssetActivation(2051451600, obj_act_id=52407)
    AND_15.Add(FlagEnabled(9440))
    AND_15.Add(FlagEnabled(2051450180))
    
    MAIN.Await(AND_15)
    
    EnableAssetActivation(2051451600, obj_act_id=52407)
    Restart()


@RestartOnRest(2051452601)
def Event_2051452601():
    """Event 2051452601"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    AND_1.Add(FlagEnabled(2051452602))
    
    MAIN.Await(AND_1)
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=ALL_PLAYERS,
        destination_type=CoordEntityType.Region,
        destination=25002601,
        dummy_id=10,
        copy_draw_parent=25000800,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    EnableFlag(25002806)
    End()


@ContinueOnRest(2051452580)
def Event_2051452580():
    """Event 2051452580"""
    RegisterLadder(start_climbing_flag=2051450580, stop_climbing_flag=2051450581, asset=2051451580)


@RestartOnRest(2051450700)
def Event_2051450700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 2051450700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    SkipLinesIfFlagDisabled(6, flag_1)
    AND_10.Add(FlagEnabled(flag_5))
    SkipLinesIfConditionFalse(1, AND_10)
    Goto(Label.L20)
    AND_11.Add(FlagEnabled(flag_6))
    SkipLinesIfConditionFalse(1, AND_11)
    Goto(Label.L20)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_5.Add(FlagDisabled(flag_2))
    SkipLinesIfConditionFalse(1, AND_5)
    Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    DisableGravity(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    WaitRealFrames(frames=1)
    Move(character, destination=2051452700, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(flag_3)
    ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.FriendlyNPC)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_1))
    OR_10.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(2051450701)
def Event_2051450701(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    animation_id_1: int,
    flag_5: Flag | int,
):
    """Event 2051450701"""
    DisableNetworkSync()
    WaitRealFrames(frames=2)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(flag_5):
        EnableFlag(flag_5)
        End()
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(flag_3):
        return
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    WaitRealFrames(frames=1)
    AND_5.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_5)
    
    Move(character, destination=2051452702, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=1)
    if FlagEnabled(flag_4):
        ForceAnimation(character, animation_id_1)
        Goto(Label.L20)
    ForceAnimation(character, animation_id)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_1))
    OR_10.Add(FlagDisabled(flag_2))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(2051450702)
def Event_2051450702(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag_2)
    End()


@RestartOnRest(2051450703)
def Event_2051450703(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag_2)
    End()


@RestartOnRest(2051450704)
def Event_2051450704(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    distance: float,
    flag_4: Flag | int,
):
    """Event 2051450704"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag_4))
    
    SetCharacterTalkRange(character=character, distance=distance)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L3, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_2))
    OR_10.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(2051450705)
def Event_2051450705(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 2051450705"""
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    End()


@RestartOnRest(2051450706)
def Event_2051450706(
    _,
    entity: uint,
    action_button_id: int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 2051450706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    if FlagDisabled(flag_3):
        return
    DisableFlag(flag)
    DisableNetworkFlag(2051452424)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    EnableFlag(flag)
    EnableNetworkFlag(flag_1)
    EnableNetworkFlag(2051452424)
    Wait(1.0)
    End()


@RestartOnRest(2051450707)
def Event_2051450707(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    seconds: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds_1: float,
    flag_5: Flag | int,
    animation_1: int,
    flag_6: Flag | int,
):
    """Event 2051450707"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_4)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLinesIfConditionFalse(3, AND_1)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    SkipLinesIfConditionFalse(3, AND_15)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    DisableFlag(flag_2)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfValueEqual(5, left=dummy_id, right=0)
    ResetAnimation(PLAYER)
    SkipLinesIfFlagEnabled(3, flag_4)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    Goto(Label.L15)
    EnableFlag(flag_3)
    Wait(seconds_1)

    # --- Label 15 --- #
    DefineLabel(15)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    if FlagEnabled(flag_5):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
        Goto(Label.L8)
    if FlagEnabled(flag_6):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation_1, wait_for_completion=True)
        Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2051450708)
def Event_2051450708(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    left_2: int,
    special_effect: int,
    seconds: float,
    flag_2: Flag | int,
    animation__animation_id_1: int,
    flag_3: Flag | int,
):
    """Event 2051450708"""
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    SkipLinesIfValueEqual(5, left=special_effect, right=-1)
    SkipLinesIfFlagDisabled(1, flag_2)
    ForceAnimation(character, animation__animation_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    ForceAnimation(character, animation__animation_id_1)
    SkipLines(1)
    if FlagEnabled(flag_2):
        ForceAnimation(character, animation__animation_id)
    if FlagEnabled(flag_3):
        ForceAnimation(character, animation__animation_id_1)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(5, left=special_effect, right=-1)
    SkipLinesIfFlagDisabled(1, flag_2)
    FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id_1)
    SkipLines(1)
    if FlagEnabled(flag_2):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    if FlagEnabled(flag_3):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id_1)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_1.Add(FlagDisabled(flag))
    if ValueNotEqual(left=special_effect, right=-1):
        AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=left_2, right=-1)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2051450709)
def Event_2051450709(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 2051450709"""
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2051450710)
def Event_2051450710(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    animation_id_1: int,
    distance: float,
    left: uint,
    flag_9: Flag | int,
    flag_10: Flag | int,
):
    """Event 2051450710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    DisableFlag(flag_9)
    if FlagEnabled(flag_1):
        GotoIfFlagEnabled(Label.L20, flag=flag_3)
    AND_8.Add(FlagEnabled(flag_1))
    AND_8.Add(FlagDisabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_8)
    
    MAIN.Await(AND_8)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    ForceAnimation(character, animation_id)
    DisableGravity(character)
    AND_5.Add(CharacterBackreadEnabled(character))
    AND_5.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_5)
    
    WaitRealFrames(frames=1)
    if UnsignedEqual(left=left, right=0):
        ResetCharacterPosition(character=character)
    else:
        Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    SetTeamType(character, TeamType.FriendlyNPC)
    if FlagDisabled(flag_5):
        GotoIfFlagDisabled(Label.L20, flag=flag_4)
        EnableFlag(flag_5)
        Goto(Label.L20)
    AND_1.Add(FlagEnabled(flag_6))
    AND_1.Add(FlagEnabled(flag_8))
    AND_2.Add(FlagEnabled(flag_10))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    GotoIfConditionTrue(Label.L20, input_condition=OR_1)
    EnableFlag(flag_6)
    EnableFlag(flag_7)
    ForceAnimation(character, animation_id_1)
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagDisabled(flag_1))
    OR_15.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(2051450721)
def Event_2051450721(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    animation_id: int,
    seconds_1: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds_2: float,
):
    """Event 2051450721"""
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L20, flag=flag)
    GotoIfFlagEnabled(Label.L20, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        Wait(seconds)
        EnableFlag(flag_2)
        DisableCharacter(character)
        Wait(seconds_2)
        DisableBackread(character)
        Goto(Label.L20)
    ForceAnimation(character, animation_id)
    Wait(seconds_1)
    EnableFlag(flag_2)

    # --- Label 20 --- #
    DefineLabel(20)
    if FlagEnabled(flag_1):
        EnableFlag(flag_3)
    End()


@RestartOnRest(2051450722)
def Event_2051450722(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2051450722"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag)
    End()


@RestartOnRest(2051450711)
def Event_2051450711(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    distance: float,
    flag_4: Flag | int,
):
    """Event 2051450711"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L3, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_1.Add(FlagEnabled(flag_3))
    AND_1.Add(FlagEnabled(flag_4))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@RestartOnRest(2051450712)
def Event_2051450712(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    region: Region | int,
    region_1: Region | int,
    flag_2: Flag | int,
    asset: Asset | int,
    animation_id: int,
    obj_act_id: int,
    flag_3: Flag | int,
):
    """Event 2051450712"""
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        DisableFlag(flag_3)
        End()
    AND_10.Add(FlagDisabled(flag_2))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_10)
    
    EnableFlag(flag_2)
    if PlayerInOwnWorld():
        EnableFlag(flag_3)
    EndOfAnimation(asset=asset, animation_id=animation_id)
    DisableAssetActivation(asset, obj_act_id=obj_act_id)
    WaitFrames(frames=1)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(2051450713)
def Event_2051450713(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(2051450714)
def Event_2051450714(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2051450714"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(2051450715)
def Event_2051450715(
    _,
    asset: Asset | int,
    animation_id: int,
    obj_act_id: int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    obj_act_id_1: uint,
):
    """Event 2051450715"""
    WaitFrames(frames=2)
    AND_5.Add(FlagDisabled(flag_5))
    AND_6.Add(FlagEnabled(flag_3))
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    SkipLinesIfConditionFalse(4, OR_2)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagEnabled(2051452739))
    SkipLinesIfConditionTrue(1, AND_10)
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(2051452739))
    AND_4.Add(FlagEnabled(flag_1))
    AND_4.Add(FlagEnabled(flag_1))
    AND_4.Add(FlagEnabled(flag_5))
    AND_4.Add(FlagDisabled(flag_6))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagEnabled(flag_5))
    AND_2.Add(FlagEnabled(flag_6))
    AND_3.Add(FlagEnabled(flag_2))
    AND_3.Add(FlagDisabled(flag_3))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    SkipLinesIfConditionFalse(3, OR_1)
    EndOfAnimation(asset=asset, animation_id=animation_id)
    DisableAssetActivation(asset, obj_act_id=obj_act_id)
    End()
    if FlagEnabled(flag_4):
        EndOfAnimation(asset=asset, animation_id=0)
        DisableAssetActivation(asset, obj_act_id=obj_act_id)
    
        MAIN.Await(FlagEnabled(flag))
    
        EnableAssetActivation(asset, obj_act_id=obj_act_id)
    
        MAIN.Await(AssetActivated(obj_act_id=obj_act_id_1))
    
        EnableFlag(flag_1)
        EnableFlag(2051459250)
        End()
    if FlagDisabled(flag_5):
        EndOfAnimation(asset=asset, animation_id=0)
        DisableAssetActivation(asset, obj_act_id=obj_act_id)
        End()
    if FlagEnabled(flag_5):
        EndOfAnimation(asset=asset, animation_id=0)
        EnableAssetActivation(asset, obj_act_id=obj_act_id)
        if FlagEnabled(flag_1):
            return
    AND_10.Add(FlagEnabled(flag_6))
    AND_10.Add(AssetActivated(obj_act_id=obj_act_id_1))
    AND_11.Add(FlagEnabled(flag_5))
    AND_11.Add(AssetActivated(obj_act_id=obj_act_id_1))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    
    MAIN.Await(OR_10)
    
    EnableFlag(flag_1)
    End()


@RestartOnRest(2051450716)
def Event_2051450716(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450716"""
    WaitFrames(frames=1)
    EnableNetworkFlag(flag)
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    DisableNetworkFlag(flag)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()


@RestartOnRest(2051450717)
def Event_2051450717(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2051450717"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(2051450718)
def Event_2051450718(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2051450718"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(2051450719)
def Event_2051450719(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450719"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    Restart()


@RestartOnRest(2051450725)
def Event_2051450725(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2051450725"""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagEnabled(flag_2))
    AND_10.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_10)
    
    EnableNetworkFlag(flag_1)
