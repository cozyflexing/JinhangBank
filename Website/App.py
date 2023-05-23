# app.py
from views import create_app
from db import create_tunnel

app = create_app()
# db, tunnel = create_tunnel()

app.secret_key = "some_secret_key"

if __name__ == "__main__":
    try:
        # tunnel.start()
        app.run(debug=True)
    finally:
        pass
        # tunnel.stop()
