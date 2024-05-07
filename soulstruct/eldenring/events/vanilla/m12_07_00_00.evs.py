"""
Siofra River (Start)

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
from .enums.m12_07_00_00_enums import *
from .enums.m60_45_37_00_enums import Assets as m60_45_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=71270, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=71271, asset=Assets.AEG099_060_9001)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)
    CommonFunc_90005501(
        0,
        flag=12070525,
        flag_1=12071525,
        left=4,
        asset=Assets.AEG239_010_0502,
        asset_1=m60_45_Assets.AEG239_020_2000,
        asset_2=Assets.AEG239_021_0500,
        flag_2=12070527,
    )
    CommonFunc_90005501(
        0,
        flag=12070515,
        flag_1=12071515,
        left=7,
        asset=Assets.AEG239_010_0500,
        asset_1=Assets.AEG239_020_0501,
        asset_2=Assets.AEG239_020_0500,
        flag_2=12070516,
    )
    Event_12070510()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12070700)
    DisableBackread(12070701)
    Event_12070519()
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman0, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman1, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman2, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman3, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman4, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman5, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Clayman6, region=12072250, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Clayman7,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=1.7999999523162842,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Clayman8,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=0.5,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Clayman9,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Clayman10,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=1.2000000476837158,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Clayman11,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=1.399999976158142,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Clayman12,
        animation_id=30001,
        animation_id_1=20001,
        region=12072271,
        radius=2.0,
        seconds=0.30000001192092896,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear0,
        animation_id=30001,
        animation_id_1=20001,
        region=12072300,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear1,
        animation_id=30001,
        animation_id_1=20001,
        region=12072300,
        radius=10.0,
        seconds=0.5,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear2,
        animation_id=30001,
        animation_id_1=20001,
        region=12072310,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear3,
        animation_id=30001,
        animation_id_1=20001,
        region=12072310,
        radius=10.0,
        seconds=0.30000001192092896,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear4,
        animation_id=30001,
        animation_id_1=20001,
        region=12072310,
        radius=10.0,
        seconds=0.8999999761581421,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear5,
        animation_id=30001,
        animation_id_1=20001,
        region=12072310,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.SilverTear6, region=12072300, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear7,
        animation_id=30001,
        animation_id_1=20001,
        region=12072320,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SilverTear8,
        animation_id=30001,
        animation_id_1=20001,
        region=12072320,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005200(
        0,
        character=12070340,
        animation_id=30000,
        animation_id_1=20000,
        region=12072340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=12070341,
        animation_id=30000,
        animation_id_1=20000,
        region=12072340,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=12070342,
        animation_id=30000,
        animation_id_1=20000,
        region=12072340,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=12070343,
        animation_id=30000,
        animation_id_1=20000,
        region=12072340,
        seconds=4.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=12070345, radius=5.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear9,
        animation_id=30000,
        animation_id_1=20000,
        region=12072355,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear10,
        animation_id=30000,
        animation_id_1=20000,
        region=12072355,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear11,
        animation_id=30000,
        animation_id_1=20000,
        region=12072355,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=12070358,
        animation_id=30000,
        animation_id_1=20000,
        region=12072355,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=12070380, radius=60.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=12070385,
        animation_id=30000,
        animation_id_1=20000,
        region=12072340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Dummy, region=12072382, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=12070402, character=Characters.Scarab1, item_lot=40652, seconds=1.5, item_is_dropped=0)
    Event_12073700(0, character=12070700, character_1=12070701)


@ContinueOnRest(12070510)
def Event_12070510():
    """Event 12070510"""
    CommonFunc_90005500(
        0,
        flag=12070525,
        flag_1=12070526,
        left=4,
        asset=Assets.AEG239_010_0502,
        asset_1=m60_45_Assets.AEG239_020_2000,
        obj_act_id=1045373526,
        asset_2=Assets.AEG239_021_0500,
        obj_act_id_1=12073527,
        region=1045372526,
        region_1=12072527,
        flag_2=12070527,
        flag_3=12070528,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=12070515,
        flag_1=12071515,
        left=7,
        asset=Assets.AEG239_010_0500,
        asset_1=Assets.AEG239_020_0501,
        obj_act_id=12073516,
        asset_2=Assets.AEG239_020_0500,
        obj_act_id_1=12073517,
        region=12072516,
        region_1=12072517,
        flag_2=12070516,
        flag_3=12072517,
        left_1=0,
    )


@ContinueOnRest(12070519)
def Event_12070519():
    """Event 12070519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(12070525)
    DisableFlag(12070515)


@RestartOnRest(12073700)
def Event_12073700(_, character: uint, character_1: uint):
    """Event 12073700"""
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@RestartOnRest(12073701)
def Event_12073701():
    """Event 12073701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3503):
        return
    AND_1.Add(FlagEnabled(3506))
    AND_1.Add(FlagDisabled(12079006))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12072700))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12079005)
    End()


@RestartOnRest(12073702)
def Event_12073702():
    """Event 12073702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3503):
        return
    AND_1.Add(FlagEnabled(3506))
    AND_1.Add(FlagDisabled(12079008))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12072701))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12079007)
    End()
