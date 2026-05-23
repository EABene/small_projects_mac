
class BankAccount:
    def __init__(self, name, account_number, password, balance):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("going lower than 0 not possible")
        else: self.balance -= amount

    def get_balance(self):
        print(f"Current balance: € {self.balance}")



account = BankAccount("John Doe", "1234", "geheim", 1000)

print(account.name)
print(account.balance)
account.deposit(50)
account.withdraw(600)
account.get_balance()




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