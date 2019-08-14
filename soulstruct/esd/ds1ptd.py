from soulstruct.esd._structs import get_esd_class

__all__ = ['ESD']


ESD = get_esd_class(game_version=1, long=False)
