"""
Northwest Mountaintops (SE) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_51_57_00_enums import *
from .enums.m60_50_57_00_enums import Characters as m60_50_57_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1051570000, asset=Assets.AEG099_060_9003)
    CommonFunc_90005100(
        0,
        flag=76524,
        flag_1=76521,
        asset=Assets.AEG099_090_9004,
        source_flag=77510,
        value=0,
        flag_2=78510,
        flag_3=78511,
        flag_4=78512,
        flag_5=78513,
        flag_6=78514,
        flag_7=78515,
        flag_8=78516,
        flag_9=78517,
        flag_10=78518,
        flag_11=78519,
    )
    RegisterGrace(grace_flag=1051570001, asset=Assets.AEG099_060_9002)
    CommonFunc_90005100(
        0,
        flag=76524,
        flag_1=76522,
        asset=Assets.AEG099_090_9005,
        source_flag=77510,
        value=1,
        flag_2=78510,
        flag_3=78511,
        flag_4=78512,
        flag_5=78513,
        flag_6=78514,
        flag_7=78515,
        flag_8=78516,
        flag_9=78517,
        flag_10=78518,
        flag_11=78519,
    )
    RegisterGrace(grace_flag=1051570002, asset=Assets.AEG099_060_9000)
    CommonFunc_9005810(
        0,
        flag=1051570800,
        grace_flag=1051570003,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    Event_1051572580()
    CommonFunc_90005511(
        0,
        flag=1051570560,
        asset=Assets.AEG030_933_2000,
        obj_act_id=1051573560,
        obj_act_id_1=30000,
        left=0,
    )
    CommonFunc_90005512(0, flag=1051570560, region=1051572560, region_1=1051572561)
    Event_1051572350()
    Event_1051572350(slot=1)
    Event_1051572510()
    CommonFunc_90005501(
        0,
        flag=1051570510,
        flag_1=1051570511,
        left=0,
        asset=Assets.AEG030_095_2000,
        asset_1=Assets.AEG030_183_2001,
        asset_2=Assets.AEG030_183_2000,
        flag_2=1051570512,
    )
    CommonFunc_90005502(0, flag=1051570514, asset=Assets.AEG030_183_2000, region=1051572511)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9008, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005632(0, flag=580030, asset=Assets.AEG099_387_2000, item_lot=80030)
    Event_1051572849()
    Event_1051572800()
    Event_1051572810()
    Event_1051572811()
    Event_1051572812()
    Event_1051572820(
        0,
        character=Characters.Commander,
        character_1=1051575801,
        special_effect=11130,
        animation_id=20015,
    )
    Event_1051572821(
        0,
        character=Characters.Commander,
        character_1=1051575801,
        special_effect=11136,
        animation_id=20016,
    )
    Event_1051572822(
        0,
        character=Characters.Commander,
        character_1=Characters.BanishedKnight5,
        character_2=Characters.BanishedKnight6,
        special_effect=11135,
    )
    Event_1051572828(0, region=1051572829)
    Event_1051572829(0, region=1051572829)
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard0,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572200,
        radius=5.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard1,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572201,
        radius=5.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570202,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572202,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard2,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572203,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard3,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard4,
        region=1051572205,
        radius=3.0,
        seconds=0.699999988079071,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard5,
        region=1051572206,
        radius=3.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard6,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572207,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard7,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572208,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570210,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570211,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572211,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570212,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572212,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570213,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard9,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572214,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570216,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard10,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572214,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570218,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570219,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570220,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CastleGuard11,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572200,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570222,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570223,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570224,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570225,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570226,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570227,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570228,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570229,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout0,
        animation_id=30002,
        animation_id_1=20011,
        region=1051572240,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout1,
        animation_id=30002,
        animation_id_1=20011,
        region=1051572241,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.AlbinauricLookout2,
        region=1051572242,
        radius=0.5,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.AlbinauricLookout3,
        region=1051572242,
        radius=0.5,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.AlbinauricLookout4,
        region=1051572242,
        radius=0.5,
        seconds=0.0,
        animation_id=0,
    )
    Event_1051572250(
        0,
        character=Characters.BanishedKnight2,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        seconds=1.0,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.AlbinauricLookout0,
    )
    Event_1051572250(
        5,
        character=1051570215,
        animation_id=30001,
        animation_id_1=20001,
        region=0,
        seconds=2.5,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.AlbinauricLookout1,
    )
    Event_1051572250(
        6,
        character=Characters.CastleGuard8,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        seconds=5.0,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.AlbinauricLookout1,
    )
    Event_1051572250(
        7,
        character=Characters.CastleGuard12,
        animation_id=30001,
        animation_id_1=20001,
        region=0,
        seconds=2.5,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.AlbinauricLookout1,
    )
    Event_1051572250(
        8,
        character=Characters.CastleGuard13,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        seconds=4.5,
        seconds_1=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.AlbinauricLookout1,
    )
    CommonFunc_90005211(
        0,
        character=1051570251,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572251,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570252,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570253,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570254,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572254,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570256,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570257,
        animation_id=30001,
        animation_id_1=20001,
        region=1051572257,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570258,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570259,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.BanishedKnight0,
        animation_id=30011,
        animation_id_1=20011,
        region=1051572270,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BanishedKnight1,
        region=1051572271,
        radius=0.5,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570273,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1051572274(
        0,
        character=Characters.BanishedKnight3,
        animation_id=30011,
        animation_id_1=20011,
        region=1051572274,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570276,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570277,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570278,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570279,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570280,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570281,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570282,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570283,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570284,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570285,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570286,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570287,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570288,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570289,
        animation_id=30010,
        animation_id_1=20010,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=1051570395, region=1051572275, radius=3.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=1051570315, region=1051572315, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=1051570315, character=1051570315, item_lot=40508, seconds=0.0, left=0)
    Event_1051572310(
        0,
        character=Characters.LionGuardian1,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572310,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1051572311(0, character=Characters.LionGuardian1, special_effect=13360)
    CommonFunc_90005300(
        0,
        flag=1051570310,
        character=Characters.LionGuardian0,
        item_lot=1051570800,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=1051570311,
        character=Characters.LionGuardian1,
        item_lot=1051570810,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(0, character=Characters.Wolf0, region=1051572370, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Wolf1,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572372,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Wolf2, region=1051572370, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=1051570381,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=1051570383,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WolfPackLeader1,
        region=1051572385,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1051572450(0, character=Characters.GiantSkeletonTorso0, special_effect=5021)
    Event_1051572430(0, character=Characters.GiantSkeletonTorso0, region=1051572430, flag=1051572440)
    Event_1051572430(1, character=Characters.GiantSkeletonTorso1, region=1051572430, flag=1051572441)
    Event_1051572430(2, character=Characters.GiantSkeletonTorso2, region=1051572430, flag=1051572442)
    Event_1051572430(3, character=Characters.GiantSkeletonTorso3, region=1051572430, flag=1051572443)
    Event_1051572430(6, character=Characters.GiantSkeletonTorso4, region=1051572430, flag=1051572446)
    Event_1051572430(7, character=Characters.GiantSkeletonTorso5, region=1051572430, flag=1051572447)
    CommonFunc_90005211(
        0,
        character=Characters.GiantSkeletonTorso0,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=1051570421, character=Characters.TibiaMariner, item_lot=1051570720, seconds=0.0, left=0)
    Event_1051572460(
        0,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso0,
        special_effect=15335,
    )
    Event_1051572460(
        1,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso1,
        special_effect=15335,
    )
    Event_1051572460(
        2,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso2,
        special_effect=15335,
    )
    Event_1051572460(
        3,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso3,
        special_effect=15335,
    )
    Event_1051572460(
        6,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso4,
        special_effect=15335,
    )
    Event_1051572460(
        7,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso5,
        special_effect=15335,
    )
    Event_1051572460(
        9,
        character=Characters.TibiaMariner,
        character_1=m60_50_57_00_Characters.GiantSkeletonTorso,
        special_effect=15335,
    )
    CommonFunc_90005616(0, flag=1051577720, region=1051572700)
    CommonFunc_90005211(
        0,
        character=Characters.Slug4,
        animation_id=30000,
        animation_id_1=20000,
        region=1051572368,
        radius=0.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930025, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1051570700)
    DisableBackread(Characters.WanderingNoble)
    Event_1051570519()


@ContinueOnRest(1051572510)
def Event_1051572510():
    """Event 1051572510"""
    CommonFunc_90005500(
        0,
        flag=1051570510,
        flag_1=1051570511,
        left=0,
        asset=Assets.AEG030_095_2000,
        asset_1=Assets.AEG030_183_2001,
        obj_act_id=1051573511,
        asset_2=Assets.AEG030_183_2000,
        obj_act_id_1=1051573512,
        region=1051572511,
        region_1=1051572512,
        flag_2=1051570512,
        flag_3=1051570513,
        left_1=1051570514,
    )


@ContinueOnRest(1051570519)
def Event_1051570519():
    """Event 1051570519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(1051570510)
    EnableThisSlotFlag()


