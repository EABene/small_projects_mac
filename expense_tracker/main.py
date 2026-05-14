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
    # Just print table
    print("ID   |Expense             |Amount    |Category       |Date")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<15} {row[4]}")


def add_expense():
    # User Input erfragen
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
    # User input erfragen
    id = input("ID of expense to delete: >> ")

    # Tabelleneintrag löschen
    cursor.execute("""
        DELETE FROM expenses WHERE id = ?
    """, (id,))

    #Änderungen speichern
    conn.commit()



def sum_category():
    pass



# Eigentliches Programm
keys = {
    '1': view_expenses,
    '2': add_expense,
    '3': del_expense,
    '4': sum_category
}

user_input = ""

while user_input != '5':
    user_input = input("""-----Expense Tracker-----
1: Ausgaben anzeigen
2: Ausgabe hinzufügen
3: Ausgabe löschen
4: Kategorie zusammenfassen
5: Programm BEENDEN
-------------------------
>>> """)
    if user_input in ['1', '2', '3', '4']:
        keys[user_input]()
    elif user_input == '5':
        break
    else: print("Invalid input.")

print("Programm erfolgreich beendet.")






# Verbindung schließen
conn.close()