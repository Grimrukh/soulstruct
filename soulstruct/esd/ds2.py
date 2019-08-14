from soulstruct.esd._structs import get_esd_class

__all__ = ['ESD']

# TODO: Confirm DS2 uses long format.

ESD = get_esd_class(game_version=2, long=True)