@RestartOnRest(1051572430)
def Event_1051572430(_, character: Character | int, region: Region | int, flag: Flag | int):
    """Event 1051572430"""
    AND_15.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    AND_14.Add(CharacterBackreadEnabled(character))
    AwaitConditionTrue(AND_14)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_1)
    AND_2.Add(AllPlayersOutsideRegion(region=region))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(character, 15338)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_5.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_5.Add(AND_5)
    OR_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_6.Add(OR_5)
    AND_6.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_6.Add(AND_6)
    OR_6.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_6)
    
    DisableNetworkFlag(flag)
    AddSpecialEffect(character, 15339)
    Wait(3.0)
    Restart()


@RestartOnRest(1051572450)
def Event_1051572450(_, character: Character | int, special_effect: int):
    """Event 1051572450"""
    AddSpecialEffect(character, special_effect)


@RestartOnRest(1051572460)
def Event_1051572460(_, character: Character | int, character_1: uint, special_effect: int):
    """Event 1051572460"""
    GotoIfFlagDisabled(Label.L0, flag=1051570421)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) == 0)
    
    AND_1.Add(CharacterHasSpecialEffect(character_1, special_effect))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Kill(character_1, award_runes=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Kill(character_1, award_runes=True)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1051572250)
def Event_1051572250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    seconds_1: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    character_1: Character | int,
):
    """Event 1051572250"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(CharacterHasSpecialEffect(character_1, 17126))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds_1)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()
    Wait(seconds)


@RestartOnRest(1051572274)
def Event_1051572274(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1051572274"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(HealthRatio(Characters.BanishedKnight2) <= 0.4000000059604645)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(1051572310)
def Event_1051572310(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1051572310"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_3.Add(HealthRatio(Characters.LionGuardian0) <= 0.5)
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(1051572311)
def Event_1051572311(_, character: Character | int, special_effect: int):
    """Event 1051572311"""
    if ThisEventSlotFlagEnabled():
        return
    DisableHealthBar(character)
    AddSpecialEffect(character, special_effect)
    Wait(0.10000000149011612)
    EnableHealthBar(character)
    End()


@RestartOnRest(1051572350)
def Event_1051572350():
    """Event 1051572350"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1051572350))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1051572351,
            dummy_id=900,
            behavior_id=802105070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1051572580)
