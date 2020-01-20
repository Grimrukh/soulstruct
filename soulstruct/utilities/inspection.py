import logging
import struct

_LOGGER = logging.getLogger(__name__)


def print_binary_as_integers(file_name):
    """Tool for inspecting data you assume or suspect is integers."""
    with open(file_name, 'rb') as file:
        offset = 0
        data = file.read(4)
        while data != -1:
            try:
                integer = struct.unpack('<i', data)
            except struct.error:
                _LOGGER.warning("Finished with less than four bytes remaining.")
                return
            print(f"{offset} | {hex(offset)} | {integer}")
            data = file.read(4)
            offset += 4
