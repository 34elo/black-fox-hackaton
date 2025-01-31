def get_id_user(name):
    import sqlite3
    data = sqlite3.connect('../../data/users_data.sqlite')
    data_cursor = data.cursor()
    data_cursor.execute(f"select 'Username TG' from employees_wishes where 'ФИО' = {name}")
    data = data_cursor.fetchone()

    return data
