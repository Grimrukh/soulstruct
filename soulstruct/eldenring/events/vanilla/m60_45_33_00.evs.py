"""
East Weeping Peninsula (SW) (NE)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_45_33_00_entities import *
from .entities.m60_33_40_00_entities import Assets as m60_33_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1045330000, asset=Assets.AEG099_060_9000)
    CommonFunc_9005910(0, asset=1045331940, first_flag=1045330101, last_flag=1045330103, right=3)
    CommonFunc_9005911(0, asset=1045331941)
    CommonFunc_9005912(0, flag=1045330100, text=605053)
    CommonFunc_90005300(0, flag=1045330200, character=Characters.Turtle0, item_lot=45000000, seconds=0.0, left=0)
    Event_1045332220()
    Event_1045332250(0, flag=1045330200, flag_1=1045330201, flag_2=1045330202, flag_3=1045330205)
    Event_1045332251(0, flag=1045330200, attacked_entity=Characters.Turtle0)
    Event_1045332251(1, flag=1045330201, attacked_entity=Characters.Turtle1)
    Event_1045332251(2, flag=1045330202, attacked_entity=Characters.Turtle2)
    Event_1045332252(0, flag=1045330200, character=Characters.Turtle0)
    Event_1045332252(1, flag=1045330201, character=Characters.Turtle1)
    Event_1045332252(2, flag=1045330202, character=Characters.Turtle2)
    Event_1045332253()
    Event_1045332254()
    Event_1045332255()
    Event_1045332256()
    CommonFunc_90005300(0, flag=1045330200, character=Characters.Turtle0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1045330201, character=Characters.Turtle1, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1045330202, character=Characters.Turtle2, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005251(0, character=Characters.Turtle1, radius=0.0, seconds=0.0, animation_id=0)
    CommonFunc_90005300(0, flag=1045330900, character=Characters.OnyxLord, item_lot=1045330400, seconds=0.0, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=1045330210, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330211, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330212, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330213, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330214, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330215, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330216, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330217, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330218, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=1045330219, region=1045332210, radius=15.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005251(0, character=Characters.OnyxLord, radius=20.0, seconds=0.0, animation_id=1700)
    Event_1045332265(0, vfx_id=1045332200)
    Event_1045332265(1, vfx_id=1045332201)
    Event_1045332265(2, vfx_id=1045332202)
    Event_1045332265(3, vfx_id=1045332203)
    Event_1045332265(4, vfx_id=1045332204)
    Event_1045332265(5, vfx_id=1045332205)
    Event_1045332265(6, vfx_id=1045332206)
    Event_1045332265(7, vfx_id=1045332207)
    Event_1045332265(8, vfx_id=1045332208)
    Event_1045332265(9, vfx_id=1045332209)
    Event_1045332265(10, vfx_id=1045332210)
    Event_1045332265(11, vfx_id=1045332211)
    Event_1045332265(12, vfx_id=1045332212)
    Event_1045332265(13, vfx_id=1045332213)
    Event_1045332265(14, vfx_id=1045332214)
    Event_1045332265(15, vfx_id=1045332215)
    Event_1045332265(16, vfx_id=1045332216)


@RestartOnRest(1045332220)
def Event_1045332220():
    """Event 1045332220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.WolfPackLeader, radius=30.0))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(Characters.WolfPackLeader, 3011)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1045332220, unk_8_12=1)
    End()


@RestartOnRest(1045332250)
def Event_1045332250(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1045332250"""
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    CreateAssetVFX(Assets.AEG099_251_2000, vfx_id=200, model_point=1500)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_3)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    PlaySoundEffect(Assets.AEG099_251_2000, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()


@RestartOnRest(1045332251)
def Event_1045332251(_, flag: uint, attacked_entity: uint):
    """Event 1045332251"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 20008)
    EnableFlag(flag)


@RestartOnRest(1045332252)
def Event_1045332252(_, flag: uint, character: uint):
    """Event 1045332252"""
    DisableCharacter(character)
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        EnableInvincibility(character)
    AND_1.Add(FlagEnabled(1045332621))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1045332253)
