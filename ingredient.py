from abc import ABC
from appareil import Appareil

class Ingredient(ABC):
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f" {self.quantity}{self.unit} de {self.name}"

    def add_quantity(self, amount: float):
        #pour pouvoir ajouter une quantité
        self.quantity += amount

    def merge(self, other: "Ingredient"):
        """Fusionne avec un autre ingrédient."""
        if type(self) == type(other):
            self.add_quantity(other.quantity)
            return self
        else:
            return Appareil([self, other])

class Oeuf(Ingredient):
    def __init__(self, quantity: int):
        super().__init__(name="Oeuf", quantity=quantity, unit="pièce")

class Chocolat(Ingredient):
    def __init__(self, quantity: int):
        super().__init__(name="Chocolat", quantity=quantity, unit="g")
