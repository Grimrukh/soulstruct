"""Script that compares an arbitrary number of DrawParam parameters."""
from soulstruct.darksouls1r.params.draw_param import DrawParamDirectory


def compare_draw_params(
    draw_params_one: DrawParamDirectory,
    draw_params_two: DrawParamDirectory,
    names=None,
    ignore_matches=True,
    ignore_param_names=(),
    float_diff=0.01,
):
    """View all values that differ between the two given DSR `DrawParamDirectory` instances."""

    if names is None:
        names = ("DrawParams1", "DrawParams2")

    for map_name in DrawParamDirectory.DRAW_PARAM_AREAS.keys():
        draw_blocks = [draw_params_one[map_name], draw_params_two[map_name]]
        map_printed = False
        for param_name in DrawParamDirectory.PARAM_NAMES:
            if param_name in ignore_param_names:
                continue
            try:
                draw_tables = [block[param_name] for block in draw_blocks]
            except AttributeError:
                # Table missing from at least one DrawParam.
                continue
            for slot in (0, 1):
                table_printed = False
                active_params = []
                slots = []
                if all(dt[slot] is None for dt in draw_tables):
                    if slot == 0:
                        raise ValueError(
                            f"At least one DrawParam is missing slot 0 of table {param_name} " f"in map {map_name}."
                        )
                    # Otherwise, this means all DrawParams only have one slot for this table.
                    continue
                for dt in draw_tables:
                    if dt[slot] is None:
                        # Default to slot 0.
                        active_params.append(dt[0].get_nonzero_entries())
                        slots.append(0)
                    else:
                        active_params.append(dt[slot].get_nonzero_entries())
                        slots.append(slot)
                combined_entries = []
                for ap in active_params:
                    combined_entries.extend(list(ap.keys()))
                if not combined_entries:
                    # All empty.
                    continue
                for i in range(max(combined_entries)):
                    entries = []
                    missing_entries = []
                    for j, ap in enumerate(active_params):
                        try:
                            entry = ap[i]
                        except KeyError:
                            missing_entries.append(names[j])
                        else:
                            entries.append(entry)

                    if not entries:
                        # No DrawParam has an entry with this ID.
                        continue

                    if missing_entries:
                        if not map_printed:
                            print(f"\n\n{map_name}:")
                            map_printed = True
                        if not table_printed:
                            print(f"\n      {param_name} (slots {' vs. '.join([str(s) for s in slots])}):\n")
                            table_printed = True
                        print(f"          {i}: {' | '.join([e.name for e in entries])}")
                        print(f"               <MISSING> for {', '.join(missing_entries)}")

                    name_printed = False
                    for fields in zip(*entries):
                        if not all(f[0] == fields[0][0] for f in fields[1:]):
                            print(fields)
                            raise ValueError(
                                f"Field names in entry {i} of table {param_name} (slot {slots[0]} vs. "
                                f"{slots[1]}) of map {map_name} do not match: {[f[0] for f in fields]}"
                            )
                        if any(f[1] != fields[0][1] for f in fields[1:]):

                            if ignore_matches and fields[1][1] == fields[0][1]:
                                continue

                            if all(isinstance(f[1], float) for f in fields):
                                if all(
                                    abs(fields[j][1] - fields[j + 1][1]) < float_diff for j in range(len(fields) - 1)
                                ):
                                    # Ignore float imprecision differences.
                                    continue
                            if all(isinstance(f[1], float) for f in fields):
                                values = "   ".join([f"{f[1]:.3f}" for f in fields])
                            else:
                                values = "   ".join([f"{f[1]}" + " " * (4 - len(str(f[1]))) for f in fields])

                            if not map_printed:
                                print(f"\n\n{map_name}:")
                                map_printed = True
                            if not table_printed:
                                print(f"\n      {param_name} (slots {' vs. '.join([str(s) for s in slots])}):\n")
                                table_printed = True
                            if not name_printed:
                                print(f"          {i}: {' | '.join([e.name for e in entries])}")
                                name_printed = True

                            print(f"              {fields[0][0]} {' ' * (13 - len(fields[0][0]))}: {values}")
