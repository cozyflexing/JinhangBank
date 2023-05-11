# views/bePatientReceipt.py
from flask import Blueprint, render_template

bePatientReceipt_bp = Blueprint("bePatientReceipt", __name__)


@bePatientReceipt_bp.route("/bePatientReceipt")
def bePatientReceipt():
    """
    Render the bePatientReceipt.html template when the route is accessed.
    """
    return render_template("bePatientReceipt.html")
