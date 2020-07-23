import sqlite3
import time

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
select_query = "SELECT * FROM baiviet"
select_query0 = "PRAGMA table_info(baiviet)"

select_query1 = "SELECT linkpost FROM baiviet WHERE username = ?"
username = 'loc'
result = cursor.execute(select_query1,(username,))
a = result.fetchall()
# print(result)
print(len(a))
#cursor.execute(select_query0)
# lock = 1
# update_query = "UPDATE users set lock = 0 WHERE lock = ?"
# cursor.execute(update_query, (lock,))

# for row in cursor.execute(select_query):
#      print(row)
# delete = "DELETE FROM logs"
# cursor.execute(delete)
# user3 = ('ha','1234',0,2)
# # insert = "INSERT INTO users VALUES(NULL,?,?,?,?)"
# # cursor.execute(insert, user3)
# query = "DELETE FROM users WHERE username = ?"
# username = "ha"
# cursor.execute(query,(username,))
# for row in cursor.execute(select_query1):
for row in a:
    print(''.join(row))

print("                          ")
for row in cursor.execute(select_query0):
    print(row)
connection.commit()
connection.close()

# print(int(time.time()))
# time.sleep(30)
#print(int(time.time()))