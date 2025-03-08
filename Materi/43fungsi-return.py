'''FUNGSI DENGAN KEMBALIAN (RETURN)'''

# template fungsi dengan kembalian (return)
# def nama_fungsi(argument) :
#       badan fungsi
#       return output

### FUNGSI KUADRAT 

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(10)
print(y)

print(kuadrat(5))

z = 10 + kuadrat(7)
print(z)

### FUNGSI TAMBAH

def fungsi_tambah(angka1, angka2):
    '''Fungsi return dengan multi input'''
    return angka1 + angka2

hasil = fungsi_tambah(100, 25)
print(hasil)

### FUNGSI DENGAN RETURN BANYAK 

def operasi_math(angka1, angka2) :
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

o, p, q, r = operasi_math(20, 5)

print(f"Hasil tambah = {o}")
print(f"Hasil kurang = {p}")
print(f"Hasil kali = {q}")
print(f"Hasil bagi = {r}")
