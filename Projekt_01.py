# Registrovaní uživatelé
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Tři texty pro analýzu
TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# 1. Přihlašování uživatele
username = input("username: ")
password = input("password: ")

# 2. Ověření uživatele
if registered_users.get(username) == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")

    # 3. Výběr textu pro analýzu
    try:
        text_choice = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
        if text_choice not in range(len(TEXTS)):
            print("Invalid choice, terminating the program.")
            exit()
    except ValueError:
        print("Invalid input, terminating the program.")
        exit()

    # 4. Analýza vybraného textu
    selected_text = TEXTS[text_choice]
    words = selected_text.split()

    # Počet slov
    word_count = len(words)

    # Počet slov začínajících velkým písmenem, velkých slov, malých slov
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    
    # Počet čísel (ne cifer) a součet čísel
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())

    # Výpis výsledků analýzy
    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")
    print("----------------------------------------")

    # 5. Sloupcový graf pro četnost délek slov
    word_lengths = {}
    for word in words:
        length = len(word.strip(",.!?"))
        word_lengths[length] = word_lengths.get(length, 0) + 1

    # Výpis grafu
    print("LEN|  OCCURRENCES  |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
        occurrences = word_lengths[length]
        print(f"{length:>3}|{'*' * occurrences:<15}|{occurrences}")

else:
    print("unregistered user, terminating the program.")
