__all__ = [
    "CHARACTER_MODELS",
    "UNUSED_CHARACTERS",
    "WEAPON_MODELS",
    "BONFIRE_ESDS",
    "FOG_WALL_MODELS",
    "BEHAVIOR_SUB_ID",
    "PLAYER_WEAPON_BEHAVIOR_VARIATIONS",
    "HAS_ONE_HANDED_SPECIAL_ATTACK",
    "HAS_TWO_HANDED_SPECIAL_ATTACK",
    "SPECIAL_EFFECT_RANGES",
    "OBJECT_POSES",
    "HELLKITE_BRIDGE_FIRE_FFX",
]

CHARACTER_MODELS = {
    0: "Player Character",
    1000: "Empty Character",  # e.g. bonfires
    1200: "Large Rat",
    1201: "Small Rat",
    1202: "Giant Rat",
    1203: "Snow Rat",
    2060: "Infested Ghoul",
    2220: "Unused Knight (DSR)",
    2230: "Stray Demon",
    2231: "Demon Firesage",
    2232: "Asylum Demon",
    2239: "Stray/Asylum Demon (textures)",  # has skin textures used by both c2230 and c2232
    2240: "Capra Demon",
    2250: "Taurus Demon",
    2260: "Batwing Demon",
    2270: "Mushroom Parent",
    2280: "Mushroom Child",
    2290: "Chained Prisoner (unused)",
    2300: "Titanite Demon",
    2310: "Crow Demon",
    2320: "Iron Golem",
    2330: "Demonic Foliage",
    2360: "Executioner Smough",  # both versions
    2370: "Channeler",
    2380: "Stone Knight",
    2390: "Darkwraith",
    2400: "Painting Guardian",
    2410: "Silver Knight",
    2430: "Demonic Statue",
    2500: "Hollow",
    2509: "Hollow (textures only)",
    2510: "Undead Merchant",  # both genders
    2511: "Undead Merchant (unused)",
    2519: "Undead Merchant (textures only)",
    2520: "Hollow Assassin",
    2530: "Blowdart Sniper",
    2540: "Hollow Warrior",
    2550: "Hollow Soldier",
    2560: "Balder Knight",
    2570: "Berenike Knight",
    2590: "Marvelous Chester (unused 1)",
    2591: "Marvelous Chester (unused 2)",
    2600: "Young Witch Beatrice (unused)",
    2640: "Andre",
    2650: "Necromancer",
    2660: "Butcher",
    2670: "Ghost (Male)",
    2680: "Ghost (Female)",
    2690: "Serpent Soldier",
    2700: "Serpent Mage",
    2710: "Crystal Golem",
    2711: "Golden Crystal Golem",
    2730: "Crossbreed Priscilla",
    2731: "Crossbreed Priscilla (tail)",
    2750: "Anastacia",
    2780: "Mimic",
    2790: "Black Knight (All Weapons)",  # contains all four weapon models and animation sets
    2791: "Black Knight (Ghost)",  # textured all white
    2792: "Black Knight (Sword Only)",
    2793: "Black Knight (Greatsword Only)",
    2794: "Black Knight (Greataxe Only)",
    2795: "Black Knight (Halberd Only)",
    2800: "Undead Crystal Soldier",
    2810: "Infested Barbarian (club)",
    2811: "Infested Barbarian (boulder)",
    2820: "Spider Hollow (unused)",
    2830: "Phalanx",
    2840: "Engorged Hollow",
    2860: "Giant",
    2870: "Sentinel",  # includes Royal Sentinel
    2900: "Skeleton",
    2910: "Giant Skeleton",
    2920: "Vamos",
    2930: "Bonewheel Skeleton",
    2940: "Skeleton Baby",
    2950: "Skeleton Beast",
    2960: "Bone Tower",
    3090: "Giant Mosquito",
    3110: "Crystal Lizard (unused)",  # from Demon's Souls
    3200: "Slime",
    3210: "Egg Carrier",
    3220: "Vile Maggot",
    3230: "Moonlight Butterfly",
    3240: "Chaos Eater",
    3250: "Man-Eater Shell",
    3270: "Basilisk",
    3290: "Brain Bug (unused)",
    3300: "Crystal Lizard",
    3320: "Pinwheel",
    3330: "Pisaca",
    3340: "Attack Dog",
    3341: "Flaming Attack Dog",
    3350: "Possessed Tree",
    3370: "Tree Lizard",
    3380: "Giant Leech",
    3390: "Burrowing Rockworm",
    3400: "Cragspider",
    3410: "Frog-Ray",
    3420: "Undead Dragon",
    3421: "Bounding Demon",  # aka Undead Dragon (legs)
    3422: "Undead Dragon (wing)",
    3430: "Hellkite Dragon",
    3431: "Hellkite Dragon (tail)",
    3440: "Black Dragon Kalameet (unused)",
    3450: "Everlasting Dragon",
    3451: "Everlasting Dragon (tail)",
    3460: "Armored Tusk",
    3461: "Armored Tusk (rear guard)",
    3470: "Sanctuary Guardian (unused)",
    3471: "Sanctuary Guardian",
    3472: "Sanctuary Guardian (tail)",
    3480: "Chaos Bug",
    3490: "Good Vagrant",
    3491: "Evil Vagrant",
    3500: "Mass of Souls",
    3501: "Wisp",
    3510: "Giant Crow",
    3511: "Giant Crow (cutscene)",
    3520: "Drake",
    3530: "Hydra",
    3531: "Hydra (head)",
    4090: "Marvelous Chester",
    4091: "Marvelous Chester (unused 3)",
    4095: "Marvelous Chester (unused 4)",
    4100: "Artorias",
    4110: "Hawkeye Gough",
    4120: "Stone Guardian",
    4130: "Scarecrow",
    4140: "Elizabeth",
    4150: "Bloathead",
    4160: "Bloathead Sorcerer",
    4170: "Humanity Phantom (large)",
    4171: "Humanity Phantom (medium)",
    4172: "Humanity Phantom (small)",
    4180: "Chained Prisoner",
    4190: "Abyss Attack Dog",
    4500: "Manus",
    4510: "Black Dragon Kalameet",
    4511: "Black Dragon Kalameet (tail)",
    4520: "Young Sif",
    4530: "Young Alvina (unused)",
    4531: "Young Alvina",
    5200: "Centipede Demon",
    5201: "Centipede Demon (arm)",
    5202: "Centipede Demon (tail)",
    5210: "Sif",
    5220: "Gravelord Nito",
    5230: "Bed of Chaos",
    5231: "Bed of Chaos (unused)",  # incomplete mobile version
    5240: "Parasitic Wall Hugger",
    5250: "Ceaseless Discharge",
    5260: "Gaping Dragon",
    5261: "Gaping Dragon (tail)",
    5270: "Ornstein",
    5271: "Giant Ornstein",
    5280: "Quelaag",
    5290: "Seath the Scaleless",
    5291: "Seath the Scaleless (tail)",
    5300: "Undead King Jareel",  # incomplete New Londo Ruins boss
    5310: "Gwynevere",
    5320: "Gwyndolin",
    5330: "Primordial Serpent",  # Frampt / Kaathe
    5340: "Fair Lady",  # aka Daughter of Chaos, aka Quelaag's Sister
    5350: "Bell Gargoyle",
    5351: "Lightning Gargoyle",
    5352: "Bell Gargoyle (tail)",
    5353: "Lightning Gargoyle (tail)",
    5360: "Great Feline",
    5361: "Alvina",
    5362: "Alvina (unused)",
    5370: "Gwyn",
    5390: "Four Kings",
    5400: "Bed of Chaos (spirit)",
    5401: "Bed of Chaos (bug)",
}

