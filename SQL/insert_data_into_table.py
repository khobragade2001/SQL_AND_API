import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    database="khobragade",
    passwd="654321")

cursor = connection.cursor()

### To insert multiple data at a same time
insert = "insert into emp (cust_id,cust_name,cust_city) values (%s, %s, %s)"
lists = [
        # (1,'Ashish','Yavatmal'),
        #  (2,'Mahesh','Nashik'),
        #  (3,'vijay','Hedrabad'),
        #  (4,'Shivamani','Rangareddy'),
        #  (5,'Balasubramanyam','Kerla'),
         (6,'Gurpeet','Bhatinda')]
cursor.executemany(insert,lists)
connection.commit()