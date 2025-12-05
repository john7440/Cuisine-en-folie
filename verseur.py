import threading
import time
import copy
from commis import Commis
from recipient import Recipient

class Verseur(Commis):
    """
    Commis chargé de verser le contenu d'un récipient source
    dans un récipient cible à un certain rythme
    """
    lock = threading.Lock()

    def __init__(self, recipient_source: Recipient, recipient_target: Recipient, portions: int, name: str, tempo: float = 1.0):
        super().__init__(name)
        self.recipient_source = recipient_source
        self.recipient_target = recipient_target
        self.portions = portions
        self.tempo = tempo

    def run(self):
        with Verseur.lock:
            for i in range(1, self.portions + 1):
                print(
                    f"{self.name}: je verse la portion {i}/{self.portions} de '{self.recipient_source.name}' vers '{self.recipient_target.name}'"
                )
                time.sleep(self.tempo)

            #on fait une copie du contenu
            transferred_content = copy.deepcopy(self.recipient_source.content)

            # fusion automatique
            if transferred_content is not None:
                self.recipient_target.add_content(transferred_content)

            self.recipient_source.content = None

            print(
                f"Transfert terminé, '{self.recipient_target.name}' contient désormais {self.recipient_target.describe()}"
            )


class VerseurSansLock(Commis):
    def __init__(self, recipient_source: Recipient, recipient_target: Recipient, portions: int, name: str, tempo: float = 1.0):
        super().__init__(name)
        self.recipient_source = recipient_source
        self.recipient_target = recipient_target
        self.portions = portions
        self.tempo = tempo

    def run(self):
        for i in range(1, self.portions + 1):
            print(f"{self.name}: portion {i}/{self.portions}")
            time.sleep(self.tempo)

        transferred_content = copy.deepcopy(self.recipient_source.content)
        if transferred_content is not None:
            self.recipient_target.add_content(transferred_content)
        self.recipient_source.content = None
        print(f"{self.name}: transfert terminé → {self.recipient_target.describe()}")