UNUSED_CHARACTERS = (
    2511,  # Undead Merchant prototype?
    2590,  # Marvelous Chester (1)
    2591,  # Marvelous Chester (2)
    2600,  # Young Witch Beatrice
    2290,  # Chained Prisoner prototype
    3110,  # Crystal Lizard prototype
    3290,  # Brain Bug
    3440,  # Kalameet prototype
    3470,  # Sanctuary Guardian prototype
    3472,  # Sanctuary Guardian prototype (2)
    4091,  # Marvelous Chester prototype (3)
    4095,  # Marvelous Chester prototype (4)
    4530,  # Young Alvina
    5231,  # Bed of Chaos (mobile)
    5300,  # Jar Eel
    5362,  # Alvina prototype
)


WEAPON_MODELS = {
    # Daggers (9)
    100: "Dagger",
    101: "Bandit's Knife",
    103: "Ghost Blade",
    104: "Priscilla's Dagger",
    107: "Parrying Dagger",
    111: "Dark Silver Tracer",
    # Straight Swords (14)
    200: "Broken Straight Sword",
    201: "Longsword",
    202: "Balder Side Sword",
    203: "Crystal Straight Sword",
    204: "Broadsword",
    207: "Shortsword",
    212: "Silv. Knight Str. Sword",
    231: "Sunlight Straight Sword",
    259: "Black Knight Sword",
    260: "Darksword",
    264: "Barbed Straight Sword",
    271: "Astora's Straight Sword",
    272: "Straight Sword Hilt",
    291: "Drake Sword",
    # Greatswords (12)
    206: "Bastard Sword",
    210: "Man-serpent Greatsword",
    211: "Flamberge",
    220: "Stone Greatsword",
    240: "Obsidian Greatsword",
    258: "Moonlight Greatsword",
    263: "Crystal Greatsword",
    266: "Claymore",
    267: "Greatsword of Artorias",  # (True)
    268: "Great Lord Greatsword",
    269: "Greatsword of Artorias (Cursed)",
    274: "Abyss Greatsword",
    # Ultra Greatswords (5)
    208: "Zweihander",
    221: "Black Knight Greatsword",
    251: "Greatsword",
    270: "Demon Great Machete",
    281: "Dragon Greatsword",
    # Curved Greatswords (2)
    280: "Server",
    282: "Gravelord Sword",
    284: "Murakumo",
    # Thrusting Swords (5)
    106: "Mail Breaker",
    230: "Velka's Rapier",
    300: "Rapier",
    301: "Estoc",
    302: "Ricard's Rapier",
    # Curved Swords (7)
    102: "Jagged Ghost Blade",
    110: "Gold Tracer",
    213: "Quelaag's Furysword",
    400: "Scimitar",
    401: "Falchion",
    403: "Shotel",
    406: "Painting Guardian Sword",
    # Katanas (4)
    402: "Uchigatana",
    450: "Washing Pole",
    451: "Chaos Blade",
    452: "Iaito",
    # Axes (6)
    252: "Butcher Knife",
    502: "Hand Axe",
    503: "Crescent Axe",
    505: "Battle Axe",
    508: "Golem Axe",
    509: "Gargoyle Tail Axe",
    # Greataxes (5)
    504: "Greataxe",
    506: "Dragon King Greataxe",
    507: "Black Knight Greataxe",
    510: "Stone Greataxe",
    651: "Demon's Greataxe",
    # Hammers (9)
    600: "Club",
    602: "Reinforced Club",
    603: "Morning Star",
    604: "Warpick",
    605: "Pickaxe",
    606: "Mace",
    656: "Blacksmith Hammer",
    657: "Blacksmith Giant Hammer",
    658: "Hammer of Vamos",
    # Great Hammers (6)
    607: "Great Club",
    608: "Grant",
    652: "Smough's Hammer",
    654: "Demon's Great Hammer",
    655: "Dragon Tooth",
    659: "Large Club",
    # Spears (10)
    700: "Spear",
    702: "Winged Spear",
    703: "Partizan",
    710: "Demon's Spear",
    720: "Channeler's Trident",
    740: "Four-pronged Plow",
    1100: "Pike",
    1101: "Silver Knight Spear",
    1102: "Dragonslayer Spear",
    1103: "Moonlight Butterfly Horn",
    # Halberds / Scythes (7)
    730: "Titanite Catch Pole",
    731: "Black Knight Halberd",
    801: "Great Scythe",
    802: "Lucerne",
    803: "Scythe",
    804: "Halberd",
    805: "Giant's Halberd",
    810: "Lifehunt Scythe",
    811: "Gargoyle's Halberd",
    # Catalysts (12)
    653: "Demon's Catalyst",
    721: "Tin Banishment Catalyst",
    901: "Logan's Catalyst",
    910: "Sorcerer's Catalyst",
    911: "Pyromancy Flame",
    912: "Beatrice's Catalyst",
    913: "Tin Darkmoon Catalyst",
    914: "Oolacile Ivory Catalyst",
    915: "Tin Crystallization Ctlyst.",
    916: "Izalith Catalyst",
    920: "Oolacile Catalyst",
    921: "Manus Catalyst",
    # Talismans (7)
    902: "Talisman",
    903: "Canvas Talisman",
    904: "Thorolund Talisman",
    905: "Ivory Talisman",
    907: "Sunlight Talisman",
    908: "Darkmoon Talisman",
    909: "Velka's Talisman",
    # Fists (5)
    1000: "Caestus",
    1002: "Claw",
    1003: "Dragon Bone Fist",
    1004: "Dark Hand",
    1005: "Fists",
    # Whips (3)
    1200: "Whip",
    1201: "Notched Whip",
    1210: "Guardian Tail",
    # Bows (5)
    1300: "Short Bow",
    1301: "Longbow",
    1302: "Composite Bow",
    1304: "Black Bow of Pharis",
    1305: "Darkmoon Bow",
    # Greatbows (2)
    1360: "Dragonslayer Greatbow",
    1361: "Gough's Greatbow",
    1399: "Gough's Great Arrow",
    # Crossbows (4)
    1401: "Light Crossbow",
    1402: "Heavy Crossbow",
    1404: "Sniper Crossbow",
    1405: "Avelyn",
    # Shields (43)
    1501: "Target Shield",
    1502: "Hollow Soldier Shield",
    1503: "Cracked Round Shield",
    1504: "Balder Shield",
    1505: "Tower Shield",
    1507: "Spiked Shield",
    1509: "Crystal Shield",
    1510: "Stone Greatshield",
    1511: "Sunlight Shield",
    1513: "Tower Kite Shield",
    1514: "Black Knight Shield",
    1515: "Heater Shield",
    1516: "Knight Shield",
    1517: "Grass Crest Shield",
    1518: "Red and White Round Shield",
    1519: "Iron Round Shield",
    1520: "Spider Shield",
    1521: "East-West Shield",
    1522: "Wooden Shield",
    1523: "Plank Shield",
    1524: "Large Leather Shield",
    1525: "Small Leather Shield",
    1526: "Leather Shield",
    1527: "Giant Shield",
    1528: "Buckler",
    1529: "Eagle Shield",
    1530: "Pierce Shield",
    1531: "Crystal Ring Shield",
    1532: "Havel's Greatshield",
    1533: "Silver Knight Shield",
    1534: "Greatshield of Artorias",
    1535: "Crest Shield",
    1536: "Warrior's Round Shield",
    1537: "Caduceus Kite Shield",
    1538: "Caduceus Round Shield",
    1539: "Gargoyle's Shield",
    1540: "Bonewheel Shield",
    1541: "Dragon Crest Shield",
    1542: "Effigy Shield",
    1543: "Sanctus",
    1544: "Bloodshield",
    1545: "Black Iron Greatshield",
    1550: "Cleansing Greatshield",
    # Ammo / Special
    1700: "Lightning Bolt",
    1801: "Skull Lantern",
    2025: "Arrow",
    2026: "Bolt",
}

