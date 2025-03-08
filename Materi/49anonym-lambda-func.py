# LAMBDA FUNCTION

def f_kuadrat(angka):
    return angka**2

print(f"Hasil fungsi kuadrat = {f_kuadrat(4)}")

# Contoh dengan lambda
# output = lambda argument : expression
kuadrat = lambda angka : angka**2
print(f"Hasil lambda kuadrat = {kuadrat(10)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil lambda pangkat {pangkat(3,2)}")

## Penggunaan
# Sorting untuk list biasa
data_list = ['Eren', 'Neji', 'Gojo', 'Jinwoo']
data_list.sort()
print(f"Sorted list = {data_list}")

# Sorting dipakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key = panjang_nama)
print(f"Sorted list by panjang = {data_list}")

# Sort pakai lambda
data_list = ["Eren", "Neji", "Gojo"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")

# Filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x<7, data_angka))
print(data_angka_baru)

# Kasus Genap 
data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(data_genap)

# Kasus Ganjil
data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))
print(data_ganjil)

# Kelipatan 3
data_3 = list(filter(lambda x:(x%3==0), data_angka))
print(data_3)

## ANONYMOUS FUNCTION
# Currying <-- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"Fungsi biasa = {data_hasil}")

# Dengan Currying menjadi : 
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"Pangkat 3 = {pangkat3(3)}")
print(f"Pangkat bebas =  {pangkat(4)(5)}")
