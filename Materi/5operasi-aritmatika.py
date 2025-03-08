# OPERASI ARITMATIKA

a = 20
b = 3
# 1. Penambahan (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# 2. Pengurangan (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# 3. Perkalian (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# 4. Pembagian (/)
hasil =  a / b
print(a, '/', b, '=', hasil)

# 5. Eksponen (**)
hasil = a ** b
print(a, '**', b, '=', hasil)

# 6. Modulus (%)
hasil = a % b
print(a, '%', b, '=', hasil)

# 7. Floor Divison (//)
hasil = a // b
print(a, '//', b, '=', hasil)

# PRIORITAS OPERASI 
'''
    1. ()
    2. Exponen (**)
    3. Perkalian, Pembagian (*, /)
    4. Modulus, Floor divison(%, //)
    5. Pertambahan, pengurangan (+, -)

'''

x = 10
y = 5
z = 2

hasil = x ** y * z + y / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, hasil)

# kurung akan mengambil langkah paling pertama
hasil = (x+y) * z
print('(', x, '+', y, ') *', z, '=', hasil)