# 1000 and 100 digits, multiplied by 10000, give TAE animation offset (excluding ammo).
# e.g. Straight Sword (variation 2300+) use animation set a23_0000 (offset 230000).
# Other TAE offsets:
#   - 00_0000: default (one-handed sword)
#   - 02_0000: sword resting on shoulder
#   - 03_0000: one-handed spear
#   - 10_0000: two-handed sword
#   - 12_0000: two-handed sword resting on shoulder
#   - 13_0000: two-handed spear
PLAYER_WEAPON_BEHAVIOR_VARIATIONS = {
    1000: "Standard Arrow",
    1001: "Large Arrow",
    1002: "Feather Arrow",
    1003: "Fire Arrow",
    1004: "Poison Arrow",
    1005: "Moonlight Arrow",
    1006: "Wooden Arrow",
    1007: "Dragonslayer Arrow",
    1008: "Gough's Great Arrow",
    1100: "Standard Bolt",
    1101: "Heavy Bolt",
    1102: "Sniper Bolt",
    1103: "Wood Bolt",
    1104: "Lightning Bolt",
    2000: "Dagger",  # and Parrying Dagger
    2001: "Bandit's Knife",
    2002: "Priscilla's Dagger",
    2003: "Ghost Blade",
    2004: "Dark Silver Tracer",
    2300: "Straight Swords 1",  # Shortsword, Longsword, Broken/Crystal/Sunlight/Astora's Straight Sword
    2301: "Straight Swords 2",  # Broadsword, Barbed Straight Sword, Straight Sword Hilt
    2302: "Balder Side Sword",
    2303: "Silv. Knight Str. Sword",
    2304: "Darksword",
    2305: "Drake Sword",
    2500: "Heavy Sword",  # Bastard Sword, Man-serpent Greatsword, Crystal Greatsword
    2501: "Black Knight Sword",
    2502: "Flamberge",
    2503: "Stone Greatsword",
    2504: "Moonlight Greatsword",
    2505: "Claymore",
    2506: "Greatsword of Artorias",
    2507: "Great Lord Greatsword",
    2508: "Abyss Greatsword",
    2509: "Obsidian Greatsword",
    2600: "Zweihander",
    2601: "Dragon Greatsword",
    2602: "Greatsword",
    2603: "Demon Great Machete",
    2604: "Black Knight Greatsword",
    2700: "Rapier",
    2701: "Mail Breaker",
    2702: "Estoc",
    2703: "Velka's Rapier",
    2704: "Ricard's Rapier",
    2800: "Scimitar/Falchion",
    2801: "Shotel",
    2802: "Jagged Ghost Blade",
    2803: "Painting Guardian Sword",
    2804: "Quelaag's Furysword",
    2805: "Gold Tracer",
    2900: "Uchigatana/Washing Pole",
    2901: "Iaito",
    2902: "Chaos Blade",
    3000: "Battle Axe/Crescent Axe",
    3001: "Hand Axe",
    3002: "Golem Axe",
    3003: "Butcher Knife",
    3004: "Gargoyle Tail Axe",
    3200: "Greataxe",
    3201: "Dragon King Greataxe",
    3202: "Demon's Greataxe",
    3203: "Black Knight Greataxe",
    3204: "Stone Greataxe",
    3300: "Small Hammers",  # Mace, Morning Star, Blacksmith Hammer, Hammer of Vamos
    3301: "Warpick",
    3302: "Large Hammers",  # Club, Blacksmith Giant Hammer
    3303: "Pickaxe",
    3500: "Great Hammers",  # Grant, Demon's Great Hammer, Dragon Tooth
    3501: "Great Club",
    3502: "Large Club",
    3503: "Smough's Hammer",
    3600: "Spears",  # Spear, Winged Spear, Moonlight Butterfly Horn
    3601: "Pike",
    3602: "Channeler's Trident",
    3603: "Dragonslayer Spear",
    3604: "Partizan",
    3605: "Demon's Spear",
    3606: "Silver Knight Spear",
    3607: "Four-pronged Plow",
    3800: "Halberd/Gargoyle's Halberd",
    3801: "Scythe",
    3802: "Lucerne",
    3803: "Giant's Halberd",
    3804: "Titanite Catch Pole",
    3805: "Black Knight Halberd",
    4100: "Talismans/Pyromancy Flame",
    4101: "Weak Catalysts",  # Sorcerer's, Beatrice's Logan's, Tin Darkmoon, Oolacile Ivory, Oolacile
    4102: "Melee Catalysts",  # Tin Banishment, Tin Crystallization, Demon's
    4103: "Skull Lantern",
    4104: "Manus Catalyst",
    4200: "Caestus",
    4201: "Fists",
    4202: "Claw",
    4203: "Dark Hand",
    4204: "Dragon Bone Fist",
    4300: "Whips",
    4400: "Bows",  # all Bows
    4600: "Crossbows",  # all Crossbows
    4700: "Greatshields",
    4701: "Eagle Shield",
    4702: "Bonewheel Shield",
    4800: "Medium Shields",
    4801: "Small Shields",
    4802: "Crystal Ring Shield",
    4803: "Spiked Shield/Pierced Shield",
    5000: "Great Scythe/Lifehunt Scythe",
    5100: "Server/Murakumo",
    5101: "Gravelord Sword",
}

