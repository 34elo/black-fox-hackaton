def put_data(chat_id, input_role) -> None:
    import sqlite3

    data = sqlite3.connect('data/users_data.sqlite')
    data_cursor = data.cursor()
    data_cursor.execute(f'''INSERT INTO chatID_and_roles(ChatID, Role) 
                                   VALUES ({chat_id}, {input_role})''').fetchall()
    data.commit()
    data.close()
