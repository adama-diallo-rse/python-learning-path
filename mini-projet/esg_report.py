import csv
import json
import sys

# Vérifier l'argument
if len(sys.argv) != 2:
    sys.exit("Usage: python esg_report.py esg_data.csv")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Lire le CSV
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        data = list(reader)
except FileNotFoundError:
    sys.exit(f"File {sys.argv[1]} not found")

# Calculer les moyennes par catégorie
categories = {}
for row in data:
    cat = row["categorie"]
    score = int(row["score"])
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(score)

moyennes_categories = {}
for cat, scores in categories.items():
    moyennes_categories[cat] = round(sum(scores) / len(scores), 2)

# Calculer les moyennes par entreprise
entreprises = {}
for row in data:
    nom = row["entreprise"]
    score = int(row["score"])
    if nom not in entreprises:
        entreprises[nom] = []
    entreprises[nom].append(score)

moyennes_entreprises = {}
for nom, scores in entreprises.items():
    moyennes_entreprises[nom] = round(sum(scores) / len(scores), 2)

# Construire le rapport
rapport = {
    "titre": "Rapport ESG",
    "nombre_entreprises": len(entreprises),
    "moyennes_par_categorie": {
        "E (Environnement)": moyennes_categories.get("E", 0),
        "S (Social)": moyennes_categories.get("S", 0),
        "G (Gouvernance)": moyennes_categories.get("G", 0)
    },
    "moyennes_par_entreprise": moyennes_entreprises
}

# Exporter en JSON
with open("rapport_esg.json", "w") as outfile:
    json.dump(rapport, outfile, indent=4, ensure_ascii=False)

print("Rapport généré : rapport_esg.json")