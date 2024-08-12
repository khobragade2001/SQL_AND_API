import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()

## Delete data
delete = "delete from khobragade.emp where cust_name = 'Mahesh'"
cursor.execute(delete)
connection.commit()
print("Records Deleted....")

# Truncate Data
# truncate = "truncate table khobragade.emp"
# cursor.execute(truncate)
# connection.commit()