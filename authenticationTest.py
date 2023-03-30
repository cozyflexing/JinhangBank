from Read import readRFID
from Write import writeRFID
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()
users = []


class User:
    def __init__(self, accountNumber, cardNumber, pinCode, balance, tries):
        self.accountNumber = accountNumber
        self.cards = [cardNumber]
        self.pinCode = pinCode
        self.balance = balance
        self.tries = tries


def printBalance(self):
    print(f"Balance: {self.balance}")


def withdraw(self, amount):
    self.balance -= amount


def add(self, amount):
    self.balance += amount


def pinCodeCheck(userPinCode, givenPinCode):
    if userPinCode == givenPinCode:
        return True
    else:
        return False


def authentication(givenCard, users=[]):
    for user in users:
        if givenCard in user.cards:
            while user.tries < 3:
                pinCode = input("Pin code please: ")
                if pinCodeCheck(int(user.pinCode), int(pinCode)):
                    user.tries = 0
                    return print("Authentication Successful")
                else:
                    user.tries += 1
                    if 3 - user.tries > 0:
                        print(f"Authentication Failed. {3-user.tries} tries remaining.")
                    else:
                        return print(
                            f"Authentication Failed. {3-user.tries} try remaining."
                        )

            if user.tries == 3:
                return print("Your cards have been blocked, too many failed attempts.")


def login():
    givenCard = readRFID()
    authentication(givenCard[0], users)
