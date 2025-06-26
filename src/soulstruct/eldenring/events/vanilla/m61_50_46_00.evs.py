"""
Land of Shadow 12-11 NE SW

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
    CommonFunc_90005271(0, character=2050460250, seconds=0.0, animation_id=-1)
    Event_2050462690()
    Event_2050462695()
    Event_2050462699()
    CommonFunc_90005557(0, entity=2050461680)
    CommonFunc_90005557(0, entity=2050461681)
    CommonFunc_90005557(0, entity=2050461682)
    CommonFunc_90005557(0, entity=2050461683)
    CommonFunc_90005557(0, entity=2050461684)
    CommonFunc_90005557(0, entity=2050461685)
    CommonFunc_90005557(0, entity=2050461686)
    CommonFunc_90005557(0, entity=2050461687)
    CommonFunc_90005556(0, asset=2050461688, flag=2050467800)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    Event_2050462300(0, character=2050460300, animation_id=30008, animation_id_1=20008, flag=2250460308)
    Event_2050462330(0, character=2050460300, flag=2250462308, flag_1=2250462309, flag_2=2250460308)
    Event_2050462335(
        0,
        character=2050460300,
        flag=2250462301,
        flag_1=2250462302,
        flag_2=2250462303,
        flag_3=2250462304,
        flag_4=2250460308,
    )
    CommonFunc_90005430(0, character=2050460300)
    Event_2050462320(0, character=2050460300, flag=2250462300, flag_1=2250460309)
    CommonFunc_90005301(0, flag=2050460300, character=2050460300, item_lot__unk1=2050460500, seconds=4.0, unk1=0)
    Event_2050462310(
        0,
        character=2050460310,
        animation_id=30007,
        animation_id_1=20007,
        region=2050462310,
        flag=2250462318,
    )
    CommonFunc_90005430(0, character=2050460310)
    Event_2050462320(1, character=2050460310, flag=2250462310, flag_1=2250462318)
    CommonFunc_90005301(0, flag=2050460310, character=2050460310, item_lot__unk1=2050460510, seconds=4.0, unk1=0)
    Event_2050462330(1, character=2050460310, flag=2250462318, flag_1=2250462319, flag_2=2250462320)
    Event_2050462335(
        1,
        character=2050460310,
        flag=2250462311,
        flag_1=2250462312,
        flag_2=2250462313,
        flag_3=2250462314,
        flag_4=2250462320,
    )
    CommonFunc_90005433(0, character=2050460300, flag=2250462305, flag_1=2250462306, flag_2=2250462307)
    CommonFunc_90005434(0, character=2050460300, flag=2250462305, flag_1=2250462306, flag_2=2250462307)
    CommonFunc_90005433(0, character=2050460310, flag=2250462315, flag_1=2250462316, flag_2=2250462317)
    CommonFunc_90005434(0, character=2050460310, flag=2250462315, flag_1=2250462316, flag_2=2250462317)
    Event_2050462350()


@RestartOnRest(2050462310)
def Event_2050462310(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    flag: Flag | int,
):
    """Event 2050462310"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    ForceAnimation(character, animation_id_1, loop=True, wait_for_completion=True)
    EnableNetworkFlag(2250462320)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(2050462300)
