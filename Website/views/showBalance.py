# views/showBalance.py
from flask import Blueprint, render_template
import mysql.connector

showBalance_bp = Blueprint("showBalance", __name__)


def connect_to_db():
    # Function to establish a connection to the database
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",
        database="JinhangBank",
    )


@showBalance_bp.route("/showBalance/<int:bankpas_id>")
def showBalance(bankpas_id):
    """
    Retrieve the balance of the account associated with the bankpas_id and render the showBalance.html template.
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT rekening_nummer FROM bankpassen WHERE bankpas_id = %s",
        (bankpas_id,),
    )
    (rekening_nummer,) = cursor.fetchone()
    cursor.execute(
        "SELECT balans FROM rekeningen WHERE rekening_nummer = %s", (rekening_nummer,)
    )
    (balans,) = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template("showBalance.html", balans=balans)
