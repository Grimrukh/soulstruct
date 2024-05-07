"""
Auriza Hero's Grave

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
from .enums.m30_10_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73010, asset=Assets.AEG099_060_9000)
    CommonFunc_90005646(
        0,
        flag=30100800,
        left_flag=30102840,
        cancel_flag__right_flag=30102841,
        asset=Assets.AEG099_065_9000,
        player_start=30102840,
        area_id=30,
        block_id=10,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005501(
        0,
        flag=30100510,
        flag_1=30101510,
        left=1,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30100511,
    )
    CommonFunc_90005501(
        0,
        flag=30100515,
        flag_1=30101515,
        left=3,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0502,
        asset_2=Assets.AEG027_002_0503,
        flag_2=30100516,
    )
    CommonFunc_90005501(
        0,
        flag=30100510,
        flag_1=30100511,
        left=1,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30100512,
    )
    CommonFunc_90005501(
        0,
        flag=30100515,
        flag_1=30100516,
        left=3,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0502,
        asset_2=Assets.AEG027_002_0503,
        flag_2=30100517,
    )
    Event_30102510()
    CommonFunc_90005680(
        0,
        flag=30100500,
        flag_1=30100501,
        flag_2=30100502,
        flag_3=30100503,
        asset=Assets.AEG027_057_0500,
    )
    Event_30102500()
    Event_30102560()
    Event_30102580()
    Event_30102200()
    Event_30100100(0, flag=30100540, asset=Assets.AEG027_041_0500, obj_act_id=30103540, obj_act_id_1=27041)
    CommonFunc_90005620(
        0,
        flag=30100570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30102570,
        cancel_flag__right_flag=30102571,
        right=30102572,
    )
    CommonFunc_90005621(0, flag=30100570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005200(
        0,
        character=30100202,
        animation_id=30003,
        animation_id_1=20003,
        region=30102202,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=30100203,
        animation_id=30003,
        animation_id_1=20003,
        region=30102202,
        seconds=0.0,
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
        region=30102200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.CatacombsSkeleton1,
        animation_id=30003,
        animation_id_1=20003,
        region=30102200,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Basilisk6, region=30102205, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.Basilisk7, region=30102205, seconds=0.5, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.CatacombsSkeleton2, region=30102215, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton3,
        animation_id=30003,
        animation_id_1=20003,
        region=30102211,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton4,
        animation_id=30003,
        animation_id_1=20003,
        region=30102212,
        radius=5.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.CatacombsSkeleton5, region=30102213, seconds=0.0, animation_id=3011)
    CommonFunc_90005200(
        0,
        character=30100228,
        animation_id=30003,
        animation_id_1=20003,
        region=30102228,
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
        region=30102236,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.CatacombsSkeleton10,
        animation_id=30003,
        animation_id_1=20003,
        region=30102236,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=30100238,
        animation_id=30003,
        animation_id_1=20003,
        region=30102236,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=30100239,
        animation_id=30003,
        animation_id_1=20003,
        region=30102236,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.CatacombsSkeleton11, region=30102240, seconds=0.0, animation_id=3008)
    CommonFunc_90005200(
        1,
        character=30100241,
        animation_id=30003,
        animation_id_1=20003,
        region=30102240,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.CatacombsSkeleton6, region=30102232, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.CatacombsSkeleton7, region=30102232, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(2, character=Characters.CatacombsSkeleton8, region=30102232, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Basilisk0, region=30102250, seconds=0.0, animation_id=3001)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.Basilisk1, region=30102250, seconds=0.0, animation_id=3001)
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk2,
        animation_id=30001,
        animation_id_1=20001,
        region=30102255,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Basilisk3,
        animation_id=30001,
        animation_id_1=20001,
        region=30102255,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.Basilisk4,
        animation_id=30001,
        animation_id_1=20001,
        region=30102255,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=Characters.Basilisk5,
        animation_id=30001,
        animation_id_1=20001,
        region=30102258,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Basilisk8, region=30102209, radius=1.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005261(0, character=Characters.Basilisk9, region=30102219, radius=10.0, seconds=0.5, animation_id=0)
    CommonFunc_90005261(1, character=Characters.Basilisk10, region=30102219, radius=10.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(2, character=Characters.Basilisk11, region=30102219, radius=10.0, seconds=4.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Basilisk12, region=30102221, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.Basilisk13,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Omen, region=30102300, seconds=0.0, animation_id=0)
    Event_30102480()
    Event_30102490()
    Event_30102400(0, character=Characters.MercilessChariot0)
    Event_30102410(
        4,
        character=Characters.MercilessChariot0,
        region=30102454,
        patrol_information_id=30103451,
        region_1=30102455,
        patrol_information_id_1=30103452,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.MercilessChariot1, region=30102415, seconds=0.0, animation_id=0)
    Event_30102400(1, character=Characters.MercilessChariot1)
    Event_30102410(
        1,
        character=Characters.MercilessChariot1,
        region=30102410,
        patrol_information_id=30103410,
        region_1=30102411,
        patrol_information_id_1=30103411,
    )
    Event_30102410(
        2,
        character=Characters.MercilessChariot1,
        region=30102413,
        patrol_information_id=30103411,
        region_1=30102412,
        patrol_information_id_1=30103412,
    )
    Event_30102465(0, character=Characters.MercilessChariot1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.MercilessChariot2, region=30102425, seconds=0.0, animation_id=0)
    Event_30102400(2, character=Characters.MercilessChariot2)
    Event_30102410(
        3,
        character=Characters.MercilessChariot2,
        region=30102420,
        patrol_information_id=30103420,
        region_1=30102412,
        patrol_information_id_1=30103421,
    )
    Event_30102465(1, character=Characters.MercilessChariot2)
    Event_30102445()
    Event_30102450(slot=1)
    Event_30102455(slot=2)
    Event_30102460(slot=3)
    Event_30102470()
    Event_30102800()
    Event_30102810()
    Event_30102849()
    Event_30102811()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30100050()
    Event_30100519()


@ContinueOnRest(30100050)
def Event_30100050():
    """Event 30100050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(30100100)
