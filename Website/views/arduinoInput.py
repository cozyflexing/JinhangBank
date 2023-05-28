# views/arduinoInput.py
import serial
from flask import Blueprint, jsonify

arduinoInput_bp = Blueprint("arduinoInput", __name__)

ser = serial.Serial("/dev/serial0", 9600)


@arduinoInput_bp.route("/arduinoInput")
def arduinoInput():
    if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").rstrip()
        return jsonify(button_pressed=line)
    else:
        return jsonify(button_pressed=None)
