from abc import ABC

class Ingredient(ABC):
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

class Oeuf(Ingredient):
    def __init__(self, name, quantity, unit):
        Ingredient.__init__(self, name, quantity, unit)

class Chocolat(Ingredient):
    def __init__(self, name, quantity, unit):
        Ingredient.__init__(self, name, quantity, unit)
