# Surcharge des methodes
class AnalyseuPaquet:
    def analyse(self, paquet:str):
        print(paquet)

class AnalysePaquetHTTP(AnalyseuPaquet):
    # surcharge
    def analyse(self, paquet: str):
        if "HTTP" in paquet:
            print(f"Analyse http specifique du paquet : {paquet}")

        else:
            super().analyse(paquet)

analyser = AnalysePaquetHTTP() # pyright: ignore[reportCallIssue]

analyser.analyse("HTTP GET /index.html")
analyser.analyse("ICMP echo Request")