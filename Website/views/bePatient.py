# views/bePatient.py
from flask import Blueprint, render_template, request
from models import Bankpassen, Rekeningen
from db import db

bePatient_bp = Blueprint("bePatient", __name__)


@bePatient_bp.route("/bepatientamount/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientAmount(bankpas_id):
    if request.method == "POST":
        if request.form["amount"] != "":
            amount_to_withdraw = int(request.form["amount"])

            bankpas = Bankpassen.query.get(bankpas_id)
            if not bankpas:
                return "Bankpassen not found"

            rekening_nummer = bankpas.rekening_nummer

            rekening = Rekeningen.query.get(rekening_nummer)
            if not rekening:
                return "Rekeningen not found"

            current_balance = rekening.balans

            if current_balance < amount_to_withdraw:
                return "INSUFFICIENT FUNDS"

            new_balance = current_balance - amount_to_withdraw
            rekening.balans = new_balance
            db.session.commit()

            return render_template("bePatient.html", bankpas_id=bankpas_id)

    return render_template("goodBye.html")


@bePatient_bp.route("/bepatientotheramount/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientOtherAmount(bankpas_id):
    if request.method == "POST":
        if request.form["other_amount"] != "":
            amount_to_withdraw = int(request.form["other_amount"])

            # Retrieve the account number associated with the bankpas_id
            bankpas = Bankpassen.query.get(bankpas_id)
            if bankpas is None:
                return "INVALID BANKPAS ID"

            rekening_nummer = bankpas.rekening_nummer

            # Retrieve the current balance of the account
            rekening = Rekeningen.query.get(rekening_nummer)
            if rekening is None:
                return "INVALID REKENING NUMMER"

            current_balance = rekening.balans

            if current_balance < amount_to_withdraw:
                # If the current balance is less than the amount to withdraw, return "INSUFFICIENT FUNDS"
                return "INSUFFICIENT FUNDS"

            new_balance = current_balance - amount_to_withdraw

            # Update the balance of the account after withdrawal
            rekening.balans = new_balance
            db.session.commit()

            return render_template("bePatient.html", bankpas_id=bankpas_id)
        else:
            pass

        return render_template("goodBye.html")


@bePatient_bp.route("/bepatientnewpin/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientNewPin(bankpas_id):
    if request.method == "POST":
        if request.form["new_pin"] != "":
            newPin = request.form["new_pin"]
            bankpas = Bankpassen.query.get(bankpas_id)
            if not bankpas:
                return "Bankpassen not found"

            bankpas.pin_code = newPin
            db.session.commit()

            return render_template("goodBye.html", bankpas_id=bankpas_id)

    return render_template("goodBye.html")
