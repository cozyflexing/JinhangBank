# views/verifyPasNummer.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import Bankpassen
from db import db
from apiPost import post_balance

verifyPasNummer_bp = Blueprint("verifyPasNummer", __name__)


@verifyPasNummer_bp.route("/verifyPasNummer", methods=["GET"])
def verifyPasNummer():
    """
    Verify the pas_nummer and redirect to the appropriate route based on the verification result.
    """
    pas_nummer = request.args.get("pas_nummer")

    # If the pas_nummer doesn't start with 'CHJNHB', return a suitable response
    if not pas_nummer.startswith("CHJNHB"):
        return render_template(
            url_for("enterPin.enterPinOutside", bankpas_id=pas_nummer)
        )

    bankpas = Bankpassen.query.filter_by(rekening_nummer=pas_nummer).first()

    if bankpas:
        if bankpas.is_locked == 3:
            return redirect(url_for("blocked.blocked", bankpas_id=bankpas.bankpas_id))
        else:
            return redirect(url_for("enterPin.enterPin", bankpas_id=bankpas.bankpas_id))
    else:
        return "THIS CARD DOES NOT EXIST"
