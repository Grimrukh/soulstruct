import keyboard
import psutil

from soulstruct.utilities.memory import DSRMemoryHook

__all__ = ["RUN"]

def print_position(hook: DSRMemoryHook):
    x = hook.get("player_x")
    y = hook.get("player_y")
    z = hook.get("player_z")
    angle = hook.get("player_angle")
    print(f"xyz = [{x:.3f}, {y:.3f}, {z:3f}]\n"
          f"angle = [0, {angle:.3f}, 0]")

def RUN():
    hook = DSRMemoryHook()
    keyboard.add_hotkey("ctrl+shift+p", print_position, args=(hook,))
    keyboard.wait("ctrl+shift+end")
