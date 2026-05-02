import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="pp2_test_1",
    user="postgres", password="        "
)
cur = conn.cursor()

#deleting
cur.execute("""
    DROP TABLE IF EXISTS phones CASCADE;
    DROP TABLE IF EXISTS contacts CASCADE;
    DROP TABLE IF EXISTS groups CASCADE;
""")

cur.execute("""
    CREATE TABLE groups (
        id   SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE contacts (
        id       SERIAL PRIMARY KEY,
        name     VARCHAR(100) NOT NULL,
        email    VARCHAR(100) UNIQUE,
        birthday DATE,
        group_id INTEGER REFERENCES groups(id)
    );
""")

cur.execute("""
    CREATE TABLE phones (
        id         SERIAL PRIMARY KEY,
        contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
        phone      VARCHAR(20) NOT NULL,
        type       VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
    );
""")

cur.execute("""
    INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Friend'), ('Other')
    ON CONFLICT (name) DO NOTHING;
""")

cur.execute("""
        INSERT INTO contacts (name,  email, birthday, group_id)
        VALUES(    'Alice','alice@email.com','1990-05-15',(SELECT id FROM groups WHERE name = 'Work'));""")

cur.execute("""INSERT INTO phones (contact_id, phone, type) VALUES (1, '555-1234','home');""")

cur.execute("""INSERT INTO phones (contact_id, phone, type) VALUES (1, '555-5678','work');""")

conn.commit()       
print("Table created.")

cur.close()
conn.close()