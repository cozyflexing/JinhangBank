# views/blocked.py
from flask import Blueprint, render_template

blocked_bp = Blueprint("blocked", __name__)


@blocked_bp.route("/blocked/<int:bankpas_id>")
def blocked(bankpas_id):
    """
    Render the blocked.html template when the route is accessed.
    """
    return render_template("blocked.html", bankpas_id=bankpas_id)
