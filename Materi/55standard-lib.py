import datetime

data_waktu = datetime.datetime.now()
print(f"date time now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ['a', 'b', 'c', 'd', 'a', 'c', 'c', 'd', 'a', 'a']
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

import io
file = io.open("teks coba.txt", 'r')
print(file.read())