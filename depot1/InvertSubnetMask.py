# Définit le masque de sous-réseau (ici /24) sous forme d'un entier binaire littéral de 32 bits.
subnet_mask = 0b11111111111111111111111100000000

# Applique l'opérateur NOT (~) pour inverser les bits : les 1 deviennent 0 et inversement, créant la valeur brute du wildcard.
wildcard_mask = ~subnet_mask

# Force le résultat sur 32 bits via un ET logique avec 0xFFFFFFFF pour éliminer le signe négatif de l'inversion Python,
# convertit en chaîne binaire via bin(), retire le préfixe '0b' avec le slicing [2:], et complète à gauche par des zéros.
wildcard_mask = bin(wildcard_mask & 0xFFFFFFFF)[2:].zfill(32)

# Initialise une liste vide destinée à stocker les quatre octets du masque en format textuel.
list_mask = []

# Extrait les 8 premiers bits, les convertit de la base 2 vers l'entier, puis en chaîne de caractères pour l'ajouter à la liste.
list_mask.append(format(int(wildcard_mask[0:8], 2)))
# Extrait les bits 8 à 16 (deuxième octet), effectue la conversion de type et l'ajoute à la liste.
list_mask.append(format(int(wildcard_mask[8:16], 2)))
# Extrait les bits 16 à 24 (troisième octet), effectue la conversion de type et l'ajoute à la liste.
list_mask.append(format(int(wildcard_mask[16:24], 2)))
# Extrait les 8 derniers bits (quatrième octet), effectue la conversion de type et l'ajoute à la liste.
list_mask.append(format(int(wildcard_mask[24:32], 2)))

# Agrège les éléments de 'list_mask' en une seule chaîne de caractères, en utilisant le point comme séparateur (ex: "0.0.0.255").
ip_addr = '.'.join(list_mask)

# Affiche la liste finale contenant les quatre octets sous forme de chaînes de caractères décimales.
print(list_mask)
