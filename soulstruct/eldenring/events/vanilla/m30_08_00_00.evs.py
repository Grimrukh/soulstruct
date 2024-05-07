"""
Sainted Hero's Grave

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
from .enums.m30_08_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30080800,
        left_flag=30082840,
        cancel_flag__right_flag=30082841,
        asset=Assets.AEG099_065_9000,
        player_start=30082840,
        area_id=30,
        block_id=8,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=73008, asset=Assets.AEG099_060_9000)
    CommonFunc_90005620(
        0,
        flag=30080575,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30082575,
        cancel_flag__right_flag=30082576,
        right=30082577,
    )
    CommonFunc_90005621(0, flag=30080575, asset=Assets.AEG099_272_9000)
    CommonFunc_90005620(
        0,
        flag=30080565,
        asset=Assets.AEG027_079_9001,
        asset_1=Assets.AEG027_216_9001,
        asset_2=0,
        left_flag=30082565,
        cancel_flag__right_flag=30082566,
        right=30082567,
    )
    Event_30082564(0, flag=30080565, asset=Assets.AEG099_271_9000)
    Event_30082400(0, character=Characters.Imp0)
    Event_30082400(1, character=Characters.Imp1)
    Event_30082400(2, character=30080302)
    CommonFunc_90005261(0, character=Characters.Imp0, region=30082312, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Imp1,
        animation_id=30002,
        animation_id_1=20002,
        region=30082210,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp2, region=30082303, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(1, character=Characters.Imp3, region=30082303, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(2, character=30080305, region=30082303, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(3, character=30080306, region=30082303, radius=2.0, seconds=0.0, animation_id=0)
    Event_30082400(4, character=Characters.Imp2)
    Event_30082400(5, character=Characters.Imp3)
    Event_30082400(6, character=30080305)
    Event_30082400(7, character=30080306)
    CommonFunc_90005261(
        0,
        character=Characters.Imp4,
        region=30082307,
        radius=2.0,
        seconds=0.800000011920929,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.Imp5,
        region=30082307,
        radius=2.0,
        seconds=6.300000190734863,
        animation_id=-1,
    )
    CommonFunc_90005261(2, character=Characters.Imp6, region=30082307, radius=2.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005261(
        3,
        character=Characters.Imp7,
        region=30082307,
        radius=2.0,
        seconds=4.300000190734863,
        animation_id=-1,
    )
    Event_30082400(8, character=Characters.Imp4)
    Event_30082400(9, character=Characters.Imp5)
    Event_30082400(10, character=Characters.Imp6)
    Event_30082400(11, character=Characters.Imp7)
    Event_30082400(12, character=Characters.GraveWardenDuelist)
    CommonFunc_90005300(0, flag=30080450, character=Characters.GraveWardenDuelist, item_lot=0, seconds=3.0, item_is_dropped=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.RevenantFollower1, region=30082403, seconds=0.0, animation_id=3022)
    CommonFunc_AITrigger_RegionOrHurt(
        1,
        character=Characters.RevenantFollower2,
        region=30082403,
        seconds=0.8999999761581421,
        animation_id=3022,
    )
    CommonFunc_AITrigger_RegionOrHurt(2, character=30080405, region=30082403, seconds=0.5, animation_id=3022)
    CommonFunc_90005251(0, character=30080406, radius=4.0, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.RevenantFollower0, region=30082400, seconds=0.0, animation_id=3022)
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=30082409,
        radius=10.0,
        seconds=0.0,
        animation_id=3022,
    )
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.RevenantFollower4, region=30082410, seconds=0.0, animation_id=3022)
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower5,
        region=30082412,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_30082300(0, character=Characters.RevenantFollower5)
    CommonFunc_90005261(0, character=Characters.PutridCorpse0, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(1, character=Characters.PutridCorpse1, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(2, character=Characters.PutridCorpse2, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(3, character=Characters.PutridCorpse3, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(4, character=Characters.PutridCorpse4, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(5, character=Characters.PutridCorpse5, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(6, character=Characters.PutridCorpse6, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(7, character=Characters.PutridCorpse7, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(8, character=Characters.PutridCorpse8, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(9, character=Characters.PutridCorpse9, region=30082200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse12,
        region=30082220,
        radius=5.0,
        seconds=0.0,
        animation_id=3035,
    )
    CommonFunc_90005261(
        1,
        character=Characters.PutridCorpse13,
        region=30082220,
        radius=5.0,
        seconds=1.0,
        animation_id=3035,
    )
    CommonFunc_90005251(0, character=Characters.PutridCorpse10, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.PutridCorpse11, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse14,
        region=30082225,
        radius=5.0,
        seconds=0.0,
        animation_id=3035,
    )
    CommonFunc_90005251(0, character=Characters.RevenantFollower6, radius=7.0, seconds=0.0, animation_id=0)
    Event_30082550()
    Event_30082501()
    CommonFunc_90005200(
        0,
        character=Characters.Revenant1,
        animation_id=30000,
        animation_id_1=20000,
        region=30082461,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Revenant2,
        animation_id=30000,
        animation_id_1=20000,
        region=30082462,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005652(0, flag=30080540, asset=Assets.AEG027_041_0500, flag_1=30080400)
    CommonFunc_90005651(0, flag=30080540, anchor_entity=Assets.AEG027_041_0500)
    Event_30082401()
    Event_30082500()
    CommonFunc_90005501(
        0,
        flag=30080510,
        flag_1=30081510,
        left=3,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0501,
        asset_2=Assets.AEG027_002_0500,
        flag_2=30080511,
    )
    CommonFunc_90005513(
        0,
        flag=30080542,
        asset=Assets.AEG027_056_0500,
        asset_1=Assets.AEG027_002_0502,
        obj_act_id=30083543,
        obj_act_id_1=27115,
        animation_id=0,
        animation_id_1=0,
    )
    Event_30082510()
    Event_30082580()
    Event_30080520()
    CommonFunc_90005525(0, flag=30080570, asset=30081570)
    Event_30080790(0, asset=30081520, flag=30080800)
    Event_30082800()
    Event_30082810()
    Event_30082849()
    Event_30082811()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30080519()


@RestartOnRest(30082300)
def Event_30082300(_, character: uint):
    """Event 30082300"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3009, loop=True, skip_transition=True)
    Wait(2.0)
    ForceAnimation(character, 3012, loop=True, skip_transition=True)
    End()


