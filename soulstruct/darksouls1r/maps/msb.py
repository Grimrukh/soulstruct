__all__ = ["MSB"]

import logging

from soulstruct.base.maps.msb import MSB as _BaseMSB, ENTITY_GAME_TYPES
from soulstruct.games import DarkSoulsDSRType

from .constants import VANILLA_MSB_TRANSLATIONS
from .models import MSBModelList
from .events import MSBEventList
from .regions import MSBRegionList
from .parts import MSBPartList

_LOGGER = logging.getLogger(__name__)


class MSB(_BaseMSB, DarkSoulsDSRType):
    """Only difference from DS1PTDE is in the methods."""

    MODEL_LIST_CLASS = MSBModelList
    EVENT_LIST_CLASS = MSBEventList
    REGION_LIST_CLASS = MSBRegionList
    PART_LIST_CLASS = MSBPartList

    models: MSBModelList
    events: MSBEventList
    regions: MSBRegionList
    parts: MSBPartList

    GAME: DarkSoulsDSRType

    def translate_entity_id_names(self):
        for entry_type_name, entry_subtypes in ENTITY_GAME_TYPES.items():
            if entry_type_name == "parts":
                continue  # translations not provided for parts (names are all ASCII already)
            translated_entity_ids = set()  # reset per entry type
            for entry_subtype in entry_subtypes:
                for entry in self[entry_type_name].get_entries(entry_subtype):
                    if entry.entity_id not in {-1, 0}:
                        if entry.entity_id in translated_entity_ids:
                            _LOGGER.warning(f"Found repeated entity ID while translating: {entry.entity_id}. Ignored.")
                            continue
                        if entry.entity_id not in VANILLA_MSB_TRANSLATIONS:
                            _LOGGER.warning(f"Unexpected entity ID for vanilla DSR: {entry.entity_id}. Not translated.")
                        else:
                            old_name = entry.name
                            entry.name = VANILLA_MSB_TRANSLATIONS[entry.entity_id]
                            self.rename_references(old_name, entry.name, entry_types=[entry_type_name])
                            translated_entity_ids.add(entry.entity_id)
