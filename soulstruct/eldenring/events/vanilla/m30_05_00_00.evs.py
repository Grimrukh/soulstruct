"""
Black Knife Catacombs

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
from .entities.m30_05_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30050800,
        left_flag=30052840,
        cancel_flag__right_flag=30052841,
        asset=Assets.AEG099_065_9000,
        player_start=30052840,
        area_id=30,
        block_id=5,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005646(
        0,
        flag=30050850,
        left_flag=30052890,
        cancel_flag__right_flag=30052891,
        asset=Assets.AEG099_065_9001,
        player_start=30052840,
        area_id=30,
        block_id=5,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=300500, asset=Assets.AEG099_060_9000)
    Event_30052880()
    Event_30052800()
    Event_30052810()
    Event_30052849()
    Event_30052811()
    Event_30052850()
    Event_30052860()
    Event_30052899()
    Event_30052861()
    CommonFunc_90005616(0, flag=30057030, region=30052700)
    CommonFunc_90005650(
        0,
        flag=30050540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30053541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30050540, anchor_entity=Assets.AEG027_041_0500)
    Event_30052400()
    CommonFunc_90005513(
        0,
        flag=30050542,
        asset=Assets.AEG027_042_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=30053543,
        obj_act_id_1=27002,
        animation_id=0,
        animation_id_1=0,
    )
    CommonFunc_90005525(0, flag=30050570, asset=30051570)
    Event_30052580()
    CommonFunc_90005620(
        0,
        flag=30050575,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30052575,
        cancel_flag__right_flag=30052576,
        right=30052577,
    )
    CommonFunc_90005621(0, flag=30050575, asset=Assets.AEG099_272_9000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.CemeteryShade,
        animation_id=30001,
        animation_id_1=20001,
        region=30052800,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton15,
        animation_id=30003,
        animation_id_1=20003,
        region=30052800,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton16,
        animation_id=30003,
        animation_id_1=20003,
        region=30052800,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton17,
        animation_id=30003,
        animation_id_1=20003,
        region=30052800,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton0,
        animation_id=30003,
        animation_id_1=20003,
        region=30052200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton2,
        animation_id=30003,
        animation_id_1=20003,
        region=30052202,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30052203(0, character=Characters.CatacombsSkeleton3)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton3,
        animation_id=30003,
        animation_id_1=20003,
        region=30052202,
        seconds=1.7000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton1,
        animation_id=30003,
        animation_id_1=20003,
        region=30052302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton4,
        animation_id=30003,
        animation_id_1=20003,
        region=30052302,
        seconds=4.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton5,
        animation_id=30003,
        animation_id_1=20003,
        region=30052205,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton6,
        animation_id=30003,
        animation_id_1=20003,
        region=30052205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CatacombsSkeleton7, region=30052207, seconds=0.0, animation_id=3021)
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton8,
        animation_id=30003,
        animation_id_1=20003,
        region=30052208,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton9,
        animation_id=30003,
        animation_id_1=20003,
        region=30052209,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton10,
        animation_id=30003,
        animation_id_1=20003,
        region=30052209,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CatacombsSkeleton11, region=30052211, seconds=0.0, animation_id=3011)
    Event_30052203(1, character=Characters.CatacombsSkeleton12)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton12,
        animation_id=30003,
        animation_id_1=20003,
        region=30052212,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CatacombsSkeleton18, region=30052215, seconds=0.0, animation_id=3030)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton13,
        animation_id=30003,
        animation_id_1=20003,
        region=30052213,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton14,
        animation_id=30003,
        animation_id_1=20003,
        region=30052214,
        seconds=9.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Commoner0, region=30052450, radius=7.0, seconds=0.0, animation_id=0)
    Event_30052302()
    Event_30052300(0, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton5)
    Event_30052300(1, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton6)
    Event_30052300(2, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton8)
    Event_30052350(0, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton5)
    Event_30052350(1, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton6)
    Event_30052350(2, character=Characters.Commoner0, character_1=Characters.CatacombsSkeleton8)
    CommonFunc_90005250(0, character=Characters.Commoner1, region=30052301, seconds=0.0, animation_id=3015)
    Event_30052301()
    Event_30052300(3, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton9)
    Event_30052300(4, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton10)
    Event_30052300(5, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton11)
    Event_30052350(3, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton9)
    Event_30052350(4, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton10)
    Event_30052350(5, character=Characters.Commoner1, character_1=Characters.CatacombsSkeleton11)
    CommonFunc_90005250(0, character=Characters.Commoner2, region=30052302, seconds=0.0, animation_id=3015)
    Event_30052300(6, character=Characters.Commoner2, character_1=Characters.CatacombsSkeleton1)
    Event_30052300(7, character=Characters.Commoner2, character_1=Characters.CatacombsSkeleton4)
    Event_30052350(6, character=Characters.Commoner2, character_1=Characters.CatacombsSkeleton1)
    Event_30052350(7, character=Characters.Commoner2, character_1=Characters.CatacombsSkeleton4)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms0, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms1, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms2, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms3, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms4, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms5, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms6, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms7, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms8, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms9, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms10, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms11, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms12, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms13, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SmallCrabWorms14, region=30052400, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrabInjured0,
        animation_id=30001,
        animation_id_1=20001,
        region=30052450,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30052450(
        0,
        character=Characters.LargeCrabInjured1,
        animation_id=30001,
        animation_id_1=20001,
        region=30052450,
        seconds=8.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005780(
        0,
        flag=30050850,
        summon_flag=30052160,
        dismissal_flag=30052161,
        character=Characters.DHunteroftheDead,
        sign_type=20,
        region=30052711,
        right=11109649,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=30050850, flag_1=30052160, flag_2=30052161, character=Characters.DHunteroftheDead)
    CommonFunc_90005782(
        0,
        flag=30052160,
        region=30052855,
        character=Characters.DHunteroftheDead,
        target_entity=30052855,
        region_1=30052809,
        animation=0,
    )


@ContinueOnRest(30052580)
def Event_30052580():
    """Event 30052580"""
    RegisterLadder(start_climbing_flag=30050580, stop_climbing_flag=30050581, asset=Assets.AEG027_000_0500)


@RestartOnRest(30052203)
def Event_30052203(_, character: uint):
    """Event 30052203"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 17210)
    EnableThisNetworkSlotFlag()


