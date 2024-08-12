import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()

