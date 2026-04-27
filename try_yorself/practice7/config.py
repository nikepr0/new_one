import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="pp3",
    user="postgres",
    password=""
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook1 (
        id         SERIAL       PRIMARY KEY,
        name       VARCHAR(100) NOT NULL,
        phonehumber  INTEGER NOT NULL
    );
""")

conn.commit()       # IMPORTANT: persist the changes
print("Table created.")

cur.close()
conn.close()