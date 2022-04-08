import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user=" root", password="", database=" cadastor")


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM clientes")
clientes = mycursor.fetchall()


for cliente in clientes:
    print(cliente)
