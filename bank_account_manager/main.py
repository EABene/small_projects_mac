# TODO: CLI Menü bauen rund um das ganze
# FIXME
# HACK
# NOTE
# XXX 

import datetime
today = str(datetime.date.today())

class BankAccount:
    def __init__(self, name, account_number, password, balance):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.transaction_history = []

    def __str__(self):
        return f"Owner: {self.name} | IBAN: {self.account_number} | Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"{today}: +{amount}")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.transaction_history.append(f"{today}: -{amount}") # add to history    
        else: print("Going lower than 0 not possible")

    def get_balance(self):
        print(f"Current balance: € {self.balance}")

    def get_transaction_history(self):
        print(self.transaction_history)


class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, password, balance, interest_rate):
        super().__init__(name, account_number, password, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest
        self.transaction_history.append(f"{today}: +{interest}")




# Actual Program

account = BankAccount("John Doe", "1234", "geheim", 1000)
sparkonto = SavingsAccount("Anna Lisitsa", "5678", "geheim", 800, 0.02)



print(account)
print(sparkonto)

"""
sparkonto.deposit(800)
sparkonto.get_balance()
sparkonto.add_interest()
sparkonto.get_balance()
sparkonto.get_transaction_history()

print(account.name)
print(account.balance)
account.deposit(50)
account.withdraw(600)
account.deposit(500)
account.withdraw(700)
account.get_balance()
account.get_transaction_history()
"""



def greet(name, account_number, balance):

    print(f"""Welcome, {name}!
    Account Number: {account_number}
    Balance: €{balance}

    1 - Einzahlen
    2 - Abheben
    3 - Kontostand anzeigen
    4 - Transaktionsverlauf
    5 - Sparkonto anzeigen""")

# greet("Ben")