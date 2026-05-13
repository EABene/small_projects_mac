import sqlite3

# Verbindung öffnen (erstellt .db Datei falls nicht existiert)
conn = sqlite3.connect("expenses.db")

# Cursor — das ist dein "Werkzeug" um Befehle zu schicken
cursor = conn.cursor()

# Befehl ausführen
cursor.execute("SQL-BEFEHL HIER")

# Änderungen speichern
conn.commit()

# Verbindung schließen
conn.close()
