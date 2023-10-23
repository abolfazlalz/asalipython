names = ["Abolfazl", "Fatima", "Armin", "Aida", "y", "x"]
blocked = ["y", "x"]

for block in blocked:
    if block in names:
        print(block + " is blocked and you can't invite him")

# Dirty alternative
for block in blocked:
    for name in names:
        if name == block:
            print(block + " is blocked and you can't invite him")
