from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


RUNTIME_BONE_CONTROL_PARAM_ST = {
    "param_type": "RUNTIME_BONE_CONTROL_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "chrId",
            "Character ID",
            True,
            int,
            'Character ID',
        ),
        ParamFieldInfo(
            "ctrlType",
            "Bone Control Type",
            True,
            int,
            'Control type',
        ),
        ParamFieldInfo(
            "pad[11]",
            "pad",
            False,
            pad_field(11),
            '',
        ),
        ParamFieldInfo(
            "applyBone[32]",
            "Applicable Joint",
            True,
            str,
            'Applicable joint',
        ),
        ParamFieldInfo(
            "targetBone1[32]",
            "Target Joint [1]",
            True,
            str,
            'Target joint 1',
        ),
        ParamFieldInfo(
            "targetBone2[32]",
            "Target Joint [2]",
            True,
            str,
            'Target joint 2',
        ),
    ],
}
