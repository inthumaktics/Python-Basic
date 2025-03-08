import datetime
import os
import string
import random

mahasiswa_template ={
    'nama':'nama_mahasiswa',
    'nim':'0000000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True : 
    os.system("cls")

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("_"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    #-------------------------------------------------------
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    tahun_lahir = int(input("Tahun Lahir (YYYY): "))
    bulan_lahir = int(input("Bulan Lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':^10} {'Nama':^25} {'NIM':^15} {'SKS Lulus':^10} {'Tanggal Lahir':^10}")

    for mahasiswa in data_mahasiswa :
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:^10} {NAMA:^25} {NIM:^15} {SKS:^10} {LAHIR:^10}")

    print("\n")
    is_done = input("Menambahkan data lagi? (y/n)")
    if is_done == "n":
        break

print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")