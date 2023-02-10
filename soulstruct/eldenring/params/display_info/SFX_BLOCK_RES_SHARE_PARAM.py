from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SFX_BLOCK_RES_SHARE_PARAM = {
    "param_type": "SFX_BLOCK_RES_SHARE_PARAM",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "shareBlockRsMapUidVal",
            "Shared Resource Block - Map UID",
            True,
            int,
            'The map number that references the resource. Set the numerical value of the map number. (m12_34_56_78 �� 12345678)',
        ),
    ],
}
