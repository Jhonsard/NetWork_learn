# partie address ip
ip = "192.168.1.13"
bitip = ip.split(".")
table_bytes =[]
table_ip = []
invertTable = []

for i in bitip:
    ip = format(int(i), '08b')
    table_ip.append(ip)
    table_bytes.append(format((int (ip, 2))))

local_ip = '.'.join(table_bytes)
local_ip_byte = ''.join(table_ip)

ip_address_in_int = int(local_ip_byte,2)
binary_ip_address= bin(ip_address_in_int & 0xFFFFFFFF)[2:].zfill(32)

# partie mask sous reseaux
table_mask = []
mask_address = "255.255.255.0"
bitmask = mask_address.split('.')
table_bytes_mask=[]

for i in bitmask:
    ip = format(int(i), "08b")
    table_mask.append(ip)
    table_bytes_mask.append(format(int(ip,2)))

mask_tail = ''.join(table_mask)
subnet_mask_byte = int(mask_tail,2)

# Partie broadcast
table_broadcast= []
subnet_cast = ~(subnet_mask_byte)

int_broadcast = (subnet_cast | ip_address_in_int) & 0xFFFFFFFF

binary_broadcast = bin(int_broadcast)[2:].zfill(32)

table_broadcast.append(str(int(binary_broadcast[0:8],2)))
table_broadcast.append(str(int(binary_broadcast[8:16],2)))
table_broadcast.append(str(int(binary_broadcast[16:24],2)))
table_broadcast.append(str(int(binary_broadcast[24:32],2)))

broadcast_address = ".".join(table_broadcast)
print(broadcast_address)