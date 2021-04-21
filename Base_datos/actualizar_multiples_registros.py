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

# Crear sentencia SQL para actualizar múltiples registros en bd
sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = (
  ('JULIAN', 'FLORES', 'julian.flores@ues.mx', 1),
  ('IVAN', 'BUELNA', 'ivan.buelna@ues.mx', 2),
  ('FERNANDA', 'CARO', 'fernanda.caro@ues.mx', 3)
)

# Creamos la variable cursor y utilizaremos el método execute()
# Le pasaremos como parámetros la consulta SQL y los valores
cursor.executemany(sql, valores)

# Guardamos la información en la base de datos
# Utilizaremos el objeto de conexión invocando el método commit()
conexion.commit()

# Recuperar los registros que se han actualizado en la base de datos
registros_actualizados = cursor.rowcount
print(f'Registros Actualizados: {registros_actualizados}')

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
