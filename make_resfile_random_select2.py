import itertools
import re

data = [
  "39 H K--38 L D",
  "39 H D--38 L K",
  "39 H E--38 L K",
  "105 H K--43 L D",
  "105 H D--43 L K",
  "143 H D--124 L D",
  "179 H D--176 L K",
  "179 H K--176 L D",
  "161 H R--169 L D",
  "171 H K--131 L E,180 L E",
  "171 H E,143 H E--131 L K,180 L K",
  "183 H E,114 H A--137 L K",
  "164 H A,166 H G--135 L Y,176 L W",
  "141 H Q,179 H V--133 L T,176 L V",
  "141 H E,124 H A--133 L W",
  "181 H A--135 L W,137 L A"
]

for index, item in enumerate(data):
  with open(f"mutant_{index+1}.resfile", "w") as f:

    f.write("NATAA\nUSE_INPUT_SC\nEX 1 LEVEL 2\nEX 2 LEVEL 4\nEX_CUTOFF 2\nstart\n")

    parts = item.split("--")
    
    for part in parts:
      residues = part.split(",")
      for residue in residues:
        res_info = residue.strip().split(" ")
        
        res_num = res_info[0]
        chain = res_info[1]
        res_name = res_info[2]
        
        f.write(f"{res_num} {chain} PIKAA {res_name}\n")

    f.write("\n")

print("Resfiles generated successfully!")
