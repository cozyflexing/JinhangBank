# views/scanCard.py
from flask import Blueprint, render_template, session
import Read
from threading import Thread


scanCard_bp = Blueprint("scanCard", __name__)


def runThreadedScript():
    session["cardNumber"] = Read.readRFID()


thread = Thread(target=runThreadedScript)
thread.start()


@scanCard_bp.route("/")
def scanCard():
    """
    Render the scanCard.html template when the route is accessed.
    """
    if session.get("cardNumber"):
        return render_template("enterPin.html")
    else:
        return render_template("scanCard.html")
