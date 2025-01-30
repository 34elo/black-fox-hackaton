import sqlite3


def get_data_about_point(arg) -> {}:

    conn = sqlite3.connect('data/schedule.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM "{arg}"')
    conn.commit()

    data = list(cursor.fetchall()[0][1:])
    data = list(map(str, data))

    schedule = {
        "Понедельник": {
            "Утро": data[0],
            "Вечер": data[1],
        },
        "Вторник": {
            "Утро": data[2],
            "Вечер": data[3],
        },
        "Среда": {
            "Утро": data[4],
            "Вечер": data[5],
        },
        "Четверг": {
            "Утро": data[6],
            "Вечер": data[7],
        },
        "Пятница": {
            "Утро": data[8],
            "Вечер": data[9],
        },
        "Суббота": {
            "Утро": data[10],
            "Вечер": data[11],
        },
        "Воскресенье": {
            "Утро": data[12],
            "Вечер": data[13],
        },
    }
    return schedule
