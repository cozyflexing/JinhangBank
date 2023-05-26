# models.py
from db import db
from sqlalchemy import func


class Adressen(db.Model):
    __tablename__ = "adressen"

    adres_id = db.Column(db.Integer, primary_key=True)
    huisnummer = db.Column(db.String(10))
    postcode = db.Column(db.String(10))


class Bankpassen(db.Model):
    __tablename__ = "bankpassen"

    bankpas_id = db.Column(db.Integer, primary_key=True)
    pas_nummer = db.Column(db.BigInteger)
    pin_code = db.Column(db.String(4))
    is_locked = db.Column(db.Integer)
    rekening_nummer = db.Column(
        db.String(255), db.ForeignKey("rekeningen.rekening_nummer")
    )
    klant_id = db.Column(db.Integer, db.ForeignKey("klanten.klant_id"))


class Klanten(db.Model):
    __tablename__ = "klanten"

    klant_id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(50))
    tussenvoegsel = db.Column(db.String(20))
    achternaam = db.Column(db.String(50))
    email = db.Column(db.String(100))
    telefoonnummer = db.Column(db.String(20))
    geboortedatum = db.Column(db.Date)
    adres_id = db.Column(db.Integer, db.ForeignKey("adressen.adres_id"))


class Rekeningen(db.Model):
    __tablename__ = "rekeningen"

    rekening_nummer = db.Column(db.String(255), primary_key=True)
    balans = db.Column(db.Numeric(10, 2))


class Transacties(db.Model):
    __tablename__ = "transacties"

    transactie_id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date)
    tijd = db.Column(db.Time)
    locatie = db.Column(db.String(255))
    type = db.Column(db.String(255))
    hoeveelheid = db.Column(db.Numeric(10, 2))
    bankpas_id = db.Column(db.Integer, db.ForeignKey("bankpassen.bankpas_id"))
    rekening_nummer = db.Column(
        db.String(255), db.ForeignKey("rekeningen.rekening_nummer")
    )


class Biljetten(db.Model):
    __tablename__ = "biljetten"

    waarde = db.Column(db.Integer, primary_key=True)
    hoeveelheid = db.Column(db.Integer)

    @staticmethod
    def total_value():
        result = db.session.query(
            func.sum(Biljetten.waarde * Biljetten.hoeveelheid)
        ).scalar()
        return result if result is not None else 0
