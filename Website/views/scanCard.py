# views/scanCard.py
from flask import Blueprint, render_template
from Read import readRFID

scanCard_bp = Blueprint("scanCard", __name__)


@scanCard_bp.route("/")
def scanCard():
    """
    Render the scanCard.html template when the route is accessed.
    """
    return render_template("scanCard.html")
