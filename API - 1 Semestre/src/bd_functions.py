import pymysql
import os

def get_db_connection():
    # Definindo as variáveis diretamente no código para testar a conexão
    host = "mysql.railway.internal"  # Host do banco de dados fornecido pelo Railway
    user = "root"  # Usuário do banco de dados
    password = "yxMUYClFgePIrjDDIqNFIetjSuPBAwmc"  # Senha do banco de dados
    db = "railway"  # Nome do banco de dados
    port = 3306  # Porta do banco de dados, geralmente 3306 para MySQL

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
