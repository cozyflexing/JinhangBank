from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from db import create_tunnel, db_uri
from models import Adressen, Bankpassen, Klanten, Rekeningen, Transacties
from flask import Flask
import random

# Create a Flask application instance
app = Flask(__name__)
db, _ = create_tunnel(app)

# Create engine
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

# Assign engine to session
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()


def populate_db(num_entries=100):
    for _ in range(num_entries):
        # Populate Adressen
        adres = Adressen(
            huisnummer=str(random.randint(1, 999)), postcode=fake.postcode()
        )
        session.add(adres)
        session.commit()  # We need to commit after each add to get the primary key.

        # Populate Rekeningen
        rekening = Rekeningen(
            rekening_nummer=f"CHJNHB{generate_random_number()}",
            balans=random.uniform(0, 100000),
        )
        session.add(rekening)
        session.commit()

        # Populate Klanten
        klant = Klanten(
            voornaam=fake.first_name(),
            tussenvoegsel=fake.prefix(),
            achternaam=fake.last_name(),
            email=fake.email(),
            telefoonnummer=fake.phone_number(),
            geboortedatum=fake.date_of_birth(minimum_age=18, maximum_age=90),
            adres_id=adres.adres_id,
        )
        session.add(klant)
        session.commit()

        # Populate Bankpassen
        bankpas = Bankpassen(
            pas_nummer=int(generate_random_number()),
            pin_code=str(random.randint(0000, 9999)),
            is_locked=0,
            rekening_nummer=rekening.rekening_nummer,
            klant_id=klant.klant_id,
        )
        session.add(bankpas)
        session.commit()

        # Populate Transacties
        transactie = Transacties(
            datum=fake.date_this_year(),
            tijd=fake.time(),
            locatie=fake.address(),
            type=random.choice(["deposit", "withdrawal", "payment"]),
            hoeveelheid=random.uniform(0, 1000),
            bankpas_id=bankpas.bankpas_id,
            rekening_nummer=rekening.rekening_nummer,
        )
        session.add(transactie)

    # Commit all changes to the database
    session.commit()


def generate_random_number():
    min_value = 10**8  # this is the smallest 9-digit number
    max_value = 10**9 - 1  # this is the largest 9-digit number
    return str(random.randint(min_value, max_value))


if __name__ == "__main__":
    populate_db()
