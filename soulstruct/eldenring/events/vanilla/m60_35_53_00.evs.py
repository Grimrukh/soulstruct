"""
Far West Altus Plateau (SE) (NE)

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
from .enums.m60_35_53_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76355, asset=Assets.AEG099_060_9000, enemy_block_distance=5.0, character=0)
    Event_1035532200(0, attacker__character=1035535200, region=1035532200)
    Event_1035532210()
    CommonFunc_90005251(
        0,
        character=Characters.ThornSorcerer1,
        radius=10.0,
        seconds=0.20000000298023224,
        animation_id=-1,
    )
    CommonFunc_90005251(
        1,
        character=Characters.ThornSorcerer6,
        radius=10.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005251(
        2,
        character=Characters.ThornSorcerer7,
        radius=10.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005251(
        3,
        character=Characters.ThornSorcerer0,
        radius=10.0,
        seconds=0.4000000059604645,
        animation_id=-1,
    )
    CommonFunc_90005251(4, character=1035530254, radius=10.0, seconds=0.4000000059604645, animation_id=-1)
    CommonFunc_90005261(0, character=1035530230, region=1035532230, radius=30.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1035530231, region=1035532230, radius=30.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.ManeuverableFlamethrower,
        region=1035532400,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MagmaWyrm,
        animation_id=30001,
        animation_id_1=20001,
        region=1035532346,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.MagmaWyrm, region=1035532346, seconds=0.5, animation_id=3004)
    Event_1035532300()
    CommonFunc_90005870(0, character=Characters.MagmaWyrm, name=904910600, npc_threat_level=5)
    CommonFunc_90005861(
        0,
        flag=1035530800,
        left=1035530800,
        character=Characters.MagmaWyrm,
        left_1=1,
        item_lot=30390,
        text=30062,
        seconds=0.0,
    )
    Event_1035532500()
    Event_1035532450(0, asset=Assets.AEG007_434_9000)
    Event_1035532450(1, asset=Assets.AEG007_434_9001)
    Event_1035532450(2, asset=Assets.AEG007_434_9002)
    CommonFunc_90005704(0, attacked_entity=Characters.LivingPot, flag=3661, flag_1=3660, flag_2=1043399301, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot,
        flag=3661,
        flag_1=3662,
        flag_2=1043399301,
        flag_3=3661,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.LivingPot, flag=3663, first_flag=3660, last_flag=3663)
    Event_1035533700(0, character=Characters.LivingPot)
    Event_1035533701()
    CommonFunc_90005730(
        0,
        flag=1035532702,
        seconds=40.0,
        flag_1=1035539206,
        flag_2=1051369265,
        flag_3=1035539205,
        flag_4=1035539205,
    )


@RestartOnRest(1035532200)
def Event_1035532200(_, attacker__character: uint, region: uint):
    """Event 1035532200"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5658)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1050562200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5658)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1050562200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5658)


@ContinueOnRest(1035532210)
def Event_1035532210():
    """Event 1035532210"""
    AddSpecialEffect(1035530210, 8092)
    AddSpecialEffect(1035530211, 8092)


@RestartOnRest(1035532300)
def Event_1035532300():
    """Event 1035532300"""
    MAIN.Await(HasAIStatus(Characters.MagmaWyrm, ai_status=AIStatusType.Battle))
    
    ForceAnimation(Characters.MagmaWyrm, 3004, skip_transition=True)
    End()


@RestartOnRest(1035532340)
def Event_1035532340(_, character: uint, region: uint, destination: uint):
    """Event 1035532340"""
    if FlagEnabled(1035530340):
        End()
    AND_1.Add(FlagDisabled(1035530340))
    ForceAnimation(character, 30001, loop=True)
    AND_2.Add(FlagDisabled(1035530340))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20002, loop=True)
    EnableNetworkFlag(1035530340)
    End()


@RestartOnRest(1035532450)
def Event_1035532450(_, asset: uint):
    """Event 1035532450"""
    DisableAsset(asset)
    End()


@ContinueOnRest(1035532500)
def Event_1035532500():
    """Event 1035532500"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1035532250,
            asset=Assets.AEG007_557_1025,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1035532251,
            asset=Assets.AEG007_557_1026,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1035532252,
            asset=Assets.AEG007_557_1027,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )


@RestartOnRest(1035533700)
def Event_1035533700(_, character: uint):
    """Event 1035533700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3669))
    OR_1.Add(FlagEnabled(3670))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_2.Add(FlagEnabled(3669))
    OR_2.Add(FlagEnabled(3670))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930020)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3669))
    AND_15.Add(FlagDisabled(3670))
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1035533701)
def Event_1035533701():
    """Event 1035533701"""
    AND_1.Add(FlagDisabled(3669))
    AND_1.Add(FlagDisabled(3670))
    if AND_1:
        return
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.LivingPot, radius=90.0))
    EnableNetworkFlag(1035539204)
    AwaitFlagEnabled(flag=1035530800)
    if FlagDisabled(1035539207):
        EnableNetworkFlag(1035539207)
        Wait(20.0)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.LivingPot, radius=90.0))
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1035539206)
    AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.LivingPot, radius=90.0))
    AwaitConditionTrue(AND_4)
    DisableNetworkFlag(1035539206)
    Restart()
