from dataclasses import dataclass, field

@dataclass
class Appareil:
    """Représente un mélange d’ingrédients"""
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        noms = " + ".join(str(i) for i in self.ingredients)
        return f"Appareil ({noms})"