import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()

query = "update khobragade.emp set cust_city= %s where cust_id= %s"
values = ("Shimla",8)
cursor.execute(query,values)
connection.commit()