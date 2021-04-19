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
sql = 'SELECT * FROM persona WHERE id_persona IN %s'

# Declaramos una variable, utilizando la función INPUT
entrada = input("Proporciona las claves que deseas consultar (Separarlos por comas): ")
tupla = tuple(entrada.split(','))

# Creamos una tupla asignando la variable
llaves_primarias = (tupla,)

# Utilizar como parámetros la sentencia SQL y la tupla
cursor.execute(sql, llaves_primarias)

# Recuperar los registros
registros = cursor.fetchall()

# Utilizando el método Print, agregaremos un for
for registro in registros:
  print(registro)

# Cerrar las conexiones: cursor, conexión
cursor.close()
conexion.close()