# General schematic for player behavior IDs. Not all of them are used by all weapons,
# even if the param entries are there (e.g. Dagger has no "strong attack 2").
BEHAVIOR_SUB_ID = {
    0: "One-handed normal attack 1",  # 3000 / 3030 (too heavy)
    1: "One-handed normal attack 1 (Ultra Greatsword AoE)",  # 3300 usually
    10: "One-handed normal attack 2",  # 3001
    20: "One-handed normal attack 3",  # 3002
    30: "One-handed jump attack",  # 3600
    40: "One-handed plunging attack (in air)",  # 3800 / 3801
    50: "One-handed plunging attack (hit ground)",  # 3810
    100: "One-handed strong attack 1",  # 3300 / 3301 / 3305 (not enough dur. for special attack)
    110: "One-handed strong attack 2",  # 3310
    120: "One-handed strong attack 1 (special)",  # 3300 / 3301
    200: "Two-handed normal attack 1",  # 4000 / 4030
    210: "Two-handed normal attack 2",  # 4001
    220: "Two-handed normal attack 3",  # 4002
    230: "Two-handed jump attack",  # 4600
    240: "Two-handed plunging attack (in air)",
    250: "Two-handed plunging attack (impact)",
    300: "Two-handed strong attack 1",  # 4300 / 4305 (not enough durability for special attack)
    310: "Two-handed strong attack 2",  # 4310 / 4315 (not enough durability for special attack)
    320: "Two-handed strong attack 1 (special)",  # 4300 (special attacks)
    330: "Two-handed strong attack 2 (special)",  # 4310 (Dragon Greatsword special attack)
    400: "Left-handed",  # 5000+
    410: "One-handed kick",  # 3100
    420: "Two-handed kick",  # 4100
    430: "One-handed guard",
    440: "Two-handed guard",
    450: "Parry",  # 5100
    490: "Plunging attack",  # 3820
    500: "Backstab",  # 3400
    501: "Backstab (second hit)",  # 3400 (some weapons)
    505: "Strong backstab",
    506: "Strong backstab (second hit)",  # 3400 (some weapons)
    510: "Riposte",  # 3201 / 3203 / 3980 (coffin stab)
    511: "Riposte (second hit)",  # 3201 / 3203 (some weapons)
    515: "Strong riposte",  # 3202, possibly?
    516: "Strong riposte (second hit)",  # 3202 (most weapons)
    517: "Strong riposte (third hit)",  # 3202 (some weapons)
    520: "One-handed running attack",  # 3500
    530: "Two-handed running attack",  # 4500
    540: "One-handed backstep attack",  # 3900
    580: "Two-handed backstep attack",  # 4900
    600: "Parry guard",  # TODO: "failed parry" guard I think
    800: "Special bullet",  # used by some special weapons, like Dragonslayer Spear R2 (3300)
}

