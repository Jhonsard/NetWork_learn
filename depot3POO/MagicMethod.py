class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def to_Binary(self):
        pass

    def __str__(self):
        return f"IP Adrress : {self.ip}"
    
    def __repr__(self):
        return f"Address IP ('{self.ip}')"
    
    def __eq__(self, other_ip: object) -> bool:
        return self.ip == other_ip
    
    # surcharge d'operateur
    def __lt__(self, other_ip:object):
        return self.convertir_in_int() < other_ip.convertir_in_int()

    def convertir_in_int(self):
        octets = map(int, self.ip.split("."))

        return (next(octets) << 24) + (next(octets) << 16) + (next(octets) << 8) + (next(octets))

ip1 = IPAddress("192.168.10.1")
ip2 = IPAddress("192.168.1.1")
ip3 = IPAddress("192.168.1.1")


print(ip1)
print()
print(repr(ip2))
print()
print(ip2 == ip3)
print()
print(ip1 > ip2)
print()
print(ip1 < ip3)