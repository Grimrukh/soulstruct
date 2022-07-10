"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_799()
    Event_801()
    Event_899()
    Event_900()
    Event_901()
    Event_910(0, item=1501, item_1=1601, flag=941)
    Event_910(1, item=1502, item_1=1602, flag=942)
    Event_910(2, item=1503, item_1=1603, flag=943)
    Event_910(3, item=1504, item_1=1604, flag=944)
    Event_910(4, item=1505, item_1=1605, flag=945)
    Event_910(5, item=1506, item_1=1606, flag=946)
    Event_910(6, item=1507, item_1=1607, flag=947)
    Event_910(7, item=1508, item_1=1608, flag=948)
    Event_910(8, item=1509, item_1=1609, flag=949)
    Event_910(9, item=1510, item_1=1610, flag=950)
    Event_910(10, item=1511, item_1=1611, flag=951)
    Event_910(11, item=1512, item_1=1612, flag=952)
    Event_910(12, item=1513, item_1=1613, flag=953)
    Event_910(13, item=1514, item_1=1614, flag=954)
    Event_910(14, item=1515, item_1=1615, flag=955)
    Event_910(15, item=1516, item_1=1616, flag=956)
    Event_970(1, flag=971, item=1501, item_1=1601, area_id=14, block_id=1, player_start=1410992)
    Event_970(2, flag=972, item=1502, item_1=1602, area_id=10, block_id=1, player_start=1010993)
    Event_970(3, flag=973, item=1503, item_1=1603, area_id=10, block_id=1, player_start=1010994)
    Event_970(4, flag=974, item=1504, item_1=1604, area_id=13, block_id=1, player_start=1310990)
    Event_970(5, flag=975, item=1505, item_1=1605, area_id=15, block_id=0, player_start=1500991)
    Event_970(6, flag=976, item=1506, item_1=1606, area_id=15, block_id=0, player_start=1500992)
    Event_970(7, flag=977, item=1507, item_1=1607, area_id=15, block_id=0, player_start=1500993)
    Event_970(8, flag=978, item=1508, item_1=1608, area_id=15, block_id=0, player_start=1210991)
    Event_970(9, flag=979, item=1509, item_1=1609, area_id=10, block_id=0, player_start=1000991)
    Event_970(10, flag=980, item=1510, item_1=1610, area_id=10, block_id=0, player_start=1000992)
    Event_970(11, flag=981, item=1511, item_1=1611, area_id=17, block_id=0, player_start=1700992)
    Event_970(12, flag=982, item=1512, item_1=1612, area_id=14, block_id=1, player_start=1410993)
    Event_970(13, flag=983, item=1513, item_1=1613, area_id=12, block_id=0, player_start=1200990)
    Event_970(14, flag=984, item=1514, item_1=1614, area_id=12, block_id=0, player_start=1200993)
    Event_970(15, flag=985, item=1515, item_1=1615, area_id=10, block_id=1, player_start=1010995)
    Event_970(16, flag=986, item=1516, item_1=1616, area_id=12, block_id=1, player_start=1210992)
    DisableFlag(760)
    DisableFlag(762)
    EnableFlag(765)
    Event_761()
    Event_763()
    Event_730()
    Event_731()
    Event_8131(0, item=202, item_1=203)
    Event_8131(1, item=204, item_1=205)
    Event_8131(2, item=206, item_1=207)
    Event_8131(3, item=208, item_1=209)
    Event_8131(4, item=210, item_1=211)
    Event_8131(5, item=212, item_1=213)
    Event_8131(6, item=214, item_1=215)
    Event_9051()
    NightfallSendToScript(int1=100, int2=10, float1=0.0, float2=0.0)
    Event_9054()
    Event_9055(0, int2__special_effect__special_effect_id=93050)
    Event_9055(1, int2__special_effect__special_effect_id=93051)
    Event_9055(2, int2__special_effect__special_effect_id=93052)
    Event_9055(3, int2__special_effect__special_effect_id=93053)
    Event_9058()
    Event_9059(0, 10000)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    if FlagEnabled(11813104):
        Event_802()
        Event_800()
        Event_840(0, value=15, text=900001)
        Event_840(1, value=30, text=900002)
        Event_840(2, value=45, text=900003)
        Event_840(3, value=60, text=900004)
        Event_840(4, value=75, text=900005)
        Event_840(5, value=90, text=900006)
        Event_840(6, value=105, text=900007)
        Event_840(7, value=120, text=900008)
        Event_840(8, value=135, text=900009)
        Event_840(9, value=150, text=900010)
        Event_840(10, value=165, text=900011)
    else:
        Event_809()
    Wait(0.10000000149011612)


