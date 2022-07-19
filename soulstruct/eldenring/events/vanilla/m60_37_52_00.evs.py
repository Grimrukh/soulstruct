"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_52_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76354, asset=1037521950, enemy_block_distance=3.0, character=0)
    CommonFunc_90005261(0, 1037520204, 1037522204, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520205, 1037522204, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520206, 1037522204, 10.0, 0.0, -1)
    CommonFunc_90005261(
        0,
        character=Characters.DemiHuman2,
        region=1037522500,
        radius=7.0,
        seconds=1.5,
        animation_id=3022,
    )
    CommonFunc_90005261(
        0,
        character=Characters.IronVirgin,
        region=1037522500,
        radius=10.0,
        seconds=1.0,
        animation_id=3013,
    )
    CommonFunc_90005261(0, 1037520301, 1037522301, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520303, 1037522301, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520304, 1037522301, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520305, 1037522301, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1037520401, 1037522301, 10.0, 0.0, -1)
    CommonFunc_90005211(
        0,
        character=Characters.DemiHumanBeastman0,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522405,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, 1037520300, 1037522302, 5.0, 2.0, -1)
    CommonFunc_90005261(0, 1037520310, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(1, 1037520311, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(2, 1037520312, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(3, 1037520313, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(4, 1037520314, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(5, 1037520315, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005261(6, 1037520350, 1037522350, 10.0, 0.0, -1)
    CommonFunc_90005771(0, 1037520951, 1037522700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005300(0, flag=1037520355, character=1037525350, item_lot_param_id=0, seconds=0.0, left=0)
    CommonFunc_90005600(0, grace_flag=1037520001, asset=Assets.AEG099_060_9001, enemy_block_distance=5.0, character=0)
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower0,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower1,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower2,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower3,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower4,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower5,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower6,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower7,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522614,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1037520622, 30000, 20000, 1037522614, 0.0, 0, 0, 0, 0)


@RestartOnRest(1035542210)
def Event_1035542210(_, character: uint):
    """Event 1035542210"""
    AND_1.Add(FlagEnabled(1037520350))
    if AND_1:
        return
    DisableCharacter(character)
    
    MAIN.Await(HealthRatio(Characters.RayaLucariaScholar) < 0.699999988079071)
    
    EnableCharacter(character)
    AddSpecialEffect(character, 8971)


@RestartOnRest(1037522220)
def Event_1037522220():
    """Event 1037522220"""
    Kill(1037520220)
    Kill(1037520221)
    Kill(1037520222)
    Kill(1037520223)
    Kill(1037520224)
    Kill(1037520225)
    Kill(1037520226)
    Kill(1037520227)
    Kill(1037520228)
    Kill(1037520229)


@RestartOnRest(1037522900)
def Event_1037522900(
    _,
    grace_flag: uint,
    character: uint,
    asset: uint,
    enemy_block_distance: float,
    character_1: uint,
    character_2: uint,
    flag: uint,
):
    """Event 1037522900"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_2)
    DisableAsset(asset)
    Wait(1.0)
    
    MAIN.Await(CharacterDead(character_1))
    
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=asset, model_point=200, anchor_type=CoordEntityType.Asset)
    EnableFlag(flag)
    Wait(0.5)
    EnableCharacter(character)
    EnableCharacter(character_2)
    EnableAsset(asset)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(
        grace_flag=grace_flag,
        asset=asset,
        reaction_distance=5.0,
        reaction_angle=180.0,
        enemy_block_distance=enemy_block_distance,
    )


@RestartOnRest(1037522300)
def Event_1037522300():
    """Event 1037522300"""
    RemoveSpecialEffect(Characters.DemiHuman6, 5070)
    RemoveSpecialEffect(Characters.DemiHumanShaman0, 5070)


@RestartOnRest(1037522350)
def Event_1037522350(_, character: uint):
    """Event 1037522350"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3021, wait_for_completion=True)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037522370)
def Event_1037522370(_, character: uint):
    """Event 1037522370"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3022, wait_for_completion=True)
    DisableThisSlotFlag()
    End()
