from dataclasses import dataclass, field
from typing import List

from ingredient import Ingredient

@dataclass
class Appareil:
    name: str
    ingredients: List[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.ingredients.append(ingredient)
        print(f"Ingrédient ajouté: {ingredient.quantity}{ingredient.unit} de {ingredient.name}")

    def homogenize(self) -> None:
        # On simule l'action de rendre le mélange homogène
        print(f"Je mélange 'soigneusement' tous les ingrédients de l'appareil '{self.name}'...")
        print("Le mélange est homogène et prêt à être utilisé !")