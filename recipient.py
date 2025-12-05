from dataclasses import dataclass, field
from typing import Union

from appareil import Appareil
from ingredient import Ingredient

@dataclass
class Recipient:
    name: str
    content: Union[Ingredient, Appareil, None] = None

    def describe(self):
        if self.content is None:
            return f"Recipient {self.name} est vide!"
        else:
            return f"Recipient {self.name} contient: {self.content}"

    def add_content(self, ingredient: Ingredient):
        #On ajoute un ingrédient en fusionnant si nécessaire
        if self.content is None:
            self.content = ingredient
        elif isinstance(self.content, Ingredient):
            self.content = self.content.merge(ingredient)
        elif isinstance(self.content, Appareil):
            self.content.ingredients.append(ingredient)
        else:
            self.content = ingredient