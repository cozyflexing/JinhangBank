# views/amountUnavailable.py
from flask import Blueprint, render_template

amountUnavailable_bp = Blueprint("amountUnavailable", __name__)


@amountUnavailable_bp.route("/amountUnavailable")
def amountUnavailable():
    """
    Render the amountUnavailable.html template when the route is accessed.
    """
    return render_template("amountUnavailable.html")
