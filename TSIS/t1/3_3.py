import psycopg2
import json

conn = psycopg2.connect(
    host="localhost", dbname="pp2_test_1",
    user="postgres", password="        "
)
cur = conn.cursor()

# 1 EXPORT TO JSON

def export_to_json(filename="contacts.json"):
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name as group_name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    contacts = cur.fetchall()

    result = []
    for c in contacts:
        contact_id, name, email, birthday, group_name = c

        
        cur.execute("""
            SELECT phone, type FROM phones WHERE contact_id = %s
        """, (contact_id,))
        phones = [{"phone": row[0], "type": row[1]} for row in cur.fetchall()]

        result.append({
            "name": name,
            "email": email,
            "birthday": str(birthday) if birthday else None,
            "group": group_name,
            "phones": phones
        })

    with open(filename, "w") as f:
        json.dump(result, f, indent=4)

    print(f"Exported {len(result)} contacts to {filename}")



# 2 IMPORT FROM JSON

def import_from_json(filename="contacts.json"):
    with open(filename, "r") as f:
        contacts = json.load(f)

    for c in contacts:
        name     = c["name"]
        email    = c.get("email")
        birthday = c.get("birthday")
        group    = c.get("group")
        phones   = c.get("phones", [])

        # check if contact already exists
        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cur.fetchone()

        if existing:
            print(f"  '{name}' already exists. Skip or overwrite? (skip/overwrite): ", end="")
            choice = input().strip().lower()
            if choice == "skip":
                print(f"  Skipped '{name}'")
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
                print(f"  Overwriting '{name}'...")

        # get or create group
        if group:
            cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (group,))
            cur.execute("SELECT id FROM groups WHERE name = %s", (group,))
            group_id = cur.fetchone()[0]
        else:
            group_id = None

        # insert contact
        cur.execute("""
            INSERT INTO contacts (name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (name, email, birthday, group_id))
        contact_id = cur.fetchone()[0]

        # insert phones
        for p in phones:
            cur.execute("""
                INSERT INTO phones (contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, p["phone"], p["type"]))

        print(f"  Imported '{name}'")

    conn.commit()
    print("Import done!")



# 3 MENU

def main():
    while True:
        print("\n=== Import / Export ===")
        print("1. Export contacts to JSON")
        print("2. Import contacts from JSON")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            filename = input("Enter filename (default: contacts.json): ").strip() or "contacts.json"
            export_to_json(filename)

        elif choice == "2":
            filename = input("Enter filename (default: contacts.json): ").strip() or "contacts.json"
            import_from_json(filename)

        elif choice == "0":
            break

main()

cur.close()
conn.close()