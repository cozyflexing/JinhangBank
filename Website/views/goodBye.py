# views/goodBye.py
from flask import Blueprint, render_template

goodBye_bp = Blueprint("goodBye", __name__)


@goodBye_bp.route("/goodBye")
def goodBye():
    """
    Render the goodBye.html template when the route is accessed.
    """
    return render_template("goodBye.html")
