import pymysql
import os
import urllib.parse

def get_db_connection():
    db_url = os.getenv("DATABASE_URL")
    if db_url is None:
        raise Exception("DATABASE_URL não encontrada")

    parsed_url = urllib.parse.urlparse(db_url)

    conn = pymysql.connect(
        host=parsed_url.hostname,
        user=parsed_url.username,
        password=parsed_url.password,
        db=parsed_url.path.lstrip('/'),  # remove a primeira "/" do nome do banco
        port=parsed_url.port,
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
