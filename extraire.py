#ACAD C
#GHERBI SOUHIL 222231404213
#MOURI RAFIK 212131093211

import os
import re
import codecs
import unicodedata
from collections import defaultdict

def normaliser_lettre(lettre):
    """Normalise une lettre pour regrouper E et É."""
    lettre_normalisee = unicodedata.normalize('NFD', lettre).encode('ascii', 'ignore').decode('utf-8')
    return lettre_normalisee.lower()

def extraire_noms_substances(dossier_vidal):
    substances = defaultdict(list)

    for fichier in sorted(os.listdir(dossier_vidal)):
        if fichier.endswith(".htm"):
            chemin_fichier = os.path.join(dossier_vidal, fichier)
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                contenu = f.read()

            matches = re.findall(r'href="Substance/[^"]+">([^<]+)</a>', contenu)

            for match in matches:
                substance = match.strip()
                lettre_initiale = normaliser_lettre(substance[0])
                substances[lettre_initiale].append(substance)

    return substances

def generer_dictionnaire_delaf(substances, fichier_sortie):
    with open(fichier_sortie, "w", encoding="utf-16") as f:
        # ajoute le BOM
        f.write('\ufeff')
        for lettre, noms in sorted(substances.items()):
            for nom in sorted(set(noms)):
                f.write(f"{nom},.N+subst\n")

def generer_infos(substances, fichier_infos):
    with open(fichier_infos, "w", encoding="utf-8") as f:
        total = 0
        for lettre, noms in sorted(substances.items()):
            count = len(set(noms))
            total += count
            f.write(f"{lettre.upper()}: {count}\n")

        f.write(f"Total: {total}\n")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python extraire.py <dossier_vidal>")
        sys.exit(1)

    dossier_vidal = sys.argv[1]

    if not os.path.isdir(dossier_vidal):
        print(f"Erreur: le dossier {dossier_vidal} n'existe pas.")
        sys.exit(1)

    substances = extraire_noms_substances(dossier_vidal)

    fichier_dictionnaire = "subst.dic"
    generer_dictionnaire_delaf(substances, fichier_dictionnaire)

    fichier_infos = "infos1.txt"
    generer_infos(substances, fichier_infos)

    for lettre, noms in sorted(substances.items()):
        print(f"{lettre.upper()}: {len(set(noms))}")

    print(f"\nTotal: {sum(len(set(noms)) for noms in substances.values())}")

if __name__ == "__main__":
    main()
