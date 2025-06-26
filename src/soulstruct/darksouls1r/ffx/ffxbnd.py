from __future__ import annotations

__all__ = [
    "DEFAULT_REQUIRED_FFX_IDS",
    "FFXBND",
]

import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.maps import MSB

_LOGGER = logging.getLogger(__name__)


# All FFX/FLVER/TPF IDs required by vanilla enemy models.
# You'll note that most required FFX IDs for model 'cABC0' use IDs with five-digit format '1ABC?'.
# However, this is a very loose pattern and broken with random IDs all the time (including some seven-digit). In
# particular, enemies freely re-use FFX already created for other enemies, e.g. Sanctuary Guardian (c3470) uses the
# Titanite Demon's (c2300) lightning FFX, Gwyn (c5370) uses the Flaming Attack Dog's (c3341) fire TPF, etc.
DEFAULT_REQUIRED_FFX_IDS = {
    0: [],
    1000: [],
    1200: [],
    1201: [],
    1202: [1212000],
    1203: [1120300, 1120400, 1120401, 1120500],
    2060: [12061],
    2210: [],
    2230: [12230, 12231, 12232, 12234, 12235, 12237, 12238, 12239],
    2231: [11030, 11031, 11032, 11035, 11036, 12230, 12231, 12232, 12235, 12237, 12238, 12239],
    2232: [12232, 12237, 12238, 12239],
    2240: [12240, 12241, 12242],
    2250: [12250, 12258, 1225000],
    2260: [12260, 12261, 12262],
    2270: [],
    2280: [],
    2290: [],
    2300: [12303, 12304, 12305, 12306, 1223000, 1223100, 1223500, 1223600],
    2310: [1223200, 1223300],
    2320: [12320, 12321, 12322, 12324, 12325, 1222000],
    2330: [12330],
    2360: [12360, 12362, 12363, 12364, 12365],
    2370: [12370, 12371, 12372, 12373, 12374, 12375, 12376],
    2380: [12380, 12382, 12383],
    2390: [12390, 12391, 12392],
    2400: [12520, 12521, 12522],
    2410: [12410, 12411],
    2430: [12430],
    2500: [12500],
    2510: [],
    2520: [12520, 12521, 12522, 12523],
    2530: [12530, 12531, 12532],
    2540: [12540],
    2550: [],
    2560: [],
    2570: [],
    2590: [],
    2591: [],
    2600: [],
    2640: [12865],
    2650: [12650, 12651, 12652, 12653, 12654],
    2660: [12660, 12661],
    2670: [12670, 12671, 12672, 12673, 12674],
    2680: [12672, 12673, 12680, 12681, 12682],
    2690: [],
    2700: [12700, 12701, 12702, 12703, 12704],
    2710: [12713, 12714],
    2711: [12710, 12711, 12712],
    2730: [12730, 12732, 12733, 1273000, 1273100],
    2731: [],
    2750: [12750],
    2780: [12780],
    2790: [],
    2791: [12790],
    2792: [],
    2793: [],
    2794: [],
    2795: [],
    2800: [],
    2810: [],
    2811: [12810, 12811, 12812],
    2820: [],
    2830: [12830, 12831, 12832],
    2840: [12500, 12840, 12841, 12842, 12843, 12844, 12846, 12847, 12849],
    2860: [12859, 12864, 12865],
    2870: [12870, 12872, 12873, 12874, 12875, 12876],
    2900: [4600, 12900, 12901],
    2910: [12901, 12910, 12911, 12914],
    2920: [12865],
    2930: [],
    2940: [],
    2950: [],
    2960: [12960],
    3090: [13090],
    3110: [13110],
    3200: [13200, 13201, 13202],
    3210: [13211],
    3220: [13090],
    3230: [13226, 13227, 13228, 13229, 13232, 13233, 13234, 13235, 13236, 13237, 13238, 13239],
    3240: [13240, 13242, 13243],
    3250: [13250],
    3270: [13270, 13271, 13272],
    3290: [13290, 13291, 13292, 1329000],
    3300: [13110],
    3320: [13314, 13315, 13316, 13317, 13318, 13319, 13320, 13321, 13322, 13323, 13325, 13326, 13327, 13328, 13329],
    3330: [13330, 13331, 13332],
    3340: [],
    3341: [13340, 13341],
    3350: [],
    3370: [],
    3380: [13380],
    3390: [13390, 13391, 13392, 13395, 13396, 13397, 13398, 13399],
    3400: [13400, 13401, 13402],
    3410: [13410, 13411, 1341100, 1341200],
    3420: [
        13420, 13421, 13422, 13423, 13424, 13426, 13427, 13428, 13429,
        16005, 16006, 16007, 16009, 16010, 16011, 16012, 16013,
    ],
    3421: [1342000],
    3422: [],
    3430: [
        15130, 15131, 15135, 15136, 15138, 15140, 15141, 15142, 15143, 15147, 15148, 15149, 15151, 15155,
        15163, 15164, 15166, 15167, 15170, 15171, 15174, 15175, 15176, 15177,
    ],
    3431: [15176],
    3440: [],
    3450: [13450, 13451, 13452, 13453, 15176],
    3451: [],
    3460: [13460, 13461, 13462, 13463, 13464, 13465, 13466, 13467, 13468],
    3461: [13460, 13461, 13462, 13463, 13464, 13465, 13466, 13467, 13468],
    3470: [12303, 12304],
    3471: [],
    3472: [],
    3480: [13480, 13481],
    3490: [],
    3491: [],
    3500: [13500, 13501, 13503],
    3501: [13506, 13507, 13509],
    3510: [],
    3511: [],
    3520: [13520, 13521, 13522, 13523],
    3530: [13530, 13533, 13536, 13537, 13539, 13540],
    3531: [13534, 13541],
    4090: [14290, 14291, 14292],
    4100: [],
    4110: [14110, 14111, 14112, 14113, 14114, 14115],
    4120: [12384, 12385, 1412000, 1412100],
    4130: [14230, 14231, 14232],
    4140: [],
    4150: [14150],
    4160: [14150, 14250, 14251, 14252, 14254, 14255, 14256],
    4170: [14260, 14261, 14267, 14278],
    4171: [14268, 14270, 14271, 14277],
    4172: [14269, 14277, 14280, 14281],
    4180: [14181, 1412000],
    4190: [14190],
    4500: [],
    4510: [14410, 14411, 14412, 14430],
    4511: [],
    4520: [14520, 14521, 14522],
    4531: [15363, 15364, 15365],
    5200: [
        15200, 15201, 15202, 15203, 15204, 15205, 15207, 15208, 15209,
        15300, 15301, 15302, 15303, 15304, 15306, 15307, 1520000, 1520100,
    ],
    5201: [15300, 15306, 1520000, 1520100],
    5202: [15306, 1520000, 1520100],
    5210: [15210, 15211, 1521000, 1521100, 1521200],
    5220: [15220, 15221, 15223, 15225, 15226, 15227, 15228, 15229, 17220, 17221, 17222, 17223, 17224, 17225, 17226],
    5230: [15232, 15233, 15234, 15236],
    5231: [15233, 15234],
    5240: [],
    5250: [15242, 15246, 15247, 15248, 15249, 15250, 15252, 15254, 15256, 15257, 15258, 15259, 1525000],
    5260: [15260, 15261, 15262, 15263, 15264, 15510, 1526000, 1526100],
    5261: [15510],
    5270: [15243, 15244, 15270, 15273, 15276],
    5271: [15245, 15267, 15268, 15269, 15271, 15272, 15274, 15275, 15276, 15277, 15278, 15279],
    5280: [15280, 15281, 15282, 15283, 15284, 15285, 15286, 15287, 15288, 15289, 16000, 16001, 16003],
    5290: [15290, 15293, 15294, 15297, 15298, 15299, 15903, 15904, 15905],
    5291: [15903],
    5300: [15308, 15309],
    5310: [15310, 15311],
    5320: [15320, 15321, 15322, 15324, 15325, 15326, 15327, 15328, 15329],
    5330: [],
    5340: [],
    5350: [15350, 15351, 15353, 15354, 15355, 15358, 15359, 15368, 15369, 41100],
    5351: [15347, 15348, 15351, 15355, 15368, 15369],
    5352: [15368],
    5353: [15368],
    5360: [15360, 15361],
    5361: [15363],
    5370: [15371, 15373, 15374, 15375],
    5390: [15388, 15389, 15390, 15391, 15395, 15398, 15400, 15401, 15402, 15403, 15404],
    5400: [15410, 15411, 15412, 15414, 15415, 15416, 15417, 15418, 15419, 15421, 15422, 15423],
    5401: [15424, 15425],
}


