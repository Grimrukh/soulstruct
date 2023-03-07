from __future__ import annotations

import logging
import typing as tp

from soulstruct.base.project.editors.lighting import LightingEditor as _BaseLightingEditor
from soulstruct.exceptions import InvalidFieldValueError

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params.draw_param import DrawParam
    from .links import WindowLinker

_LOGGER = logging.getLogger(__name__)


class LightingEditor(_BaseLightingEditor):

    linker: WindowLinker

    def __init__(self, project, linker, master=None, toplevel=False):
        self.auto_inject = None
        self.injection_delay_warning_done = False
        super().__init__(project, linker, master=master, toplevel=toplevel)

    def build(self, super_only=False):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(
                pady=10, sticky="w", row_weights=[1], column_weights=[1, 0, 0, 1, 1, 1], auto_columns=0
            ):
                map_display_names = [f"{k} [{v}]" for k, v in self.lighting.DRAW_PARAM_AREAS.items()]
                self.map_area_choice = self.Combobox(
                    values=map_display_names,
                    on_select_function=self._on_map_area_choice,
                    width=40,
                    padx=10,
                    label="Map Area:",
                    label_position="left",
                    font=self.CONFIG.REGULAR_FONT,
                ).var
                self.slot_choice_label = self.Label(text="Slot:", padx=(30, 0))
                self.slot_choice = self.Combobox(
                    values=("0", "1"), font=self.CONFIG.REGULAR_FONT,
                    on_select_function=self._on_slot_choice, width=2, padx=10
                )
                self.Button(
                    text="Copy Slot 0 to Slot 1",
                    bg="#622",
                    width=25,
                    padx=5,
                    command=self.regenerate_slot_1,
                )
                self.Button(
                    text="Inject This Param",
                    bg="#622",
                    width=20,
                    padx=(50, 10),
                    command=self.inject_current_param,
                )
                self.auto_inject = self.Checkbutton(
                    label="Auto Inject", command=self.toggle_auto_inject,
                )

            super(_BaseLightingEditor, self).build()

    def get_category_data(self, category=None) -> tp.Union[DrawParam, dict]:
        """Overridden just for return type."""
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        map_area_choice = self.get_map_area_name()
        slot_choice = int(self.slot_choice.var.get())
        return self.lighting.get_drawparambnd(map_area_choice).get_draw_param_slot(category, slot_choice)

    def inject_current_param(self):
        """Hook into game memory and update the current param."""
        if not self.linker.hook_created:
            if (
                self.CustomDialog(
                    title="Cannot Write Memory",
                    message="Game has not been hooked. Would you like to try hooking into the game now?",
                    default_output=0,
                    cancel_output=1,
                    return_output=0,
                    button_names=("Yes, hook in", "No, forget it"),
                    button_kwargs=("YES", "NO"),
                )
                == 1
            ):
                return
            if not self.linker.runtime_hook():
                return

        self._show_injection_warning()

        self.linker.inject_draw_param(
            draw_param=self.get_category_data(),
            area_id=int(self.get_map_area_name()[1:3]),
            slot=int(self.slot_choice.var.get()),
        )

    def toggle_auto_inject(self):
        if not self.auto_inject.var.get():
            return
        if not self.linker.hook_created:
            if (
                self.CustomDialog(
                    title="Cannot Write Memory",
                    message="Game has not been hooked. Would you like to try hooking into the game now?",
                    default_output=0,
                    cancel_output=1,
                    return_output=0,
                    button_names=("Yes, hook in", "No, forget it"),
                    button_kwargs=("YES", "NO"),
                )
                == 1
            ):
                return
            if not self.linker.runtime_hook():
                return
            self._show_injection_warning()

    def change_field_value(self, field_name: str, new_value):
        """Auto-injects new value if enabled."""
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            field_dict[field_name] = new_value
        except InvalidFieldValueError as e:
            _LOGGER.error(f"Invalid value {new_value} for field {field_name}. Error: {str(e)}")
            self.bell()
            self.CustomDialog(title="Field Value Error", message=str(e))
            return False
        if self.auto_inject.var.get():
            self._show_injection_warning()
            self.linker.inject_draw_param(
                draw_param=self.get_category_data(),
                area_id=int(self.get_map_area_name()[1:3]),
                slot=int(self.slot_choice.var.get()),
            )
        return True

    def _show_injection_warning(self):
        if not self.injection_delay_warning_done:
            self.CustomDialog(
                title="Injecting Lighting Data",
                message=(
                    "Note that Soulstruct will briefly pause the first time you inject a new lighting table\n"
                    "as it locates and saves the table's location in game memory."
                ),
            )
            self.injection_delay_warning_done = True
