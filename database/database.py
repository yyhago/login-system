import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conexaoBanco = psycopg2.connect(
    database= os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

cursorSQL= conexaoBanco.cursor()

cursorSQL.execute("SELECT * FROM users")
resultadoSQL = cursorSQL.fetchall()

for x in resultadoSQL:
    print(x)

conexaoBanco.close()
cursorSQL.close()