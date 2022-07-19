"""
Southeast Liurnia (SE) (SE)

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
from .entities.m60_39_40_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039400000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76200,
        asset=Assets.AEG099_090_9000,
        source_flag=77200,
        value=0,
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
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9001, vfx_id=100, model_point=800, right=0)
    Event_1039400700(0, character=Characters.Hyetta)
    CommonFunc_90005702(0, character=Characters.Hyetta, flag=3383, first_flag=3380, last_flag=3383)
    CommonFunc_90005703(
        0,
        character=Characters.Hyetta,
        flag=3381,
        flag_1=3382,
        flag_2=1039409201,
        flag_3=3381,
        first_flag=3380,
        last_flag=3383,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Hyetta, flag=3381, flag_1=3380, flag_2=1039409201, right=3)
    Event_1039400701()
    CommonFunc_90005703(
        0,
        character=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3942,
        flag_2=1039409251,
        flag_3=3941,
        first_flag=3940,
        last_flag=3943,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3940,
        flag_2=1039409251,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_1039403710(0, character=Characters.DemiHumanShaman)
    Event_1039403711(0, 1039400710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Hyetta)
    DisableBackread(Characters.DemiHumanShaman)
    CommonFunc_90005261(0, 1039400210, 1039402210, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1039400211, 1039402211, 5.0, 0.5, -1)
    CommonFunc_90005261(0, 1039400212, 1039402211, 5.0, 1.0, -1)
    CommonFunc_90005261(0, 1039400213, 1039402211, 5.0, 0.0, -1)
    CommonFunc_90005211(0, 1039400220, 30001, 20001, 1039402220, 0.0, 0.0, 0, 0, 0, 0)


@RestartOnRest(1039400700)
def Event_1039400700(_, character: uint):
    """Event 1039400700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3380):
        DisableFlag(1039409202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3387)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3387))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
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
    
    MAIN.Await(FlagDisabled(3387))
    
    Restart()


@RestartOnRest(1039400701)
def Event_1039400701():
    """Event 1039400701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045349259):
        return
    
    MAIN.Await(FlagEnabled(1039409206))
    
    EnableFlag(3418)


@RestartOnRest(1039403710)
def Event_1039403710(_, character: uint):
    """Event 1039403710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DisableFlag(1039409250)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(3940))
    AND_1.Add(FlagEnabled(1043379353))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    AND_5.Add(FlagEnabled(3947))
    AND_5.Add(FlagDisabled(1036489213))
    AND_5.Add(FlagDisabled(1039519209))
    AND_5.Add(FlagDisabled(11109819))
    AND_5.Add(FlagDisabled(3955))
    AND_5.Add(FlagDisabled(3956))
    AND_5.Add(FlagDisabled(3957))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_6.Add(FlagEnabled(3947))
    AND_6.Add(FlagDisabled(1036489213))
    AND_6.Add(FlagDisabled(1039519209))
    AND_6.Add(FlagDisabled(11109819))
    AND_6.Add(FlagDisabled(3955))
    AND_6.Add(FlagDisabled(3956))
    AND_6.Add(FlagDisabled(3957))
    
    MAIN.Await(AND_6)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3954)
    SkipLinesIfFlagEnabled(3, 1039409264)
    AND_6.Add(FlagEnabled(76200))
    AND_6.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    EnableNetworkFlag(1039409264)
    EnableNetworkFlag(3954)
    Goto(Label.L20)

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
    AND_15.Add(FlagEnabled(3947))
    AND_15.Add(FlagDisabled(1036489213))
    AND_15.Add(FlagDisabled(1039519209))
    AND_15.Add(FlagDisabled(11109819))
    AND_15.Add(FlagDisabled(3955))
    AND_15.Add(FlagDisabled(3956))
    AND_15.Add(FlagDisabled(3957))
    
    MAIN.Await(not AND_15)
    
    Restart()


@RestartOnRest(1039403711)
def Event_1039403711(_, entity: uint):
    """Event 1039403711"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(3943))
    OR_1.Add(FlagDisabled(3947))
    OR_1.Add(FlagEnabled(1039409259))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=20000, radius=4.0))
    AND_1.Add(CharacterHasSpecialEffect(20000, 9690))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()
