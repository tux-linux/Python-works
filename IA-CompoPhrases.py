import random

pronoms = ["Je", "Tu", "Il", "Elle", "On", "Nous", "Vous", "Ils", "Elles"]
pronom = random.choice(pronoms)

print("-------- Créateur de phrases automatisé Python --------")
print("Créé par tux-linux, avril 2020. Tous droits réservés")

# Transformation des mots en listes
verbes = input("Quels sont les verbes des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listeverbes = verbes.split()
noms = input("Quels sont les noms des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listenoms = noms.split()
adjectifs = input("Quels sont les adjectifs des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listeadjectifs = adjectifs.split()

# Définition de l'accord du verbe "aller" selon les pronoms
if pronom == "Je":
    verbe = "vais"
elif pronom == "Tu":
    verbe = "vas"
elif pronom == "Il" or pronom == "Elle" or pronom == "On":
    verbe = "va"
elif pronom == "Nous":
    verbe = "allons"
elif pronom == "Vous":
    verbe = "allez"
elif pronom == "Ils" or pronom == "Elles":
    verbe = "vont"

# Choix du verbe final utilisé selon la liste donnée
if listeverbes == []:
    listeverbes = ["manger", "boire", "mettre", "aller", "être", "avoir", "prendre", "obtenir"]
    verbe1 = random.choice(listeverbes)
else:
    verbe1 = random.choice(listeverbes)

# Choix du nom utilisé selon la liste donnée
if listenoms == []:
    listenoms = ["arbre", "fruit", "insecte", "terrain", "serveur", "professeur", "maître", "mentor", "pays", "mot", "mélangeur"]
    nom = random.choice(listenoms)
else:
    nom = random.choice(listenoms)

# Choix du déterminant utilisé selon une liste donnée
listedeterminants = ["leur", "notre", "votre", "le", "son", "mon", "ton", "ce"]
determinant = random.choice(listedeterminants)

# Choix de l'adjectif utilisé selon une liste donnée
if listeadjectifs == []:
    listeadjectifs = ["doux", "fort", "tendre", "amusant", "proactif", "attentif", "gentil", "méchant"]
    adjectif = random.choice(listeadjectifs)
else:
    adjectif = random.choice(listeadjectifs)

print("\n\nVoici la phrase finale:")

# Définition d'exceptions selon le verbe utilisé, les déterminants utilisés, etc.
if verbe1 == "aller":
    etatphrase = 1
    verbes2 = ["voir", "manger", "enterrer", "détruire", "boire"]
    verbe2 = random.choice(verbes2)
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
elif verbe1 == "mettre" or verbe1 == "apporter" or verbe1 == "déposer" or verbe1 == "aimer" or verbe1 == "aider" or verbe1 == "apprendre" or verbe1 == "attendre" or verbe1 == "chercher" or verbe1 == "choisir" or verbe1 == "commander" or verbe1 == "commencer" or verbe1 == "connaître" or verbe1 == "continuer" or verbe1 == "détester" or verbe1 == "écouter" or verbe1 == "enseigner" or verbe1 == "entendre" or verbe1 == "envoyer" or verbe1 == "faire" or verbe1 == "féliciter" or verbe1 == "finir" or verbe1 == "garder" or verbe1 == "inviter" or verbe1 == "oublier" or verbe1 == "préparer" or verbe1 == "refuser" or verbe1 == "regretter" or verbe1 == "remercier" or verbe1 == "voir" or verbe1 == "vouloir":
    etatphrase = 2
    suites = ["dans un", "près d'un", "à côté d'un", "dans le", "dans leur", "dans notre", "dans votre", "dans son", "dans ton", "dans mon"]
    suite = random.choice(suites)
    nom2 = random.choice(listenoms)
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
else:
    etatphrase = 0
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
# Impression de la phrase finale
if etatphrase == 1:
    print("{0} {1} {2} {3} {4} {5} {6}.".format(pronom, verbe, verbe1, verbe2, determinant, nom, adjectif))
elif etatphrase == 2:
    print("{0} {1} {2} {3} {4} {5} {6} {7}.".format(pronom, verbe, verbe1, determinant, nom, adjectif, suite, nom2))
else:
    print("{0} {1} {2} {3} {4} {5}.".format(pronom, verbe, verbe1, determinant, nom, adjectif))
