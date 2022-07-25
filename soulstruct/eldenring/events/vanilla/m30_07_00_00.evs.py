"""
Wyndham Catacombs

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
from .entities.m30_07_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=300700, asset=Assets.AEG099_060_9000)
    CommonFunc_90005501(
        0,
        flag=30070515,
        flag_1=30070516,
        left=3,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0502,
        flag_2=30070517,
    )
    Event_30070510()
    CommonFunc_90005650(
        0,
        flag=30070540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30073541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30070540, anchor_entity=Assets.AEG027_041_0500)
    Event_30072505(0, flag=30072502, asset_flag=30073502, asset=Assets.AEG027_013_0500, region=30072502, seconds=0.0)
    Event_30072610(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020000,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072610(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020000,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072611(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020010,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072611(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020010,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072612(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020020,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072612(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020020,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072613(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020030,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072613(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020030,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072614(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020040,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072614(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020040,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072615(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020050,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072615(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020050,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072616(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020060,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072616(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020060,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072617(
        0,
        owner_entity=Characters.Dummy2,
        entity=Assets.AEG027_044_0504,
        region=30072610,
        behavior_id=801020070,
        source_entity=30072611,
        source_entity_1=30072612,
        source_entity_2=30072613,
        source_entity_3=30072614,
        source_entity_4=30072615,
        source_entity_5=30072616,
        source_entity_6=30072617,
        source_entity_7=30072618,
        source_entity_8=30072619,
        source_entity_9=30072620,
        source_entity_10=30072621,
        source_entity_11=30072622,
        source_entity_12=30072623,
    )
    Event_30072617(
        1,
        owner_entity=Characters.Dummy3,
        entity=Assets.AEG027_044_0505,
        region=30072645,
        behavior_id=801020070,
        source_entity=30072630,
        source_entity_1=30072631,
        source_entity_2=30072632,
        source_entity_3=30072633,
        source_entity_4=30072634,
        source_entity_5=30072635,
        source_entity_6=30072636,
        source_entity_7=30072637,
        source_entity_8=30072638,
        source_entity_9=30072639,
        source_entity_10=30072640,
        source_entity_11=30072641,
        source_entity_12=30072642,
    )
    Event_30072510()
    Event_30072515()
    Event_30072516()
    CommonFunc_90005513(
        0,
        flag=30070542,
        asset=Assets.AEG027_042_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=30073543,
        obj_act_id_1=27002,
        animation_id=0,
        animation_id_1=0,
    )
    CommonFunc_90005620(
        0,
        flag=30070570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30072570,
        cancel_flag__right_flag=30072571,
        right=30072572,
    )
    CommonFunc_90005621(0, flag=30070570, asset=Assets.AEG099_272_9000)
    Event_30072580()
    CommonFunc_90005646(
        0,
        flag=30070800,
        left_flag=30072840,
        cancel_flag__right_flag=30072841,
        asset=Assets.AEG099_065_9000,
        player_start=30072840,
        area_id=30,
        block_id=7,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, flag=30072800, asset=30071695, model_point=5)
    Event_30072800()
    Event_30072810()
    Event_30072849()
    Event_30072811()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=Characters.Imp0,
        animation_id=30010,
        animation_id_1=20010,
        region=30072200,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Imp1,
        animation_id=30010,
        animation_id_1=20010,
        region=30072200,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp2, region=30072205, seconds=0.0, animation_id=3004)
    CommonFunc_90005211(
        0,
        character=Characters.Imp3,
        animation_id=30002,
        animation_id_1=20002,
        region=30072205,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp4,
        animation_id=30001,
        animation_id_1=20001,
        region=30072210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp5, region=30072510, radius=7.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Imp6, region=30072216, seconds=0.0, animation_id=-1)
    Event_30072500()
    Event_30072501()
    CommonFunc_90005250(0, character=Characters.Imp7, region=30072215, seconds=1.0, animation_id=3005)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=30072300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(1, character=Characters.PutridCorpse1, region=30072300, seconds=0.0, animation_id=0)
    CommonFunc_90005250(2, character=30070302, region=30072300, seconds=0.0, animation_id=0)
    CommonFunc_90005250(3, character=30070303, region=30072300, seconds=0.0, animation_id=0)
    CommonFunc_90005250(4, character=Characters.PutridCorpse6, region=30072300, seconds=0.0, animation_id=0)
    CommonFunc_90005250(5, character=Characters.PutridCorpse7, region=30072300, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30000,
        animation_id_1=20000,
        region=30072307,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.PutridCorpse3,
        animation_id=30000,
        animation_id_1=20000,
        region=30072307,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.PutridCorpse4,
        animation_id=30000,
        animation_id_1=20000,
        region=30072307,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=Characters.PutridCorpse5,
        animation_id=30000,
        animation_id_1=20000,
        region=30072307,
        seconds=1.2999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PutridCorpse8, region=30072313, seconds=0.0, animation_id=0)
    CommonFunc_90005250(1, character=Characters.PutridCorpse9, region=30072313, seconds=0.0, animation_id=0)
    CommonFunc_90005250(2, character=Characters.PutridCorpse10, region=30072313, seconds=0.0, animation_id=0)
    CommonFunc_90005250(3, character=Characters.PutridCorpse11, region=30072313, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=30070320, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=30070321, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=30070322, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=30070323, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=30070324, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass0,
        animation_id=30000,
        animation_id_1=20000,
        region=30072350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass1,
        animation_id=30000,
        animation_id_1=20000,
        region=30072351,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30070352,
        animation_id=30000,
        animation_id_1=20000,
        region=30072352,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30070353,
        animation_id=30000,
        animation_id_1=20000,
        region=30072353,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30070354,
        animation_id=30000,
        animation_id_1=20000,
        region=30072354,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass2,
        animation_id=30000,
        animation_id_1=20000,
        region=30072355,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass3,
        animation_id=30000,
        animation_id_1=20000,
        region=30072356,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass4,
        animation_id=30000,
        animation_id_1=20000,
        region=30072357,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=30070358,
        animation_id=30000,
        animation_id_1=20000,
        region=30072350,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.LivingMass5,
        animation_id=30000,
        animation_id_1=20000,
        region=30072350,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellKnight0,
        region=30072400,
        radius=4.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrab0,
        animation_id=30001,
        animation_id_1=20001,
        region=30072410,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrab1,
        animation_id=30001,
        animation_id_1=20001,
        region=30072411,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30070519()
    Event_30072618()


@ContinueOnRest(30070510)
def Event_30070510():
    """Event 30070510"""
    CommonFunc_90005500(
        0,
        30070515,
        30070516,
        3,
        30071515,
        30071516,
        30073516,
        30071517,
        30073517,
        30072516,
        30072517,
        30070517,
        30070518,
        0,
    )


@ContinueOnRest(30070519)
def Event_30070519():
    """Event 30070519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30070515)


