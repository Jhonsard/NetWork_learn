# Surcharge des methodes
class AnalyseuPaquet:
    def analyse(self, paquet:str):
        print(paquet)

class AnalysePaquetHTTP(AnalyseuPaquet):
    def who_are_you(self):
        print("I'm an HTTP Analyser")
    # surcharge
    def analyse(self, paquet: str):
        if "HTTP" in paquet:
            print(f"Analyse http specifique du paquet : {paquet}")

        else:
            super().analyse(paquet)

class AnalysePaquetDNS(AnalyseuPaquet):
    def who_are_you(self):
        print("I'm an DNS Analyser")
    # surcharge
    def analyse(self, paquet: str):
        if "DNS" in paquet:
            print(f"Analyse dns specifique du paquet : {paquet}")

        else:
            super().analyse(paquet)

    
analyser = AnalysePaquetHTTP() # pyright: ignore[reportCallIssue]
analysers = [AnalysePaquetDNS(), AnalysePaquetHTTP()] # type: ignore

paquets = ["HTTP GET /index.html", "DNS Query", "ICMP echo Request"]

for analys in analysers:
    analys.who_are_you()
    for paquet in paquets:
        analys.analyse(paquet)