@NeverRestart(799)
def Event_799():
    """Event 799"""
    if ThisEventFlagEnabled():
        return
    EnableFlag(11813507)
    End()


@NeverRestart(800)
def Event_800():
    """Event 800"""
    Wait(1.0)
    SkipLinesIfFlagEnabled(5, 830)
    IncrementEventValue(820, bit_count=8, max_value=60)
    OR_7.Add(EventValueEqual(flag=820, bit_count=8, value=60))
    SkipLinesIfConditionFalse(2, OR_7)
    ClearEventValue(820, bit_count=8)
    IncrementEventValue(810, bit_count=8, max_value=180)
    Restart()


@NeverRestart(801)
def Event_801():
    """Event 801"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 900))
    
    EnableFlag(11813100)
    EnableFlag(11813101)
    EnableFlag(11813102)
    EnableFlag(11813103)
    EnableFlag(11813104)
    ClearEventValue(810, bit_count=8)
    ClearEventValue(820, bit_count=8)
    DisableFlagRange((840, 851))
    DisableFlag(899)
    DisableFlag(802)
    DisableFlagRange((11000000, 11002999))
    DisableFlagRange((11010000, 11012999))
    DisableFlagRange((11020000, 11022999))
    DisableFlagRange((11100000, 11102999))
    DisableFlagRange((11200000, 11202999))
    DisableFlagRange((11210000, 11212999))
    DisableFlagRange((11300000, 11302999))
    DisableFlagRange((11310000, 11312999))
    DisableFlagRange((11320000, 11322999))
    DisableFlagRange((11400000, 11402999))
    DisableFlagRange((11410000, 11412999))
    DisableFlagRange((11500000, 11502999))
    DisableFlagRange((11510000, 11512999))
    DisableFlagRange((11600000, 11602999))
    DisableFlagRange((11700000, 11702999))
    DisableFlagRange((11800000, 11802999))
    DisableFlagRange((11810000, 11812999))
    DisableFlagRange((50001000, 51819999))
    DisableFlag(803)
    DisableFlag(804)
    DisableFlag(805)
    Event_803()
    Event_804()
    Event_805()
    AND_1.Add(FlagEnabled(803))
    AND_1.Add(FlagEnabled(804))
    AND_1.Add(FlagEnabled(805))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11813501):
        WarpToMap(game_map=PAINTED_WORLD, player_start=1100990)
    else:
        WarpToMap(game_map=KILN_OF_THE_FIRST_FLAME)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 900))
    
    Restart()


@NeverRestart(840)
def Event_840(_, value: uint, text: int):
    """Event 840"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(EventValueEqual(flag=810, bit_count=8, value=value))
    
    DisplayBattlefieldMessage(text, display_location_index=0)


@NeverRestart(802)
def Event_802():
    """Event 802"""
    if ThisEventFlagEnabled():
        return
    EnableFlag(250)
    EnableFlag(251)
    EnableFlag(252)
    EnableFlag(258)
    Wait(5.0)
    DisplayBattlefieldMessage(900000, display_location_index=0)


@NeverRestart(809)
def Event_809():
    """Event 809"""
    MAIN.Await(FlagEnabled(11813104))
    
    Event_802()
    Event_800()
    Event_840(0, value=15, text=900001)
    Event_840(1, value=30, text=900002)
    Event_840(2, value=45, text=900003)
    Event_840(3, value=60, text=900004)
    Event_840(4, value=75, text=900005)
    Event_840(5, value=90, text=900006)
    Event_840(6, value=105, text=900007)
    Event_840(7, value=120, text=900008)
    Event_840(8, value=135, text=900009)
    Event_840(9, value=150, text=900010)
    Event_840(10, 165, 900011)


