"""
Projekt 1 - Datový analytik s pythonem - 17/10/2024
autor: Michal Dvořák
e-mail: dvmichal@gmail.com
"""
# Registrovaní uživatelé
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Tři texty pro analýzu
# Registrovaní uživatelé
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Tři texty pro analýzu
TEXTS = [
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
    """Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.""",
    """Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."""
]

# 1. Přihlašování uživatele
username = input("nom d'utilisateur : ")
password = input("mot de passe : ")

# 2. Ověření uživatele
if registered_users.get(username) == password:
    print("----------------------------------------")
    print(f"Bienvenue dans l'application, {username}")
    print(f"Nous avons {len(TEXTS)} textes à analyser.")
    print("----------------------------------------")

    # 3. Výběr textu pro analýzu
    try:
        text_choice = int(input("Entrez un nombre entre 1 et 3 pour sélectionner : ")) - 1
        if text_choice not in range(len(TEXTS)):
            print("Choix invalide, fin du programme.")
            exit()
    except ValueError:
        print("Entrée invalide, fin du programme.")
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
    print(f"Il y a {word_count} mots dans le texte sélectionné.")
    print(f"Il y a {titlecase_count} mots en majuscule.")
    print(f"Il y a {uppercase_count} mots entièrement en majuscules.")
    print(f"Il y a {lowercase_count} mots en minuscules.")
    print(f"Il y a {numeric_count} chaînes numériques.")
    print(f"La somme de tous les nombres est {numeric_sum}")
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
    print("utilisateur non enregistré, fin du programme.")


# 1. Přihlašování uživatele
username = input("nom d'utilisateur : ")
password = input("mot de passe : ")

# 2. Ověření uživatele
if registered_users.get(username) == password:
    print("----------------------------------------")
    print(f"Bienvenue dans l'application, {username}")
    print(f"Nous avons {len(TEXTS)} textes à analyser.")
    print("----------------------------------------")

    # 3. Výběr textu pro analýzu
    try:
        text_choice = int(input("Entrez un nombre entre 1 et 3 pour sélectionner : ")) - 1
        if text_choice not in range(len(TEXTS)):
            print("Choix invalide, fin du programme.")
            exit()
    except ValueError:
        print("Entrée invalide, fin du programme.")
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
    print(f"Il y a {word_count} mots dans le texte sélectionné.")
    print(f"Il y a {titlecase_count} mots en majuscule.")
    print(f"Il y a {uppercase_count} mots entièrement en majuscules.")
    print(f"Il y a {lowercase_count} mots en minuscules.")
    print(f"Il y a {numeric_count} chaînes numériques.")
    print(f"La somme de tous les nombres est {numeric_sum}")
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
    print("utilisateur non enregistré, fin du programme.")
Projekt_01FR.py
Zobrazování položky Projekt_01FR.py.