# Source FFX files to find character model FFX/FLVER/TPF files in.
DEFAULT_CHARACTER_FFX_SOURCES = {
    0: {},
    1000: {},
    1200: {},
    1201: {},
    1202: {
        1212000: "FRPG_SfxBnd_m10_00",
    },
    1203: {
        1120400: "FRPG_SfxBnd_m11",
        1120300: "FRPG_SfxBnd_m11",
        1120500: "FRPG_SfxBnd_m11",
        1120401: "FRPG_SfxBnd_m11",
    },
    2060: {
        12061: "FRPG_SfxBnd_m14",
    },
    2210: {},
    2230: {
        12239: "FRPG_SfxBnd_m18_01",
        12232: "FRPG_SfxBnd_m18_01",
        12234: "FRPG_SfxBnd_m18_01",
        12237: "FRPG_SfxBnd_m18_01",
        12235: "FRPG_SfxBnd_m18_01",
        12238: "FRPG_SfxBnd_m18_01",
        12230: "FRPG_SfxBnd_m18_01",
        12231: "FRPG_SfxBnd_m18_01",
    },
    2231: {
        11035: "FRPG_SfxBnd_m14_01",
        11030: "FRPG_SfxBnd_m14_01",
        11031: "FRPG_SfxBnd_m14_01",
        11032: "FRPG_SfxBnd_m14_01",
        12239: "FRPG_SfxBnd_m18_01",
        12232: "FRPG_SfxBnd_m18_01",
        12237: "FRPG_SfxBnd_m18_01",
        11036: "FRPG_SfxBnd_m14_01",
        12235: "FRPG_SfxBnd_m18_01",
        12230: "FRPG_SfxBnd_m18_01",
        12238: "FRPG_SfxBnd_m18_01",
        12231: "FRPG_SfxBnd_m18_01",
    },
    2232: {
        12239: "FRPG_SfxBnd_m18_01",
        12232: "FRPG_SfxBnd_m18_01",
        12237: "FRPG_SfxBnd_m18_01",
        12238: "FRPG_SfxBnd_m18_01",
    },
    2240: {
        12242: "FRPG_SfxBnd_m14_01",
        12241: "FRPG_SfxBnd_m14_01",
        12240: "FRPG_SfxBnd_m14_01",
    },
    2250: {
        12258: "FRPG_SfxBnd_m18_00",
        1225000: "FRPG_SfxBnd_m18_00",
        12250: "FRPG_SfxBnd_m18_00",
    },
    2260: {
        12262: "FRPG_SfxBnd_m15",
        12261: "FRPG_SfxBnd_m15",
        12260: "FRPG_SfxBnd_m15",
    },
    2270: {},
    2280: {},
    2290: {},
    2300: {
        1223500: "FRPG_SfxBnd_m15",
        1223000: "FRPG_SfxBnd_m15",
        1223600: "FRPG_SfxBnd_m15",
        1223100: "FRPG_SfxBnd_m15",
        12304: "FRPG_SfxBnd_m15",
        12303: "FRPG_SfxBnd_m15",
        12305: "FRPG_SfxBnd_m15",
        12306: "FRPG_SfxBnd_m15",
    },
    2310: {
        1223200: "FRPG_SfxBnd_m11",
        1223300: "FRPG_SfxBnd_m11",
    },
    2320: {
        1222000: "FRPG_SfxBnd_m15_00",
        12320: "FRPG_SfxBnd_m15_00",
        12322: "FRPG_SfxBnd_m15_00",
        12325: "FRPG_SfxBnd_m15_00",
        12324: "FRPG_SfxBnd_m15_00",
        12321: "FRPG_SfxBnd_m15_00",
    },
    2330: {
        12330: "FRPG_SfxBnd_m12",
    },
    2360: {
        12364: "FRPG_SfxBnd_m15_01",
        12365: "FRPG_SfxBnd_m15_01",
        12360: "FRPG_SfxBnd_m15_01",
        12362: "FRPG_SfxBnd_m15_01",
        12363: "FRPG_SfxBnd_m15_01",
    },
    2370: {
        12373: "FRPG_SfxBnd_m17",
        12371: "FRPG_SfxBnd_m17",
        12370: "FRPG_SfxBnd_m17",
        12374: "FRPG_SfxBnd_m17",
        12372: "FRPG_SfxBnd_m17",
        12375: "FRPG_SfxBnd_m17",
        12376: "FRPG_SfxBnd_m17",
    },
    2380: {
        12383: "FRPG_SfxBnd_m12",
        12382: "FRPG_SfxBnd_m12",
        12380: "FRPG_SfxBnd_m12",
    },
    2390: {
        12390: "FRPG_SfxBnd_m18",
        12391: "FRPG_SfxBnd_m18",
        12392: "FRPG_SfxBnd_m18",
    },
    2400: {
        12522: "FRPG_SfxBnd_m15_01",
        12521: "FRPG_SfxBnd_m15_01",
        12520: "FRPG_SfxBnd_m15_01",
    },
    2410: {
        12411: "FRPG_SfxBnd_m15_01",
        12410: "FRPG_SfxBnd_m15_01",
    },
    2430: {
        12430: "FRPG_SfxBnd_m14_01",
    },
    2500: {
        12500: "FRPG_SfxBnd_m18_01",
    },
    2510: {},
    2520: {
        12522: "FRPG_SfxBnd_m15_01",
        12521: "FRPG_SfxBnd_m15_01",
        12520: "FRPG_SfxBnd_m15_01",
        12523: "FRPG_SfxBnd_m10_01",
    },
    2530: {
        12532: "FRPG_SfxBnd_m14",
        12531: "FRPG_SfxBnd_m14",
        12530: "FRPG_SfxBnd_m14",
    },
    2540: {
        12540: "FRPG_SfxBnd_m11",
    },
    2550: {},
    2560: {},
    2570: {},
    2590: {},
    2591: {},
    2600: {},
    2640: {
        12865: "FRPG_SfxBnd_m15_01",
    },
    2650: {
        12653: "FRPG_SfxBnd_m13",
        12651: "FRPG_SfxBnd_m13",
        12650: "FRPG_SfxBnd_m13",
        12654: "FRPG_SfxBnd_m13",
        12652: "FRPG_SfxBnd_m13",
    },
    2660: {
        12660: "FRPG_SfxBnd_m10_00",
        12661: "FRPG_SfxBnd_m10_00",
    },
    2670: {
        12672: "FRPG_SfxBnd_m16",
        12673: "FRPG_SfxBnd_m16",
        12671: "FRPG_SfxBnd_m16",
        12670: "FRPG_SfxBnd_m16",
        12674: "FRPG_SfxBnd_m16",
    },
    2680: {
        12672: "FRPG_SfxBnd_m16",
        12673: "FRPG_SfxBnd_m16",
        12681: "FRPG_SfxBnd_m16",
        12680: "FRPG_SfxBnd_m16",
        12682: "FRPG_SfxBnd_m16",
    },
    2690: {},
    2700: {
        12701: "FRPG_SfxBnd_m17",
        12700: "FRPG_SfxBnd_m17",
        12703: "FRPG_SfxBnd_m17",
        12702: "FRPG_SfxBnd_m17",
        12704: "FRPG_SfxBnd_m17",
    },
    2710: {
        12713: "FRPG_SfxBnd_m17",
        12714: "FRPG_SfxBnd_m17",
    },
    2711: {
        12710: "FRPG_SfxBnd_m17",
        12711: "FRPG_SfxBnd_m17",
        12712: "FRPG_SfxBnd_m17",
    },
    2730: {
        12730: "FRPG_SfxBnd_m11",
        12732: "FRPG_SfxBnd_m11",
        12733: "FRPG_SfxBnd_m11",
        1273000: "FRPG_SfxBnd_m11",
        1273100: "FRPG_SfxBnd_m11",
    },
    2731: {},
    2750: {
        12750: "FRPG_SfxBnd_m10_02",
    },
    2780: {
        12780: "FRPG_SfxBnd_m17",
    },
    2790: {},
    2791: {
        12790: "FRPG_SfxBnd_m18_00",
    },
    2792: {},
    2793: {},
    2794: {},
    2795: {},
    2800: {},
    2810: {},
    2811: {
        12812: "FRPG_SfxBnd_m14",
        12811: "FRPG_SfxBnd_m14",
        12810: "FRPG_SfxBnd_m14",
    },
    2820: {},
    2830: {
        12832: "FRPG_SfxBnd_m11",
        12831: "FRPG_SfxBnd_m11",
        12830: "FRPG_SfxBnd_m11",
    },
    2840: {
        12500: "FRPG_SfxBnd_m18_01",
        12849: "FRPG_SfxBnd_m11",
        12846: "FRPG_SfxBnd_m11",
        12841: "FRPG_SfxBnd_m11",
        12840: "FRPG_SfxBnd_m11",
        12843: "FRPG_SfxBnd_m11",
        12842: "FRPG_SfxBnd_m11",
        12844: "FRPG_SfxBnd_m11",
        12847: "FRPG_SfxBnd_m11",
    },
    2860: {
        12859: "FRPG_SfxBnd_m15_00",
        12865: "FRPG_SfxBnd_m15_01",
        12864: "FRPG_SfxBnd_m15_01",
    },
    2870: {
        12870: "FRPG_SfxBnd_m15_01",
        12872: "FRPG_SfxBnd_m15_01",
        12876: "FRPG_SfxBnd_m15_01",
        12873: "FRPG_SfxBnd_m15_01",
        12874: "FRPG_SfxBnd_m15_01",
        12875: "FRPG_SfxBnd_m15_01",
    },
    2900: {
        12900: "FRPG_SfxBnd_m13",
        4600: "FRPG_SfxBnd_m13",
        12901: "FRPG_SfxBnd_m13",
    },
    2910: {
        12914: "FRPG_SfxBnd_m13",
        12901: "FRPG_SfxBnd_m13",
        12911: "FRPG_SfxBnd_m13",
        12910: "FRPG_SfxBnd_m13",
    },
    2920: {
        12865: "FRPG_SfxBnd_m15_01",
    },
    2930: {},
    2940: {},
    2950: {},
    2960: {
        12960: "FRPG_SfxBnd_m13",
    },
    3090: {
        13090: "FRPG_SfxBnd_m14",
    },
    3110: {
        13110: "FRPG_SfxBnd_m17",
    },
    3200: {
        13200: "FRPG_SfxBnd_m10_00",
        13202: "FRPG_SfxBnd_m10_00",
        13201: "FRPG_SfxBnd_m10_00",
    },
    3210: {
        13211: "FRPG_SfxBnd_m14",
    },
    3220: {
        13090: "FRPG_SfxBnd_m14",
    },
    3230: {
        13232: "FRPG_SfxBnd_m17",
        13237: "FRPG_SfxBnd_m17",
        13235: "FRPG_SfxBnd_m17",
        13233: "FRPG_SfxBnd_m17",
        13234: "FRPG_SfxBnd_m17",
        13236: "FRPG_SfxBnd_m17",
        13238: "FRPG_SfxBnd_m17",
        13239: "FRPG_SfxBnd_m17",
        13228: "FRPG_SfxBnd_m17",
        13226: "FRPG_SfxBnd_m17",
        13227: "FRPG_SfxBnd_m17",
        13229: "FRPG_SfxBnd_m17",
    },
    3240: {
        13240: "FRPG_SfxBnd_m14_01",
        13242: "FRPG_SfxBnd_m14_01",
        13243: "FRPG_SfxBnd_m14_01",
    },
    3250: {
        13250: "FRPG_SfxBnd_m17",
    },
    3270: {
        13270: "FRPG_SfxBnd_m13_02",
        13271: "FRPG_SfxBnd_m13_02",
        13272: "FRPG_SfxBnd_m13_02",
    },
    3290: {
        1329000: "FRPG_SfxBnd_m14_00",
        13290: "FRPG_SfxBnd_m14_00",
        13292: "FRPG_SfxBnd_m14_00",
        13291: "FRPG_SfxBnd_m14_00",
    },
    3300: {
        13110: "FRPG_SfxBnd_m17",
    },
    3320: {
        13320: "FRPG_SfxBnd_m13_01",
        13325: "FRPG_SfxBnd_m13_01",
        13322: "FRPG_SfxBnd_m13_01",
        13321: "FRPG_SfxBnd_m13_01",
        13318: "FRPG_SfxBnd_m13_01",
        13326: "FRPG_SfxBnd_m13_01",
        13323: "FRPG_SfxBnd_m13_01",
        13319: "FRPG_SfxBnd_m13_01",
        13327: "FRPG_SfxBnd_m13_01",
        13314: "FRPG_SfxBnd_m13_01",
        13315: "FRPG_SfxBnd_m13_01",
        13328: "FRPG_SfxBnd_m13_01",
        13317: "FRPG_SfxBnd_m13_01",
        13316: "FRPG_SfxBnd_m13_01",
        13329: "FRPG_SfxBnd_m13_01",
    },
    3330: {
        13331: "FRPG_SfxBnd_m17",
        13330: "FRPG_SfxBnd_m17",
        13332: "FRPG_SfxBnd_m17",
    },
    3340: {},
    3341: {
        13341: "FRPG_SfxBnd_m14",
        13340: "FRPG_SfxBnd_m14",
    },
    3350: {},
    3370: {},
    3380: {
        13380: "FRPG_SfxBnd_m14",
    },
    3390: {
        13391: "FRPG_SfxBnd_m14",
        13390: "FRPG_SfxBnd_m14",
        13397: "FRPG_SfxBnd_m14",
        13396: "FRPG_SfxBnd_m14",
        13392: "FRPG_SfxBnd_m14",
        13395: "FRPG_SfxBnd_m14",
        13398: "FRPG_SfxBnd_m14",
        13399: "FRPG_SfxBnd_m14",
    },
    3400: {
        13400: "FRPG_SfxBnd_m14",
        13401: "FRPG_SfxBnd_m14",
        13402: "FRPG_SfxBnd_m14",
    },
    3410: {
        13411: "FRPG_SfxBnd_m12",
        1341100: "FRPG_SfxBnd_m12",
        1341200: "FRPG_SfxBnd_m12",
        13410: "FRPG_SfxBnd_m12",
    },
    3420: {
        13422: "FRPG_SfxBnd_m11",
        13423: "FRPG_SfxBnd_m11",
        16005: "FRPG_SfxBnd_m11",
        13421: "FRPG_SfxBnd_m16",
        13426: "FRPG_SfxBnd_m11",
        13427: "FRPG_SfxBnd_m11",
        13420: "FRPG_SfxBnd_m16",
        13428: "FRPG_SfxBnd_m11",
        13429: "FRPG_SfxBnd_m16",
        16006: "FRPG_SfxBnd_m16",
        16007: "FRPG_SfxBnd_m16",
        13424: "FRPG_SfxBnd_m11",
        16009: "FRPG_SfxBnd_m16",
        16013: "FRPG_SfxBnd_m16",
        16010: "FRPG_SfxBnd_m16",
        16011: "FRPG_SfxBnd_m16",
        16012: "FRPG_SfxBnd_m16",
    },
    3421: {
        1342000: "FRPG_SfxBnd_m14",
    },
    3422: {},
    3430: {
        15130: "FRPG_SfxBnd_m10_01",
        15131: "FRPG_SfxBnd_m10_01",
        15136: "FRPG_SfxBnd_m10_01",
        15135: "FRPG_SfxBnd_m10_01",
        15138: "FRPG_SfxBnd_m10_01",
        15143: "FRPG_SfxBnd_m10_01",
        15140: "FRPG_SfxBnd_m10_01",
        15141: "FRPG_SfxBnd_m10_01",
        15142: "FRPG_SfxBnd_m10_01",
        15151: "FRPG_SfxBnd_m10_01",
        15155: "FRPG_SfxBnd_m10_01",
        15163: "FRPG_SfxBnd_m10_01",
        15164: "FRPG_SfxBnd_m10_01",
        15167: "FRPG_SfxBnd_m10_01",
        15166: "FRPG_SfxBnd_m10_01",
        15170: "FRPG_SfxBnd_m10_01",
        15171: "FRPG_SfxBnd_m10_01",
        15174: "FRPG_SfxBnd_m10_01",
        15175: "FRPG_SfxBnd_m10_01",
        15148: "FRPG_SfxBnd_m10_01",
        15149: "FRPG_SfxBnd_m10_01",
        15147: "FRPG_SfxBnd_m10_01",
        15177: "FRPG_SfxBnd_m10_01",
        15176: "FRPG_SfxBnd_m13_02",
    },
    3431: {
        15176: "FRPG_SfxBnd_m13_02",
    },
    3440: {},
    3450: {
        13452: "FRPG_SfxBnd_m13_02",
        13453: "FRPG_SfxBnd_m13_02",
        13450: "FRPG_SfxBnd_m13_02",
        13451: "FRPG_SfxBnd_m13_02",
        15176: "FRPG_SfxBnd_m13_02",
    },
    3451: {},
    3460: {
        13461: "FRPG_SfxBnd_m17",
        13466: "FRPG_SfxBnd_m17",
        13462: "FRPG_SfxBnd_m17",
        13463: "FRPG_SfxBnd_m17",
        13460: "FRPG_SfxBnd_m17",
        13467: "FRPG_SfxBnd_m17",
        13464: "FRPG_SfxBnd_m17",
        13465: "FRPG_SfxBnd_m17",
        13468: "FRPG_SfxBnd_m17",
    },
    3461: {
        13461: "FRPG_SfxBnd_m17",
        13466: "FRPG_SfxBnd_m17",
        13462: "FRPG_SfxBnd_m17",
        13463: "FRPG_SfxBnd_m17",
        13460: "FRPG_SfxBnd_m17",
        13467: "FRPG_SfxBnd_m17",
        13464: "FRPG_SfxBnd_m17",
        13465: "FRPG_SfxBnd_m17",
        13468: "FRPG_SfxBnd_m17",
    },
    3470: {
        12304: "FRPG_SfxBnd_m15",
        12303: "FRPG_SfxBnd_m15",
    },
    3471: {},
    3472: {},
    3480: {
        13480: "FRPG_SfxBnd_m14_01",
        13481: "FRPG_SfxBnd_m14_01",
    },
    3490: {},
    3491: {},
    3500: {
        13501: "FRPG_SfxBnd_m16",
        13503: "FRPG_SfxBnd_m16",
        13500: "FRPG_SfxBnd_m16",
    },
    3501: {
        13507: "FRPG_SfxBnd_m16",
        13506: "FRPG_SfxBnd_m16",
        13509: "FRPG_SfxBnd_m16",
    },
    3510: {},
    3511: {},
    3520: {
        13522: "FRPG_SfxBnd_m16",
        13520: "FRPG_SfxBnd_m16",
        13521: "FRPG_SfxBnd_m16",
        13523: "FRPG_SfxBnd_m16",
    },
    3530: {
        13540: "FRPG_SfxBnd_m13_02",
        13537: "FRPG_SfxBnd_m13_02",
        13530: "FRPG_SfxBnd_m13_02",
        13533: "FRPG_SfxBnd_m13_02",
        13539: "FRPG_SfxBnd_m13_02",
        13536: "FRPG_SfxBnd_m13_02",
    },
    3531: {
        13541: "FRPG_SfxBnd_m13_02",
        13534: "FRPG_SfxBnd_m13_02",
    },
    4090: {
        14292: "FRPG_SfxBnd_m12_01",
        14291: "FRPG_SfxBnd_m12_01",
        14290: "FRPG_SfxBnd_m12_01",
    },
    4100: {},
    4110: {
        14110: "FRPG_SfxBnd_m12_01",
        14111: "FRPG_SfxBnd_m12_01",
        14112: "FRPG_SfxBnd_m12_01",
        14113: "FRPG_SfxBnd_m12_01",
        14114: "FRPG_SfxBnd_m12_01",
        14115: "FRPG_SfxBnd_m12_01",
    },
    4120: {
        1412100: "FRPG_SfxBnd_m12_01",
        1412000: "FRPG_SfxBnd_m12_01",
        12385: "FRPG_SfxBnd_m12_01",
        12384: "FRPG_SfxBnd_m12_01",
    },
    4130: {
        14230: "FRPG_SfxBnd_m12_01",
        14231: "FRPG_SfxBnd_m12_01",
        14232: "FRPG_SfxBnd_m12_01",
    },
    4140: {},
    4150: {
        14150: "FRPG_SfxBnd_m12_01",
    },
    4160: {
        14255: "FRPG_SfxBnd_m12_01",
        14251: "FRPG_SfxBnd_m12_01",
        14250: "FRPG_SfxBnd_m12_01",
        14256: "FRPG_SfxBnd_m12_01",
        14254: "FRPG_SfxBnd_m12_01",
        14252: "FRPG_SfxBnd_m12_01",
        14150: "FRPG_SfxBnd_m12_01",
    },
    4170: {
        14260: "FRPG_SfxBnd_m12_01",
        14261: "FRPG_SfxBnd_m12_01",
        14267: "FRPG_SfxBnd_m12_01",
        14278: "FRPG_SfxBnd_m12_01",
    },
    4171: {
        14270: "FRPG_SfxBnd_m12_01",
        14271: "FRPG_SfxBnd_m12_01",
        14268: "FRPG_SfxBnd_m12_01",
        14277: "FRPG_SfxBnd_m12_01",
    },
    4172: {
        14280: "FRPG_SfxBnd_m12_01",
        14281: "FRPG_SfxBnd_m12_01",
        14269: "FRPG_SfxBnd_m12_01",
        14277: "FRPG_SfxBnd_m12_01",
    },
    4180: {
        1412000: "FRPG_SfxBnd_m12_01",
        14181: "FRPG_SfxBnd_m12_01",
    },
    4190: {
        14190: "FRPG_SfxBnd_m12_01",
    },
    4500: {},
    4510: {
        14430: "FRPG_SfxBnd_m12_01",
        14412: "FRPG_SfxBnd_m12_01",
        14411: "FRPG_SfxBnd_m12_01",
        14410: "FRPG_SfxBnd_m12_01",
    },
    4511: {},
    4520: {
        14521: "FRPG_SfxBnd_m12_01",
        14522: "FRPG_SfxBnd_m12_01",
        14520: "FRPG_SfxBnd_m12_01",
    },
    4531: {
        15365: "FRPG_SfxBnd_m12_01",
        15364: "FRPG_SfxBnd_m12_01",
        15363: "FRPG_SfxBnd_m12",
    },
    5200: {
        15204: "FRPG_SfxBnd_m14_01",
        15208: "FRPG_SfxBnd_m14",
        15207: "FRPG_SfxBnd_m14",
        1520000: "FRPG_SfxBnd_m14",
        1520100: "FRPG_SfxBnd_m14",
        15205: "FRPG_SfxBnd_m14",
        15209: "FRPG_SfxBnd_m14",
        15203: "FRPG_SfxBnd_m14",
        15300: "FRPG_SfxBnd_m14",
        15202: "FRPG_SfxBnd_m14",
        15201: "FRPG_SfxBnd_m14",
        15200: "FRPG_SfxBnd_m14",
        15303: "FRPG_SfxBnd_m14",
        15302: "FRPG_SfxBnd_m14",
        15301: "FRPG_SfxBnd_m14",
        15304: "FRPG_SfxBnd_m14",
        15306: "FRPG_SfxBnd_m14",
        15307: "FRPG_SfxBnd_m14",
    },
    5201: {
        1520000: "FRPG_SfxBnd_m14",
        1520100: "FRPG_SfxBnd_m14",
        15306: "FRPG_SfxBnd_m14",
        15300: "FRPG_SfxBnd_m14",
    },
    5202: {
        1520000: "FRPG_SfxBnd_m14",
        1520100: "FRPG_SfxBnd_m14",
        15306: "FRPG_SfxBnd_m14",
    },
    5210: {
        15211: "FRPG_SfxBnd_m12",
        1521100: "FRPG_SfxBnd_m12",
        1521000: "FRPG_SfxBnd_m12",
        1521200: "FRPG_SfxBnd_m12",
        15210: "FRPG_SfxBnd_m12",
    },
    5220: {
        15220: "FRPG_SfxBnd_m13",
        15221: "FRPG_SfxBnd_m13",
        15225: "FRPG_SfxBnd_m13",
        15223: "FRPG_SfxBnd_m13",
        15228: "FRPG_SfxBnd_m13",
        15229: "FRPG_SfxBnd_m13",
        15227: "FRPG_SfxBnd_m13",
        17222: "FRPG_SfxBnd_m13",
        17220: "FRPG_SfxBnd_m13",
        17225: "FRPG_SfxBnd_m13",
        17221: "FRPG_SfxBnd_m13",
        17223: "FRPG_SfxBnd_m13",
        17224: "FRPG_SfxBnd_m13",
        17226: "FRPG_SfxBnd_m13",
        15226: "FRPG_SfxBnd_m13",
    },
    5230: {
        15233: "FRPG_SfxBnd_m14",
        15236: "FRPG_SfxBnd_m14_01",
        15234: "FRPG_SfxBnd_m14_01",
        15232: "FRPG_SfxBnd_m14_01",
    },
    5231: {
        15233: "FRPG_SfxBnd_m14",
        15234: "FRPG_SfxBnd_m14_01",
    },
    5240: {},
    5250: {
        15252: "FRPG_SfxBnd_m14_01",
        15248: "FRPG_SfxBnd_m14_01",
        1525000: "FRPG_SfxBnd_m14_01",
        15258: "FRPG_SfxBnd_m14_01",
        15257: "FRPG_SfxBnd_m14_01",
        15250: "FRPG_SfxBnd_m14_01",
        15254: "FRPG_SfxBnd_m14_01",
        15249: "FRPG_SfxBnd_m14_01",
        15242: "FRPG_SfxBnd_m14_01",
        15247: "FRPG_SfxBnd_m14_01",
        15246: "FRPG_SfxBnd_m14_01",
        15256: "FRPG_SfxBnd_m14_01",
        15259: "FRPG_SfxBnd_m14_01",
    },
    5260: {
        1526000: "FRPG_SfxBnd_m10_00",
        1526100: "FRPG_SfxBnd_m10_00",
        15262: "FRPG_SfxBnd_m10_00",
        15263: "FRPG_SfxBnd_m10_00",
        15264: "FRPG_SfxBnd_m10_00",
        15260: "FRPG_SfxBnd_m10_00",
        15261: "FRPG_SfxBnd_m10_00",
        15510: "FRPG_SfxBnd_m10_00",
    },
    5261: {
        15510: "FRPG_SfxBnd_m10_00",
    },
    5270: {
        15276: "FRPG_SfxBnd_m15_01",
        15273: "FRPG_SfxBnd_m15_01",
        15244: "FRPG_SfxBnd_m15_01",
        15243: "FRPG_SfxBnd_m15_01",
        15270: "FRPG_SfxBnd_m15_01",
    },
    5271: {
        15274: "FRPG_SfxBnd_m15_01",
        15275: "FRPG_SfxBnd_m15_01",
        15276: "FRPG_SfxBnd_m15_01",
        15279: "FRPG_SfxBnd_m15_01",
        15278: "FRPG_SfxBnd_m15_01",
        15272: "FRPG_SfxBnd_m15_01",
        15271: "FRPG_SfxBnd_m15_01",
        15277: "FRPG_SfxBnd_m15_01",
        15269: "FRPG_SfxBnd_m15_01",
        15267: "FRPG_SfxBnd_m15_01",
        15268: "FRPG_SfxBnd_m15_01",
        15245: "FRPG_SfxBnd_m15_01",
    },
    5280: {
        15286: "FRPG_SfxBnd_m14_00",
        15287: "FRPG_SfxBnd_m14_00",
        16001: "FRPG_SfxBnd_m14_00",
        15280: "FRPG_SfxBnd_m14_00",
        16000: "FRPG_SfxBnd_m14_00",
        15281: "FRPG_SfxBnd_m14_00",
        15282: "FRPG_SfxBnd_m14_00",
        15289: "FRPG_SfxBnd_m14_00",
        15283: "FRPG_SfxBnd_m14_00",
        16003: "FRPG_SfxBnd_m14_00",
        15288: "FRPG_SfxBnd_m14_00",
        15285: "FRPG_SfxBnd_m14_00",
        15284: "FRPG_SfxBnd_m14_00",
    },
    5290: {
        15299: "FRPG_SfxBnd_m17",
        15290: "FRPG_SfxBnd_m17",
        15294: "FRPG_SfxBnd_m17",
        15297: "FRPG_SfxBnd_m17",
        15904: "FRPG_SfxBnd_m17",
        15293: "FRPG_SfxBnd_m17",
        15298: "FRPG_SfxBnd_m17",
        15903: "FRPG_SfxBnd_m17",
        15905: "FRPG_SfxBnd_m17",
    },
    5291: {
        15903: "FRPG_SfxBnd_m17",
    },
    5300: {
        15308: "FRPG_SfxBnd_m18",
        15309: "FRPG_SfxBnd_m18",
    },
    5310: {
        15310: "FRPG_SfxBnd_m15_01",
        15311: "FRPG_SfxBnd_m15_01",
    },
    5320: {
        15321: "FRPG_SfxBnd_m15_01",
        15320: "FRPG_SfxBnd_m15_01",
        15322: "FRPG_SfxBnd_m15_01",
        15326: "FRPG_SfxBnd_m15_01",
        15325: "FRPG_SfxBnd_m15_01",
        15324: "FRPG_SfxBnd_m15_01",
        15327: "FRPG_SfxBnd_m15_01",
        15329: "FRPG_SfxBnd_m15_01",
        15328: "FRPG_SfxBnd_m15_01",
    },
    5330: {},
    5340: {},
    5350: {
        15369: "FRPG_SfxBnd_m15_01",
        15351: "FRPG_SfxBnd_m15_01",
        15350: "FRPG_SfxBnd_m15_01",
        15358: "FRPG_SfxBnd_m15_01",
        15354: "FRPG_SfxBnd_m15_01",
        15359: "FRPG_SfxBnd_m15_01",
        15355: "FRPG_SfxBnd_m15_01",
        15353: "FRPG_SfxBnd_m15_01",
        41100: "FRPG_SfxBnd_m10_01",
        15368: "FRPG_SfxBnd_m15_01",
    },
    5351: {
        15369: "FRPG_SfxBnd_m15_01",
        15351: "FRPG_SfxBnd_m15_01",
        15348: "FRPG_SfxBnd_m15_01",
        15347: "FRPG_SfxBnd_m15_01",
        15355: "FRPG_SfxBnd_m15_01",
        15368: "FRPG_SfxBnd_m15_01",
    },
    5352: {
        15368: "FRPG_SfxBnd_m15_01",
    },
    5353: {
        15368: "FRPG_SfxBnd_m15_01",
    },
    5360: {
        15360: "FRPG_SfxBnd_m12",
        15361: "FRPG_SfxBnd_m12",
    },
    5361: {
        15363: "FRPG_SfxBnd_m12",
    },
    5370: {
        15371: "FRPG_SfxBnd_m18_00",
        15373: "FRPG_SfxBnd_m18_00",
        15375: "FRPG_SfxBnd_m18_00",
        15374: "FRPG_SfxBnd_m18_00",
    },
    5390: {
        15403: "FRPG_SfxBnd_m16",
        15388: "FRPG_SfxBnd_m16",
        15389: "FRPG_SfxBnd_m16",
        15398: "FRPG_SfxBnd_m16",
        15395: "FRPG_SfxBnd_m16",
        15391: "FRPG_SfxBnd_m16",
        15390: "FRPG_SfxBnd_m16",
        15401: "FRPG_SfxBnd_m16",
        15400: "FRPG_SfxBnd_m16",
        15402: "FRPG_SfxBnd_m16",
        15404: "FRPG_SfxBnd_m16",
    },
    5400: {
        15410: "FRPG_SfxBnd_m14_01",
        15419: "FRPG_SfxBnd_m14_01",
        15417: "FRPG_SfxBnd_m14_01",
        15418: "FRPG_SfxBnd_m14_01",
        15421: "FRPG_SfxBnd_m14_01",
        15422: "FRPG_SfxBnd_m14_01",
        15412: "FRPG_SfxBnd_m14_01",
        15411: "FRPG_SfxBnd_m14_01",
        15414: "FRPG_SfxBnd_m14_01",
        15423: "FRPG_SfxBnd_m14_01",
        15416: "FRPG_SfxBnd_m14_01",
        15415: "FRPG_SfxBnd_m14_01",
    },
    5401: {
        15425: "FRPG_SfxBnd_m14_01",
        15424: "FRPG_SfxBnd_m14_01",
    },
}


