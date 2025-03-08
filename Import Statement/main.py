# IMPORT 

# fungsinya adalah untuk mengambil
# program dari file external.py

##1. Untuk menyambung program dari external
import p_print
import print2

##2. Import dengan data
import var
import alpro

#data ada di namespace variabel
print(var.data)
print(alpro.data2)

##3. Import dengan fungsi
import matematika

hasil = matematika.tambah(10,10)
print(hasil)

import coba

### Module matematika dengan import
import matematika

hasil_tambah = matematika.tambah(10, 5, 10, 5, 10, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = matematika.kali(2, 2, 2, 2)
print(f"Hasil tambah = {hasil_kali}")

pangkat_2 = matematika.pangkat(2)
print(f"Hasil pangkat 2 = {pangkat_2(2)}")