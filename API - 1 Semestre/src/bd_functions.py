import pymysql
import os

def get_db_connection():
    
    host = "mysql-epnp.railway.internal"  
    user = "root" 
    password = "StICbNaYmEOiCZYCKlqOvnhgzJzcMSBQ"  
    db = "railway"  
    port = 3306 

    print(f"Conectando ao banco de dados: {host}, na porta {port}")

    # Conectando ao banco de dados
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db,
        port=port
    )
    return conn

def executar_consulta(query, params=None, dict_cursor=True):
    conn = get_db_connection()
    cursor_class = pymysql.cursors.DictCursor if dict_cursor else None
    cursor = conn.cursor(cursor_class) if cursor_class else conn.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        resultado = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return resultado
