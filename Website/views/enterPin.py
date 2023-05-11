# views/enterPin.py
from flask import Blueprint, render_template, request

enterPin_bp = Blueprint("enterPin", __name__)


@enterPin_bp.route("/enterPin")
def enterPin():
    bankpas_id = request.args.get("bankpas_id", None)
    if bankpas_id is None:
        return render_template("scanCard.html")
    return render_template("enterPin.html", bankpas_id=bankpas_id)
