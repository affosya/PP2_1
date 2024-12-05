import sqlite3
import csv

# Подключение к базе данных SQLite
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS PhoneBook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    phone_number TEXT UNIQUE NOT NULL
)
''')

# Функция для добавления данных из консоли
def add_entry():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    try:
        cursor.execute('''
        INSERT INTO PhoneBook (first_name, last_name, phone_number)
        VALUES (?, ?, ?)
        ''', (first_name, last_name, phone_number))
        conn.commit()
        print("Запись успешно добавлена!")
    except sqlite3.IntegrityError:
        print("Номер телефона уже существует!")

# Функция для загрузки данных из CSV
def upload_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовок
            for row in reader:
                cursor.execute('''
                INSERT OR IGNORE INTO PhoneBook (first_name, last_name, phone_number)
                VALUES (?, ?, ?)
                ''', (row[0], row[1], row[2]))
            conn.commit()
        print("Данные из CSV успешно загружены!")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

# Функция для обновления данных
def update_entry():
    phone_number = input("Введите номер телефона для обновления: ")
    new_first_name = input("Введите новое имя (оставьте пустым, если не нужно менять): ")
    new_last_name = input("Введите новую фамилию (оставьте пустым, если не нужно менять): ")
    
    if new_first_name:
        cursor.execute('''
        UPDATE PhoneBook SET first_name = ? WHERE phone_number = ?
        ''', (new_first_name, phone_number))
    if new_last_name:
        cursor.execute('''
        UPDATE PhoneBook SET last_name = ? WHERE phone_number = ?
        ''', (new_last_name, phone_number))
    
    conn.commit()
    print("Запись успешно обновлена!")

# Функция для записи данных в файл
def export_to_file():
    cursor.execute('SELECT * FROM PhoneBook')
    results = cursor.fetchall()
    
    file_path = input("Введите путь для сохранения файла (например, name.txt): ")
    try:
        with open(file_path, 'w') as file:
            for row in results:
                file.write(f"Имя: {row[1]}, Фамилия: {row[2]}, Номер: {row[3]}\n")
        print("Данные успешно записаны в файл!")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Функция для поиска данных
def query_entries():
    filter_value = input("Введите имя, фамилию или номер для поиска: ")
    cursor.execute('''
    SELECT * FROM PhoneBook
    WHERE first_name LIKE ? OR last_name LIKE ? OR phone_number LIKE ?
    ''', (f"%{filter_value}%", f"%{filter_value}%", f"%{filter_value}%"))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("Записей не найдено!")

# Функция для удаления данных по имени или номеру
def delete_entry():
    identifier = input("Введите имя или номер телефона для удаления: ")
    cursor.execute('''
    DELETE FROM PhoneBook
    WHERE first_name = ? OR phone_number = ?
    ''', (identifier, identifier))
    conn.commit()
    print("Запись успешно удалена!")

# Функция для удаления всех данных
def delete_all_entries():
    confirm = input("Вы уверены, что хотите удалить все данные? (yes/no): ")
    if confirm.lower() == 'yes':
        cursor.execute('DELETE FROM PhoneBook')
        conn.commit()
        print("Все записи успешно удалены!")
    else:
        print("Операция отменена.")

# Главное меню
def main():
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить запись")
        print("2. Загрузить данные из CSV")
        print("3. Обновить запись")
        print("4. Запрос записей")
        print("5. Экспорт данных в файл")
        print("6. Удалить запись")
        print("7. Удалить все записи")
        print("8. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            file_path = input("Введите путь к CSV-файлу: ")
            upload_from_csv(file_path)
        elif choice == '3':
            update_entry()
        elif choice == '4':
            query_entries()
        elif choice == '5':
            export_to_file()
        elif choice == '6':
            delete_entry()
        elif choice == '7':
            delete_all_entries()
        elif choice == '8':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

    conn.close()

if __name__ == "__main__":
    main()
