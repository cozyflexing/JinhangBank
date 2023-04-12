# views/makeChoice.py
from flask import Blueprint, render_template

makeChoice_bp = Blueprint("makeChoice", __name__)


@makeChoice_bp.route("/makeChoice")
def makeChoice():
    return render_template("makeChoice.html")
