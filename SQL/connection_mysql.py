import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()
## To create table
cursor.execute("CREATE TABLE EMP (cust_id int, cust_name VARCHAR(255), cust_city VARCHAR(100) );")
connection.commit()

# To insert data into table
query = "insert into emp (cust_id,cust_name,cust_city) values (5, 'Abhinandan','Kondareddy');"
cursor.execute(query)
connection.commit()
connection.close()

