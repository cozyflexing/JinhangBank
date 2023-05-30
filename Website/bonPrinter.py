import serial
import time
from models import Bankpassen, Klanten, Transacties, Rekeningen
from datetime import datetime


def generate_receipt(bankpas_id, transactie_id):
    # Fetch the necessary data
    bankpas = Bankpassen.query.get(bankpas_id)
    klant = Klanten.query.get(bankpas.klant_id)
    transactie = Transacties.query.get(transactie_id)
    rekening = Rekeningen.query.filter_by(
        rekening_nummer=transactie.rekening_nummer
    ).first()

    # Build the receipt text
    receipt_text = f"-------------------------------\n"
    receipt_text += f"ATM Withdrawal Receipt\n"
    receipt_text += f"-------------------------------\n"
    receipt_text += f"Customer: {klant.voornaam} {klant.tussenvoegsel if klant.tussenvoegsel else ''} {klant.achternaam}\n"
    receipt_text += f"Card Number: {bankpas.pas_nummer}\n"
    receipt_text += f"Account Number: {rekening.rekening_nummer}\n"
    receipt_text += f"-------------------------------\n"
    receipt_text += f"Date: {transactie.datum.strftime('%Y-%m-%d')}\n"
    receipt_text += f"Time: {transactie.tijd.strftime('%H:%M:%S')}\n"
    receipt_text += f"Location: {transactie.locatie}\n"
    receipt_text += f"Transaction Type: {transactie.type}\n"
    receipt_text += f"Withdrawal Amount: {transactie.hoeveelheid}\n"
    receipt_text += f"-------------------------------\n"
    receipt_text += f"Remaining Balance: {rekening.balans}\n"
    receipt_text += f"-------------------------------\n"
    receipt_text += f"Thank you for using our services.\n"
    receipt_text += f"-------------------------------\n"

    return receipt_text


# Replace '/dev/serial0' with the port that your Adafruit printer is connected to
ser = serial.Serial("/dev/serial0", 19200, timeout=1)

# Wake the printer
ser.write(bytearray([0x1B, 0x40]))

time.sleep(0.5)

# Write "Hello, world!" to the printer
ser.write(b"Hello, world!\n")

# Feed three lines to give some space
ser.write(bytearray([0x1B, 0x64, 0x03]))

ser.close()
