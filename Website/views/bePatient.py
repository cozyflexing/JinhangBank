# views/bePatient.py
from flask import Blueprint, render_template, request
from models import Bankpassen, Rekeningen, Biljetten
from db import db
import serial

# Start serial communication
ser = serial.Serial("/dev/serial0", 9600)  # check your COM port and baud rate


bePatient_bp = Blueprint("bePatient", __name__)


@bePatient_bp.route("/bepatientamount/<int:bankpas_id>", methods=["GET", "POST"])
def bePatientAmount(bankpas_id):
    if request.method == "POST":
        if request.form["amount"] != "":
            totalFifty = Biljetten.query.get(50).hoeveelheid
            fifty = Biljetten.query.get(50)
            totalTwenty = Biljetten.query.get(20).hoeveelheid
            twenty = Biljetten.query.get(20)
            totalTen = Biljetten.query.get(10).hoeveelheid
            ten = Biljetten.query.get(10)
            bills = []
            amount_to_withdraw = int(request.form["amount"])
            if amount_to_withdraw % 10 != 0:
                print("Pin more money")
            else:
                while amount_to_withdraw != 0:
                    if amount_to_withdraw > Biljetten.total_value():
                        print("Pick a lesser amount")
                        break
                    else:
                        if (
                            amount_to_withdraw >= 50
                            and Biljetten.query.get(50).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 50
                            fifty.hoeveelheid = totalFifty - 1
                            bills.append(50)
                        elif (
                            amount_to_withdraw >= 20
                            and Biljetten.query.get(20).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 20
                            twenty.hoeveelheid = totalTwenty - 1
                            bills.append(20)
                        elif (
                            amount_to_withdraw >= 10
                            and Biljetten.query.get(10).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 10
                            ten.hoeveelheid = totalTen - 1
                            bills.append(10)
            ser.write(str(bills).encode())
            ser.close()
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
        totalFifty = Biljetten.query.get(50).hoeveelheid
        fifty = Biljetten.query.get(50)
        totalTwenty = Biljetten.query.get(20).hoeveelheid
        twenty = Biljetten.query.get(20)
        totalTen = Biljetten.query.get(10).hoeveelheid
        ten = Biljetten.query.get(10)
        bills = []
        if request.form["other_amount"] != "":
            amount_to_withdraw = int(request.form["other_amount"])
            if amount_to_withdraw % 10 != 0:
                print("Pin more money")
            else:
                while amount_to_withdraw != 0:
                    if amount_to_withdraw > Biljetten.total_value():
                        print("Pick a lesser amount")
                        break
                    else:
                        if (
                            amount_to_withdraw >= 50
                            and Biljetten.query.get(50).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 50
                            fifty.hoeveelheid = totalFifty - 1
                            bills.append(50)
                        elif (
                            amount_to_withdraw >= 20
                            and Biljetten.query.get(20).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 20
                            twenty.hoeveelheid = totalTwenty - 1
                            bills.append(20)
                        elif (
                            amount_to_withdraw >= 10
                            and Biljetten.query.get(10).hoeveelheid > 0
                        ):
                            amount_to_withdraw -= 10
                            ten.hoeveelheid = totalTen - 1
                            bills.append(10)
            ser.write(str(bills).encode())
            ser.close()
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
