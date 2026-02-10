"""
    Test de filtrage des adresse ip avec startwith
    ips = ["192.168.1.1", "192.168.1.10", "192.168.1.15"]

ips = ["192.168.1.1", "192.168.1.10", "192.168.3.15"]

suspious_ip = [print(x+1,"Suspious ip found :",ip) for x,ip in enumerate(ips) if ip.startswith("192.168.1")]
    """



logs = [
    {
        "ip": "192.168.1.1",
        "status" : "success"
    },
    {
        "ip": "192.168.1.2",
        "status" : "failed"
    }
]

index = 0
while index < len(logs):
    insert = input("Entre l'address ip de login: ")
    log = logs[index]
    if insert in log["ip"] & log["status"] == "failed":
        print(logs["status"])
        break     