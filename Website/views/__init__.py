# views/__init__.py
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder="/Users/aleniriskic/Desktop/JinhangBank/Website/templates",
        static_folder="/Users/aleniriskic/Desktop/JinhangBank/Website/static",
    )

    from .index import index_bp
    from .enterPin import enterPin_bp
    from .makeChoice import makeChoice_bp
    from .goodBye import goodBye_bp
    from .changePin import changePin_bp
    from .chooseAmount import chooseAmount_bp
    from .showBalance import showBalance_bp
    from .enterAmount import enterAmount_bp
    from .amountUnavailable import amountUnavailable_bp
    from .pickLanguage import pickLanguage_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(enterPin_bp)
    app.register_blueprint(makeChoice_bp)
    app.register_blueprint(goodBye_bp)
    app.register_blueprint(changePin_bp)
    app.register_blueprint(chooseAmount_bp)
    app.register_blueprint(showBalance_bp)
    app.register_blueprint(enterAmount_bp)
    app.register_blueprint(amountUnavailable_bp)
    app.register_blueprint(pickLanguage_bp)

    return app
