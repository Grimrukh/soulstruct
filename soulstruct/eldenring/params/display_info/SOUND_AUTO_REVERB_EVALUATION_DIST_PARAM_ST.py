from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST = {
    "param_type": "SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "NoHitDist",
            "No Hit Distance",
            True,
            float,
            'Collision points above this distance [m] are judged as No Hit (less than 0: invalid)',
        ),
        ParamFieldInfo(
            "isCollectNoHitPoint",
            "Include Collision Point of No Hit",
            True,
            int,
            'Do you include NoHit collision points?',
        ),
        ParamFieldInfo(
            "isCollectOutdoorPoint",
            "Include Outdoor Collision Point",
            True,
            int,
            'Do you include outdoor collision points?',
        ),
        ParamFieldInfo(
            "isCollectFloorPoint",
            "Include Floor Collision Point",
            True,
            int,
            'Do you include floor collision points?',
        ),
        ParamFieldInfo(
            "distValCalcType",
            "Evaluation Distance Calculation Type",
            True,
            int,
            'Evaluation distance calculation type (0: normal, average from 1: Max)',
        ),
        ParamFieldInfo(
            "enableLifeTime",
            "Invalidate after Duration",
            True,
            float,
            'Collision points longer than this life [second] are treated as invalid. Set to be less than or equal to the life of the common setting',
        ),
        ParamFieldInfo(
            "maxDistRecordNum",
            "Max Collision Point Count",
            True,
            int,
            'Max Number of collision point records',
        ),
        ParamFieldInfo(
            "ignoreDistNumForMax",
            "Max Distance until Ignore",
            True,
            int,
            'Max distance decimation number (0: not decimation) (must be set to the value of "Max collision point record number-1". Incorrect value will be corrected)',
        ),
    ],
}
