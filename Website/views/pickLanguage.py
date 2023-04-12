# views/pickLanguage.py
from flask import Blueprint, render_template

pickLanguage_bp = Blueprint("pickLanguage", __name__)


@pickLanguage_bp.route("/pickLanguage")
def pickLanguage():
    return render_template("pickLanguage.html")
