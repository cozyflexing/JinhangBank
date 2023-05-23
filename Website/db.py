# db.py
from sshtunnel import SSHTunnelForwarder
from flask_sqlalchemy import SQLAlchemy
from flask import current_app


def create_tunnel():
    ssh_config = {
        "ssh_address_or_host": ("145.24.222.16", 22),
        "ssh_username": "ubuntu-1051158",
        "ssh_password": "NS24^vpY",
        "remote_bind_address": ("localhost", 3306),
    }

    tunnel = SSHTunnelForwarder(**ssh_config)

    db_config = {
        "username": "Admin",
        "password": "adminPasswordisholydonotgetitwrong",
        "host": "localhost",
        "port": tunnel.local_bind_port,
        "database": "JinhangBank",
    }

    db_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
        **db_config
    )

    # The SQLAlchemy object contains the engine
    current_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(current_app)

    return db, tunnel
