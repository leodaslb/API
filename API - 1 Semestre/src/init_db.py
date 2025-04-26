import pymysql
import os

def init_db():
    conn = pymysql.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        db=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT"))
    )

    with conn.cursor() as cursor:
        with open("ranking_municipios.sql", "r") as f:
            sql = f.read()
            for statement in sql.split(";"):
                if statement.strip():
                    cursor.execute(statement)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
