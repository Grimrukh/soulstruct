"""
Southeast Liurnia (SE) (NW)

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
from .entities.m60_38_41_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038410000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76202,
        asset=Assets.AEG099_090_9001,
        source_flag=77200,
        value=2,
        flag_2=78200,
        flag_3=78201,
        flag_4=78202,
        flag_5=78203,
        flag_6=78204,
        flag_7=78205,
        flag_8=78206,
        flag_9=78207,
        flag_10=78208,
        flag_11=78209,
    )
    CommonFunc_90005880(
        0,
        flag=1038410800,
        flag_1=1038410805,
        flag_2=1038412800,
        character=Characters.AdanThiefofFire,
        item_lot_param_id=30245,
        area_id=60,
        block_id=38,
        cc_id=41,
        dd_id=0,
        player_start=1038412805,
    )
    CommonFunc_90005881(
        0,
        flag=1038410800,
        flag_1=1038410805,
        left_flag=1038412801,
        cancel_flag__right_flag=1038412802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=38,
        cc_id=41,
        dd_id=0,
        player_start=1038412805,
    )
    CommonFunc_90005882(
        0,
        flag=1038410800,
        flag_1=1038410805,
        flag_2=1038412800,
        character=Characters.AdanThiefofFire,
        flag_3=1038412806,
        character_1=1038415810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.TalkDummy0,
        source_entity=1038412810,
        name=900000520,
        animation_id=-1,
        animation_id_1=90005,
    )
    CommonFunc_90005883(0, flag=1038410800, flag_1=1038410805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1038410800,
        bgm_boss_conv_param_id=0,
        flag_1=1038412806,
        flag_2=1038412807,
        left=0,
        left_1=1,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Hyetta, flag=3381, flag_1=3380, flag_2=1038419201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Hyetta,
        flag=3381,
        flag_1=3382,
        flag_2=1038419201,
        flag_3=3381,
        first_flag=3380,
        last_flag=3384,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Hyetta, flag=3383, first_flag=3380, last_flag=3384)
    Event_1038413700(0, character=Characters.Hyetta)
    CommonFunc_90005706(0, character=1038410720, animation_id=30018, left=0)
    CommonFunc_90005725(
        0,
        flag=4740,
        flag_1=4741,
        flag_2=4743,
        flag_3=1043339205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1038416700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4741,
        flag_1=4742,
        flag_2=1043339206,
        flag_3=4741,
        first_flag=4740,
        last_flag=4744,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4741, flag_1=4740, flag_2=1043339206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4743, first_flag=4740, last_flag=4744)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4741,
        flag_1=4742,
        flag_2=1043339207,
        flag_3=4741,
        first_flag=4740,
        last_flag=4744,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4741, flag_1=4740, flag_2=1043339207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1043332706, flag_1=1043332707)
    CommonFunc_90005727(0, 4741, 1038410730, 1038400730, 4740, 4743)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038410700)
    DisableBackread(Characters.Hyetta)
    DisableBackread(1038410720)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1038413700)
def Event_1038413700(_, character: uint):
    """Event 1038413700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3380):
        DisableFlag(1038419202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L8, flag=3388)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3388))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3388))
    
    Restart()


@RestartOnRest(1038413710)
def Event_1038413710(_, character: uint):
    """Event 1038413710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3687)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3687))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    OR_4.Add(FlagEnabled(3687))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1038413711)
def Event_1038413711(_, character: uint, flag: uint, flag_1: uint):
    """Event 1038413711"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    if AND_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3681))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    End()


@RestartOnRest(1038413712)
def Event_1038413712():
    """Event 1038413712"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(31009206):
        return
    if FlagEnabled(1038419254):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    if AND_1:
        return
    EnableFlag(1038419254)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()
