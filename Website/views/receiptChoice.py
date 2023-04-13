# views/receiptChoice.py
from flask import Blueprint, render_template

receiptChoice_bp = Blueprint("receiptChoice", __name__)


@receiptChoice_bp.route("/receiptChoice")
def receiptChoice():
    return render_template("receiptChoice.html")
