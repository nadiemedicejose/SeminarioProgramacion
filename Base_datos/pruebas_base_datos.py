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
sql = 'SELECT * FROM persona ORDER BY id_persona ASC'
cursor.execute(sql)

# Recuperar los registros
registros = cursor.fetchall()

# Utilizando el método Print
print(registros)

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
