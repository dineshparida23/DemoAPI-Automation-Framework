import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("database/demo.db")
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        self.cursor.execute(
            "SELECT id, name, email FROM users WHERE id=?",
            (user_id,)
        )

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()