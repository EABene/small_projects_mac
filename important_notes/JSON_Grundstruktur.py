# Fixiert den File Path auf genau die Stelle im Ordner neben main.py
FILE_PATH = Path(__file__).parent / "dict.json"

# 1. Initialisieren/erstellen falls nicht existiert
if not FILE_PATH.exists():
    with open(FILE_PATH, "w") as f:
        json.dump({}, f)

# 2. Laden → ins Dict
with open(FILE_PATH, "r") as f:
    habit_list = json.load(f)

# 3. Mit dem Dict arbeiten
# ... ganzes Programm ...

# 4. Dict → zurück in JSON
with open(FILE_PATH, "w") as f:
    json.dump(habit_list, f, indent=2)

# "w" = write, "r" = read
