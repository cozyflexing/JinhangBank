# views/showBalance.py
from flask import Blueprint, render_template
from models import Bankpassen, Rekeningen

showBalance_bp = Blueprint("showBalance", __name__)


@showBalance_bp.route("/showBalance/<int:bankpas_id>")
def showBalance(bankpas_id):
    """
    Retrieve the balance of the account associated with the bankpas_id and render the showBalance.html template.
    """
    bankpas = Bankpassen.query.get(bankpas_id)
    rekening = Rekeningen.query.get(bankpas.rekening_nummer)
    return render_template("showBalance.html", balans=rekening.balans)
