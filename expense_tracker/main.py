# TODO: write update function
# make CLI app to call functions directly on the terminal

import sqlite3
import datetime

today = str(datetime.date.today())

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

# Funktionen
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

def update_expense():
    id = input("Which id do you want to update? >> ")
    column = input("Which column do you want to change? >> ")
    if column in ["Expense", "Amount", "Category", "Date"]:
        pass
    else: print(f"Column {column} does not exist.")


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
    category = input("Category to sum up: >> ")
    cursor.execute("""
        SELECT SUM(amount) FROM expenses WHERE category = ?
        """, (category,))
    result = cursor.fetchone()
    print(f"Total expenses of category {category}: {result[0]}")

def sum_all():
    cursor.execute("""
        SELECT SUM(amount) FROM expenses
        """)
    result = cursor.fetchone()
    print(f"Total expenses are {result[0]}")

def sum_month():
    month = input("What month to sum up? >> ")
    year = today[:4]
    cursor.execute("""
        SELECT SUM(amount) FROM expenses WHERE date LIKE ?
        """, (f"{year}-{month}%",))
    result = cursor.fetchone()
    print(f"Expenses of month {month} are: {result[0]}")

def info():
    print("Here will be a manual for the CLI App\n")



# Eigentliches Programm
keys = {
    '1': view_expenses,
    '2': add_expense,
    '3': del_expense,
    '4': sum_all,
    '5': sum_month,
    '6': sum_category,
    '8': info,
}

user_input = ""

while user_input != '9':
    user_input = input("""-----Expense Tracker-----
1: View expenses                6: Sum category
2: Add expense                  7: ---
3: Delete expense               8: Info
4: Sum all expenses             9: EXIT program
5: Sum of month this year
-------------------------
>>> """)
    if user_input in ['1', '2', '3', '4', '5', '6', '7', '8']:
        keys[user_input]()
    elif user_input == '9':
        break
    else: print("Invalid input.")

print("EXIT successful.")




# Verbindung schließen
conn.close()