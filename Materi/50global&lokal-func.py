'''GLOBAL DAN LOCAL SCOPE'''

nama_global = "Sung jinwoo" #ini variabel global

# Akses variabel global dalam fungsi
def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")

fungsi1()

# Akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# Percabangan 
if True:
    print(f"if menampilakn {nama_global}")

## Variabel Local Scope 

def fungsi2():
    nama_local = "Eren Yeager" # <- variabel local scope

fungsi2()
# print(nama_local) #tidak bisa dilakukan

## CONTOH 1 : Penggunaan akses variabel
def sapa():
    print(f"Hello {nama}")

nama = "Neji"
sapa()

## CONTOH 2 : Merubah variabel global
angka = 0
name = 'Itachi'

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapatkan akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka, name}")
ubah(100, 'Kakashi')
print(f"Sesudah {angka, name}")

## CONTOH 3 :
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)