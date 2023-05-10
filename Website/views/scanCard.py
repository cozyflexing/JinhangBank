# views/scanCard.py
from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

scanCard_bp = Blueprint("scanCard", __name__)


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",  # Replace with your own password
        database="JinhangBank",
    )


@scanCard_bp.route("/", methods=["POST", "GET"])
def scanCard():
    if request.method == "POST":
        pas_nummer = request.form["usernameForm"]
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bankpassen WHERE pas_nummer = %s", (pas_nummer,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return redirect(url_for("enterPin", bankpas_id=result[0]))
        else:
            return render_template("scanCard.html")
    else:
        return render_template("scanCard.html")