def Event_2050462300(_, character: uint, animation_id: int, animation_id_1: int, flag: Flag | int):
    """Event 2050462300"""
    GotoIfFlagDisabled(Label.L4, flag=flag)
    PostDestruction(2050461600)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAssetInvulnerability(2050461600)
    ForceAnimation(character, animation_id, loop=True)
    DisableAI(character)
    WaitRealFrames(frames=1)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=106,
        material_vfx_id=106,
        unk_16_20=139,
        unk_20_24=117,
        unk_24_28=-1,
    )
    SetNPCPartEffects(
        character,
        npc_part_id=31,
        material_sfx_id=106,
        material_vfx_id=106,
        unk_16_20=139,
        unk_20_24=117,
        unk_24_28=-1,
    )
    CreateNPCPart(character, npc_part_id=32, part_index=NPCPartType.Part1, part_health=99999)
    SetNPCPartEffects(
        character,
        npc_part_id=32,
        material_sfx_id=106,
        material_vfx_id=106,
        unk_16_20=139,
        unk_20_24=117,
        unk_24_28=-1,
    )
    CreateNPCPart(character, npc_part_id=33, part_index=NPCPartType.Part2, part_health=99999)
    SetNPCPartEffects(
        character,
        npc_part_id=33,
        material_sfx_id=106,
        material_vfx_id=106,
        unk_16_20=139,
        unk_20_24=117,
        unk_24_28=-1,
    )
    OR_2.Add(CharacterHasSpecialEffect(character, 20011135))
    
    MAIN.Await(OR_2)
    
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=-1,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=120,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        character,
        npc_part_id=31,
        material_sfx_id=-1,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=120,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        character,
        npc_part_id=32,
        material_sfx_id=-1,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=120,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        character,
        npc_part_id=33,
        material_sfx_id=-1,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=120,
        unk_24_28=0,
    )
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    DisableAssetInvulnerability(2050461600)
    DestroyAsset(2050461600, request_slot=0)
    ForceAnimation(character, animation_id_1, loop=True, wait_for_completion=True)
    EnableAI(character)
    EnableNetworkFlag(2250460309)
    End()


