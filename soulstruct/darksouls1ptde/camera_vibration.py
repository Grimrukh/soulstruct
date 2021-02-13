"""My descriptions of the various camera vibration IDs."""
from enum import IntEnum


class CameraVibration(IntEnum):

    # playcam

    # eventcam
    LongWobble = 100  # slower and noticeably side to side, like walking on a shaking platform?
    GiantLongWobble = 101  # explosion
    Thud1 = 102
    Thud2 = 103  # e.g. Ceaseless Discharge footstep
    Thud3 = 104
    Thud4 = 105  # thuds 4-6 might be a bit longer than thuds 1-3?
    Thud5 = 106
    Thud6 = 107
    Wobble1 = 200
    Wobble2 = 201

    # mapcam
    MapCam = 210  # just a low rumble
