# Importación del módulo psycopg2
import psycopg2

# Realizamos la conexión a la base de datos
conexion = psycopg2.connect(user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'test')

# Utilizaremos el método cursor()
cursor = conexion.cursor()

# Crear sentencia SQL para editar 1 registro en bd
sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = ('PEPE', 'GRILLO', 'pepe.grillo@ues.mx', 1)

# Creamos la variable cursor y utilizaremos el método execute()
# Le pasaremos como parámetros la consulta SQL y los valores
cursor.execute(sql, valores)

# Guardamos la información en la base de datos
# Utilizaremos el objeto de conexión invocando el método commit()
conexion.commit()

# Recuperar los registros que se han actualizado en la base de datos
registro_actualizado = cursor.rowcount
print(f'Registro Actualizado: {registro_actualizado}')

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
