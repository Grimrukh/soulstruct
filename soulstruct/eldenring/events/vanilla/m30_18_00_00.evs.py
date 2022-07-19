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
from .entities.m30_18_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301800, asset=Assets.AEG099_060_9000)
    CommonFunc_90005525(0, flag=30180570, asset=Assets.AEG027_157_1000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005616(0, flag=30187900, region=30182700)
    CommonFunc_90005200(
        0,
        character=Characters.Imp0,
        animation_id=30000,
        animation_id_1=20000,
        region=30182201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=30180201, region=30182207, seconds=0.0, animation_id=3004)
    CommonFunc_90005250(0, character=Characters.Imp1, region=30182205, seconds=0.0, animation_id=3004)
    CommonFunc_90005200(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30182220,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180228,
        animation_id=30000,
        animation_id_1=20000,
        region=30182206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp3,
        animation_id=30010,
        animation_id_1=20010,
        region=30182209,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180210,
        animation_id=30010,
        animation_id_1=20010,
        region=30182209,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp5,
        animation_id=30003,
        animation_id_1=20003,
        region=30182211,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30180207, 30182218, 0.0, -1)
    CommonFunc_90005250(0, 30180208, 30182300, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=30180213,
        animation_id=30002,
        animation_id_1=20002,
        region=30182212,
        seconds=3.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180214,
        animation_id=30002,
        animation_id_1=20002,
        region=30182212,
        seconds=3.700000047683716,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180215,
        animation_id=30002,
        animation_id_1=20002,
        region=30182212,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180234,
        animation_id=30002,
        animation_id_1=20002,
        region=30182212,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30180203, 30182300, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.Imp12, region=30182221, seconds=0.0, animation_id=3004)
    CommonFunc_90005250(0, character=Characters.Imp13, region=30182221, seconds=1.0, animation_id=3004)
    CommonFunc_90005200(
        0,
        character=30180217,
        animation_id=30001,
        animation_id_1=20001,
        region=30182217,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp8, region=30182227, seconds=0.0, animation_id=3004)
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeBurialWatchdog0,
        animation_id=30000,
        animation_id_1=20000,
        region=30182353,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        region=30182352,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180300,
        animation_id=30000,
        animation_id_1=20000,
        region=30182300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180301,
        animation_id=30000,
        animation_id_1=20000,
        region=30182300,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180302,
        animation_id=30000,
        animation_id_1=20000,
        region=30182300,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot4,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot10,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot7,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30180354,
        animation_id=30000,
        animation_id_1=20000,
        region=30182250,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallLivingPot7, region=30182250, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=Characters.SmallLivingPot8, region=30182250, seconds=2.0, animation_id=3003)
    CommonFunc_90005250(0, character=Characters.LivingPot4, region=30182250, seconds=0.0, animation_id=3004)
    CommonFunc_90005250(0, character=30180327, region=30182250, seconds=2.5, animation_id=3003)
    CommonFunc_90005250(0, character=30180328, region=30182250, seconds=3.0, animation_id=3003)
    CommonFunc_90005260(0, 30180324, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005260(0, 30180325, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005260(0, 30180326, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005260(0, 30180327, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005260(0, 30180328, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005260(0, 30180354, 30182301, 5.0, 0.0, -1)
    CommonFunc_90005250(0, 30180305, 30182305, 0.0, -1)
    CommonFunc_90005250(0, 30180306, 30182305, 1.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot16,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot21,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot17,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30180337,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot18,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot19,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30180340,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(
        0,
        character=Characters.SmallLivingPot0,
        region=30182251,
        seconds=0.699999988079071,
        animation_id=3010,
    )
    CommonFunc_90005250(0, character=Characters.SmallLivingPot1, region=30182251, seconds=0.5, animation_id=3011)
    CommonFunc_90005250(0, character=30180341, region=30182341, seconds=0.0, animation_id=3011)
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot9,
        animation_id=30000,
        animation_id_1=20000,
        region=30182310,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30180355, 30182212, 0.0, -1)
    CommonFunc_90005250(0, 30180342, 30182229, 0.0, -1)
    CommonFunc_90005250(0, 30180343, 30182229, 0.0, -1)
    Event_30182218(0, character=Characters.Imp6, animation_id=30010)
    Event_30182218(1, character=Characters.Imp7, animation_id=30010)
    Event_30182218(2, character=Characters.Imp9, animation_id=30001)
    Event_30182219(0, character=Characters.Imp6, animation_id=20010)
    Event_30182219(1, character=Characters.Imp7, animation_id=20010)
    Event_30182219(2, character=Characters.Imp9, animation_id=20001)
    Event_30182220(0, character=Characters.Imp6, seconds=0.0, animation_id=0)
    Event_30182220(1, character=Characters.Imp7, seconds=0.0, animation_id=0)
    Event_30182220(2, character=Characters.Imp9, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=30180230, region=30182230, seconds=0.0, animation_id=3004)
    CommonFunc_90005200(
        1,
        character=30180216,
        animation_id=30001,
        animation_id_1=20001,
        region=30182216,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot11,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot12,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallLivingPot20, region=30182333, seconds=0.0, animation_id=3011)
    CommonFunc_90005250(0, character=Characters.SmallLivingPot15, region=30182333, seconds=0.5, animation_id=3011)
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot14,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30180317, 30172317, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=30180319,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30180320,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot0,
        animation_id=30000,
        animation_id_1=20000,
        region=30182350,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30180351, 30182254, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        region=30182351,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30182350(0, character=Characters.LivingPot0)
    Event_30182350(1, character=Characters.LivingPot1)
    Event_30182350(2, character=Characters.LivingPot3)
    Event_30182350(3, character=Characters.ErdtreeBurialWatchdog0)
    Event_30182350(4, character=30180354)
    CommonFunc_90005250(0, character=30180251, region=30182251, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=30180254, region=30182254, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=30180344, region=30182344, radius=10.0, seconds=0.5, animation_id=3011)
    CommonFunc_90005261(0, character=30180345, region=30182344, radius=10.0, seconds=1.0, animation_id=3011)
    CommonFunc_90005261(
        0,
        character=30180346,
        region=30182344,
        radius=10.0,
        seconds=1.2999999523162842,
        animation_id=3011,
    )
    CommonFunc_90005261(0, 30180347, 30182254, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 30180348, 30182344, 1.0, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.ErdtreeBurialWatchdog1, region=30182257, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, 30180255, 30182255, 0.0, -1)
    CommonFunc_90005250(0, 30180256, 30182255, 0.0, -1)
    CommonFunc_90005250(0, character=30180400, region=30182401, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.FungalPod1, region=30182401, seconds=0.5, animation_id=3001)
    CommonFunc_90005250(
        0,
        character=Characters.FungalPod2,
        region=30182401,
        seconds=0.800000011920929,
        animation_id=3001,
    )
    CommonFunc_90005250(0, character=Characters.FungalPod3, region=30182401, seconds=1.5, animation_id=3001)
    CommonFunc_90005250(0, character=30180404, region=30182401, seconds=2.0, animation_id=3001)
    CommonFunc_90005250(0, character=30180405, region=30182401, seconds=2.4000000953674316, animation_id=3001)
    CommonFunc_90005250(0, character=30180406, region=30182401, seconds=3.0, animation_id=3001)
    CommonFunc_90005250(
        0,
        character=Characters.FungalPod4,
        region=30182401,
        seconds=3.299999952316284,
        animation_id=3001,
    )
    CommonFunc_90005250(0, character=Characters.FungalPod5, region=30182401, seconds=4.0, animation_id=3001)
    CommonFunc_90005250(0, character=30180409, region=30182401, seconds=4.5, animation_id=3001)
    CommonFunc_90005250(0, character=30180410, region=30182411, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.FungalPod6, region=30182411, seconds=0.5, animation_id=3001)
    CommonFunc_90005250(
        0,
        character=Characters.FungalPod7,
        region=30182411,
        seconds=0.800000011920929,
        animation_id=3001,
    )
    CommonFunc_90005250(0, character=Characters.FungalPod8, region=30182411, seconds=1.5, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.FungalPod0, region=30182411, seconds=2.0, animation_id=3001)
    CommonFunc_90005250(0, character=30180415, region=30182411, seconds=2.799999952316284, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.GiantFungalPod, region=30182450, seconds=0.0, animation_id=3002)
    CommonFunc_90005650(
        0,
        flag=30180540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30183541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30180540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005501(
        0,
        flag=30180510,
        flag_1=30181511,
        left=0,
        asset=Assets.AEG027_054_0500,
        asset_1=Assets.AEG027_002_0503,
        asset_2=Assets.AEG027_002_0504,
        flag_2=30180512,
    )
    CommonFunc_90005501(
        0,
        flag=30180515,
        flag_1=30181515,
        left=0,
        asset=Assets.AEG027_036_0500,
        asset_1=Assets.AEG027_002_0501,
        asset_2=Assets.AEG027_002_0502,
        flag_2=30180516,
    )
    CommonFunc_90005501(
        0,
        flag=30180520,
        flag_1=30181520,
        left=2,
        asset=Assets.AEG027_036_0501,
        asset_1=Assets.AEG027_002_0506,
        asset_2=Assets.AEG027_002_0507,
        flag_2=30180521,
    )
    CommonFunc_90005501(
        0,
        flag=30180510,
        flag_1=30181511,
        left=0,
        asset=Assets.AEG027_054_0500,
        asset_1=Assets.AEG027_002_0504,
        asset_2=Assets.AEG027_002_0505,
        flag_2=30180512,
    )
    Event_30182510()
    CommonFunc_90005680(
        0,
        flag=30180505,
        flag_1=30180506,
        flag_2=30180507,
        flag_3=30180508,
        asset=Assets.AEG027_156_0500,
    )
    CommonFunc_90005681(
        0,
        flag=30180505,
        flag_1=30180506,
        flag_2=30180507,
        flag_3=30180508,
        attacked_entity=Assets.AEG027_156_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30180505,
        flag_1=30180506,
        flag_2=30180507,
        flag_3=30180508,
        asset=Assets.AEG027_156_0500,
    )
    Event_30182500()
    CommonFunc_90005680(
        0,
        flag=30180500,
        flag_1=30180501,
        flag_2=30180502,
        flag_3=30180503,
        asset=Assets.AEG027_156_0501,
    )
    CommonFunc_90005681(
        0,
        flag=30180500,
        flag_1=30180501,
        flag_2=30180502,
        flag_3=30180503,
        attacked_entity=Assets.AEG027_156_0501,
    )
    CommonFunc_90005680(
        0,
        flag=30180500,
        flag_1=30180501,
        flag_2=30180502,
        flag_3=30180503,
        asset=Assets.AEG027_156_0501,
    )
    Event_30180050()
    CommonFunc_90005540(0, 30180530, 30181530, 30181531, 30183531, -1, 1, 2)
    Event_30182800()
    Event_30182810()
    Event_30182849()
    Event_30182811()
    CommonFunc_90005646(
        0,
        flag=30180800,
        left_flag=30182840,
        cancel_flag__right_flag=30182841,
        asset=Assets.AEG099_065_9000,
        player_start=30182840,
        area_id=30,
        block_id=18,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, 30182800, 30181695, 5)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30180519()


@NeverRestart(30180050)
def Event_30180050():
    """Event 30180050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30180505)
    EnableFlag(30180500)


@RestartOnRest(30182350)
def Event_30182350(_, character: uint):
    """Event 30182350"""
    AddSpecialEffect(character, 15211)
    End()


@RestartOnRest(30182218)
def Event_30182218(_, character: uint, animation_id: int):
    """Event 30182218"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30182222))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(30182219)
def Event_30182219(_, character: uint, animation_id: int):
    """Event 30182219"""
    if FlagEnabled(30182220):
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30182213))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(FlagEnabled(30182218))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(30182220)
    Wait(0.0)
    ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)
    End()


@RestartOnRest(30182220)
def Event_30182220(_, character: uint, seconds: float, animation_id: int):
    """Event 30182220"""
    if FlagEnabled(30182220):
        return
    DisableAI(character)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(30182220)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(30182227)
def Event_30182227():
    """Event 30182227"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(30180570))
    
    ForceAnimation(Characters.Imp8, 3004, loop=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@NeverRestart(30182500)
def Event_30182500():
    """Event 30182500"""
    CommonFunc_90005681(
        0,
        flag=30180500,
        flag_1=30180501,
        flag_2=30180502,
        flag_3=30180503,
        attacked_entity=Assets.AEG027_156_0501,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110070,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110060,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110050,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110040,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110030,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110020,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110010,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30180502,
            source_entity=Assets.AEG027_156_0501,
            region=30182500,
            owner_entity=Characters.Dummy1,
            behavior_id=801110000,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    CommonFunc_90005681(
        0,
        flag=30180505,
        flag_1=30180506,
        flag_2=30180507,
        flag_3=30180508,
        attacked_entity=Assets.AEG027_156_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110070,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110060,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110050,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110040,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110030,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110020,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110010,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30180507,
            source_entity=Assets.AEG027_156_0500,
            region=30182505,
            owner_entity=Characters.Dummy0,
            behavior_id=801110000,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=103,
            model_point_2=0,
            model_point_3=0,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010070,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010060,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010050,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010040,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010030,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy0,
        entity=Assets.AEG027_044_0500,
        region=30182600,
        behavior_id=801010020,
        source_entity=30182601,
        source_entity_1=30182602,
        source_entity_2=30182603,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy0,
            entity=Assets.AEG027_044_0500,
            region=30182600,
            behavior_id=801010010,
            source_entity=30182601,
            source_entity_1=30182602,
            source_entity_2=30182603,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy0,
            entity=Assets.AEG027_044_0500,
            region=30182600,
            behavior_id=801010000,
            source_entity=30182601,
            source_entity_1=30182602,
            source_entity_2=30182603,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010070,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010060,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010050,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010040,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010030,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy1,
        entity=Assets.AEG027_044_0501,
        region=30182605,
        behavior_id=801010020,
        source_entity=30182606,
        source_entity_1=30182607,
        source_entity_2=30182608,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy1,
            entity=Assets.AEG027_044_0501,
            region=30182605,
            behavior_id=801010010,
            source_entity=30182606,
            source_entity_1=30182607,
            source_entity_2=30182608,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy1,
            entity=Assets.AEG027_044_0501,
            region=30182605,
            behavior_id=801010000,
            source_entity=30182606,
            source_entity_1=30182607,
            source_entity_2=30182608,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010070,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010060,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010050,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010040,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010030,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0502,
        region=30182610,
        behavior_id=801010020,
        source_entity=30182611,
        source_entity_1=30182612,
        source_entity_2=30182613,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy2,
            entity=Assets.AEG027_044_0502,
            region=30182610,
            behavior_id=801010010,
            source_entity=30182611,
            source_entity_1=30182612,
            source_entity_2=30182613,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy2,
            entity=Assets.AEG027_044_0502,
            region=30182610,
            behavior_id=801010000,
            source_entity=30182611,
            source_entity_1=30182612,
            source_entity_2=30182613,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010070,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010060,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010050,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010040,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010030,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy3,
        entity=Assets.AEG027_044_0503,
        region=30182615,
        behavior_id=801010020,
        source_entity=30182616,
        source_entity_1=30182617,
        source_entity_2=30182618,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy3,
            entity=Assets.AEG027_044_0503,
            region=30182615,
            behavior_id=801010010,
            source_entity=30182616,
            source_entity_1=30182617,
            source_entity_2=30182618,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy3,
            entity=Assets.AEG027_044_0503,
            region=30182615,
            behavior_id=801010000,
            source_entity=30182616,
            source_entity_1=30182617,
            source_entity_2=30182618,
        )
    SkipLinesIfFlagDisabled(2, 57)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010070,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010060,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010050,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010040,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010030,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    CommonFunc_90005660(
        0,
        owner_entity=Characters.TalkDummy4,
        entity=Assets.AEG027_044_0504,
        region=30182620,
        behavior_id=801010020,
        source_entity=30182621,
        source_entity_1=30182622,
        source_entity_2=30182623,
    )
    SkipLines(4)
    if FlagEnabled(51):
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy4,
            entity=Assets.AEG027_044_0504,
            region=30182620,
            behavior_id=801010010,
            source_entity=30182621,
            source_entity_1=30182622,
            source_entity_2=30182623,
        )
    else:
        CommonFunc_90005660(
            0,
            owner_entity=Characters.TalkDummy4,
            entity=Assets.AEG027_044_0504,
            region=30182620,
            behavior_id=801010000,
            source_entity=30182621,
            source_entity_1=30182622,
            source_entity_2=30182623,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205070,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205060,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205050,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205040,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205030,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205020,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205010,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30182550,
            asset_flag=30183550,
            asset=Assets.AEG027_013_0500,
            region=30182550,
            behaviour_id=801205000,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205070,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205060,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205050,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205040,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205030,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205020,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205010,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30182552,
            asset_flag=30183552,
            asset=Assets.AEG027_013_0501,
            region=30182550,
            behaviour_id=801205000,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205070,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205060,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205050,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205040,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205030,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205020,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205010,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30182554,
            asset_flag=30183554,
            asset=Assets.AEG027_013_0502,
            region=30182550,
            behaviour_id=801205000,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205070,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205060,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205050,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205040,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205030,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205020,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205010,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30182560,
            asset_flag=30183560,
            asset=Assets.AEG027_013_0503,
            region=30182560,
            behaviour_id=801205000,
            seconds=4.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205070,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205060,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205050,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205040,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205030,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205020,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205010,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(
            0,
            flag=30182562,
            asset_flag=30183562,
            asset=Assets.AEG027_013_0504,
            region=30182560,
            behaviour_id=801205000,
            seconds=2.0,
            right=0,
        )
    if FlagEnabled(57):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205070,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205060,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205050,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205040,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205030,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205020,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005675(
            0,
            flag=30182564,
            asset_flag=30183564,
            asset=Assets.AEG027_013_0505,
            region=30182560,
            behaviour_id=801205010,
            seconds=0.0,
            right=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005675(0, 30182564, 30183564, 30181564, 30182560, 801205000, 0.0, 0)


@NeverRestart(30182510)
def Event_30182510():
    """Event 30182510"""
    CommonFunc_90005500(
        0,
        flag=30180510,
        flag_1=30181511,
        left=0,
        asset=Assets.AEG027_054_0500,
        asset_1=Assets.AEG027_002_0503,
        obj_act_id=30183511,
        asset_2=Assets.AEG027_002_0504,
        obj_act_id_1=30183512,
        region=30182511,
        region_1=30182512,
        flag_2=30180512,
        flag_3=30182512,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=30180515,
        flag_1=30181515,
        left=0,
        asset=Assets.AEG027_036_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=30183516,
        asset_2=Assets.AEG027_002_0502,
        obj_act_id_1=30183517,
        region=30182516,
        region_1=30182517,
        flag_2=30180516,
        flag_3=30182517,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=30180520,
        flag_1=30181520,
        left=2,
        asset=Assets.AEG027_036_0501,
        asset_1=Assets.AEG027_002_0506,
        obj_act_id=30183521,
        asset_2=Assets.AEG027_002_0507,
        obj_act_id_1=30183522,
        region=30182521,
        region_1=30182522,
        flag_2=30180521,
        flag_3=30182522,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        30180510,
        30181511,
        0,
        30181510,
        30181512,
        30183512,
        30181518,
        30183518,
        30182511,
        30182512,
        30180512,
        30182512,
        0,
    )


@NeverRestart(30180519)
def Event_30180519():
    """Event 30180519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30180510)
    EnableFlag(30180515)


@RestartOnRest(30182800)
def Event_30182800():
    """Event 30182800"""
    if FlagEnabled(30180800):
        return
    
    MAIN.Await(HealthValue(Characters.UlceratedTreeSpirit) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.UlceratedTreeSpirit, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.UlceratedTreeSpirit))
    
    KillBossAndDisplayBanner(character=Characters.UlceratedTreeSpirit, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG099_630_9001, obj_act_id=-1)
    EnableFlag(30180800)
    EnableFlag(9218)
    if PlayerInOwnWorld():
        EnableFlag(61218)


@RestartOnRest(30182810)
def Event_30182810():
    """Event 30182810"""
    GotoIfFlagDisabled(Label.L0, flag=30180800)
    DisableCharacter(Characters.UlceratedTreeSpirit)
    DisableAnimations(Characters.UlceratedTreeSpirit)
    Kill(Characters.UlceratedTreeSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.UlceratedTreeSpirit)
    DisableAssetActivation(Assets.AEG099_630_9001, obj_act_id=-1)
    DisableHealthBar(Characters.UlceratedTreeSpirit)
    GotoIfFlagEnabled(Label.L1, flag=30180801)
    ForceAnimation(Characters.UlceratedTreeSpirit, 30002, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30182800))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.UlceratedTreeSpirit, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.UlceratedTreeSpirit, 20002)
    EnableNetworkFlag(30180801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.UlceratedTreeSpirit, 30002, loop=True)
    AND_2.Add(FlagEnabled(30182805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30182800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.UlceratedTreeSpirit, 20002)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.UlceratedTreeSpirit)
    SetNetworkUpdateRate(Characters.UlceratedTreeSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(4.300000190734863)
    EnableBossHealthBar(Characters.UlceratedTreeSpirit, name=904640301)
    EnableNetworkFlag(30182803)


@RestartOnRest(30182811)
def Event_30182811():
    """Event 30182811"""
    if FlagEnabled(30180800):
        return
    AND_1.Add(HealthRatio(Characters.UlceratedTreeSpirit) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30182802)


@RestartOnRest(30182849)
def Event_30182849():
    """Event 30182849"""
    CommonFunc_9005800(
        0,
        flag=30180800,
        entity=Assets.AEG099_001_9000,
        region=30182800,
        flag_1=30182805,
        character=30185800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30180800,
        entity=Assets.AEG099_001_9000,
        region=30182800,
        flag_1=30182805,
        flag_2=30182806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30180800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30180800, 920600, 30182805, 30182806, 30182803, 30182802, 0, 0)