def Event_30100100(_, flag: uint, asset: uint, obj_act_id: uint, obj_act_id_1: int):
    """Event 30100100"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1)
    End()


@RestartOnRest(30102200)
def Event_30102200():
    """Event 30102200"""
    DeleteAssetVFX(Assets.AEG020_948_1000, erase_root=False)
    DeleteAssetVFX(Assets.AEG020_948_1001, erase_root=False)
    DeleteAssetVFX(Assets.AEG027_057_0500, erase_root=False)
    CreateAssetVFX(Assets.AEG020_948_1000, vfx_id=201, dummy_id=806721)
    CreateAssetVFX(Assets.AEG020_948_1001, vfx_id=201, dummy_id=806721)
    CreateAssetVFX(Assets.AEG027_057_0500, vfx_id=108, dummy_id=806721)
    End()


@RestartOnRest(30102400)
def Event_30102400(_, character: uint):
    """Event 30102400"""
    GotoIfFlagEnabled(Label.L0, flag=30102465)
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(30102300)
def Event_30102300(_, asset__asset_flag: uint, other_entity: uint):
    """Event 30102300"""
    if FlagEnabled(30100465):
        return
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=PLAYER, radius=2.4000000953674316))
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=other_entity, radius=2.4000000953674316))
    if FlagEnabled(30100465):
        return
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(30100465):
        return
    CreateHazard(
        asset_flag=asset__asset_flag,
        asset=asset__asset_flag,
        dummy_id=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=2.299999952316284,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30102305)
def Event_30102305(_, asset__asset_flag: uint, other_entity: uint):
    """Event 30102305"""
    if FlagEnabled(30100465):
        return
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=PLAYER, radius=3.0999999046325684))
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=other_entity, radius=3.0999999046325684))
    if FlagEnabled(30100465):
        return
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(30100465):
        return
    CreateHazard(
        asset_flag=asset__asset_flag,
        asset=asset__asset_flag,
        dummy_id=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=3.0999999046325684,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30102410)
def Event_30102410(
    _,
    character: uint,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
):
    """Event 30102410"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    Restart()