@RestartOnRest(30052300)
def Event_30052300(_, character: uint, character_1: uint):
    """Event 30052300"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 14716))
    
    AddSpecialEffect(character_1, 14717)
    EnableThisNetworkSlotFlag()


@RestartOnRest(30052301)
def Event_30052301():
    """Event 30052301"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30052310))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Commoner1))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    Wait(4.0)
    ChangePatrolBehavior(Characters.Commoner1, patrol_information_id=30053310)


@RestartOnRest(30052302)
def Event_30052302():
    """Event 30052302"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30052205))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Commoner0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(Characters.Commoner0, 3015)


@RestartOnRest(30052350)
def Event_30052350(_, character: uint, character_1: uint):
    """Event 30052350"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterDead(character))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14717))
    OR_11.Add(CharacterDoesNotHaveSpecialEffect(character_1, 5080))
    OR_11.Add(CharacterDoesNotHaveSpecialEffect(character_1, 5450))
    AND_1.Add(OR_11)
    
    MAIN.Await(AND_1)
    
    Wait(0.800000011920929)
    RemoveSpecialEffect(character_1, 5860)
    Kill(character_1, award_runes=True)
    EnableThisNetworkSlotFlag()


@ContinueOnRest(30052400)
def Event_30052400():
    """Event 30052400"""
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202070,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202060,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202050,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202040,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202030,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202020,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202010,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30052650,
            asset_flag=30053500,
            asset=Assets.AEG027_013_0500,
            region=30052650,
            behaviour_id=801202000,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202070,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202060,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202050,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202040,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202030,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202020,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202010,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30052702,
            asset_flag=30053502,
            asset=Assets.AEG027_013_0501,
            region=30052650,
            behaviour_id=801202000,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202070,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202060,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202050,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202040,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202030,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202020,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202010,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30052704,
            asset_flag=30053504,
            asset=Assets.AEG027_013_0502,
            region=30052650,
            behaviour_id=801202000,
            seconds=0.0,
            right=0,
        )


