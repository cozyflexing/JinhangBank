# views/amountUnavailable.py
from flask import Blueprint, render_template

amountUnavailable_bp = Blueprint("amountUnavailable", __name__)


@amountUnavailable_bp.route("/amountUnavailable")
def amountUnavailable():
    return render_template("amountUnavailable.html")
