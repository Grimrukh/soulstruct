from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


PERFORMANCE_CHECK_PARAM = {
    "param_type": "PERFORMANCE_CHECK_PARAM",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "workTag",
            "Report destination_Job type tag",
            True,
            int,
            'Report destination_Job type tag',
        ),
        ParamFieldInfo(
            "categoryTag",
            "Report destination_category tag",
            True,
            int,
            'Report destination_category tag',
        ),
        ParamFieldInfo(
            "compareType",
            "Comparison symbol",
            True,
            int,
            'Comparison symbol',
        ),
        ParamFieldInfo(
            "dummy1[1]",
            "Reservation 1",
            False,
            pad_field(1),
            'Reservation 1',
        ),
        ParamFieldInfo(
            "compareValue",
            "Comparison value",
            True,
            float,
            'Comparison value',
        ),
        ParamFieldInfo(
            "dummy2[8]",
            "Reservation 2",
            False,
            pad_field(8),
            'Reservation 2',
        ),
        ParamFieldInfo(
            "userTag[16]",
            "Report destination_user tag",
            True,
            str,
            'Report to_Performance person tag',
        ),
    ],
}
