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

intbyte = int(local_ip_byte,2)
invertby= ~(intbyte)
invertbt= bin(invertby & 0xFFFFFFFF)[2:].zfill(32)

invertTable.append(format(int(invertbt[0:8],2)))
invertTable.append(format(int(invertbt[8:16],2)))
invertTable.append(format(int(invertbt[16:24],2)))
invertTable.append(format(int(invertbt[24:32],2)))

ip_inv = '.'.join(invertTable)

# partie mask de sous reseaux
table_mask = []
mask = "255.255.255.0"
bitmask = mask.split('.')
table_bytes_mask=[]

print(local_ip_byte)

for i in bitmask:
    ip = format(int(i), "08b")
    table_mask.append(ip)
    table_bytes_mask.append(format(int(ip,2)))

mask_tail = '0b'+''.join(table_mask)

# Determination d'une masque de sous reseaux qu'utilise notre ip address
convbytenet_table = []
network_addr_byte = bin(int(mask_tail, 2)&int(intbyte))
bytenet = network_addr_byte[2:].zfill(32)

convbytenet_table.append(str(int(bytenet[0:8],2)))
convbytenet_table.append(str(int(bytenet[8:16],2)))
convbytenet_table.append(str(int(bytenet[16:24],2)))
convbytenet_table.append(str(int(bytenet[24:32],2)))

network_addr = '.'.join(convbytenet_table)

print()
print("This is your local ip address : "+local_ip)
print()
print("This is your public ip address: "+ip_inv)
print()
print("This is your network address: " + network_addr)

