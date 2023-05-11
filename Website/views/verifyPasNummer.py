# views/verifyPasNummer.py
from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

verifyPasNummer_bp = Blueprint("verifyPasNummer", __name__)


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",
        database="JinhangBank",
    )


@verifyPasNummer_bp.route("/verifyPasNummer", methods=["GET", "POST"])
def verifyPasNummer():
    if request.method == "POST":
        pas_nummer = request.form["pas_nummer"]
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bankpassen WHERE pas_nummer = %s", (pas_nummer,))
        result = cursor.fetchone()
        if result[3] == 3:
            return redirect(url_for("blocked.blocked"))
        cursor.close()
        connection.close()
        if result:
            return redirect(url_for("enterPin.enterPin", bankpas_id=result[0]))
        else:
            return "THIS CARD DOES NOT EXIST"
    return render_template("scanCard.html")
