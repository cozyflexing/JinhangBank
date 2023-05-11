# app.py
from views import create_app

app = create_app()

app.secret_key = "some_secret_key"

if __name__ == "__main__":
    app.run(debug=True)
