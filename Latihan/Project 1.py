'''KALKULATOR SEDERHANA '''
angka_1 = 0
angka_2 = 0
angka_1 = int(input("Masukkan angka pertama: "))
opr = input("Masukkan operator (+, -, *, /):")
angka_2 = int(input("Masukkan angka kedua : "))


if opr == '+':
    hasil = angka_1 + angka_2
    print(f"Hasil Penjumlahan: {angka_1} + {angka_2} = {hasil}")
elif opr == '-':
    hasil = angka_1 - angka_2
    print(f"Hasil Pengurangan: {angka_1} - {angka_2} = {hasil}")
elif opr == '*':
    hasil = angka_1 * angka_2
    print(f"Hasil Perkalian: {angka_1} * {angka_2} = {hasil}")
elif opr == '/':
    hasil = angka_1 / angka_2
    print(f"Hasil Pembagian: {angka_1} / {angka_2} = {hasil}")
else : 
    print("Salah input!")