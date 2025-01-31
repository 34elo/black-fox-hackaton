def auto_schedule_create(way_to_users_data, way_to_schedule="data/schedule.sqlite"):
    import sqlite3

    wishes = sqlite3.connect(way_to_users_data)
    wishes_cursor = wishes.cursor()
    wishes = wishes_cursor.execute('''SELECT "ФИО", "Желаемые точки", "Желаемые смены" 
                                      FROM employees_wishes''').fetchall()

    points_schedule = sqlite3.connect(way_to_schedule)
    schedule_cursor = points_schedule.cursor()
    users = wishes_cursor.execute('''SELECT "ФИО"
                                              FROM employees_wishes''').fetchall()
    users = dict([(user[0], []) for user in users])
    for wish in wishes:
        for point in wish[1].split(';'):
            for day in wish[2].split(';'):
                if schedule_cursor.execute(f'SELECT "{day}" FROM "{point}"').fetchone() == (None,) \
                        and day not in users[wish[0]]:
                    schedule_cursor.execute(f'UPDATE "{point}" '
                                            f'SET "{day}" = "{wish[0]}" '
                                            f'WHERE "Неделя" = "1"')
                    users[wish[0]].append(day)
    points_schedule.commit()
    points_schedule.close()
