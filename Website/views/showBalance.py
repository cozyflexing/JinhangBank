# views/showBalance.py
from flask import Blueprint, render_template

showBalance_bp = Blueprint("showBalance", __name__)


@showBalance_bp.route("/showBalance")
def showBalance():
    return render_template("showBalance.html")
