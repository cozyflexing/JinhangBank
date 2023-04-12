# views/enterPin.py
from flask import Blueprint, render_template

enterPin_bp = Blueprint("enterPin", __name__)


@enterPin_bp.route("/enterPin")
def enterPin():
    return render_template("enterPin.html")
