nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
print("\nChoisissez une opération :")
print("1 : addition")
print("2 : soustraction")
print("3 : multiplication")
print("4 : division")

choix = input("Votre choix (1/2/3/4) : ")
if choix == "1":
    resultat = nombre1 + nombre2
    print(f"Résultat : {nombre1} + {nombre2} = {resultat}")

elif choix == "2":
    resultat = nombre1 - nombre2
    print(f"Résultat : {nombre1} - {nombre2} = {resultat}")

elif choix == "3":
    resultat = nombre1 * nombre2
    print(f"Résultat : {nombre1} * {nombre2} = {resultat}")

elif choix == "4":
    if nombre2 == 0:
        print("Erreur : La division par zéro est impossible.")
    else:
        resultat = nombre1 / nombre2
        print(f"Résultat : {nombre1} / {nombre2} = {resultat}")

else:
    print("Choix invalide.")