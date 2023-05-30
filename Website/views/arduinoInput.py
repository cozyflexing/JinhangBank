# views/arduinoInput.py
import serial
from flask import Blueprint, jsonify

arduinoInput_bp = Blueprint("arduinoInput", __name__)

arduino_mega = serial.Serial("/dev/ttyACM0", 9600)  # Update with your Uno's device name


@arduinoInput_bp.route("/arduinoInput")
def arduinoInput():
    if arduino_mega.in_waiting > 0:
        line = arduino_mega.readline().decode("utf-8").rstrip()
        return jsonify(button_pressed=line)
    else:
        return jsonify(button_pressed=None)
