import math
import threading
from abc import ABC, abstractmethod
import time

from recipient import Recipient


class Commis(threading.Thread, ABC):
    """
    Classe abstraite représentant un commis de cuisine
    Chaque commis est un thread qui exécute une tâche spécifique
    (battre des œufs, fondre du chocolat, etc.)
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    @abstractmethod
    def run(self):
        """
        Méthode abstraite qui contient la logique de la tâche à exécuter
        """
        pass


class BatteurOeufs(Commis):
    def __init__(self, recipient: Recipient, nb_oeufs, name):
        super().__init__(name)
        self.recipient = recipient
        self.nb_oeufs = nb_oeufs

    def run(self):
        # on suppose qu'il faut 8 tours de batteur par œuf présent dans le bol
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.name}:Je bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur

class FondeurChocolat(Commis):
    lock = threading.Lock()

    def __init__(self, recipient: Recipient, quantite, name):
        super().__init__(name)
        self.recipient = recipient
        self.quantite = quantite  # en grammes

    def run(self):
        with FondeurChocolat.lock:
            print(f"{self.name}: Je mets de l'eau à chauffer dans une bouilloire")
            time.sleep(3)
            print(f"{self.name}: Je verse l'eau dans une casserole")
            time.sleep(2)
            print(f"{self.name}: J'y pose le bol rempli de chocolat")
            time.sleep(1)

            nb_tours = math.ceil(self.quantite / 10)
            for no_tour in range(1, nb_tours + 1):
                print(f"{self.name}: Je mélange {self.quantite}g de chocolat à fondre, tour n°{no_tour}")
                time.sleep(1)

            print(f"{self.name}: Chocolat fondu terminé dans {self.recipient.name}\n")

