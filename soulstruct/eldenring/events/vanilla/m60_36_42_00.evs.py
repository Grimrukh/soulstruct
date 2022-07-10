"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005637, args=(31058521, 1036420620, 1036421620), arg_types="III")
    RunCommonEvent(
        0,
        90005636,
        args=(31058521, 1036420620, 1036421620, 4470, 1036422620, 1036422621, 1036422620, 1036423620, -1),
        arg_types="IIIiIIIIi",
    )
