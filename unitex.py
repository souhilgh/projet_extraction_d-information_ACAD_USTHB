#ACAD C
#GHERBI SOUHIL 222231404213
#MOURI RAFIK 212131093211

import os
from os import path

#si corpus-medical_snt existe
if path.exists("corpus-medical_snt"):
  #si corpus-medical_snt existe le supprimme
    os.system("rd /s corpus-medical_snt")
# Cree nouveau dossier corpus-medical_snt    
os.mkdir("corpus-medical_snt")
# Normalise le fichier corpus-medical.txt en utilisant le fichier de normalisation Norm.txt
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
# Tokenise le fichier normalise corpus-medical.snt en utilisant l'alphabet Alphabet.txt
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
# Compresse le dictionnaire subst.dic
os.system("UnitexToolLogger Compress subst.dic")
# Construit le dictionnaire subst.bin et Dela_fr.bin à partir du fichier tokenisé corpus-medical.snt
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin Dela_fr.bin")
# Convertit le graphe d'extraction posologie.grf en format fst2
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
# Localise les occurrences du graphe d'extraction posologie.fst2 dans le fichier tokenisé corpus-medical.snt
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
# Extrait des concordances à partir des résultats de la localisation dans corpus-medical_snt/concord.ind
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
# Importance du fichier Alphabet.txt :
# Le fichier d'alphabet nomme "Alphabet.txt" est un fichier texte decrivant tous les caracteres d'une langue,ainsi que les correspondances entre lettres miniscules et majuscules.
# Sa presence est requise pour assurer le bon fonctionnement d'Unitex.
