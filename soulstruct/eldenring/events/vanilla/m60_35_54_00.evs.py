"""
Far West Altus Plateau (NE) (SE)

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
from .enums.m60_35_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.ManeuverableFlamethrower,
        region=1035542400,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FirePrelate,
        region=1035542200,
        radius=8.0,
        seconds=0.5,
        animation_id=-1,
    )
    Event_1035542200(0, character=Characters.FirePrelate)
    CommonFunc_90005261(0, character=Characters.FireMonk, region=1035542210, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(1, character=1035540211, region=1035542210, radius=5.0, seconds=0.0, animation_id=-1)
    Event_1035542201(0, attacker__character=1035545201, region=1035542201)
    Event_1035542236(0, character=1035540450)
    Event_1035542236(1, character=1035540451)
    Event_1035542236(2, character=1035540452)
    Event_1035542236(3, character=1035540453)
    Event_1035542236(4, character=1035540454)
    Event_1035542236(5, character=1035540455)
    Event_1035542236(6, character=1035540456)
    Event_1035542236(7, character=1035540457)
    Event_1035542236(8, character=1035540458)
    Event_1035542236(9, character=1035540459)
    CommonFunc_90005550(0, flag=1035540500, asset=Assets.AEG099_630_9000, obj_act_id=1035543500)
    CommonFunc_90005511(
        0,
        flag=1035540560,
        asset=Assets.AEG030_000_2000,
        obj_act_id=1035543560,
        obj_act_id_1=99020,
        left=0,
    )
    CommonFunc_90005512(0, flag=1035540560, region=1035542560, region_1=1035542561)
    Event_1035542580()
    Event_1035542500()
    Event_1035542450(0, asset=Assets.AEG007_434_9000)
    CommonFunc_90005261(0, character=1035540310, region=1035542310, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=1035540260,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542260,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=1035540261,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542260,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=1035540262,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542260,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper0,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542265,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.LesserFingercreeper2,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542265,
        seconds=1.399999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.LesserFingercreeper3,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542265,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=1035540268,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542265,
        seconds=1.600000023841858,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper0,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542275,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper7,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542280,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.LesserFingercreeper8,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542280,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1035540285,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542285,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=1035540286,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542285,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1035540290,
        animation_id=30003,
        animation_id_1=20003,
        region=1035542290,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=1035540291,
        animation_id=30003,
        animation_id_1=20003,
        region=1035542290,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.LesserFingercreeper10,
        animation_id=30003,
        animation_id_1=20003,
        region=1035542292,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper1,
        animation_id=30004,
        animation_id_1=20004,
        region=1035542300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper0,
        animation_id=30000,
        animation_id_1=20000,
        region=1035542275,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(
        0,
        character=Characters.LesserFingercreeper4,
        region=1035542301,
        seconds=0.5,
        animation_id=20004,
    )
    CommonFunc_AITrigger_RegionOrHurt(
        1,
        character=Characters.LesserFingercreeper5,
        region=1035542301,
        seconds=1.0,
        animation_id=20004,
    )
    CommonFunc_AITrigger_RegionOrHurt(
        2,
        character=Characters.LesserFingercreeper6,
        region=1035542301,
        seconds=1.2000000476837158,
        animation_id=20004,
    )
    CommonFunc_AITrigger_RegionOrHurt(4, character=Characters.LesserFingercreeper1, region=1035542301, seconds=1.5, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(5, character=Characters.LesserFingercreeper9, region=1035542301, seconds=1.5, animation_id=-1)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)
    Event_1035542230()
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930023, left=0)
    CommonFunc_90005730(
        0,
        flag=1035542700,
        seconds=10.0,
        flag_1=1035549200,
        flag_2=6001,
        flag_3=1035549201,
        flag_4=1035542702,
    )
    CommonFunc_90005730(
        0,
        flag=1035542700,
        seconds=20.0,
        flag_1=1035549200,
        flag_2=1035542702,
        flag_3=1035549201,
        flag_4=1035549202,
    )
    CommonFunc_90005732(0, flag=1035549200, region=1035542350, region_1=1035542350)
    Event_1035543700(0, character=Characters.WanderingNoble)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)


@RestartOnRest(1035542200)
def Event_1035542200(_, character: uint):
    """Event 1035542200"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3001, loop=True, wait_for_completion=True, skip_transition=True)
    End()


@RestartOnRest(1035542201)
def Event_1035542201(_, attacker__character: uint, region: uint):
    """Event 1035542201"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5659)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1035542201):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5659)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1035542201)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5659)


@RestartOnRest(1035542220)
def Event_1035542220():
    """Event 1035542220"""
    AddSpecialEffect(Characters.ManeuverableFlamethrower, 8089)
    
    MAIN.Await(HasAIStatus(Characters.ManeuverableFlamethrower, ai_status=AIStatusType.Battle))
    
    ForceAnimation(
        Characters.ManeuverableFlamethrower,
        3002,
        loop=True,
        wait_for_completion=True,
        skip_transition=True,
    )
    End()


@RestartOnRest(1035542230)
def Event_1035542230():
    """Event 1035542230"""
    EndOfAnimation(asset=Assets.AEG099_630_9000, animation_id=1)
    End()


@RestartOnRest(1035542236)
def Event_1035542236(_, character: uint):
    """Event 1035542236"""
    RotateToFaceEntity(character, 1035542200, animation=5002)
    WaitFrames(frames=7)
    Kill(character)
    End()


@RestartOnRest(1035542450)
def Event_1035542450(_, asset: uint):
    """Event 1035542450"""
    DisableAsset(asset)
    End()


@ContinueOnRest(1035542500)
def Event_1035542500():
    """Event 1035542500"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1035542250,
            asset=Assets.AEG007_557_1024,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )


@ContinueOnRest(1035542580)
def Event_1035542580():
    """Event 1035542580"""
    RegisterLadder(start_climbing_flag=1035540580, stop_climbing_flag=1035540581, asset=1035541580)


@RestartOnRest(1035543700)
def Event_1035543700(_, character: uint):
    """Event 1035543700"""
    if FlagEnabled(1035549201):
        return
    SetCharacterTalkRange(character=character, distance=35.0)
    
    MAIN.Await(FlagEnabled(1035549201))
    
    SetCharacterTalkRange(character=character, distance=17.0)
    End()
