# views/verifyPinCode.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Bankpassen
from db import db

verifyPinCode_bp = Blueprint("verifyPinCode", __name__)


@verifyPinCode_bp.route("/enterPin/<int:bankpas_id>", methods=["GET", "POST"])
def enter_pin(bankpas_id):
    """
    Verify the pin_code and redirect to the appropriate route based on the verification result.
    """
    if request.method == "POST":
        pin_code = request.form["pin_code"]
        bankpas = Bankpassen.query.get(bankpas_id)
        if pin_code == bankpas.pin_code:
            return redirect(
                url_for("makeChoice.makeChoice", bankpas_id=bankpas.bankpas_id)
            )
        else:
            bankpas.is_locked += 1
            db.session.commit()
            if bankpas.is_locked != 3:
                flash(f"{3 - bankpas.is_locked} tries remaining.")
            else:
                return redirect(url_for("blocked.blocked"))
    return render_template("enterPin.html", bankpas_id=bankpas_id)