@RestartOnRest(30072520)
def Event_30072520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30072520"""
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


@RestartOnRest(30072341)
def Event_30072341(_, character: uint, seconds: float, region: uint, flag: uint, region_1: uint):
    """Event 30072341"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 30001)
    EnableFlag(flag)
    Wait(4.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(PlayerInOwnWorld())
    AND_2.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_2)
    
    Wait(seconds)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20001, wait_for_completion=True)


@RestartOnRest(30072500)
def Event_30072500():
    """Event 30072500"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30072215))
    AND_1.Add(CharacterBackreadEnabled(Characters.Imp6))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(30072501)
def Event_30072501():
    """Event 30072501"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30072216))
    AND_1.Add(CharacterBackreadEnabled(Characters.Imp6))
    AND_1.Add(FlagEnabled(30072500))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(0.0)
    ForceAnimation(Characters.Imp6, 3017, loop=True, wait_for_completion=True)
    DisableNetworkFlag(30072500)
    End()


@ContinueOnRest(30072505)
def Event_30072505(_, flag: uint, asset_flag: uint, asset: uint, region: uint, seconds: float):
    """Event 30072505"""
    AND_10.Add(MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)))
    AND_10.Add(FlagEnabled(flag))
    GotoIfConditionFalse(Label.L10, input_condition=AND_10)
    DisableNetworkFlag(flag)
    DisableThisSlotFlag()

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag)
    if ThisEventSlotFlagDisabled():
        Wait(seconds)
    ForceAnimation(asset, 3)
    if FlagEnabled(50):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203200,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203210,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203220,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203230,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203240,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203250,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203260,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            model_point_start=30,
            model_point_end=31,
            behaviour_id=801203270,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    Wait(1.0)
    RemoveAssetFlag(asset_flag=asset_flag)
    Wait(4.099999904632568)
    Wait(0.10000000149011612)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag)
    Restart()


@ContinueOnRest(30072510)
def Event_30072510():
    """Event 30072510"""
    GotoIfFlagEnabled(Label.L0, flag=30070510)
    OR_9.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_9.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_9.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_9)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30072510))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Assets.AEG027_004_0500, 12, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(AllPlayersOutsideRegion(region=30072510))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    EnableFlag(30070510)
    ForceAnimation(Assets.AEG027_004_0500, 20, wait_for_completion=True)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(30070510)
    ForceAnimation(Assets.AEG027_004_0500, 21, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072515)
