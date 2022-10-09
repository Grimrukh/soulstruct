from __future__ import annotations

__all__ = ["MSB"]

import typing as tp
from enum import IntEnum

from soulstruct.base.maps.msb import MSB as _BaseMSB
from soulstruct.games import DarkSoulsPTDEType
from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.utilities.maths import Vector3

from .models import MSBModelList
from .events import MSBEventList
from .regions import MSBRegionList
from .parts import MSBPartList


class MSB(DarkSoulsPTDEType, _BaseMSB):
    """Handles MSB ('MapStudio') data for Dark Souls. Both versions of the game have identical formats."""

    MODEL_LIST_CLASS = MSBModelList
    EVENT_LIST_CLASS = MSBEventList
    REGION_LIST_CLASS = MSBRegionList
    PART_LIST_CLASS = MSBPartList

    models: MSBModelList
    events: MSBEventList
    regions: MSBRegionList
    parts: MSBPartList

    # These are ordered by convenience (same as GUI).
    ENTITY_GAME_TYPES = {
        "parts": (
            MapPiece,
            Object,
            Character,
            PlayerStart,
            Collision,
        ),
        "events": (
            SoundEvent,
            VFXEvent,
            SpawnerEvent,
            MessageEvent,
            SpawnPointEvent,
            NavigationEvent,
        ),
        "regions": (
            RegionPoint,
            RegionSphere,
            RegionCylinder,
            RegionBox,
        ),
    }

    def new_sound_event_with_box(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        width: float,
        depth: float,
        height: float,
        **sound_event_kwargs,
    ):
        if "base_region_name" in sound_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        sound = self.events.new_sound(**sound_event_kwargs)
        box = self.regions.new_box(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            width=width,
            depth=depth,
            height=height,
        )
        sound.base_region_name = box.name
        return sound

    def new_sound_event_with_sphere(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        radius: float,
        **sound_event_kwargs,
    ):
        if "base_region_name" in sound_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        sound = self.events.new_sound(**sound_event_kwargs)
        sphere = self.regions.new_sphere(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            radius=radius,
        )
        sound.base_region_name = sphere.name
        return sound

    def new_vfx_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        point_entity_enum: tp.Optional[RegionPoint] = None,
        **vfx_event_kwargs,
    ):
        if "base_region_name" in vfx_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        vfx = self.events.new_vfx(**vfx_event_kwargs)
        point_name = f"_VFXEvent_{vfx.name.lstrip('_')}"
        if point_entity_enum is not None:
            if point_entity_enum.name != point_name:
                raise ValueError(f"Name of `point_entity_enum` must be '{point_name}', not '{point_entity_enum.name}'.")
            point_entity_id = point_entity_enum.value
        else:
            point_entity_id = -1
        point = self.regions.new_point(
            name=point_name,
            entity_id=point_entity_id,
            translate=translate,
            rotate=rotate,
        )
        vfx.base_region_name = point.name
        return vfx

    def new_spawn_point_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        **spawn_point_event_kwargs,
    ):
        if "base_region_name" in spawn_point_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        spawn_point = self.events.new_spawn_point(**spawn_point_event_kwargs)
        point = self.regions.new_point(
            name=f"_SpawnPointEvent_{spawn_point.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        spawn_point.spawn_point_region_name = point.name
        return spawn_point

    def new_message_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        **message_event_kwargs,
    ):
        if "base_region_name" in message_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        message = self.events.new_message(**message_event_kwargs)
        point = self.regions.new_point(
            name=f"_MessageEvent_{message.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        message.base_region_name = point.name
        return message

    def new_objact_event_for_object(
        self,
        obj_spec: tp.Union[str, int, IntEnum],
        obj_act_entity_id: int,
        obj_act_state: int = 0,
        obj_act_param_id: int = -1,
        obj_act_flag: int = None,
        name: str = None,
    ):
        """Add an `MSBObjActEvent` to the MSB attached to the given MSB `obj_name`.

        Entity ID (generally equal to the event ID that handles the ObjAct) must be given. All other variables are
        optional: ObjAct state (defaults to 0), ObjAct param ID (defaults to -1, i.e. the object's model ID), and
        associated state flag (defaults to 60000000 + the object's entity ID, if present).

        A `ValueError` will be raised if the `obj_name` has no entity ID and `obj_act_flag` is not given.
        """
        if isinstance(obj_spec, IntEnum):
            obj_spec = obj_spec.name
        if isinstance(obj_spec, str):
            obj = self.parts.get_entry_by_name(obj_spec, "Object")
        elif isinstance(obj_spec, int):
            obj = self.parts.get_entries("Object")[obj_spec]
        else:
            raise TypeError(f"`obj_spec` must be an index, name, or name-synchronised `IntEnum`, not {obj_spec}.")
        if obj_act_flag is None:
            if obj.entity_id <= 0:
                raise ValueError(
                    f"Cannot automatically set `obj_act_flag` for ObjAct attached to object '{obj.name}', as it does "
                    f"not have a valid entity ID."
                )
            obj_act_flag = 60000000 + obj.entity_id
        if name is None:
            name = f"_ObjAct_{obj.name.lstrip('_')}"
        return self.events.new_obj_act(
            name=name,
            obj_act_part_name=obj.name,
            obj_act_entity_id=obj_act_entity_id,
            obj_act_param_id=obj_act_param_id,
            obj_act_state=obj_act_state,
            obj_act_flag=obj_act_flag,
        )
