from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine

ssh_config = {
    "ssh_address_or_host": ("145.24.222.16", 22),
    "ssh_username": "ubuntu-1051158",
    "ssh_password": "NS24^vpY",
    "remote_bind_address": ("localhost", 3306),
}

with SSHTunnelForwarder(**ssh_config) as tunnel:
    db_config = {
        "username": "Admin",
        "password": "adminPasswordisholydonotgetitwrong",
        "host": "localhost",
        "port": tunnel.local_bind_port,
        "database": "JinhangBank",  # Replace with your database name
    }
    db_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
        **db_config
    )
    engine = create_engine(db_uri)

    # Connect to the database and execute a simple query
    connection = engine.connect()
    try:
        result = connection.execute("SELECT * FROM bankpassen")
        version = result.fetchone()
        print("Database version:", version)
    finally:
        connection.close()
