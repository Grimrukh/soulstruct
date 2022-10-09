"""
Southeast Liurnia (NW) (SW)

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
from .entities.m60_36_42_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005637(0, flag=31058521, character=Characters.WanderingNoble, region=1036421620)
    CommonFunc_90005636(
        0,
        flag=31058521,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect=4470,
        destination=1036422620,
        region=1036422621,
        flag_1=1036422620,
        patrol_information_id=1036423620,
        right=-1,
    )
