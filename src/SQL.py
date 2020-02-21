import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

# c.execute("""CREATE TABLE users (
#            first text,
#            last text,
#            device text
#        )""")
#c.execute("INSERT INTO users VALUES ('Bob', 'Wild', 'firealarm')")


def insert_user(user):
    with conn:
        c.execute(
            "INSERT INTO users VALUES (:username, :first, :last, :device), {'username':user.username, 'first': user.first, 'last': user.last, 'pay': user.device")


def get_user_by_name(lastname):
    c.execute("SELECT * FROM users WHERE last=:last", {'last':})


c.execute("SELECT * FROM users")
for i in c.fetchall():
    print(i)
conn.commit()

conn.close()
