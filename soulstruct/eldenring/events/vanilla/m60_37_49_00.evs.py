"""
Liurnia to Altus Plateau (SW) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_37_49_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037490000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005790(
        0,
        right=0,
        flag=1037490180,
        summon_flag=1037492181,
        dismissal_flag=1037492182,
        character=Characters.FesteringFingerprintVyke,
        sign_type=23,
        region=1037492180,
        region_1=1037492181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1037490180,
        flag_1=1037492181,
        flag_2=1037492182,
        character=Characters.FesteringFingerprintVyke,
    )
    CommonFunc_90005792(
        0,
        flag=1037490180,
        flag_1=1037492181,
        flag_2=1037492182,
        character=Characters.FesteringFingerprintVyke,
        item_lot=1037490300,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1037490180,
        flag_1=1037492181,
        flag_2=1037492182,
        character=Characters.FesteringFingerprintVyke,
        other_entity=1037492180,
        region=0,
        left=0,
    )
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61023)
    CommonFunc_90005201(
        0,
        character=Characters.RayaLucariaFootSoldier2,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.RayaLucariaFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.RayaLucariaFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1037493700(0, character=Characters.VykesFingerMaiden)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.VykesFingerMaiden)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy0,
        character_1=Characters.RayaLucariaFootSoldier2,
        asset=Assets.AEG110_181_9000,
        asset_1=0,
        obj_act_id=0,
        region=1037492400,
        left=1,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy1,
        character_1=Characters.RayaLucariaFootSoldier0,
        asset=Assets.AEG110_181_9001,
        asset_1=0,
        obj_act_id=0,
        region=1037492402,
        left=1,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy2,
        character_1=Characters.RayaLucariaFootSoldier1,
        asset=Assets.AEG110_181_9002,
        asset_1=0,
        obj_act_id=0,
        region=1037492404,
        left=1,
    )


@RestartOnRest(1037493700)
def Event_1037493700(_, character: uint):
    """Event 1037493700"""
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    DisableAnimations(character)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400033):
        return
    if FlagDisabled(400031):
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6472, entity=character))
    
    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()
