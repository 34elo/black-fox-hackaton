def already_auth(chat_id) -> (bool, bool):  # уже зареган(true) / админ или сотрудник(false)
    import sqlite3
    a = False
    b = False
    data = sqlite3.connect('data/users_data.sqlite')
    data_cursor = data.cursor()
    datas = data_cursor.execute(f'''SELECT chatID FROM chatID_and_roles''').fetchall()
    for item in datas:
        if chat_id == item[0]:
            a = True
            if "Администратор" == item[1]:
                b = True
    data.commit()
    data.close()

    a, b = True, True # ЗАГЛУШКА
    return a, b