# Weapons that have special one- or two-handed strong attacks that consume durability.
# Special attacks use animation 3300/4300 and behavior 120/320 (plus bullet behavior 800 typically). If the
# weapon doesn't have enough durability, animation 3305/4305 is used instead, which uses the standard
# behavior 100/300.
HAS_ONE_HANDED_SPECIAL_ATTACK = {
    "Dragonslayer Spear",  # lightning bullet
    "Dark Hand",  # uses "fail" animation +5 if target can't be grabbed?
    "Golem Axe",
    "Crystal Ring Shield",
    "Moonlight Greatsword",
}
HAS_TWO_HANDED_SPECIAL_ATTACK = {
    "Drake Sword",  # shockwave
    "Moonlight Greatsword",  # moonlight slice
    "Crystal Ring Shield",
    "Dragon Greatsword",  # also uses behavior 330 (and bullet beh. 800 again) in follow-up attack 4310
    "Dragon King Greataxe",
    "Obsidian Greatsword",
}

# My rough descriptions of various SpEffect ID ranges.
# I've extended the ranges to 99 or 999 where obvious, but many are unused.
# The 8000 range is likely the best range to add custom effects.
SPECIAL_EFFECT_RANGES = {
    (0, 29): "System/Test Effects",
    (30, 99): "Animation/Permanent Effects",  # e.g. curse effect, resonance, counter damage
    (100, 109): "Bonfire Recovery Effects",  # note that Estus refill is hard-coded
    (110, 119): "Respawn Recovery Effects",
    (200, 299): "QWC Area Effects",  # unused world tendency stuff I think
    (300, 399): "QWC Player Effects",  # unused world tendency stuff I think
    (500, 1999): "Spell Effects",  # miracle, sorcery, pyromancy buffs/debuffs
    (2000, 2499): "Ring Effects",  # only goes up to 2350 (Calamity Ring)
    (2900, 2999): "Unused Ring Effects",  # DeS junk
    (3000, 3500): "Consumable Effects",
    (3900, 3999): "Unused Consumable Effects",  # DeS junk
    (4000, 4099): "Unused Environment Effects",  # DeS junk
    (4100, 4199): "Environment Effects",  # e.g. near Quelana
    (4500, 4999): "PvP Effects",  # e.g. Forest Hunters region, Battle of Stoicism
    (5000, 5099): "Unused NPC Effects",  # DeS junk
    (5100, 5999): "NPC Effects",  # any SpEffect applied to or by an NPC (including c0000)
    (6000, 6999): "Weapon Effects",  # PC weapon effects (good and bad)
    (7000, 7099): "Area Level Effects",  # 7001 to 7015, applied to all enemies in an area
    (7100, 7100): "Black Phantom Effect",  # buff applied to Gravelord Phantoms
    (7400, 7499): "NG+ Level Effects",  # buff stacked on NPC in NG+ levels
    (7500, 7599): "Boss Coop Effects",  # buffs applied to bosses depending on number of summons
    (7600, 7999): "NPC Level Effects",  # buffs applied to NPCs to power them up
    (8000, 8001): "Unused Level Tests",  # unused "doping" tests
    (9600, 9600): "Level Sync",  # symbolic effect for DSR PvP level matching
    (70000, 71111): "Immortality Flags",  # last two bits control some kind of immortality system
    (80000, 81111): "Special Flags",  # four bits toggling "remnant", "soul-sucking", "fascination", and something else
    (90000, 91111): "Status Flags",  # four bits toggling poison, bleed, toxic, and curse vulnerability
}

# Values in brackets indicate the offset of the "ground" of each pose relative to the player's position.
OBJECT_POSES = {
    "o0500": {  # Naked male Hollow corpse
        10: "Lying face-down, right knee crooked, head turned right. [-0.25 Y]",
        11: "Lying face-down, right knee crooked, head turned left [-0.25 Y]",
        20: "Lying face-up, right knee raised, left hand on chest, head turned right",
        21: "Lying face-up, fully laid out",
        31: "Folded over a thin wall (e.g. a well)",
        35: "Folded over a thick wall, head looking down",
        42: "Lying face-down, legs hanging off edge at right angle [+0.1 Y]",
        50: "Sitting against wall, legs spread [-0.2 Y]",
        51: "Sitting against wall, legs almost crossed [-0.2 Y]",
        81: "Foetal position on right side",
        82: "Almost foetal position on left side",
        90: "Arms wrapped around something (e.g. a spike statue)",
        95: "Floating face-down in water",
    },
    "o0502": {  # Hollow Soldier corpse
        41: "Folded over a rafter",
    },
    "o0504": {  # Female Hollow corpse
        61: "Kneeling, hunched over",
        81: "Foetal position on right side",
    },
}

