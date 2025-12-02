
class Ingredient():
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

class Oeuf(Ingredient):
    def __init__(self, name, quantity, unit):
        Ingredient.__init__(self, name, quantity, unit)

class Chocolate(Ingredient):
    def __init__(self, name, quantity, unit):
        Ingredient.__init__(self, name, quantity, unit)
