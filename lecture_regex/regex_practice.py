# Pratique des expressions régulières
#
# TODO 1 : Extraire tous les emails d'un texte
# TODO 2 : Extraire tous les numéros de téléphone français d'un texte
# TODO 3 : Valider qu'une chaîne respecte le format date JJ/MM/AAAA

import re

# Texte de test
texte = """
Bonjour, contactez-moi à adama7.diallo.pro@gmail.com ou bien à
contact@younivibe.fr pour le projet RSE. Mon numero est le 07 53 03 48 68
et mon collegue Jean (jean.dupont@entreprise.com) est au 0612345678.
La reunion est prevue le 15/04/2026 ou le 22/04/2026 si besoin.
"""

# ============================================================
# TODO 1 : Extraire tous les emails
# ============================================================
# Décomposition du pattern :
# [\w\.-]+   -> 1 ou plusieurs lettres/chiffres/points/tirets (avant le @)
# @          -> le caractère @ littéralement
# [\w\.-]+   -> idem pour le nom de domaine (gmail, younivibe, etc.)
# \.         -> un point littéral (échappé avec \ car . veut dire "n'importe quel caractère" en regex)
# \w+        -> l'extension (com, fr, org, etc.)

pattern_email = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(pattern_email, texte)

print("=== EMAILS TROUVES ===")
for email in emails:
    print(f"  - {email}")
print(f"Total : {len(emails)} email(s)\n")


# ============================================================
# TODO 2 : Extraire tous les numéros de téléphone français
# ============================================================
# Format français : 10 chiffres commencant par 0
# Peut être écrit avec ou sans espaces : 0612345678 ou 07 53 03 48 68
#
# Décomposition :
# 0          -> commence par 0
# \d         -> 1 chiffre
# (\s?\d{2}){4} -> groupe répété 4 fois : espace optionnel + 2 chiffres
# Total : 1 + (2*4) = 9 chiffres après le 0 = 10 chiffres OK

pattern_tel = r"0\d(\s?\d{2}){4}"
telephones = re.findall(pattern_tel, texte)

# ATTENTION : findall avec des groupes () retourne seulement les groupes capturés
# Pour avoir le numéro complet, on utilise re.finditer qui donne accès au match entier
telephones_complets = [match.group() for match in re.finditer(pattern_tel, texte)]

print("=== NUMEROS DE TELEPHONE TROUVES ===")
for tel in telephones_complets:
    print(f"  - {tel}")
print(f"Total : {len(telephones_complets)} numero(s)\n")


# ============================================================
# TODO 3 : Valider le format date JJ/MM/AAAA
# ============================================================
# Décomposition du pattern :
# \d{2}      -> exactement 2 chiffres pour le jour
# /          -> slash littéral
# \d{2}      -> exactement 2 chiffres pour le mois
# /          -> slash littéral
# \d{4}      -> exactement 4 chiffres pour l'année
#
# IMPORTANT : on utilise re.fullmatch() au lieu de re.search()
# fullmatch vérifie que TOUTE la chaîne correspond, pas juste une partie
# Sinon "abc15/04/2026xyz" serait validé à tort

def valider_date(date_str):
    """Renvoie True si la date est au format JJ/MM/AAAA, False sinon."""
    pattern_date = r"\d{2}/\d{2}/\d{4}"
    if re.fullmatch(pattern_date, date_str):
        return True
    return False


# Tests de la fonction
dates_a_tester = [
    "15/04/2026",   # OK
    "22/04/2026",   # OK
    "1/4/2026",     # KO (pas 2 chiffres pour jour et mois)
    "15-04-2026",   # KO (tirets au lieu de slashs)
    "15/04/26",     # KO (année sur 2 chiffres)
    "abc15/04/2026" # KO (caractères en plus)
]

print("=== VALIDATION DE DATES ===")
for date in dates_a_tester:
    resultat = "VALIDE" if valider_date(date) else "INVALIDE"
    print(f"  {date:<20} -> {resultat}")