@RestartOnRest(30082400)
def Event_30082400(_, character: uint):
    """Event 30082400"""
    OR_2.Add(CharacterDead(character))
    OR_2.Add(ThisEventSlotFlagEnabled())
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4320)
    DisableAnimations(character)
    OR_1.Add(CharacterInsideRegion(character=character, region=30082300))
    OR_1.Add(CharacterInsideRegion(character=character, region=30082301))
    OR_1.Add(CharacterInsideRegion(character=character, region=30082302))
    
    MAIN.Await(OR_1)
    
    EnableThisSlotFlag()
    AddSpecialEffect(character, 5881)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5882)
    RemoveSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()


@RestartOnRest(30082401)
def Event_30082401():
    """Event 30082401"""
    if FlagEnabled(30080400):
        return
    
    MAIN.Await(CharacterDead(Characters.GraveWardenDuelist))
    
    EnableFlag(30080400)
    End()


@ContinueOnRest(30082500)
def Event_30082500():
    """Event 30082500"""
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203070,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203060,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203050,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203040,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203030,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203020,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203010,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082500,
            asset_flag=30083500,
            asset=Assets.AEG027_013_0500,
            region=30082500,
            behaviour_id=801203000,
            seconds=4.0,
            right=1,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203070,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203060,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203050,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203040,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203030,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203020,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203010,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082501,
            asset_flag=30083501,
            asset=Assets.AEG027_013_0501,
            region=30082500,
            behaviour_id=801203000,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203070,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203060,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203050,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203040,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203030,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203020,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203010,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082502,
            asset_flag=30083502,
            asset=Assets.AEG027_013_0502,
            region=30082500,
            behaviour_id=801203000,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203070,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203060,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203050,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203040,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203030,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203020,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203010,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082503,
            asset_flag=30083503,
            asset=Assets.AEG027_013_0503,
            region=30082500,
            behaviour_id=801203000,
            seconds=4.5,
            right=1,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203070,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203060,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203050,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203040,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203030,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203020,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203010,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082504,
            asset_flag=30083504,
            asset=Assets.AEG027_013_0504,
            region=30082500,
            behaviour_id=801203000,
            seconds=2.0,
            right=1,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203070,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203060,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203050,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203040,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203030,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203020,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203010,
            seconds=0.0,
            right=1,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30082505,
            asset_flag=30083505,
            asset=Assets.AEG027_013_0505,
            region=30082500,
            behaviour_id=801203000,
            seconds=0.0,
            right=1,
        )