@NeverRestart(803)
def Event_803():
    """Event 803"""
    OR_1.Add(PlayerHasGood(1501))
    OR_1.Add(PlayerHasGood(1601))
    SkipLinesIfConditionFalse(2, OR_1)
    EnableFlag(11412500)
    EnableFlag(11412520)
    OR_2.Add(PlayerHasGood(1502))
    OR_2.Add(PlayerHasGood(1602))
    SkipLinesIfConditionFalse(2, OR_2)
    EnableFlag(11012500)
    EnableFlag(11012520)
    OR_3.Add(PlayerHasGood(1503))
    OR_3.Add(PlayerHasGood(1603))
    SkipLinesIfConditionFalse(2, OR_3)
    EnableFlag(11012501)
    EnableFlag(11012521)
    OR_4.Add(PlayerHasGood(1504))
    OR_4.Add(PlayerHasGood(1604))
    SkipLinesIfConditionFalse(2, OR_4)
    EnableFlag(11312500)
    EnableFlag(11312520)
    OR_5.Add(PlayerHasGood(1505))
    OR_5.Add(PlayerHasGood(1605))
    SkipLinesIfConditionFalse(2, OR_5)
    EnableFlag(11502501)
    EnableFlag(11502520)
    OR_6.Add(PlayerHasGood(1506))
    OR_6.Add(PlayerHasGood(1606))
    SkipLinesIfConditionFalse(2, OR_6)
    EnableFlag(11502500)
    EnableFlag(11502521)
    OR_7.Add(PlayerHasGood(1507))
    OR_7.Add(PlayerHasGood(1607))
    SkipLinesIfConditionFalse(2, OR_7)
    EnableFlag(11502502)
    EnableFlag(11502522)
    End()


@NeverRestart(804)
def Event_804():
    """Event 804"""
    OR_1.Add(PlayerHasGood(1508))
    OR_1.Add(PlayerHasGood(1608))
    SkipLinesIfConditionFalse(2, OR_1)
    EnableFlag(11212500)
    EnableFlag(11212520)
    OR_2.Add(PlayerHasGood(1509))
    OR_2.Add(PlayerHasGood(1609))
    SkipLinesIfConditionFalse(2, OR_2)
    EnableFlag(11002500)
    EnableFlag(11002520)
    OR_3.Add(PlayerHasGood(1510))
    OR_3.Add(PlayerHasGood(1610))
    SkipLinesIfConditionFalse(2, OR_3)
    EnableFlag(11002501)
    EnableFlag(11002521)
    OR_4.Add(PlayerHasGood(1511))
    OR_4.Add(PlayerHasGood(1611))
    SkipLinesIfConditionFalse(2, OR_4)
    EnableFlag(11702500)
    EnableFlag(11702520)
    OR_5.Add(PlayerHasGood(1512))
    OR_5.Add(PlayerHasGood(1612))
    SkipLinesIfConditionFalse(2, OR_5)
    EnableFlag(11412502)
    EnableFlag(11412522)
    OR_6.Add(PlayerHasGood(1513))
    OR_6.Add(PlayerHasGood(1613))
    SkipLinesIfConditionFalse(2, OR_6)
    EnableFlag(11202501)
    EnableFlag(11202521)
    OR_7.Add(PlayerHasGood(1514))
    OR_7.Add(PlayerHasGood(1614))
    SkipLinesIfConditionFalse(2, OR_7)
    EnableFlag(11102500)
    EnableFlag(11202522)
    End()


@NeverRestart(805)
def Event_805():
    """Event 805"""
    OR_1.Add(PlayerHasGood(1515))
    OR_1.Add(PlayerHasGood(1615))
    SkipLinesIfConditionFalse(2, OR_1)
    EnableFlag(11012502)
    EnableFlag(11012522)
    OR_2.Add(PlayerHasGood(1516))
    OR_2.Add(PlayerHasGood(1616))
    SkipLinesIfConditionFalse(2, OR_2)
    EnableFlag(11212501)
    EnableFlag(11212522)
    End()


