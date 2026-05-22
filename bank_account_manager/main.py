
class BankAccount:
    def __init__(self, name, account_number, password, balance):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(amount):
        pass


konto = BankAccount("John", "1234", "geheim", "1000€")
print(konto.balance)
print(konto.name)



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