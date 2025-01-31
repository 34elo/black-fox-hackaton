def insert_to_schedule(point, day, employee, way_to_schedule='data/schedule.sqlite') -> None:
    import sqlite3
    print(point)
    print(day)
    print(employee)
    print(way_to_schedule)

    data = sqlite3.connect(way_to_schedule)
    data_cursor = data.cursor()
    data_cursor.execute(f'UPDATE "{point}" '
                        f'SET "{day}" = "{employee}" '
                        f'WHERE "Неделя" = "1"').fetchall()
    data.commit()
    data.close()
