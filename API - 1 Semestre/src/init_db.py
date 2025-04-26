import pymysql
import os

def init_db():
    try:
        # Conexão com o banco de dados
        conn = pymysql.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            password=os.getenv("MYSQLPASSWORD"),
            db=os.getenv("MYSQLDATABASE"),
            port=int(os.getenv("MYSQLPORT"))
        )

        with conn.cursor() as cursor:
            # Lê o arquivo SQL
            with open("ranking_municipios.sql", "r", encoding="utf-8") as f:
                sql = f.read()

                # Executa cada comando SQL no arquivo, tratando possíveis erros
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:  # Se o comando não estiver vazio
                        try:
                            cursor.execute(statement)  # Executa a query
                        except pymysql.MySQLError as e:
                            print(f"Erro ao executar a query: {statement}")
                            print(f"Erro: {e}")
                            continue

        # Commit e fechamento
        conn.commit()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conn:
            conn.close()  # Garantir que a conexão será fechada

if __name__ == "__main__":
    init_db()