@RestartOnRest(30102445)
def Event_30102445():
    """Event 30102445"""
    if PlayerNotInOwnWorld():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30102405))
    AND_1.Add(FlagDisabled(30102445))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(30102460):
        return
    DisableAI(Characters.MercilessChariot0)
    EnableFlag(30102445)
    DisableFlag(30102450)
    DisableFlag(30102455)
    ForceAnimation(Characters.MercilessChariot0, 20001, loop=True, wait_for_completion=True, skip_transition=True)
    Move(
        Characters.MercilessChariot0,
        destination=30102460,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Characters.MercilessChariot0,
    )
    ForceAnimation(Characters.MercilessChariot0, 20000, loop=True, wait_for_completion=True, skip_transition=True)
    ChangePatrolBehavior(Characters.MercilessChariot0, patrol_information_id=30103400)
    Wait(1.5)
    EnableAI(Characters.MercilessChariot0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(30102450)
def Event_30102450():
    """Event 30102450"""
    if PlayerNotInOwnWorld():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30102451))
    AND_1.Add(FlagDisabled(30102450))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(30102460):
        return
    DisableAI(Characters.MercilessChariot0)
    DisableFlag(30102445)
    EnableFlag(30102450)
    DisableFlag(30102455)
    ResetAnimation(Characters.MercilessChariot0)
    ForceAnimation(Characters.MercilessChariot0, 20001, loop=True, wait_for_completion=True)
    Move(
        Characters.MercilessChariot0,
        destination=30102461,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Characters.MercilessChariot0,
    )
    ForceAnimation(Characters.MercilessChariot0, 20000, loop=True, wait_for_completion=True)
    ChangePatrolBehavior(Characters.MercilessChariot0, patrol_information_id=30103450)
    Wait(1.5)
    EnableAI(Characters.MercilessChariot0)
    Restart()


