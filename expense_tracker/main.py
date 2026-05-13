import sqlite3
import datetime 

today = str(datetime.date.today())
print(today)

# Verbindung öffnen (erstellt .db Datei falls nicht existiert)
conn = sqlite3.connect("expenses.db")

# Cursor — das ist dein "Werkzeug" um Befehle zu schicken
cursor = conn.cursor()

# Tabelle erstellen if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        category TEXT,
        date TEXT
    )
""")


def view_expenses():
    pass

def add_expense():
    description = input("Title of expense: >> ")
    amount = float(input("Amount of expense: >> "))
    category = input("Category of expense: >> ")

    # Tabelleneintrag hinzufügen
    cursor.execute("""
        INSERT INTO expenses (description, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (description, amount, category, today))

    # Änderungen speichern
    conn.commit()

def del_expense():
    pass

def sum_category():
    pass



# Eigentliches Programm

user_input = input("""-----Expense Tracker-----
1: Ausgaben anzeigen
2: Ausgabe hinzufügen
3: Ausgabe löschen
-------------------------
>>> """)

keys = {
    '1': view_expenses,
    '2': add_expense,
    '3': del_expense,
    '4': sum_category

}

if user_input in ['1', '2', '3', '4']:
    keys[user_input]()
else: print("Invalid input.")


# Verbindung schließen
conn.close()