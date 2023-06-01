# views/bePatientReceipt.py
from flask import Blueprint, render_template
from models import Transacties, Bankpassen
from sqlalchemy import desc
import serial
import time

bePatientReceipt_bp = Blueprint("bePatientReceipt", __name__)


def generate_receipt(transaction, account):
    # Build the receipt text
    receipt_text = "-------------------------------\n"
    receipt_text += "JinhangBank Withdrawal Receipt\n"
    receipt_text += "-------------------------------\n"
    receipt_text += f"Date: {transaction.datum}\n"
    receipt_text += f"Time: {transaction.tijd}\n"
    receipt_text += f"Location: {transaction.locatie}\n"
    receipt_text += f"Transaction Type: {transaction.type}\n"
    receipt_text += f"Withdrawal Amount: {transaction.hoeveelheid}\n"
    receipt_text += f"Account Number: {account.rekening_nummer}\n"
    receipt_text += "-------------------------------\n"
    receipt_text += "Thank you for using our services.\n"
    receipt_text += "-------------------------------\n"

    return receipt_text


@bePatientReceipt_bp.route("/bePatientReceipt/<int:bankpas_id>")
def bePatientReceipt(bankpas_id):
    """
    Render the bePatientReceipt.html template when the route is accessed.
    """
    most_recent_transaction = Transacties.query.filter(
        Transacties.bankpas_id == bankpas_id
    ).last()
    account = Bankpassen.query.get(bankpas_id)
    # Print the receipt with the most recent transaction details
    receipt_text = generate_receipt(most_recent_transaction, account)

    ser = serial.Serial("/dev/serial0", 19200, timeout=1)  # initialize the printer
    ser.write(bytearray([0x1B, 0x40]))  # Wake the printer
    time.sleep(0.5)
    ser.write(receipt_text.encode())  # Print the receipt
    ser.write(bytearray([0x1B, 0x64, 0x03]))  # Feed three lines
    ser.close()  # Close the printer connection

    return render_template("bePatientReceipt.html", bankpas_id=bankpas_id)
