import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()
### data in list format
# cursor.execute("select * from khobragade.emp")
# var = cursor.fetchall()
# print(var)


### data in next line
cursor.execute("select * from khobragade.emp")
for i in cursor.fetchall():
    print(i)