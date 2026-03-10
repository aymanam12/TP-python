
contacts = ["Bouchra", "Ahmed", "Sara"]
continuer = True
while continuer:
    print("\n--- MENU CARNET D'ADRESSES ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")
    
    choix = input("Votre choix (1/2/3) : ")
    if choix == "1":
        nouveau_nom = input("Entrez le nom du nouveau contact : ")
        contacts.append(nouveau_nom)
        print(f"{nouveau_nom} a été ajouté avec succès !")

    elif choix == "2":
        print("\nListe de vos contacts :")
        for index, nom in enumerate(contacts, start=1):
            print(f"{index}. {nom}")

    elif choix == "3":
        print("Au revoir !")
        continuer = False 

    else:
        print("Choix invalide, veuillez recommencer.")