#BREAK 

#contoh 1 :
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -->> {angka}")

    if angka == 3:
        print("nice!")
        break
    print("Keren!")

print("End!!!")

#contoh 2 : 
data_int = int(input("Hitung sampai ="))

angka = 0

while True :
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("Nice!")
        break
    print("Okeee!")

print("Endddd!!!")