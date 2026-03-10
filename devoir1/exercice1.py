
saisie = input("Veuillez saisir votre âge : ")
age = int(saisie)
if age <= 12:
    message = "Vous êtes dans la catégorie : Enfant."
elif age <= 17:
    message = "Vous êtes dans la catégorie : Adolescent."
elif age <= 64:
    message = "Vous êtes dans la catégorie : Adulte."
else:
  message = "Vous êtes dans la catégorie : Senior."
print(message)