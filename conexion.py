
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'beca1092'
DB_NAME = 'biblioteca'
DB_PORT = 3306

def run_query(query = ''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    # Conectarse a la base de datos
    conn = MySQLdb.Connect(*datos)
    # conn = pymysql.connect(datos)
    cursor = conn.cursor() # Crear un cursor
    cursor.execute(query) # Ejecutar la consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchAll() # Traemos los resultados
    else:
        conn.commit()
        data = None
    
    # Cerrarmos la conexión
    cursor.close()
    conn.close()

    return data

# Llamamos a la función query
print(run_query('SHOW tables'))


def insert_autores (nombre, apellido):
    statement = "INSERT INTO autor (nombre, apellido) VALUES( '"+ nombre + "','" + apellido+"')"
    print('insert ok',run_query(statement))

# Insertar un autor en la BD
insert_autores(nombre="Jorge", apellido="Chavez")