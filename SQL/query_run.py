import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()

## display perticular records
print("display perticular records : ")
query = "select cust_id, cust_name from khobragade.emp where cust_id = '5'"
cursor.execute(query)
for i in cursor.fetchall():
    print(i)

# Display duplicate records
print("Display duplicate records : ")
query2 = "select cust_id,cust_name, count(*) from khobragade.emp group by cust_id,cust_name having count(*)>1"
cursor.execute(query2)
for i in cursor.fetchall():
    print(i)

### Display unique records
print("Display unique records : ")
query3 = "select cust_id, cust_name,count(*) from khobragade.emp group by cust_id, cust_name having count(*)=1"
cursor.execute(query3)
for i in cursor.fetchall():
    print(i)

## department wise filter
print("fetch department wise data from emp_data")
query = "select * from khobragade.emp_data where department = 'Sales' and gender = 'Female'"
cursor.execute(query)
for i in cursor.fetchall():
    print(i)