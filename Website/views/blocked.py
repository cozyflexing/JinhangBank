# views/blocked.py
from flask import Blueprint, render_template

blocked_bp = Blueprint("blocked", __name__)


@blocked_bp.route("/blocked")
def blocked():
    """
    Render the blocked.html template when the route is accessed.
    """
    return render_template("blocked.html")
