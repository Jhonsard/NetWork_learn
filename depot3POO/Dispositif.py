class DispositifReseau:
    def __init__(self, nom: str, ip:str):
        self.nom = nom
        self.ip = ip

    def afficher_details(self, **kwargs:str):
        aditionnal_value = ""
        for key, value in kwargs.items():
            aditionnal_value += f"{key} : {value}"
        print(f"Nom du dispositif : {self.nom}, IP : {self.ip} Additionnal values {aditionnal_value}")
    
class Routeur(DispositifReseau):
    def __init__(self, nom: str, ip: str, versio_os:str):
        super().__init__(nom, ip)
        self.version = versio_os

    def afficher_details(self): # type: ignore
        super().afficher_details(version=self.version)

router = Routeur("Routeur1", "192.168.10.1", "IOS 15.1")
router.afficher_details()