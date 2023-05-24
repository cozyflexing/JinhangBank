# db.py
from sshtunnel import SSHTunnelForwarder
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create the SQLAlchemy object here, but do not initialize it yet.
db = SQLAlchemy()


def create_tunnel(app):
    ssh_config = {
        "ssh_address_or_host": (os.getenv("SSH_HOST"), int(os.getenv("SSH_PORT"))),
        "ssh_username": os.getenv("SSH_USERNAME"),
        "ssh_password": os.getenv("SSH_PASSWORD"),
        "remote_bind_address": ("localhost", 3306),
    }

    tunnel = SSHTunnelForwarder(**ssh_config)
    tunnel.start()

    db_config = {
        "username": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "host": "localhost",
        "port": tunnel.local_bind_port,
        "database": os.getenv("DB_NAME"),
    }

    db_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
        **db_config
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # No db.init_app(app) here

    return db, tunnel
