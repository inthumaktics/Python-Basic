# INPUT USER

# data yang dimasukkan pasti string
data = input('Masukkan data :')
print('data =', data, ',type =', type(data))

#Jika ingin mengambil int, maka :
angka1 = int(input('Masukkan angka ke-1 :'))
angka2 = float(input('Masukkan angka ke-2 :'))

print('hasil =', angka1*angka2) #tambahanku aja :)

print('data =', angka1, ',type =', type(angka1))
print('data =', angka2, ',type =', type(angka2))

#Jika dengan boolean, maka :
biner = bool(int(input('Masukkan nilai boolean :'))) #casting integer, jadi inputnya harus angka
print('data =', biner, ', type =', type(biner))