@NeverRestart(900)
def Event_900():
    """Event 900"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 901))
    
    RemoveGoodFromPlayer(item=1501)
    RemoveGoodFromPlayer(item=1502)
    RemoveGoodFromPlayer(item=1503)
    RemoveGoodFromPlayer(item=1504)
    RemoveGoodFromPlayer(item=1505)
    RemoveGoodFromPlayer(item=1506)
    RemoveGoodFromPlayer(item=1507)
    RemoveGoodFromPlayer(item=1508)
    RemoveGoodFromPlayer(item=1509)
    RemoveGoodFromPlayer(item=1510)
    RemoveGoodFromPlayer(item=1511)
    RemoveGoodFromPlayer(item=1512)
    RemoveGoodFromPlayer(item=1513)
    RemoveGoodFromPlayer(item=1514)
    RemoveGoodFromPlayer(item=1515)
    RemoveGoodFromPlayer(item=1516)
    AwardItemLot(15000, host_only=True)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 901))
    
    Restart()


@NeverRestart(901)
def Event_901():
    """Event 901"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 902))
    
    RemoveGoodFromPlayer(item=1601)
    RemoveGoodFromPlayer(item=1602)
    RemoveGoodFromPlayer(item=1603)
    RemoveGoodFromPlayer(item=1604)
    RemoveGoodFromPlayer(item=1605)
    RemoveGoodFromPlayer(item=1606)
    RemoveGoodFromPlayer(item=1607)
    RemoveGoodFromPlayer(item=1608)
    RemoveGoodFromPlayer(item=1609)
    RemoveGoodFromPlayer(item=1610)
    RemoveGoodFromPlayer(item=1611)
    RemoveGoodFromPlayer(item=1612)
    RemoveGoodFromPlayer(item=1613)
    RemoveGoodFromPlayer(item=1614)
    RemoveGoodFromPlayer(item=1615)
    RemoveGoodFromPlayer(item=1616)
    AwardItemLot(16000, host_only=True)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 902))
    
    Restart()


@NeverRestart(899)
def Event_899():
    """Event 899"""
    if ThisEventFlagEnabled():
        StopEvent(event_id=800)
        DisplayStatus(10040008)
        Wait(3.0)
        AddSpecialEffect(PLAYER, 900)
        End()
    
    MAIN.Await(EventValueGreaterThanOrEqual(flag=810, bit_count=8, value=180))
    
    DisplayBattlefieldMessage(900012, display_location_index=0)
    StopEvent(event_id=800)
    Wait(5.0)
    DisplayStatus(10040008)
    Wait(5.0)
    AddSpecialEffect(PLAYER, 900)


