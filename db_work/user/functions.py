import sqlite3

POINTS = ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
          'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
          'Энергетический_проезд3/4', 'Крупской_42', 'Студенческая_6']

DAYS_LST = ['УтроПН', 'ВечерПН', 'УтроВТ', 'ВечерВТ', 'УтроСР', 'ВечерСР', 'УтроЧТ', 'ВечерЧТ', 'УтроПТ', 'ВечерПТ',
            'УтроСБ', 'ВечерСБ', 'УтроВС', 'ВечерВС']


def get_all_points():
    return POINTS


def get_free_shift(point):
    connection = sqlite3.connect('../data/schedule.sqlite')
    cursor = connection.cursor()
    res = cursor.execute(f'''
        SELECT * FROM "{point}"
        ''').fetchall()
    tx = ('Вам доступны следующие смены:\n')
    for i in range(1, len(res[0])):
        if res[0][i] == None:
            tx += f'{DAYS_LST[i - 1]}\n'
    return tx


def get_name_from_username(username):
    connection = sqlite3.connect('../data/users_data.sqlite')
    cursor = connection.cursor()
    res = cursor.execute(f'''
    SELECT "ФИО" FROM "employees_wishes" WHERE "Username TG" = "{username}"
    ''').fetchone()
    return res




def viev_schedule(ful_name):
    result = []
    for point in POINTS:
        connection = sqlite3.connect('../data/schedule.sqlite')
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




def contact_with_admin():
    pass



def set_work_points(username, args):
    connection = sqlite3.connect('../data/schedule.sqlite')
    cursor = connection.cursor()
    cursor.execute(f'''
    UPDATE employees_wishes
    SET employees_wishes = "{args}",
    WHERE Username TG = "{username}"
    ''')
    connection.commit()
    connection.close()


def set_work_shifts():
    return
