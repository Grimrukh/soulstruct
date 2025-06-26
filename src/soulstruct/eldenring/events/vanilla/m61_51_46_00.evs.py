"""
Land of Shadow 12-11 NE SE

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005639(0, flag=2051460500, asset=2051461500, asset_1=2051461501, asset_2=2051461502, seconds=3.0)
    Event_2051462510()
    CommonFunc_90005501(
        0,
        flag=2051460510,
        flag_1=2051460511,
        left=0,
        asset=2051461510,
        asset_1=2051461511,
        asset_2=2051461512,
        flag_2=2051460512,
    )
    CommonFunc_90005502(0, flag=2051460514, asset=2051461512, region=2051462511)
    CommonFunc_90005525(0, flag=2051460620, asset=2051461620)
    Event_2051460700(0, character=2051460700, animation_id=90101)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_2051460519()


@ContinueOnRest(2051462510)
def Event_2051462510():
    """Event 2051462510"""
    CommonFunc_90005500(
        0,
        flag=2051460510,
        flag_1=2051460511,
        left=0,
        asset=2051461510,
        asset_1=2051461511,
        obj_act_id=2051463511,
        asset_2=2051461512,
        obj_act_id_1=2051463512,
        region=2051462511,
        region_1=2051462512,
        flag_2=2051460512,
        flag_3=2051460513,
        left_1=2051460514,
    )


@ContinueOnRest(2051460519)
def Event_2051460519():
    """Event 2051460519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(2051460510)
    EnableThisSlotFlag()


@RestartOnRest(2051460700)
def Event_2051460700(_, character: uint, animation_id: int):
    """Event 2051460700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, animation_id)
    End()
