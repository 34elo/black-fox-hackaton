def get_working_times(way_to_users_data='data/users_data.sqlite', way_to_schedule='data/schedule.sqlite'):
    import sqlite3

    POINTS = ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
              'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
              'Энергетический_проезд3/4', 'Крупской_42', 'Студенческая_6']

    users_connection = sqlite3.connect(way_to_users_data)
    users_cursor = users_connection.cursor()
    users = users_cursor.execute('''SELECT "ФИО" FROM employees_passwords''').fetchall()

    points_schedule = sqlite3.connect(way_to_schedule)
    schedule_cursor = points_schedule.cursor()
    users = dict([(user[0], 0) for user in users])
    for point in POINTS:
        point_schedule = schedule_cursor.execute(f'SELECT * FROM "{point}"').fetchall()
        for user in users:
            if user in point_schedule[0]:
                users[user] += 1
    points_schedule.commit()
    points_schedule.close()
    return sorted(users.items(), key=lambda item: item[1], reverse=True)
