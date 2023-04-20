from fastapi import FastAPI
import mariadb

app = FastAPI()

config = {
    "host": "localhost",
    "port": 3306,
    "user": "Admin",
    "password": "VoEj6SiLgUWIVkV*U5yLY*0bm7Ie50kL",
    "database": "JinhangBankAPI",
}


@app.get("/api/data")
async def get_data():
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM adressen")
        resultAdressen = cursor.fetchall()
        cursor.execute("SELECT * FROM klanten")
        resultKlanten = cursor.fetchall()
        cursor.execute("SELECT * FROM bankpassen")
        resultBankpassen = cursor.fetchall()
        cursor.execute("SELECT * FROM rekeningen")
        resultRekeningen = cursor.fetchall()
        cursor.execute("SELECT * FROM transacties")
        resultTransacties = cursor.fetchall()
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        if conn:
            conn.close()
    return {
        "adressen": resultAdressen,
        "klanten": resultKlanten,
        "bankpassen": resultBankpassen,
        "rekeningen": resultRekeningen,
        "transacties": resultTransacties,
    }
