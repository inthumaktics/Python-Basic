'''LATIHAN FUNGSI'''
import os

#Program menghitung luas dan keliling persegi panjang

# Membuat header program

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# Mengambil input user
# lebar = int(input('Masukkan nilai lebar :'))
# panjang = int(input('MAsukkan nilai panjang :'))

# Program menghitung luas
# Luas = panjang * lebar
# Keliling = 2*(panjang + lebar)

# Tampilkan hasilnya
# print(f"Hasil perhitungan luas = {Luas}")
# print(f"Hasil perhitungan keliling = {Keliling}")

os.system("cls")

def header():
    '''Fungsi header'''
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user() :
    '''Fungsi input user'''
    lebar = int(input('Masukkan nilai lebar :'))
    panjang = int(input('MAsukkan nilai panjang :')) 
    return lebar, panjang   

def hitung_luas(lebar, panjang):
    '''Fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    '''Fungsi keliling'''
    return 2*(lebar+panjang)

def display(message, value):
    '''Fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")

### PROGRAM UTAMANYA
while True:
    header()
    lebar, panjang = input_user()
    luas = hitung_luas(lebar, panjang)
    keliling = hitung_keliling(lebar, panjang)

    display("Luasnya adalah :", luas)
    display("Kelilingnya adalah: ", keliling)

    lanjut = input("Apakah lanjut? (y/n)")
    if lanjut == "n":
        break

print('-'*40)
print("\nProgram ini telah selsai!, Terima Kasih!")