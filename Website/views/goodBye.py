# views/goodBye.py
from flask import Blueprint, render_template

goodBye_bp = Blueprint("goodBye", __name__)


@goodBye_bp.route("/goodBye")
def goodBye():
    return render_template("goodBye.html")
