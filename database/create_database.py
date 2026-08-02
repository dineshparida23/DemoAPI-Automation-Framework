import sqlite3

connection = sqlite3.connect("database/demo.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

cursor.execute("DELETE FROM users")

cursor.executemany(
    """
    INSERT INTO users (id, name, email)
    VALUES (?, ?, ?)
    """,
    [
        (1, "Dinesh", "dinesh@gmail.com"),
        (2, "Rahul", "rahul@gmail.com"),
        (3, "Amit", "amit@gmail.com")
    ]
)

connection.commit()

connection.close()

print("Database created successfully!")