@NeverRestart(910)
def Event_910(_, item: int, item_1: int, flag: int):
    """Event 910"""
    DisableFlag(flag)
    OR_1.Add(PlayerHasGood(item))
    OR_1.Add(PlayerHasGood(item_1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    AND_1.Add(PlayerDoesNotHaveGood(item))
    AND_1.Add(PlayerDoesNotHaveGood(item_1))
    
    MAIN.Await(AND_1)
    
    Restart()


@NeverRestart(970)
def Event_970(_, flag: int, item: int, item_1: int, area_id: uchar, block_id: uchar, player_start: int):
    """Event 970"""
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_7.Add(PlayerHasGood(item))
    SkipLinesIfConditionFalse(3, OR_7)
    RemoveGoodFromPlayer(item=item)
    AwardItemLot(15000, host_only=True)
    SkipLines(4)
    AND_7.Add(PlayerHasGood(item_1))
    SkipLinesIfConditionFalse(2, AND_7)
    RemoveGoodFromPlayer(item=item_1)
    AwardItemLot(16000, host_only=True)
    DisableFlag(flag)
    Wait(1.0)
    WarpToMap(game_map=(area_id, block_id), player_start=player_start)
    Restart()


@NeverRestart(761)
def Event_761():
    """Event 761"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(760))
    
    WaitFrames(frames=200)
    DisableFlag(760)
    Restart()


@NeverRestart(763)
def Event_763():
    """Event 763"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(762))
    
    ForceAnimation(PLAYER, 7697)
    Wait(3.5)
    DisableFlag(762)
    Wait(2.799999952316284)
    DisableFlag(764)
    ForceAnimation(PLAYER, 7701, loop=True)
    Restart()


@NeverRestart(730)
def Event_730():
    """Event 730"""
    AND_1.Add(FlagDisabled(732))
    AND_1.Add(FlagEnabled(8000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(732)
    EnableFlag(735)
    Restart()


@NeverRestart(731)
def Event_731():
    """Event 731"""
    MAIN.Await(FlagDisabled(8000))
    
    DisableFlag(732)
    DisableFlag(735)
    
    MAIN.Await(FlagEnabled(8000))
    
    Restart()


@NeverRestart(8131)
def Event_8131(_, item: int, item_1: int):
    """Event 8131"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(PlayerHasGood(item))
    OR_1.Add(PlayerHasGood(item_1))
    
    MAIN.Await(OR_1)
    
    if ValueEqual(left=item, right=202):
        EnableFlag(8131)
    if ValueEqual(left=item, right=204):
        EnableFlagRange((8131, 8132))
    if ValueEqual(left=item, right=206):
        EnableFlagRange((8131, 8133))
    if ValueEqual(left=item, right=208):
        EnableFlagRange((8131, 8134))
    if ValueEqual(left=item, right=210):
        EnableFlagRange((8131, 8135))
    if ValueEqual(left=item, right=212):
        EnableFlagRange((8131, 8136))
    if ValueEqual(left=item, right=214):
        EnableFlagRange((8131, 8137))
    End()


@NeverRestart(9051)
def Event_9051():
    """Event 9051"""
    if FlagDisabled(9051):
        AwardItemLot(77770000, host_only=False)
        AwardItemLot(77770006, host_only=False)
        AwardItemLot(77770012, host_only=False)


@NeverRestart(9054)
def Event_9054():
    """Event 9054"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 93012))
    SkipLinesIfConditionTrue(3, AND_1)
    CancelSpecialEffect(PLAYER, 93012)
    NightfallSendToScript(int1=100, int2=13, float1=0.0, float2=0.0)
    SkipLines(6)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 97777))
    SkipLinesIfConditionTrue(3, AND_2)
    CancelSpecialEffect(PLAYER, 97777)
    NightfallSendToScript(int1=100, int2=12, float1=0.0, float2=0.0)
    SkipLines(1)
    NightfallSendToScript(int1=100, int2=11, float1=0.0, float2=0.0)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 97778))
    SkipLinesIfConditionTrue(2, AND_3)
    CancelSpecialEffect(PLAYER, 97778)
    PlaySoundEffect(PLAYER, 777790001, sound_type=SoundType.c_CharacterMotion)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 93013))
    SkipLinesIfConditionTrue(2, AND_4)
    NightfallSendToScript(int1=200, int2=0, float1=0.0, float2=0.0)
    SkipLines(1)
    NightfallSendToScript(int1=200, int2=1, float1=0.0, float2=0.0)
    Restart()


@NeverRestart(9055)
def Event_9055(_, int2__special_effect__special_effect_id: int):
    """Event 9055"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, int2__special_effect__special_effect_id))
    
    NightfallSendToScript(int1=300, int2=int2__special_effect__special_effect_id, float1=0.0, float2=0.0)
    CancelSpecialEffect(PLAYER, int2__special_effect__special_effect_id)
    Restart()


@NeverRestart(9056)
def Event_9056(_, int2__special_effect: int):
    """Event 9056"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, int2__special_effect))
    
    NightfallSendToScript(int1=301, int2=int2__special_effect, float1=0.0, float2=0.0)
    Restart()


@NeverRestart(9057)
def Event_9057(_, int2__special_effect: int):
    """Event 9057"""
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, int2__special_effect))
    
    NightfallSendToScript(int1=302, int2=int2__special_effect, float1=0.0, float2=0.0)
    Restart()


@NeverRestart(9058)
def Event_9058():
    """Event 9058"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 93066))
    
    PlaySoundEffect(PLAYER, 777790004, sound_type=SoundType.c_CharacterMotion)
    CancelSpecialEffect(PLAYER, 93066)
    Restart()


@NeverRestart(9059)
def Event_9059(_, character: int):
    """Event 9059"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 93031))
    SkipLinesIfConditionTrue(2, AND_1)
    PlaySoundEffect(character, 777700014, sound_type=SoundType.c_CharacterMotion)
    CancelSpecialEffect(character, 93031)
    Restart()
