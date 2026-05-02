import psycopg2

conn = psycopg2.connect(
    dbname="pp2_test_1",
    user="postgres",
    password="        ",
    host="localhost"
)
cur = conn.cursor()

PAGE_SIZE = 3  # contacts per page

def get_contacts(group=None, email_search=None, sort_by="name", offset=0):
    query = """
        SELECT c.id, c.name, c.email, c.birthday, g.name as group_name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        WHERE 1=1
    """
    params = []

    if group:
        query += " AND g.name = %s"
        params.append(group)

    if email_search:
        query += " AND c.email LIKE %s"
        params.append(f"%{email_search}%")

    # sort
    allowed_sorts = {"name": "c.name", "birthday": "c.birthday", "id": "c.id"}
    order_col = allowed_sorts.get(sort_by, "c.name")
    query += f" ORDER BY {order_col}"

    # pagination
    query += " LIMIT %s OFFSET %s"
    params.extend([PAGE_SIZE, offset])

    cur.execute(query, params)
    return cur.fetchall()


def print_contacts(contacts):
    if not contacts:
        print("  No contacts found.")
        return
    for c in contacts:
        print(f"  ID: {c[0]} | Name: {c[1]} | Email: {c[2]} | Birthday: {c[3]} | Group: {c[4]}")


def paginate_loop(group=None, email_search=None, sort_by="name"):
    offset = 0
    while True:
        contacts = get_contacts(group, email_search, sort_by, offset)
        print(f"\n--- Page {offset // PAGE_SIZE + 1} ---")
        print_contacts(contacts)

        print("\n[next] [prev] [quit]")
        cmd = input(">> ").strip().lower()

        if cmd == "next":
            if len(contacts) < PAGE_SIZE:
                print("  Already on last page.")
            else:
                offset += PAGE_SIZE
        elif cmd == "prev":
            if offset == 0:
                print("  Already on first page.")
            else:
                offset -= PAGE_SIZE
        elif cmd == "quit":
            break


def main():
    while True:
        print("\n=== Contact Search & Filter ===")
        print("1. Filter by group")
        print("2. Search by email")
        print("3. Sort contacts")
        print("4. Browse all contacts")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            group = input("Enter group (Family/Work/Friend/Other): ").strip()
            sort_by = input("Sort by (name/birthday/id): ").strip() or "name"
            paginate_loop(group=group, sort_by=sort_by)

        elif choice == "2":
            email = input("Enter email to search: ").strip()
            sort_by = input("Sort by (name/birthday/id): ").strip() or "name"
            paginate_loop(email_search=email, sort_by=sort_by)

        elif choice == "3":
            sort_by = input("Sort by (name/birthday/id): ").strip() or "name"
            paginate_loop(sort_by=sort_by)

        elif choice == "4":
            paginate_loop()

        elif choice == "0":
            break

main()

cur.close()
conn.close()