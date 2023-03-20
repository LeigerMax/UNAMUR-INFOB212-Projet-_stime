import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='dbstime')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM user')
users = cursor.fetchall()
connection.close()

print(users)