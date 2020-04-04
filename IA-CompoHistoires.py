import random

# Définition du pronom utilisé
pronoms = ["Je", "Tu", "Il", "Elle", "On", "Nous", "Vous", "Ils", "Elles"]
pronom = random.choice(pronoms)

print("-------- Créateur de phrases/histoires automatisé Python --------")
print("Créé par Nicolas Mailloux, avril 2020. Tous droits réservés")

# Transformation des mots en listes
verbes = input("Quels sont les verbes des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listeverbes = verbes.split()
noms = input("Quels sont les noms des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listenoms = noms.split()
adjectifs = input("Quels sont les adjectifs des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace.\n")
listeadjectifs = adjectifs.split()
adverbes = input("Quels sont les adverbes des mots de vocabulaire ? Les écrire ci-dessous, séparés d'un espace\n")
listeadverbes = adverbes.split()

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

print("\n\nVoici l'histoire finale:")

# Définition d'exceptions selon le verbe utilisé, les déterminants utilisés, etc.
if verbe1 == "aller":
    etatphrase = 1
    verbes2 = ["voir", "manger", "enterrer", "détruire", "boire"]
    verbe2 = random.choice(verbes2)
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
elif verbe1 == "mettre" or verbe1 == "apporter" or verbe1 == "déposer" or verbe1 == "aimer" or verbe1 == "aider" or verbe1 == "apprendre" or verbe1 == "attendre" or verbe1 == "chercher" or verbe1 == "choisir" or verbe1 == "commander" or verbe1 == "commencer" or verbe1 == "connaître" or verbe1 == "continuer" or verbe1 == "détester" or verbe1 == "écouter" or verbe1 == "enseigner" or verbe1 == "entendre" or verbe1 == "envoyer" or verbe1 == "faire" or verbe1 == "féliciter" or verbe1 == "finir" or verbe1 == "garder" or verbe1 == "inviter" or verbe1 == "oublier" or verbe1 == "préparer" or verbe1 == "refuser" or verbe1 == "regretter" or verbe1 == "remercier" or verbe1 == "voir" or verbe1 == "vouloir" or verbe1 == "péter":
    etatphrase = 2
    suites = ["dans un", "près d'un", "à côté d'un", "dans le", "dans leur", "dans notre", "dans votre", "dans son", "dans ton", "dans mon", "sur"]
    suite = random.choice(suites)
    nom2 = random.choice(listenoms)
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
else:
    etatphrase = 0
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
if etatphrase == 1:
    phrase = ("{0} {1} {2} {3} {4} {5} {6}.".format(pronom, verbe, verbe1, verbe2, determinant, nom, adjectif))
elif etatphrase == 2:
    phrase = ("{0} {1} {2} {3} {4} {5} {6} {7}.".format(pronom, verbe, verbe1, determinant, nom, adjectif, suite, nom2))
else:
    phrase = ("{0} {1} {2} {3} {4} {5}.".format(pronom, verbe, verbe1, determinant, nom, adjectif))

## Instanciation d'autres processus pour continuer l'histoire

# Définition du pronom de la deuxième phrase ainsi que de son accord au verbe
pronoms1 = ["Celui-ci", "Il"]
pronom1 = random.choice(pronoms1)
verbe11 = "va"
# Définition des adverbes
if listeadverbes == []:
    adverbes = ["doucement", "fortement", "tendrement", "proactivement", "attentivement", "gentiment", "méchamment", "désespérément"]
    adverbe = random.choice(adverbes)
else:
    adverbe = random.choice(listeadverbes)

# Définition des verbes utilisés
verbe111 = random.choice(listeverbes)

# Définition du nom utilisé
if listenoms == []:
    listenoms = ["arbre", "fruit", "insecte", "terrain", "serveur", "professeur", "maître", "mentor", "pays", "mot", "mélangeur"]
    nom1 = random.choice(listenoms)
else:
    nom1 = random.choice(listenoms)

# Définition du déterminant utilisé
if listedeterminants == []:
    listedeterminants = ["leur", "notre", "votre", "le", "son", "mon", "ton", "ce"]
    determinant1 = random.choice(listedeterminants)
else:
    determinant1 = random.choice(listedeterminants)

# Définition d'exceptions
if verbe111 == "aller":
    etatphrase = 1
    verbes22 = ["voir", "manger", "enterrer", "détruire", "boire"]
    verbe22 = random.choice(verbes22)
    if nom1[0] == "a" or nom1[0] == "e" or nom1[0] == "i" or nom1[0] == "o" or nom1[0] == "u" or nom1[0] == "y" or nom1[0] == "é":
        if determinant1 == "ce":
            determinant1 = "cet"
        elif determinant1 == "le":
            determinant1 = "l'"
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
elif verbe111 == "mettre" or verbe111 == "apporter" or verbe111 == "déposer" or verbe111 == "aimer" or verbe111 == "aider" or verbe111 == "apprendre" or verbe111 == "attendre" or verbe111 == "chercher" or verbe111 == "choisir" or verbe111 == "commander" or verbe111 == "commencer" or verbe111 == "connaître" or verbe111 == "continuer" or verbe111 == "détester" or verbe111 == "écouter" or verbe111 == "enseigner" or verbe111 == "entendre" or verbe111 == "envoyer" or verbe111 == "faire" or verbe111 == "féliciter" or verbe111 == "finir" or verbe111 == "garder" or verbe111 == "inviter" or verbe111 == "oublier" or verbe111 == "préparer" or verbe111 == "refuser" or verbe111 == "regretter" or verbe111 == "remercier" or verbe111 == "voir" or verbe111 == "vouloir" or verbe111 == "péter":
    etatphrase = 2
    suites1 = ["dans un", "près d'un", "à côté d'un", "dans le", "dans leur", "dans notre", "dans votre", "dans son", "dans ton", "dans mon", "sur"]
    suite1 = random.choice(suites1)
    nom22 = random.choice(listenoms)
    if nom1[0] == "a" or nom1[0] == "e" or nom1[0] == "i" or nom1[0] == "o" or nom1[0] == "u" or nom1[0] == "y" or nom1[0] == "é":
        if determinant1 == "ce":
            determinant1 = "cet"
        elif determinant1 == "le":
            determinant1 = "l'"
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
else:
    etatphrase = 0
    if nom1[0] == "a" or nom1[0] == "e" or nom1[0] == "i" or nom1[0] == "o" or nom1[0] == "u" or nom1[0] == "y" or nom1[0] == "é":
        if determinant1 == "ce":
            determinant1 = "cet"
        elif determinant1 == "le":
            determinant1 = "l'"
    if nom[0] == "a" or nom[0] == "e" or nom[0] == "i" or nom[0] == "o" or nom[0] == "u" or nom[0] == "y" or nom[0] == "é":
        if determinant == "ce":
            determinant = "cet"
        elif determinant == "le":
            determinant = "l'"
if etatphrase == 0:
    phrase1 = ("{0} {1} {2} {3} {4} {5}.".format(pronom1, verbe11, verbe111, determinant1, nom1, adverbe))
elif etatphrase == 1:
    phrase1 = ("{0} {1} {2} {3} {4} {5} {6}.".format(pronom1, verbe11, verbe111, verbe22, determinant1, nom1, adverbe))
elif etatphrase == 2:
    phrase1 = ("{0} {1} {2} {3} {4} {5} {6} {7}.".format(pronom1, verbe11, verbe111, determinant1, nom1, adverbe, suite1, nom22))

## Définition de la phrase finale

# Définition de la terminaison utilisée
terminaisons = ["Finalement,", "Pour finir,", "À la fin,", "Pour terminer,"]
terminaison = random.choice(terminaisons)

# Définition d'une fin de phrase (déterminant, nom, verbe, déterminant, nom, complément)
# Définition du verbe utilisé
verbes1111 = ["terminera", "finira", "concluera", "tournera", "plantera", "activera", "attendra", "mangera", "portera"]
verbe1111 = random.choice(verbes1111)

# Définition du déterminant utilisé
if listedeterminants == []:
    listedeterminants = ["leur", "notre", "votre", "le", "son", "mon", "ton", "ce"]
    determinant2 = random.choice(listedeterminants)
else:
    determinant2 = random.choice(listedeterminants)
# Définition du dernier nom utilisé
listenoms1 = ["repas", "en-cas", "insecte", "voyage", "parcours", "professeur", "maître", "mentor", "discours", "mot"]
nom2 = random.choice(listenoms1)
if nom2[0] == "a" or nom2[0] == "e" or nom2[0] == "i" or nom2[0] == "o" or nom2[0] == "u" or nom2[0] == "y" or nom2[0] == "é":
        if determinant2 == "ce":
            determinant2 = "cet"
        elif determinant2 == "le":
            determinant2 = "l'"
# Définition du complément utilisé
complements = ["et vous dira ainsi au-revoir", "et s'en ira calmement", "et quittera", "et vous regardera fixement"]
complement = random.choice(complements)
# Définition de la phrase
phrase2 = ("{0} {1} {2} {3} {4} {5} {6}.".format(terminaison, determinant, nom, verbe1111, determinant2, nom2, complement))

## Impression de l'histoire
print(phrase, phrase1, phrase2)

#### Tous droits réservés pour Nicolas Mailloux, avril 2020. Toute reproduction est illicite et constitue une contrefaçon ####