@ContinueOnRest(30082510)
def Event_30082510():
    """Event 30082510"""
    CommonFunc_90005500(
        0,
        flag=30080510,
        flag_1=30081510,
        left=3,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=30083511,
        asset_2=Assets.AEG027_002_0500,
        obj_act_id_1=30083512,
        region=30082511,
        region_1=30082512,
        flag_2=30080511,
        flag_3=30082512,
        left_1=0,
    )


@ContinueOnRest(30080519)
def Event_30080519():
    """Event 30080519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30080510)


@RestartOnRest(30080520)
def Event_30080520():
    """Event 30080520"""
    EnableAssetInvulnerability(Assets.AEG027_055_0500)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30082508))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(Assets.AEG027_055_0500)
    End()


@ContinueOnRest(30082564)
def Event_30082564(_, flag: uint, asset: uint):
    """Event 30082564"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=101, dummy_id=806043)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@ContinueOnRest(30082580)
def Event_30082580():
    """Event 30082580"""
    RegisterLadder(start_climbing_flag=30080580, stop_climbing_flag=30080581, asset=Assets.AEG027_005_0500)


@RestartOnRest(30082550)
def Event_30082550():
    """Event 30082550"""
    if FlagEnabled(30082500):
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30082460))
    AND_1.Add(CharacterBackreadEnabled(Characters.Revenant0))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(30082550)
    End()


@RestartOnRest(30082501)
def Event_30082501():
    """Event 30082501"""
    GotoIfFlagEnabled(Label.L0, flag=30082501)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30082450))
    AND_1.Add(CharacterBackreadEnabled(Characters.Revenant0))
    AND_1.Add(FlagEnabled(30082550))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(30082501)
    Wait(0.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceSpawnerToSpawn(spawner=30083460)
    EnableAI(Characters.Revenant0)
    End()


@RestartOnRest(30080790)
def Event_30080790(_, asset: uint, flag: uint):
    """Event 30080790"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ThisEventSlotFlagDisabled())
    
    MAIN.Await(AND_1)
    
    EnableThisSlotFlag()
    EnableAssetActivation(asset, obj_act_id=-1)
    End()


@RestartOnRest(30082800)
def Event_30082800():
    """Event 30082800"""
    if FlagEnabled(30080800):
        return
    
    MAIN.Await(HealthValue(Characters.AncientHeroofZamor) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.AncientHeroofZamor, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.AncientHeroofZamor))
    
    KillBossAndDisplayBanner(character=Characters.AncientHeroofZamor, banner_type=BannerType.EnemyFelled)
    EnableFlag(30080800)
    EnableFlag(9208)
    if PlayerInOwnWorld():
        EnableFlag(61208)


@RestartOnRest(30082810)
def Event_30082810():
    """Event 30082810"""
    GotoIfFlagDisabled(Label.L0, flag=30080800)
    DisableCharacter(Characters.AncientHeroofZamor)
    DisableAnimations(Characters.AncientHeroofZamor)
    Kill(Characters.AncientHeroofZamor)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.AncientHeroofZamor)
    AND_2.Add(FlagEnabled(30082805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30082800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.AncientHeroofZamor)
    SetNetworkUpdateRate(Characters.AncientHeroofZamor, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.AncientHeroofZamor, name=907100300)


@RestartOnRest(30082811)
def Event_30082811():
    """Event 30082811"""
    if FlagEnabled(30080800):
        return
    AND_1.Add(HealthRatio(Characters.AncientHeroofZamor) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30082802)


@RestartOnRest(30082849)
def Event_30082849():
    """Event 30082849"""
    CommonFunc_9005800(
        0,
        flag=30080800,
        entity=Assets.AEG099_001_9000,
        region=30082800,
        flag_1=30082805,
        character=30085800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30080800,
        entity=Assets.AEG099_001_9000,
        region=30082800,
        flag_1=30082805,
        flag_2=30082806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30080800, asset=Assets.AEG099_001_9000, dummy_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30080800,
        bgm_boss_conv_param_id=920200,
        flag_1=30082805,
        flag_2=30082806,
        right=0,
        flag_3=30082802,
        left=0,
        left_1=0,
    )
