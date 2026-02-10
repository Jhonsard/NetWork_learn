"""This is a test file for binary operations.

"""

binary_values = bin(10)

byte = 0b1010
ip_address = "192.168.1.13"

octets = ip_address.split('.')
binary_array =[]

binary_array.append(format(int(octets[0]), '08b'))
binary_array.append(format(int(octets[1]), '08b'))
binary_array.append(format(int(octets[2]), '08b'))
binary_array.append(format(int(octets[3]), '08b'))

ip_bin = ''.join(binary_array) # joindre les éléments de la liste en une seule chaîne de caractères

octets_renv_list = []
octets_renv_list.append(ip_bin[0:8])
octets_renv_list.append(ip_bin[8:16])
octets_renv_list.append(ip_bin[16:24])
octets_renv_list.append(ip_bin[24:32])

# Convertir les octets binaires en décimal
octets_renv_list[0] = str(int(octets_renv_list[0], 2))
octets_renv_list[1] = str(int(octets_renv_list[1], 2))
octets_renv_list[2] = str(int(octets_renv_list[2], 2))
octets_renv_list[3] = str(int(octets_renv_list[3], 2))

ip_renv = '.'.join(octets_renv_list) # joindre les éléments de la liste en une seule chaîne de caractères

print()
print(ip_renv)