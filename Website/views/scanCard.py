# views/scanCard.py
from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

scanCard_bp = Blueprint("scanCard", __name__)


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Alenheefteenmacbookairuit2022",  # Replace with your own password
        database="JinhangBank",
    )


@scanCard_bp.route("/")
def scanCard():
    return render_template("scanCard.html")
