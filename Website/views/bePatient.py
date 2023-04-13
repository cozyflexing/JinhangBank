# views/bePatient.py
from flask import Blueprint, render_template, request

bePatient_bp = Blueprint("bePatient", __name__)


@bePatient_bp.route("/bePatient", methods=["GET", "POST"])
def bePatient():
    if request.method == "POST":
        # You can access the submitted data using request.form.get() to avoid errors if the key does not exist
        input_text = request.form.get("input_text")
        amount = request.form.get("amount")
        print(input_text)
        print(amount)
        # Process the input text and amount here if needed

    return render_template("bePatient.html")
