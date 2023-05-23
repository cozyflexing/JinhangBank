# views/verifyPasNummer.py
from sqlalchemy import create_engine, MetaData, Table, select


def connect_to_db():
    engine = create_engine(
        "mysql+pymysql://root:Alenheefteenmacbookairuit2022@localhost:3306/JinhangBank"
    )
    return engine


id = 1
engine = connect_to_db()

# reflect an existing table called 'bankpassen'
metadata = MetaData()
bankpassen = Table("bankpassen", metadata, autoload_with=engine)

# equivalent to 'SELECT * FROM bankpassen WHERE bankpas_id = id'
query = select(bankpassen).where(bankpassen.columns.bankpas_id == id)

with engine.connect() as connection:
    result = connection.execute(query)
    row = result.fetchone()
    print(row)
