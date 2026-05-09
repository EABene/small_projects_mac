import os
from pathlib import Path
import json
from datetime import date, timedelta

# Speichert das heutige Datum in die Variable today
today = str(date.today())  # "2026-05-09"

# Fixiert den File Path auf genau die Stelle im Ordner neben main.py
FILE_PATH = Path(__file__).parent / "habits.json"

# Funktion um Habit hinzuzufügen
def add_habit(habit_list, habit):
    if habit not in habit_list:
        data[habit] = []

# Funktion um Habit abzuhaken
def complete_habit(habit_list, habit):
    if today not in habit_list[habit]:
        habit_list[habit].append(today)

# Berechnet den Streak
def streak_calc(habit_list):
    counter = 0
    day = date.today()
    while str(day) in habit_list:
        counter += 1
        day = day - timedelta(days=1)
    return counter

# Funktion, um alle Habits auszugeben und ihren Streak
def show_habits(habit_list):
    for habit in habit_list:
        print(f"{habit} - Streak: {streak_calc(habit_list[habit])} Days")


# initialisiert JSON File
if not FILE_PATH.exists():
    with open(FILE_PATH, "w") as f:
        json.dump({}, f)

# Lesen der JSON
with open(FILE_PATH, "r") as f:
    data = json.load(f)

# Eigentliche App-Ausführung
add_habit(data, "Tooth brushing")
add_habit(data, "Sports")
add_habit(data, "Meditate")
complete_habit(data, "Sports")
complete_habit(data, "Meditate")
show_habits(data)

# Schreibt alles in der Variable Data in JSON File
with open(FILE_PATH, "w") as f:
    json.dump(data, f, indent=2)




print("done")