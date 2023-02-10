from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


RIDE_PARAM_ST = {
    "param_type": "RIDE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "atkChrId",
            "Rider - Character ID",
            True,
            int,
            'It is a parameter that identifies the character of the "riding side" when riding.',
        ),
        ParamFieldInfo(
            "defChrId",
            "Mount - Character ID",
            True,
            int,
            'It is a parameter that identifies the character of the "riding side" when riding.',
        ),
        ParamFieldInfo(
            "rideCamParamId",
            "Ride - Camera Param ID",
            True,
            int,
            'It is a parameter to change the camera parameter at the time of riding to a dedicated camera. It is a parameter for PC only, and it does not work even if it is set to the enemy.',
        ),
        ParamFieldInfo(
            "atkChrAnimId",
            "Rider - Character Animation ID",
            True,
            int,
            'It is a parameter to rewrite the value of variable "RideOnAnimId" set in "RideOn (playback during riding) state" of the tool "HavokAnimationTool (HAT)" that controls character animation playback.',
        ),
        ParamFieldInfo(
            "defChrAnimId",
            "Mount - Character Animation ID",
            True,
            int,
            'It is a parameter to rewrite the value of variable "RiddenOnAnimId" set in "RiddenOn (playback when riding) state" of the tool "HavokAnimationTool (HAT)" that controls character animation playback.',
        ),
        ParamFieldInfo(
            "defAdjustDmyId",
            "Mount - Adjust Dummy Poly ID",
            True,
            int,
            "This is a Damipoli setting that is required only for the rider (the rider's character does not need to be set).",
        ),
        ParamFieldInfo(
            "defCheckDmyId",
            "Mount - Check Dummy Poly ID",
            True,
            int,
            'There is no need to set Damipoli for the character on the riding side.',
        ),
        ParamFieldInfo(
            "diffAngMyToDef",
            "Rider/Mount - Ride Angle Tolerance",
            True,
            float,
            'Judgment is made by the angle difference between the [direction] on the riding side and the "front judgment Damipoly ID" on the riding side. The higher the value, the more you can ride even if you are facing away.',
        ),
        ParamFieldInfo(
            "dist",
            "Mount Distance",
            True,
            float,
            'It is a parameter that determines the "mountable distance to the target"',
        ),
        ParamFieldInfo(
            "upperYRange",
            "Mount Distance - Max Height",
            True,
            float,
            'Is it possible to ride even if the target to be ridden is above the target to be ridden? Is set in meters',
        ),
        ParamFieldInfo(
            "lowerYRange",
            "Mount Distance - Min Height",
            True,
            float,
            'Is it possible to ride even if the target to be ridden is below the target to be ridden? Is set in meters',
        ),
        ParamFieldInfo(
            "diffAngMin",
            "Ride Angle Tolerance - Min",
            True,
            float,
            'In what range (angle) of the rider can ride? Set the minimum value of',
        ),
        ParamFieldInfo(
            "diffAngMax",
            "Ride Angle Tolerance - Max",
            True,
            float,
            'In what range (angle) of the rider can ride? Set the maximum value of',
        ),
        ParamFieldInfo(
            "pad[12]",
            "reserve",
            False,
            pad_field(12),
            'Reserved area',
        ),
    ],
}
