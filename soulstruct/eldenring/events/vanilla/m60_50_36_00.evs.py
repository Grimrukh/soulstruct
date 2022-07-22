"""
South Caelid (SE) (SW)

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
from .entities.m60_50_36_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1050360000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76458,
        flag_1=76417,
        asset=Assets.AEG099_090_9000,
        source_flag=77410,
        value=2,
        flag_2=78410,
        flag_3=78411,
        flag_4=78412,
        flag_5=78413,
        flag_6=78414,
        flag_7=78415,
        flag_8=78416,
        flag_9=78417,
        flag_10=78418,
        flag_11=78419,
    )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1050362500,
            asset=Assets.AEG007_431_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1050362502,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1050362508,
            asset=Assets.AEG007_433_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1050362509,
            asset=Assets.AEG007_433_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1050362511,
            asset=Assets.AEG007_433_1005,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    Event_1050362400(0, attacker__character=1050365400, region=1049362400)
    CommonFunc_90005251(0, character=Characters.RadahnSoldier0, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RadahnSoldier1, radius=40.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RadahnSoldier2, radius=40.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RadahnSoldier3, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1050360206, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1050360207, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1050360208, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1050360209, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier4, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1050360211, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RadahnFootSoldier0, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnFootSoldier1, region=1049362400, seconds=0.0, animation_id=-1)
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy0,
        character_1=1050360401,
        asset=1050361400,
        asset_1=0,
        obj_act_id=0,
        region=1050362400,
        left=1,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy1,
        character_1=1050360403,
        asset=1050361402,
        asset_1=0,
        obj_act_id=0,
        region=1050362402,
        left=1,
    )
    Event_1050362580()
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=51,
        cc_id=36,
        dd_id=0,
        player_start=1051360600,
        unk_8_12=0,
        flag=1050362650,
        left_flag=1050362651,
        cancel_flag__right_flag=1050362652,
        left=9410,
        text=30040,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005605(
        0,
        1050361612,
        60,
        51,
        36,
        0,
        1051360600,
        0,
        1050362653,
        1050362654,
        1050362655,
        9410,
        30040,
        0.0,
        0.0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1050362600()


@RestartOnRest(1050362400)
def Event_1050362400(_, attacker__character: uint, region: uint):
    """Event 1050362400"""
    RemoveSpecialEffect(attacker__character, 5662)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1050362400):
        return
    AddSpecialEffect(attacker__character, 5662)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    
    EnableNetworkFlag(1050362400)
    RemoveSpecialEffect(attacker__character, 5662)


@RestartOnRest(1050362600)
def Event_1050362600():
    """Event 1050362600"""
    DisableAI(1050365200)
    DisableAnimations(1050365200)


@ContinueOnRest(1050362580)
def Event_1050362580():
    """Event 1050362580"""
    RegisterLadder(start_climbing_flag=1050360580, stop_climbing_flag=1050360581, asset=Assets.AEG110_182_2000)
    RegisterLadder(start_climbing_flag=1050360582, stop_climbing_flag=1050360583, asset=Assets.AEG110_182_2001)
    RegisterLadder(start_climbing_flag=1050360584, stop_climbing_flag=1050360585, asset=Assets.AEG110_183_2000)
    RegisterLadder(start_climbing_flag=1050360586, stop_climbing_flag=1050360587, asset=Assets.AEG110_184_2000)
    RegisterLadder(start_climbing_flag=1050360588, stop_climbing_flag=1050360589, asset=Assets.AEG110_184_2001)
