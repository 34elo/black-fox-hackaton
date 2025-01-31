def check_worker_code(password) -> bool:  # проверка на сотрудника в бд
    import sqlite3

    data = sqlite3.connect('data/users_data.sqlite')
    data_cursor = data.cursor()
    data = data_cursor.execute('''SELECT "Пароль" 
                                      FROM employees_passwords''').fetchall()
    data = [i[0] for i in data]
    return True if password in data else False
