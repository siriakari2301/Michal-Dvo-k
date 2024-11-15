# Projekt 02/a/ver 03
"""
ENGETO Analytik s pythonem 17/10/2024
Michal Dvořák
dvmichal(ad)gmail.com
"""
# Bulls and Cows Game
# Includes multi-user mode, guest mode, password validation, and more.

import json
import os
import time
import random
import re

DATABASE_FILE = "player_data.json"

# 1. Pomocné funkce pro práci s databází
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

# 2. Validace hesla
def is_valid_password(password):
    """2.1 Kontroluje, zda heslo splňuje požadavky."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must include at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."
    return True, ""

# 3. Registrace a přihlašování
def register_or_login(database):
    """3.1 Umožňuje hráči přihlásit se, registrovat nebo hrát jako host."""
    print("Welcome to Bulls and Cows!")
    print("1. Log in")
    print("2. Register")
    print("3. Play as Guest")
    choice = input("Choose an option (1-3): ").strip()

    while choice not in {"1", "2", "3"}:
        print("Invalid choice! Please choose 1, 2, or 3.")
        choice = input("Choose an option (1-3): ").strip()

    if choice == "3":  # Guest mode
        print("You are playing as a guest. Your results won't be saved.")
        return "Guest", None

    username = input("Enter your username: ").strip()
    if choice == "1":  # Log in
        password = input("Enter your password: ").strip()
        if username in database and database[username]["password"] == password:
            print(f"Welcome back, {username}!")
            return username, database[username]
        else:
            print("Invalid username or password.")
            return register_or_login(database)

    elif choice == "2":  # Register
        if username in database:
            print("Username already exists. Please choose a different username.")
            return register_or_login(database)
        while True:
            password = input("Enter a password: ").strip()
            valid, message = is_valid_password(password)
            if valid:
                break
            print(message)
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

# 4. Generování tajného čísla
def generate_secret_number(num_digits):
    """4.1 Generuje tajné číslo s unikátními číslicemi."""
    while True:
        number = random.sample(range(10), num_digits)
        if number[0] != 0:
            return ''.join(map(str, number))

# 5. Validace a vyhodnocení
def is_valid_guess(guess, num_digits):
    """5.1 Kontroluje, zda je hráčův tip platný."""
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
    """5.2 Vyhodnocuje hráčův tip a počítá bulls a cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

# 6. Herní smyčka
def play_game(username, user_data, time_limit, num_digits):
    """6.1 Řídí průběh jedné hry."""
    secret = generate_secret_number(num_digits)
    attempts = 0
    start_time = time.time()

    print(f"Game started! Try to guess the {num_digits}-digit number.")
    if time_limit:
        print(f"You have {time_limit} seconds per move (0 for no limit).")

    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ").strip()
        if guess.lower() == "exit":
            print("Exiting game. Returning to main menu...")
            return None, None

        if not is_valid_guess(guess, num_digits):
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == num_digits:
            duration = time.time() - start_time
            print(f"Congratulations, {username}! You've guessed the number in {attempts} attempts!")
            return attempts, duration

# 7. Hlavní logika
def main():
    """7.1 Hlavní logika programu."""
    database = load_database()

    while True:
        print("Choose difficulty:")
        print("1. Easy (3 digits)")
        print("2. Medium (4 digits)")
        print("3. Hard (5 digits)")
        print("4. Expert (6 digits)")
        difficulty = input("Select difficulty (1-4): ").strip()

        while difficulty not in {"1", "2", "3", "4"}:
            print("Invalid choice! Please select between 1 and 4.")
            difficulty = input("Select difficulty (1-4): ").strip()

        num_digits = int(difficulty) + 2

        print("Set time limit for each move (1-120 seconds, or 0 for no limit):")
        while True:
            try:
                time_limit = int(input().strip())
                if 0 <= time_limit <= 120:
                    break
                else:
                    print("Invalid input! Enter a number between 0 and 120.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        username, user_data = register_or_login(database)

        if user_data is None:  # Guest mode
            attempts, duration = play_game(username, None, time_limit, num_digits)
            print(f"Guest results: {attempts} attempts, time: {duration}s") if attempts else None
        else:
            attempts, duration = play_game(username, user_data, time_limit, num_digits)

            if attempts is not None:  # Update stats only if game was completed
                user_data["games_played"] += 1
                user_data["total_attempts"] += attempts
                if duration and (user_data["best_time"] is None or duration < user_data["best_time"]):
                    user_data["best_time"] = duration
                user_data["stats"].append({"attempts": attempts, "time": duration})

        save_database(database)

if __name__ == "__main__":
    main()
