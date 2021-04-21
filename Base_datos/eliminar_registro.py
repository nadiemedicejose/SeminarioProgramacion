# Importación del módulo psycopg2
import psycopg2

# Realizamos la conexión a la base de datos
conexion = psycopg2.connect(user = 'postgres',
                            password = 'Jest1994/*',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'test')

# Utilizaremos el método cursor()
cursor = conexion.cursor()

# Crear sentencia SQL para eliminar 1 registro en bd
sql = 'DELETE FROM persona WHERE id_persona = %s'
entrada = input("Ingresa el Indice que deseas eliminar: ")
valores = (entrada,)

# Creamos la variable cursor y utilizaremos el método execute()
# Le pasaremos como parámetros la consulta SQL y los valores
cursor.execute(sql, valores)

# Guardamos la información en la base de datos
# Utilizaremos el objeto de conexión invocando el método commit()
conexion.commit()

# Recuperar los registros que se han eliminado en la base de datos
registro_eliminado = cursor.rowcount
print(f'Registro Eliminado: {registro_eliminado}')

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
