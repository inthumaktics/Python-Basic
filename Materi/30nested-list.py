## LIST BERSARANG

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4,5]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1]
print(f"list 2D = {list_2D}")

# contoh penggunaan 
peserta_0 = ["Erika", 20, "cewe"]
peserta_1 = ["Arya", 21, "cowo"]
peserta_2 = ["Arka", 1, "cowo"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")
