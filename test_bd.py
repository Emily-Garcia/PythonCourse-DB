#crear una base de datos
import sqlite3

#conn es el nombre del archivo
#entre los parentesis va el nombre de la base de datos
conn = sqlite3.connect('test.db')
print('Database connection succesfully')
