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
        habit_list[habit] = []

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
    print(25 * "-")
    for habit in habit_list:
        print(f"{habit} - Streak: {streak_calc(habit_list[habit])} Days")
    print(25 * "-")

#Funktion um eine Habit zu Löschen
def delete_habit(habit_list, habit):
    if habit in habit_list:
        del habit_list[habit]
        print(habit, "deleted.")
    else: print("habit not found in list.")


# initialisiert JSON File
if not FILE_PATH.exists():
    with open(FILE_PATH, "w") as f:
        json.dump({}, f)

# Lesen der JSON
with open(FILE_PATH, "r") as f:
    habit_list = json.load(f)

# Eigentliche App-Ausführung
user_input = ""
possible_options = ["1", "2", "3", "4", "5"]
function_keys = {
    "1": add_habit,
    "2": complete_habit,
    "3": show_habits,
    "4": delete_habit,
}

while user_input != "5":

    user_input = input("""Habit Tracker App Menu:
    1 - Habit hinzufügen
    2 - Habit erledigt markieren
    3 - Alle Habits anzeigen
    4 - Habit löschen
    5 - Beenden
    Was würdest du gerne tun? >> """)
   
    if user_input not in possible_options:
        print("Invalid input.")

    if user_input in ["1", "2", "4"]:
        habit = input("Welche Habit möchtest du bearbeiten? >> ")
        function_keys[user_input](habit_list, habit)
    elif user_input == "3":
        function_keys[user_input](habit_list)
    elif user_input == "5":
        print("Programm wird beendet.")
    


# Schreibt alles in der Variable habit_list in JSON File
with open(FILE_PATH, "w") as f:
    json.dump(habit_list, f, indent=2)


print("done")