""" 
ENGETO Datový analytik s pythonem 17/10/2024
Michal Dvořák
dvmichalgmail.com
 Projekt 02/a
 """
# Bulls and Cows Game
# Vylepšená verze s možností nastavení obtížnosti, limitu pokusů,
# ukládáním statistik a použitím modifikovaného algoritmu pro generování tajného čísla.

import time


def generate_secret_number_mod97():
    """Generates a 4-digit secret number using 38×x≡1(mod97)."""
    x = 1
    while True:
        if (38 * x) % 97 == 1:
            number = str(x).zfill(4)  # Ensure it's 4 digits long
            if len(set(number)) == 4 and number[0] != '0':  # Unique digits, no leading zero
                return number
        x += 1


def generate_secret_number(num_digits):
    """Generates a random secret number with unique digits."""
    from random import sample
    while True:
        number = sample(range(10), num_digits)
        if number[0] != 0:
            return ''.join(map(str, number))


def is_valid_guess(guess, num_digits):
    """Validates the user's guess."""
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
    """Evaluates the user's guess and counts bulls and cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def bulls_and_cows_game(num_digits, attempt_limit=None):
    """Main function to play the Bulls and Cows game."""
    print("\033[92mHi there!\033[0m")
    print("-----------------------------------------------")
    print("Welcome to Bulls and Cows!")
    print("Rules:")
    print(f"- A {num_digits}-digit number has been generated.")
    print("- Each digit is unique and the number does not start with 0.")
    print("- 'Bulls' mean correct digit in the correct position.")
    print("- 'Cows' mean correct digit in the wrong position.")
    print("Let's play!")
    print("-----------------------------------------------")

    secret = generate_secret_number(num_digits)
    attempts = 0
    start_time = time.time()

    while True:
        if attempt_limit and attempts >= attempt_limit:
            print("\033[91mGame over! You've reached the maximum number of attempts.\033[0m")
            print(f"The secret number was: {secret}")
            break

        guess = input("Enter a number (or type 'exit' to quit): ").strip()
        if guess.lower() == "exit":
            print("\033[93mThanks for playing! Goodbye.\033[0m")
            break

        if not is_valid_guess(guess, num_digits):
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)

        # Pluralization for output
        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")
        print("-----------------------------------------------")

        if bulls == num_digits:
            duration = time.time() - start_time
            print(f"\033[92mCorrect, you've guessed the right number in {attempts} guesses!\033[0m")
            print(f"It took you {duration:.2f} seconds.")
            print("-----------------------------------------------")
            return attempts, duration


def main():
    """Manages the game and keeps statistics."""
    game_history = []
    print("Welcome to the enhanced Bulls and Cows game!")
    print("-----------------------------------------------")
    print("Choose your difficulty:")
    print("1. Easy (3 digits)")
    print("2. Medium (4 digits)")
    print("3. Hard (5 digits)")

    while True:
        try:
            difficulty = int(input("Select difficulty (1-3): "))
            if difficulty in {1, 2, 3}:
                break
            else:
                print("Invalid choice! Please choose between 1, 2, and 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    num_digits = difficulty + 2

    print("Do you want to enable a limit on the number of attempts?")
    print("1. Yes")
    print("2. No")
    limit_choice = input("Select (1 or 2): ").strip()

    attempt_limit = None
    if limit_choice == "1":
        while True:
            try:
                attempt_limit = int(input("Enter the maximum number of attempts: "))
                if attempt_limit > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    game_count = 0

    while True:
        game_count += 1
        print(f"Starting game #{game_count}")
        attempts, duration = bulls_and_cows_game(num_digits, attempt_limit)

        game_history.append({
            "game_number": game_count,
            "attempts": attempts,
            "time": duration
        })

        print("Game History:")
        for game in game_history:
            print(f"- Game #{game['game_number']}: {game['attempts']} attempts, {game['time']:.2f} seconds")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Here is your game summary:")
            for game in game_history:
                print(f"- Game #{game['game_number']}: {game['attempts']} attempts, {game['time']:.2f} seconds")
            break


if __name__ == "__main__":
    main()