@RestartOnRest(30052450)
def Event_30052450(
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
    """Event 30052450"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=30052451))
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
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=30052451))
    SkipLinesIfConditionTrue(6, AND_4)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()
    Wait(2.5)
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


@RestartOnRest(30052800)
def Event_30052800():
    """Event 30052800"""
    if FlagEnabled(30050800):
        return
    
    MAIN.Await(HealthValue(Characters.CemeteryShade) <= 0)
    
    Kill(30055800)
    Wait(4.0)
    PlaySoundEffect(Characters.CemeteryShade, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.CemeteryShade))
    
    KillBossAndDisplayBanner(character=Characters.CemeteryShade, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG099_630_9000, obj_act_id=-1)
    Kill(Characters.CatacombsSkeleton16)
    Kill(Characters.CatacombsSkeleton15)
    Kill(Characters.CatacombsSkeleton17)
    EnableFlag(30050800)
    if PlayerInOwnWorld():
        EnableFlag(61205)
    EnableFlag(9205)


@RestartOnRest(30052850)
def Event_30052850():
    """Event 30052850"""
    if FlagEnabled(30050850):
        return
    
    MAIN.Await(HealthValue(Characters.BlackKnifeAssassin) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BlackKnifeAssassin, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.BlackKnifeAssassin))
    
    KillBossAndDisplayBanner(character=Characters.BlackKnifeAssassin, banner_type=BannerType.EnemyFelled)
    EnableFlag(30050850)
    if PlayerInOwnWorld():
        EnableFlag(61221)
    EnableFlag(9221)


@RestartOnRest(30052810)
def Event_30052810():
    """Event 30052810"""
    GotoIfFlagDisabled(Label.L0, flag=30050800)
    DisableCharacter(30055800)
    DisableCharacter(30060815)
    DisableCharacter(30060816)
    DisableCharacter(30060817)
    DisableAnimations(30055800)
    DisableAnimations(30060815)
    DisableAnimations(30060816)
    DisableAnimations(30060817)
    Kill(30055800)
    Kill(Characters.CatacombsSkeleton16)
    Kill(Characters.CatacombsSkeleton15)
    Kill(Characters.CatacombsSkeleton17)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.CemeteryShade)
    DisableAssetActivation(Assets.AEG099_630_9000, obj_act_id=-1)
    AND_2.Add(FlagEnabled(30052805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30052800))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.CemeteryShade)
    SetNetworkUpdateRate(Characters.CemeteryShade, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CemeteryShade, name=903664301)


@RestartOnRest(30052811)
def Event_30052811():
    """Event 30052811"""
    if FlagEnabled(30050800):
        return
    AND_1.Add(HealthRatio(Characters.CemeteryShade) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30052802)


@ContinueOnRest(30052825)
def Event_30052825(_, flag: uint, region: uint, character: uint, target_entity: uint, region_1: uint, animation: int):
    """Event 30052825"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(region))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    OR_15.Add(TimeElapsed(seconds=4.0))
    OR_14.Add(OR_15)
    OR_14.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_14)
    
    RestartIfFinishedConditionTrue(input_condition=OR_15)
    if ValueNotEqual(left=animation, right=0):
        RotateToFaceEntity(character, target_entity, animation=animation, wait_for_completion=True)
    else:
        RotateToFaceEntity(character, target_entity, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_5)
    
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)


@RestartOnRest(30052880)
def Event_30052880():
    """Event 30052880"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(30050570))
    AND_1.Add(FlagDisabled(30050850))
    OR_1.Add(AND_1)
    OR_1.Add(FlagDisabled(30050800))
    EnableFlag(30050880)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(30050880)
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 30050800))
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 30050850))
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 30050570))
    AwaitConditionTrue(OR_2)
    Restart()


@RestartOnRest(30052860)
def Event_30052860():
    """Event 30052860"""
    GotoIfFlagDisabled(Label.L0, flag=30050850)
    DisableCharacter(Characters.BlackKnifeAssassin)
    DisableAnimations(Characters.BlackKnifeAssassin)
    Kill(Characters.BlackKnifeAssassin)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BlackKnifeAssassin)
    AND_2.Add(FlagEnabled(30052855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30052855))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.BlackKnifeAssassin)
    SetNetworkUpdateRate(Characters.BlackKnifeAssassin, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BlackKnifeAssassin, name=902100301)


@RestartOnRest(30052861)
def Event_30052861():
    """Event 30052861"""
    if FlagEnabled(30050850):
        return
    AND_1.Add(HealthRatio(Characters.BlackKnifeAssassin) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30052852)


@RestartOnRest(30052849)
def Event_30052849():
    """Event 30052849"""
    Event_30052870(
        0,
        flag=30050800,
        entity=Assets.AEG099_001_9000,
        region=30052800,
        flag_1=30052805,
        character=30055800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30050800,
        entity=Assets.AEG099_001_9000,
        region=30052800,
        flag_1=30052805,
        flag_2=30052806,
        action_button_id=10000,
    )
    CommonFunc_9005813(0, flag=30050800, asset=Assets.AEG099_001_9000, model_point=3, right=0, model_point_1=3)
    CommonFunc_9005822(
        0,
        flag=30050800,
        bgm_boss_conv_param_id=930000,
        flag_1=30052805,
        flag_2=30052806,
        right=0,
        flag_3=30052802,
        left=0,
        left_1=0,
    )


@RestartOnRest(30052899)
def Event_30052899():
    """Event 30052899"""
    Event_30052870(
        1,
        flag=30050850,
        entity=Assets.AEG099_001_9002,
        region=30052855,
        flag_1=30052855,
        character=30055850,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30050850,
        entity=Assets.AEG099_001_9002,
        region=30052855,
        flag_1=30052855,
        flag_2=30052856,
        action_button_id=10000,
    )
    CommonFunc_9005813(0, flag=30050850, asset=Assets.AEG099_001_9002, model_point=3, right=0, model_point_1=3)
    CommonFunc_9005822(
        0,
        flag=30050850,
        bgm_boss_conv_param_id=921500,
        flag_1=30052855,
        flag_2=30052856,
        right=0,
        flag_3=30052852,
        left=0,
        left_1=0,
    )


@RestartOnRest(30052870)
def Event_30052870(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 30052870"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    else:
        RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishPhantoms(unknown=0)
    BanishInvaders(unknown=0)
    Restart()
