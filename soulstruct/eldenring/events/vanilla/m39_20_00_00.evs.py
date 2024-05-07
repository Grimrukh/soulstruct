"""
Ruin-Strewn Precipice

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
from .enums.m39_20_00_00_enums import *
from .enums.m60_37_51_00_enums import Assets as m60_37_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=39200001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=39200002, asset=Assets.AEG099_060_9002)
    Event_39202800()
    Event_39202810()
    Event_39202829()
    CommonFunc_9005810(
        0,
        flag=39200800,
        grace_flag=39200000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)
    Event_39202670()
    CommonFunc_90005501(
        0,
        flag=39200510,
        flag_1=39201510,
        left=0,
        asset=Assets.AEG027_010_0500,
        asset_1=Assets.AEG027_080_0501,
        asset_2=Assets.AEG027_080_0500,
        flag_2=39200511,
    )
    CommonFunc_90005501(
        0,
        flag=39200515,
        flag_1=39201515,
        left=0,
        asset=Assets.AEG027_011_0500,
        asset_1=Assets.AEG027_080_0503,
        asset_2=Assets.AEG027_080_0502,
        flag_2=39200516,
    )
    CommonFunc_90005501(
        0,
        flag=39200520,
        flag_1=39201520,
        left=0,
        asset=m60_37_Assets.AEG027_012_0000,
        asset_1=m60_37_Assets.AEG027_080_0000,
        asset_2=Assets.AEG027_080_8000,
        flag_2=39200521,
    )
    CommonFunc_90005501(
        0,
        flag=39200525,
        flag_1=39201525,
        left=1,
        asset=Assets.AEG027_001_0500,
        asset_1=Assets.AEG027_080_0505,
        asset_2=Assets.AEG027_080_0504,
        flag_2=39200526,
    )
    Event_39202500()
    CommonFunc_90005502(0, flag=39200514, asset=m60_37_Assets.AEG027_080_0000, region=39202522)
    Event_39202580()
    CommonFunc_90005780(
        0,
        flag=39200800,
        summon_flag=39202160,
        dismissal_flag=39202161,
        character=Characters.GreatHornedTragoth0,
        sign_type=20,
        region=39202700,
        right=0,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=39200800, flag_1=39202160, flag_2=39202161, character=Characters.GreatHornedTragoth0)
    CommonFunc_90005782(
        0,
        flag=39202160,
        region=39202805,
        character=Characters.GreatHornedTragoth0,
        target_entity=39202805,
        region_1=39202808,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=39200800,
        summon_flag=39202164,
        dismissal_flag=39202165,
        character=Characters.Millicent,
        sign_type=20,
        region=39202705,
        right=1042559206,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=39200800, flag_1=39202164, flag_2=39202165, character=Characters.Millicent)
    CommonFunc_90005782(
        0,
        flag=39202164,
        region=39202805,
        character=Characters.Millicent,
        target_entity=39202805,
        region_1=39202809,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=39200800,
        summon_flag=39202168,
        dismissal_flag=39202169,
        character=Characters.Blackguard,
        sign_type=20,
        region=39202720,
        right=39209250,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=39200800, flag_1=39202168, flag_2=39202169, character=Characters.Blackguard)
    CommonFunc_90005782(
        0,
        flag=39202168,
        region=39202805,
        character=Characters.Blackguard,
        target_entity=39202805,
        region_1=39202810,
        animation=0,
    )
    CommonFunc_90005795(
        0,
        flag=7606,
        flag_1=0,
        flag_2=39209200,
        left_flag=39202141,
        cancel_flag__right_flag=39202142,
        message=80606,
        action_button_id=9000,
        asset=Assets.AEG099_090_9001,
        dummy_id=30010,
    )
    if CeremonyActive(ceremony=50):
        CommonFunc_90005796(0, flag=7606, character=Characters.GreatHornedTragoth1, banner_type=5, region=39202141)
        Event_39202145()
    Event_39203700()
    Event_39203701()
    CommonFunc_90005774(0, flag=7606, item_lot=39200500, flag_1=39207500)
    Event_39203710()
    Event_39203720()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.GreatHornedTragoth1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner5, region=39202268, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.TunnelMiner1, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.TunnelMiner7, seconds=0.0, animation_id=-1)
    Event_39202280(
        0,
        character=Characters.TunnelMiner2,
        animation_id=30004,
        animation_id_1=20004,
        asset=Assets.AEG099_780_9000,
        special_effect=16576,
        seconds=0.10000000149011612,
        left=0,
    )
    Event_39202280(
        1,
        character=Characters.TunnelMiner3,
        animation_id=30000,
        animation_id_1=20000,
        asset=Assets.AEG099_780_9001,
        special_effect=16572,
        seconds=0.10000000149011612,
        left=0,
    )
    Event_39202280(
        2,
        character=Characters.TunnelMiner6,
        animation_id=30000,
        animation_id_1=20000,
        asset=Assets.AEG099_780_9002,
        special_effect=16572,
        seconds=0.10000000149011612,
        left=0,
    )
    Event_39202280(
        4,
        character=Characters.TunnelMiner4,
        animation_id=30000,
        animation_id_1=20000,
        asset=Assets.AEG099_780_9004,
        special_effect=16572,
        seconds=0.10000000149011612,
        left=0,
    )
    Event_39202260(0, character=Characters.TunnelMiner2, region=39202260)
    Event_39202260(1, character=Characters.TunnelMiner3, region=39202260)
    Event_39202260(2, character=Characters.TunnelMiner6, region=39202260)
    Event_39202230(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30002,
        animation_id_1=20002,
        special_effect=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_863_9000,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=39200244,
    )
    Event_39202240(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30005,
        animation_id_1=20005,
        flag=39200244,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.VulgarMilitia2, region=39202214, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia0,
        region=39202203,
        radius=2.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia1,
        region=39202203,
        radius=2.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia7,
        region=39202203,
        radius=2.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_39202200()
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.VulgarMilitia3, region=39202356, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.VulgarMilitia8, region=39202356, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat0, region=39202301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat1, region=39202301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat3, region=39202301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat4, region=39202301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat5, region=39202350, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat6, region=39202350, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Bat7, region=39202350, seconds=0.0, animation_id=-1)
    Event_39202302()
    Event_39202351()
    Event_39202318()
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.OldWomanBat0, region=39202350, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Octopus0, region=39202360, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Octopus1, region=39202360, seconds=0.0, animation_id=-1)
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, character=Characters.GiantOctopus)
    CommonFunc_90005300(0, flag=39200290, character=Characters.Scarab, item_lot=40290, seconds=0.0, item_is_dropped=0)


@RestartOnRest(39202145)
def Event_39202145():
    """Event 39202145"""
    if CeremonyInactive(ceremony=50):
        return
    EnableBackread(Characters.GreatHornedTragoth1)
    SetTeamType(Characters.GreatHornedTragoth1, TeamType.Human)
    EnableFlag(39202104)
    DeleteAssetVFX(Assets.AEG099_236_9001)
    CreateAssetVFX(Assets.AEG099_236_9001, vfx_id=200, dummy_id=806700)
    DeleteAssetVFX(Assets.AEG099_236_9000)
    CreateAssetVFX(Assets.AEG099_236_9000, vfx_id=200, dummy_id=806700)


@ContinueOnRest(39202500)
def Event_39202500():
    """Event 39202500"""
    CommonFunc_90005500(
        0,
        flag=39200510,
        flag_1=39201510,
        left=0,
        asset=Assets.AEG027_010_0500,
        asset_1=Assets.AEG027_080_0501,
        obj_act_id=39203511,
        asset_2=Assets.AEG027_080_0500,
        obj_act_id_1=39203512,
        region=39202511,
        region_1=39202512,
        flag_2=39200511,
        flag_3=39202512,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=39200515,
        flag_1=39201515,
        left=0,
        asset=Assets.AEG027_011_0500,
        asset_1=Assets.AEG027_080_0503,
        obj_act_id=39203516,
        asset_2=Assets.AEG027_080_0502,
        obj_act_id_1=39203517,
        region=39202516,
        region_1=39202517,
        flag_2=39200516,
        flag_3=39202517,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=39200520,
        flag_1=39201520,
        left=0,
        asset=m60_37_Assets.AEG027_012_0000,
        asset_1=m60_37_Assets.AEG027_080_0000,
        obj_act_id=39203521,
        asset_2=Assets.AEG027_080_8000,
        obj_act_id_1=39203522,
        region=39202521,
        region_1=39202522,
        flag_2=39200521,
        flag_3=39202522,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=39200525,
        flag_1=39201525,
        left=1,
        asset=Assets.AEG027_001_0500,
        asset_1=Assets.AEG027_080_0505,
        obj_act_id=39203526,
        asset_2=Assets.AEG027_080_0504,
        obj_act_id_1=39203527,
        region=39202526,
        region_1=39202527,
        flag_2=39200526,
        flag_3=39202527,
        left_1=0,
    )


@RestartOnRest(39202580)
def Event_39202580():
    """Event 39202580"""
    RegisterLadder(start_climbing_flag=39200530, stop_climbing_flag=39200531, asset=Assets.AEG027_008_0501)
    RegisterLadder(start_climbing_flag=39200532, stop_climbing_flag=39200533, asset=Assets.AEG027_007_0500)
    RegisterLadder(start_climbing_flag=39200534, stop_climbing_flag=39200535, asset=Assets.AEG027_014_0500)
    RegisterLadder(start_climbing_flag=39200536, stop_climbing_flag=39200537, asset=Assets.AEG027_008_0500)
    RegisterLadder(start_climbing_flag=39200538, stop_climbing_flag=39200539, asset=Assets.AEG027_009_0501)
    RegisterLadder(start_climbing_flag=39200540, stop_climbing_flag=39200541, asset=Assets.AEG027_045_0500)


@RestartOnRest(39202670)
def Event_39202670():
    """Event 39202670"""
    DisableAsset(39201670)
    DisableAsset(39201671)


@RestartOnRest(39202200)
def Event_39202200():
    """Event 39202200"""
    if ThisEventSlotFlagEnabled():
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.VulgarMilitia4)
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.VulgarMilitia5)
    DisableAI(Characters.VulgarMilitia4)
    DisableAI(Characters.VulgarMilitia5)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=39202207))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.VulgarMilitia4))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia4, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia4, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia4, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia4, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia4, state_info=260))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.VulgarMilitia5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia5, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia5, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia5, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia5, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.VulgarMilitia5, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=Characters.VulgarMilitia4, state=True)
    SetSpecialStandbyEndedFlag(character=Characters.VulgarMilitia5, state=True)
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=39202356))
    GotoIfConditionTrue(Label.L10, input_condition=AND_5)
    EnableAI(Characters.VulgarMilitia4)
    EnableAI(Characters.VulgarMilitia5)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(Characters.VulgarMilitia4)
    EnableAI(Characters.VulgarMilitia5)
    ChangePatrolBehavior(Characters.VulgarMilitia4, patrol_information_id=39203207)
    ChangePatrolBehavior(Characters.VulgarMilitia5, patrol_information_id=39203208)
    End()


@RestartOnRest(39202280)
def Event_39202280(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    asset: uint,
    special_effect: int,
    seconds: float,
    left: uint,
):
    """Event 39202280"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_10.Add(AssetDestroyed(asset))
    AND_1.Add(OR_10)
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
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(39202220)
def Event_39202220(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
):
    """Event 39202220"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_10.Add(AssetDestroyed(asset))
    OR_10.Add(AssetDestroyed(asset_1))
    OR_10.Add(AssetDestroyed(asset_2))
    OR_10.Add(AssetDestroyed(asset_3))
    AND_1.Add(OR_10)
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
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(39202230)
def Event_39202230(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    flag: uint,
):
    """Event 39202230"""
    if FlagEnabled(flag):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_10.Add(AssetDestroyed(asset))
    OR_10.Add(AssetDestroyed(asset_1))
    OR_10.Add(AssetDestroyed(asset_2))
    OR_10.Add(AssetDestroyed(asset_3))
    AND_1.Add(OR_10)
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
    EnableFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(39202240)
def Event_39202240(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    flag: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 39202240"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if FlagDisabled(flag):
        return
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


@RestartOnRest(39202260)
def Event_39202260(_, character: uint, region: uint):
    """Event 39202260"""
    if ThisEventSlotFlagEnabled():
        return
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.EveryTwoFrames)


@RestartOnRest(39202302)
def Event_39202302():
    """Event 39202302"""
    OR_15.Add(CharacterDead(Characters.Bat2))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=39202301))
    
    AddSpecialEffect(Characters.Bat2, 8080)
    EnableThisNetworkSlotFlag()


@RestartOnRest(39202306)
def Event_39202306():
    """Event 39202306"""
    OR_15.Add(CharacterDead(39200306))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=39202306, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=39202306))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(39200306, 8080)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_1)
    ForceAnimation(39200306, 3000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(39202318)
def Event_39202318():
    """Event 39202318"""
    OR_15.Add(CharacterDead(Characters.Bat11))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=39202318))
    
    AddSpecialEffect(Characters.Bat11, 8080)
    EnableThisNetworkSlotFlag()


@RestartOnRest(39202351)
def Event_39202351():
    """Event 39202351"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(Characters.Bat5, 8033)
    AddSpecialEffect(Characters.Bat5, 8081)
    AddSpecialEffect(Characters.Bat6, 8033)
    AddSpecialEffect(Characters.Bat6, 8081)
    AddSpecialEffect(Characters.Bat7, 8033)
    AddSpecialEffect(Characters.Bat7, 8081)
    AddSpecialEffect(Characters.Bat8, 8033)
    AddSpecialEffect(Characters.Bat8, 8081)
    AddSpecialEffect(Characters.Bat9, 8033)
    AddSpecialEffect(Characters.Bat9, 8081)
    AddSpecialEffect(Characters.Bat10, 8033)
    AddSpecialEffect(Characters.Bat10, 8081)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Bat6))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Bat7))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Bat9))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Bat10))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.OldWomanBat0))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=39202350))
    AND_1.Add(HasAIStatus(Characters.OldWomanBat0, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(Characters.Bat5, 8033)
    RemoveSpecialEffect(Characters.Bat5, 8081)
    RemoveSpecialEffect(Characters.Bat6, 8033)
    RemoveSpecialEffect(Characters.Bat6, 8081)
    RemoveSpecialEffect(Characters.Bat7, 8033)
    RemoveSpecialEffect(Characters.Bat7, 8081)
    RemoveSpecialEffect(Characters.Bat8, 8033)
    RemoveSpecialEffect(Characters.Bat8, 8081)
    RemoveSpecialEffect(Characters.Bat9, 8033)
    RemoveSpecialEffect(Characters.Bat9, 8081)
    RemoveSpecialEffect(Characters.Bat10, 8033)
    RemoveSpecialEffect(Characters.Bat10, 8081)
    AddSpecialEffect(Characters.Bat5, 8080)
    AddSpecialEffect(Characters.Bat6, 8080)
    AddSpecialEffect(Characters.Bat7, 8080)
    AddSpecialEffect(Characters.Bat8, 8080)
    AddSpecialEffect(Characters.Bat9, 8080)
    AddSpecialEffect(Characters.Bat10, 8080)
    AddSpecialEffect(Characters.OldWomanBat0, 8080)
    ChangePatrolBehavior(Characters.Bat5, patrol_information_id=39203307)
    ChangePatrolBehavior(Characters.Bat8, patrol_information_id=39203310)
    EnableThisNetworkSlotFlag()


@RestartOnRest(39202800)
def Event_39202800():
    """Event 39202800"""
    if FlagEnabled(39200800):
        return
    
    MAIN.Await(HealthValue(Characters.MagmaWyrm) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.MagmaWyrm, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(HealthValue(Characters.MagmaWyrm) == 0)
    
    KillBossAndDisplayBanner(character=Characters.MagmaWyrm, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(39200800)
    EnableFlag(9126)
    if PlayerInOwnWorld():
        EnableFlag(61126)


@RestartOnRest(39202810)
def Event_39202810():
    """Event 39202810"""
    GotoIfFlagDisabled(Label.L0, flag=39200800)
    DisableCharacter(Characters.MagmaWyrm)
    DisableAnimations(Characters.MagmaWyrm)
    Kill(Characters.MagmaWyrm)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MagmaWyrm)
    GotoIfFlagEnabled(Label.L1, flag=39200801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=39202801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.MagmaWyrm, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.MagmaWyrm, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.MagmaWyrm, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.MagmaWyrm, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.MagmaWyrm, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.MagmaWyrm, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(39200801)
    DisableHealthBar(Characters.MagmaWyrm)
    EnableAI(Characters.MagmaWyrm)
    ForceAnimation(Characters.MagmaWyrm, 3004)
    Wait(8.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(39202805))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MagmaWyrm)
    SetNetworkUpdateRate(Characters.MagmaWyrm, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableHealthBar(Characters.MagmaWyrm)
    EnableBossHealthBar(Characters.MagmaWyrm, name=904910000)


@RestartOnRest(39202829)
def Event_39202829():
    """Event 39202829"""
    CommonFunc_9005800(
        0,
        flag=39200800,
        entity=Assets.AEG099_002_9000,
        region=39202800,
        flag_1=39202805,
        character=Characters.MagmaWyrm,
        action_button_id=10000,
        left=0,
        region_1=39202801,
    )
    CommonFunc_9005801(
        0,
        flag=39200800,
        entity=Assets.AEG099_002_9000,
        region=39202800,
        flag_1=39202805,
        flag_2=39202806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=39200800, asset=Assets.AEG099_002_9000, dummy_id=5, right=0)
    CommonFunc_9005811(0, flag=39200800, asset=Assets.AEG099_002_9001, dummy_id=5, right=0)
    CommonFunc_9005822(
        0,
        flag=39200800,
        bgm_boss_conv_param_id=920900,
        flag_1=39202805,
        flag_2=39202806,
        right=0,
        flag_3=39202802,
        left=0,
        left_1=0,
    )


@RestartOnRest(39203700)
def Event_39203700():
    """Event 39203700"""
    if FlagDisabled(39200800):
        return
    if FlagDisabled(400180):
        return
    EnableFlag(39209200)
    End()


@RestartOnRest(39203701)
def Event_39203701():
    """Event 39203701"""
    if FlagEnabled(39209201):
        return
    if FlagDisabled(400180):
        return
    
    MAIN.Await(FlagEnabled(39202141))
    
    EnableFlag(39209201)
    End()


@RestartOnRest(39203710)
def Event_39203710():
    """Event 39203710"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4181, 4183)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1042559206)
    End()


@RestartOnRest(39203720)
def Event_39203720():
    """Event 39203720"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(39209250)
    if FlagEnabled(39200800):
        return
    if FlagDisabled(4140):
        return
    if FlagEnabled(4147):
        return
    if FlagEnabled(1044529259):
        return
    if FlagDisabled(1036439210):
        return
    EnableFlag(39209250)
    End()
