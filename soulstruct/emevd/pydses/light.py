from soulstruct.emevd.pydses import format_instruction


def set_area_texture_parambank_slot_index(area_id, texture_parambank_slot_index):
    event_format = ['2003', '19', 'hh']
    return format_instruction(event_format, area_id, texture_parambank_slot_index)