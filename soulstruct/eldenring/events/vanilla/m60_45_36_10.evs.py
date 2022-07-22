"""
East Limgrave (Meteor) (SW) (SE)

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
from .entities.m60_45_36_10_entities import *
from .entities.m60_45_36_00_entities import Characters as m60_45_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1045360000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005460(0, character=m60_45_Characters.GiantOctopus)
    CommonFunc_90005461(0, character=m60_45_Characters.GiantOctopus)
    CommonFunc_90005462(0, character=m60_45_Characters.GiantOctopus)
    CommonFunc_90005463(0, character=1045362212, character_1=m60_45_Characters.GiantOctopus)
    CommonFunc_90005464(
        0,
        flag=1045362212,
        character=m60_45_Characters.GiantOctopus,
        character_1=m60_45_Characters.Octopus0,
        value=0,
    )
    CommonFunc_90005464(
        0,
        flag=1045362212,
        character=m60_45_Characters.GiantOctopus,
        character_1=m60_45_Characters.Octopus1,
        value=1,
    )
    CommonFunc_90005464(
        0,
        flag=1045362212,
        character=m60_45_Characters.GiantOctopus,
        character_1=m60_45_Characters.Octopus2,
        value=2,
    )
    CommonFunc_90005464(
        0,
        flag=1045362212,
        character=m60_45_Characters.GiantOctopus,
        character_1=m60_45_Characters.Octopus3,
        value=3,
    )
    CommonFunc_90005464(
        0,
        flag=1045362212,
        character=m60_45_Characters.GiantOctopus,
        character_1=m60_45_Characters.Octopus4,
        value=4,
    )
    Event_1045362200()
    Event_1045362400()
    CommonFunc_90005725(
        0,
        flag=4725,
        flag_1=4726,
        flag_2=4728,
        flag_3=1045369305,
        character=m60_45_Characters.Merchant,
        character_1=m60_45_Characters.NomadMule,
        asset=1045366700,
    )
    CommonFunc_90005703(
        0,
        character=m60_45_Characters.Merchant,
        flag=4726,
        flag_1=4727,
        flag_2=1045369306,
        flag_3=4726,
        first_flag=4725,
        last_flag=4729,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=m60_45_Characters.Merchant,
        flag=4726,
        flag_1=4725,
        flag_2=1045369306,
        right=3,
    )
    CommonFunc_90005702(0, character=m60_45_Characters.Merchant, flag=4728, first_flag=4725, last_flag=4729)
    CommonFunc_90005703(
        0,
        character=m60_45_Characters.NomadMule,
        flag=4726,
        flag_1=4727,
        flag_2=1045369307,
        flag_3=4726,
        first_flag=4725,
        last_flag=4729,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=m60_45_Characters.NomadMule,
        flag=4726,
        flag_1=4725,
        flag_2=1045369307,
        right=3,
    )
    CommonFunc_90005728(0, attacked_entity=m60_45_Characters.NomadMule, flag=1045362706, flag_1=1045362707)
    CommonFunc_90005727(
        0,
        flag=4726,
        character=m60_45_Characters.Merchant,
        character_1=m60_45_Characters.NomadMule,
        first_flag=4725,
        last_flag=4728,
    )
    CommonFunc_90005729(0, flag=1045369300, character=m60_45_Characters.Merchant, distance=40.0, flag_1=1045362702)
    CommonFunc_90005725(
        0,
        flag=4725,
        flag_1=4726,
        flag_2=4728,
        flag_3=1045369305,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1045366701,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4726,
        flag_1=4727,
        flag_2=1045369306,
        flag_3=4726,
        first_flag=4725,
        last_flag=4729,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4726, flag_1=4725, flag_2=1045369306, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4728, first_flag=4725, last_flag=4729)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4726,
        flag_1=4727,
        flag_2=1045369307,
        flag_3=4726,
        first_flag=4725,
        last_flag=4729,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4726, flag_1=4725, flag_2=1045369307, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1045362706, flag_1=1045362707)
    CommonFunc_90005727(
        0,
        flag=4726,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4725,
        last_flag=4728,
    )
    CommonFunc_90005729(0, flag=1045369300, character=Characters.Merchant, distance=40.0, flag_1=1045362702)
    CommonFunc_90005706(0, character=m60_45_Characters.WanderingNoble, animation_id=930023, left=0)
    Event_1045363704()
    CommonFunc_90005706(0, character=m60_45_Characters.WanderingNoble, animation_id=30023, left=0)
    Event_1045363715()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(m60_45_Characters.Merchant)
    DisableBackread(m60_45_Characters.NomadMule)
    DisableBackread(m60_45_Characters.WanderingNoble)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1045362200)
def Event_1045362200():
    """Event 1045362200"""
    AddSpecialEffect(m60_45_Characters.GiantOctopus, 11771)


@RestartOnRest(1045362400)
def Event_1045362400():
    """Event 1045362400"""
    if FlagEnabled(1045360500):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(310))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1045362400))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1045360500)


@RestartOnRest(1045363700)
def Event_1045363700(_, character: uint, character_1: uint, character_2: uint, asset: uint):
    """Event 1045363700"""
    WaitFrames(frames=1)
    DisableFlag(1045369200)
    GotoIfPlayerNotInOwnWorld(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1045369221))
    GotoIfConditionFalse(Label.L20, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L1, flag=4740)
    GotoIfFlagEnabled(Label.L2, flag=4741)
    GotoIfFlagEnabled(Label.L4, flag=4743)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    SkipLinesIfFlagRangeAllDisabled(1, (4982, 4983))
    ForceAnimation(character, 30002)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    SkipLinesIfFlagRangeAllDisabled(2, (4982, 4983))
    ForceAnimation(character, 30002)
    DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L20, flag=1045369222)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1045369200))
    
    Restart()


@ContinueOnRest(1045363702)
def Event_1045363702(_, character: uint):
    """Event 1045363702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4743):
        return
    if FlagDisabled(1045369221):
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableNetworkFlag(1045369222)
    End()


