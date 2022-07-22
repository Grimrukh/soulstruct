"""
Cliffbottom Catacombs

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
from .entities.m30_06_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30060800,
        left_flag=30062840,
        cancel_flag__right_flag=30062841,
        asset=Assets.AEG099_065_9000,
        player_start=30062840,
        area_id=30,
        block_id=6,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=300600, asset=Assets.AEG099_060_9000)
    Event_30062800()
    Event_30062810()
    Event_30062849()
    Event_30062811()
    CommonFunc_90005501(
        0,
        flag=30060510,
        flag_1=30060511,
        left=0,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30060512,
    )
    Event_30062510()
    CommonFunc_90005650(
        0,
        flag=30060540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30063541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30060540, anchor_entity=Assets.AEG027_041_0500)
    RunCommonEvent(
        30062400,
        slot=0,
        args=(30060600, 30061600, 30062600, 0, 30062601, 30062602, 30062603),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        30062400,
        slot=1,
        args=(30060605, 30061605, 30062605, 0, 30062606, 30062607, 30062608),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        30062400,
        slot=2,
        args=(30060610, 30061610, 30062610, 0, 30062611, 30062612, 30062613),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        30062400,
        slot=3,
        args=(30060615, 30061615, 30062615, 0, 30062616, 30062617, 30062618),
        arg_types="IIIiIII",
    )
    Event_30062580()
    CommonFunc_90005410(0, flag=30062100, character=30061100, entity_b=30065100)
    CommonFunc_90005411(0, asset=Assets.AEG099_053_9000, character=Characters.TalkDummy4, left=10)
    CommonFunc_90005620(
        0,
        flag=30060570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30062570,
        cancel_flag__right_flag=30062571,
        right=30062572,
    )
    CommonFunc_90005621(0, 30060570, 30061573)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30060519()
    CommonFunc_90005211(
        0,
        character=Characters.Imp0,
        animation_id=30009,
        animation_id_1=20009,
        region=30062200,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.Imp1, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Imp2, region=30062202, radius=5.0, seconds=1.0, animation_id=3002)
    CommonFunc_90005211(
        0,
        character=Characters.Imp3,
        animation_id=30000,
        animation_id_1=20000,
        region=30062203,
        radius=2.0,
        seconds=2.5999999046325684,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp4, region=30062204, seconds=0.0, animation_id=0)
    Event_30062206()
    CommonFunc_90005200(
        0,
        character=Characters.Imp5,
        animation_id=30000,
        animation_id_1=20000,
        region=30062205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30062211(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30062211(
        1,
        character=Characters.Imp7,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp8,
        animation_id=30002,
        animation_id_1=20002,
        region=30062208,
        radius=5.0,
        seconds=2.799999952316284,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp9,
        animation_id=30010,
        animation_id_1=20010,
        region=30062208,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp10,
        animation_id=30010,
        animation_id_1=20010,
        region=30062210,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp11,
        animation_id=30010,
        animation_id_1=20010,
        region=30062210,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp12,
        animation_id=30003,
        animation_id_1=20003,
        region=30062212,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp13,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp14,
        animation_id=30004,
        animation_id_1=20004,
        region=30062214,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp15,
        animation_id=30002,
        animation_id_1=20002,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Imp16,
        region=30062216,
        radius=2.0,
        seconds=0.4000000059604645,
        animation_id=3005,
    )
    CommonFunc_90005261(0, character=0, region=0, radius=0.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.Omen0,
        animation_id=30001,
        animation_id_1=20001,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Omen1, region=30062301, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Omen2,
        animation_id=30000,
        animation_id_1=20000,
        region=30062302,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    RunCommonEvent(30062300, slot=0, args=(30060303, 30000, 20000, 30062303, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    CommonFunc_90005261(0, character=Characters.Omen4, region=30062304, radius=5.0, seconds=0.0, animation_id=-1)
    Event_30062304()
    CommonFunc_90005200(0, 30060305, 30000, 20000, 30062305, 0.0, 0, 0, 0, 0)


@RestartOnRest(30062206)
def Event_30062206():
    """Event 30062206"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_11.Add(CharacterInsideRegion(character=PLAYER, region=30062294))
    OR_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.Imp4, radius=3.0))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(Characters.Imp4, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.Imp4, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.Imp4, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.Imp4, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.Imp4, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Imp4, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Imp4, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Imp4, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Imp4, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Imp4, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Imp4, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Imp4, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    ForceAnimation(Characters.Imp4, 3004, loop=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30062211)
def Event_30062211(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30062211"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_14.Add(HasAIStatus(Characters.Omen1, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_14)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(30062304)
def Event_30062304():
    """Event 30062304"""
    AND_1.Add(CharacterDead(Characters.Omen4))
    DisableHealthBar(Characters.Omen4)
    AddSpecialEffect(Characters.Omen4, 4403)
    Wait(1.0)
    EnableHealthBar(Characters.Omen4)


@ContinueOnRest(30062400)
def Event_30062400(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 30062400"""
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L1)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L2)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@RestartOnRest(30062300)
def Event_30062300(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30062300"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    DisableAI(character)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableAI(character)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@ContinueOnRest(30062510)
def Event_30062510():
    """Event 30062510"""
    CommonFunc_90005500(
        0,
        30060510,
        30060511,
        0,
        30061510,
        30061511,
        30063511,
        30061512,
        30063512,
        30062511,
        30062512,
        30060512,
        30060513,
        0,
    )


@ContinueOnRest(30060519)
def Event_30060519():
    """Event 30060519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30060510)


@RestartOnRest(30062520)
def Event_30062520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30062520"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@ContinueOnRest(30062580)
def Event_30062580():
    """Event 30062580"""
    RegisterLadder(start_climbing_flag=30060580, stop_climbing_flag=30060581, asset=Assets.AEG027_005_0500)


@RestartOnRest(30062800)
def Event_30062800():
    """Event 30062800"""
    if FlagEnabled(30060800):
        return
    
    MAIN.Await(HealthValue(Characters.ErdtreeBurialWatchdog) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.ErdtreeBurialWatchdog, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.ErdtreeBurialWatchdog))
    
    KillBossAndDisplayBanner(character=Characters.ErdtreeBurialWatchdog, banner_type=BannerType.EnemyFelled)
    EnableFlag(30060800)
    if PlayerInOwnWorld():
        EnableFlag(61207)
    EnableFlag(9207)


@RestartOnRest(30062810)
def Event_30062810():
    """Event 30062810"""
    GotoIfFlagDisabled(Label.L0, flag=30060800)
    DisableCharacter(Characters.ErdtreeBurialWatchdog)
    DisableAnimations(Characters.ErdtreeBurialWatchdog)
    Kill(Characters.ErdtreeBurialWatchdog)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ErdtreeBurialWatchdog)
    AND_2.Add(FlagEnabled(30062805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30062800))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.ErdtreeBurialWatchdog)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog, name=904260302)


@RestartOnRest(30062811)
def Event_30062811():
    """Event 30062811"""
    if FlagEnabled(30060800):
        return
    AND_1.Add(HealthRatio(Characters.ErdtreeBurialWatchdog) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30062802)


@RestartOnRest(30062849)
def Event_30062849():
    """Event 30062849"""
    CommonFunc_9005800(
        0,
        flag=30060800,
        entity=Assets.AEG099_001_9000,
        region=30062800,
        flag_1=30062805,
        character=30065800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30060800,
        entity=Assets.AEG099_001_9000,
        region=30062800,
        flag_1=30062805,
        flag_2=30062806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30060800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30060800, 930000, 30062805, 30062806, 0, 30062802, 0, 0)
