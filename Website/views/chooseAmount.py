# views/chooseAmount.py
from flask import Blueprint, render_template

chooseAmount_bp = Blueprint("chooseAmount", __name__)


@chooseAmount_bp.route("/chooseAmount/<int:bankpas_id>", methods=["GET", "POST"])
def chooseAmount(bankpas_id):
    """
    Render the chooseAmount.html template with the provided bankpas_id when the route is accessed.
    """
    return render_template("chooseAmount.html", bankpas_id=bankpas_id)
