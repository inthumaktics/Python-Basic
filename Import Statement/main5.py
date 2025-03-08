import sains
from sains.bio import basic
from sains.bio import bioo
import sains.bio


hasil_tambah = sains.basic.tambah(10, 5, 10, 5, 10, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = sains.basic.kali(2, 2, 2, 2)
print(f"Hasil tambah = {hasil_kali}")

pangkat_2 = sains.basic.pangkat(2)
print(f"Hasil pangkat 2 = {pangkat_2(2)}")

hasil_fisika = sains.fisika.gaya(25, 5)
print(f"Hasil fisika ={hasil_fisika}")

hasil_bioo = bioo.gaya(10, 5)
print(f"Hasil bioo = {hasil_bioo}")