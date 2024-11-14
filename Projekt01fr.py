"""
Projekt 1 - Datový analytik s pythonem - 17/10/2024
autor: Michal Dvořák
e-mail: dvmichal@gmail.com
Původní text jsem kopiroval z e-mailu, protože jsem nemohl otevřít - ochrana systému, přípona "py",
takže se random něco zkopírovalo vícekrát. Obecný text nahrazen zadáním. FR protože EN je ordinerní...
"""
# 1. Registrovaní uživatelé
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# 2. Tři texty pro analýzu
TEXTS = [
'''bobSituated about 10 miles west of Kemmerer,
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

# 3. Přihlašování uživatele
username = input("nom d'utilisateur : ")
password = input("mot de passe : ")

# 4. Ověření uživatele
if registered_users.get(username) == password:
    print("----------------------------------------")
    print(f"Bienvenue dans l'application, {username}")
    print(f"Nous avons {len(TEXTS)} textes à analyser.")
    print("----------------------------------------")

    # 5. Výběr textu pro analýzu
    try:
        text_choice = int(input("Entrez un nombre entre 1 et 3 pour sélectionner : ")) - 1
        if text_choice not in range(len(TEXTS)):
            print("Choix invalide, fin du programme.")
            exit()
    except ValueError:
        print("Entrée invalide, fin du programme.")
        exit()

    # 6. Analýza vybraného textu
    selected_text = TEXTS[text_choice]
    words = selected_text.split()

    # 7. Počet slov
    word_count = len(words)

    # 8. Počet slov začínajících velkým písmenem, velkých slov, malých slov
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    
    # 9. Počet čísel (ne cifer) a součet čísel
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())

    # 10. Výpis výsledků analýzy
    print("----------------------------------------")
    print(f"Il y a {word_count} mots dans le texte sélectionné.")
    print(f"Il y a {titlecase_count} mots en majuscule.")
    print(f"Il y a {uppercase_count} mots entièrement en majuscules.")
    print(f"Il y a {lowercase_count} mots en minuscules.")
    print(f"Il y a {numeric_count} chaînes numériques.")
    print(f"La somme de tous les nombres est {numeric_sum}")
    print("----------------------------------------")

    # 11. Sloupcový graf pro četnost délek slov
    word_lengths = {}
    for word in words:
        length = len(word.strip(",.!?"))
        word_lengths[length] = word_lengths.get(length, 0) + 1

    # 12. Výpis grafu
    print("LEN|  OCCURRENCES  |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
        occurrences = word_lengths[length]
        print(f"{length:>3}|{'*' * occurrences:<15}|{occurrences}")

else:
    print("utilisateur non enregistré, fin du programme.")