# Maps `talkesd` map file stems to lists of `tXXXXXX` bonfire ESD files inside them.
# All vanilla bonfire ESD files are identical, so this helps with modifying all of them at once.
BONFIRE_ESDS = {
    "m10_00_00_00": [
        "t100000",
        "t100001",
        "t100002",
        "t100010",
    ],
    "m10_01_00_00": [
        "t100100",
        "t100101",
        "t100102",
        "t100103",
        "t100104",
        "t100105",
        "t100106",
        "t100110",
    ],
    "m10_02_00_00": [
        "t100200",
        "t100201",
        "t100202",
        "t100210",
    ],
    "m11_00_00_00": [
        "t110000",
        "t110001",
        "t110002",
        "t110010",
    ],
    "m12_00_00_00": [
        "t120000",
        "t120001",
        "t120002",
        "t120010",
    ],
    "m12_01_00_00": [
        "t121000",
        "t121001",
        "t121002",
        "t121003",
        "t121004",
    ],
    "m13_00_00_00": [
        "t130000",
        "t130001",
        "t130002",
        "t130010",
    ],
    "m13_01_00_00": [
        "t131000",
        "t131001",
        "t131002",
        "t131010",
    ],
    "m13_02_00_00": [
        "t132000",
        "t132001",
        "t132002",
        "t132010",
    ],
    "m14_00_00_00": [
        "t140000",
        "t140001",
        "t140002",
        "t140010",
    ],
    "m14_01_00_00": [
        "t141000",
        "t141001",
        "t141002",
        "t141003",
        "t141004",
        "t141010",
    ],
    "m15_00_00_00": [
        "t150000",
        "t150001",
        "t150002",
        "t150010",
    ],
    "m15_01_00_00": [
        "t151000",
        "t151001",
        "t151002",
        "t151010",
    ],
    "m16_00_00_00": [
        "t160000",
        "t160001",
        "t160002",
        "t160010",
    ],
    "m17_00_00_00": [
        "t170000",
        "t170001",
        "t170002",
        "t170010",
    ],
    "m18_00_00_00": [
        "t180000",
        "t180001",
        "t180002",
        "t180010",
    ],
    "m18_01_00_00": [
        "t181000",
        "t181001",
    ],
}

