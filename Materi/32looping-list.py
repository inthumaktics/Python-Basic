# LOOPING DARI LIST 

# for loop 
print("\n FOR LOOP")
kumpulan_angka = [4, 3, 5, 6, 7, 8]

for angka in kumpulan_angka :
    print(f"angka = {angka}")

peserta = ["Erika", "cipi", "meta", "gemi", "bebox"]

for nama in peserta :
    print(f"nama = {nama}")


# for loop dan range

print("\n FOR LOOP AND RANGE")
kumpulan_angka = [4, 3, 5, 6, 7, 8]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f" angka = {kumpulan_angka}")


# while
print("\n WHILE LOOP")
kumpulan_angka = [4, 3, 5, 6, 7, 8]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension 
print("\n LIST COMPREHENSION")
data = ["cipi", 1,2,3, "gemi"]

[print(f" data ={i}") for i in data]

angka = [4, 3, 5, 6, 7, 8]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\n ENUMERATE")
data_list = ["cipi", 1,2,3, "gemi"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")