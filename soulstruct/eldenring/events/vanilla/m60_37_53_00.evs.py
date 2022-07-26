"""
West Altus Plateau (SW) (NE)

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
from .entities.m60_37_53_00_entities import *
from .entities.m60_37_54_00_entities import Characters as m60_37_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76357, asset=Assets.AEG099_060_9000, enemy_block_distance=5.0, character=0)
    CommonFunc_90005870(0, character=Characters.DemiHumanQueen, name=904130600, npc_threat_level=16)
    Event_1037532345()
    Event_1037532350()
    CommonFunc_90005860(
        0,
        flag=1037530800,
        left=1037530800,
        character=Characters.DemiHumanQueen,
        left_1=0,
        item_lot=30395,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.DemiHumanQueen, npc_threat_level=16, right=0)
    Event_1037532450(
        0,
        character=Characters.DemiHumanQueen,
        region=1037532400,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.RayaLucariaScholar1,
        region=1037532400,
        radius=5.0,
        seconds=2.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        2,
        character=Characters.RayaLucariaScholar2,
        region=1037532400,
        radius=5.0,
        seconds=2.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        3,
        character=Characters.RayaLucariaScholar0,
        region=1037532400,
        radius=5.0,
        seconds=10.0,
        animation_id=-1,
    )
    CommonFunc_90005300(0, flag=1037530400, character=Characters.LargeScarab, item_lot=40332, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=m60_37_Characters.LeyndellFootSoldier2,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542370,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=m60_37_Characters.LeyndellFootSoldier2,
        region=1037542370,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        1,
        character=1037540371,
        animation_id=30002,
        animation_id_1=20002,
        region=1037542370,
        radius=5.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(1, character=1037540371, region=1037542370, radius=5.0, seconds=1.5, animation_id=-1)
    CommonFunc_90005211(
        2,
        character=1037540372,
        animation_id=30002,
        animation_id_1=20002,
        region=1037542370,
        radius=5.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(2, character=1037540372, region=1037542370, radius=5.0, seconds=4.0, animation_id=-1)
    CommonFunc_90005211(
        3,
        character=1037540373,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542370,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(3, character=1037540373, region=1037542370, radius=5.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005211(
        4,
        character=1037540374,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542370,
        radius=5.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(4, character=1037540374, region=1037542370, radius=5.0, seconds=2.0, animation_id=-1)
    CommonFunc_90005211(
        5,
        character=1037540375,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542370,
        radius=5.0,
        seconds=3.299999952316284,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        5,
        character=1037540375,
        region=1037542370,
        radius=5.0,
        seconds=3.299999952316284,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.WolfPackLeader,
        animation_id=30000,
        animation_id_1=20010,
        region=1037532360,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Wolf0,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Wolf2,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1037532400(0, character=Characters.Wolf1, region=1037532300, owner_entity=Characters.Dummy1)
    Event_1037532400(1, character=Characters.Wolf3, region=1037532300, owner_entity=Characters.Dummy1)
    Event_1037532400(2, character=Characters.Wolf4, region=1037532300, owner_entity=Characters.Dummy1)
    Event_1037532400(3, character=Characters.Wolf5, region=1037532300, owner_entity=Characters.Dummy1)
    Event_1037532201()
    Event_1037532200(0, source_entity=Assets.AEG099_048_9001, seconds=4.199999809265137)
    Event_1037532200(1, source_entity=Assets.AEG099_048_9002, seconds=4.599999904632568)
    Event_1037532200(2, source_entity=Assets.AEG099_048_9003, seconds=1.7999999523162842)
    Event_1037532200(3, source_entity=Assets.AEG099_048_9004, seconds=5.0)
    Event_1037532200(4, source_entity=Assets.AEG099_048_9005, seconds=1.899999976158142)
    Event_1037532200(5, source_entity=Assets.AEG099_048_9006, seconds=2.0)
    Event_1037532200(6, source_entity=Assets.AEG099_048_9007, seconds=3.0)
    Event_1037532200(7, source_entity=Assets.AEG099_048_9008, seconds=11.0)
    Event_1037532200(8, source_entity=Assets.AEG099_048_9017, seconds=2.5)
    Event_1037532200(9, source_entity=Assets.AEG099_048_9018, seconds=1.5)
    Event_1037532200(10, source_entity=Assets.AEG099_048_9019, seconds=2.0)
    Event_1037532200(11, source_entity=1037531211, seconds=7.099999904632568)
    Event_1037532200(12, source_entity=1037531212, seconds=2.200000047683716)
    Event_1037532200(13, source_entity=1037531213, seconds=2.299999952316284)
    Event_1037532200(14, source_entity=1037531214, seconds=1.899999976158142)
    Event_1037532200(15, source_entity=Assets.AEG099_048_9000, seconds=4.599999904632568)
    Event_1037532200(16, source_entity=1037531216, seconds=4.0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1037538620)
    Event_1037533700(0, character=Characters.Azur)


@RestartOnRest(1037532300)
def Event_1037532300():
    """Event 1037532300"""
    RemoveSpecialEffect(1037530210, 5070)
    RemoveSpecialEffect(1037530211, 5070)
    RemoveSpecialEffect(1037530212, 5070)
    RemoveSpecialEffect(1037530213, 5070)
    RemoveSpecialEffect(1037530214, 5070)
    RemoveSpecialEffect(1037530215, 5070)
    RemoveSpecialEffect(1037530216, 5070)
    RemoveSpecialEffect(1037530217, 5070)
    RemoveSpecialEffect(1037530218, 5070)
    RemoveSpecialEffect(1037530219, 5070)
    RemoveSpecialEffect(1037530220, 5070)
    RemoveSpecialEffect(1037530221, 5070)
    RemoveSpecialEffect(1037530222, 5070)
    RemoveSpecialEffect(1037530223, 5070)
    RemoveSpecialEffect(1037530224, 5070)
    RemoveSpecialEffect(1037530225, 5070)
    RemoveSpecialEffect(1037530226, 5070)
    RemoveSpecialEffect(1037530227, 5070)
    RemoveSpecialEffect(1037530228, 5070)


@RestartOnRest(1037532345)
def Event_1037532345():
    """Event 1037532345"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(Characters.DemiHumanQueen, 8087)
    EnableThisSlotFlag()
    End()


