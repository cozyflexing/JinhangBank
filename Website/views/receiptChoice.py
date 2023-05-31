# views/receiptChoice.py
from flask import Blueprint, render_template

receiptChoice_bp = Blueprint("receiptChoice", __name__)


@receiptChoice_bp.route("/receiptChoice/<int:bankpas_id>")
def receiptChoice(bankpas_id):
    """
    Render the receiptChoice.html template when the route is accessed.
    """
    return render_template("receiptChoice.html", bankpas_id=bankpas_id)
