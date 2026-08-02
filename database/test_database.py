from db_utils import Database

db = Database()

users = db.execute("SELECT * FROM users")

for user in users:
    print(user)

db.close()