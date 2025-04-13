import json
import random

names = ["Marita", 
         "Huanyu", 
         "Pit", 
         "Ricardo",
         "Mariana",
         "Gabriel",
         "Secil",
         "Valentino",
         "Riaz",
         "Nestor",]

random.shuffle(names)
pairing = {}

for i in range(len(names)):
    pairing[names[i]] = names[(i + 1) % len(names)]

save_to_file = "./data/name_picker.json"

# Save to file
with open(save_to_file, "w") as f:
    json.dump(pairing, f)

print(f"Pairs have been made and saved to {save_to_file}!")