@RestartOnRest(2050462320)
def Event_2050462320(_, character: uint, flag: Flag | int, flag_1: Flag | int):
    """Event 2050462320"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableGravity(character)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 30010, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=200.0))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 20010, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    EnableGravity(character)
    AddSpecialEffect(character, 5006)
    ReplanAI(character)
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_1, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_2, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_3, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_4, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_5, radius=220.0))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(2050462330)
def Event_2050462330(_, character: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2050462330"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 20011135))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L3, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag)
    EnableFlag(flag)
    if FlagEnabled(flag_2):
        ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_1)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20009, wait_for_completion=True)
    DisableFlag(flag)
    DisableFlag(flag_1)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(2050462335)
def Event_2050462335(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 2050462335"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 20011113))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_4):
        EnableFlag(flag)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableFlag(flag_3)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(character, 20009, wait_for_completion=True)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(2050462350)
def Event_2050462350():
    """Event 2050462350"""
    AND_1.Add(CharacterBackreadEnabled(2050460300))
    AND_1.Add(CharacterBackreadEnabled(2050460310))
    AND_1.Add(HasAIStatus(2050460300, ai_status=AIStatusType.Battle))
    AND_1.Add(HasAIStatus(2050460310, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2050460310, 20011144)
    AND_2.Add(CharacterBackreadEnabled(2050460300))
    AND_2.Add(CharacterBackreadEnabled(2050460310))
    AND_3.Add(HasAIStatus(2050460300, ai_status=AIStatusType.Battle))
    AND_3.Add(HasAIStatus(2050460310, ai_status=AIStatusType.Battle))
    AND_2.Add(not AND_3)
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(2050460310, 20011144)
    Restart()


@RestartOnRest(2050462690)
def Event_2050462690():
    """Event 2050462690"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2050462691)
    DisableFlag(2050462692)
    if FlagEnabled(2050460690):
        return
    GotoIfFlagEnabled(Label.L10, flag=2045470690)
    GotoIfFlagEnabled(Label.L13, flag=40000690)
    DeleteAssetVFX(2050461690)
    CreateAssetVFX(2050461690, dummy_id=100, vfx_id=6102)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209524, entity=2050461690))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60071)
    EnableFlag(2050460690)
    AwardItemLot(2045470900, host_only=True)
    DeleteAssetVFX(2050461690)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(ActionButtonParamActivated(action_button_id=209525, entity=2050461691))
    OR_1.Add(PlayerHasWeapon(2540000))
    OR_1.Add(PlayerHasWeapon(2540001))
    OR_1.Add(PlayerHasWeapon(2540002))
    OR_1.Add(PlayerHasWeapon(2540003))
    OR_1.Add(PlayerHasWeapon(2540004))
    OR_1.Add(PlayerHasWeapon(2540005))
    OR_1.Add(PlayerHasWeapon(2540006))
    OR_1.Add(PlayerHasWeapon(2540007))
    OR_1.Add(PlayerHasWeapon(2540008))
    OR_1.Add(PlayerHasWeapon(2540009))
    OR_1.Add(PlayerHasWeapon(2540010))
    AND_3.Add(OR_1)
    OR_2.Add(AND_3)
    OR_2.Add(not OR_1)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_3)
    AwaitDialogResponse(
        message=2020025,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2050461691,
        display_distance=2.0,
        left_flag=2050462691,
        right_flag=2050462692,
        cancel_flag=2050462692,
    )
    if FlagDisabled(2050462691):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    OR_3.Add(PlayerHasWeapon(2540010))
    SkipLinesIfConditionFalse(5, OR_3)
    RemoveWeaponFromPlayer(item=2540010, quantity=1)
    AwardItemLot(2045470600, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477600)
    Goto(Label.L11)
    AND_15.Add(PlayerHasWeapon(2540009))
    SkipLinesIfConditionFalse(5, AND_15)
    RemoveWeaponFromPlayer(item=2540009, quantity=1)
    AwardItemLot(2045470590, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477590)
    Goto(Label.L11)
    AND_14.Add(PlayerHasWeapon(2540008))
    SkipLinesIfConditionFalse(5, AND_14)
    RemoveWeaponFromPlayer(item=2540008, quantity=1)
    AwardItemLot(2045470580, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477580)
    Goto(Label.L11)
    AND_13.Add(PlayerHasWeapon(2540007))
    SkipLinesIfConditionFalse(5, AND_13)
    RemoveWeaponFromPlayer(item=2540007, quantity=1)
    AwardItemLot(2045470570, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477570)
    Goto(Label.L11)
    AND_12.Add(PlayerHasWeapon(2540006))
    SkipLinesIfConditionFalse(5, AND_12)
    RemoveWeaponFromPlayer(item=2540006, quantity=1)
    AwardItemLot(2045470560, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477560)
    Goto(Label.L11)
    AND_11.Add(PlayerHasWeapon(2540005))
    SkipLinesIfConditionFalse(5, AND_11)
    RemoveWeaponFromPlayer(item=2540005, quantity=1)
    AwardItemLot(2045470550, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477550)
    Goto(Label.L11)
    AND_10.Add(PlayerHasWeapon(2540004))
    SkipLinesIfConditionFalse(5, AND_10)
    RemoveWeaponFromPlayer(item=2540004, quantity=1)
    AwardItemLot(2045470540, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477540)
    Goto(Label.L11)
    AND_9.Add(PlayerHasWeapon(2540003))
    SkipLinesIfConditionFalse(5, AND_9)
    RemoveWeaponFromPlayer(item=2540003, quantity=1)
    AwardItemLot(2045470530, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477530)
    Goto(Label.L11)
    AND_8.Add(PlayerHasWeapon(2540002))
    SkipLinesIfConditionFalse(5, AND_8)
    RemoveWeaponFromPlayer(item=2540002, quantity=1)
    AwardItemLot(2045470520, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477520)
    Goto(Label.L11)
    AND_7.Add(PlayerHasWeapon(2540001))
    SkipLinesIfConditionFalse(5, AND_7)
    RemoveWeaponFromPlayer(item=2540001, quantity=1)
    AwardItemLot(2045470510, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477510)
    Goto(Label.L11)
    AND_6.Add(PlayerHasWeapon(2540000))
    SkipLinesIfConditionFalse(5, AND_6)
    RemoveWeaponFromPlayer(item=2540000, quantity=1)
    AwardItemLot(2045470500, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477500)
    Goto(Label.L11)

    # --- Label 11 --- #
    DefineLabel(11)
    Wait(2.0)
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    ClearMainCondition()
    AND_5.Add(PlayerInOwnWorld())
    AND_5.Add(ActionButtonParamActivated(action_button_id=209526, entity=2050461692))
    OR_2.Add(PlayerHasWeapon(2540000))
    OR_2.Add(PlayerHasWeapon(2540001))
    OR_2.Add(PlayerHasWeapon(2540002))
    OR_2.Add(PlayerHasWeapon(2540003))
    OR_2.Add(PlayerHasWeapon(2540004))
    OR_2.Add(PlayerHasWeapon(2540005))
    OR_2.Add(PlayerHasWeapon(2540006))
    OR_2.Add(PlayerHasWeapon(2540007))
    OR_2.Add(PlayerHasWeapon(2540008))
    OR_2.Add(PlayerHasWeapon(2540009))
    OR_2.Add(PlayerHasWeapon(2540010))
    AND_5.Add(OR_2)
    OR_3.Add(AND_5)
    OR_3.Add(not OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_5)
    AwaitDialogResponse(
        message=2020026,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2050461692,
        display_distance=2.0,
        left_flag=2050462691,
        right_flag=2050462692,
        cancel_flag=2050462692,
    )
    if FlagDisabled(2050462691):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    OR_14.Add(PlayerHasWeapon(2540010))
    SkipLinesIfConditionFalse(5, OR_14)
    RemoveWeaponFromPlayer(item=2540010, quantity=1)
    AwardItemLot(2045470800, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477800)
    Goto(Label.L14)
    OR_13.Add(PlayerHasWeapon(2540009))
    SkipLinesIfConditionFalse(5, OR_13)
    RemoveWeaponFromPlayer(item=2540009, quantity=1)
    AwardItemLot(2045470790, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477790)
    Goto(Label.L14)
    OR_12.Add(PlayerHasWeapon(2540008))
    SkipLinesIfConditionFalse(5, OR_12)
    RemoveWeaponFromPlayer(item=2540008, quantity=1)
    AwardItemLot(2045470780, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477780)
    Goto(Label.L14)
    OR_11.Add(PlayerHasWeapon(2540007))
    SkipLinesIfConditionFalse(5, OR_11)
    RemoveWeaponFromPlayer(item=2540007, quantity=1)
    AwardItemLot(2045470770, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477770)
    Goto(Label.L14)
    OR_10.Add(PlayerHasWeapon(2540006))
    SkipLinesIfConditionFalse(5, OR_10)
    RemoveWeaponFromPlayer(item=2540006, quantity=1)
    AwardItemLot(2045470760, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477760)
    Goto(Label.L14)
    OR_9.Add(PlayerHasWeapon(2540005))
    SkipLinesIfConditionFalse(5, OR_9)
    RemoveWeaponFromPlayer(item=2540005, quantity=1)
    AwardItemLot(2045470750, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477750)
    Goto(Label.L14)
    OR_8.Add(PlayerHasWeapon(2540004))
    SkipLinesIfConditionFalse(5, OR_8)
    RemoveWeaponFromPlayer(item=2540004, quantity=1)
    AwardItemLot(2045470740, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477740)
    Goto(Label.L14)
    OR_7.Add(PlayerHasWeapon(2540003))
    SkipLinesIfConditionFalse(5, OR_7)
    RemoveWeaponFromPlayer(item=2540003, quantity=1)
    AwardItemLot(2045470730, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477730)
    Goto(Label.L14)
    OR_6.Add(PlayerHasWeapon(2540002))
    SkipLinesIfConditionFalse(5, OR_6)
    RemoveWeaponFromPlayer(item=2540002, quantity=1)
    AwardItemLot(2045470720, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477720)
    Goto(Label.L14)
    OR_5.Add(PlayerHasWeapon(2540001))
    SkipLinesIfConditionFalse(5, OR_5)
    RemoveWeaponFromPlayer(item=2540001, quantity=1)
    AwardItemLot(2045470710, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477710)
    Goto(Label.L14)
    OR_4.Add(PlayerHasWeapon(2540000))
    SkipLinesIfConditionFalse(5, OR_4)
    RemoveWeaponFromPlayer(item=2540000, quantity=1)
    AwardItemLot(2045470700, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477700)
    Goto(Label.L14)

    # --- Label 14 --- #
    DefineLabel(14)
    Wait(2.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ClearMainCondition()
    OR_1.Add(PlayerHasWeapon(2540000))
    OR_1.Add(PlayerHasWeapon(2540001))
    OR_1.Add(PlayerHasWeapon(2540002))
    OR_1.Add(PlayerHasWeapon(2540003))
    OR_1.Add(PlayerHasWeapon(2540004))
    OR_1.Add(PlayerHasWeapon(2540005))
    OR_1.Add(PlayerHasWeapon(2540006))
    OR_1.Add(PlayerHasWeapon(2540007))
    OR_1.Add(PlayerHasWeapon(2540008))
    OR_1.Add(PlayerHasWeapon(2540009))
    OR_1.Add(PlayerHasWeapon(2540010))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(2050462695)
def Event_2050462695():
    """Event 2050462695"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2050462693)
    DisableFlag(2050462694)
    if FlagEnabled(2050460690):
        return
    GotoIfFlagEnabled(Label.L10, flag=2045470690)
    GotoIfFlagEnabled(Label.L13, flag=40000690)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(ActionButtonParamActivated(action_button_id=209525, entity=2050461691))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_1.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_1.Add(PlayerHasWeapon(2560000))
    OR_1.Add(PlayerHasWeapon(2560001))
    OR_1.Add(PlayerHasWeapon(2560002))
    OR_1.Add(PlayerHasWeapon(2560003))
    OR_1.Add(PlayerHasWeapon(2560004))
    OR_1.Add(PlayerHasWeapon(2560005))
    OR_1.Add(PlayerHasWeapon(2560006))
    OR_1.Add(PlayerHasWeapon(2560007))
    OR_1.Add(PlayerHasWeapon(2560008))
    OR_1.Add(PlayerHasWeapon(2560009))
    OR_1.Add(PlayerHasWeapon(2560010))
    AND_1.Add(OR_1)
    AND_3.Add(AND_1)
    OR_2.Add(AND_3)
    OR_2.Add(not AND_1)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_3)
    AwaitDialogResponse(
        message=2020027,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2050461691,
        display_distance=2.0,
        left_flag=2050462693,
        right_flag=2050462694,
        cancel_flag=2050462694,
    )
    if FlagDisabled(2050462693):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    OR_3.Add(PlayerHasWeapon(2560010))
    SkipLinesIfConditionFalse(5, OR_3)
    RemoveWeaponFromPlayer(item=2560010, quantity=1)
    AwardItemLot(2045470600, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477600)
    Goto(Label.L11)
    AND_15.Add(PlayerHasWeapon(2560009))
    SkipLinesIfConditionFalse(5, AND_15)
    RemoveWeaponFromPlayer(item=2560009, quantity=1)
    AwardItemLot(2045470590, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477590)
    Goto(Label.L11)
    AND_14.Add(PlayerHasWeapon(2560008))
    SkipLinesIfConditionFalse(5, AND_14)
    RemoveWeaponFromPlayer(item=2560008, quantity=1)
    AwardItemLot(2045470580, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477580)
    Goto(Label.L11)
    AND_13.Add(PlayerHasWeapon(2560007))
    SkipLinesIfConditionFalse(5, AND_13)
    RemoveWeaponFromPlayer(item=2560007, quantity=1)
    AwardItemLot(2045470570, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477570)
    Goto(Label.L11)
    AND_12.Add(PlayerHasWeapon(2560006))
    SkipLinesIfConditionFalse(5, AND_12)
    RemoveWeaponFromPlayer(item=2560006, quantity=1)
    AwardItemLot(2045470560, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477560)
    Goto(Label.L11)
    AND_11.Add(PlayerHasWeapon(2560005))
    SkipLinesIfConditionFalse(5, AND_11)
    RemoveWeaponFromPlayer(item=2560005, quantity=1)
    AwardItemLot(2045470550, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477550)
    Goto(Label.L11)
    AND_10.Add(PlayerHasWeapon(2560004))
    SkipLinesIfConditionFalse(5, AND_10)
    RemoveWeaponFromPlayer(item=2560004, quantity=1)
    AwardItemLot(2045470540, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477540)
    Goto(Label.L11)
    AND_9.Add(PlayerHasWeapon(2560003))
    SkipLinesIfConditionFalse(5, AND_9)
    RemoveWeaponFromPlayer(item=2560003, quantity=1)
    AwardItemLot(2045470530, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477530)
    Goto(Label.L11)
    AND_8.Add(PlayerHasWeapon(2560002))
    SkipLinesIfConditionFalse(5, AND_8)
    RemoveWeaponFromPlayer(item=2560002, quantity=1)
    AwardItemLot(2045470520, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477520)
    Goto(Label.L11)
    AND_7.Add(PlayerHasWeapon(2560001))
    SkipLinesIfConditionFalse(5, AND_7)
    RemoveWeaponFromPlayer(item=2560001, quantity=1)
    AwardItemLot(2045470510, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477510)
    Goto(Label.L11)
    AND_6.Add(PlayerHasWeapon(2560000))
    SkipLinesIfConditionFalse(5, AND_6)
    RemoveWeaponFromPlayer(item=2560000, quantity=1)
    AwardItemLot(2045470500, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477500)
    Goto(Label.L11)

    # --- Label 11 --- #
    DefineLabel(11)
    Wait(2.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ClearMainCondition()
    AND_3.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_1.Add(PlayerHasWeapon(2560000))
    OR_1.Add(PlayerHasWeapon(2560001))
    OR_1.Add(PlayerHasWeapon(2560002))
    OR_1.Add(PlayerHasWeapon(2560003))
    OR_1.Add(PlayerHasWeapon(2560004))
    OR_1.Add(PlayerHasWeapon(2560005))
    OR_1.Add(PlayerHasWeapon(2560006))
    OR_1.Add(PlayerHasWeapon(2560007))
    OR_1.Add(PlayerHasWeapon(2560008))
    OR_1.Add(PlayerHasWeapon(2560009))
    OR_1.Add(PlayerHasWeapon(2560010))
    AND_3.Add(OR_1)
    
    MAIN.Await(AND_3)
    
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    AND_5.Add(PlayerInOwnWorld())
    AND_5.Add(ActionButtonParamActivated(action_button_id=209526, entity=2050461692))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_2.Add(PlayerHasWeapon(2550000))
    OR_2.Add(PlayerHasWeapon(2550001))
    OR_2.Add(PlayerHasWeapon(2550002))
    OR_2.Add(PlayerHasWeapon(2550003))
    OR_2.Add(PlayerHasWeapon(2550004))
    OR_2.Add(PlayerHasWeapon(2550005))
    OR_2.Add(PlayerHasWeapon(2550006))
    OR_2.Add(PlayerHasWeapon(2550007))
    OR_2.Add(PlayerHasWeapon(2550008))
    OR_2.Add(PlayerHasWeapon(2550009))
    OR_2.Add(PlayerHasWeapon(2550010))
    AND_3.Add(OR_2)
    AND_5.Add(AND_3)
    OR_3.Add(AND_5)
    OR_3.Add(not AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_5)
    AwaitDialogResponse(
        message=2020028,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2050461692,
        display_distance=2.0,
        left_flag=2050462693,
        right_flag=2050462694,
        cancel_flag=2050462694,
    )
    if FlagDisabled(2050462693):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    OR_14.Add(PlayerHasWeapon(2550010))
    SkipLinesIfConditionFalse(5, OR_14)
    RemoveWeaponFromPlayer(item=2550010, quantity=1)
    AwardItemLot(2045470800, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477800)
    Goto(Label.L14)
    OR_13.Add(PlayerHasWeapon(2550009))
    SkipLinesIfConditionFalse(5, OR_13)
    RemoveWeaponFromPlayer(item=2550009, quantity=1)
    AwardItemLot(2045470790, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477790)
    Goto(Label.L14)
    OR_12.Add(PlayerHasWeapon(2550008))
    SkipLinesIfConditionFalse(5, OR_12)
    RemoveWeaponFromPlayer(item=2550008, quantity=1)
    AwardItemLot(2045470780, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477780)
    Goto(Label.L14)
    OR_11.Add(PlayerHasWeapon(2550007))
    SkipLinesIfConditionFalse(5, OR_11)
    RemoveWeaponFromPlayer(item=2550007, quantity=1)
    AwardItemLot(2045470770, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477770)
    Goto(Label.L14)
    OR_10.Add(PlayerHasWeapon(2550006))
    SkipLinesIfConditionFalse(5, OR_10)
    RemoveWeaponFromPlayer(item=2550006, quantity=1)
    AwardItemLot(2045470760, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477760)
    Goto(Label.L14)
    OR_9.Add(PlayerHasWeapon(2550005))
    SkipLinesIfConditionFalse(5, OR_9)
    RemoveWeaponFromPlayer(item=2550005, quantity=1)
    AwardItemLot(2045470750, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477750)
    Goto(Label.L14)
    OR_8.Add(PlayerHasWeapon(2550004))
    SkipLinesIfConditionFalse(5, OR_8)
    RemoveWeaponFromPlayer(item=2550004, quantity=1)
    AwardItemLot(2045470740, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477740)
    Goto(Label.L14)
    OR_7.Add(PlayerHasWeapon(2550003))
    SkipLinesIfConditionFalse(5, OR_7)
    RemoveWeaponFromPlayer(item=2550003, quantity=1)
    AwardItemLot(2045470730, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477730)
    Goto(Label.L14)
    OR_6.Add(PlayerHasWeapon(2550002))
    SkipLinesIfConditionFalse(5, OR_6)
    RemoveWeaponFromPlayer(item=2550002, quantity=1)
    AwardItemLot(2045470720, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477720)
    Goto(Label.L14)
    OR_5.Add(PlayerHasWeapon(2550001))
    SkipLinesIfConditionFalse(5, OR_5)
    RemoveWeaponFromPlayer(item=2550001, quantity=1)
    AwardItemLot(2045470710, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477710)
    Goto(Label.L14)
    OR_4.Add(PlayerHasWeapon(2550000))
    SkipLinesIfConditionFalse(5, OR_4)
    RemoveWeaponFromPlayer(item=2550000, quantity=1)
    AwardItemLot(2045470700, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477700)
    Goto(Label.L14)

    # --- Label 14 --- #
    DefineLabel(14)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ClearMainCondition()
    AND_3.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_1.Add(PlayerHasWeapon(2550000))
    OR_1.Add(PlayerHasWeapon(2550001))
    OR_1.Add(PlayerHasWeapon(2550002))
    OR_1.Add(PlayerHasWeapon(2550003))
    OR_1.Add(PlayerHasWeapon(2550004))
    OR_1.Add(PlayerHasWeapon(2550005))
    OR_1.Add(PlayerHasWeapon(2550006))
    OR_1.Add(PlayerHasWeapon(2550007))
    OR_1.Add(PlayerHasWeapon(2550008))
    OR_1.Add(PlayerHasWeapon(2550009))
    OR_1.Add(PlayerHasWeapon(2550010))
    AND_3.Add(OR_1)
    
    MAIN.Await(AND_3)
    
    Restart()


@RestartOnRest(2050462699)
def Event_2050462699():
    """Event 2050462699"""
    GotoIfPlayerNotInOwnWorld(Label.L15)
    GotoIfFlagEnabled(Label.L1, flag=2050460690)
    GotoIfFlagEnabled(Label.L10, flag=2045470690)
    GotoIfFlagEnabled(Label.L11, flag=40000690)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(2050462696)
    DisableNetworkFlag(2050462697)
    DisableNetworkFlag(2050462698)
    EnableAsset(2050461690)
    DisableAsset(2050461691)
    DisableAsset(2050461692)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableNetworkFlag(2050462696)
    EnableNetworkFlag(2050462697)
    DisableNetworkFlag(2050462698)
    DisableAsset(2050461690)
    EnableAsset(2050461691)
    DisableAsset(2050461692)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    DisableNetworkFlag(2050462696)
    DisableNetworkFlag(2050462697)
    EnableNetworkFlag(2050462698)
    DisableAsset(2050461690)
    DisableAsset(2050461691)
    EnableAsset(2050461692)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    EnableAsset(2045472690)
    DisableAsset(2045472691)
    DisableAsset(2045472692)
    OR_1.Add(FlagEnabled(2045472696))
    OR_1.Add(FlagEnabled(2045472697))
    OR_1.Add(FlagEnabled(2045472698))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(2045472696):
        return
    GotoIfFlagEnabled(Label.L16, flag=2045472698)
    DisableAsset(2045471690)
    EnableAsset(2045471691)
    DisableAsset(2045471692)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    DisableAsset(2045471690)
    DisableAsset(2045471691)
    EnableAsset(2045471692)
    End()