@RestartOnRest(30102455)
def Event_30102455():
    """Event 30102455"""
    if PlayerNotInOwnWorld():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30102452))
    AND_1.Add(FlagDisabled(30102455))
    AND_1.Add(FlagDisabled(30100550))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(30102460):
        return
    AND_2.Add(FlagDisabled(30100503))
    AND_2.Add(FlagDisabled(30100500))
    
    MAIN.Await(AND_2)
    
    DisableAI(Characters.MercilessChariot0)
    DisableFlag(30102445)
    EnableFlag(30102455)
    DisableFlag(30102450)
    ResetAnimation(Characters.MercilessChariot0)
    ForceAnimation(Characters.MercilessChariot0, 20001, loop=True, wait_for_completion=True)
    Move(
        Characters.MercilessChariot0,
        destination=30102462,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Characters.MercilessChariot0,
    )
    ForceAnimation(Characters.MercilessChariot0, 20000, loop=True, wait_for_completion=True)
    ChangePatrolBehavior(Characters.MercilessChariot0, patrol_information_id=30103451)
    Wait(1.5)
    EnableAI(Characters.MercilessChariot0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(30102460)
def Event_30102460():
    """Event 30102460"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(30102460):
        return
    AND_2.Add(FlagEnabled(30100500))
    AND_2.Add(FlagDisabled(30100503))
    
    MAIN.Await(AND_2)
    
    GotoIfFlagDisabled(Label.L0, flag=30100500)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30102453))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=30100500)
    DisableAI(Characters.MercilessChariot0)
    ResetAnimation(Characters.MercilessChariot0)
    ForceAnimation(Characters.MercilessChariot0, 20001, loop=True, wait_for_completion=True)
    Move(
        Characters.MercilessChariot0,
        destination=30102463,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Characters.MercilessChariot0,
    )
    ForceAnimation(Characters.MercilessChariot0, 20000, loop=True, wait_for_completion=True)
    DisableFlag(30102445)
    EnableFlag(30102450)
    EnableFlag(30102455)
    EnableFlag(30102460)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(30102465)
def Event_30102465(_, character: uint):
    """Event 30102465"""
    AND_1.Add(FlagEnabled(30102460))
    AND_1.Add(CharacterInsideRegion(character=character, region=30102470))
    
    MAIN.Await(AND_1)
    
    Kill(character)
    Kill(Characters.MercilessChariot0)
    AND_2.Add(CharacterInsideRegion(character=Characters.MercilessChariot0, region=30102470))
    AND_2.Add(CharacterInsideRegion(character=Characters.MercilessChariot1, region=30102470))
    AND_2.Add(CharacterInsideRegion(character=Characters.MercilessChariot2, region=30102470))
    
    MAIN.Await(AND_2)
    
    EnableFlag(30100465)
    End()


@RestartOnRest(30102470)
def Event_30102470():
    """Event 30102470"""
    if FlagEnabled(30102460):
        return
    AND_1.Add(FlagEnabled(30102445))
    AND_1.Add(CharacterBackreadDisabled(Characters.MercilessChariot0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(30102445)
    Restart()


@RestartOnRest(30102480)
def Event_30102480():
    """Event 30102480"""
    if FlagDisabled(30100465):
        return
    DisableCharacter(Characters.MercilessChariot0)
    DisableCharacter(Characters.MercilessChariot1)
    DisableCharacter(Characters.MercilessChariot2)
    End()


@RestartOnRest(30102490)
def Event_30102490():
    """Event 30102490"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(30107100):
        return
    
    MAIN.Await(FlagEnabled(30100465))
    
    if PlayerNotInOwnWorld():
        return
    AwardItemLot(30100100, host_only=False)
    End()


@ContinueOnRest(30102510)
def Event_30102510():
    """Event 30102510"""
    CommonFunc_90005500(
        0,
        flag=30100510,
        flag_1=30100511,
        left=1,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0500,
        obj_act_id=30103511,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=30103512,
        region=30102511,
        region_1=30102512,
        flag_2=30100512,
        flag_3=30100513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=30100515,
        flag_1=30100516,
        left=3,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0502,
        obj_act_id=30103516,
        asset_2=Assets.AEG027_002_0503,
        obj_act_id_1=30103517,
        region=30102516,
        region_1=30102517,
        flag_2=30100517,
        flag_3=30100518,
        left_1=0,
    )


@ContinueOnRest(30100519)
def Event_30100519():
    """Event 30100519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30100510)


@ContinueOnRest(30102500)
def Event_30102500():
    """Event 30102500"""
    CommonFunc_90005681(0, flag=30100500, flag_1=30100501, flag_2=30100502, flag_3=30100503, attacked_entity=30101500)
    Event_30102521(0, flag=30100503, region=30102500, entity=Characters.TalkDummy0)


@ContinueOnRest(30102520)
def Event_30102520(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    dummy_id: int,
    dummy_id_1: int,
    dummy_id_2: int,
    dummy_id_3: int,
    dummy_id_4: int,
    dummy_id_5: int,
    dummy_id_6: int,
    dummy_id_7: int,
):
    """Event 30102520"""
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=dummy_id_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=dummy_id_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=dummy_id_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=dummy_id_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=dummy_id_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=dummy_id_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@ContinueOnRest(30102521)
def Event_30102521(_, flag: uint, region: uint, entity: uint):
    """Event 30102521"""
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=entity)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103300,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103300,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103300,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103310,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103310,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103310,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103320,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103320,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103320,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103330,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103330,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103330,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103340,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103340,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103340,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103350,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103350,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103350,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103360,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103360,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103360,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103370,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=102,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103370,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=104,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103370,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=Characters.TalkDummy0,
            source_entity=Assets.AEG027_057_0500,
            dummy_id=109,
            behavior_id=801103305,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(7.199999809265137)
    Restart()


@ContinueOnRest(30102530)
def Event_30102530(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    dummy_id: int,
    dummy_id_1: int,
    dummy_id_2: int,
    dummy_id_3: int,
    dummy_id_4: int,
    dummy_id_5: int,
    dummy_id_6: int,
    dummy_id_7: int,
):
    """Event 30102530"""
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=dummy_id_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=dummy_id_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_4,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_5,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_6,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_7,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@ContinueOnRest(30102540)
def Event_30102540(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, attacked_entity: uint):
    """Event 30102540"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    OR_1.Add(FlagDisabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(AND_2)
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    
    MAIN.Await(OR_4)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(2, unk_state=False, game_map=(0, 0, 0, 0))  # NOTE: useless skip
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(1, unk_state=False, game_map=(0, 0, 0, 0))  # NOTE: useless skip
    DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(FlagEnabled(flag))
    AND_6.Add(FlagDisabled(flag_1))
    AND_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_6.Add(AND_6)
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    
    MAIN.Await(OR_8)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(2, unk_state=False, game_map=(0, 0, 0, 0))  # NOTE: useless skip
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(1, unk_state=False, game_map=(0, 0, 0, 0))  # NOTE: useless skip
    DisableNetworkFlag(flag_3)
    DisableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_3))
    
    Restart()


