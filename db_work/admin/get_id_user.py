def get_id_user(name):
    import sqlite3
    conn = sqlite3.connect('../../data/users_data.sqlite')
    data_cursor = conn.cursor()
    data = data_cursor.execute(f"select 'Username TG' from employees_wishes where 'ФИО' = '{name}'").fetchall()

    return data


print(get_id_user('Петр Максимович Астафьев'))
