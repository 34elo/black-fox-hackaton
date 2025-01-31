import sqlite3

from aiogram import Bot


def send_notifications(message) -> None:
    conn = sqlite3.connect('data/users_data.sqlite')
    cursor = conn.cursor()
    data = cursor.execute('SELECT chatID FROM chatID_and_roles WHERE role = "Сотрудник"').fetchall()
    for item in data:
        Bot(token='7970347344:AAGhbs_C2DoGZpFOJ_ywDEwUbjzFS3WajVs').send_message(item, message)
    conn.close()
