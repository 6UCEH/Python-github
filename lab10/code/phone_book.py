import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="bisert",      # замените на ваше имя базы данных
    user="bisert",        # замените на ваше имя пользователя
    password="123",       # замените на ваш пароль
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            phone_number VARCHAR(20)
        )
    """)
    conn.commit()

# 2.1 Ввод данных с консоли
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()

# 2.2 Загрузка данных из CSV
def insert_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

# 3. Обновление данных
def update_user(old_value, new_value, column="first_name"):
    if column not in ["first_name", "phone_number"]:
        print("Invalid column")
        return
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, old_value))
    conn.commit()

# 4. Запросы с фильтрами
def query_data(column, value):
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    for row in cur.fetchall():
        print(row)

# 5. Удаление данных
def delete_user_by_value(column, value):
    cur.execute(f"DELETE FROM phonebook WHERE {column} = %s", (value,))
    conn.commit()

# Пример работы
def main():
    create_table()
    while True:
        print("\nМеню:\n1. Вставить вручную\n2. Вставить из CSV\n3. Обновить\n4. Найти\n5. Удалить\n6. Выйти")
        choice = input("Выберите опцию: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            path = input("Введите путь к CSV: ")
            insert_from_csv(path)
        elif choice == "3":
            col = input("Что обновить (first_name/phone_number): ")
            old = input("Старое значение: ")
            new = input("Новое значение: ")
            update_user(old, new, col)
        elif choice == "4":
            col = input("Поле (first_name/phone_number): ")
            val = input("Значение: ")
            query_data(col, val)
        elif choice == "5":
            col = input("Удалить по (first_name/phone_number): ")
            val = input("Значение: ")
            delete_user_by_value(col, val)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
