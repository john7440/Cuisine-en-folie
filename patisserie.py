from commis import BatteurOeufs,FondeurChocolat
from ingredient import Chocolat, Oeuf
from recipient import Recipient
from verseur import Verseur, VerseurSansLock

def test_verseurs_sans_lock():
    culdepoule = Recipient("Cul de poule en carton", content=Oeuf(6))
    bol_chocolat1 = Recipient("Bol 1", content=Chocolat(200))
    bol_chocolat2 = Recipient("Bol 2", content=Chocolat(150))

    verseur1 = VerseurSansLock(bol_chocolat1, culdepoule, portions=3, name="Machin", tempo=0.5)
    verseur2 = VerseurSansLock(bol_chocolat2, culdepoule, portions=3, name="Bidule", tempo=0.5)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    print("\nRésultat final :", culdepoule.describe())

def main():
    # Récipients
    cul_de_poule = Recipient(name="Cul de poule en inox", content=Oeuf(6))
    bol_chocolat = Recipient(name="Bol", content=Chocolat(200))
    bol_inox = Recipient(name="Bol en inox", content=Chocolat(150))
    moule = Recipient(name="Petit moule")

    # Commis
    batteur = BatteurOeufs(cul_de_poule, nb_oeufs=6, name="Hannibale")
    fondeur1 = FondeurChocolat(bol_chocolat, quantite=200, name="Casimir")
    fondeur2 = FondeurChocolat(bol_inox, quantite=150, name="Tartenpion")

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
    verseur1 = Verseur(bol_chocolat, cul_de_poule, portions=3, name="Pignouf", tempo=0.5)
    verseur2 = Verseur(bol_inox, cul_de_poule, portions=3, name="HarryPotter", tempo=0.5)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    print("\nLe mélange oeufs + chocolat est prêt!")
    print("On peut maintenant le transvaser dans le petit moule\n")

    verseur_final = Verseur(cul_de_poule, moule, portions=4, name="Patatrack", tempo=0.7)
    verseur_final.start()
    verseur_final.join()

    print("\nLe petit moule est rempli, prêt à être enfourné dans un petit four !")

if __name__ == "__main__":
    #test_verseurs_sans_lock()
    main()
