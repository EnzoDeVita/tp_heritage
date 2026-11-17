class Batiment:
    def __init__(self, nb_etages, adresse,):
        
        self.nb_etages = nb_etages
        self.adresse = adresse
        print("Bienvenue dans la ville de Logre")


    def get_nb_etages(self):
        return self.nb_etages

    def get_adresse(self):
        return self.adresse

class Immeuble(Batiment):
    def __init__(self, adresse, nb_etages, nb_balcons):
        super().__init__(adresse, nb_etages)
        self.nb_balcons = nb_balcons

    def get_nb_balcons(self):
        return self.nb_balcons

class Market(Batiment):
    def __init__(self, nb_etages, adresse, nb_rayons):
        super().__init__(nb_etages, adresse)
        self.nb_rayons = nb_rayons

    def get_nb_rayons(self):
        return self.get_nb_rayons

class Banque(Batiment):
    def __init__(self, adresse, nb_etages, pseudo, nb_coffres):
        super().__init__(nb_etages, adresse)
        self.pseudo = pseudo
        self.nb_coffres = nb_coffres

    def get_pseudo(self):
        return self.pseudo

    def get_nb_coffres(self):
        return self.nb_coffres

    


Immeuble = Immeuble(4, "25 rue des peupliers", 5)
Immeuble2 = Immeuble()
Immeuble3 = Immeuble()
Immeuble4 = Immeuble()
