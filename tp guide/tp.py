from abc import ABC, abstractmethod
from dataclasses import dataclass
class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass
    def __add__(self, autre_boisson):
        class BoissonCombinee(Boisson):
            def __init__(self, b1, b2):
                self.b1 = b1
                self.b2 = b2
            def cout(self):
                return self.b1.cout() + self.b2.cout()
            def description(self):
                return self.b1.description() + " + " + self.b2.description()
        return BoissonCombinee(self, autre_boisson)

class Cafe(Boisson):
    def cout(self):
        return 2.0
    def description(self):
        return "Café simple"

class The(Boisson):
    def cout(self):
        return 1.5
    def description(self):
        return "Thé"

class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    def description(self):
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
    def description(self):
        return self._boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.7
    def description(self):
        return self._boisson.description() + ", Caramel"

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def calculer_prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher_commande(self):
        print(f"\n--- Commande de {self.client.nom} ---")
        for boisson in self.boissons:
            print(f"Commande: {boisson.description()}")
            print(f"Prix: {boisson.cout()}€")
        print(f"TOTAL: {self.calculer_prix_total()}€")

class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print("\n[Type: SUR PLACE]")
        super().afficher_commande()

class CommandeEmporter(Commande):
    def afficher_commande(self):
        print("\n[Type: À EMPORTER]")
        super().afficher_commande()

class Fidelite:
    def ajouter_points(self, client, montant):
        # Exemple : 10 points par euro dépensé
        points = int(montant * 10)
        client.points_fidelite += points
        print(f"> {points} points de fidélité ajoutés.")

class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        montant_total = self.calculer_prix_total()
        self.ajouter_points(self.client, montant_total)
        print(f"> Solde actuel de points pour {self.client.nom} : {self.client.points_fidelite}")

if __name__ == "__main__":
    client1 = Client("Aymane", 101)
    mon_cafe = Sucre(Lait(Cafe()))
    mon_the = Caramel(The())
    menu_combine = mon_cafe + mon_the
    commande = CommandeFidele(client1)
    commande.ajouter_boisson(mon_cafe)
    commande.ajouter_boisson(menu_combine)
    
    commande.afficher_commande()
    commande.valider_commande()