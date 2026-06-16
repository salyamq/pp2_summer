import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 75)
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn    = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu   = attrs["mtu"]

    print(f"{dn} {descr}                               {speed} {mtu}")



