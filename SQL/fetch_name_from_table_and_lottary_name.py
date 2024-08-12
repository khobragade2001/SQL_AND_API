import mysql.connector
import random

connection = mysql.connector.connect(
    user = "root",
    host = "localhost",
    database = "khobragade",
    passwd = "654321")
cursor = connection.cursor()

query = "select id,first_name from khobragade.emp_data"
cursor.execute(query)
ls = cursor.fetchall()


def select_name():
    global ls
    selection = random.choice(ls)
    return selection
selected = []

while len(selected) <3:
    name = select_name()
    if name not in selected:
        selected.append(name)

print("Congratulation.... following are win 10,00,000 $ : ",selected)