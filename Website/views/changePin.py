# views/changePin.py
from flask import Blueprint, render_template

changePin_bp = Blueprint("changePin", __name__)


@changePin_bp.route("/changePin")
def changePin():

    return render_template("changePin.html")
