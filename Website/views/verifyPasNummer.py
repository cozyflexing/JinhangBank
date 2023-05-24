# views/verifyPasNummer.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import Bankpassen
from db import db

verifyPasNummer_bp = Blueprint("verifyPasNummer", __name__)


@verifyPasNummer_bp.route("/verifyPasNummer", methods=["GET", "POST"])
def verifyPasNummer():
    """
    Verify the pas_nummer and redirect to the appropriate route based on the verification result.
    """
    if request.method == "POST":
        pas_nummer = request.form["pas_nummer"]
        bankpas = Bankpassen.query.filter_by(pas_nummer=pas_nummer).first()

        if bankpas:
            if bankpas.is_locked == 3:
                return redirect(url_for("blocked.blocked"))
            else:
                return redirect(
                    url_for("enterPin.enterPin", bankpas_id=bankpas.bankpas_id)
                )
        else:
            return "THIS CARD DOES NOT EXIST"
    return render_template("scanCard.html")
