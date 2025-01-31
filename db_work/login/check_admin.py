def check_admin_code(password) -> bool:  # проверка на админа в бд
    import sqlite3

    data = sqlite3.connect('data/users_data.sqlite')
    data_cursor = data.cursor()
    data = data_cursor.execute('''SELECT "Пароль" 
                                  FROM admin_passwords''').fetchall()
    data = [i[0] for i in data]
    return True if password in data else False
