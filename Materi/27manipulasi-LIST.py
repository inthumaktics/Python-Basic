### MANIPULASI LIST

# index 0(-3)  1(-2)      2(-1)
data = ["Apa", "Siapa", "Kenapa", ]

# a. Mengambil data dari list
data_0 = data[0]
print(f"data pertama adalah = {data_0}")

data_last = data[-1]
print(f"data terakhir adalah = {data_last}")

data_ke2 = data[-2]
print(f"data tengah adalah {data_ke2}")

print(30*"-")

# b. mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

print(30*"-")

### MANIPULASI DATA LIST

#1. Menambah item pada list sesuai posisi
print(f"Data sebelum ditambahkan = \n{data}")

data.insert(2, "Dimana?")
print(f"data setelah ditambahkan = \n{data}")

print(30*"-")

#2. Menambah data di akhir list 
data.append("Kapan???")
print(f"Data ditambah diakhir = \n{data}")

print(30*"-")

#3. Menambah list dengan list
data_new = ["Entah", "Itu saja", "Gatau"]
data.extend(data_new)
print(f"data yang telah digabungkan = \n{data}")

print(30*"-")

#4. Merubah data
# Mengubah data 3 menjadi Berubah 
data[3] = "Berubah"
print(f"data yang telah di ubah = \n{data}")

print(30*"-")

#5. Meremove data
data.remove("Gatau")
print(f"data yang telah dihapus = \n{data}")

print(30*"-")

#6. Meremove data paling akhir
data_akhir = data.pop()
print(f"data akhirnya adalah = \n{data}")

print(data_akhir)

print(20*"="+"Sudah selesai!!!"+"="*20)