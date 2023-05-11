# views/changePin.py
from flask import Blueprint, render_template

changePin_bp = Blueprint("changePin", __name__)


@changePin_bp.route("/changePin/<int:bankpas_id>")
def changePin(bankpas_id):
    """
    Render the changePin.html template with the provided bankpas_id when the route is accessed.
    """
    return render_template("changePin.html", bankpas_id=bankpas_id)
