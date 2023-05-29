# views/pollForCard.py
from flask import Blueprint, jsonify
from Read import readRFID

pollForCard_bp = Blueprint("pollForCard", __name__)


@pollForCard_bp.route("/poll_for_card")
def poll_for_card():
    pas_nummer = readRFID()
    print("test")
    return jsonify({"pas_nummer": pas_nummer})
