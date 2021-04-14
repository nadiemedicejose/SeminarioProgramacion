# Importación del módulo psycopg2
import psycopg2

conexion = psycopg2.connect(user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'test')

# Realizar una consulta
cursor = conexion.cursor()

# Crear sentencia SQL, utilizando una variable
sql = 'SELECT * FROM persona WHERE id_persona = %s'

# Creamos una variable y asignamos un valor
id_persona = int(input("Ingresa el valor que deseas buscar: "))

# Creamos una tupla asignando la variable
llave_primaria = (id_persona,)

# Utilizar como parámetros la sentencia SQL y la tupla
cursor.execute(sql, llave_primaria)

# Recuperar los registros
registros = cursor.fetchone()

# Utilizando el método Print
print(registros)

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
