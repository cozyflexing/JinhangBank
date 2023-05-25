# views/RFID.py
from flask import Blueprint, render_template
from Read import readRFID

RFID_bp = Blueprint("RFID", __name__)


@RFID_bp.route("/rfid")
def scanRfid():
    card = ""
    while card == "":
        card = readRFID()
    return render_template("enterPin.html")
