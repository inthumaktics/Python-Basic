# Copy Dictionary

daftar_nama = {
    "S":"Sung Jinwoo",
    "E":"Eren Yeager",
    "HN":"Hyuga Neji",
    "Itch":"Uciha Itachi",
    "IK":"Ishigami Senku"
}

husbu = daftar_nama

print(f"daftar_nama : {daftar_nama}\n")
print(f"husbu : {husbu}\n")

daftar_nama["Itch"] = "itachi akatsuki"
print(f"daftar_nama : {daftar_nama}\n")
print(f"husbu : {husbu}\n")

# pop Dictionary
dataE = husbu.pop("E")
print(f"daftar_nama : {daftar_nama}\n")
print(f"husbu : {husbu}\n")

# popitem Dictionary
dataterakhir = husbu.popitem()
print(f"data terakhir = {dataterakhir}\n")
print(f"husbu = {husbu}\n")