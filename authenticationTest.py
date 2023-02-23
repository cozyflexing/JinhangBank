from time import sleep
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
users = []


class User:
    def __init__(self, accountNumber, cardNumber, pinCode, balance):
        self.accountNumber = accountNumber
        self.cards = [cardNumber]
        self.pinCode = pinCode
        self.balance = balance

    def printBalance(self):
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def add(self, amount):
        self.balance += amount

    def addCards(self):
        try:
            print("Hold card near reader. ")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id, text))
            self.cards.append(id)
            self.pinCode = text
        except KeyboardInterrupt:
            GPIO.cleanup()
            raise


def authentication(accountNumber, pinCode, user=[]):
    for user in users:
        if user.accountNumber == accountNumber:
            if user.pinCode == pinCode:
                print("Authentication successful.")
            else:
                print("Authentication failed, incorrect pin code.")
        else:
            print("Authentication failed, user does not exist.")


def login():
    accountNumber = input("Accountnumber please: ")
    pinCode = input("Pin code please: ")
    authentication(accountNumber, pinCode, users)
