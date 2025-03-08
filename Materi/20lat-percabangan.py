#LATIHAN PERCABANGAN 

#Membuat kalkulator sederhana

print(20*"="+"Kalkulator sederhana"+"="*20)

angka_1 = float(input("Masukkan angka 1 ="))
operator = input("Masukkan operatornya (+,-,x,/) =")
angka_2 = float(input("Masukkan angka 2 ="))

#Percabangannya :
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah :{hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah :{hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah :{hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah :{hasil}")
else :
    print("Menurut lo???")

print(10*"-"+"Terima kasih sudah berkunjung!"+"-"*10)