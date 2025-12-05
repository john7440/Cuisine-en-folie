import threading
import time
import math
from commis import Commis
from ingredient import Chocolat, Oeuf
from recipient import Recipient
from verseur import Verseur

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

def main():
    # Récipients
    culdepoule = Recipient(name="Cul de poule en inox", content=Oeuf(6))
    bol_chocolat1 = Recipient(name="Bol en verre", content=Chocolat(200))
    bol_chocolat2 = Recipient(name="Bol en inox", content=Chocolat(150))
    moule = Recipient(name="Moule en papier maché")

    # Commis
    batteur = BatteurOeufs(culdepoule, nb_oeufs=6, name="Hannibale")
    fondeur1 = FondeurChocolat(bol_chocolat1, quantite=200, name="Casimir")
    fondeur2 = FondeurChocolat(bol_chocolat2, quantite=150, name="Tartenpion")

    # Lancement en parallèle
    batteur.start()
    fondeur1.start()
    fondeur2.start()

    batteur.join()
    fondeur1.join()
    fondeur2.join()

    print("\nLes oeufs sont battus et les deux bols de chocolat sont fondus")
    print("On peut maintenant incorporer le chocolat aux oeufs\n")

    #les verseurs en simultané
    verseur1 = Verseur(bol_chocolat1, culdepoule, portions=3, name="Pignouf", tempo=0.5)
    verseur2 = Verseur(bol_chocolat2, culdepoule, portions=3, name="HarryPotter", tempo=0.5)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    print("\nLe mélange oeufs + chocolat est prêt!")
    print("On peut maintenant le transvaser dans le moule\n")

    verseur_final = Verseur(culdepoule, moule, portions=4, name="Patatrack", tempo=0.7)
    verseur_final.start()
    verseur_final.join()

    print("\nLe moule est rempli, prêt à être enfourné !")

if __name__ == "__main__":
    main()
