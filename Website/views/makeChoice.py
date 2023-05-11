# views/makeChoice.py
from flask import Blueprint, render_template

makeChoice_bp = Blueprint("makeChoice", __name__)


@makeChoice_bp.route("/makeChoice/<int:bankpas_id>")
def makeChoice(bankpas_id):
    """
    Render the makeChoice.html template with the provided bankpas_id when the route is accessed.
    """
    return render_template("makeChoice.html", bankpas_id=bankpas_id)
