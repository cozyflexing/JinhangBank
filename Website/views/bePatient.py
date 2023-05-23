# views/bePatient.py
from flask import Blueprint, render_template, request
import mysql.connector

bePatient_bp = Blueprint("bePatient", __name__)


def connect_to_db():
    # Function to establish a connection to the database
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",
        database="JinhangBank",
    )


@bePatient_bp.route("/bepatientamount/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientAmount(bankpas_id):
    if request.method == "POST":
        # If the request method is POST
        connection = connect_to_db()
        cursor = connection.cursor()

        if request.form["amount"] != "":
            amount_to_withdraw = int(request.form["amount"])

            # Retrieve the account number associated with the bankpas_id
            cursor.execute(
                "SELECT rekening_nummer FROM bankpassen WHERE bankpas_id = %s",
                (bankpas_id,),
            )
            (rekening_nummer,) = cursor.fetchone()

            # Retrieve the current balance of the account
            cursor.execute(
                "SELECT balans FROM rekeningen WHERE rekening_nummer = %s",
                (rekening_nummer,),
            )
            (current_balance,) = cursor.fetchone()

            if current_balance < amount_to_withdraw:
                # If the current balance is less than the amount to withdraw, return "INSUFFICIENT FUNDS"
                cursor.close()
                connection.close()
                return "INSUFFICIENT FUNDS"

            new_balance = current_balance - amount_to_withdraw

            # Update the balance of the account after withdrawal
            cursor.execute(
                "UPDATE rekeningen SET balans = %s WHERE rekening_nummer = %s",
                (new_balance, rekening_nummer),
            )
            connection.commit()
            cursor.close()
            connection.close()

            return render_template("bePatient.html", bankpas_id=bankpas_id)
        else:
            pass
        connection.commit()
        cursor.close()
        connection.close()

        return render_template("goodBye.html")


@bePatient_bp.route("/bepatientotheramount/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientOtherAmount(bankpas_id):
    if request.method == "POST":
        # If the request method is POST
        connection = connect_to_db()
        cursor = connection.cursor()

        if request.form["other_amount"] != "":
            amount_to_withdraw = int(request.form["other_amount"])
            # Retrieve the account number associated with the bankpas_id
            cursor.execute(
                "SELECT rekening_nummer FROM bankpassen WHERE bankpas_id = %s",
                (bankpas_id,),
            )
            (rekening_nummer,) = cursor.fetchone()

            # Retrieve the current balance of the account
            cursor.execute(
                "SELECT balans FROM rekeningen WHERE rekening_nummer = %s",
                (rekening_nummer,),
            )
            (current_balance,) = cursor.fetchone()

            if current_balance < amount_to_withdraw:
                # If the current balance is less than the amount to withdraw, return "INSUFFICIENT FUNDS"
                cursor.close()
                connection.close()
                return "INSUFFICIENT FUNDS"

            new_balance = current_balance - amount_to_withdraw

            # Update the balance of the account after withdrawal
            cursor.execute(
                "UPDATE rekeningen SET balans = %s WHERE rekening_nummer = %s",
                (new_balance, rekening_nummer),
            )
            connection.commit()
            cursor.close()
            connection.close()

            return render_template("bePatient.html", bankpas_id=bankpas_id)
        else:
            pass
        connection.commit()
        cursor.close()
        connection.close()

        return render_template("goodBye.html")


@bePatient_bp.route("/bepatientnewpin/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientNewPin(bankpas_id):
    if request.method == "POST":
        connection = connect_to_db()
        cursor = connection.cursor()
        if request.form["new_pin"] != "":
            newPin = request.form["new_pin"]
            cursor.execute(
                "UPDATE bankpassen SET pin_code = %s WHERE bankpas_id = %s",
                (newPin, bankpas_id),
            )
            connection.commit()
            cursor.close()
            connection.close()
            return render_template("goodBye.html", bankpas_id=bankpas_id)
        else:
            pass
        connection.commit()
        cursor.close()
        connection.close()

        return render_template("goodBye.html")
