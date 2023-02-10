from __future__ import annotations

__all__ = ["NPC_THINK_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


NPC_THINK_PARAM_ST = {
    "param_type": "NPC_THINK_PARAM_ST",
    "file_name": "NpcThinkParam",
    "nickname": "AI",
    "fields": [
        ParamFieldInfo("logicId", "LogicID", True, LogicAIScript, "ID of logic (non-battle) Lua script."),
        ParamFieldInfo(
            "battleGoalID",
            "BattleID",
            True,
            BattleAIScript,
            "Battle goal ID used to look up battle Lua script.",
        ),
        ParamFieldInfo(
            "nearDist",
            "NearDistance",
            True,
            float,
            "Distance considered to be close range by this NPC (for scripts).",
        ),
        ParamFieldInfo(
            "midDist",
            "MidDistance",
            True,
            float,
            "Distance considered to be medium range by this NPC (for scripts).",
        ),
        ParamFieldInfo(
            "farDist", "FarDistance", True, float, "Distance considered to be long range by this NPC (for scripts)."
        ),
        ParamFieldInfo(
            "outDist", "OutOfRangeDistance", True, float, "Distance beyond which the NPC will not attempt to fight."
        ),
        ParamFieldInfo(
            "BackHomeLife_OnHitEneWal",
            "RetreatTimeAfterHittingEnemyWall",
            False,
            float,
            "Retreat goal time when touching an 'enemy wall' that blocks the NPC's path. (Not clear what an "
            "'enemy wall' means. Almost always set to 5 (rarely 6).",
        ),
        ParamFieldInfo(
            "goalID_ToCaution",
            "CautionGoalID",
            True,
            LogicAIScript,
            "Lua script to use when NPC's AI enters the 'Caution' state (I think). Requires a CautionGoalAction "
            "value of 4. Used only by Hawkeye Gough (411000); zero otherwise.",
        ),
        ParamFieldInfo(
            "idAttackCannotMove",
            "StuckAnimationID",
            True,
            int,  # TODO: Animation
            "Animation to use if the NPC gets stuck on a destructible object. Usually 3000 (basic attack).",
        ),
        ParamFieldInfo(
            "goalID_ToFind",
            "SearchGoalID",
            True,
            LogicAIScript,
            "Lua script to use when NPC's AI enters the 'Search' state (I think). Requires a SearchGoalAction "
            "value of 4. Not used by any vanilla NPC (all zero).",
        ),
        ParamFieldInfo(
            "callHelp_ActionAnimId",
            "HelpCallResponseAnimation",
            True,
            int,  # TODO: Animation
            "Animation to play when responding to a call for help. Usually set to -1 for NPCs who can reply to "
            "calls for help, which I assume means no animation is played. Set to 0 for NPCs who ignore calls for "
            "help.",
        ),
        ParamFieldInfo(
            "callHelp_CallActionId",
            "HelpCallSendAnimation",
            True,
            int,  # TODO: Animation
            "Animation to play when calling for help. Only used by Female Ghost (7300) and Male Ghost and summons "
            "(-1). I assume -1 means no animation is played. Set to 0 for all other NPCs.",
        ),
        ParamFieldInfo("eye_dist", "SightDistance", True, int, "Distance of NPC eyesight (in meters)."),
        ParamFieldInfo("ear_dist", "HearingDistance", True, int, "Distance of NPC hearing (in meters)."),
        ParamFieldInfo(
            "ear_soundcut_dist",
            "HearingCutDistance",
            False,
            int,
            "Internal description: 'Distance to reduce the size of the sound source. Sounds less than this "
            "distance will not be heard.' Set to 1 for Bloatheads and Bloathead Sorcerers and 0 for everyone "
            "else.",
        ),
        ParamFieldInfo("nose_dist", "SmellDistance", True, int, "Distance of NPC smell (auto-detect)."),
        ParamFieldInfo(
            "maxBackhomeDist",
            "MaxRetreatDistance",
            True,
            int,
            "Absolute furthest the NPC can travel from their nest before retreating, in or out of battle. ("
            "Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.) Usually set to about 50% more than "
            "BattleRetreatDistance.",
        ),
        ParamFieldInfo(
            "backhomeDist",
            "BattleRetreatDistance",
            True,
            int,
            "Furthest distance the NPC can travel from their nest before retreating in battle. (Argument of "
            "internal GOAL function 'COMMON_SetBattleActLogic()'.)",
        ),
        ParamFieldInfo(
            "backhomeBattleDist",
            "RetreatBattleStartDistance",
            True,
            int,
            "Target distance at which battle mode is triggered while the enemy is retreating. (Argument of "
            "internal GOAL function 'COMMON_SetBattleActLogic()'.)",
        ),
        ParamFieldInfo(
            "nonBattleActLife",
            "NonBattleActLife",
            False,
            int,
            "Lifespan of Acts outside of battle. Set to 10 for Bloatheads and Bloathead Sorcerers, "
            "0 for Priscilla's Tail and the Bed of Chaos bug, and 5 for everyone else. (Argument of internal GOAL "
            "function 'COMMON_SetBattleActLogic()'.)",
        ),
        ParamFieldInfo(
            "BackHome_LookTargetTime",
            "SearchTimeBeforeRetreat",
            True,
            int,
            "Time that NPC will search for a lost target before retreating (I think). Set to 20 for everyone "
            "except the Bounding Demons of Izalith, who have a value of 0.",
        ),
        ParamFieldInfo(
            "BackHome_LookTargetDist",
            "SearchDistanceBeforeRetreat",
            True,
            int,
            "Distance that NPC will search for a lost target before retreating (I think). Set to 20 for everyone "
            "except the Bounding Demons of Izalith, who have a value of 0.",
        ),
        ParamFieldInfo(
            "SightTargetForgetTime",
            "SightForgetTime",
            True,
            int,
            "Time to forget about sighted targets. Usually set to 600.",
        ),
        ParamFieldInfo(
            "SoundTargetForgetTime",
            "HearingForgetTime",
            True,
            int,
            "Time to forget about heard targets. Usually set to 300.",
        ),
        ParamFieldInfo(
            "BattleStartDist",
            "BattleStartDistance",
            True,
            int,
            "Target distance at which battle mode is triggered.",
        ),
        ParamFieldInfo(
            "callHelp_MyPeerId",
            "HelpGroupID",
            True,
            int,
            "Determines which calls for help this NPC will respond to (must match caller's HelpCallGroupID). Only "
            "0 (no ID) and 1 are used.",
        ),
        ParamFieldInfo(
            "callHelp_CallPeerId",
            "HelpCallGroupID",
            True,
            int,
            "HelpGroupID value of NPCs who should respond to calls for help by this NPC. Only 0 (no ID) and 1 are "
            "used.",
        ),
        ParamFieldInfo(
            "targetSys_DmgEffectRate",
            "TargetSysDamageRate",
            False,
            int,
            "Internal description: 'Get damage rate (%) for target system evaluation information.' Set to 0 for "
            "summons, phantoms, and the Parasitic Wall Hugger, and 100 for everyone else.",
        ),
        ParamFieldInfo(
            "TeamAttackEffectivity",
            "TeamAttackEffectivity",
            True,
            int,
            "Value from 0 to 100 that determines the number of simultaneous attacks made by this NPC's team. "
            "Higher values mean that less members of this team can participate in attacks at the same time. (I "
            "presume that the total score of attacking team members cannot exceed 100.) Usually set to 25 or 100.",
        ),
        # TODO: Apparently X is height and Y is width here. The internal descriptions or names may be incorrect.
        ParamFieldInfo("eye_angX", "SightRangeHeight", True, int, "Angular width of sight field in degrees."),
        ParamFieldInfo("eye_angY", "SightRangeWidth", True, int, "Angular height of sight field in degrees."),
        ParamFieldInfo("ear_angX", "HearingRangeHeight", True, int, "Angular width of hearing field in degrees."),
        ParamFieldInfo("ear_angY", "HearingRangeWidth", True, int, "Angular height of hearing field in degrees."),
        ParamFieldInfo(
            "callHelp_CallValidMinDistTarget",
            "HelpCallTargetMinDistance",
            False,
            int,
            "Minimum distance from AI target for help call to be made. Always zero.",
        ),
        ParamFieldInfo(
            "callHelp_CallValidRange",
            "HelpCallFriendMaxDistance",
            True,
            int,
            "Maximum distance of friend to receive help call from this NPC. Set to 50 for both Male and Female "
            "Ghosts, and 0 for everyone else.",
        ),
        ParamFieldInfo(
            "callHelp_ForgetTimeByArrival",
            "HelpCallForgetTime",
            True,
            int,
            "Time until call for help is forgotten by responder.",
        ),
        ParamFieldInfo(
            "callHelp_MinWaitTime",
            "HelpCallMinWaitTime",
            True,
            int,
            "Internal description: 'Minimum time for response goal at first waiting goal'. Units are in tenths of "
            "a second. Only used for Male Ghosts (20).",
        ),
        ParamFieldInfo(
            "callHelp_MaxWaitTime",
            "HelpCallMaxWaitTime",
            True,
            int,
            "Internal description: 'Maximum time for response goal at first waiting goal'. Units are in tenths of "
            "a second. Only used for Female Ghosts (40).",
        ),
        ParamFieldInfo(
            "goalAction_ToCaution",
            "CautionGoalAction",
            True,
            NPC_THINK_GOAL_ACTION,
            "Type of action taken when AI enters the 'Caution' state.",
        ),
        ParamFieldInfo(
            "goalAction_ToFind",
            "SearchGoalAction",
            True,
            NPC_THINK_GOAL_ACTION,
            "Type of action taken when AI enters the 'Search' state.",
        ),
        ParamFieldInfo(
            "callHelp_ReplyBehaviorType",
            "HelpCallReplyType",
            True,
            NPC_THINK_REPLY_BEHAVIOR_TYPE,
            "Set to 0 for NPCs who do not reply to calls for help and 1 for NPCs who do.",
        ),
        # NOTE: Not a boolean field, but used like one.
        ParamFieldInfo(
            "disablePathMove",
            "IgnoreNavmesh",
            True,
            bool,
            "If 1, this NPC will ignore navmesh when moving. True for Ghosts and enemies that don't move at all.",
        ),
        ParamFieldInfo(
            "skipArrivalVisibleCheck",
            "SkipArrivalVisibleCheck",
            False,
            bool,
            "Internal description: 'If enabled, arrival determination is performed even if the line of sight"
            "is not passed.' True only for Hawkeye Gough.",
        ),
        ParamFieldInfo(
            "thinkAttr_doAdmirer",
            "AdmirerAttribute",
            True,
            bool,
            "Internal description: 'Thought attribute: when enabled, it plays the role of a wrap.' I don't"
            "know exactly what that means, but this is likely important for something. Enabled for Soulmass"
            "and Pursuers, non-giant Rats, Infested Ghouls, Mushrooms, most Hollows (not archers), Male"
            "Ghosts, normal Skeletons and Skeleton Beasts, and Pisaca.",
        ),
        ParamFieldInfo(
            "enableNaviFlg_Edge:1",
            "CanFallOffEdges",
            True,
            bool,
            "If True, this NPC will pursue targets off navmesh edges (survivable falls).",
        ),
        ParamFieldInfo(
            "enableNaviFlg_LargeSpace:1",
            "CanNavigateWideSpaces",
            True,
            bool,
            "If True, this NPC can enter navmesh regions flagged as 'large spaces'.",
        ),
        ParamFieldInfo(
            "enableNaviFlg_Ladder:1", "CanNavigateLadders", True, bool, "If True, this NPC will use ladders."
        ),
        ParamFieldInfo(
            "enableNaviFlg_Hole:1", "CanNavigateHoles", True, bool, "If True, this NPC can fall into navmesh holes."
        ),
        ParamFieldInfo(
            "enableNaviFlg_Door:1",
            "CanNavigateDoors",
            True,
            bool,
            "If True, this NPC can go through doors (but not necessarily open closed doors).",
        ),
        ParamFieldInfo(
            "enableNaviFlg_InSideWall:1",
            "CanNavigateInsideWalls",
            True,
            bool,
            "If True, this NPC can go through walls (i.e. ignores navmesh walls).",
        ),
        ParamFieldInfo(
            "enableNaviFlg_reserve0:2",
            "UnusedNavmeshCheckX2",
            False,
            bool,
            "Two unused bytes reserved for other navmesh checks. No effect.",
        ),
        ParamFieldInfo(
            "enableNaviFlg_reserve1[3]",
            "UnusedNavmeshCheckX3",
            False,
            bool,
            "Three unused bytes reserved for other navmesh checks. No effect.",
        ),
        ParamFieldInfo("pad0[12]", "Pad0", False, pad_field(12), "Null padding."),
    ],
}
