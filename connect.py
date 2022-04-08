
from django.forms import PasswordInput
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user=" root", password="", database=" cadastor")


mycursor = mydb.cursor()
sql = "INSERT INTO clientes(nome, idade ,email) VALUES (%s,%s,%s)"
val = [

    ("Gabriel", 23, "gabriel@gmail.com"),
    ("gb", 25, "gabriel@gmail.com")



]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "Registros inseridos")
