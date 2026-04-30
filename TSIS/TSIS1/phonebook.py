import psycopg2
import json
import csv
from config import params

def get_connection():
    return psycopg2.connect(**params)

# --- НОВАЯ ФУНКЦИЯ: Импорт из CSV (Task 3.3 Extended) ---
def import_from_csv(filename="TSIS1/contacts.csv"):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # 1. Работа с группой (создаем если нет)
                        cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (row['group_name'],))
                        cur.execute("SELECT id FROM groups WHERE name = %s", (row['group_name'],))
                        group_id = cur.fetchone()[0]

                        # 2. Проверка дубликата контакта
                        cur.execute("SELECT id FROM contacts WHERE name = %s", (row['name'],))
                        exists = cur.fetchone()

                        if exists:
                            # Логика из условия: спрашиваем skip or overwrite
                            choice = input(f"Контакт {row['name']} уже существует. Перезаписать? (y/n): ").lower()
                            if choice != 'y':
                                continue
                            cur.execute("DELETE FROM contacts WHERE id = %s", (exists[0],))

                        # 3. Вставка контакта
                        cur.execute("""
                            INSERT INTO contacts (name, email, birthday, group_id)
                            VALUES (%s, %s, %s, %s) RETURNING id
                        """, (row['name'], row['email'], row['birthday'], group_id))
                        
                        contact_id = cur.fetchone()[0]

                        # 4. Вставка телефона
                        cur.execute("""
                            INSERT INTO phones (contact_id, phone, type)
                            VALUES (%s, %s, %s)
                        """, (contact_id, row['phone'], row['phone_type']))
                
                conn.commit()
        print("✅ Данные из CSV успешно импортированы!")
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

# ... (остальные функции: export_to_json, search, paginated_view остаются такими же) ...

def main():
    while True:
        print("\n==== PHONEBOOK MENU ====")
        print("1. Search (Name/Email/Phone)")
        print("2. Paginated View")
        print("3. Export to JSON")
        print("4. Import from JSON")
        print("5. Filter by Group")
        print("6. Import from CSV") # Добавили этот пункт
        print("0. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            q = input("Введите запрос для поиска: ")
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
                    results = cur.fetchall()
                    for r in results: print(r)
        elif choice == '2':
            paginated_view()
        elif choice == '3':
            export_to_json()
        elif choice == '4':
            import_from_json()
        elif choice == '5':
            # Логика фильтрации
            g = input("Введите название группы: ")
            # ... вызвать SELECT с фильтром ...
        elif choice == '6':
            import_from_csv("TSIS1/contacts.csv") # Вызов новой функции
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()