import math
from struct import unpack, pack


""" HELPER FUNCTIONS """


def floatify(i):
    """ Convert an integer to a float. Useful for ambiguous data in the unpacked resources. """
    h = hex(i)[2:]
    return unpack('!f', bytes.fromhex(h))[0]


def int_to_two_shorts(integer, unsigned=True):
    """ Converted an integer (unsigned by default) to two shorts. """
    if unsigned:
        return unpack('<HH', pack('<I', integer))
    else:
        return unpack('<hh', pack('<i', integer))


def two_shorts_to_int(short1, short2, unsigned=True):
    """ Converted two shorts (unsigned by default) to one integer. """
    if unsigned:
        return unpack('<I', pack('<HH', short1, short2))
    else:
        return unpack('<i', pack('<hh', short1, short2))


def shift_msb_coordinates(ry, distance, xyz=(0.0, 0.0, 0.0)):
    """ Shift an MSB entity with given x, z, ry coordinates forward or back. """
    ry_rad = math.radians(ry)
    delta_x = -distance * math.sin(ry_rad)
    delta_z = -distance * math.cos(ry_rad)
    return xyz[0] + delta_x, xyz[1], xyz[2] + delta_z


def shift(rel_x, rel_z, origin=(0, 0), rotation=0):
    rot_rad = math.radians(rotation)
    r, th = math.hypot(rel_x, rel_z), math.atan2(rel_z, rel_x)
    th += rot_rad
    dx, dz = r * -math.sin(th), r * -math.cos(th)
    return origin[0] + dx, origin[1] + dz


""" PRIVATE HELPER FUNCTIONS """


