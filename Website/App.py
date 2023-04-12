# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enterPin")
def enterPin():
    return render_template("enterPin.html")


@app.route("/makeChoice")
def makeChoice():
    return render_template("makeChoice.html")


@app.route("/goodBye")
def goodBye():
    return render_template("goodBye.html")


@app.route("/changePin")
def changePin():
    return render_template("changePin.html")


@app.route("/chooseAmount")
def chooseAmount():
    return render_template("chooseAmount.html")


@app.route("/showBalance")
def showBalance():
    return render_template("showBalance.html")


@app.route("/enterAmount")
def enterAmount():
    return render_template("enterAmount.html")


@app.route("/amountUnavailable")
def amountUnavailable():
    return render_template("amountUnavailable.html")


@app.route("/pickLanguage")
def pickLanguage():
    return render_template("pickLanguage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
