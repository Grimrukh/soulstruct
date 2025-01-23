"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).
"""
from __future__ import annotations

__all__ = [
    "EVSInstructionCompiler",
]

import logging

from soulstruct.base.events.evs.compiler import EVSInstructionCompiler as _BaseCompiler
from soulstruct.base.events.emevd.utils import get_coord_entity_type
from soulstruct.bloodborne.game_types import *

from .emedf import EMEDF_ALIASES
from ..enums import *

_LOGGER = logging.getLogger("soulstruct")


class EVSInstructionCompiler(_BaseCompiler):

    EMEDF_ALIASES = EMEDF_ALIASES

    def EnableObjectActivation(self, obj: ObjectTyping, obj_act_id: int, relative_index=None):
        """
        Allows the given ObjAct to be performed with the object, optionally only at the given relative_index.
    
        I've combined two instructions into one here, as they're very similar.
        """
        if relative_index is None:
            return self._base_compile(
                "SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=True
            )
        return self._base_compile(
            "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=True
        )

    def DisableObjectActivation(self, obj: ObjectTyping, obj_act_id, relative_index=None):
        """
        Prevents the given ObjAct from being performed with the object.
    
        Used for doors that you can only open once, for example. Again, I've combined the relative index version here.
        """
        if relative_index is None:
            return self._base_compile("SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=False)
        return self._base_compile(
            "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=False
        )

    def AwardItemLot(self, item_lot: int, host_only=True):
        """Directly award an item lot to player(s). By default, only the host receives the item."""
        if host_only:
            return self._base_compile("AwardItemLotToHostOnly", item_lot=item_lot)
        return self._base_compile("AwardItemLotToAllPlayers", item_lot=item_lot)

    def PlayCutscene(
        self,
        cutscene_id: int,
        cutscene_flags: int = 0,
        player_id: int = None,
        game_map: MapTyping = None,
        move_to_region: RegionTyping = None,
        rotation: int = 0,
        relative_rotation_axis_x: float = 0.0,
        relative_rotation_axis_z: float = 0.0,
        vertical_translation: float = 0.0,
    ):
        """Unified instruction for playing cutscenes. EMEVD has several instructions for playing cutscenes that allow
        different side-effects like playing the cutscene to a specific player, moving a player to a new region/map, or
        rotating a player. This method detects the appropriate low-level instruction to call.
    
        Args:
            cutscene_id: six-digit cutscene ID which looks up "remo/scn{cutscene_id}.remobnd" in your game files.
            cutscene_flags: bit flags from `CutsceneFlags`, e.g. for unskippable or fade-out cutscenes. Cutscenes are
                generally not skippable in multiplayer.
            player_id: player who will see cutscene or be moved/rotated. Defaults to host player (`10000`). Note that 
                other players, e.g. summons, will generally have their own cutscene be played to them in their own 
                EMEVD.
            game_map: game map that player will be moved to (`move_to_region` also required).
            move_to_region: MSB region that player will be moved to (`game_map` also required).
            rotation: degrees around Y axis by which to rotate `player_id` after the cutscene is done. Cannot be used 
                with `move` args, but can be used with `vertical_translation`. Used once in known vanilla EMEVD, after 
                you move the giant Anor Londo elevator for the first time in DS1.
            relative_rotation_axis_x: world X coordinate that `rotation` is relative to. Default is 0.0.
            relative_rotation_axis_z: world Z coordinate that `rotation` is relative to. Default is 0.0
            vertical_translation: vertical distance player should be moved. Can be used with `rotation`. Note that this 
                is never used in any Soulstruct-supported game.
        """
        if game_map or move_to_region:
            if not (game_map and move_to_region):
                raise ValueError("You must set both 'game_map' and 'move_to_region' for cutscene moves, or neither.")
            if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
                raise ValueError("You cannot use move arguments AND rotation/translation arguments with cutscenes.")
            if player_id is None:
                return self._base_compile(
                    "PlayCutsceneAndMovePlayer",
                    cutscene_id=cutscene_id,
                    cutscene_flags=cutscene_flags,
                    move_to_region=move_to_region,
                    game_map=game_map,
                )
            return self._base_compile(
                "PlayCutsceneAndMoveSpecificPlayer",
                cutscene_id=cutscene_id,
                cutscene_flags=cutscene_flags,
                move_to_region=move_to_region,
                game_map=game_map,
                player_id=player_id,
            )

        if player_id is None:
            player_id = PLAYER

        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            return self._base_compile(
                "PlayCutsceneAndRotatePlayer",
                cutscene_id=cutscene_id,
                cutscene_flags=cutscene_flags,
                relative_rotation_axis_x=relative_rotation_axis_x,
                relative_rotation_axis_z=relative_rotation_axis_z,
                rotation=rotation,
                vertical_translation=vertical_translation,
                player_id=player_id,
            )

        return self._base_compile(
            "PlayCutsceneToPlayer",
            cutscene_id=cutscene_id,
            cutscene_flags=cutscene_flags,
            player_id=player_id,
        )

    def Move(
        self,
        character: CharacterTyping,
        destination: CoordEntityTyping,
        dummy_id=-1,
        copy_draw_parent: MapPartTyping = None,
        set_draw_parent: MapPartTyping = None,
        short_move=False,
        destination_type=None,
    ):
        """Unified instruction for moving a character to some destination entity in the same map.
    
        Not sure what sort of optimizations 'short' makes, but it's used at various times by the game. I would guess you
        can safely use it when you are moving the character within the same draw group collision. You can also change 
        the draw parent of the moved character, which changes when it will be drawn, by setting it manually to a 
        collision in the MSB or copying it from an existing map entity (often the same entity as the warp destination).
    
        I'm calling this 'Move' to distinguish it from warping between maps, which is what people will typically think
        of when they see the term 'warp'.
        """
        if destination_type is None:
            if destination == PLAYER:
                destination_type = CoordEntityType.Character
            else:
                try:
                    destination_type = get_coord_entity_type(CoordEntityType, destination)
                except AttributeError:
                    raise AttributeError(
                        "Warp destination has no category. Use 'destination_type' keyword or a " "typed destination."
                    )
        if copy_draw_parent is not None and set_draw_parent is not None:
            raise ValueError("You cannot copy and set the draw parent at the same time.")
        if short_move:
            if copy_draw_parent or set_draw_parent:
                raise ValueError("You cannot copy or set the draw parent during a short move.")
            return self._base_compile(
                "ShortMove",
                character=character,
                destination=destination,
                dummy_id=dummy_id,
                destination_type=destination_type,
            )
        if copy_draw_parent is not None:
            return self._base_compile(
                "MoveAndCopyDrawParent",
                character=character,
                destination=destination,
                copy_draw_parent=copy_draw_parent,
                dummy_id=dummy_id,
                destination_type=destination_type,
            )
        if set_draw_parent is not None:
            return self._base_compile(
                "MoveAndSetDrawParent",
                character=character,
                destination=destination,
                set_draw_parent=set_draw_parent,
                dummy_id=dummy_id,
                destination_type=destination_type,
            )
        return self._base_compile(
            "MoveToEntity",
            character=character,
            destination=destination,
            dummy_id=dummy_id,
            destination_type=destination_type,
        )

    def IfPlayerItemState(
        self,
        condition: int, state: bool, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False
    ):
        """My wrapper for the two versions that do and do not include storage (e.g., Bottomless Box) in the test."""
        if item_type is None:
            try:
                item_type = item.get_item_enum()
            except AttributeError:
                raise AttributeError("Item type not detected. Use keyword or typed item.")
        if including_storage:
            return self._base_compile(
                "IfPlayerItemStateIncludingStorage", condition=condition, item_type=item_type, item=item, state=state
            )
        return self._base_compile(
            "IfPlayerItemStateExcludingStorage", condition=condition, item_type=item_type, item=item, state=state
        )

    # region `IfPlayerItemState` partials
    def IfPlayerHasItem(
        self, condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False
    ):
        return self.IfPlayerItemState(condition, True, item, item_type, including_storage)

    def IfPlayerHasWeapon(self, condition: int, weapon: WeaponTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, True, weapon, ItemType.Weapon, including_storage)

    def IfPlayerHasArmor(self, condition: int, armor: ArmorTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, True, armor, ItemType.Armor, including_storage)

    def IfPlayerHasRune(self, condition: int, rune: AccessoryTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, True, rune, ItemType.GemOrRune, including_storage)

    def IfPlayerHasGood(self, condition: int, good: GoodTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, True, good, ItemType.Good, including_storage)

    def IfPlayerDoesNotHaveItem(
        self,
        condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False
    ):
        return self.IfPlayerItemState(condition, False, item, item_type, including_storage)

    def IfPlayerDoesNotHaveWeapon(self, condition: int, weapon: WeaponTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, False, weapon, ItemType.Weapon, including_storage)

    def IfPlayerDoesNotHaveArmor(self, condition: int, armor: ArmorTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, False, armor, ItemType.Armor, including_storage)

    def IfPlayerDoesNotHaveRune(self, condition: int, ring: AccessoryTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, False, ring, ItemType.GemOrRune, including_storage)

    def IfPlayerDoesNotHaveGood(self, condition: int, good: GoodTyping, including_storage: bool = False):
        return self.IfPlayerItemState(condition, False, good, ItemType.Good, including_storage)

    # endregion

    def IfActionButton(
        self,
        condition: int,
        prompt_text: EventTextTyping,
        anchor_entity: CoordEntityTyping,
        anchor_type: CoordEntityType = None,
        facing_angle: float = None,
        max_distance: float = None,
        dummy_id: int = -1,
        trigger_attribute: TriggerAttribute = TriggerAttribute.Human | TriggerAttribute.Hollow,
        button: int = 0,
        boss_version: bool = False,
        line_intersects: CoordEntityTyping = None,
    ):
        if anchor_type is None:
            # Anchor type will never be PLAYER here.
            try:
                anchor_type = get_coord_entity_type(CoordEntityType, anchor_entity)
            except AttributeError:
                raise ValueError(
                    "The `anchor_type` keyword is needed if `anchor_entity` is "
                    "not an `Object`, `Region`, or `Character`."
                )

        kwargs = dict(
            condition=condition,
            anchor_type=anchor_type,
            anchor_entity=anchor_entity,
            facing_angle=facing_angle,
            dummy_id=dummy_id,
            max_distance=max_distance,
            prompt_text=prompt_text,
            trigger_attribute=trigger_attribute,
            button=button,
        )

        if boss_version:
            if line_intersects is None:
                return self._base_compile("IfActionButtonBoss", **kwargs)
            return self._base_compile(
                "IfActionButtonBossLineIntersect", **kwargs, line_intersects=line_intersects
            )
        if line_intersects is None:
            return self._base_compile("IfActionButtonBasic", **kwargs)
        return self._base_compile(
            "IfActionButtonBasicLineIntersect", **kwargs, line_intersects=line_intersects
        )

    def DefineLabel(self, label: Label | int):
        """Wrapper for generating any valid label (0-9, inclusive)."""
        if not 0 <= label <= 9:
            raise ValueError(f"Label for `DefineLabel` must be between 0 and 9, inclusive, not: {label}")
        return self._base_compile(f"DefineLabel_{int(label)}")


EVSInstructionCompiler.process_custom_instructions()
