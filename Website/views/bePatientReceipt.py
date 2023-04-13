# views/bePatientReceipt.py
from flask import Blueprint, render_template

bePatientReceipt_bp = Blueprint("bePatientReceipt", __name__)


@bePatientReceipt_bp.route("/bePatientReceipt")
def bePatientReceipt():
    return render_template("bePatientReceipt.html")
