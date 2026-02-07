subnet_mask = 0b11111111111111111111111100000000

wildcard_mask = ~subnet_mask
wildcard_mask = bin(wildcard_mask&0xFFFFFFFF)[2:].zfill(32) # inversement de la mask de sous reseau : 00000000000000000000000011111111

list_mask = []

list_mask.append(format(int(wildcard_mask[0:8], 2)));list_mask.append(format(int(wildcard_mask[8:16], 2)))
list_mask.append(format(int(wildcard_mask[16:24], 2)));list_mask.append(format(int(wildcard_mask[24:32], 2)))

ip_addr = '.'.join(list_mask)



print(list_mask)