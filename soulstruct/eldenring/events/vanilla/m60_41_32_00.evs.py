"""
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
from .entities.m60_41_32_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1041320000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005724(
        0,
        flag=1041320290,
        character=1041320290,
        item_lot_param_id=70000,
        seconds=0.0,
        left=1,
        character_1=1041325291,
    )
    CommonFunc_90005722(0, character=1041320290, character_1=1041320291)
    CommonFunc_90005720(0, character=1041320290, character_1=1041320292, special_effect=10961, model_point=181)
    CommonFunc_90005720(0, character=1041320290, character_1=1041320293, special_effect=10961, model_point=182)
    CommonFunc_90005721(0, character=1041320290, character_1=1041320292)
    CommonFunc_90005721(0, character=1041320290, character_1=1041320293)
    CommonFunc_90005723(0, character=1041320290)
    CommonFunc_90005920(0, flag=1041320900, asset=1041321900, obj_act_id=1041323900)
    CommonFunc_90005261(0, character=1041329200, region=1041322200, radius=5.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(0, character=1041329201, region=1041322200, radius=5.0, seconds=2.0, animation_id=1701)
    CommonFunc_90005261(0, character=1041329202, region=1041322200, radius=5.0, seconds=1.0, animation_id=1702)
    CommonFunc_90005261(0, character=1041329203, region=1041322200, radius=5.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(0, character=1041329204, region=1041322200, radius=5.0, seconds=2.0, animation_id=1702)
    CommonFunc_90005261(0, character=1041329205, region=1041322200, radius=5.0, seconds=1.0, animation_id=1702)
    CommonFunc_90005261(0, character=1041329206, region=1041322200, radius=5.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005725(
        0,
        flag=4745,
        flag_1=4746,
        flag_2=4748,
        flag_3=1041329205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1041326700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4746,
        flag_1=4747,
        flag_2=1041329206,
        flag_3=4746,
        first_flag=4745,
        last_flag=4749,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4746, flag_1=4745, flag_2=1041329206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4748, first_flag=4745, last_flag=4749)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4746,
        flag_1=4747,
        flag_2=1041329207,
        flag_3=4746,
        first_flag=4745,
        last_flag=4749,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4746, flag_1=4745, flag_2=1041329207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1041322706, flag_1=1041322707)
    CommonFunc_90005727(0, 4746, 1041320700, 1041320701, 4745, 4748)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1041320300)
def Event_1041320300():
    """Event 1041320300"""
    DropMandatoryTreasure(1041320360)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(1041320321))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1041322350))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1041322320)


@RestartOnRest(1041320301)
def Event_1041320301():
    """Event 1041320301"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1041322320))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1041322350))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(1041320350)
    DisableAnimations(1041320350)
    EnableFlag(1041320321)
    DisableFlag(1041322320)