def Event_30072515():
    """Event 30072515"""
    AND_1.Add(FlagEnabled(30070510))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30072512))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4195))
    
    MAIN.Await(AND_1)
    
    MoveAssetToCharacter(Assets.AEG003_316_9000, character=PLAYER, model_point=93)
    WaitFrames(frames=1)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303200,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303210,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303220,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303230,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303240,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303250,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303260,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=30073511,
            asset=Assets.AEG003_316_9000,
            model_point=100,
            behavior_param_id=801303270,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=30073511)
    Wait(0.5)
    Restart()


@ContinueOnRest(30072516)
def Event_30072516():
    """Event 30072516"""
    AND_1.Add(FlagEnabled(30070510))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30072511))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@ContinueOnRest(30072580)
def Event_30072580():
    """Event 30072580"""
    RegisterLadder(start_climbing_flag=30070580, stop_climbing_flag=30070581, asset=Assets.AEG027_009_0500)


@ContinueOnRest(30072605)
def Event_30072605(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
):
    """Event 30072605"""
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072610)
def Event_30072610(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072610"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072611)
def Event_30072611(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072611"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072612)
def Event_30072612(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072612"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072613)
def Event_30072613(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072613"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072614)
def Event_30072614(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072614"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagDisabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072615)
def Event_30072615(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072615"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagDisabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072616)
def Event_30072616(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072616"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagDisabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072617)
def Event_30072617(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072617"""
    OR_1.Add(FlagEnabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagDisabled(57))
    if OR_1:
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
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
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_3,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_4,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_5,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_6,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_7,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_8,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_9,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_10,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_11,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_12,
            model_point=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(30072618)
def Event_30072618():
    """Event 30072618"""
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020070,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020060,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020050,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020040,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020030,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy0,
        entity=Assets.AEG027_044_0502,
        region=30072600,
        behavior_id=801020020,
        source_entity=30072601,
        source_entity_1=30072602,
        source_entity_2=30072603,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.Dummy0,
            entity=Assets.AEG027_044_0502,
            region=30072600,
            behavior_id=801020010,
            source_entity=30072601,
            source_entity_1=30072602,
            source_entity_2=30072603,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.Dummy0,
            entity=Assets.AEG027_044_0502,
            region=30072600,
            behavior_id=801020000,
            source_entity=30072601,
            source_entity_1=30072602,
            source_entity_2=30072603,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020070,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020060,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020050,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020040,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020030,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.Dummy1,
        entity=Assets.AEG027_044_0503,
        region=30072605,
        behavior_id=801020020,
        source_entity=30072606,
        source_entity_1=30072607,
        source_entity_2=30072608,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.Dummy1,
            entity=Assets.AEG027_044_0503,
            region=30072605,
            behavior_id=801020010,
            source_entity=30072606,
            source_entity_1=30072607,
            source_entity_2=30072608,
        )
    else:
        CommonFunc_90005660(0, 30070605, 30071605, 30072605, 801020000, 30072606, 30072607, 30072608)


@RestartOnRest(30072800)
def Event_30072800():
    """Event 30072800"""
    if FlagEnabled(30070800):
        return
    
    MAIN.Await(HealthValue(Characters.ErdtreeBurialWatchdog) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.ErdtreeBurialWatchdog, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.ErdtreeBurialWatchdog))
    
    KillBossAndDisplayBanner(character=Characters.ErdtreeBurialWatchdog, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(30070800)
    EnableFlag(9212)
    if PlayerInOwnWorld():
        EnableFlag(61212)


@RestartOnRest(30072810)
def Event_30072810():
    """Event 30072810"""
    GotoIfFlagDisabled(Label.L0, flag=30070800)
    DisableCharacter(Characters.ErdtreeBurialWatchdog)
    DisableAnimations(Characters.ErdtreeBurialWatchdog)
    Kill(Characters.ErdtreeBurialWatchdog)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ErdtreeBurialWatchdog)
    AND_2.Add(FlagEnabled(30072805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30072800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.ErdtreeBurialWatchdog)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog, name=904260303)


@RestartOnRest(30072811)
def Event_30072811():
    """Event 30072811"""
    if FlagEnabled(30070800):
        return
    AND_1.Add(HealthRatio(Characters.ErdtreeBurialWatchdog) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30072802)


@RestartOnRest(30072849)
def Event_30072849():
    """Event 30072849"""
    CommonFunc_9005800(
        0,
        flag=30070800,
        entity=Assets.AEG099_001_9000,
        region=30072800,
        flag_1=30072805,
        character=30075800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30070800,
        entity=Assets.AEG099_001_9000,
        region=30072800,
        flag_1=30072805,
        flag_2=30072806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30070800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30070800, 930000, 30072805, 30072806, 0, 30072802, 0, 0)
