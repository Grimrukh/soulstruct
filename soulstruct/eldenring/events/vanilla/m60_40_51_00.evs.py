"""
South Altus Plateau (NW) (NW)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_40_51_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, flag=1040510500, character=Characters.Scarab, item_lot=40310, seconds=0.0, left=0)
    CommonFunc_90005706(0, character=Characters.Commoner, animation_id=930023, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier1, region=1040512407, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier2, region=1040512407, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier1, region=1040512408, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier2, region=1040512408, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
