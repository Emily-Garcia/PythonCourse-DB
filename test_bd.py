#crear una base de datos
import sqlite3

#conn es el nombre del archivo
#entre los parentesis va el nombre de la base de datos
conn = sqlite3.connect('test.db')
print('Database connection succesfully')

# creamos una tabla en la base de datos de sql query
#lo estamos igualando a una variable
#se le debe de poner 3 comillas simples
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS user (
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        phone_number VARCHAR(15),
        date_birth DATETIME,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
'''

# creando la tabla en el programa
conn.execute(create_table_sql)
print("Table created succesfully")

# insertamos datos

insert_sql = '''
    INSERT INTO
        user (first_name, last_name, email, phone_number)
    VALUES
        ('Martin', 'Melo', 'martin.melo@gmail.com', '8828182921')
'''

insert_sql_v2 = '''
    INSERT INTO
        user (first_name, last_name, email, phone_number, date_birth)
    VALUES
    ('Emily', 'Garcia', 'emigq@gmail.com', '3283823823', '2000-11-11')
'''
#ejecutamos para que se guarden los datos en la tabla
conn.execute(insert_sql)
conn.execute(insert_sql_v2)

# hacemos un commit para que se guarden todos los cambios de la base de datos
conn.commit()

#imprimimos los datos
select_all_sql = 'SELECT rowid, first_name, last_name, email, phone_number, date_birth, timestamp FROM user'
#guardamos los datos en una variable cursos
cursor = conn.execute(select_all_sql)
for row in cursor:
    print('\n')
    print(f'ID: {row[0]}')
    print(f'Nombre: {row[1]}')
    print(f'Apellidos: {row[2]}')
    print(f'Email: {row[3]}')
    print(f'Telefono: {row[4]}')
    print(f'Fecha de nacimiento: {row[5]}') if row[5] else print('FEcha de nacimiento no especificada')
    print(f'Ultima actualizacion: {row[6]}')
    print('\n')

#actualizar la tabla
#cambiamos el nombre
update_sql = '''
    UPDATE user SET first_name = 'Ringo' WHERE rowid = 1
'''
conn.execute(update_sql)
conn.commit()

print('ROWS UPDATED: ', conn.total_changes)

select_all_sql = 'SELECT rowid, first_name, last_name, email, phone_number, date_birth, timestamp FROM user'
#guardamos los datos en una variable cursos
cursor = conn.execute(select_all_sql)
print('Showing updated data')
for row in cursor:
    print('\n')
    print(f'ID: {row[0]}')
    print(f'Nombre: {row[1]}')
    print(f'Apellidos: {row[2]}')
    print(f'Email: {row[3]}')
    print(f'Telefono: {row[4]}')
    print(f'Fecha de nacimiento: {row[5]}') if row[5] else print('FEcha de nacimiento no especificada')
    print(f'Ultima actualizacion: {row[6]}')
    print('\n')

conn.close()
print("Database connecction closed")