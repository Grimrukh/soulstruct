"""
Northwest Caelid (SE) (SE)

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
from .entities.m60_47_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1047400900, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76403,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=1,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402502,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402506,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402507,
            asset=Assets.AEG007_433_1001,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402511,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
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
            asset_flag=1047402512,
            asset=Assets.AEG007_470_2001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    CommonFunc_90005683(0, flag=62410, asset=Assets.AEG099_055_2000, vfx_id=207, flag_1=78490, flag_2=78490)
    CommonFunc_90005620(
        0,
        flag=1047400570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1047402570,
        cancel_flag__right_flag=1047402571,
        right=1047402572,
    )
    CommonFunc_90005621(0, flag=1047400570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005250(0, character=Characters.MonstrousCrow0, region=1047402259, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400259, region=1047402259, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MonstrousCrow1, region=1047402260, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=1047400290, character=Characters.Scarab, item_lot_param_id=40400, seconds=0.0, left=0)
    Event_1047402399()
    CommonFunc_90005250(0, character=Characters.Dummy, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse1, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse2, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse3, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse4, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse5, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse6, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse7, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse8, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse9, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse10, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse11, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse12, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse13, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse14, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse15, region=1047402399, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400321, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400322, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400323, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400324, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400325, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400326, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400327, region=1047402321, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400328, region=1047402321, seconds=0.0, animation_id=-1)
    Event_1047402302()
    CommonFunc_90005250(0, character=Characters.PutridCorpse16, region=1047402336, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse17, region=1047402336, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse18, region=1047402336, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse19, region=1047402336, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse20, region=1047402340, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse21, region=1047402340, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse22, region=1047402340, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse23, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse24, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare1, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare2, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare3, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare4, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare5, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare6, region=1047402402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare7, region=1047402336, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1047400468, region=1047402468, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1047400391, radius=60.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005870(0, character=Characters.PutridAvatar, name=904811602, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1047400800,
        left=0,
        character=Characters.PutridAvatar,
        left_1=0,
        item_lot__item_lot_param_id=30410,
        seconds=0.0,
    )
    CommonFunc_90005872(0, 1047400800, 18, 0)


@RestartOnRest(1047402301)
def Event_1047402301(_, character: uint, region: uint, patrol_information_id: uint):
    """Event 1047402301"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(1047402302)
def Event_1047402302():
    """Event 1047402302"""
    DisableCharacter(Characters.PutridCorpse0)
    DisableCharacter(Characters.PutridCorpse1)
    DisableCharacter(Characters.PutridCorpse2)
    DisableCharacter(Characters.PutridCorpse3)
    DisableCharacter(Characters.PutridCorpse4)
    DisableCharacter(Characters.PutridCorpse5)
    DisableCharacter(Characters.PutridCorpse6)
    DisableCharacter(Characters.PutridCorpse7)
    DisableCharacter(Characters.PutridCorpse8)
    DisableCharacter(Characters.PutridCorpse9)
    DisableCharacter(Characters.PutridCorpse10)
    DisableCharacter(Characters.PutridCorpse11)
    DisableCharacter(Characters.PutridCorpse12)
    DisableCharacter(Characters.PutridCorpse13)
    DisableCharacter(Characters.PutridCorpse14)
    DisableCharacter(Characters.PutridCorpse15)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1047402399))
    
    EnableCharacter(Characters.PutridCorpse0)
    EnableCharacter(Characters.PutridCorpse1)
    EnableCharacter(Characters.PutridCorpse2)
    EnableCharacter(Characters.PutridCorpse3)
    EnableCharacter(Characters.PutridCorpse4)
    EnableCharacter(Characters.PutridCorpse5)
    EnableCharacter(Characters.PutridCorpse6)
    EnableCharacter(Characters.PutridCorpse7)
    EnableCharacter(Characters.PutridCorpse8)
    EnableCharacter(Characters.PutridCorpse9)
    EnableCharacter(Characters.PutridCorpse10)
    EnableCharacter(Characters.PutridCorpse11)
    EnableCharacter(Characters.PutridCorpse12)
    EnableCharacter(Characters.PutridCorpse13)
    EnableCharacter(Characters.PutridCorpse14)
    EnableCharacter(Characters.PutridCorpse15)


@RestartOnRest(1047402399)
def Event_1047402399():
    """Event 1047402399"""
    MAIN.Await(CharacterInsideRegion(character=Characters.Dummy, region=1046402399))
    
    Wait(30.0)
    ChangePatrolBehavior(Characters.Dummy, patrol_information_id=1046403201)
