import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()
query = "select * from khobragade.emp where salary= (select max(salary) from khobragade.emp)"
cursor.execute(query)
var = cursor.fetchall()
print(var)
