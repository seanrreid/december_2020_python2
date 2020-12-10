# FOR LOOP

power_rangers = ["Jason", "Trini", "Billy", "Zack", "Kim"]

# FOR A SINGULAR ITEM FROM A LIST OF ITEMS
for ranger in power_rangers:
    print(ranger)

# Similar WHILE loop version
index = 0
ranger = ""

while index < len(power_rangers):
    ranger = power_rangers[index]
    print(ranger)
    index += 1