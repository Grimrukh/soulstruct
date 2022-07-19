"""
West Liurnia (SE) (NW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_34_45_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.GlintstoneDragon, name=904502600, npc_threat_level=25)
    CommonFunc_90005861(
        0,
        flag=1034450800,
        left=0,
        character=Characters.GlintstoneDragon,
        left_1=1,
        item_lot__item_lot_param_id=30210,
        text=30061,
        seconds=0.0,
    )
    Event_1034452800()
    Event_1034452805()
    CommonFunc_90005211(
        0,
        character=Characters.GlintstoneDragon,
        animation_id=30000,
        animation_id_1=20000,
        region=1034452800,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, 1034450800, 1034452800, 5.0, 0.0, -1)
    CommonFunc_90005251(0, character=Characters.Scarab4, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab5, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab6, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab7, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab8, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab0, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab1, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab2, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.Scarab3, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005460(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005460(0, character=1034450201)
    CommonFunc_90005460(0, character=1034450202)
    CommonFunc_90005460(0, character=1034450203)
    CommonFunc_90005460(0, character=1034450204)
    CommonFunc_90005461(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005462(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005461(0, character=1034450201)
    CommonFunc_90005462(0, character=1034450201)
    CommonFunc_90005461(0, character=1034450202)
    CommonFunc_90005462(0, character=1034450202)
    CommonFunc_90005461(0, character=1034450203)
    CommonFunc_90005462(0, character=1034450203)
    CommonFunc_90005461(0, character=1034450204)
    CommonFunc_90005462(0, character=1034450204)
    CommonFunc_90005201(0, 1034450200, 30010, -1, 0.0, 0.0, 0, 0, 0, 0)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005620(
        0,
        flag=1034450570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1034452571,
        cancel_flag__right_flag=1034452572,
        right=1034452573,
    )
    CommonFunc_90005621(0, 1034450570, 1034451573)


@RestartOnRest(1034452800)
def Event_1034452800():
    """Event 1034452800"""
    if FlagEnabled(1034450800):
        return
    AddSpecialEffect(Characters.GlintstoneDragon, 10247)


@RestartOnRest(1034452805)
def Event_1034452805():
    """Event 1034452805"""
    if FlagEnabled(1034450800):
        return
    SetNest(Characters.GlintstoneDragon, region=1034452810)
    Wait(1.0)
    Restart()
