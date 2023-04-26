"""
Northeast Mountaintops (SW) (SE)

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
from .enums.m60_53_56_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1053562200(0, character=1053565200)
    Event_1053562250(
        0,
        flag=1053560250,
        destination=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1053562250(
        1,
        flag=1053560251,
        destination=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1053562250(
        2,
        flag=1053560252,
        destination=Assets.AEG099_160_9002,
        character=Characters.Balloon2,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1053562260(
        0,
        flag=1053560250,
        asset=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        character_1=1053565250,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1053560700,
        flag_1=1053562250,
    )
    Event_1053562260(
        1,
        flag=1053560251,
        asset=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        character_1=1053565251,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1053560710,
        flag_1=1053562251,
    )
    Event_1053562260(
        2,
        flag=1053560252,
        asset=Assets.AEG099_160_9002,
        character=Characters.Balloon2,
        character_1=1053565252,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1053560720,
        flag_1=1053562252,
    )
    Event_1053562270(
        0,
        flag=1053560250,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        radius=45.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag_1=1053562250,
    )
    Event_1053562270(
        1,
        flag=1053560250,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character=Characters.Marionette7,
        animation_id=30010,
        animation_id_1=20010,
        radius=45.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag_1=1053562250,
    )
    Event_1053562270(
        3,
        flag=1053560251,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character=Characters.Marionette3,
        animation_id=30010,
        animation_id_1=20010,
        radius=35.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag_1=1053562251,
    )
    Event_1053562270(
        4,
        flag=1053560251,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character=Characters.Marionette8,
        animation_id=30010,
        animation_id_1=20010,
        radius=35.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag_1=1053562251,
    )
    Event_1053562270(
        5,
        flag=1053560251,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character=Characters.Marionette9,
        animation_id=30010,
        animation_id_1=20010,
        radius=35.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag_1=1053562251,
    )
    CommonFunc_90005880(
        0,
        flag=1053560800,
        flag_1=1053560805,
        flag_2=1053562800,
        character=Characters.RoundtableKnightVyke,
        item_lot=30515,
        area_id=60,
        block_id=53,
        cc_id=56,
        dd_id=0,
        player_start=1053562805,
    )
    CommonFunc_90005881(
        0,
        flag=1053560800,
        flag_1=1053560805,
        left_flag=1053562801,
        cancel_flag__right_flag=1053562802,
        message=20300,
        anchor_entity=Assets.AEG099_171_1000,
        area_id=60,
        block_id=53,
        cc_id=56,
        dd_id=0,
        player_start=1053562805,
    )
    CommonFunc_90005882(
        0,
        flag=1053560800,
        flag_1=1053560805,
        flag_2=1053562800,
        character=Characters.RoundtableKnightVyke,
        flag_3=1053562806,
        character_1=1053565810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.TalkDummy,
        source_entity=1053562810,
        name=130401,
        animation_id=-1,
        animation_id_1=90005,
    )
    CommonFunc_90005883(0, flag=1053560800, flag_1=1053560805, entity=Assets.AEG099_171_1000)
    CommonFunc_90005885(
        0,
        flag=1053560800,
        bgm_boss_conv_param_id=921100,
        flag_1=1053562806,
        flag_2=1053562807,
        left=0,
        left_1=1,
    )
    Event_1053562820(0, flag=1053560800, flag_1=1053560805)
    CommonFunc_90005620(
        0,
        flag=1053560570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1053562570,
        cancel_flag__right_flag=1053562571,
        right=1053562572,
    )
    CommonFunc_90005621(0, flag=1053560570, asset=Assets.AEG099_272_9000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1053560700)


@RestartOnRest(1053562200)
def Event_1053562200(_, character: uint):
    """Event 1053562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1053562250)
def Event_1053562250(
    _,
    flag: uint,
    destination: uint,
    character: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1053562250"""
    if FlagEnabled(flag):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    if AND_1:
        return
    ForceAnimation(destination, 0)
    Move(character, destination=destination, destination_type=CoordEntityType.Asset, model_point=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1053562260)
def Event_1053562260(
    _,
    flag: uint,
    asset: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot: int,
    flag_1: uint,
):
    """Event 1053562260"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=200, model_point=803160)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ForceAnimation(asset, 1)
    DeleteAssetVFX(asset)
    Wait(1.0)
    DisableAsset(asset)
    if PlayerInOwnWorld():
        Wait(0.30000001192092896)
        AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1053562270)
def Event_1053562270(
    _,
    flag: uint,
    seconds: float,
    attacked_entity: uint,
    seconds_1: float,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag_1: uint,
):
    """Event 1053562270"""
    if FlagEnabled(flag):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, animation_id)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=character, other_entity=20000, radius=radius))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag_1)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    Wait(seconds_2)
    ForceAnimation(character, animation_id_1)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1053562820)
def Event_1053562820(_, flag: uint, flag_1: uint):
    """Event 1053562820"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=5)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=True)
