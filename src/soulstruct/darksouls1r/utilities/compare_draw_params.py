"""Script that compares two `DrawParamDirectory` instances (e.g. vanilla vs. modded) and prints all of the
values that differ between them, area by area and table by table, using `rich` for readable formatting."""
from rich.console import Console
from rich.table import Table

from soulstruct.darksouls1r.params.draw_param import DrawParamDirectory


def compare_draw_params(
    draw_params_dir_one: DrawParamDirectory,
    draw_params_dir_two: DrawParamDirectory,
    names=None,
    ignore_matches=True,
    ignore_param_names=(),
    float_diff=0.01,
):
    """Print all values that differ between the two given DSR `DrawParamDirectory` instances.

    Iterates over every map area, then every DrawParam table nickname (e.g. 'BakedLight'), then both slots (0
    and 1), comparing the non-zero (i.e. named, non-default) row entries of each table. Entries and fields that
    are missing or differ between the two directories are printed in a nested, readable format with `rich`.

    Args:
        draw_params_dir_one: First `DrawParamDirectory` to compare.
        draw_params_dir_two: Second `DrawParamDirectory` to compare.
        names: Two display names to use for the two directories in the output. Defaults to
            `("DrawParams1", "DrawParams2")`.
        ignore_matches: If True (default), only matching fields that differ are shown for each differing entry.
            If False, all fields are shown for any entry that has at least one differing field (with matching
            fields dimmed), which can be useful for context.
        ignore_param_names: Iterable of DrawParam nicknames (e.g. 'BakedLight') to skip entirely.
        float_diff: Float fields whose values differ by less than this amount are treated as equal (to ignore
            floating point imprecision).
    """
    if names is None:
        names = ("DrawParams1", "DrawParams2")

    console = Console()
    any_diff_found = False

    for area_name, area_desc in DrawParamDirectory.DRAW_PARAM_AREAS.items():
        draw_param_bnd_one = draw_params_dir_one[area_name]
        draw_param_bnd_two = draw_params_dir_two[area_name]
        area_header_printed = False

        def print_area_header():
            nonlocal area_header_printed
            if not area_header_printed:
                console.print(f"\n[bold underline cyan]{area_name}[/bold underline cyan] ({area_desc})")
                area_header_printed = True

        for param_name in draw_param_bnd_one.PARAM_NICKNAMES.values():
            if param_name in ignore_param_names:
                continue
            for slot in (0, 1):
                # NOTE: `get_draw_param_slot()` raises `KeyError` both for invalid nicknames (shouldn't happen
                # here, since `param_name` comes from `PARAM_NICKNAMES`) and for nicknames that were simply never
                # loaded into this particular `DrawParamBND` (e.g. unused tables). We treat the latter case the
                # same as an explicit `None` slot, i.e. "missing", rather than silently skipping it.
                try:
                    draw_param_one = draw_param_bnd_one.get_draw_param_slot(param_name, slot)
                except KeyError:
                    draw_param_one = None
                try:
                    draw_param_two = draw_param_bnd_two.get_draw_param_slot(param_name, slot)
                except KeyError:
                    draw_param_two = None

                if draw_param_one is None and draw_param_two is None:
                    # Neither comparand has this slot at all.
                    continue

                if draw_param_one is None or draw_param_two is None:
                    # One comparand is missing this slot entirely.
                    missing_in = names[0] if draw_param_one is None else names[1]
                    any_diff_found = True
                    print_area_header()
                    console.print(
                        f"  [yellow]{param_name}[/yellow] (slot {slot}): entire table "
                        f"[red]missing[/red] in {missing_in}"
                    )
                    continue

                entries_one = draw_param_one.get_nonzero_entries()
                entries_two = draw_param_two.get_nonzero_entries()
                all_indices = sorted(set(entries_one) | set(entries_two))
                if not all_indices:
                    continue  # both tables are empty (of non-default entries)

                table_header_printed = False

                def print_table_header():
                    nonlocal table_header_printed
                    if not table_header_printed:
                        print_area_header()
                        console.print(f"  [magenta]{param_name}[/magenta] (slot {slot}):")
                        table_header_printed = True

                for i in all_indices:
                    row_one = entries_one.get(i)
                    row_two = entries_two.get(i)

                    if row_one is None or row_two is None:
                        missing_in = names[0] if row_one is None else names[1]
                        present_row = row_two if row_one is None else row_one
                        any_diff_found = True
                        print_table_header()
                        console.print(
                            f"    \\[{i}] {present_row.Name}: [red]MISSING[/red] in {missing_in}"
                        )
                        continue

                    diff_table = Table(show_header=True, header_style="bold", box=None, padding=(0, 1, 0, 0))
                    diff_table.add_column("Field")
                    diff_table.add_column(names[0], justify="right")
                    diff_table.add_column(names[1], justify="right")

                    entry_has_diff = False
                    for (field_name_one, value_one), (field_name_two, value_two) in zip(row_one, row_two):
                        if field_name_one != field_name_two:
                            raise ValueError(
                                f"Field name mismatch in entry {i} of table {param_name} (slot {slot}) of "
                                f"area {area_name}: '{field_name_one}' vs. '{field_name_two}'."
                            )

                        values_equal = value_one == value_two
                        if not values_equal and isinstance(value_one, float) and isinstance(value_two, float):
                            if abs(value_one - value_two) < float_diff:
                                values_equal = True  # ignore float imprecision

                        if not values_equal:
                            entry_has_diff = True
                        elif ignore_matches:
                            continue  # skip matching fields entirely

                        if isinstance(value_one, float) and isinstance(value_two, float):
                            value_one_str, value_two_str = f"{value_one:.4f}", f"{value_two:.4f}"
                        else:
                            value_one_str, value_two_str = str(value_one), str(value_two)

                        row_style = None if not values_equal else "dim"
                        diff_table.add_row(field_name_one, value_one_str, value_two_str, style=row_style)

                    if entry_has_diff:
                        any_diff_found = True
                        print_table_header()
                        console.print(f"    \\[{i}] [bold]{row_one.Name}[/bold]")
                        console.print(diff_table)

    if not any_diff_found:
        console.print("[green]No differences found.[/green]")