def Event_1051572580():
    """Event 1051572580"""
    RegisterLadder(start_climbing_flag=1051570580, stop_climbing_flag=1051570581, asset=Assets.AEG030_833_2000)
    RegisterLadder(start_climbing_flag=1051570582, stop_climbing_flag=1051570583, asset=Assets.AEG030_834_2000)
    RegisterLadder(start_climbing_flag=1051570584, stop_climbing_flag=1051570585, asset=Assets.AEG030_834_2001)
    RegisterLadder(start_climbing_flag=1051570590, stop_climbing_flag=1051570591, asset=Assets.AEG030_822_2001)
    RegisterLadder(start_climbing_flag=1051570592, stop_climbing_flag=1051570593, asset=Assets.AEG030_822_2003)
    RegisterLadder(start_climbing_flag=1051570594, stop_climbing_flag=1051570595, asset=Assets.AEG030_822_2005)


@ContinueOnRest(1051572800)
def Event_1051572800():
    """Event 1051572800"""
    if FlagEnabled(1051570800):
        return
    
    MAIN.Await(HealthRatio(Characters.Commander) <= 0.0)
    
    MAIN.Await(CharacterDead(Characters.Commander))
    
    KillBossAndDisplayBanner(character=Characters.Commander, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(1051570800)
    EnableFlag(9184)
    if PlayerInOwnWorld():
        EnableFlag(61184)


@RestartOnRest(1051572810)
def Event_1051572810():
    """Event 1051572810"""
    GotoIfFlagDisabled(Label.L0, flag=1051570800)
    DisableCharacter(Characters.Commander)
    DisableAnimations(Characters.Commander)
    Kill(Characters.Commander)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Commander)
    GotoIfFlagEnabled(Label.L1, flag=1051570801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1051572801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Commander))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Commander, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Commander, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Commander, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Commander, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Commander, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(1051570801)
    ForceAnimation(Characters.Commander, 20010)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1051572805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1051572800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.Commander, 20010)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Commander)
    SetNetworkUpdateRate(1051575800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Commander, name=903050500)


@RestartOnRest(1051572811)
def Event_1051572811():
    """Event 1051572811"""
    if FlagEnabled(1051570800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.Commander, 11155))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1051572802)


@RestartOnRest(1051572812)
def Event_1051572812():
    """Event 1051572812"""
    DisableNetworkSync()
    if FlagEnabled(1051570800):
        return
    AND_1.Add(FlagDisabled(1051570800))
    AND_1.Add(HealthValue(Characters.Commander) != 0)
    AND_1.Add(CharacterHasSpecialEffect(Characters.Commander, 11135))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.Commander, 11135))
    
    MAIN.Await(AND_2)
    
    OR_15.Add(HealthValue(Characters.Commander) == 0)
    if OR_15:
        return
    Restart()


