# views/takeReceipt.py
from flask import Blueprint, render_template

takeReceipt_bp = Blueprint("takeReceipt", __name__)


@takeReceipt_bp.route("/takeReceipt")
def takeReceipt():
    """
    Render the takeReceipt.html template when the route is accessed.
    """
    return render_template("takeReceipt.html")
