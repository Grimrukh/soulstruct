
__all__ = ["FIELD_INFO"]

# Maps assorted MSB field names (across all types) to their display names and descriptions for the GUI.
# Used as default info if field metadata is unspecified.
FIELD_INFO = {
    "model": (
        "Part Model",
        "Model in MSB to use for instantiating this part.",
    ),
    "sib_path": (
        "Placeholder Path",
        "Internal path to model placeholder SIB file. The path's base name should match the model name.",
    ),
    "draw_parent": (
        "Draw Parent",
        "Object will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn. Used as "
        "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set). Set "
        "to `None` to indicate no draw parent and force the use of draw groups instead.",
    ),

    "parts[translate]": (
        "Translate", "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
    ),
    "parts[rotate]": (
        "Rotate", "Euler angles for part rotation around its local X, Y, and Z axes.",
    ),
    "parts[scale]": (
        "Scale",
        "Scale of part. Only works for Map Pieces and Objects.",
    ),
    "parts[sib_path]": (
        "SIB Placeholder Path",
        "Internal path to SIB placeholder file for part.",
    ),
    "parts[draw_groups]": (
        "Draw Groups",
        "Draw groups of part. This part will be drawn when the corresponding display group is active.",
    ),
    "parts[display_groups]": (
        "Display Groups",
        "Display groups are present in all MSB Parts, but only function for collisions.",
    ),
    "parts[ambient_light_id]": (
        "Ambient Light ID",
        "ID of Ambient Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[fog_id]": (
        "Fog ID",
        "ID of Fog parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[scattered_light_id]": (
        "Scattered Light ID",
        "ID of Scattered Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[lens_flare_id]": (
        "Lens Flare ID",
        "ID of Lens Flare parameter (both types) to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[shadow_id]": (
        "Shadow ID",
        "ID of Shadow parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[dof_id]": (
        "Depth of Field ID",
        "ID of Depth Of Field ID parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[tone_map_id]": (
        "Tone Map ID",
        "ID of Tone Map parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[point_light_id]": (
        "Point Light ID",
        "ID of Point Light parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[tone_correction_id]": (
        "Tone Correction ID",
        "ID of Tone Correction parameter to use from this map's lighting parameters (DrawParam).",
    ),
    "parts[lod_id]": (
        "Level of Detail ID",
        "Level of Detail (LoD) parameter. Always -1 or 0, seemingly at random; probably unused.",
    ),
    "parts[is_shadow_source]": (
        "Casts Shadow",
        "If True, this entity will cast dynamic shadows.",
    ),
    "parts[is_shadow_destination]": (
        "Receives Shadow",
        "If True, this entity can have dynamic shadows cast onto it.",
    ),
    "parts[is_shadow_only]": (
        "Only Casts Shadow",
        "If True, this entity only casts shadows.",
    ),
    "parts[draw_by_reflect_cam]": (
        "Is Reflected",
        "If True, this entity will be reflected in water, etc.",
    ),
    "parts[draw_only_reflect_cam]": (
        "Is Only Reflected",
        "If True, this entity will only be drawn in reflections in water, etc.",
    ),
    "parts[use_depth_bias_float]": (
        "Use Depth Bias Float",
        "Unknown.",
    ),
    "parts[disable_point_light_effect]": (
        "Ignore Point Lights",
        "If True, this entity will not be illuminated by point lights (I think).",
    ),

    "regions[translate]": (
        "Translate",
        "3D coordinates of the region's position. Note that this is the middle of the bottom face for box regions.",
    ),
    "circles[radius]": (
        "Radius",
        "Radius (in xy-plane) of circular region.",
    ),
    "spheres[radius]": (
        "Radius",
        "Radius of sphere-shaped region.",
    ),
    "cylinders[radius]": (
        "Radius",
        "Radius (in xz-plane) of cylinder-shaped region.",
    ),
    "cylinders[height]": (
        "Height",
        "Height (along y-axis) of cylinder-shaped region.",
    ),
    "rects[width]": (
        "Width",
        "Width (along x-axis) of rectangle-shaped region.",
    ),
    "rects[height]": (
        "Height",
        "Height (along y-axis) of rectangle-shaped region.",
    ),

    "boxes[width]": (
        "Width",
        "Width (along x-axis) of box-shaped region.",
    ),
    "boxes[depth]": (
        "Depth",
        "Depth (along z-axis) of box-shaped region.",
    ),
    "boxes[height]": (
        "Height",
        "Height (along y-axis) of box-shaped region.",
    ),

    "objects[break_term]": (
        "Break Term",
        "Unknown. Related to object breakage.",
    ),
    "objects[net_sync_type]": (
        "Net Sync Type",
        "Unknown. Related to online object synchronization.",
    ),
    "objects[collision_hit_filter]": (
        "Collision Hit Filter",
        "Unclear what this does when enabled.",
    ),

    # DS1
    "objects[default_animation_id]": (
        "Default Animation ID",
        "Default animation for object to play (or just pose in)."
    ),
    "objects[set_main_object_structure_bools]": (
        "Set Main Object Structure Bools",
        "Unknown.",
    ),
    "objects[unk_x0e_x10]": (
        "Unknown [0e-10]",
        "Unknown.",
    ),
    "objects[unk_x10_x14]": (
        "Unknown [10-14]",
        "Unknown.",
    ),

    # Bloodborne
    "objects[animation_ids]": (
        "Animation IDs",
        "Default animation IDs for object (e.g. corpse poses). Only the first is used, according to Pav.",
    ),
    "objects[model_vfx_param_id_offsets]": (
        "Model VFX Param ID Offsets",
        "Offsets for model VFX param IDs. Only the first is used, according to Pav.",
    ),

    "characters[ai_id]": (
        "AI ID",
        "Character's AI param ID. If set to -1, the default AI ID from the Character param (below) will be used.",
    ),
    "characters[character_id]": (
        "Character ID",
        "Character's main Character param ID, which contains basic character information. For 'player' characters "
        "who use model c0000, most of the fields in this param are unused (e.g. health is determined by their "
        "Vitality stat rather than the HP field in this param).",
    ),
    "characters[talk_id]": (
        "Talk Script ID",
        "Talk ID of character, which determines their interactions (conversations, shops, etc.). This is used "
        "to look up the corresponding 't{talk_id}.esd' file inside the 'talkesdbnd' file for this map.",
    ),
    "characters[player_id]": (
        "Player ID",
        "Player ID of character, which is used to initialize the stats, appearance, equipment, etc. of 'player' "
        "characters ('NPCs') who use model c0000. Unused (-1) for all other character models.",
    ),
    "characters[patrol_regions]": (
        "Patrol Regions",
        "List of regions that this character will patrol between (if they have standard AI logic).",
    ),
    "characters[default_animation]": (
        "Default Animation ID",
        "Default standby animation to loop for character (e.g. sitting, leaning, clutching head in hands).",
    ),
    "characters[damage_animation]": (
        "Damage Animation ID",
        "Default damage animation to use for character.",
    ),

    "player_starts[model]": (
        "Player Start Model (c0000)",
        "Character model to use for this PlayerStart. This should always be c0000.",
    ),

    "collisions[display_groups]": (
        "Display Groups",
        "Display groups of collision. These display groups will be active when the player is standing on this "
        "Collision, which will draw any parts with an overlapping draw group.",
    ),
    "collisions[hit_filter_id]": (
        "Hit Filter ID",
        "Determines what happens when the player activates this collision (normal physics, killplane, etc.).",
    ),
    "collisions[sound_space_type]": (
        "Sound Space Type",
        "Determines how sounds are filtered when player is standing on this collision.",
    ),
    "collisions[environment_event]": (
        "Environment Event",
        "Environment MSB event in map that determines ambience when standing on this collision.",
    ),
    "collisions[reflect_plane_height]": (
        "Reflect Plane Height",
        "Vertical height of the reflect plane for this collision (for screen space reflections).",
    ),
    "collisions[place_name_banner_id]": (
        "Area Name",
        "Name of area that this collision is in, which determines the area banner that is shown when you step on "
        "this collision (a linked texture ID lookup) and the area name that appears in the load screen (text ID). "
        "Set it to -1 to use the default area name for this map (i.e. text ID XXYY for map 'mXX_YY').",
    ),
    "collisions[force_place_name_banner]": (
        "Show Area Banner",
        "By default, the game will only show an area name banner when you enter a map (e.g. after warping). If "
        "this option is enabled, the area name banner will be shown when you step on this collision if the area ID "
        "changes to a new value. Typical usage is to have this disabled for collisions that are very close to a "
        "different area (a 'silent area transition') and have it enabled for collisions that are further away, "
        "which produces a 'delayed area banner' effect.\n\n"
        ""
        "Do NOT enable this for two adjacent collisions with different area names, or moving back and forth "
        "between those collisions will build up a huge queue of area banners to display, which can only be cleared "
        "by restarting the game entirely.",
    ),
    "collisions[starts_disabled]": (
        "Starts Disabled",
        "If True, this collision is disabled on map load and must be manually enabled with an event script.",
    ),
    "collisions[play_region_id]": (
        "Play Region ID",
        "Determines the multiplayer (e.g. invasion) sub-area this collision is part of. If set to 0 (default), no "
        "multiplayer activity can occur while the player is on this collision.\n\n"
        ""
        "NOTE: This field shares space with Stable Footing Flag, so only one of them can be set to a non-zero "
        "value per collision.",
    ),
    "collisions[stable_footing_flag]": (
        "Stable Footing Flag",
        "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
        "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
        "defeated. If set to 0 (default), stable footing is ALWAYS updated here. If set to -1, stable footing is "
        "NEVER updated here.\n\n"
        ""
        "NOTE: This field shares space with Play Region ID, so only one of them can be set to a non-zero value "
        "per collision.",
    ),
    "collisions[camera_1_id]": (
        "Camera Param ID 1",
        "First camera ID to use on this collision. Unsure how the two slots differ.",
    ),
    "collisions[camera_2_id]": (
        "Camera Param ID 2",
        "Second camera ID to use on this collision. Unsure how the two slots differ.",
    ),

    # DS1
    "collisions[attached_bonfire]": (
        "Attached Bonfire",
        "If this is set to a bonfire entity ID, that bonfire will be unusable if any living enemy characters are "
        "on this collision. Note that this also checks for enemies that are disabled by events.",
    ),
    "collisions[vagrant_entity_ids]": (
        "Vagrant Entity IDs",
        "Entity IDs of Vagrants that will appear on this collision. Handled internally (not EMEVD).",
    ),
    "collisions[unk_x27_x28]": (
        "Unknown [27-28]",
        "Unknown. Almost always zero, but see e.g. Anor Londo spinning tower collision.",
    ),
    "collisions[navmesh_groups]": (
        "Navmesh Groups",
        "Controls collision backread.",
    ),

    # Bloodborne
    "collisions[attached_lantern]": (
        "Attached Lantern",
        "If this is set to a lantern entity ID, that lantern will be unusable if any living enemy characters are "
        "on this collision. Note that this also checks for enemies that are disabled by events.",
    ),

    # DS1
    "navmeshes[navmesh_groups]": (
        "Navmesh Groups",
        "Controls collision backread.",
    ),

    "map_connections[collision]": (
        "Collision Part Name",
        "Collision part that triggers this map connection.",
    ),
    "map_connections[connected_map]": (
        "Map ID",
        "Vanilla name or 'mAA_BB_CC_DD'-style name or (AA, BB, CC, DD) sequence of the map to be loaded.",
    ),

    "events[entity_id]": (
        "Entity ID",
        "Entity ID for event. Not used for this event type.",
    ),
    "events[attached_part]": (
        "Attached Part",
        "MSB part to which event is attached. Not used for this event type.",
    ),
    "events[attached_region]": (
        "Attached Region",
        "MSB region to which event is attached. Not used for this event type.",
    ),

    # DS1
    "lights[attached_part]": (
        "Draw Parent",
        "Light will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "lights[attached_region]": (
        "Light Region",
        "Region (usually a Point) at which Light appears.",
    ),
    "lights[point_light_id]": (
        "Point Light",
        "Point Light lighting parameter ID to use for this light.",
    ),

    "sounds[attached_part]": (
        "Sound Parent Part",
        "If given, sound will only be audible if this MSB part is being drawn (I think). Usually a Map Piece or "
        "Collision.",
    ),
    "sounds[attached_region]": (
        "Sound Region",
        "Sound will only be audible while player is inside this region.",
    ),
    "sounds[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to sound event in other files (e.g. EMEVD).",
    ),
    "sounds[sound_type]": (
        "Sound Type",
        "Type of sound, which is used to find the sound data (sound name prefix letter).",
    ),
    "sounds[sound_id]": (
        "Sound ID",
        "Sound data ID, which refers to an ID in loaded sound events.",
    ),

    "vfx[attached_part]": (
        "Draw Parent",
        "VFX will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "vfx[attached_region]": (
        "VFX Region",
        "Region (usually a Point) at which VFX appears.",
    ),
    "vfx[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to this VFX in other game files.",
    ),
    "vfx[vfx_id]": (
        "VFX ID",
        "Visual effect ID, which refers to a loaded VFX file.",
    ),
    "vfx[starts_disabled]": (
        "Starts Disabled",
        "VFX will not be automatically created on map load (requires event script).",
    ),

    # DS1
    "wind[wind_vector_min]": (
        "Wind Vector Min",
        "Wind vector minimum.",
    ),
    "wind[unk_x04_x08]": (
        "Unknown [04-08]",
        "Unknown Wind parameter (floating-point number).",
    ),
    "wind[wind_vector_max]": (
        "Wind Vector Max",
        "Wind vector maximum.",
    ),
    "wind[unk_x0c_x10]": (
        "Unknown [0c-10]",
        "Unknown Wind parameter (floating-point number).",
    ),
    "wind[wind_swing_cycles]": (
        "Wind Swing Cycles",
        "Wind swing cycles (four values).",
    ),
    "wind[wind_swing_powers]": (
        "Wind Swing Powers",
        "Wind swing powers (four values).",
    ),

    "treasure[treasure_part]": (
        "Treasure Object",
        "Object on which treasure will appear (usually a corpse or chest).",
    ),
    "treasures[item_lot_1]": (
        "Item Lot 1",
        "First item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "treasures[item_lot_2]": (
        "Item Lot 2",
        "Second item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "treasures[item_lot_3]": (
        "Item Lot 3",
        "Third item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "treasures[item_lot_4]": (
        "Item Lot 4",
        "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "treasures[item_lot_5]": (
        "Item Lot 5",
        "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
        "awarded.)",
    ),
    "treasures[is_in_chest]": (
        "Is In Chest",
        "Indicates if this treasure is inside a chest (affects appearance).",  # TODO: effect?
    ),
    "treasures[is_hidden]": (
        "Is Hidden",
        "If True, this treasure will start disabled and will need to be enabled manually with an event script.",
    ),
    "treasures[unknown_x1c_x20]": (
        "Unknown [1c-20]",
        "Unknown integer.",
    ),
    "treasures[unknown_x20_x24]": (
        "Unknown [20-24]",
        "Unknown integer.",
    ),
    "treasures[unknown_x24_x28]": (
        "Unknown [24-28]",
        "Unknown integer.",
        ),
    "treasures[unknown_x28_x2c]": (
        "Unknown [28-2c]",
        "Unknown integer.",
    ),
    "treasures[unknown_x2c_x30]": (
        "Unknown [2c-30]",
        "Unknown integer.",
    ),
    "treasures[unknown_x30_x34]": (
        "Unknown [30-34]",
        "Unknown integer.",
    ),
    "treasures[unknown_x34_x38]": (
        "Unknown [34-38]",
        "Unknown integer.",
    ),
    "treasures[unknown_x38_x3c]": (
        "Unknown [38-3c]",
        "Unknown integer.",
    ),
    "treasures[unknown_x3c_x40]": (
        "Unknown [3c-40]",
        "Unknown integer.",
    ),
    "treasures[unknown_x42_x44]": (
        "Unknown [42-44]",
        "Unknown short.",
    ),
    "treasures[unknown_x44_x48]": (
        "Unknown [44-48]",
        "Unknown integer.",
    ),
    "treasures[unknown_x48_x4c]": (
        "Unknown [48-4c]",
        "Unknown integer.",
    ),

    "spawners[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Spawner in other game files.",
    ),
    "spawners[max_count]": (
        "Max Count",
        "Unsure; I suspect this is the total number of entities this spawner can produce.",
    ),
    "spawners[spawner_type]": (
        "Spawner Type",
        "Unsure what this enumeration is.",
    ),
    "spawners[limit_count]": (
        "Limit Count",
        "Unsure; I suspect this is the number of spawned entities that can be alive at once.",
    ),
    "spawners[min_spawner_count]": (
        "Min Spawner Count",
        "Unsure.",
    ),
    "spawners[max_spawner_count]": (
        "Max Spawner Count",
        "Unsure.",
    ),
    "spawners[min_interval]": (
        "Min Interval",
        "Minimum number of seconds between spawns.",
    ),
    "spawners[max_interval]": (
        "Max Interval",
        "Maximum number of seconds between spawns.",
    ),
    "spawners[initial_spawn_count]": (
        "Initial Spawn Count",
        "Unsure; I suspect this is the number of entities spawned immediately on map load.",
    ),
    "spawners[spawn_parts]": (
        "Spawn Characters",
        "Entities that will be spawned at given regions.",
    ),
    "spawners[spawn_regions]": (
        "Spawn Regions",
        "Regions where entities will be spawned.",
    ),

    "messages[attached_part]": (
        "Draw Parent",
        "Message will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
    ),
    "messages[attached_region]": (
        "Message Region",
        "Region (usually a Point) at which Message appears.",
    ),
    "messages[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Message in other game files.",
    ),
    "messages[text_id]": (
        "Message Text ID",
        "Soapstone Messages text ID shown when soapstone message is examined.",
    ),
    "messages[unk_x02_x04]": (
        "Unknown [02-04]",
        "Unknown. Often set to 2.",
    ),
    "messages[is_hidden]": (
        "Is Hidden",
        "If True, the message must be manually enabled with an event script or by using Seek Guidance.",
    ),

    "obj_acts[obj_act_entity_id]": (
        "ObjAct Entity ID",
        "ID that identifies this object activation event in event scripts.",
    ),
    "obj_acts[obj_act_part]": (
        "Object",
        "Object to which this object activation event is attached.",
    ),
    "obj_acts[obj_act_param_id]": (
        "ObjAct Param",
        "Param entry containing information about this object activation event. If it is -1, it will "
        "default to the model ID of the object it is attached to.",
    ),
    "obj_acts[obj_act_state]": (
        "ObjAct State",
        "State of object activation. Known values include Default (0), Door (1), and Loop (2).",
    ),
    "obj_acts[obj_act_flag]": (
        "ObjAct Flag",
        "Flag that stores the persistent state (e.g. open/closed) of this object activation.",
    ),

    # DS1
    "npc_invasions[base_region_name]": (
        "Invasion Region",
        "Region in which NPC Invasion event can be triggered (e.g. with Black Eye Orb).",
    ),
    "npc_invasions[host_entity_id]": (
        "Host Entity ID",
        "Entity ID of NPC character to be invaded.",
    ),
    "npc_invasions[invasion_flag_id]": (
        "Invasion Flag",
        "Flag that is enabled while the invasion is active, which should trigger changes to the world.",
    ),
    "npc_invasions[spawn_point_region_name]": (
        "Spawn Point Region",
        "Region where player will spawn during invasion event.",
    ),

    # Bloodborne
    "wind_vfx[attached_part]": (
        "Draw Parent",
        "VFX will be drawn if this parent (usually a Collision or Map Piece part) is drawn. Possibly unused.",
    ),
    "wind_vfx[attached_region]": (
        "Attached Region",
        "Base event region. Probably unused with WindVFX (see Wind Region Name instead).",
    ),
    "wind_vfx[wind_region]": (
        "VFX Region",
        "Region at or in which WindVFX appears.",
    ),
    "wind_vfx[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to this VFX in other game files. Possibly unused with WindVFX.",
    ),
    "wind_vfx[vfx_id]": (
        "VFX ID",
        "Visual effect ID, which refers to a loaded VFX file.",
    ),
    "wind_vfx[unk_x08_x0c]": (
        "Unknown [08-0c]",
        "Unknown floating-point number.",
    ),

    "patrol_routes[attached_part]": (
        "Draw Parent",
        "Probably unused for Patrol Route.",
    ),
    "patrol_routes[attached_region]": (
        "Attached Region",
        "Probably unused for Patrol Route.",
    ),
    "patrol_routes[entity_id]": (
        "Entity ID",
        "Probably unused for Patrol Route.",
    ),
    "patrol_routes[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown integer.",
    ),
    "patrol_routes[patrol_regions]": (
        "Patrol Regions",
        "List of regions that define this Patrol Route."
    ),

    "dark_locks[attached_part]": (
        "Draw Parent",
        "Probably unused for Dark Lock.",
    ),
    "dark_locks[attached_region]": (
        "Attached Region",
        "Probably unused for Dark Lock.",
    ),
    "dark_locks[entity_id]": (
        "Entity ID",
        "Probably unused for Dark Lock.",
    ),

    "platoons[attached_part]": (
        "Draw Parent",
        "Probably unused for Platoon.",
    ),
    "platoons[attached_region]": (
        "Attached Region",
        "Probably unused for Platoon.",
    ),
    "platoons[entity_id]": (
        "Entity ID",
        "Probably unused for Platoon.",
    ),
    "platoons[platoon_characters]": (
        "Platoon Character Names",
        "Characters in this Platoon.",
    ),
    "platoons[platoon_parents]": (
        "Platoon Parent Names",
        "Parent parts of this Platoon.",
    ),
    "platoons[platoon_id_script_active]": (
        "Platoon Active Script ID",
        "Unknown. Possibly an AI param ID.",
    ),
    "platoons[state]": (
        "Platoon State",
        "Unknown.",
    ),

    "multi_summons[attached_part]": (
        "Draw Parent",
        "Probably unused for Multi Summon.",
    ),
    "multi_summons[attached_region]": (
        "Attached Region",
        "Probably unused for Multi Summon.",
    ),
    "multi_summons[entity_id]": (
        "Entity ID",
        "Probably unused for Multi Summon.",
    ),
    "multi_summons[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown integer.",
    ),
    "multi_summons[unk_x04_x06]": (
        "Unknown [04-06]",
        "Unknown 16-bit integer.",
    ),
    "multi_summons[unk_x06_x08]": (
        "Unknown [06-08]",
        "Unknown 16-bit integer.",
    ),
    "multi_summons[unk_x08_x0a]": (
        "Unknown [08-0a]",
        "Unknown 16-bit integer.",
    ),
    "multi_summons[unk_x0a_x0c]": (
        "Unknown [0a-0c]",
        "Unknown 16-bit integer.",
    ),

    "spawn_points[attached_part]": (
        "Draw Parent",
        "Some Spawn Points use this; unclear what it does, but it is presumably the Collision of the Spawn Point.",
    ),
    "spawn_points[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Spawn Point in other game files.",
    ),
    "spawn_points[spawn_point_region]": (
        "Spawn Point Region",
        "Region where player will spawn when registered to this spawn point.",
    ),

    "map_offsets[translate]": (
        "Translate",
        "Vector of (x, y, z) coordinates of map offset.",
    ),
    "map_offsets[rotate_y]": (
        "Y Rotation",
        "Euler angle of rotation around the Y (vertical) axis.",
    ),

    "navigation[entity_id]": (
        "Entity ID",
        "Entity ID used to refer to the Navigation event in other game files.",
    ),
    "navigation[navigation_region]": (
        "Navmesh Region",
        "Region to which Navigation event is attached, which encloses faces of one or more Navmesh parts.",
    ),

    "environments[attached_part]": (
        "Draw Parent",
        "Environment (or 'map spot') will be drawn whenever its parent is drawn.",
    ),
    "environments[attached_region]": (
        "Environment Region",
        "Region (usually a Point) at which Environment appears (whatever that means).",
    ),
    "environments[entity_id]": (
        "Environment ID",
        "Unknown index. Note that this replaces the usual Entity ID field.",
    ),
    "environments[unk_x00_x04]": (
        "Unknown [00-04]",
        "Unknown Environment parameter (integer).",
    ),
    "environments[unk_x04_x08]": (
        "Unknown [04-08]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "environments[unk_x08_x0c]": (
        "Unknown [08-0c]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "environments[unk_x0c_x10]": (
        "Unknown [0c-10]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "environments[unk_x10_x14]": (
        "Unknown [10-14]",
        "Unknown Environment parameter (floating-point number).",
    ),
    "environments[unk_x14_x18]": (
        "Unknown [14-18]",
        "Unknown Environment parameter (floating-point number).",
    ),
}
