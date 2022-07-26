"""
Gaol Cave

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
from .entities.m31_21_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31210000, asset=Assets.AEG099_060_9000)
    Event_31212800()
    Event_31212810()
    Event_31212815()
    Event_31032849()
    Event_312112811()
    Event_31212830(0, flag=31210801, character=Characters.TalkDummy1)
    Event_31212860()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005261(
        0,
        character=Characters.GraveWardenDuelist,
        region=31212810,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31212500()
    CommonFunc_90005646(
        0,
        flag=31210800,
        left_flag=31212840,
        cancel_flag__right_flag=31212841,
        asset=Assets.AEG099_065_9000,
        player_start=31212840,
        area_id=31,
        block_id=21,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005511(0, flag=31210560, asset=Assets.AEG027_143_1000, obj_act_id=31213560, obj_act_id_1=27043, left=0)
    CommonFunc_90005512(0, flag=31210560, region=31212560, region_1=31212561)
    Event_31212400(
        0,
        flag=31210600,
        asset=Assets.AEG027_144_1000,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        1,
        flag=31210600,
        asset=Assets.AEG027_144_1001,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        2,
        flag=31210600,
        asset=Assets.AEG027_144_1002,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        3,
        flag=31210600,
        asset=Assets.AEG027_144_1003,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        4,
        flag=31210600,
        asset=Assets.AEG027_144_1004,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        5,
        flag=31210600,
        asset=Assets.AEG027_144_1005,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        6,
        flag=31210600,
        asset=Assets.AEG027_144_1006,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        7,
        flag=31210600,
        asset=Assets.AEG027_144_1007,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        8,
        flag=31210600,
        asset=Assets.AEG027_144_1008,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        9,
        flag=31210600,
        asset=Assets.AEG027_144_1010,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        10,
        flag=31210600,
        asset=Assets.AEG027_042_1000,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    Event_31212400(
        11,
        flag=31210600,
        asset=Assets.AEG027_042_1001,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0,
    )
    CommonFunc_90005621(0, flag=1047380570, asset=Assets.AEG099_272_9001)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_31212205()
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia1,
        animation_id=30000,
        animation_id_1=20000,
        region=31212209,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia2,
        region=31212209,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia5,
        region=31212219,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia6,
        region=31212219,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia7,
        region=31212219,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31212230(0, character=Characters.VulgarMilitia8)
    Event_31212230(1, character=Characters.VulgarMilitia9)
    Event_31212230(2, character=Characters.VulgarMilitia10)
    Event_31212230(3, character=Characters.VulgarMilitia11)
    Event_31212230(4, character=Characters.VulgarMilitia12)
    Event_31212230(5, character=Characters.VulgarMilitia13)
    Event_31212230(6, character=Characters.VulgarMilitia14)
    Event_31212230(7, character=Characters.VulgarMilitia15)
    Event_31212230(8, character=Characters.VulgarMilitia16)
    Event_31212230(9, character=Characters.VulgarMilitia17)
    Event_31212230(10, character=Characters.VulgarMilitia18)
    Event_31212230(11, character=Characters.VulgarMilitia19)
    Event_31212230(12, character=Characters.VulgarMilitia20)
    Event_31212230(13, character=Characters.PutridCorpse17)
    Event_31212230(14, character=Characters.PutridCorpse18)
    Event_31212230(15, character=Characters.PutridCorpse19)
    Event_31212250(
        0,
        character=Characters.PutridCorpse0,
        animation_id=30008,
        animation_id_1=20008,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        1,
        character=Characters.PutridCorpse1,
        animation_id=30005,
        animation_id_1=20005,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        2,
        character=Characters.PutridCorpse2,
        animation_id=30008,
        animation_id_1=20008,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        3,
        character=Characters.PutridCorpse4,
        animation_id=30005,
        animation_id_1=20005,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        17,
        character=Characters.PutridCorpse24,
        animation_id=30005,
        animation_id_1=20005,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        18,
        character=Characters.PutridCorpse25,
        animation_id=30005,
        animation_id_1=20005,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212260(0, character=Characters.PutridCorpse3, region=31212253, patrol_information_id=31213254)
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30002,
        animation_id_1=20002,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31212250(
        4,
        character=Characters.PutridCorpse6,
        animation_id=30008,
        animation_id_1=20008,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        5,
        character=Characters.PutridCorpse7,
        animation_id=30005,
        animation_id_1=20005,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        6,
        character=Characters.PutridCorpse8,
        animation_id=30005,
        animation_id_1=20005,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        7,
        character=Characters.PutridCorpse9,
        animation_id=30008,
        animation_id_1=20008,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        8,
        character=Characters.PutridCorpse10,
        animation_id=30005,
        animation_id_1=20005,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212260(1, character=Characters.PutridCorpse11, region=31212259, patrol_information_id=31213264)
    Event_31212250(
        9,
        character=Characters.PutridCorpse12,
        animation_id=30005,
        animation_id_1=20005,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        10,
        character=Characters.PutridCorpse13,
        animation_id=30005,
        animation_id_1=20005,
        region=31212259,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        11,
        character=Characters.PutridCorpse14,
        animation_id=30008,
        animation_id_1=20008,
        region=31212268,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        12,
        character=Characters.PutridCorpse15,
        animation_id=30005,
        animation_id_1=20005,
        region=31212268,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        13,
        character=Characters.PutridCorpse16,
        animation_id=30005,
        animation_id_1=20005,
        region=31212268,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        14,
        character=Characters.PutridCorpse20,
        animation_id=30008,
        animation_id_1=20008,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212260(2, character=Characters.PutridCorpse21, region=31212253, patrol_information_id=31213279)
    Event_31212250(
        15,
        character=Characters.PutridCorpse22,
        animation_id=30008,
        animation_id_1=20008,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    Event_31212250(
        16,
        character=Characters.PutridCorpse23,
        animation_id=30005,
        animation_id_1=20005,
        region=31212253,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        patrol_information_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Rat0, region=31212300, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=31212305, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat2, region=31212316, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat3, region=31212316, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat4, region=31212316, radius=2.0, seconds=0.0, animation_id=0)
    Event_31212308(0, character=31210306, region=31212306)
    Event_31212308(1, character=31210307, region=31212307)
    CommonFunc_90005261(0, character=Characters.GiantRat, region=31212316, radius=2.0, seconds=0.0, animation_id=0)


@RestartOnRest(31212500)
def Event_31212500():
    """Event 31212500"""
    GotoIfFlagDisabled(Label.L0, flag=31210500)
    DisableAsset(Assets.AEG020_126_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31212500))
    
    MAIN.Await(AND_1)
    
    DestroyAsset(Assets.AEG020_126_1000)
    EnableNetworkFlag(31210500)


@RestartOnRest(31212205)
def Event_31212205():
    """Event 31212205"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(Characters.VulgarMilitia0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31212205))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31212204))
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    ChangePatrolBehavior(Characters.VulgarMilitia0, patrol_information_id=31213205)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(Characters.VulgarMilitia0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212210)
def Event_31212210(_, character: uint):
    """Event 31212210"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31212230)
def Event_31212230(_, character: uint):
    """Event 31212230"""
    Kill(character)


@RestartOnRest(31212250)
def Event_31212250(
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
    patrol_information_id: uint,
):
    """Event 31212250"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(31210600))
    OR_2.Add(AND_1)
    
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
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    RemoveSpecialEffect(character, 8082)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(31212260)
def Event_31212260(_, character: uint, region: uint, patrol_information_id: uint):
    """Event 31212260"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagEnabled(31210600))
    OR_5.Add(AND_1)
    
    MAIN.Await(OR_5)
    
    RemoveSpecialEffect(character, 8082)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212308)
def Event_31212308(_, character: uint, region: uint):
    """Event 31212308"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    RemoveSpecialEffect(character, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212400)
