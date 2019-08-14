from soulstruct.esd._structs import get_esd_class

__all__ = ['ESD']


ESD = get_esd_class(game_version=1, long=True)


if __name__ == '__main__':
    bonfire = ESD('talk_dsr/m10_00_00_00.talkesdbnd.dcx.unpacked/t100000.esd', esd_type='talk')
    # bonfire.write_html('t100000.esd.html')
    bonfire.write_py('t100000.esd.py')
