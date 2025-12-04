import time
from commis import Commis
from recipient import Recipient

class Verseur(Commis):
    """
    Commis chargé de verser le contenu d'un récipient source
    dans un récipient cible à un certain rythme.
    """

    def __init__(self, recipient_source: Recipient, recipient_target: Recipient, portions: int, name: str, tempo: float = 1.0):
        """
        :param recipient_source: récipient contenant le mélange ou ingrédient
        :param recipient_target: récipient dans lequel on verse
        :param portions: nombre de portions à verser
        :param name: nom du commis
        :param tempo: temps (en secondes) entre chaque portion
        """
        super().__init__(name)
        self.recipient_source = recipient_source
        self.recipient_target = recipient_target
        self.portions = portions
        self.tempo = tempo

    def run(self):
        for i in range(1, self.portions + 1):
            print(f"{self.name}: je verse la portion {i}/{self.portions} de '{self.recipient_source.name}' vers '{self.recipient_target.name}'")
            time.sleep(self.tempo)

        # Une fois terminé, on simule que le contenu est transféré
        self.recipient_target.content = self.recipient_source.content
        self.recipient_source.content = None
        print(f"{self.name}: transfert terminé, '{self.recipient_target.name}' contient désormais {self.recipient_target.content}")