def Event_31212400(
    _,
    flag: uint,
    asset: uint,
    asset_1: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 31212400"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    ForceAnimation(asset, animation_id)


@RestartOnRest(31212800)
def Event_31212800():
    """Event 31212800"""
    if FlagEnabled(31210800):
        return
    
    MAIN.Await(HealthValue(Characters.GraveWardenDuelist) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GraveWardenDuelist, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GraveWardenDuelist))
    
    KillBossAndDisplayBanner(character=Characters.GraveWardenDuelist, banner_type=BannerType.EnemyFelled)
    EnableFlag(31210800)
    EnableFlag(9243)
    if PlayerInOwnWorld():
        EnableFlag(61243)


@RestartOnRest(31212810)
def Event_31212810():
    """Event 31212810"""
    GotoIfFlagDisabled(Label.L0, flag=31210800)
    DisableCharacter(Characters.GraveWardenDuelist)
    DisableAnimations(Characters.GraveWardenDuelist)
    Kill(Characters.GraveWardenDuelist)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31210801)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GraveWardenDuelist, attacker=PLAYER))
    OR_1.Add(HasAIStatus(Characters.GraveWardenDuelist, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31212805))
    AND_1.Add(PlayerInOwnWorld())
    OR_5.Add(AND_1)
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=31212801))
    
    MAIN.Await(OR_5)
    
    EnableNetworkFlag(31210801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GraveWardenDuelist, attacker=PLAYER))
    OR_2.Add(HasAIStatus(Characters.GraveWardenDuelist, ai_status=AIStatusType.Battle))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31212805))
    AND_2.Add(FlagEnabled(31212805))
    OR_6.Add(AND_2)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=31212801))
    
    MAIN.Await(OR_6)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.GraveWardenDuelist, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GraveWardenDuelist, name=903400310)


