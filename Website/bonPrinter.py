import serial
import time
from models import Bankpassen, Klanten, Transacties, Rekeningen
from datetime import datetime


def generate_receipt():
    # Build the receipt text
    receipt_text = "-------------------------------\n"
    receipt_text += "ATM Withdrawal Receipt\n"
    receipt_text += "-------------------------------\n"
    receipt_text += "Customer: John Doe\n"
    receipt_text += "Card Number: 123456789\n"
    receipt_text += "Account Number: 987654321\n"
    receipt_text += "-------------------------------\n"
    receipt_text += "Date: 2023-05-31\n"
    receipt_text += "Time: 12:34:56\n"
    receipt_text += "Location: ATM Location\n"
    receipt_text += "Transaction Type: Withdrawal\n"
    receipt_text += "Withdrawal Amount: 100\n"
    receipt_text += "-------------------------------\n"
    receipt_text += "Remaining Balance: 900\n"
    receipt_text += "-------------------------------\n"
    receipt_text += "Thank you for using our services.\n"
    receipt_text += "-------------------------------\n"

    return receipt_text


# Replace '/dev/serial0' with the port that your Adafruit printer is connected to
ser = serial.Serial("/dev/serial0", 19200, timeout=1)

# Wake the printer
ser.write(bytearray([0x1B, 0x40]))

time.sleep(0.5)

# Write "Hello, world!" to the printer
ser.write(generate_receipt.encode())

# Feed three lines to give some space
ser.write(bytearray([0x1B, 0x64, 0x03]))

ser.close()
Traceback (most recent call last):
  File "/home/pi/Desktop/JinhangBank/Website/bonPrinter.py", line 39, in <module>
    ser.write(generate_receipt.encode())
AttributeError: 'function' object has no attribute 'encode'