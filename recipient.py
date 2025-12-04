from dataclasses import dataclass
from typing import Union

from appareil import Appareil
from ingredient import Ingredient


@dataclass
class Recipient:
    name: str
    content : Union[Ingredient, Appareil, None] = None

    def desccribe(self):
        if self.content is None:
            return f"Recipient {self.name} est vide!"
        else:
            return f"Recipient {self.name} contiens: {self.content}"