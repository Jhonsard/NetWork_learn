# Définition de deux adresses IP (IPv4) sous leur forme binaire entière de 32 bits.

ip1 = 0b11000000101010000000000100001101

ip2 = 0b11000000101010000000000100001110



# Application de l'opérateur XOR (^). 

# Chaque bit identique donne 0, chaque bit différent donne 1. 

# ip_diff contiendra la position exacte des bits qui diffèrent entre les deux adresses.

ip_diff = ip1 ^ ip2



# Définit la longueur du préfixe réseau (nombre de bits à 1).

cidr_prefix = 24 



# Décale le bit '1' de 24 positions vers la gauche. 

# Cela crée une valeur binaire composée d'un 1 suivi de 24 zéros.

value = 1 << cidr_prefix 



# En soustrayant 1, on transforme cette valeur en une suite de 24 bits à 1 (0b111...111).

# C'est une méthode mathématique élégante pour générer une série de bits actifs.

value2 = value - 1 



# Décale ces 24 bits vers la gauche pour les aligner sur le poids fort d'une adresse 32 bits.

# Le calcul (32 - 24) déplace les bits de 8 positions pour laisser la place à la partie "Hôte".

subnetmask_address = value2 << (32 - cidr_prefix)



# Conversion de l'entier résultant en sa représentation textuelle binaire.

subnetmask = bin(subnetmask_address)



# Affiche le masque final (255.255.255.0 en binaire).

print(subnetmask)



# Adresse IP source en format binaire.

ip_address = 0b11000000101010000000000100001101



# Décale l'adresse de 24 bits vers la droite pour placer le premier octet au poids faible.

value = ip_address >> 24 

# Applique un masque ET (AND) avec 0xFF (11111111) pour isoler strictement ces 8 bits.

value_isol = value & 0xFF



# Décale de 16 bits vers la droite pour amener le deuxième octet au poids faible.

value2 = ip_address >> 16 

# Isole le deuxième octet.

value2_isol = value2 & 0xFF 



# Décale de 8 bits vers la droite pour amener le troisième octet au poids faible.

value3 = ip_address >> 8

# Isole le troisième octet.

value3_isol = value3 & 0xFF 



# Pour le dernier octet, aucun décalage n'est nécessaire car il est déjà au poids faible.

# On applique simplement le masque 0xFF pour supprimer tout ce qui précède.

value4_isol = ip_address & 0xFF 



# Affiche la valeur décimale du dernier octet (ici 13).

print(value4_isol)
