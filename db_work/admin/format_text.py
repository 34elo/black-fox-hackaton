def format_worker_schedule_table(schedule_data, name_column_title, table_title='Расписание'):
    days = list(schedule_data.keys())
    names = list(schedule_data.values())

    max_name_length = max(len(name) for name in names if name != 'None')
    if max_name_length == 0:
        max_name_length = 4

    column_width_day = max(len(day) for day in days) + 2
    column_width_name = max_name_length + 2

    title_width = len(table_title) + 4
    title_row = f"{' ' * ((column_width_day + column_width_name - title_width) // 2)}{table_title}\n"

    header = f"{'День'.ljust(column_width_day)} {name_column_title.ljust(column_width_name)}"
    separator = f"{'-' * column_width_day} {'-' * column_width_name}"

    row = ""
    for i, day in enumerate(days):
        row += f"{day.ljust(column_width_day)} {names[i].ljust(column_width_name)}\n"

    table = title_row + header + "\n" + separator + "\n" + row
    return table
