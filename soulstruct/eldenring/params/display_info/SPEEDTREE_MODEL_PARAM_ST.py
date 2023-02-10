from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SPEEDTREE_MODEL_PARAM_ST = {
    "param_type": "SPEEDTREE_MODEL_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "MinFadeLeaf",
            "Leaf - Min Fade",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MinFadeFrond",
            "Frond - Min Fade",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MinFadeBranch",
            "Branch - Min Fade",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MinTranslucencyLeaf",
            "Leaf - Min Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MaxTranslucencyLeaf",
            "Leaf - Max Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MinTranslucencyFrond",
            "Frond - Min Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MaxTranslucencyFrond",
            "Frond - Max Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MinTranslucencyBranch",
            "Branch - Min Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "MaxTranslucencyBranch",
            "Branch - Max Translucency",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "BillboardBackSpecularWeakenParam",
            "Billboard Specular Suppression Value",
            True,
            float,
            '',
        ),
    ],
}
