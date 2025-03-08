### OPERATOR LIST

data_angka = [1,5,7,8,9,2,3,5,6,3,4,5,5,9,8,6,8,9,0,2,3,5]
print(f"data angka = \n{data_angka}")

#1. Count data
jumlah_data_5 = data_angka.count(5)
jumlah_data_9 = data_angka.count(9)

print(f"jumlah angka 5 = {jumlah_data_5}")
print(f"jumlah data_angka 9 = {jumlah_data_9}")

#2. Ambil posisi data (index)

data_str = ["Erika", "Erika2", "Plummy", "Ester"]
print(f"data string = {data_str}")

index_plummy = data_str.index("Plummy")
index_Erika2 = data_str.index("Erika2")
print(f"Index dari plummy = {index_plummy}")
print(f"Index dari Erika 2 = {index_Erika2}")

#3. Mengurutkan List
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka setelah sort = \n{data_angka}")

print(f"data string sebelum sort = {data_str}")
data_str.sort()
print(f"data string setelah sort = {data_str}")

#4. Membalikkan list 
data_angka.reverse()
data_str.reverse()
print(f"data setelah reverse = \n {data_angka} \n{data_str}")

