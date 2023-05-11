# views/enterAmount.py
from flask import Blueprint, render_template

enterAmount_bp = Blueprint("enterAmount", __name__)


@enterAmount_bp.route("/enterAmount")
def enterAmount():
    """
    Render the enterAmount.html template when the route is accessed.
    """
    return render_template("enterAmount.html")
