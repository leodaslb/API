import pymysql
import os

def get_db_connection():
    # Acessando as variáveis de ambiente corretamente
    host = os.getenv("MYSQL_HOST")  
    user = os.getenv("MYSQL_USER")  
    password = os.getenv("MYSQL_PASSWORD")  
    db = os.getenv("MYSQL_DATABASE")  
    port = int(os.getenv("MYSQL_PORT", 3306)) 

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
