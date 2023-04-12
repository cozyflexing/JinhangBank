# views/chooseAmount.py
from flask import Blueprint, render_template

chooseAmount_bp = Blueprint("chooseAmount", __name__)


@chooseAmount_bp.route("/chooseAmount")
def chooseAmount():
    return render_template("chooseAmount.html")
