import sqlite3


def get_data_about_point(arg) -> {}:

    conn = sqlite3.connect('data/schedule.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM "{arg}"')
    conn.commit()

    data = list(cursor.fetchall()[0][1:])
    data = list(map(str, data))

    schedule = {
        "Понедельник": [0],
        "Вторник": [1],
        "Среда": [2],
        "Четверг": [3],
        "Пятница": [4],
        "Суббота": [5],
        "Воскресенье": [6],
    }
    return schedule
