# LOOPING DICTIONARY

daftar_nama = {
    "S":"Sung Jinwoo",
    "E":"Eren Yeager",
    "HN":"Hyuga Neji",
    "Itch":"Uchiha Itachi",
    "Uz":"Uzumaki Naruto"
}

# Looping first try ( yang keluar key-nya)

for nama in daftar_nama:
    print(nama)

# Operator untuk mengambil item / iterables
keys = daftar_nama.keys()
print(keys)

for key in daftar_nama.keys():
    print(daftar_nama.get(key))

values = daftar_nama.values()
print(values)

for value in daftar_nama.values():
    print(value)

items = daftar_nama.items()
print(items)

for item in daftar_nama.items():
    print(item)

for key,value in daftar_nama.items():
    print(f"key = {key}, value = {value}")
    