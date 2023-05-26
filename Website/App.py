# app.py
from views import create_app
from db import create_tunnel
import os
from dotenv import load_dotenv
from models import Biljetten

load_dotenv()

app = create_app()

with app.app_context():
    db, tunnel = create_tunnel(app)
    db.init_app(app)
    total_value = Biljetten.total_value()

app.secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        tunnel.stop()