# Maps each fog wall object ID to its matching VFX (FFX) ID, FFXBND source file name, and a description of its location.
FOG_WALL_MODELS = {
    # Depths
    1400: (81000, "FRPG_SfxBnd_m10_00", "Gaping Dragon entrance"),
    1401: (81001, "FRPG_SfxBnd_m10_00", "Undead Burg entrance"),  # bottom of stairs after locked door
    1402: (81002, "FRPG_SfxBnd_m10_00", "Blighttown entrance"),
    1420: (81020, "FRPG_SfxBnd_m10_00", "Depths checkpoint"),  # before Channeler

    # Undead Burg / Parish
    1403: (81003, "FRPG_SfxBnd_m10_01", "Bell Gargoyles entrance"),
    1404: (81004, "FRPG_SfxBnd_m10_01", "Bell Gargoyles exit"),
    1405: (81005, "FRPG_SfxBnd_m10_01", "Taurus Demon entrance"),
    1406: (81006, "FRPG_SfxBnd_m10_01", "Taurus Demon exit"),
    1407: (81007, "FRPG_SfxBnd_m10_01", "Upper Burg exit to Firelink Shrine"),  # bottom of stairs
    1408: (81008, "FRPG_SfxBnd_m10_01", "Parish exit to Andre"),  # start of long walkway behind Parish
    1409: (81009, "FRPG_SfxBnd_m10_01", "Bridge exit to Taurus Demon"),  # opposite Basement door
    1410: (81010, "FRPG_SfxBnd_m10_01", "Parish elevator to Firelink Shrine"),  # blocks both elevators
    1411: (81011, "FRPG_SfxBnd_m10_01", "Upper Burg exit to Darkroot Basin"),  # behind Havel
    1412: (81012, "FRPG_SfxBnd_m10_01", "Bridge exit to Lower Burg"),  # Basement door
    1413: (81013, "FRPG_SfxBnd_m10_01", "Capra Demon entrance"),
    1414: (81014, "FRPG_SfxBnd_m10_01", "Lower Burg exit to Firelink Shrine"),  # near Female Undead Merchant
    1415: (81015, "FRPG_SfxBnd_m10_01", "Lower Burg exit to Bridge"),  # below Basement door
    1416: (81016, "FRPG_SfxBnd_m10_01", "Parish checkpoint"),  # to bridge above gate
    1417: (81017, "FRPG_SfxBnd_m10_01", "Lower Burg one-way gate"),  # to Upper Burg
    1418: (81018, "FRPG_SfxBnd_m10_01", "Upper Burg bonfire room lower entrance"),
    1419: (81019, "FRPG_SfxBnd_m10_01", "Upper Burg checkpoint"),  # before first Hellkite appearance
    1421: (81021, "FRPG_SfxBnd_m10_01", "Upper Burg bonfire room upper entrance"),  # just below bridge

    # Painted World
    1600: (81100, "FRPG_SfxBnd_m11", "Priscilla entrance"),
    1601: (81101, "FRPG_SfxBnd_m11", "Unused Priscilla exit"),  # off to the side
    1602: (-1, "", "<UNUSED>"),
    1603: (81103, "FRPG_SfxBnd_m11", "Painted World checkpoint"),  # bottom of tower to Phalanx courtyard
    1604: (81104, "FRPG_SfxBnd_m11", "Sewer exit to courtyard"),
    1605: (-1, "", "<UNUSED>"),

    # Darkroot Garden / Basin
    2900: (81200, "FRPG_SfxBnd_m12", "Sif entrance"),
    2901: (81201, "FRPG_SfxBnd_m12", "Garden exit to Parish"),  # behind Titanite Demon
    2902: (81202, "FRPG_SfxBnd_m12", "Basin exit to Upper Burg"),  # into Havel's tower
    2903: (81203, "FRPG_SfxBnd_m12", "Basin exit to Valley of Drakes"),  # entrance to bonfire tunnel
    2904: (81204, "FRPG_SfxBnd_m12", "Moonlight Butterfly entrance"),
    2905: (81205, "FRPG_SfxBnd_m12", "Moonlight Butterfly exit"),
    2906: (81206, "FRPG_SfxBnd_m12", "Darkroot Garden checkpoint"),  # entrance to area before Butterfly
    2907: (81207, "FRPG_SfxBnd_m12", "Bridge above Hydra"),  # ladder side of bridge
    2908: (81209, "FRPG_SfxBnd_m12", "Crest of Artorias door"),

    # Oolacile / Chasm of the Abyss
    2909: (81213, "FRPG_SfxBnd_m12_01", "Sanctuary Guardian entrance"),
    2910: (81214, "FRPG_SfxBnd_m12_01", "Sanctuary Guardian exit"),
    2911: (81210, "FRPG_SfxBnd_m12_01", "Manus entrance"),
    2912: (81218, "FRPG_SfxBnd_m12_01", "Chasm exit to Royal Wood"),  # bottom of elevator
    2913: (81215, "FRPG_SfxBnd_m12_01", "Sanctuary exit to Royal Wood"),  # before bridge
    2914: (81216, "FRPG_SfxBnd_m12_01", "Royal Wood exit to Chasm"),  # top of elevator
    2915: (81211, "FRPG_SfxBnd_m12_01", "Artorias entrance"),
    2916: (81212, "FRPG_SfxBnd_m12_01", "Artorias exit"),
    2917: (81217, "FRPG_SfxBnd_m12_01", "Battle of Stoicism exit to Township"),
    2918: (-1, "", "<UNUSED>"),
    2919: (81220, "FRPG_SfxBnd_m12_01", "Kalameet entrance"),
    2920: (81221, "FRPG_SfxBnd_m12_01", "Battle of Stoicism exit to Artorias"),  # immediately after Artorias exit

    # Catacombs
    3950: (-1, "", "<UNUSED>"),
    3951: (81301, "FRPG_SfxBnd_m13_00", "Catacombs exit to Firelink Shrine"),  # top of first ladder
    3952: (81302, "FRPG_SfxBnd_m13_00", "Catacombs checkpoint"),  # after first rotating bridge
    3953: (-1, "", "<UNUSED>"),
    3954: (81300, "FRPG_SfxBnd_m13_00", "Pinwheel entrance"),  # in rock tunnel before drop
    3955: (-1, "", "<UNUSED>"),

    # Tomb of the Giants
    3960: (-1, "", "<UNUSED>"),
    3961: (81310, "FRPG_SfxBnd_m13_01", "Tomb exit to Catacombs"),  # giant fog wall above Pinwheel coffin
    3962: (81311, "FRPG_SfxBnd_m13_01", "Tomb checkpoint"),  # shortly after Patches
    3963: (81312, "FRPG_SfxBnd_m13_01", "Tomb golden fog wall"),
    3964: (81315, "FRPG_SfxBnd_m13_01", "Nito entrance"),
    3965: (-1, "", "<UNUSED>"),

    # Great Hollow / Ash Lake
    3970: (81320, "FRPG_SfxBnd_m13_02", "Great Hollow exit to Blighttown"),  # before both illusory walls
    3971: (81321, "FRPG_SfxBnd_m13_02", "Ash Lake checkpoint"),  # in tunnel between Great Hollow and Ash Lake
    3972: (-1, "", "<UNUSED>"),
    3973: (-1, "", "<UNUSED>"),

    # Blighttown / Quelaag's Domain
    4950: (81400, "FRPG_SfxBnd_m14_00", "Quelaag entrance"),
    4951: (81401, "FRPG_SfxBnd_m14_00", "Quelaag exit"),
    4952: (81402, "FRPG_SfxBnd_m14_00", "Blighttown exit to Depths"),
    4953: (81403, "FRPG_SfxBnd_m14_00", "Blighttown exit to Valley of Drakes"),
    4954: (81404, "FRPG_SfxBnd_m14_00", "Blighttown exit to Great Hollow"),  # before both illusory walls
    4955: (-1, "", "<UNUSED>"),
    4956: (81406, "FRPG_SfxBnd_m14_00", "Blighttown checkpoint"),  # before last ladders down to swamp
    4957: (-1, "", "<UNUSED>"),
    4958: (-1, "", "<UNUSED>"),

    # Demon Ruins / Lost Izalith
    4960: (81410, "FRPG_SfxBnd_m14_01", "Demon Ruins golden fog wall"),
    4961: (81411, "FRPG_SfxBnd_m14_01", "Ceaseless Discharge entrance"),
    4962: (81412, "FRPG_SfxBnd_m14_01", "Demon Firesage entrance"),
    4963: (81413, "FRPG_SfxBnd_m14_01", "Demon Firesage exit"),
    4964: (81414, "FRPG_SfxBnd_m14_01", "Centipede Demon entrance"),
    4965: (81415, "FRPG_SfxBnd_m14_01", "Centipede Demon exit"),
    4966: (81416, "FRPG_SfxBnd_m14_01", "Demon Ruins exit to Quelaag's Domain"),  # just before first bonfire
    4967: (81417, "FRPG_SfxBnd_m14_01", "Demon Ruins elevator bottom"),  # on stairs to elevator
    4968: (81418, "FRPG_SfxBnd_m14_01", "Ceaseless lava field exit"),  # near first Kirk invasion
    4969: (81419, "FRPG_SfxBnd_m14_01", "Demon Firesage exit (multiplayer)"),
    4970: (81420, "FRPG_SfxBnd_m14_01", "Centipede Demon exit (multiplayer)"),
    4971: (81422, "FRPG_SfxBnd_m14_01", "Izalith shortcut gate"),
    4972: (81421, "FRPG_SfxBnd_m14_01", "Bed of Chaos entrance"),
    4973: (81423, "FRPG_SfxBnd_m14_01", "Arch before Ceaseless bridge"),

    # Sen's Fortress
    5150: (81500, "FRPG_SfxBnd_m15_00", "Iron Golem entrance"),
    5151: (81501, "FRPG_SfxBnd_m15_00", "Fortress exit to Parish"),  # start of bridge
    5152: (81502, "FRPG_SfxBnd_m15_00", "Fortress checkpoint 1"),  # after outdoor boulder ramp
    5153: (81503, "FRPG_SfxBnd_m15_00", "Fortress checkpoint 2"),  # to roof area
    5154: (-1, "", "<UNUSED>"),
    5155: (-1, "", "<UNUSED>"),

    # Anor Londo
    5860: (81510, "FRPG_SfxBnd_m15_01", "O&S entrance"),
    5861: (81511, "FRPG_SfxBnd_m15_01", "O&S exit (small)"),
    5862: (81512, "FRPG_SfxBnd_m15_01", "O&S exit (large)"),
    5863: (81513, "FRPG_SfxBnd_m15_01", "Corkscrew elevator bottom"),
    5864: (81514, "FRPG_SfxBnd_m15_01", "Anor Londo checkpoint 1"),  # from rafters to spinning tower
    5865: (81515, "FRPG_SfxBnd_m15_01", "Anor Londo checkpoint 2"),  # balcony after archers
    5866: (-1, "", "<UNUSED>"),
    5867: (81517, "FRPG_SfxBnd_m15_01", "Gwyndolin entrance"),
    5868: (81518, "FRPG_SfxBnd_m15_01", "Gwyndolin entrance in endless corridor"),
    5869: (81521, "FRPG_SfxBnd_m15_01", "Cathedral broken window"),  # to Dragonslayer Greatbow
    5870: (81519, "FRPG_SfxBnd_m15_01", "Cathedral to Giant Blacksmith"),
    5871: (81520, "FRPG_SfxBnd_m15_01", "Cathedral to bedroom area"),

    # New Londo Ruins
    6600: (-1, "", "<UNUSED>"),
    6601: (81601, "FRPG_SfxBnd_m16", "New Londo exit to Firelink Shrine"),  # bottom of elevator
    6602: (81602, "FRPG_SfxBnd_m16", "New Londo exit to Valley of Drakes"),  # locked gate
    6603: (81603, "FRPG_SfxBnd_m16", "New Londo giant gate"),
    6604: (81604, "FRPG_SfxBnd_m16", "New Londo checkpoint 1"),  # above broken cathedral
    6605: (81605, "FRPG_SfxBnd_m16", "New Londo checkpoint 2"),  # entrance to broken cathedral ground floor
    6606: (81608, "FRPG_SfxBnd_m16", "Four Kings entrance"),
    6607: (-1, "", "<UNUSED>"),

    # Duke's Archives
    7900: (81700, "FRPG_SfxBnd_m17", "Seath cave entrance"),
    7901: (81701, "FRPG_SfxBnd_m17", "Seath tower entrance"),
    7902: (81702, "FRPG_SfxBnd_m17", "Archives first elevator top"),  # top of first elevator
    7903: (-1, "", "<UNUSED>"),
    7904: (-1, "", "<UNUSED>"),
    7905: (-1, "", "<UNUSED>"),
    7906: (81706, "FRPG_SfxBnd_m17", "Archives checkpoint"),  # from wooden room to garden area
    7907: (81707, "FRPG_SfxBnd_m17", "Archives golden fog"),
    7908: (81708, "FRPG_SfxBnd_m17", "Archives tower elevator top"),  # bottom of long passage to Seath

    # Kiln of the First Flame
    8050: (81800, "FRPG_SfxBnd_m18_00", "Gwyn entrance"),
    8051: (81801, "FRPG_SfxBnd_m18_00", "Ghost staircase bottom"),

    # Undead Asylum
    8950: (81802, "FRPG_SfxBnd_m18_01", "Asylum Demon top entrance"),
    8951: (-1, "", "<UNUSED>"),
    8952: (81805, "FRPG_SfxBnd_m18_01", "Asylum checkpoint"),  # before Oscar
    8953: (81806, "FRPG_SfxBnd_m18_01", "Stray Demon exit"),  # in front of ladder
}


HELLKITE_BRIDGE_FIRE_FFX = (
    14010,
    14011,
    14015,
    14025,
    14035,
    14040,
    14045,
    14120,
    14130,
    14151,
    14152,
    14153,
    14154,
    14162,
)
