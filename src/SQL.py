import sqlite3
from user import User

conn = sqlite3.connect('memory.db')

c = conn.cursor()

# c.execute("""CREATE TABLE users (
# 		   email text,
#            first text,
#            last text,
#            device text
#        )""")

def get_user_by_email(email):
    with conn:
        c.execute("SELECT * FROM users WHERE email=:email", {'email':email})
        return c.fetchall()

def insert_user(user):
    with conn:
        if get_user_by_email(user.email) == []:
            c.execute(
                "INSERT INTO users VALUES (:email, :first, :last, :device)", {'email':user.email, 'first': user.first, 'last': user.last, 'device': user.device})
            print('User with email {} succesfully added!'.format(user.email))
        else:
            print('User with email {} already exist in database!'.format(user.email))

def delete_user(user):
    with conn:
	    c.execute("DELETE FROM users WHERE email=:email", {'email':user.email})

new_user = User('osuuster@gmail.com', "Oliver", 'Suuster', 'door')
new_user2 = User('osuuster2@gmail.com', "Oliver", 'Suuster', 'door')
insert_user(new_user)
insert_user(new_user2)
print(get_user_by_email('osuuster@gmail.com'))

delete_user(new_user)
delete_user(new_user2)

print(get_user_by_email('osuuster2@gmail.com'))

conn.close()
