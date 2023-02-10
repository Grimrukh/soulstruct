from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


REVERB_AUX_SEND_BUS_PARAM_ST = {
    "param_type": "REVERB_AUX_SEND_BUS_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "ReverbAuxSendBusName[32]",
            "Reverb Aux Send Bus Name",
            True,
            str,
            'ReverbAuxSendBus name',
        ),
    ],
}