@RestartOnRest(301002550)
def Event_301002550():
    """Event 301002550"""
    AND_1.Add(FlagEnabled(30100550))
    AND_1.Add(FlagDisabled(30100500))
    
    MAIN.Await(AND_1)
    
    DisableFlag(30100550)
    Restart()


@RestartOnRest(30102560)
def Event_30102560():
    """Event 30102560"""
    GotoIfFlagEnabled(Label.L0, flag=30100500)
    DeleteVFX(30102463)
    Wait(5.0)
    CreateVFX(30102462)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(30102462)
    Wait(5.0)
    CreateVFX(30102463)
    Restart()


@ContinueOnRest(30102580)
def Event_30102580():
    """Event 30102580"""
    RegisterLadder(start_climbing_flag=30100580, stop_climbing_flag=30100581, asset=Assets.AEG027_009_0500)
    RegisterLadder(start_climbing_flag=30100582, stop_climbing_flag=30100583, asset=30101582)
    RegisterLadder(start_climbing_flag=30100584, stop_climbing_flag=30100585, asset=Assets.AEG027_064_0500)


@RestartOnRest(30102800)
def Event_30102800():
    """Event 30102800"""
    if FlagEnabled(30100800):
        return
    AND_1.Add(HealthValue(Characters.CrucibleKnight0) <= 0)
    AND_1.Add(HealthValue(Characters.CrucibleKnight1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CrucibleKnight0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.CrucibleKnight0))
    AND_2.Add(CharacterDead(Characters.CrucibleKnight1))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.CrucibleKnight0, banner_type=BannerType.EnemyFelled)
    EnableFlag(30100800)
    EnableFlag(9210)
    if PlayerInOwnWorld():
        EnableFlag(61210)


@RestartOnRest(30102810)
def Event_30102810():
    """Event 30102810"""
    GotoIfFlagDisabled(Label.L0, flag=30100800)
    DisableCharacter(Characters.CrucibleKnight0)
    DisableAnimations(Characters.CrucibleKnight0)
    Kill(Characters.CrucibleKnight0)
    DisableCharacter(Characters.CrucibleKnight1)
    DisableAnimations(Characters.CrucibleKnight1)
    Kill(Characters.CrucibleKnight1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.CrucibleKnight0)
    DisableAI(Characters.CrucibleKnight1)
    AND_2.Add(FlagEnabled(30102805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30102800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.CrucibleKnight0)
    SetNetworkUpdateRate(Characters.CrucibleKnight0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CrucibleKnight0, name=902500300)
    EnableAI(Characters.CrucibleKnight1)
    SetNetworkUpdateRate(Characters.CrucibleKnight1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CrucibleKnight1, name=902500301, bar_slot=1)


@RestartOnRest(30102811)
def Event_30102811():
    """Event 30102811"""
    if FlagEnabled(30100800):
        return
    OR_1.Add(CharacterDead(Characters.CrucibleKnight0))
    OR_1.Add(CharacterDead(Characters.CrucibleKnight1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(30102802)


@RestartOnRest(30102849)
def Event_30102849():
    """Event 30102849"""
    CommonFunc_9005800(
        0,
        flag=30100800,
        entity=Assets.AEG099_001_9000,
        region=30102800,
        flag_1=30102805,
        character=30105800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30100800,
        entity=Assets.AEG099_001_9000,
        region=30102800,
        flag_1=30102805,
        flag_2=30102806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30100800, asset=Assets.AEG099_001_9000, dummy_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30100800,
        bgm_boss_conv_param_id=920200,
        flag_1=30102805,
        flag_2=30102806,
        right=0,
        flag_3=30102802,
        left=0,
        left_1=0,
    )
