class ConfigurationFirewall:
    def __init__(self):
        self.regles = []


    def __getitem__(self, index:int):
        return self.regles[index]
    
    def __setitem__(self, index, valeur):
        self.regles[index] = valeur

    def ajouter_regle(self, regle):
        self.regles.append(regle)

config = ConfigurationFirewall()

config.ajouter_regle("ALLOW TCP 80")
config.ajouter_regle("DENY IP 192.168.1.1")

print(config[0])
