"""
Southwest Liurnia (SW) (SE)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_33_40_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1033400000, asset=Assets.AEG099_060_9000)
    Event_1033402510()
    CommonFunc_90005501(
        0,
        flag=1033400510,
        flag_1=1033400511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        asset_2=Assets.AEG099_182_2000,
        flag_2=1033400512,
    )
    Event_1033402610(0, flag=1033400610, flag_1=1033420610, flag_2=1035410610, flag_3=1033400615)
    Event_1034432613(0, flag=1033400610, character=Characters.GiantTurtle)
    Event_1034432614(0, flag=1033400610, attacked_entity=Characters.GiantTurtle)
    Event_1033402611()
    Event_1034432612()
    CommonFunc_90005201(
        0,
        character=Characters.GiantTurtle,
        animation_id=30006,
        animation_id_1=20006,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=1033400610, character=Characters.GiantTurtle, item_lot=0, seconds=0.0, item_is_dropped=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1033400519()


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    Event_1033402615()


@RestartOnRest(1033402510)
def Event_1033402510():
    """Event 1033402510"""
    CommonFunc_90005500(
        0,
        flag=1033400510,
        flag_1=1033400511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        obj_act_id=1033403511,
        asset_2=Assets.AEG099_182_2000,
        obj_act_id_1=1033403512,
        region=1033402511,
        region_1=1033402512,
        flag_2=1033400512,
        flag_3=1033400513,
        left_1=0,
    )


@ContinueOnRest(1033400519)
def Event_1033400519():
    """Event 1033400519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1033400510)
    EnableThisSlotFlag()


@RestartOnRest(1033402610)
def Event_1033402610(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1033402610"""
    GotoIfFlagDisabled(Label.L0, flag=flag_3)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    CreateAssetVFX(Assets.AEG099_251_2000, vfx_id=200, dummy_id=1500)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_3)
    PlaySoundEffect(Assets.AEG099_251_2000, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()


@RestartOnRest(1033402611)
def Event_1033402611():
    """Event 1033402611"""
    DisableNetworkSync()
    if FlagEnabled(1033400615):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=Assets.AEG099_251_2000))
    OR_1.Add(FlagEnabled(1033400615))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1033400615):
        return
    DisplayDialog(text=20200, anchor_entity=Assets.AEG099_251_2000)
    Wait(1.0)
    Restart()


@RestartOnRest(1034432612)
def Event_1034432612():
    """Event 1034432612"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_004_2001))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60026, anchor_entity=Assets.AEG099_004_2001)
    if PlayerInOwnWorld():
        EnableNetworkFlag(1034432616)
    Wait(1.0)
    Restart()


@RestartOnRest(1034432613)
def Event_1034432613(_, flag: uint, character: uint):
    """Event 1034432613"""
    if FlagEnabled(flag):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    if PlayerNotInOwnWorld():
        EnableInvincibility(character)
    AND_1.Add(FlagEnabled(1034432616))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1034432614)
def Event_1034432614(_, flag: uint, attacked_entity: uint):
    """Event 1034432614"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    ForceAnimation(attacked_entity, 20008)
    EnableFlag(flag)


@RestartOnRest(1033402615)
def Event_1033402615():
    """Event 1033402615"""
    if FlagEnabled(1033400615):
        return
    AND_1.Add(FlagEnabled(1033400610))
    AND_1.Add(FlagEnabled(1033420610))
    AND_1.Add(FlagEnabled(1035410610))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
