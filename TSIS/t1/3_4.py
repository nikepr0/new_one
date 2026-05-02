import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="pp2_test_1",
    user="postgres", password="        "
)
cur = conn.cursor()


# 1 PROCEDURE: add_phone

cur.execute("""
    CREATE OR REPLACE PROCEDURE add_phone(
        p_contact_name VARCHAR,
        p_phone        VARCHAR,
        p_type         VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    DECLARE
        v_contact_id INTEGER;
    BEGIN
        -- find contact id by name
        SELECT id INTO v_contact_id
        FROM contacts
        WHERE name = p_contact_name;

        -- if contact not found, raise error
        IF v_contact_id IS NULL THEN
            RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
        END IF;

        -- insert the new phone
        INSERT INTO phones (contact_id, phone, type)
        VALUES (v_contact_id, p_phone, p_type);

        RAISE NOTICE 'Phone % added to %', p_phone, p_contact_name;
    END;
    $$;
""")


# 2 PROCEDURE: move_to_group

cur.execute("""
    CREATE OR REPLACE PROCEDURE move_to_group(
        p_contact_name VARCHAR,
        p_group_name   VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    DECLARE
        v_contact_id INTEGER;
        v_group_id   INTEGER;
    BEGIN
        -- find contact
        SELECT id INTO v_contact_id
        FROM contacts
        WHERE name = p_contact_name;

        IF v_contact_id IS NULL THEN
            RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
        END IF;

        -- find or create group
        SELECT id INTO v_group_id
        FROM groups
        WHERE name = p_group_name;

        IF v_group_id IS NULL THEN
            INSERT INTO groups (name)
            VALUES (p_group_name)
            RETURNING id INTO v_group_id;
            RAISE NOTICE 'Group "%" created', p_group_name;
        END IF;

        -- move contact to group
        UPDATE contacts
        SET group_id = v_group_id
        WHERE id = v_contact_id;

        RAISE NOTICE 'Contact "%" moved to group "%"', p_contact_name, p_group_name;
    END;
    $$;
""")


# 3 FUNCTION: search_contacts

cur.execute("""
    CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
    RETURNS TABLE (
        id       INTEGER,
        name     VARCHAR,
        email    VARCHAR,
        birthday DATE,
        phone    VARCHAR,
        grp      VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT DISTINCT
            c.id,
            c.name,
            c.email,
            c.birthday,
            p.phone,
            g.name as grp
        FROM contacts c
        LEFT JOIN phones  p ON p.contact_id = c.id
        LEFT JOIN groups  g ON g.id = c.group_id
        WHERE
            c.name  ILIKE '%' || p_query || '%' OR
            c.email ILIKE '%' || p_query || '%' OR
            p.phone ILIKE '%' || p_query || '%';
    END;
    $$;
""")

conn.commit()
print("Stored procedures created!")



# 4 MENU — test the procedures

def main():
    while True:
        print("\n=== Stored Procedures ===")
        print("1. Add phone to contact")
        print("2. Move contact to group")
        print("3. Search contacts")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name  = input("Contact name: ").strip()
            phone = input("Phone number: ").strip()
            ptype = input("Type (home/work/mobile): ").strip()
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
            conn.commit()
            print("Done!")

        elif choice == "2":
            name  = input("Contact name: ").strip()
            group = input("Group name: ").strip()
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()
            print("Done!")

        elif choice == "3":
            query = input("Search query: ").strip()
            cur.execute("SELECT * FROM search_contacts(%s)", (query,))
            results = cur.fetchall()
            if not results:
                print("  No results found.")
            for r in results:
                print(f"  ID: {r[0]} | Name: {r[1]} | Email: {r[2]} | Birthday: {r[3]} | Phone: {r[4]} | Group: {r[5]}")

        elif choice == "0":
            break

main()

cur.close()
conn.close()