def Event_1045332253():
    """Event 1045332253"""
    DisableNetworkSync()
    if FlagEnabled(1045330205):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=m60_33_Assets.AEG099_251_2000))
    OR_1.Add(FlagEnabled(1045330205))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1045330205):
        return
    DisplayDialog(text=20200, anchor_entity=Assets.AEG099_251_2000)
    Wait(1.0)
    Restart()


@RestartOnRest(1045332254)
def Event_1045332254():
    """Event 1045332254"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_004_2000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60011, anchor_entity=Assets.AEG099_004_2000)
    if PlayerInOwnWorld():
        EnableNetworkFlag(1045332621)
    Wait(1.0)
    Restart()


@RestartOnRest(1045332255)
def Event_1045332255():
    """Event 1045332255"""
    RegisterLadder(start_climbing_flag=45330580, stop_climbing_flag=45330851, asset=Assets.AEG110_119_2000)


@RestartOnRest(1045332256)
def Event_1045332256():
    """Event 1045332256"""
    if FlagEnabled(1045330202):
        return
    if PlayerNotInOwnWorld():
        return
    SetNetworkUpdateAuthority(PLAYER, authority_level=UpdateAuthority.Forced)
    AddSpecialEffect(Characters.Turtle2, 11434)
    Move(Characters.Turtle2, destination=1045331202, destination_type=CoordEntityType.Region, short_move=True)
    AND_1.Add(AttackedWithDamageType(attacked_entity=Characters.Turtle2, attacker=PLAYER))
    SkipLinesIfConditionFalse(2, AND_1)
    Kill(Characters.Turtle2)
    End()
    Wait(7.0)
    Restart()


@RestartOnRest(1045332260)
def Event_1045332260(_, vfx_id: uint, earliest_hour: uchar, earliest_minute: uchar, flag: uint):
    """Event 1045332260"""
    DeleteVFX(vfx_id, erase_root_only=False)
    DisableNetworkFlag(flag)
    if FlagEnabled(1045330900):
        return
    WaitUntilRandomTimeOfDay(earliest=(earliest_hour, earliest_minute, 0), latest=(1, 0, 0))
    EnableNetworkFlag(flag)
    CreateVFX(vfx_id)
    AND_1.Add(TimeOfDayInRange(earliest=(1, 0, 1), latest=(20, 59, 59)))
    AND_1.Add(HasAIStatus(Characters.OnyxLord, ai_status=AIStatusType.Normal))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(1045330900))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(1045332265)
def Event_1045332265(_, vfx_id: uint):
    """Event 1045332265"""
    GotoIfFlagEnabled(Label.L0, flag=1045330900)
    
    MAIN.Await(CharacterDead(Characters.OnyxLord))

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()


@RestartOnRest(1045332900)
def Event_1045332900():
    """Event 1045332900"""
    if FlagEnabled(1045330900):
        return
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return RESTART
    if FlagEnabled(1045332901):
        return
    DisableCharacter(Characters.OnyxLord)
    DisableAnimations(Characters.OnyxLord)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    AND_1.Add(TimeOfDayInRange(earliest=(0, 0, 0), latest=(1, 0, 0)))
    
    MAIN.Await(AND_1)
    
    CreateAssetVFX(Assets.AEG099_090_9000, vfx_id=100, model_point=806901)
    
    MAIN.Await(TimeOfDayInRange(earliest=(1, 0, 1), latest=(23, 59, 59)))
    
    Restart()


@RestartOnRest(1045332920)
def Event_1045332920():
    """Event 1045332920"""
    if FlagEnabled(1045330900):
        return
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return RESTART
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(TimeOfDayInRange(earliest=(0, 0, 0), latest=(1, 0, 0)))
    AND_3.Add(ActionButtonParamActivated(action_button_id=9250, entity=Assets.AEG099_090_9001))
    
    MAIN.Await(AND_3)
    
    Wait(2.0)
    EnableFlag(1045332901)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=Assets.AEG099_090_9000, anchor_type=CoordEntityType.Asset)
    EnableCharacter(Characters.OnyxLord)
    EnableAnimations(Characters.OnyxLord)
