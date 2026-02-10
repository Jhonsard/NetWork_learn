class SecurityParfeu:
    def fiter_ip(self):
        print("Filtrages d'ips en cours")

class IDs:
    def detecter_intrusion(self):
        print("Intrusion sur le reseau")

class PareFeu(SecurityParfeu, IDs):
    pass

parfeu = PareFeu()

parfeu.fiter_ip()
parfeu.detecter_intrusion()

