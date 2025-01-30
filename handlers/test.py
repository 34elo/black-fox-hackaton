import sqlite3

POINTS = ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
          'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
          'Энергетический_проезд3/4', 'Крупской_42']

conn = sqlite3.connect('../data/schedule.sqlite')
cursor = conn.cursor()

cursor.execute(f'SELECT * FROM "{POINTS[0]}"')
conn.commit()

print(cursor.fetchall()[0][1:])
