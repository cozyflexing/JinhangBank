# views/__init__.py
from flask import Flask
import os


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "../static"),
    )

    # Importing and registering blueprints for different views
    from .scanCard import scanCard_bp
    from .enterPin import enterPin_bp
    from .makeChoice import makeChoice_bp
    from .goodBye import goodBye_bp
    from .changePin import changePin_bp
    from .chooseAmount import chooseAmount_bp
    from .showBalance import showBalance_bp
    from .enterAmount import enterAmount_bp
    from .amountUnavailable import amountUnavailable_bp
    from .pickLanguage import pickLanguage_bp
    from .bePatient import bePatient_bp
    from .bePatientReceipt import bePatientReceipt_bp
    from .takeMoney import takeMoney_bp
    from .receiptChoice import receiptChoice_bp
    from .takeReceipt import takeReceipt_bp
    from .verifyPasNummer import verifyPasNummer_bp
    from .verifyPinCode import verifyPinCode_bp
    from .blocked import blocked_bp
    from .RFID import RFID_bp

    app.register_blueprint(scanCard_bp)
    app.register_blueprint(enterPin_bp)
    app.register_blueprint(makeChoice_bp)
    app.register_blueprint(goodBye_bp)
    app.register_blueprint(changePin_bp)
    app.register_blueprint(chooseAmount_bp)
    app.register_blueprint(showBalance_bp)
    app.register_blueprint(enterAmount_bp)
    app.register_blueprint(amountUnavailable_bp)
    app.register_blueprint(pickLanguage_bp)
    app.register_blueprint(bePatient_bp)
    app.register_blueprint(bePatientReceipt_bp)
    app.register_blueprint(takeMoney_bp)
    app.register_blueprint(receiptChoice_bp)
    app.register_blueprint(takeReceipt_bp)
    app.register_blueprint(verifyPasNummer_bp)
    app.register_blueprint(verifyPinCode_bp)
    app.register_blueprint(blocked_bp)
    app.register_blueprint(RFID_bp)

    return app
