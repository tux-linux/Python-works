import random
from math import sqrt

nombres = range(1, 100000)
operations = ["*", "/", "+", "-", "sqrt"]

print("Calculatrice aléatoire Python")
_init_ = 1
while _init_ == 1:
    nombre1 = random.choice(nombres)
    nombre2 = random.choice(nombres)
    operation = random.choice(operations)
    if operation == "*":
        resultat = nombre1 * nombre2
        print("Le produit de {0} et de {1} donne {2}.".format(nombre1, nombre2, resultat))
        input("")
    elif operation == "/":
        resultat = nombre1 / nombre2
        print("Le quotient de {0} et de {1} donne {2}.".format(nombre1, nombre2, resultat))
        input("")
    elif operation == "+":
        resultat = nombre1 + nombre2
        print("La somme de {0} et de {1} donne {2}.".format(nombre1, nombre2, resultat))
        input("")
    elif operation == "-":
        resultat = nombre1 - nombre2
        print("La différence de {0} et de {1} donne {2}.".format(nombre1, nombre2, resultat))
        input("")
    elif operation == "sqrt":
        nombresR = [nombre1, nombre2]
        nombre3R = random.choice(nombresR)
        resultat = sqrt(nombre3R)
        print("La racine carrée de {0} donne {1}.".format(nombre3R, resultat))
        input("")