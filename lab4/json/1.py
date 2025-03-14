import json


  


with open("sample.json", "r") as file:
    data = json.load(file)



for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "N/A"  
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(dn)
    print(description)
    print(speed)
    print(mtu)

