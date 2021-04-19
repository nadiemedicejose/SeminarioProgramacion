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

# Crear sentencia SQL para insertar 1 registro en bd
sql = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = ('JOEL', 'VIDRIO', 'joel.vidrio@ues.mx')

# Creamos la variable cursor y utilizaremos el método execute()
# Le pasaremos como parámetros la consulta SQL y los valores
cursor.execute(sql, valores)

# Guardamos la información en la base de datos
# Utilizaremos el objeto de conexión invocando el método commit()
conexion.commit()

# Recuperar los registros que se han ingresado en la base de datos
registros_insertados = cursor.rowcount
print(f'Registro insertado: {registros_insertados}')

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
