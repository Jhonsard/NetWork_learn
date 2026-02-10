class AdressIP:
    def __init__(self, ip: str):
        self.ip = ip

    def binary_trans(self):
        pass

class Utilisateur:
    """Classe permetant de gerer les utilisateurs
    """

    nombre_utilisateurs = 0
    def __init__(self, nom: str, ip:str, status_connexion: bool):
        """Constructeur machin tou ca

        Args:
            nom (str): nom de l'utilisateur
            ip (str): l'adresse ip de l'utilisateur
            status_connexion (bool): l'etat de sa connection
        """
        self.nom = nom
        self.ip = AdressIP(ip)
        self.statuts = status_connexion
        self.__password = "myPass" # Variable priver
        Utilisateur.nombre_utilisateurs += 1

    def __str__(self):
        return f"Utilisateur : {self.nom}, IP : {self.ip.ip}, Statuts : {self.statuts}"

    def afficher_details(self):
        print(f"Utilisateur : {self.nom}, IP : {self.ip.ip}, Statuts : {self.statuts}")

    @classmethod
    def afficher_nombre_utilisateur(cls):
        print(f"Nombre total d'utilisateurs: {cls.nombre_utilisateurs} ")

    @staticmethod
    def afficher_bienvenu():
        print("Bienvenue dans le systemme de gestion d'utilisateur")


# Instantion la classe.
alice = Utilisateur("Alice", "192.168.12.1", True)
aboubakar = Utilisateur("Aboubakar", "192.168.10.2", False)

"""Utilisateur.afficher_bienvenu()
alice.afficher_details()
aboubakar.afficher_details()
Utilisateur.afficher_nombre_utilisateur()"""

print(alice)
print(aboubakar)
