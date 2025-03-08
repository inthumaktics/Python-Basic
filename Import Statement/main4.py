import sains.math
from sains import fisika
from sains.fisika import gaya as F

hasil_tambah = sains.math.tambah(2, 2, 2, 2, 2)
print(f"Hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(20, 5)
print(f"Gaya adalah = {gaya}")

gaya = F(20, 5)
print(f" Gaya adalah = {gaya}")

