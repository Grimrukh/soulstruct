
__all__ = [
    "CHARACTER_MODELS",
]


CHARACTER_MODELS = {
    0: "Human NPC/Player",
    100: "c0100 (?)",
    110: "c0110 (?)",
    120: "c0120 (?)",
    130: "c0130 (?)",
    1000: "No Model",  # for interaction points or misc. talk ESD, like Sites of Grace
    # SPECIAL
    2010: "Blaidd",
    2030: "Rennala Phase One / Friendly",
    2031: "Rennala Phase Two",
    2040: "Rennala Student",
    2041: "Lesser Kindred of Rot",
    2050: "Ranni",
    2060: "The Two Fingers",
    2070: "The Three Fingers",
    2100: "Black Knife Assassin",  # all variants including Alecto
    2110: "Beast Clergyman / Maliketh",  # yes, same model
    2120: "Malenia",  # both phases
    2130: "Morgott / Margit",
    2131: "Morgott (Defeated)",
    2140: "Fell Twins",
    2150: "Wisp",
    2160: "Finger Reader Crone",
    2170: "Finger Reader Enia",
    2180: "Melina",
    2190: "Radagon",
    2200: "Elden Beast",
    # CRABS
    2270: "Large Crab",
    2271: "Small Crab",
    2272: "Large Crab (Injured)",
    2273: "Small Crab (Worms)",
    2274: "Large Crab (Snow)",
    2275: "Small Crab (Crystal)",
    2276: "Small Crab (Very Dirty)",
    2277: "Small Crab (Dirty)",
    # GENERAL
    2500: "Crucible Knight",
    3000: "Exile Soldier",
    3010: "Banished Knight",
    3020: "Exile Soldier (Giant)",
    3050: "Commander Niall/O'Neil",
    3060: "Skeletal Executioner",
    3061: "Skeletal Beastman",
    3070: "Celebrant",  # dancing Dominula women
    3080: "Fanged Imp",
    3100: "Elemer / Bell Bearing Hunter",
    3150: "Night's Calvary",
    3160: "Night's Calvary Horse",
    3170: "Albinauric Archer",
    3171: "Albinauric Archer (Giant)",  # "Phillia" at end of Latenna's quest
    3180: "Albinauric Archer Wolf",  # surely (other wolves below)
    3181: "Red Wolf",  # boss and non-boss variants
    3200: "Nomad Trader (Hat and Cape)",
    3201: "Nomad Trader (Long Hair)",
    3210: "Nomad Mule",
    3250: "Draconic Tree Sentinel",
    3251: "Tree Sentinel",
    3252: "Loretta",  # Royal and Haligtree variants
    3300: "Nox Warrior",  # all variants, including ant riders
    3320: "Silver Tear",
    3330: "Silver Tear Orb",
    3350: "Crystalian",  # all variants
    3360: "Ancestral Follower",
    3361: "Ancestral Follower (Scarlet Rot)",  # cut content, removed from Lake of Rot after 1.00
    3370: "Ancestral Follower Shaman",
    3371: "Ancestral Follower Shaman (Scarlet Rot)",  # cut content, removed from Lake of Rot after 1.00
    3400: "Grave Warden Duelist",
    3450: "Misbegotten",
    3451: "Misbegotten (Axe) / Hewg",
    3460: "Leonine Misbegotten",
    3470: "Second-Generation Albinauric (Small)",  # cartwheeling froggy
    3471: "Second-Generation Albinauric (Large)",  # cartwheeling froggy
    3500: "Skeleton (Curved Sword)",
    3510: "Skeleton (Scimitar)",
    3550: "Sanguine Noble",
    3560: "Godskin Apostle",
    3570: "Godskin Noble",
    3600: "Onyx/Alabaster Lord",
    3610: "Oracle Envoy (Small)",
    3620: "Oracle Envoy (Medium)",
    3630: "Oracle Envoy (Large)",
    3650: "Erdtree Guardian",
    3660: "Commoner",
    3661: "Putrid Corpse",
    3662: "Putrid Corpse (Bare)",
    3664: "Cemetery Shade",
    3665: "Devious Commoner / Gostoc",
    3666: "Sunflower Commoner / Goldmask",
    3670: "First-Generation Albinauric",  # all emaciated, weak-legged variants
    3700: "Perfumer Tricia",
    3701: "Depraved Perfumer",
    3702: "Raya Lucaria Scholar",  # with stone heads; multiple subtypes/schools
    3703: "Noble's Page",  # aka crossbow/knife guy
    3704: "Battle Mage Hugues",
    3710: "Crystallized Battlemage",
    3720: "Orbhead Sorcerer",  # cut content?
    3730: "Arcane Sphere of Faces",
    3750: "Clayman",
    3800: "Cleanrot Knight",
    3810: "Kindred of Rot",  # aka "Pests"
    3850: "Marionette",
    3860: "Avionette",
    3900: "Fire Monk",
    3901: "Blackflame Monk",
    3910: "Fire Prelate",
    3950: "Man-Serpent",
    3970: "Beastman",  # all variants
    4000: "Wraith Caller / Rider",  # includes horse for rider
    4020: "Revenant",  # looks grafted but isn't
    4040: "Sewer Slug",
    4050: "Kaiden Sellsword",
    4060: "Kaiden Sellsword Horse",
    4070: "Wolf (Small)",
    4071: "Wolf (Large)",
    4080: "Rat",
    4090: "Giant Rat",
    # DEMI-HUMANS
    4100: "Demi-Human",
    4101: "Large Demi-Human",
    4110: "Demi-Human Shaman",
    4120: "Demi-Human Chief",
    4130: "Demi-Human Queen",
    # CREATURES OF THE LANDS BETWEEN
    4140: "Snail",  # all variants: serpent, skull-shell, crystal, Spirit-Caller
    4150: "Basilisk",
    4160: "Shaggy Stray (Large)",  # red tint
    4161: "Shaggy Stray (Small)",  # yellow tint
    4162: "Stray (Large)",
    4163: "Stray (Small)",
    4164: "Blistered Stray (Large)",  # inflicts bleed
    4165: "Blistered Stray (Small)",  # inflicts bleed
    4166: "Rotten Stray (Large)",  # fungal growths
    4167: "Rotten Stray (Small)",  # fungal growths
    4170: "Living Mass (Small)",  # has animal parts (feathers, bones)
    4171: "Living Mass (Large)",  # no discernable animal parts
    4180: "Spirit Jellyfish",
    4190: "Scarab",
    4191: "Scarab (Small)",
    4192: "Scarab (Large)",
    4200: "Giant Bat",
    4201: "Chanting Winged Dame",
    4210: "Bladed Talon Eagle",
    4220: "Land Octopus (Large)",
    4230: "Land Octopus (Small)",
    # GENERAL
    4240: "Fingercreeper (Large)",
    4241: "Fingercreeper (Giant)",
    4250: "Fingercreeper (Small)",
    4260: "Erdtree Burial Watchdog",
    4270: "Elder Lion",
    4280: "Giant Flying Ant",  # with optional "Numen sacs"; also enslaved as Nox mounts
    4281: "Giant Hard-Headed Ant",
    4290: "Bloodhound Knight",
    # MILITARY FACTIONS (+ Vulgar Militia and Mad Pumpkin Head)
    4300: "Wandering Noble",
    4310: "Soldier",
    4311: "Godrick Soldier",
    4312: "Raya Lucaria Soldier",
    4313: "Leyndell Soldier",
    4314: "Radahn Soldier",
    4315: "Mausoleum Soldier",
    4316: "Haligtree Soldier",
    4320: "Vulgar Militia (Removed)",  # no CHRBND file?
    4321: "Vulgar Militia",
    4340: "Mad Pumpkin Head (Giant)",
    4341: "Mad Pumpkin Head",
    4350: "Castle Knight",
    4351: "Godrick Knight",
    4352: "Cuckoo Knight",
    4353: "Leyndell Knight",
    4354: "Redmane Knight",
    4355: "Mausoleum Knight",
    4356: "Haligtree Knight",
    4360: "Knight's Horse",
    4361: "Godrick Knight's Horse",
    4362: "Cuckoo Knight's Horse",
    4363: "Leyndell Knight's Horse",
    4364: "Redmane Knight's Horse",
    4365: "Mausoleum Knight's Horse",
    4366: "Haligtree Knight's Horse",
    4370: "Foot Soldier",
    4371: "Godrick Foot Soldier",
    4372: "Raya Lucaria Foot Soldier",
    4373: "Leyndell Foot Soldier",
    4374: "Radahn Foot Soldier",
    4375: "Mausoleum Foot Soldier",
    4376: "Haligtree Foot Soldier",
    # GENERAL
    4377: "Highwayman",
    4380: "Starcaller",
    4381: "Bloodthorn Exile",
    4382: "Tunnel Miner",
    4383: "Glintstone Miner",
    4384: "Glintstone Miner (Small Sack)",
    4385: "Fungal Sorcerer",
    4420: "Giant Lobster",
    4430: "Abnormal Stone Cluster",  # both Evergaol "worm" and "explosive trap" variants
    4440: "Fungal Pod",
    4441: "Giant Fungal Pod",
    4442: "Giant Fungal Pod (Rot)",
    4450: "Walking Mausoleum",
    4460: "Flame Chariot",  # intact and damaged variants
    4470: "Abductor Virgin",  # all variants
    4480: "Miranda the Blighted Bloom/Blossom",
    4481: "Miranda Sprout",
    4482: "Giant Miranda Sprout",
    4483: "Miranda Sprout",
    4490: "Living Jar (Large)",
    4491: "Living Jar (Small)",
    4492: "Great Jar",
    # DRAGONS
    4500: "Flying Dragon Agheel/Greyll",
    4501: "Decaying Ekzykes",  # largest non-ancient dragon after Greyoll
    4502: "Glintstone Dragon Smarag/Adula",  # sword in mouth; same size as Agheel/Greyll
    4503: "Borealis the Freezing Fog",  # same size as Agheel/Greyll
    4504: "Elder Dragon Greyoll",  # colossal
    4505: "Lesser Dragon",  # smallest
    4510: "Ancient Dragon Lansseax",  # similar size to Agheel and co.
    4511: "Lichdragon Fortissax",
    4520: "Dragonlord Placidusax",
    # GENERAL
    4550: "Monstrous Dog",
    4560: "Monstrous Crow (c4560)",
    4561: "Monstrous Crow (c4561)",
    4570: "Wormface (Regular)",
    4580: "Wormface (Giant)",
    4600: "Stonedigger Troll / Bols, Carian Knight",  # optional cloak
    4601: "Carian Troll Knight",  # helmet
    4602: "Shaggy Troll",  # white
    4603: "Naked Troll",  # has Iji's club but nothing else
    4604: "Iji",  # club, helmet, and book
    4620: "Astel / Malformed Star",
    4630: "Giant Runebear",  # normal-sized bears below
    4640: "Ulcerated/Putrid Tree Spirit",
    4650: "Dragonkin Soldier",
    4660: "Guardian Golem",
    4670: "(Regal) Ancestor Spirit",
    4680: "Fallingstar Beast",
    4690: "Grafted Scion",
    4710: "God-Devouring Serpent / Rykard",
    4711: "Rykard Slime",
    4720: "Godfrey",  # golden and real variants
    4721: "Hoarah Loux",
    4730: "Starscourge Radahn",
    4750: "Godrick the Grafted",
    4751: "Godrick the Grafted (Defeated)",
    4760: "Fire Giant",
    4770: "Gargoyle / Black Blade Kindred",  # all variants
    4800: "Mohg",  # both bosses
    4810: "Erdtree Avatar",  # all variants except Putrid
    4811: "Putrid Avatar",
    4820: "Omenkiller",
    4910: "Magma Wyrm",
    4911: "Great Wyrm Theodorix",
    4950: "Tibia Mariner",
    4960: "Giant Skeleton Torso",  # summoned by Tibia Mariners
    4980: "Deathbird / Death Rite Bird",  # Death Rite Bird has blackflame wings
    # WILDLIFE
    6000: "Eagle (c6000)",
    6001: "Eagle (c6001)",
    6010: "Deer",
    6030: "Bear (c6030)",
    6031: "Bear (c6031)",
    6040: "Owl",
    6050: "Boar",
    6060: "Wild Mouflon",
    6070: "Guillemot (c6070)",
    6071: "Guillemot (c6071)",
    6072: "Carrier Pigeon",
    6080: "Giant Dragonfly (c6080)",
    6081: "Giant Dragonfly (c6081)",
    6082: "Giant Dragonfly (c6082)",
    6090: "Turtle",
    6091: "Giant Turtle / Miriel",
    6100: "Springhare",
    # MISC.
    7000: "Fallen Hawks Soldier",
    7100: "Ancient Hero of Zamor",
    # TORRENT
    8000: "Torrent",
    # WEAPONS
    8100: "Ballista",
    8101: "Giant Ballista",
    8110: "Dragon-Faced Flamethrower",
    8120: "Merciless Chariot",  # from Hero's Grave dungeons
    # NPC VARIANTS
    8900: "Malenia (c8900)",  # TODO: not used in Haligtree map...?
    8901: "Beast Clergyman / Maliketh, the Black Blade (c8901)",
    8903: "Rennala (c8903)",
    8904: "Morgott (c8904)",
    8905: "Mohg, Lord of Blood (c8905)",
    8906: "Melina (c8906)",
    8907: "Malformed Ranni (c8907)",
    9001: "Unknown (c9001)",

    # region Shadow of the Erdtree (DLC)
    5000: "Commander Gaius",
    5010: "Golden Hippopotamus",
    5011: "Golden Hippopotamus (Lesser)",
    5020: "Putrescent Knight",
    5030: "Romina, Saint of the Bud",
    5040: "Curseblade",
    5050: "Midra (Human)",
    5051: "Midra, Lord of Frenzied Flames",
    5060: "Finger Ruin Serpent",
    5061: "Finger Ruin Serpent (Large)",  # TODO: pale version?
    5070: "Death Knight",
    5080: "Bloodfiend",
    5081: "Bloodfiend Chief",
    5090: "Gravebird",
    5110: "Spirit Worm",  # TODO: real name?
    5120: "Bayle the Dread",
    5130: "Messmer the Impaler (Phase 1)",
    5131: "Messmer the Impaler (Phase 1)",  # TODO: use?
    5132: "Messmer the Impaler (Phase 2)",
    5140: "Messmer's Serpent (Large)",
    5141: "Messmer's Serpent (Medium)",
    5160: "Fire Monk",
    5170: "Furnace Golem",
    5180: "Empty (c5180)",
    5181: "Empty (c5181)",
    5190: "Winged Scorpion (Large)",
    5192: "Winged Scorpion (Giant)",
    5193: "Winged Scorpion (Small)",
    5194: "Winged Scorpion (Medium)",
    5200: "Metyr, Mother of Fingers",
    5210: "Divine Beast Dancing Lion",
    5220: "Promised Consort Radahn",  # both phases
    5221: "Miquella's Arms (Radahn)",
    5230: "Scadutree Avatar",
    5240: "Shadow Commoner",
    5241: "Large Shadow Commoner",
    5250: "Divine Lion Warrior",
    5251: "Divine Hornsent Priest",  # ranged spell spammer
    5260: "Forge Giant (Large)",
    5261: "Forge Giant (Medium)",
    5270: "Pot Shaman (Medium)",
    5271: "Pot Shaman (Large)",
    5280: "Winter Lantern",
    5300: "Rellana, Twin Moon Knight",
    5311: "Hornsent Priest",
    5312: "Hornsent Priest (Tall)",  # possibly just the boss
    5320: "Fat Hornsent Priest",
    5330: "St. Trina",
    5340: "Empty (c5340)",
    5350: "Eyes of Death",
    5360: "Undead Beastman (DLC)",
    5370: "Ancient Dragon (DLC)",
    5380: "Miranda Blossom (DLC)",
    5381: "Miranda Sprout (DLC)",
    5390: "Troll (DLC)",
    5391: "Carian Troll Knight (DLC)",
    5401: "Eagle (DLC)",
    5410: "Deer (DLC)",
    5421: "Bear (DLC)",
    5430: "Owl (DLC)",
    5440: "Boar (DLC)",
    5450: "Ram (DLC)",
    5460: "Crow (DLC)",
    5470: "Dragonfly (Small) (DLC)",
    5471: "Dragonfly (Medium) (DLC)",
    5472: "Dragonfly (Large) (DLC)",
    5480: "Turtle (DLC)",
    5490: "Springhare (DLC)",
    5500: "Magma Tear",
    5511: "Putrid Corpse (DLC)",
    5512: "Putrid Corpse (Large) (DLC)",
    5513: "Cemetery Shade (DLC)",
    5520: "Rotten Stray (Large) (DLC)",
    5521: "Rotten Stray (Small) (DLC)",
    5522: "Stray (Large) (DLC)",  # TODO: guess, very similar to 5520
    5523: "Stray (Small) (DLC)",
    5524: "Shaggy Stray (Large) (DLC)",
    5525: "Shaggy Stray (Small) (DLC)",
    5526: "Blistered Stray (Large) (DLC)",
    5527: "Blistered Stray (Small) (DLC)",
    5530: "Giant Bat (DLC)",
    5540: "Wolf (DLC)",
    5541: "Wolf (Large) (DLC)",
    5560: "Fingercreeper (Small) (DLC)",
    5570: "Marionette (DLC)",
    5580: "Jagged Peak Drake",
    5590: "Slime (DLC)",
    5591: "Slime (Large) (DLC)",
    5600: "Skeleton (DLC)",
    5620: "Tibia Mariner (DLC)",
    5630: "Crayfish (DLC)",
    5640: "Crab (Large) (DLC)",
    5641: "Crab (Small) (DLC)",
    5651: "Messmer Foot Soldier",
    5661: "Vulgar Militia (DLC)",
    5680: "Messmer Giant Ballista",
    5690: "Messmer Flamethrower",
    5700: "Demi-Human",
    5701: "Large Demi-Human",
    5710: "Demi-Human Shaman",
    5720: "Demi-Human Chief",
    5730: "Demi-Human Queen",
    5740: "Kindred of Rot",
    5750: "Living Jar (Large) (DLC)",
    5751: "Living Jar (Small) (DLC)",
    5760: "Rat (Small) (DLC)",
    5761: "Rat (Large) (DLC)",
    5780: "Runebear (DLC)",
    5790: "Guardian Golem (DLC)",
    5800: "Crucible Knight (DLC)",
    5810: "Demi-Human Swordmaster",
    5820: "Red Runebear",
    5830: "Messmer Soldier",
    5840: "Messmer Knight",
    5850: "Giant Sheep",
    5860: "Ghostflame Dragon",
    5870: "Fanged Imp (DLC)",  # only flower and bigmouth variants
    5871: "Bigmouth Imp (Large)",
    5872: "Bigmouth Imp (Giant)",
    5880: "Catacombs Sorcerer",
    5890: "Messmer Knight's Horse",
    5900: "Fly-Man",
    5910: "Hornsent Grandam",
    5920: "Magma Wyrm (DLC)",
    5930: "Undead Mariner (DLC)",
    5931: "Undead Beastman Mariner (DLC)",
    5940: "Sentry Stones (DLC)",
    5950: "Leonine Misbegotten (DLC)",
    5960: "Ulcerated Tree Spirit (DLC)",
    5970: "Abductor Virgin (DLC)",
    5980: "Omenkiller (DLC)",
    5990: "Basilisk (DLC)",

    6201: "Scarab (DLC)",
    6210: "Albinauric Archer (DLC)",
    6220: "Albinauric Archer Wolf (DLC)",
    6231: "Depraved Perfumer (DLC)",
    6232: "Raya Lucaria Scholar (DLC)",
    6233: "Noble's Page (DLC)",
    6240: "Empty (c6240)",
    6251: "Tree Sentinel (DLC)",
    6260: "Death Rite Bird (DLC)",
    6270: "Royal Revenant (DLC)",
    6290: "Misbegotten (DLC)",
    6291: "Misbegotten (Large) (DLC)",
    6300: "Snail (DLC)",
    6310: "Morningstar Beast (DLC)",
    6320: "Wandering Noble (DLC)",
    # endregion
}
