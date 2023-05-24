# app.py
from views import create_app
from db import create_tunnel, db
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

with app.app_context():
    db, tunnel = create_tunnel(app)
    db.init_app(app)

app.secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        tunnel.stop()
