# views/scanCard.py
from flask import Blueprint, render_template

scanCard_bp = Blueprint("scanCard", __name__)


@scanCard_bp.route("/")
def scanCard():
    return render_template("scanCard.html")
