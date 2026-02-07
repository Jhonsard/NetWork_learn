""" Operateurs XOR

Detecter la differance entre deux addresse ip (Par exemple, la comparaison des addresse MAC pour des changements)

ip1 = 0b11000000101010000000000100001101
ip2 = 0b11000000101010000000000100001110
    """

ip1 = 0b11000000101010000000000100001101
ip2 = 0b11000000101010000000000100001110

ip_diff = ip1^ip2

#print(bin(ip_diff))

""" Generation rapide du masque de sous reseau avec decalage a gauche
    cidr_prefix = 24 # /24
    """
# operation sur 24 bites d'une adress ip.
cidr_prefix = 24 # /24
value = 1 << cidr_prefix # 0b1000000000000000000000000 = 16777216

value2 = value - 1 # c'est l'inverse de value

subnetmask_address = value2 << 32 - cidr_prefix
subnetmask = bin(subnetmask_address)

print(subnetmask) # 0b11111111111111111111111100000000 : voila notre address


""" Extraction des octets d'une address ip pour un affichage en decimal

    ip1 = 0b11000000101010000000000100001101
    """
ip_address = 0b11000000101010000000000100001101

value = ip_address >> 24 # pour le premier octets de 192
value_isol = value & 0xFF

value2 = ip_address >> 16 # pour le deuxieme octets 168
value2_isol = value2 & 0xFF # isole deuxiemme segment

value3 = ip_address >> 8
value3_isol = value3 & 0xFF # 1

value4_isol = ip_address & 0xFF # 13

print(value4_isol)





