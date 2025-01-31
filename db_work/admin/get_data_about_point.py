import sqlite3


def get_data_about_point(arg) -> {}:

    conn = sqlite3.connect('data/schedule.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM "{arg}"')
    conn.commit()

    data = list(cursor.fetchall()[0][1:])
    data = list(map(str, data))

    schedule = {
        "Понедельник": data[0],
        "Вторник": data[1],
        "Среда": data[2],
        "Четверг": data[3],
        "Пятница": data[4],
        "Суббота": data[5],
        "Воскресенье": data[6],
    }
    return schedule

print(get_data_about_point('Дзержинского_9'))
