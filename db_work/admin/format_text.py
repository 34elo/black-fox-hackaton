def format_schedule_table(schedule, shop_name) -> str:
    """Форматирует расписание в виде таблицы."""

    # Определение максимальной длины для выравнивания
    max_day_len = max(len(day) for day in schedule)
    max_name_len = max(max(len(name) for name in shifts.values()) for shifts in schedule.values())

    header = f"| {'День':<{max_day_len}} | {'Утро':<{max_name_len}} | {'Вечер':<{max_name_len}} |\n"
    separator = f"|{'-' * (max_day_len + 2)}|{'-' * (max_name_len + 2)}|{'-' * (max_name_len + 2)}|\n"

    table = header + separator
    for day, shifts in schedule.items():
        morning_shift = shifts.get("Утро", " - ")
        evening_shift = shifts.get("Вечер", " - ")
        table += f"| {day:<{max_day_len}} | {morning_shift:<{max_name_len}} | {evening_shift:<{max_name_len}} |\n"

    formatted_text = f"<b>График работы магазина: {shop_name}</b>\n<pre>{table}</pre>"
    return formatted_text  # <pre> чтобы форматирование выглядело таблицей
