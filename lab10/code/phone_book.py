import psycopg2
import csv

# Подключение к базе данных bisert
conn = psycopg2.connect(
    dbname="bisert",           # <--  база
    user="bisert",             # <-- имя пользователя 
    password="123",              
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            phone_number VARCHAR(20)
        )
    """)
    conn.commit()

# Вставка данных вручную
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()

# Основной цикл
def main():
    create_table()
    insert_from_console()

if __name__ == "__main__":
    main()
