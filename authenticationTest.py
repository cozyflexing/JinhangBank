users = []


class User:
    def __init__(self, accountNumber, cardNumber, pinCode, balance):
        self.accountNumber = accountNumber
        self.cardNumber = cardNumber
        self.pinCode = pinCode
        self.balance = balance

    def printBalance(self):
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def add(self, amount):
        self.balance += amount


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


users.append(User("NL00JHBK1234567890", "000", "0000", 100))


User.printBalance(users[0])
User.add(users[0], 100)
User.printBalance(users[0])
User.withdraw(users[0], 75)
User.printBalance(users[0])
