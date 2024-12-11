from __future__ import annotations

__all__ = ["MapFieldMetadata", "MapFieldInfo", "FIELD_INFO"]

from dataclasses import dataclass
from enum import IntEnum

from soulstruct.base.game_types import GAME_TYPE


@dataclass(slots=True)
class MapFieldMetadata:
    """Stores extra display-related information about an `MSBEntry` field.

    If not used for a field, it will be generated by that `MSBEntry` class from defaults in `FIELD_INFO` below. Note
    that `game_type` must always be specified in the class, though, as these types are typically game-specific.

    Has to be mutable, as nickname/tooltip may be added later by `MSBEntry`.
    """
    nickname: str = ""
    tooltip: str = ""
    game_type: GAME_TYPE = None


def MapFieldInfo(
    nickname="", tooltip="", game_type: GAME_TYPE | type[IntEnum] = None
) -> dict[str, dict[str, MapFieldMetadata]]:
    """Convenience 'metadata' dictionary generator for use with ** in `field()`."""
    return {"metadata": {"msb": MapFieldMetadata(nickname, tooltip, game_type)}}


# Maps assorted MSB field names (across all types) to their display names and tooltips for the GUI.
# Used as default info if field metadata is unspecified. Subtype key is checked first, then supertype as fallback.
FIELD_INFO = {

    # region MODELS
    "MODELS[sib_path]": (
        "Placeholder Path",
        "Internal path to model placeholder SIB file. The path's base name should match the model name.",
    ),
    # endregion

    # region REGIONS
    "REGIONS[translate]": (
        "Translate",
        "3D coordinates of the region's position. Note that this is the middle of the bottom face for box regions.",
    ),
    "REGIONS[rotate]": (
        "Rotate", "Euler angles for region rotation around its local X, Y, and Z axes.",
    ),
    "REGIONS[shape]": (
        "Shape",
        "Shape of region, which vary in used dimensions. Width, height, and depth correspond to game X, Y, and Z.",
    ),
    "REGIONS[entity_id]": (
        "Entity ID",
        "Entity ID for region, for referring to it in EMEVD event scripts.",
    ),

    "Object[break_term]": (
        "Break Term",
        "Unknown. Related to object breakage.",
    ),
    "Object[net_sync_type]": (
        "Net Sync Type",
        "Unknown. Related to online object synchronization.",
    ),
    "Object[collision_hit_filter]": (
        "Collision Hit Filter",
        "Unclear what this does when enabled.",
    ),

    # DS1
    "Object[default_animation]": (
        "Default Animation ID",
        "Default animation for object to play (or just pose in)."
    ),
    "Object[set_main_object_structure_bools]": (
        "Set Main Object Structure Bools",
        "Unknown.",
    ),
    "Object[unk_x0e]": (
        "Unknown [0e-10]",
        "Unknown.",
    ),
    "Object[unk_x10]": (
        "Unknown [10-14]",
        "Unknown.",
    ),
    # endregion (All Games)

    # region PARTS
    "PARTS[model]": (
        "Part Model",
        "Model in MSB to use for instantiating this part.",
    ),
    "PARTS[entity_id]": (
        "Entity ID",
        "Entity ID for part, for referring to it in EMEVD event scripts.",
    ),
    "PARTS[sib_path]": (
        "Placeholder Path",
        "Internal path to part/model placeholder SIB file. Generally constant per subtype and ends in 'layout.sib'.",
    ),
    "PARTS[draw_parent]": (
        "Draw Parent",
        "Part will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn. Used as "
        "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set). Set "
        "to `None` to indicate no draw parent and force the use of draw groups instead.",
    ),
    "PARTS[translate]": (
        "Translate", "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
    ),
    "PARTS[rotate]": (
        "Rotate", "Euler angles for part rotation around its local X, Y, and Z axes.",
    ),
    "PARTS[scale]": (
        "Scale",
        "Scale of part. Only works for Map Pieces and Objects.",
    ),
    "PARTS[draw_groups]": (
        "Draw Groups",
        "Draw groups of part. This part will be drawn when the corresponding display group is active.",
    ),
    "PARTS[display_groups]": (
        "Display Groups",
        "Display groups are present in all MSB Parts, but only function for collisions.",
    ),
    "PARTS[ambient_light_id]": (
        "Ambient Light ID",
        "ID of Ambient Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[fog_id]": (
        "Fog ID",
        "ID of Fog parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[scattered_light_id]": (
        "Scattered Light ID",
        "ID of Scattered Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[lens_flare_id]": (
        "Lens Flare ID",
        "ID of Lens Flare parameter (both types) to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[shadow_id]": (
        "Shadow ID",
        "ID of Shadow parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[dof_id]": (
        "Depth of Field ID",
        "ID of Depth Of Field ID parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[tone_map_id]": (
        "Tone Map ID",
        "ID of Tone Map parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[point_light_id]": (
        "Point Light ID",
        "ID of Point Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[tone_correction_id]": (
        "Tone Correction ID",
        "ID of Tone Correction parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "PARTS[lod_id]": (
        "Level of Detail ID",
        "Level of Detail (LoD) parameter. Always -1 or 0, seemingly at random; probably unused.",
    ),
    "PARTS[is_shadow_source]": (
        "Casts Shadow",
        "If True, this entity will cast dynamic shadows.",
    ),
    "PARTS[is_shadow_destination]": (
        "Receives Shadow",
        "If True, this entity can have dynamic shadows cast onto it.",
    ),
    "PARTS[is_shadow_only]": (
        "Only Casts Shadow",
        "If True, this entity only casts shadows.",
    ),
    "PARTS[draw_by_reflect_cam]": (
        "Is Reflected",
        "If True, this entity will be reflected in water, etc.",
    ),
    "PARTS[draw_only_reflect_cam]": (
        "Is Only Reflected",
        "If True, this entity will only be drawn in reflections in water, etc.",
    ),
    "PARTS[use_depth_bias_float]": (
        "Use Depth Bias Float",
        "Unknown.",
    ),
    "PARTS[disable_point_light_effect]": (
        "Ignore Point Lights",
        "If True, this entity will not be illuminated by point lights (I think).",
    ),

    "MapPiece[model]": (
        "Map Piece Model",
        "Model in MSB to use for instantiating this map piece.",
    ),

    "Object[model]": (
        "Object Model",
        "Model in MSB to use for instantiating this object.",
    ),
    "Object[animation_ids]": (
        "Animation IDs",
        "Default animation IDs for object (e.g. corpse poses). Only the first is used, according to Pav.",
    ),
    "Object[model_vfx_param_id_offsets]": (
        "Model VFX Param ID Offsets",
        "Offsets for model VFX param IDs. Only the first is used, according to Pav.",
    ),

    "Character[model]": (
        "Character Model",
        "Model in MSB to use for instantiating this character.",
    ),
    "Character[ai_id]": (
        "AI ID",
        "Character's AI param ID. If set to -1, the default AI ID from the Character param (below) will be used.",
    ),
    "Character[character_id]": (
        "Character ID",
        "Character's main Character param ID, which contains basic character information. For 'player' characters "
        "who use model c0000, most of the fields in this param are unused (e.g. health is determined by their "
        "Vitality stat rather than the HP field in this param).",
    ),
    "Character[talk_id]": (
        "Talk Script ID",
        "Talk ID of character, which determines their interactions (conversations, shops, etc.). This is used "
        "to look up the corresponding 't{talk_id}.esd' file inside the 'talkesdbnd' file for this map.",
    ),
    "Character[player_id]": (
        "Player ID",
        "Player ID of character, which is used to initialize the stats, appearance, equipment, etc. of 'player' "
        "characters ('NPCs') who use model c0000. Unused (-1) for all other character models.",
    ),
    "Character[platoon_id]": (
        "Platoon ID",
        "Unknown",
    ),
    "Character[patrol_type]": (
        "Patrol Type",
        "Unknown",
    ),
    "Character[patrol_regions]": (
        "Patrol Regions",
        "List of regions that this character will patrol between (if they have standard AI logic).",
    ),
    "Character[default_animation]": (
        "Default Animation ID",
        "Default standby animation to loop for character (e.g. sitting, leaning, clutching head in hands).",
    ),
    "Character[damage_animation]": (
        "Damage Animation ID",
        "Default damage animation to use for character.",
    ),

    "PlayerStart[model]": (
        "Player Model [c0000]",
        "Character model to use for this PlayerStart. This should always be c0000.",
    ),

    "Collision[model]": (
        "Collision Model",
        "Model in MSB to use for instantiating this collision.",
    ),
    "Collision[display_groups]": (
        "Display Groups",
        "Display groups of collision. These display groups will be active when the player is standing on this "
        "Collision, which will draw any parts with an overlapping draw group.",
    ),
    "Collision[hit_filter_id]": (
        "Hit Filter ID",
        "Determines what happens when the player activates this collision (normal physics, killplane, etc.).",
    ),
    "Collision[sound_space_type]": (
        "Sound Space Type",
        "Determines how sounds are filtered when player is standing on this collision.",
    ),
    "Collision[environment_event]": (
        "Environment Event",
        "Environment MSB event in map that determines ambience when standing on this collision.",
    ),
    "Collision[reflect_plane_height]": (
        "Reflect Plane Height",
        "Vertical height of the reflect plane for this collision (for screen space reflections).",
    ),
    "Collision[place_name_banner_id]": (
        "Place Name",
        "ID of place/zone banner that is shown when you step on this collision, which involves both a linked texture "
        "ID lookup), a 'PlaceName' text lookup shown at the character select screen, and a 'PlaceName' text lookup for "
        "an optional subtitle that can appear below the banner (all blank in DS1 by default and possibly disabled in "
        "later games).\n\n"
        "Set it to -1 to use the default place ID for this map, e.g. to use 1001 for map m10_01_00_00.",
    ),
    "Collision[force_place_name_banner]": (
        "Show Place Name Banner",
        "By default, the game will only show a place name banner when you enter a map (e.g. after warping). If "
        "this option is enabled, the place name banner will be shown when you step on this collision if the area ID "
        "changes to a new value. Typical usage is to have this disabled for collisions that are very close to a "
        "different place (a 'silent zone transition') and have it enabled for collisions that are further away, "
        "which produces a 'delayed zone banner' effect.\n\n"
        ""
        "Do NOT enable this for two adjacent collisions with different place names, or moving back and forth "
        "between those collisions will build up a huge queue of place  banners to display, which can only be cleared "
        "by restarting the game entirely!",
    ),
    "Collision[starts_disabled]": (
        "Starts Disabled",
        "If True, this collision is disabled on map load and must be manually enabled with an event script.",
    ),
    "Collision[play_region_id]": (
        "Play Region ID",
        "Determines the multiplayer (e.g. invasion) sub-area this collision is part of. If set to 0 (default), no "
        "multiplayer activity can occur while the player is on this collision.\n\n"
        ""
        "NOTE: This field shares space with Stable Footing Flag, so only one of them can be set to a non-zero "
        "value per collision.",
    ),
    "Collision[stable_footing_flag]": (
        "Stable Footing Flag",
        "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
        "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
        "defeated. If set to 0 (default), stable footing is ALWAYS updated here. If set to -1, stable footing is "
        "NEVER updated here.\n\n"
        ""
        "NOTE: This field shares space with Play Region ID, so only one of them can be set to a non-zero value "
        "per collision.",
    ),
    "Collision[camera_1_id]": (
        "Camera Param ID 1",
        "First camera ID to use on this collision. Unsure how the two slots differ.",
    ),
    "Collision[camera_2_id]": (
        "Camera Param ID 2",
        "Second camera ID to use on this collision. Unsure how the two slots differ.",
    ),

    "Collision[attached_bonfire]": (
        "Attached Bonfire",
        "If this is set to a bonfire entity ID, that bonfire will be unusable if any living enemy characters are "
        "on this collision. Note that this also checks for enemies that are disabled by events.",
    ),
    "Collision[vagrant_entity_ids]": (
        "Vagrant Entity IDs",
        "Entity IDs of Vagrants that will appear on this collision. Handled internally (not EMEVD).",
    ),
    "Collision[unk_x27_x28]": (
        "Unknown [27-28]",
        "Unknown. Almost always zero, but see e.g. Anor Londo spinning tower collision.",
    ),
    "Collision[navmesh_groups]": (
        "Navmesh Groups",
        "Controls collision backread.",
    ),

    "Collision[attached_lantern]": (
        "Attached Lantern",
        "If this is set to a lantern entity ID, that lantern will be unusable if any living enemy characters are "
        "on this collision. Note that this also checks for enemies that are disabled by events.",
    ),

    "Navmesh[navmesh_groups]": (
        "Navmesh Groups",
        "Controls collision backread.",
    ),

    "ConnectCollision[collision]": (
        "Collision Part Name",
        "Collision part that triggers this connect collision.",
    ),
    "ConnectCollision[connected_map_id]": (
        "Map ID",
        "(AA, BB, CC, DD) sequence of the map to be loaded (corresponding to file 'mAA_BB_CC_DD). "
        "-1 and 0 mean the same thing.",
    ),
    # endregion

    # region EVENTS
    "EVENTS[entity_id]": (
        "Entity ID",
        "Entity ID for event. Not used for this event type.",
    ),
    "EVENTS[attached_part]": (
        "Attached Part",
        "MSB part to which event is attached. Not used for this event type.",
    ),
    "EVENTS[attached_region]": (
        "Attached Region",
        "MSB region to which event is attached. Not used for this event type.",
    ),
    "EVENTS[unknowns]": (
        "Unknown Integers",
        "Four unknown integers that appear in all events.",
    ),

    # DS1
    "Light[attached_part]": (
        "Draw Parent",
        "Light will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "Light[attached_region]": (
        "Light Region",
        "Region (usually a Point) at which Light appears.",
    ),
    "Light[point_light_id]": (
        "Point Light",
        "Point Light lighting parameter ID to use for this light.",
    ),

    "Sound[attached_part]": (
        "Sound Parent Part",
        "If given, sound will only be audible if this MSB part is being drawn (I think). Usually a Map Piece or "
        "Collision.",
    ),
    "Sound[attached_region]": (
        "Sound Region",
        "Sound will only be audible while player is inside this region.",
    ),
    "Sound[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to sound event in other files (e.g. EMEVD).",
    ),
    "Sound[sound_type]": (
        "Sound Type",
        "Type of sound, which is used to find the sound data (sound name prefix letter).",
    ),
    "Sound[sound_id]": (
        "Sound ID",
        "Sound data ID, which refers to an ID in loaded sound events.",
    ),

    "VFX[attached_part]": (
        "Draw Parent",
        "VFX will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "VFX[attached_region]": (
        "VFX Region",
        "Region (usually a Point) at which VFX appears.",
    ),
    "VFX[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to this VFX in other game files.",
    ),
    "VFX[vfx_id]": (
        "VFX ID",
        "Visual effect ID, which refers to a loaded VFX file.",
    ),
    "VFX[starts_disabled]": (
        "Starts Disabled",
        "VFX will not be automatically created on map load (requires event script).",
    ),

    # DS1
    "Wind[wind_vector_min]": (
        "Wind Vector Min",
        "Wind vector minimum.",
    ),
    "Wind[unk_x04_x08]": (
        "Unknown [04-08]",
        "Unknown Wind parameter (floating-point number).",
    ),
    "Wind[wind_vector_max]": (
        "Wind Vector Max",
        "Wind vector maximum.",
    ),
    "Wind[unk_x0c_x10]": (
        "Unknown [0c-10]",
        "Unknown Wind parameter (floating-point number).",
    ),
    "Wind[wind_swing_cycles]": (
        "Wind Swing Cycles",
        "Wind swing cycles (four values).",
    ),
    "Wind[wind_swing_powers]": (
        "Wind Swing Powers",
        "Wind swing powers (four values).",
    ),

    "Treasure[treasure_part]": (
        "Treasure Object",
        "Object on which treasure will appear (usually a corpse or chest).",
    ),
    "Treasure[item_lot_1]": (
        "Item Lot 1",
        "First item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "Treasure[item_lot_2]": (
        "Item Lot 2",
        "Second item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "Treasure[item_lot_3]": (
        "Item Lot 3",
        "Third item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "Treasure[item_lot_4]": (
        "Item Lot 4",
        "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "Treasure[item_lot_5]": (
        "Item Lot 5",
        "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "Treasure[is_in_chest]": (
        "Is In Chest",
        "Indicates if this treasure is inside a chest (affects appearance).",  # TODO: effect?
    ),
    "Treasure[is_hidden]": (
        "Is Hidden",
        "If True, this treasure will start disabled and will need to be enabled manually with an event script.",
    ),
    "Treasure[unknown_x1c_x20]": (
        "Unknown [1c-20]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x20_x24]": (
        "Unknown [20-24]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x24_x28]": (
        "Unknown [24-28]",
        "Unknown integer.",
        ),
    "Treasure[unknown_x28_x2c]": (
        "Unknown [28-2c]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x2c_x30]": (
        "Unknown [2c-30]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x30_x34]": (
        "Unknown [30-34]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x34_x38]": (
        "Unknown [34-38]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x38_x3c]": (
        "Unknown [38-3c]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x3c_x40]": (
        "Unknown [3c-40]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x42_x44]": (
        "Unknown [42-44]",
        "Unknown short.",
    ),
    "Treasure[unknown_x44_x48]": (
        "Unknown [44-48]",
        "Unknown integer.",
    ),
    "Treasure[unknown_x48_x4c]": (
        "Unknown [48-4c]",
        "Unknown integer.",
    ),

    "Spawner[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Spawner in other game files.",
    ),
    "Spawner[max_count]": (
        "Max Count",
        "Unsure; I suspect this is the total number of entities this spawner can produce.",
    ),
    "Spawner[spawner_type]": (
        "Spawner Type",
        "Unsure what this enumeration is.",
    ),
    "Spawner[limit_count]": (
        "Limit Count",
        "Unsure; I suspect this is the number of spawned entities that can be alive at once.",
    ),
    "Spawner[min_spawner_count]": (
        "Min Spawner Count",
        "Unsure.",
    ),
    "Spawner[max_spawner_count]": (
        "Max Spawner Count",
        "Unsure.",
    ),
    "Spawner[min_interval]": (
        "Min Interval",
        "Minimum number of seconds between spawns.",
    ),
    "Spawner[max_interval]": (
        "Max Interval",
        "Maximum number of seconds between spawns.",
    ),
    "Spawner[initial_spawn_count]": (
        "Initial Spawn Count",
        "Unsure; I suspect this is the number of entities spawned immediately on map load.",
    ),
    "Spawner[spawn_parts]": (
        "Spawn Characters",
        "Entities that will be spawned at given regions.",
    ),
    "Spawner[spawn_regions]": (
        "Spawn Regions",
        "Regions where entities will be spawned.",
    ),

    "Message[attached_part]": (
        "Draw Parent",
        "Message will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "Message[attached_region]": (
        "Message Region",
        "Region (usually a Point) at which Message appears.",
    ),
    "Message[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Message in other game files.",
    ),
    "Message[text_id]": (
        "Message Text ID",
        "Soapstone Messages text ID shown when soapstone message is examined.",
    ),
    "Message[unk_x02_x04]": (
        "Unknown [02-04]",
        "Unknown. Often set to 2.",
    ),
    "Message[is_hidden]": (
        "Is Hidden",
        "If True, the message must be manually enabled with an event script or by using Seek Guidance.",
    ),

    "ObjAct[obj_act_entity_id]": (
        "ObjAct Entity ID",
        "ID that identifies this object activation event in event scripts.",
    ),
    "ObjAct[obj_act_part]": (
        "Object",
        "Object to which this object activation event is attached.",
    ),
    "ObjAct[obj_act_param_id]": (
        "ObjAct Param",
        "Param entry containing information about this object activation event. If it is -1, it will "
        "default to the model ID of the object it is attached to.",
    ),
    "ObjAct[obj_act_state]": (
        "ObjAct State",
        "State of object activation. Known values include Default (0), Door (1), and Loop (2).",
    ),
    "ObjAct[obj_act_flag]": (
        "ObjAct Flag",
        "Flag that stores the persistent state (e.g. open/closed) of this object activation.",
    ),

    # DS1
    "NPCInvasion[base_region_name]": (
        "Invasion Region",
        "Region in which NPC Invasion event can be triggered (e.g. with Black Eye Orb).",
    ),
    "NPCInvasion[host_entity_id]": (
        "Host Entity ID",
        "Entity ID of NPC character to be invaded.",
    ),
    "NPCInvasion[invasion_flag_id]": (
        "Invasion Flag",
        "Flag that is enabled while the invasion is active, which should trigger changes to the world.",
    ),
    "NPCInvasion[spawn_point_region_name]": (
        "Spawn Point Region",
        "Region where player will spawn during invasion event.",
    ),

    # Bloodborne
    "WindVFX[attached_part]": (
        "Draw Parent",
        "VFX will be drawn if this parent (usually a Collision or Map Piece part) is drawn. Possibly unused.",
    ),
    "WindVFX[attached_region]": (
        "Attached Region",
        "Base event region. Probably unused with WindVFX (see Wind Region Name instead).",
    ),
    "WindVFX[wind_region]": (
        "VFX Region",
        "Region at or in which WindVFX appears.",
    ),
    "WindVFX[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to this VFX in other game files. Possibly unused with WindVFX.",
    ),
    "WindVFX[vfx_id]": (
        "VFX ID",
        "Visual effect ID, which refers to a loaded VFX file.",
    ),
    "WindVFX[unk_x08_x0c]": (
        "Unknown [08-0c]",
        "Unknown floating-point number.",
    ),

    "PatrolRoute[attached_part]": (
        "Draw Parent",
        "Probably unused for Patrol Route.",
    ),
    "PatrolRoute[attached_region]": (
        "Attached Region",
        "Probably unused for Patrol Route.",
    ),
    "PatrolRoute[entity_id]": (
        "Entity ID",
        "Probably unused for Patrol Route.",
    ),
    "PatrolRoute[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown integer.",
    ),
    "PatrolRoute[patrol_regions]": (
        "Patrol Regions",
        "List of regions that define this Patrol Route."
    ),

    "DarkLock[attached_part]": (
        "Draw Parent",
        "Probably unused for Dark Lock.",
    ),
    "DarkLock[attached_region]": (
        "Attached Region",
        "Probably unused for Dark Lock.",
    ),
    "DarkLock[entity_id]": (
        "Entity ID",
        "Probably unused for Dark Lock.",
    ),

    "Platoon[attached_part]": (
        "Draw Parent",
        "Probably unused for Platoon.",
    ),
    "Platoon[attached_region]": (
        "Attached Region",
        "Probably unused for Platoon.",
    ),
    "Platoon[entity_id]": (
        "Entity ID",
        "Probably unused for Platoon.",
    ),
    "Platoon[platoon_characters]": (
        "Platoon Character Names",
        "Characters in this Platoon.",
    ),
    "Platoon[platoon_parents]": (
        "Platoon Parent Names",
        "Parent parts of this Platoon.",
    ),
    "Platoon[platoon_id_script_activate]": (
        "Platoon Active Script ID",
        "Unknown. Possibly an AI param ID.",
    ),
    "Platoon[state]": (
        "Platoon State",
        "Unknown.",
    ),

    "MultiSummon[attached_part]": (
        "Draw Parent",
        "Probably unused for Multi Summon.",
    ),
    "MultiSummon[attached_region]": (
        "Attached Region",
        "Probably unused for Multi Summon.",
    ),
    "MultiSummon[entity_id]": (
        "Entity ID",
        "Probably unused for Multi Summon.",
    ),
    "MultiSummon[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown integer.",
    ),
    "MultiSummon[unk_x04_x06]": (
        "Unknown [04-06]",
        "Unknown 16-bit integer.",
    ),
    "MultiSummon[unk_x06_x08]": (
        "Unknown [06-08]",
        "Unknown 16-bit integer.",
    ),
    "MultiSummon[unk_x08_x0a]": (
        "Unknown [08-0a]",
        "Unknown 16-bit integer.",
    ),
    "MultiSummon[unk_x0a_x0c]": (
        "Unknown [0a-0c]",
        "Unknown 16-bit integer.",
    ),

    "SpawnPoint[attached_part]": (
        "Draw Parent",
        "Some Spawn Points use this; unclear what it does, but it is presumably the Collision of the Spawn Point.",
    ),
    "SpawnPoint[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Spawn Point in other game files.",
    ),
    "SpawnPoint[spawn_point_region]": (
        "Spawn Point Region",
        "Region where player will spawn when registered to this spawn point.",
    ),

    "MapOffset[translate]": (
        "Translate",
        "Vector of (x, y, z) coordinates of map offset.",
    ),
    "MapOffset[rotate_y]": (
        "Y Rotation",
        "Euler angle of rotation around the Y (vertical) axis.",
    ),

    "Navigation[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Navigation event in other game files.",
    ),
    "Navigation[navigation_region]": (
        "Navmesh Region",
        "Region to which Navigation event is attached, which encloses faces of one or more Navmesh parts.",
    ),

    "Environment[attached_part]": (
        "Draw Parent",
        "Environment (or 'map spot') will be drawn whenever its parent is drawn.",
    ),
    "Environment[attached_region]": (
        "Environment Region",
        "Region (usually a Point) at which Environment appears (whatever that means).",
    ),
    "Environment[entity_id]": (
        "Environment ID",
        "Unknown index. Note that this replaces the usual Entity ID field.",
    ),
    "Environment[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown Environment parameter (integer).",
    ),
    "Environment[unk_x04_x08]": (
        "Unknown [04-08]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "Environment[unk_x08_x0c]": (
        "Unknown [08-0c]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "Environment[unk_x0c_x10]": (
        "Unknown [0c-10]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "Environment[unk_x10_x14]": (
        "Unknown [10-14]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "Environment[unk_x14_x18]": (
        "Unknown [14-18]",
        "Unknown Environment parameter (floating-point number).",
    ),
    # endregion

}