@RestartOnRest(1037532350)
def Event_1037532350():
    """Event 1037532350"""
    GotoIfFlagEnabled(Label.L0, flag=1037530800)
    
    MAIN.Await(FlagEnabled(1037530800))
    
    Kill(Characters.RayaLucariaScholar1, award_runes=True)
    Kill(Characters.RayaLucariaScholar2, award_runes=True)
    Kill(Characters.RayaLucariaScholar0, award_runes=True)
    Kill(Characters.DemiHumanShaman0, award_runes=True)
    Kill(Characters.DemiHumanShaman1, award_runes=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.RayaLucariaScholar1)
    DisableCharacter(Characters.RayaLucariaScholar2)
    DisableCharacter(Characters.RayaLucariaScholar0)
    DisableCharacter(Characters.DemiHumanShaman0)
    DisableCharacter(Characters.DemiHumanShaman1)
    End()


@RestartOnRest(1037532200)
def Event_1037532200(_, source_entity: uint, seconds: float):
    """Event 1037532200"""
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    EnableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803210,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803220,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803230,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803240,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803250,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803260,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802803270,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(6.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(1037532201)
def Event_1037532201():
    """Event 1037532201"""
    CreateProjectileOwner(entity=Characters.Dummy0)


@RestartOnRest(1037532400)
def Event_1037532400(_, character: uint, region: uint, owner_entity: uint):
    """Event 1037532400"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_11.Add(OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    ForceAnimation(character, 20011)
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    RemoveSpecialEffect(character, 8090)


@RestartOnRest(1037532450)
def Event_1037532450(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 1037532450"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(HasAIStatus(Characters.RayaLucariaScholar2, ai_status=AIStatusType.Search))
    OR_2.Add(HasAIStatus(Characters.RayaLucariaScholar2, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.RayaLucariaScholar0, ai_status=AIStatusType.Search))
    OR_2.Add(HasAIStatus(Characters.RayaLucariaScholar0, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1037533700)
def Event_1037533700(_, character: uint):
    """Event 1037533700"""
    if PlayerNotInOwnWorld():
        return
    DisableCharacter(character)
    DisableBackread(character)
    if FlagEnabled(400441):
        return
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    AND_1.Add(FlagEnabled(14009267))
    AwaitConditionTrue(AND_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character)
    End()
