from math import pi, sqrt

def airecerclerayon(r):
    float(r)
    res = pi * r * r
    print(res)
def airecerclediametre(d):
    float(d)
    res = pi * (d/2) * (d/2)
    print(res)
def circonferencecerclerayon(r):
    float(r)
    res = (r * 2) * pi
    print(res)
def circonferencecerclediametre(d):
    float(d)
    res = pi * d
    print(res)
def rayoncercle(C):
    float(C)
    res = ((C / pi)/2)
    print(res)
def diametrecercle(C):
    float(C)
    res = (C / pi)
    print(res)
def airepolygoneregulier(c, a, n):
    float(c)
    float(a)
    float(n)
    res = (c * a * n) * 0.5
    print(res)
def circonferencecercleaire(A):
    float(A)
    res0 = sqrt(A / pi)
    res1 = (res0 * 2) * pi
    print(res1)
def rayoncercleaire(A):
    float(A)
    res = sqrt(A / pi)
    print(res)
def diametrecercleaire(A):
    float(A)
    res = (sqrt(A / pi)) * 2
    print(res)
def addition(nb1, nb2):
    float(nb1)
    float(nb2)
    res = nb1 + nb2
    print(res)
def soustraction(nb1, nb2):
    float(nb1)
    float(nb2)
    res = nb1 - nb2
    print(res)
def multiplication(nb1, nb2):
    float(nb1)
    float(nb2)
    res = nb1 * nb2
    print(res)
def division(nb1, nb2):
    float(nb1)
    float(nb2)
    res = nb1 / nb2 
    print(res)
def racinecarree(n):
    float(n)
    res = sqrt(n)
    print(res)

print("Calculatrice Python pour la géométrie")
choix = input("Opération?\n1. Aire d'un cercle avec son rayon\n2. Aire d'un cercle avec son diamètre\n3. Circonférence d'un cercle avec son rayon\n4. Circonférence d'un cercle avec son diamètre\n5. Rayon d'un cercle avec sa circonférence\n6. Diamètre d'un cercle avec sa circonférence\n7. Aire d'un polygone régulier\n8. Circonférence d'un cercle avec son aire\n9. Rayon d'un cercle avec son aire\n10. Diamètre d'un cercle avec son aire\n11. Addition\n12. Soustraction\n13. Multiplication\n14. Division\n15. Racine carrée d'un nombre\n")
if choix == "1":
    r = float(input("Quel est le rayon du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    airecerclerayon(r)
elif choix == "2":
    d = float(input("Quel est le diamètre du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    airecerclediametre(d)
elif choix == "3":
    r = float(input("Quel est le rayon du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    circonferencecerclerayon(r)
elif choix == "4":
    d = float(input("Quel est le diamètre du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    circonferencecerclediametre(d)
elif choix == "5":
    C = float(input("Quelle est la circonférence du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    rayoncercle(C)
elif choix == "6":
    C = float(input("Quelle est la circonférence du cercle?\n"))
    print("\nLe résultat de l'opération est:")
    diametrecercle(C)
elif choix == "7":
    c = float(input("Quelle est la mesure du côté du polygone?\n"))
    a = float(input("Quelle est la mesure de l'apothème du polygone?\n"))
    n = float(input("Quel est le nombre de côtés du polygone?\n"))
    print("Le résultat est:")
    airepolygoneregulier(c, a, n)
elif choix == "8":
    A = float(input("Quelle est l'aire du cercle?\n"))
    print("Le résultat de l'opération est:")
    circonferencecercleaire(A)
elif choix == "9":
    A = float(input("Quelle est l'aire du cercle?\n"))
    print("Le résultat de l'opération est:")
    rayoncercleaire(A)
elif choix == "10":
    A = float(input("Quelle est l'aire du cercle?\n"))
    print("Le résultat de l'opération est:")
    diametrecercleaire(A)
elif choix == "11":
    nb1 = float(input("Quel est le premier nombre de l'équation?\n"))
    nb2 = float(input("Quel est le deuxième nombre de l'équation?\n"))
    print("Le résultat de l'opération est:")
    addition(nb1, nb2)
elif choix == "12":
    nb1 = float(input("Quel est le premier nombre de l'équation?\n"))
    nb2 = float(input("Quel est le deuxième nombre de l'équation?\n"))
    print("Le résultat de l'opération est:")
    soustraction(nb1, nb2)
elif choix == "13":
    nb1 = float(input("Quel est le premier nombre de l'équation?\n"))
    nb2 = float(input("Quel est le deuxième nombre de l'équation?\n"))
    print("Le résultat de l'opération est:")
    multiplication(nb1, nb2)
elif choix == "14":
    nb1 = float(input("Quel est le premier nombre de l'équation?\n"))
    nb2 = float(input("Quel est le deuxième nombre de l'équation?\n"))
    print("Le résultat de l'opération est:")
    division(nb1, nb2)
elif choix == "15":
    n = float(input("Quel est le nombre dont la racine carrée doit être trouvée?\n"))
    print("Le résultat de l'opération est:")
    racinecarree(n)