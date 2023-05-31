from flask import Flask, request, jsonify
from db import db
from models import Rekeningen, Bankpassen

app = Flask(__name__)


@app.route("/api/balance", methods=["POST"])
def balance():
    data = request.get_json()
    rekening_nummer: str = data.get("acctNo")
    pin: str = data.get("pin")

    account = (
        db.session.query(Rekeningen).filter_by(rekening_nummer=rekening_nummer).first()
    )
    if not account:
        return jsonify(
            {
                "status": 400,
                "message": "Invalid account number.",
                "success": False,
                "acctNo": None,
            }
        )

    bankpas = (
        db.session.query(Bankpassen).filter_by(rekening_nummer=rekening_nummer).first()
    )
    if not bankpas or bankpas.pin_code != pin:
        return jsonify(
            {
                "status": 401,
                "message": "Invalid PIN.",
                "success": False,
                "acctNo": None,
            }
        )

    balance = account.balans
    return jsonify(
        {"status": 200, "balance": balance, "success": True, "acctNo": rekening_nummer}
    )


@app.route("/api/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    rekening_nummer: str = data.get("acctNo")
    pin: str = data.get("pin")
    amount: int = data.get("amount")

    account = (
        db.session.query(Rekeningen).filter_by(rekening_nummer=rekening_nummer).first()
    )
    if not account:
        return jsonify(
            {
                "status": 400,
                "message": "Invalid account number.",
                "success": False,
                "acctNo": None,
            }
        )

    bankpas = (
        db.session.query(Bankpassen).filter_by(rekening_nummer=rekening_nummer).first()
    )
    if not bankpas or bankpas.pin_code != pin:
        return jsonify(
            {
                "status": 401,
                "message": "Invalid PIN.",
                "success": False,
                "acctNo": None,
            }
        )

    if account.balans < amount:
        return jsonify(
            {
                "status": 402,
                "message": "Insufficient balance.",
                "success": False,
                "acctNo": None,
            }
        )

    account.balans -= amount
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "message": "Withdrawal successful.",
            "success": True,
            "acctNo": rekening_nummer,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
