__all__ = [
    "MSBSupertype",
    "MSBModelSubtype",
    "MSBEventSubtype",
    "MSBRegionSubtype",
    "MSBPartSubtype",
    "MSBRouteSubtype",
    "CollisionHitFilter",
]

from enum import IntEnum, StrEnum

from soulstruct.base.maps.msb.enums import *


class MSBSupertype(StrEnum):
    """Same for most games."""
    MODELS = "MODEL_PARAM_ST"
    EVENTS = "EVENT_PARAM_ST"
    REGIONS = "POINT_PARAM_ST"
    ROUTES = "ROUTE_PARAM_ST"
    LAYERS = "LAYER_PARAM_ST"  # empty supertype
    PARTS = "PARTS_PARAM_ST"

    @classmethod
    def resolve(cls, supertype: str) -> MSBSupertype:
        """Resolve various forms of the supertype name into this enum."""
        if supertype.upper().startswith("MODEL"):
            return cls.MODELS
        if supertype.upper().startswith("EVENT"):
            return cls.EVENTS
        if supertype.upper().startswith("REGION") or supertype.upper().startswith("POINT"):
            return cls.REGIONS
        if supertype.upper().startswith("ROUTE"):
            return cls.ROUTES
        if supertype.upper().startswith("LAYER"):
            return cls.LAYERS
        if supertype.upper().startswith("PARTS"):
            return cls.PARTS
        raise ValueError(f"Cannot resolve unknown MSB supertype name: {supertype}")

    @classmethod
    def entity_id_supertypes(cls):
        """Returns all supertypes whose entries use entity IDs."""
        return cls.EVENTS, cls.REGIONS, cls.PARTS


class MSBModelSubtype(BaseMSBModelSubtype):
    MapPieceModel = 0
    CharacterModel = 2
    PlayerModel = 4
    CollisionModel = 5
    AssetModel = 10

    @classmethod
    def get_sib_path_stem(cls):
        return "N:\\GR\\data\\Model\\"

    @classmethod
    def get_plural_supertype_name(cls):
        return "Models"


class MSBEventSubtype(BaseMSBEventSubtype):
    Treasure = 4
    Spawner = 5
    ObjAct = 7
    Navigation = 10
    Environment = 11
    NPCInvasion = 12
    Platoon = 15
    PatrolRouteEvent = 20  # needs `Event` suffix to distinguish it from Region subtype
    Mount = 21
    SignPool = 23
    RetryPoint = 24
    OtherEvent = -1

    @classmethod
    def get_plural_supertype_name(cls):
        return "Events"


class MSBRegionSubtype(BaseMSBRegionSubtype):
    """NOTE: Not just shapes anymore. Any of these subtypes can have any shape."""
    InvasionPoint = 1
    EnvironmentMapPoint = 2
    Sound = 4
    VFX = 5
    WindVFX = 6
    SpawnPoint = 8
    Message = 9
    EnvironmentMapEffectBox = 17
    WindArea = 18
    Connection = 21
    PatrolRoute22 = 22
    BuddySummonPoint = 26
    MufflingBox = 28
    MufflingPortal = 29
    OtherSound = 30
    MufflingPlane = 31
    PatrolRoute = 32
    MapPoint = 33
    WeatherOverride = 35
    AutoDrawGroupPoint = 36
    GroupDefeatReward = 37
    MapPointDiscoveryOverride = 38
    MapPointParticipationOverride = 39
    Hitset = 40
    FastTravelRestriction = 41
    WeatherCreateAssetPoint = 42
    PlayArea = 43
    EnvironmentMapOutput = 44
    MountJump = 46
    Dummy = 48
    FallPreventionRemoval = 49
    NavmeshCutting = 50
    MapNameOverride = 51
    MountJumpFall = 52
    HorseRideOverride = 53
    OtherRegion = -1

    @classmethod
    def get_plural_supertype_name(cls):
        return "Regions"


class MSBPartSubtype(BaseMSBPartSubtype):
    MapPiece = 0
    Character = 2
    PlayerStart = 4
    Collision = 5
    Navmesh = 8
    UnusedAsset = 9
    DummyCharacter = 10
    ConnectCollision = 11
    Asset = 13

    @classmethod
    def get_plural_supertype_name(cls):
        return "Parts"


class MSBRouteSubtype(BaseMSBSubtype):
    MufflingPortalLink = 3
    MufflingBoxLink = 4
    OtherRoute = -1


class CollisionHitFilter(IntEnum):
    """Defines behavior of `MSBCollision` instances in maps. Courtesy of horkrux.

    TODO: Not sure if any of the unknown ones here match earlier games, but we know they're not all identical.
    """
    Normal = 8
    CameraOnly = 9
    NPCOnly = 11
    FallDeathCam = 13
    Kill = 15
    Unk16 = 16
    Unk17 = 17
    Unk19 = 19
    Unk20 = 20
    Unk22 = 22
    Unk23 = 23
    Unk24 = 24
    Unk29 = 29