@RestartOnRest(312112811)
def Event_312112811():
    """Event 312112811"""
    if FlagEnabled(31210800):
        return
    AND_1.Add(HealthRatio(Characters.GraveWardenDuelist) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31212852)


@RestartOnRest(31212815)
def Event_31212815():
    """Event 31212815"""
    GotoIfFlagEnabled(Label.L10, flag=31210800)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=31210801, right=0)
    GotoIfFlagEnabled(Label.L0, flag=31210801)
    OR_1.Add(FlagState(FlagSetting.On, FlagType.RelativeToThisEventSlot, 31212810))
    OR_1.Add(FlagEnabled(31210801))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(31210800))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(31210800):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(31210800))
    AND_3.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_001_9000))
    OR_3.Add(FlagEnabled(31210800))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(31210800):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        RotateToFaceEntity(PLAYER, 31212800, animation=60060, wait_for_completion=True)
    else:
        RotateToFaceEntity(PLAYER, 31212800, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=31212805)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=31212800))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(31210800))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(31210800))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(31210800):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagDisabled(31210801):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(31215800, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(31215800)
    EnableNetworkFlag(31212805)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(31210800))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_001_9000))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, 31212800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31212860)
def Event_31212860():
    """Event 31212860"""
    if FlagEnabled(31210800):
        return
    AND_1.Add(FlagEnabled(31212805))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GraveWardenDuelist, attacker=PLAYER))
    OR_1.Add(HasAIStatus(Characters.GraveWardenDuelist, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GraveWardenDuelist, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GraveWardenDuelist, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GraveWardenDuelist, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GraveWardenDuelist, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GraveWardenDuelist, state_info=260))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31212805))
    AND_1.Add(PlayerInOwnWorld())
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(31212865)
    NotifyBossBattleStart()


@RestartOnRest(31212830)
def Event_31212830(_, flag: uint, character: uint):
    """Event 31212830"""
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31032849)
def Event_31032849():
    """Event 31032849"""
    CommonFunc_9005801(
        0,
        flag=31210800,
        entity=Assets.AEG099_001_9000,
        region=31212800,
        flag_1=31212865,
        flag_2=31212806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31210800, asset=Assets.AEG099_001_9000, model_point=3, right=31210801)
    CommonFunc_9005811(0, flag=31210800, asset=Assets.AEG099_001_9001, model_point=3, right=31210801)
    CommonFunc_9005822(
        0,
        flag=31210800,
        bgm_boss_conv_param_id=931000,
        flag_1=31212805,
        flag_2=31212806,
        right=31212810,
        flag_3=31212852,
        left=31212802,
        left_1=0,
    )
