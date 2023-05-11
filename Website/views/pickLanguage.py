# views/pickLanguage.py
from flask import Blueprint, render_template

pickLanguage_bp = Blueprint("pickLanguage", __name__)


@pickLanguage_bp.route("/pickLanguage")
def pickLanguage():
    """
    Render the pickLanguage.html template when the route is accessed.
    """
    return render_template("pickLanguage.html")
