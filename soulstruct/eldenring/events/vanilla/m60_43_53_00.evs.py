"""
North Altus Plateau (SE) (NE)

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
from .entities.m60_43_53_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76311, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=76312, asset=Assets.AEG099_060_9002)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76312,
        asset=Assets.AEG099_060_9003,
        source_flag=77300,
        value=4,
        flag_2=78300,
        flag_3=78301,
        flag_4=78302,
        flag_5=78303,
        flag_6=78304,
        flag_7=78305,
        flag_8=78306,
        flag_9=78307,
        flag_10=78308,
        flag_11=78309,
    )
    CommonFunc_90005300(0, flag=1043530500, character=Characters.Scarab, item_lot_param_id=40318, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30005,
        animation_id_1=20021,
        region=1043532350,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30005,
        animation_id_1=20021,
        region=1043532350,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellSoldier,
        animation_id=30000,
        animation_id_1=20000,
        region=1043532350,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=Characters.BellBearingHunter, name=903100602, npc_threat_level=10)
    CommonFunc_90005860(
        0,
        flag=1043530800,
        left=0,
        character=Characters.BellBearingHunter,
        left_1=0,
        item_lot__item_lot_param_id=1043530400,
        seconds=0.0,
    )
    CommonFunc_90005760(
        0,
        flag=1043530800,
        character=Characters.BellBearingHunter,
        region=1043532400,
        flag_1=1043532708,
    )
    CommonFunc_90005872(0, character=Characters.BellBearingHunter, npc_threat_level=10, right=0)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4763, first_flag=4760, last_flag=4763)
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4761,
        flag_1=4762,
        flag_2=1043530702,
        flag_3=4761,
        first_flag=4760,
        last_flag=4763,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4761, flag_1=4760, flag_2=1043530702, right=3)
    Event_1043530700(0, character=Characters.Merchant, character_1=Characters.NomadMule, asset=1043536700)
    CommonFunc_90005770(0, flag=1043530701)
    CommonFunc_90005727(
        0,
        flag=4761,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4760,
        last_flag=4763,
    )
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1043532706, flag_1=1043532707)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4761,
        flag_1=4762,
        flag_2=1043530702,
        flag_3=4761,
        first_flag=4760,
        last_flag=4763,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4761, flag_1=4760, flag_2=1043530702, right=3)
    CommonFunc_90005771(0, 1043530951, 1043532710)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton0,
        animation_id=30016,
        animation_id_1=20016,
        region=1043532203,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton1,
        animation_id=30016,
        animation_id_1=20016,
        region=1043532203,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton2,
        animation_id=30016,
        animation_id_1=20016,
        region=1043532204,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton3,
        animation_id=30014,
        animation_id_1=20014,
        region=1043532206,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton4,
        animation_id=30014,
        animation_id_1=20014,
        region=1043532206,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton5,
        animation_id=30014,
        animation_id_1=20014,
        region=1043532208,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1043530218,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1043530219,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton12,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1043530222,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton13,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton14,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton6,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton7,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton8,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton10,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton11,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1043530216,
        animation_id=30014,
        animation_id_1=20014,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton15,
        animation_id=30014,
        animation_id_1=20014,
        region=1043532230,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1043530212, 30016, 20016, 1043532212, 0.0, 0, 0, 0, 0)


@RestartOnRest(1043530700)
def Event_1043530700(_, character: uint, character_1: uint, asset: uint):
    """Event 1043530700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4760):
        DisableFlag(1043539205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=1043532709)
    DisableNetworkFlag(1043532708)
    OR_1.Add(FlagEnabled(1043530701))
    OR_1.Add(FlagEnabled(4761))
    OR_1.Add(FlagEnabled(4763))
    AND_1.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    AND_1.Add(FlagDisabled(1043530800))
    AND_1.Add(OR_1)
    GotoIfConditionFalse(Label.L4, input_condition=AND_1)
    EnableNetworkFlag(1043532708)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(1043532709)
    GotoIfFlagEnabled(Label.L0, flag=4760)
    GotoIfFlagEnabled(Label.L1, flag=4761)
    GotoIfFlagEnabled(Label.L3, flag=4763)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1043532708):
        DisableCharacter(character)
        DisableBackread(character)
        DisableCharacter(character_1)
        DisableBackread(character_1)
        DisableAsset(asset)
        Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930003)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1043532708):
        DisableCharacter(character)
        DisableBackread(character)
        DisableCharacter(character_1)
        DisableBackread(character_1)
        DisableAsset(asset)
        Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()
