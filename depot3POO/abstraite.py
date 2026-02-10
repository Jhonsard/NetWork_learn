from abc import ABC, abstractmethod

class DispositifSecurity(ABC):
    """Classe abstraite representant un dispositif de securite reseau
    """

    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def activer(self):
        '''
        Methode abstraite pour activer le dispositif de securite
        '''
        pass

    @abstractmethod
    def desactiver(self):
        '''
        Methode abstraite pour desactiver le dispositif de securite
        '''
        pass

    def afficher_nom(self):
        return print(f"dispositif de securite : {self.nom}")

class Parefeu(DispositifSecurity):
    def __init__(self, nom):
        super().__init__(nom)


    def activer(self):
        return f"{self.nom} est activer"
    

    def desactiver(self):
        return f"{self.nom} est desactiver"
    
class IDs(DispositifSecurity):
     def __init__(self, nom):
         super().__init__(nom)

     def activer(self):
        return f"L'ids {self.nom} est activer"
    
     def desactiver(self):
        return f"L'ids {self.nom} est desactiver"
     
# Interface
class Interface(ABC):
    @abstractmethod
    def authentify(self,user, password):
        pass

class AuthentificationLDAP(Interface):
    def authentify(self, user, password):
        print("Authentification LDAP ")
    
parfeu = Parefeu("cisco_01")
ids = IDs("1024")

print(parfeu.afficher_nom())
print(parfeu.activer())
print()
print(ids.afficher_nom())
print(ids.activer())