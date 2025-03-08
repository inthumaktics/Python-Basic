#FOR LOOP

# for kondisi :
#    aksi

#1. Dengan List

angka_list = [0,2,4,6,8,10]
print(angka_list)

for i in angka_list :
    print(f" i sekarang -->> {i}")

print("Selesai! \n")

#2. Dengan Range 
angka_range = range(2,10)

for i in angka_range:
    print(f"i sekarang -->> {i}")

print("Selesai! \n")

#3. Menggunakan string

data_str = "Saya keren!"

for i in data_str:
    print(i)

print("Selesai! \n")