@RestartOnRest(1051572820)
def Event_1051572820(_, character: Character | int, character_1: uint, special_effect: int, animation_id: int):
    """Event 1051572820"""
    GotoIfFlagDisabled(Label.L0, flag=1051570800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character_1)
    DisableCharacter(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    ForceAnimation(character_1, animation_id, wait_for_completion=True)


@RestartOnRest(1051572821)
def Event_1051572821(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1051572821"""
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(CharacterDead(character))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character_1, animation_id, skip_transition=True)
    WaitFrames(frames=300)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()


@RestartOnRest(1051572822)
def Event_1051572822(
    _,
    character: uint,
    character_1: Character | int,
    character_2: Character | int,
    special_effect: int,
):
    """Event 1051572822"""
    if FlagEnabled(character):
        return
    AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterDead(character_2))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect)


@RestartOnRest(1051572828)
def Event_1051572828(_, region: Region | int):
    """Event 1051572828"""
    if FlagEnabled(1051570800):
        return
    AND_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    
    MAIN.Await(AND_2)
    
    WaitRealFrames(frames=1)
    AddSpecialEffect(ALL_SPIRIT_SUMMONS, 10859)


@RestartOnRest(1051572829)
def Event_1051572829(_, region: Region | int):
    """Event 1051572829"""
    if FlagEnabled(1051570800):
        return
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(ALL_PLAYERS, 10859)
    Wait(0.10000000149011612)
    AND_3.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region))
    
    MAIN.Await(AND_3)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(ALL_PLAYERS, 10859)
    Restart()


@ContinueOnRest(1051572849)
def Event_1051572849():
    """Event 1051572849"""
    CommonFunc_9005800(
        0,
        flag=1051570800,
        entity=Assets.AEG099_002_9000,
        region=1051572800,
        flag_1=1051572805,
        character=1051575800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1051570800,
        entity=Assets.AEG099_002_9000,
        region=1051572800,
        flag_1=1051572805,
        flag_2=1051572806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1051570800, asset=Assets.AEG099_002_9000, vfx_id=3, right=0)
    CommonFunc_9005811(0, flag=1051570800, asset=Assets.AEG099_002_9001, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1051570800,
        bgm_boss_conv_param_id=950000,
        flag_1=1051572805,
        flag_2=1051572806,
        right=0,
        flag_3=1051572802,
        left=0,
        left_1=0,
    )


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    RunEvent(1051572581, slot=0, args=(0,))
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1251576420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1251570400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1251572400, flag_1=1251570400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9000,
        dummy_id=101,
        seconds=0.0,
    )
    CommonFunc_90005453(
        1,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9001,
        dummy_id=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9002,
        dummy_id=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9003,
        dummy_id=104,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9004,
        dummy_id=105,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9005,
        dummy_id=106,
        seconds=0.5,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9006,
        dummy_id=107,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9007,
        dummy_id=108,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9008,
        dummy_id=109,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9009,
        dummy_id=110,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9010,
        dummy_id=111,
        seconds=1.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9016,
        dummy_id=117,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9017,
        dummy_id=118,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9018,
        dummy_id=119,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9019,
        dummy_id=120,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9020,
        dummy_id=121,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9021,
        dummy_id=122,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9022,
        dummy_id=123,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9023,
        dummy_id=124,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9024,
        dummy_id=125,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9025,
        dummy_id=126,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9026,
        dummy_id=127,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9027,
        dummy_id=128,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9032,
        dummy_id=133,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9033,
        dummy_id=134,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9034,
        dummy_id=135,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9035,
        dummy_id=136,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9036,
        dummy_id=137,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9037,
        dummy_id=138,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9038,
        dummy_id=139,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9039,
        dummy_id=140,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9040,
        dummy_id=141,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9041,
        dummy_id=142,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9048,
        dummy_id=149,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9049,
        dummy_id=150,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9050,
        dummy_id=151,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9051,
        dummy_id=152,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9052,
        dummy_id=153,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9053,
        dummy_id=154,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9054,
        dummy_id=155,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9055,
        dummy_id=156,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9056,
        dummy_id=157,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9057,
        dummy_id=158,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9058,
        dummy_id=159,
        seconds=0.0,
    )
    CommonFunc_90005456(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_004_9000,
        asset_1=Assets.AEG300_005_9000,
        flag=1251570400,
    )


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_014_9000,
        asset_1=Assets.AEG300_004_9000,
        asset_2=Assets.AEG300_005_9000,
    )
