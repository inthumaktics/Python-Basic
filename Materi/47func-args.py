'''*args'''

# memasukkan data/argument

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Neji", 172, 60)

def fungsi(data_list):
    data = data_list
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Eren", 180, 75])

# kenalan dengan *args :

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Sung Jin-woo", 175, 75)

# Studi Kasus 

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data :
        output += angka
    return output

hasil = tambah(20, 25, 10, 5, 5, 5, 10)
print(f"hasil = {hasil}")

hasil = tambah(10, 10, 10)
print(f"hasil = {hasil}")