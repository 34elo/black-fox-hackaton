import sqlite3

POINTS = ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
          'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
          'Энергетический_проезд3/4', 'Крупской_42', 'Студенческая_6']

DAYS_LST = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']


def get_all_points():
    return POINTS


def get_free_shift(point):
    connection = sqlite3.connect('data/schedule.sqlite')
    cursor = connection.cursor()
    res = cursor.execute(f'''
        SELECT * FROM "{point}"
        ''').fetchall()
    tx = 'Вам доступны следующие смены:\n'
    for i in range(1, len(res[0])):
        if res[0][i] is None:
            tx += f'{DAYS_LST[i - 1]}\n'
    return tx


def get_name_from_username(username):
    connection = sqlite3.connect('data/users_data.sqlite')
    cursor = connection.cursor()
    res = cursor.execute(f'''
    SELECT "ФИО" FROM "employees_wishes" WHERE "Username TG" = "{username}"
    ''').fetchone()
    return res


def viev_schedule(ful_name):
    result = []
    for point in POINTS:
        connection = sqlite3.connect('data/schedule.sqlite')
        cursor = connection.cursor()
        res = cursor.execute(f'''
                SELECT * FROM "{point}"
                ''').fetchall()
        for i in range(1, len(res[0])):
            if res[0][i] == ful_name:
                result.append(f'{point} {DAYS_LST[i - 1]}')
    if result:
        result = 'Вот смены на которых вы работаете: \n' + '; '.join(result)
    else:
        result = 'Видимо на этой неделе у вас нет смен) Решили взять выходной?'

    return result


# connection = sqlite3.connect('../../data/users_data.sqlite')
# cursor = connection.cursor()
# cursor.execute(f'''
# UPDATE "employees_wishes"
# SET "ФИО" = "Иван Иванов"
# WHERE "ФИО" = "Петр Максимович Астафьев"
# ''')
# connection.commit()
# connection.close()
# res = cursor.execute(f'''
# SELECT * FROM "employees_wishes"
# ''').fetchall()
# print(res)
def get_all_admins():
    connection = sqlite3.connect('data/users_data.sqlite')
    cursor = connection.cursor()
    res = cursor.execute(f'''
        SELECT username, "ФИО" FROM "admin_passwords"
    ''').fetchall()
    return [list(map(lambda x: x[0], res)), list(map(lambda x: x[1], res))]


def contact_with_admin():
    pass


def set_work_points(username, args):
    print(username)
    connection = sqlite3.connect('data/users_data.sqlite')
    cursor = connection.cursor()
    try:
        res = cursor.execute(f'''
        SELECT "Желаемые точки" FROM employees_wishes
        WHERE "Username TG" = "{username}"
''').fetchone()[0]
    except Exception as e:
        print(e)
    if res:
        res += f';{args}'
    else:
        res = args
    cursor.execute(f'''
    UPDATE employees_wishes
    SET "Желаемые точки" = "{res}"
    WHERE "Username TG" = "{username}"
    ''')
    connection.commit()
    connection.close()

def set_work_schedule(username, args):
    connection = sqlite3.connect('data/users_data.sqlite')
    cursor = connection.cursor()
    try:
        res = cursor.execute(f'''
        SELECT "Желаемые смены" FROM employees_wishes
        WHERE "Username TG" = "{username}"
''').fetchone()[0]
    except Exception as e:
        print(e)
    if res:
        res += f';{args}'
    else:
        res = args
    cursor.execute(f'''
    UPDATE employees_wishes
    SET "Желаемые смены" = "{res}"
    WHERE "Username TG" = "{username}"
    ''')
    connection.commit()
    connection.close()



# def set_work_points(username, args):
#     connection = sqlite3.connect('../data/users_data.sqlite')
#     cursor = connection.cursor()
#     res = list(cursor.execute(f'''
#     SELECT "Желаемые точки" FROM employees_wishes
#     WHERE Username TG = "{username}"
#     ''').fetchone()[0])
#     if res:
#         res += f';{args}'
#     else:
#         res = args
#     cursor.execute(f'''
#     UPDATE employees_wishes
#     SET "Желаемые точки" = "{res}",
#     WHERE Username TG = "{username}"
#     ''')
#     connection.commit()
#     connection.close()
def get_all_schedule():
    return DAYS_LST
