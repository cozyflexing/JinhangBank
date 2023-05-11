# views/verifyPinCode.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector

verifyPinCode_bp = Blueprint("verifyPinCode", __name__)


def connect_to_db():
    """
    Establish a connection to the database.
    """
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",
        database="JinhangBank",
    )


@verifyPinCode_bp.route("/enterPin/<int:bankpas_id>", methods=["GET", "POST"])
def enter_pin(bankpas_id):
    """
    Verify the pin_code and redirect to the appropriate route based on the verification result.
    """
    if request.method == "POST":
        pin_code = request.form["pin_code"]
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM bankpassen WHERE bankpas_id = %s",
            (bankpas_id,),
        )
        result = cursor.fetchone()
        pinCode = result[2]
        incorrect_attempts = result[3]

        if pin_code == pinCode:
            cursor.close()
            connection.close()
            return redirect(url_for("makeChoice.makeChoice", bankpas_id=result[0]))
        else:
            incorrect_attempts += 1
            cursor.execute(
                "UPDATE bankpassen SET is_locked = %s WHERE bankpas_id = %s",
                (incorrect_attempts, bankpas_id),
            )
            connection.commit()
            cursor.close()
            connection.close()
            if incorrect_attempts != 3:
                flash(f"{3 - incorrect_attempts} tries remaining.")
            else:
                return redirect(url_for("blocked.blocked"))
    return render_template("enterPin.html", bankpas_id=bankpas_id)
