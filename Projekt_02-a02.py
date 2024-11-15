# Projekt 02/a/ver.02
"""
ENGETO Datový analytik s pythonem 17/10/2024
Michal Dvořák
dvmichalgmail.com
 Bulls and Cows Game
 """
# This game supports multiple players, adaptive difficulty, time-limited moves, and statistics storage.

import json
import os
import time
import random

# 1. Konstanty a pomocné funkce
DATABASE_FILE = "player_data.json"

def load_database():
    """1.1 Načte databázi hráčů ze souboru JSON."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_database(database):
    """1.2 Uloží databázi hráčů do souboru JSON."""
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)

# 2. Registrace a přihlašování hráčů
def register_or_login(database):
    """
    2.1 Umožňuje hráči buď se přihlásit, nebo zaregistrovat.
    - Uchovává uživatelské jméno, heslo a statistiky.
    """
    print("Welcome to Bulls and Cows!")
    print("1. Log in")
    print("2. Register")
    choice = input("Choose an option (1 or 2): ").strip()

    while choice not in {"1", "2"}:
        print("Invalid choice! Please choose 1 or 2.")
        choice = input("Choose an option (1 or 2): ").strip()

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if choice == "1":  # Přihlášení
        if username in database and database[username]["password"] == password:
            print(f"Welcome back, {username}!")
            return username, database[username]
        else:
            print("Invalid username or password.")
            return register_or_login(database)

    elif choice == "2":  # Registrace
        if username in database:
            print("Username already exists. Please log in.")
            return register_or_login(database)
        database[username] = {
            "password": password,
            "games_played": 0,
            "total_attempts": 0,
            "best_time": None,
            "adaptive_difficulty": True,
            "stats": [],
        }
        print(f"Registration successful! Welcome, {username}!")
        return username, database[username]

# 3. Generování tajného čísla
def generate_secret_number(num_digits):
    """
    3.1 Generuje tajné číslo s unikátními číslicemi, které nezačíná nulou.
    """
    while True:
        number = random.sample(range(10), num_digits)
        if number[0] != 0:
            return ''.join(map(str, number))

# 4. Validace a vyhodnocení
def is_valid_guess(guess, num_digits):
    """
    4.1 Kontroluje, zda je hráčův tip platný:
    - Musí být číselný, správné délky, nezačínat nulou a mít unikátní číslice.
    """
    if not guess.isdigit():
        print("\033[91mInvalid input! Please enter a number.\033[0m")
        return False
    if len(guess) != num_digits:
        print(f"\033[91mInvalid input! Number must be {num_digits} digits long.\033[0m")
        return False
    if guess[0] == '0':
        print("\033[91mInvalid input! Number cannot start with 0.\033[0m")
        return False
    if len(set(guess)) != len(guess):
        print("\033[91mInvalid input! Digits must be unique.\033[0m")
        return False
    return True

def evaluate_guess(secret, guess):
    """
    4.2 Vyhodnocuje hráčův tip a počítá bulls (správná číslice, správná pozice)
        a cows (správná číslice, špatná pozice).
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

# 5. Herní smyčka
def play_game(username, user_data, time_limit, adaptive_difficulty, num_digits):
    """
    5.1 Řídí průběh jedné hry:
    - Generuje tajné číslo, počítá pokusy a hlídá čas.
    - Zobrazuje zpětnou vazbu hráči.
    """
    secret = generate_secret_number(num_digits)
    attempts = 0
    start_time = time.time()

    print(f"Game started! Try to guess the {num_digits}-digit number.")
    print(f"You have {time_limit} seconds per move.") if time_limit else None

    while True:
        if time_limit:
            remaining_time = time_limit - (time.time() - start_time)
            if remaining_time <= 0:
                print("\033[91mTime's up for this move! Game over.\033[0m")
                print(f"The secret number was: {secret}")
                return attempts, None

        guess = input(f"Enter your guess (time left: {remaining_time:.2f}s): ").strip() if time_limit else input(
            "Enter your guess: ").strip()

        if not is_valid_guess(guess, num_digits):
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == num_digits:
            duration = time.time() - start_time
            print(f"Congratulations, {username}! You've guessed the number in {attempts} attempts!")
            return attempts, duration

# 6. Hlavní funkce
def main():
    """
    6.1 Hlavní logika:
    - Umožňuje výběr režimu (single/multi-player), přihlašování a spuštění hry.
    - Spravuje statistiky hráčů.
    """
    database = load_database()

    print("Do you want to enable multi-player mode?")
    print("1. Yes")
    print("2. No")
    multiplayer = input("Select (1 or 2): ").strip() == "1"

    players = []
    if multiplayer:
        num_players = int(input("Enter the number of players: "))
        for _ in range(num_players):
            players.append(register_or_login(database))
    else:
        players.append(register_or_login(database))

    for username, user_data in players:
        print(f"Welcome, {username}!")
        adaptive_difficulty = user_data.get("adaptive_difficulty", True)
        print("Do you want adaptive difficulty? (yes/no)")
        adaptive_difficulty = input().strip().lower() == "yes"

        print("Set time limit for each move (0 for no limit): ")
        time_limit = int(input().strip())

        num_digits = 4  # Default difficulty
        if adaptive_difficulty:
            num_digits += user_data["games_played"] // 2

        attempts, duration = play_game(username, user_data, time_limit, adaptive_difficulty, num_digits)

        # Aktualizace statistik hráče
        user_data["games_played"] += 1
        user_data["total_attempts"] += attempts
        if duration and (user_data["best_time"] is None or duration < user_data["best_time"]):
            user_data["best_time"] = duration
        user_data["stats"].append({"attempts": attempts, "time": duration})

        print(f"We hope to see you soon, {username}!")
        time.sleep(5)

    save_database(database)


if __name__ == "__main__":
    main()