@ContinueOnRest(1045363703)
def Event_1045363703(_, character: uint):
    """Event 1045363703"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    OR_2.Add(FlagEnabled(4740))
    OR_2.Add(FlagEnabled(4741))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(CharacterHasSpecialEffect(character, 9601))
    OR_5.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_5)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(EntityWithinDistance(entity=20000, other_entity=character, radius=4.0))
    OR_6.Add(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    MAIN.Await(OR_6)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_7.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=6.0))
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_7)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20010)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_10.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_10)
    
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    OR_11.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=6.0))
    OR_11.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_11)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=9603)
    ForceAnimation(character, 20011)
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1045363704)
def Event_1045363704():
    """Event 1045363704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045369229):
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=m60_45_Characters.Merchant, radius=7.5))
    
    EnableNetworkFlag(1045369229)
    End()


@RestartOnRest(1045363705)
def Event_1045363705(_, character: uint):
    """Event 1045363705"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    OR_2.Add(FlagEnabled(4740))
    OR_2.Add(FlagEnabled(4741))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9602))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9602))
    
    Restart()


@RestartOnRest(1045363706)
def Event_1045363706(_, character: uint, attacked_entity: uint):
    """Event 1045363706"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=40000))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1041362709))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1041362708)
    if FlagEnabled(4741):
        return
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9602)
    ForceAnimation(character, 20006)


@ContinueOnRest(1045363707)
def Event_1045363707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1045363707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(first_flag):
        return
    DisableNetworkFlag(flag_2)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    AND_1.Add(HealthValue(character) < 1)
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_3.Add(FlagEnabled(flag_2))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=20000))
    AND_3.Add(HealthValue(character_1) < 1)
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    OR_5.Add(OR_2)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1045363710)
def Event_1045363710(_, character: uint):
    """Event 1045363710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023)


@RestartOnRest(1045363715)
def Event_1045363715():
    """Event 1045363715"""
    DisableFlag(1044399265)
    if FlagDisabled(4728):
        EnableFlag(1044399265)
    End()
