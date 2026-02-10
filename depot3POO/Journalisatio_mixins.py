class JournalisatioMixins:
    def Journalisation(self, message):
        print(f"[journal] {message}")

class PareFeu:
    def filtrer_paquets(self):
        print("filtrage paquets en cours")

class PareFeuJournal(PareFeu, JournalisatioMixins):
    def filtrer_paquets(self):
        self.Journalisation("fitrage des paquets")
        super().filtrer_paquets()
        self.Journalisation("Filtrage des paquets Terminer")

journal = PareFeuJournal()
journal.filtrer_paquets()