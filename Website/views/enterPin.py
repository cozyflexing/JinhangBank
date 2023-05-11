# views/enterPin.py
from flask import Blueprint, render_template, request

enterPin_bp = Blueprint("enterPin", __name__)


@enterPin_bp.route("/enterPin")
def enterPin():
    """
    Render the enterPin.html template with the provided bankpas_id or redirect to scanCard.html if bankpas_id is not provided.
    """
    bankpas_id = request.args.get("bankpas_id", None)

    if bankpas_id is None:
        return render_template("scanCard.html")

    return render_template("enterPin.html", bankpas_id=bankpas_id)
