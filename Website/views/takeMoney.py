# views/takeMoney.py
from flask import Blueprint, render_template

takeMoney_bp = Blueprint("takeMoney", __name__)


@takeMoney_bp.route("/takeMoney")
def takeMoney():
    return render_template("takeMoney.html")
