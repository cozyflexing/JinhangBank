# views/verifyPasNummer.py
import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",
        database="JinhangBank",
    )


id = 1
connection = connect_to_db()
cursor = connection.cursor()
cursor.execute(f"SELECT * FROM bankpassen WHERE bankpas_id = {id}")
result = cursor.fetchone()
print(result)
cursor.close()
connection.close()
