# views/takeReceipt.py
from flask import Blueprint, render_template

takeReceipt_bp = Blueprint("takeReceipt", __name__)


@takeReceipt_bp.route("/takeReceipt/<int:bankpas_id>")
def takeReceipt(bankpas_id):
    """
    Render the takeReceipt.html template when the route is accessed.
    """
    return render_template("takeReceipt.html", bankpas_id=bankpas_id)
