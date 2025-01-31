def insert_to_schedule(point, day, employee):
    import sqlite3

    data = sqlite3.connect('../data/schedule.sqlite')
    data_cursor = data.cursor()
    data_cursor.execute(f'UPDATE "{point}" '
                        f'SET "{day}" = "{employee}" '
                        f'WHERE "Неделя" = "1"').fetchall()
    data.commit()
    data.close()
    return True, True
