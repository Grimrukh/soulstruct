"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Wait(0.10000000149011612)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)
