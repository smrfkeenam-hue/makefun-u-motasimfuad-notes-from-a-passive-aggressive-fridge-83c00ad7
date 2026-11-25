import os

# A smart fridge's door-screen note: smug sensor log, petty grudge,
# and one concrete witness (the yogurt) for the sting.
ENTRY = "Door alarm log, 3:12 a.m.: you opened me just to stare at the light. The yogurt saw it too. We are both disappointed."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = out_dir + "/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
