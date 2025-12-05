import threading
from abc import ABC, abstractmethod

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


