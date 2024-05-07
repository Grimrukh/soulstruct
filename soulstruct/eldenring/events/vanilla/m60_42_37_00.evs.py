"""
West Limgrave (SE) (NW)

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
from .enums.m60_42_37_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1042370000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=71001,
        flag_1=76111,
        asset=Assets.AEG099_090_9000,
        source_flag=77100,
        value=2,
        flag_2=78100,
        flag_3=78101,
        flag_4=78102,
        flag_5=78103,
        flag_6=78104,
        flag_7=78105,
        flag_8=78106,
        flag_9=78107,
        flag_10=78108,
        flag_11=78109,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, vfx_id=100, dummy_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, dummy_id=800, right=0)
    CommonFunc_90005880(
        0,
        flag=1042370800,
        flag_1=1042370805,
        flag_2=1042372800,
        character=Characters.CrucibleKnight,
        item_lot=30120,
        area_id=60,
        block_id=42,
        cc_id=37,
        dd_id=0,
        player_start=1042372805,
    )
    CommonFunc_90005881(
        0,
        flag=1042370800,
        flag_1=1042370805,
        left_flag=1042372801,
        cancel_flag__right_flag=1042372802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=42,
        cc_id=37,
        dd_id=0,
        player_start=1042372805,
    )
    CommonFunc_90005882(
        0,
        flag=1042370800,
        flag_1=1042370805,
        flag_2=1042372800,
        character=Characters.CrucibleKnight,
        flag_3=1042372806,
        character_1=1042375810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.Dummy,
        source_entity=1042372810,
        name=902500520,
        animation_id=-1,
        animation_id_1=20000,
    )
    CommonFunc_90005883(0, flag=1042370800, flag_1=1042370805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1042370800,
        bgm_boss_conv_param_id=0,
        flag_1=1042372806,
        flag_2=1042372807,
        left=0,
        left_1=1,
    )
    Event_1042372610()
    Event_1042372651(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    Event_1042373700(0, flag=78102, other_entity=Characters.TalkDummy1, flag_1=1042379204)
    Event_1042373701(0, other_entity=Characters.TalkDummy1, flag=1042379204)
    Event_1042373702(0, other_entity=Characters.TalkDummy1, flag=1042379205)
    Event_1042373703(0, other_entity=Characters.TalkDummy1, flag=1042379205)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005251(0, character=Characters.GodrickSoldier, radius=5.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1042372610)
def Event_1042372610():
    """Event 1042372610"""
    DisableAsset(Assets.AEG007_434_9000)


@RestartOnRest(1042372620)
def Event_1042372620(_, asset: uint, entity: uint, flag: uint):
    """Event 1042372620"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=200, dummy_id=803220)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1042372651)
def Event_1042372651(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1042372651"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_NW))
    AND_1.Add(PlayerDoesNotHaveGood(9109))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100690))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_2):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1042373700)
def Event_1042373700(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042373700"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372701)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042373701)
def Event_1042373701(_, other_entity: uint, flag: uint):
    """Event 1042373701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4680):
        return
    
    MAIN.Await(FlagEnabled(4680))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042373702)
def Event_1042373702(_, other_entity: uint, flag: uint):
    """Event 1042373702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    
    MAIN.Await(FlagEnabled(1042379203))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042373703)
def Event_1042373703(_, other_entity: uint, flag: uint):
    """Event 1042373703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379207):
        return
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372702)
    
    MAIN.Await(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    
    DisableFlag(1042372702)
    Restart()
