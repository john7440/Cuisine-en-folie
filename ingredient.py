from abc import ABC

class Ingredient(ABC):
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
         return f"{self.quantity}{self.unit} de {self.name}"

class Oeuf(Ingredient):
    def __init__(self, quantity: int):
        super().__init__(name="Oeuf", quantity=quantity, unit="pièce")

class Chocolat(Ingredient):
    def __init__(self,quantity: int):
        super().__init__(name="Chocolat", quantity=quantity, unit="g")
