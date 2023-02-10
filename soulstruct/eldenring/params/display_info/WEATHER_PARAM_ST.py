from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WEATHER_PARAM_ST = {
    "param_type": "WEATHER_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "SfxId",
            "Weather SFX ID",
            True,
            int,
            'SfxId for weather -1: No weather Sfx Set for indoor and outdoor use. Items that can be erased with Above Shadow, such as raindrops of interactive particles, are OK here.',
        ),
        ParamFieldInfo(
            "WindSfxId",
            "Wind SFX ID",
            True,
            int,
            'Wind SfxId -1: No wind Sfx Created only outdoors',
        ),
        ParamFieldInfo(
            "GroundHitSfxId",
            "Ground Hit SFX ID",
            True,
            int,
            'SfxId for ground hit effect -1: None for ground hit effect',
        ),
        ParamFieldInfo(
            "SoundId",
            "Sound ID",
            True,
            int,
            'SoundId for weather -1: No Sound',
        ),
        ParamFieldInfo(
            "WetTime",
            "Wet Time",
            True,
            float,
            'Time to get completely wet (time until the weight of m00_00_0000_WeatherBase reaches 1.0) -1: No wetness (m00_00_0000_WeatherBase remains 0.0)',
        ),
        ParamFieldInfo(
            "GparamId",
            "GPARAM ID",
            True,
            int,
            'Specify the XXX part of Gparam (m00_00_? XXX_WeatherOutdoor.gparamxml) for outdoor weather. Gparam to be used can be shared between weather.',
        ),
        ParamFieldInfo(
            "NextLotIngameSecondsMin",
            "Next Weather Lot - Min Duration",
            True,
            int,
            'Specify the minimum time to the next weather lottery in in-game seconds. When transitioning to this weather, the time to the next weather will be a random time between the minimum and maximum.',
        ),
        ParamFieldInfo(
            "NextLotIngameSecondsMax",
            "Next Weather Lot - Max Duration",
            True,
            int,
            'Specify the maximum time until the next weather lottery in in-game seconds. When transitioning to this weather, the time to the next weather will be a random time between the minimum and maximum.',
        ),
        ParamFieldInfo(
            "WetSpEffectId00",
            "Wet SpEffect [0]",
            True,
            int,
            'Special effect ID on the character (-1: None)',
        ),
        ParamFieldInfo(
            "WetSpEffectId01",
            "Wet SpEffect [1]",
            True,
            int,
            'Special effect ID on the character (-1: None)',
        ),
        ParamFieldInfo(
            "WetSpEffectId02",
            "Wet SpEffect [2]",
            True,
            int,
            'Special effect ID on the character (-1: None)',
        ),
        ParamFieldInfo(
            "WetSpEffectId03",
            "Wet SpEffect [3]",
            True,
            int,
            'Special effect ID on the character (-1: None)',
        ),
        ParamFieldInfo(
            "WetSpEffectId04",
            "Wet SpEffect [4]",
            True,
            int,
            'Special effect ID on the character (-1: None)',
        ),
        ParamFieldInfo(
            "SfxIdInoor",
            "Weather SFX - Indoors Only - SFX ID",
            True,
            int,
            'Weather SfxId -1: No weather Sfx indoors only',
        ),
        ParamFieldInfo(
            "SfxIdOutdoor",
            "Weather SFX - Outdoors Only - SFX ID",
            True,
            int,
            'Weather SfxId -1: No weather Sfx, outdoor only',
        ),
        ParamFieldInfo(
            "aiSightRate",
            "AI Sight Rate",
            True,
            float,
            'AI field of view magnification',
        ),
        ParamFieldInfo(
            "DistViewWeatherGparamOverrideWeight",
            "Overwrite Weight Valuue in Distant View Camera",
            True,
            float,
            'Overwrite weight value in distant view camera (SEQ16724)',
        ),
    ],
}
