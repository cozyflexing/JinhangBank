# views/takeMoney.py
from flask import Blueprint, render_template

takeMoney_bp = Blueprint("takeMoney", __name__)


@takeMoney_bp.route("/takeMoney")
def takeMoney():
    """
    Render the takeMoney.html template when the route is accessed.
    """
    return render_template("takeMoney.html")