_BLOCK_FFXBND_RE = re.compile(r"FRPG_SfxBnd_m(\d\d)_(\d\d)\.ffxbnd(\.dcx)?$")

_FFX_STEM_MATCH = re.compile(r"f(\d+)")  # typically 7 digits
_FLVER_STEM_MATCH = re.compile(r"s(\d+)")  # typically 5 digits
_TPF_STEM_MATCH = re.compile(r"s(\d+)(_n|_s|_h)?")  # typically 5 digits


class FFXBND(Binder):
    """Manages the structure of an FFXBND containing FFX, FLVER, and TPF files for visual effects.

    Does not currently read FFX files. FLVER and TPF files probably rarely need use.
    """

    EXT: tp.ClassVar[str] = ".ffxbnd"
    NAME_PREFIX: tp.ClassVar[str] = "FRPG_SfxBnd_"

    def get_ffx_entries(self) -> list[BinderEntry]:
        return [entry for entry in self.entries if entry.entry_id < 100000]

    def get_ffx_entries_by_ffx_id(self) -> dict[int, BinderEntry]:
        return {
            int(entry.minimal_stem[1:]): entry
            for entry in self.entries
            if entry.entry_id < 100000
        }

    def get_tpf_entries(self) -> list[BinderEntry]:
        return [entry for entry in self.entries if 100000 <= entry.entry_id < 200000]

    def get_tpf_entries_by_tpf_id(self) -> dict[int, BinderEntry]:
        return {
            int(entry.minimal_stem[1:]): entry
            for entry in self.entries
            if 100000 <= entry.entry_id < 200000
        }

    def get_flver_entries(self) -> list[BinderEntry]:
        return [entry for entry in self.entries if entry.entry_id >= 200000]

    def get_flver_entries_by_flver_id(self) -> dict[int, BinderEntry]:
        return {
            int(entry.minimal_stem[1:]): entry
            for entry in self.entries
            if entry.entry_id >= 200000
        }

    def entry_autogen(self):
        """Sort and change the IDs of all entries depending on their type (FFX, TPF, or FLVER), and raise an error if
        any other entry types exist, or if any entry names are invalid.

        Any extra '_*' suffixes in the stems of FFX and FLVER entry names will be stripped. For TPF files, the suffices
        '_n', '_s', and '_h' are permitted. Any other '_*' suffices, or suffices that come after an allowed suffix (e.g.
        's12345_n_MyInfo.tpf'), will be stripped.
        """

        ffx_entries = []
        tpf_entries = []
        flver_entries = []

        for entry in self.entries:
            suffix = entry.suffix
            match suffix:
                case ".ffx":
                    ffx_stem = entry.minimal_stem.split("_")[0]
                    if not _FFX_STEM_MATCH.match(ffx_stem):
                        raise ValueError(f"FFX entry name '{entry.name}' does not match expected format.")
                    entry.set_path_name(f"f{int(ffx_stem[1:]):07d}.ffx")
                    ffx_entries.append(entry)
                case ".tpf":
                    tpf_stem = entry.minimal_stem
                    # Requires more careful suffix stripping.
                    parts = tpf_stem.split("_")
                    if len(parts) >= 2:
                        if parts[1] in ("n", "s", "h"):
                            tpf_stem = f"{parts[0]}_{parts[1]}"
                        else:
                            tpf_stem = parts[0]  # strip unknown suffix
                    if not _TPF_STEM_MATCH.match(tpf_stem):
                        raise ValueError(f"TPF entry name '{entry.name}' does not match expected format.")
                    # Split again to properly format name ID.
                    if "_" in tpf_stem:
                        parts = tpf_stem.split("_")
                        tpf_stem = f"s{int(parts[0][1:]):05d}_{parts[1]}"
                    else:
                        tpf_stem = f"s{int(tpf_stem[1:]):05d}"
                    entry.set_path_name(f"{tpf_stem}.tpf")
                    tpf_entries.append(entry)
                case ".flver":
                    flver_stem = entry.minimal_stem.split("_")[0]
                    if not _FLVER_STEM_MATCH.match(flver_stem):
                        raise ValueError(f"FLVER entry name '{entry.name}' does not match expected format.")
                    entry.set_path_name(f"s{int(flver_stem[1:]):05d}.flver")
                    flver_entries.append(entry)
                case _:
                    raise ValueError(
                        f"Entry '{entry.name}' has an invalid extension for an FFXBND. Should be '.ffx', '.tpf', "
                        f"or '.flver'."
                    )

        ffx_entries = sorted(ffx_entries, key=lambda e: int(e.minimal_stem[1:]))
        tpf_entries = sorted(tpf_entries, key=lambda e: int(e.minimal_stem[1:].split("_")[0]))
        flver_entries = sorted(flver_entries, key=lambda e: int(e.minimal_stem[1:]))

        for i, ffx_entry in enumerate(ffx_entries):
            ffx_entry.entry_id = i
        for i, tpf_entry in enumerate(tpf_entries):
            tpf_entry.entry_id = 100000 + i
        for i, flver_entry in enumerate(flver_entries):
            flver_entry.entry_id = 200000 + i

        self.entries = ffx_entries + tpf_entries + flver_entries

    def support_msb(
        self,
        msb: MSB | None,
        ffx_search_directories: tp.Sequence[Path] | Path,
        required_ffx_id_overrides: dict[int, list[int]] = None,
        remapped_character_ffx_sources: dict[int, int | None] = None,
        ignore_if_in_ffxbnds: tp.Sequence[FFXBND] | FFXBND = None,
        prefer_ffxbnd_bak=True,
    ):
        """Iterate over all character models and VFX events in given `msb` and ensure all their FFX files (including
        FLVER and TPF files) are present in this `FFXBND`, as understood by the `DEFAULT_REQUIRED_FFX_IDS` dictionary
        mapping character models to all of their required FFX IDs.

        Missing files will be searched for in several locations across `ffx_search_directories`, in the order below.
        Note that this search is 'breath-first' across the given directories, so we search all of them for character
        subfolders, then search all of them for loose files, etc.:
            - Character subfolder loose files in any of the given directories, e.g. '{dir}/c1234/f00001234.ffx'.
            - Loose files in any of the given directories, e.g. '{dir}/f00001234.ffx'.
            - The FFXBND file source given in `CHARACTER_FFX_SOURCES` for that character model and FFX ID.
            - *Any* FFXBND file in the given directories that contains the required FFX ID (searched alphabetically).

        If a required file is not found in any of the above locations, an error will be raised.

        Any character model keys given in `required_ffx_id_overrides` will be used instead of that key in
        `DEFAULT_REQUIRED_FFX_IDS`. This is useful for modded characters that use different effect IDs. Note that the
        full list of IDs must be given; it will not be merged with the default list for that character.

        There is currently no built-in way to detect whether a given FFX ID should expect a FLVER and/or TPF file to
        accompany it. These extra files will simply be used if they are found in the same location as the FFX ID (i.e.
        as a loose file next to it, or in the same FFXBND). No error will be raised if they are missing, as most FFXs
        do not use them. The user should ensure that these files are kept with their FFX when required.

        Args:
            msb (MSB): MSB structure to check.
            ffx_search_directories (list[Path], optional): path(s) to directory containing character subfolders
                with loose files, loose files directly, or FFXBND files to search for missing FFX/FLVER/TPF files in.
            required_ffx_id_overrides: optional dictionary mapping character model IDs to lists of FFX IDs that should
                be used instead of the default list in `DEFAULT_REQUIRED_FFX_IDS`. This is necessary for any new
                character models in the MSB, unless that model appears in `remapped_character_ffx_sources` below.
            remapped_character_ffx_sources: optional dictionary mapping new character model IDs to IDs that should be
                used instead for finding required FFX IDs or default FFXBND sources. This is useful for characters that
                are just reskins of existing characters and should use the same effects.
            ignore_if_in_ffxbnds (list[FFXBND] or FFXBND, optional): any FFXBNDs given here will be checked to see if
                they already contain each required FFX ID. If they do, that FFX ID will not be checked in this FFXBND.
                (It may already exist and will be left alone.) This is useful for checking 'CommonEffects' and/or
                checking the 'mAA' FFXBND before adding an FFX to 'mAA_BB'.
            prefer_ffxbnd_bak (bool): if True (default), look for '.bak' backup versions of FFXBND files (NOT loose
                files) first, in case the FFXBNDs have been modded and some vanilla FFX entries removed.
        """
        if isinstance(ffx_search_directories, (str, Path)):
            ffx_search_directories = [ffx_search_directories]
        if not ffx_search_directories:
            raise ValueError("No FFX search directories given.")
        ffx_search_directories = [Path(d) for d in ffx_search_directories]

        required_ffx_id_overrides = required_ffx_id_overrides or {}
        remapped_character_ffx_sources = remapped_character_ffx_sources or {}
        if isinstance(ignore_if_in_ffxbnds, Binder):
            ignore_if_in_ffxbnds = [ignore_if_in_ffxbnds]
        elif ignore_if_in_ffxbnds is None:
            ignore_if_in_ffxbnds = []

        # NOTE: Entries found in other FFXBNDs will have their IDs changed in this FFXBND, but as we are only opening
        # other FFXBNDs temporarily in this method, we don't both copying the entries.
        opened_ffxbnd_paths = set()
        opened_ffx_entries = {}
        opened_tpf_entries = {}
        opened_flver_entries = {}

        # First, find any IDs that already exist in this FFXBND or another given one.
        # We will also add to this list as we find required IDs and add their entries.
        existing_ffx_ids = set(self.get_ffx_entries_by_ffx_id())
        existing_tpf_ids = set(self.get_tpf_entries_by_tpf_id())
        existing_flver_ids = set(self.get_flver_entries_by_flver_id())
        for ffxbnd in ignore_if_in_ffxbnds:
            existing_ffx_ids |= set(ffxbnd.get_ffx_entries_by_ffx_id())
            existing_tpf_ids |= set(ffxbnd.get_tpf_entries_by_tpf_id())
            existing_flver_ids |= set(ffxbnd.get_flver_entries_by_flver_id())

        def find_ffx_id(_ffx_id: int, _chr_id: int) -> BinderEntry | Path | None:
            if _ffx_id in existing_ffx_ids:
                return None

            # TODO: This is currently depth-first in each folder, not breadth-first.
            for search_dir in ffx_search_directories:

                # 1. Search character subfolder.
                chr_subdir = Path(search_dir, f"c{_chr_id:04d}")
                if chr_subdir.is_dir():
                    for ffx_file in chr_subdir.glob("f*.ffx"):
                        try:
                            check_id = int(ffx_file.stem.split("_")[0][1:])
                        except ValueError:
                            pass
                        else:
                            if check_id == _ffx_id:
                                return ffx_file

                # 2. Search loose files.
                for ffx_file in search_dir.glob("f*.ffx"):
                    try:
                        check_id = int(ffx_file.stem.split("_")[0][1:])
                    except ValueError:
                        pass
                    else:
                        if check_id == _ffx_id:
                            return ffx_file

                # 3. Search known FFXBND. TODO: No DCX for PTDE.
                try:
                    known_ffxbnd_stem = DEFAULT_CHARACTER_FFX_SOURCES[_chr_id][_ffx_id]
                except KeyError:
                    _LOGGER.warning(f"No known FFXBND source for character {_chr_id} and FFX ID {_ffx_id}.")
                    pass  # will just check all FFXBNDs
                else:
                    known_ffxbnd_path = search_dir / f"{known_ffxbnd_stem}.ffxbnd.dcx"
                    if prefer_ffxbnd_bak:
                        if (bak_path := known_ffxbnd_path.with_suffix(known_ffxbnd_path.suffix + ".bak")).is_file():
                            known_ffxbnd_path = bak_path
                    if known_ffxbnd_path in opened_ffxbnd_paths:
                        continue
                    else:
                        if known_ffxbnd_path.is_file():
                            _ffxbnd = FFXBND.from_path(known_ffxbnd_path)
                            opened_ffxbnd_paths.add(known_ffxbnd_path)
                            opened_ffx_entries.update(_ffxbnd.get_ffx_entries_by_ffx_id())

                if _ffx_id in opened_ffx_entries:
                    return opened_ffx_entries[_ffx_id]

                # 4. Search all FFXBNDs.
                for ffxbnd_path in search_dir.glob("*.ffxbnd.dcx"):
                    if prefer_ffxbnd_bak:
                        if (bak_path := ffxbnd_path.with_suffix(ffxbnd_path.suffix + ".bak")).is_file():
                            ffxbnd_path = bak_path
                    if ffxbnd_path in opened_ffxbnd_paths:
                        continue
                    _ffxbnd = FFXBND.from_path(ffxbnd_path)
                    opened_ffxbnd_paths.add(ffxbnd_path)
                    opened_ffx_entries.update(_ffxbnd.get_ffx_entries_by_ffx_id())
                    if _ffx_id in opened_ffx_entries:
                        return opened_ffx_entries[_ffx_id]

            return None

        for character in msb.characters:
            character_id = int(character.name[1:])

            if character_id in remapped_character_ffx_sources:
                character_id = remapped_character_ffx_sources[character_id]

            if character_id in required_ffx_id_overrides:
                required_ffx_ids = required_ffx_id_overrides[character_id]
            else:
                try:
                    required_ffx_ids = DEFAULT_REQUIRED_FFX_IDS
                except KeyError:
                    raise KeyError(
                        f"Character ID {character_id} not found in DEFAULT_REQUIRED_FFX_IDS and no override "
                        f"required IDs were given."
                    )

            for required_ffx_id in required_ffx_ids:
                if required_ffx_id in existing_ffx_ids:
                    continue

                ffx_source = find_ffx_id(required_ffx_id, character_id)

                if ffx_source is None:
                    raise FileNotFoundError(
                        f"Required FFX file not found for character {character_id} and FFX ID {required_ffx_id}."
                    )
                elif isinstance(ffx_source, Path):
                    # Create new entry from loose file.
                    ffx_entry = BinderEntry(
                        data=ffx_source.read_bytes(),
                        entry_id=len(self.get_ffx_entries()),  # will be set properly on FFXBND write
                        path=f"N:\\FRPG\\data\\Sfx\\OutputData\\Main\\Effect_x64\\{ffx_source.name}",
                        # Default flags (0x2).
                    )
                    self.add_entry(ffx_entry)
                else:  # BinderEntry
                    # We don't copy the entry.
                    self.add_entry(ffx_source)

            # TODO: Haven't mapped out required FLVERs and TPFs.
