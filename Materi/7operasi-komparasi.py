# OPERASI KOMPARASI
#Setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 10
b = 5

# 1. Lebih besar dari (>)
print('=====LEBIH BESAR DARI (>)=====')

hasil = a > 5
print(a, '>', 5, '=', hasil)
hasil = b > 5
print(b, '>', 5, '=', hasil)
hasil = b > 4
print(b, '>', 2, '=', hasil)

# 2. Kurang dari (<)
print('=====KURANG DARI (<)=====')

hasil = a < 5
print(a, '<', 5, '=', hasil)
hasil = b < 5
print(b, '<', 5, '=', hasil)
hasil = b < 4 
print(b, '<', 4, '=', hasil)

# 3. Lebih dari sama dengan (>=)
print('=====LEBIH DARI SAMA DENGAN (>=)=====')

hasil = a >= 5
print(a, '>=', 5, '=', hasil)
hasil = b >= 5
print(b, '>=', 5, '=', hasil)
hasil = b >=4
print(b, '>=', 4, '=', hasil)

# 4. Kurang dari sama dengan (<=)
print('=====KURANG DARI SAMA DENGAN (<=)=====')

hasil = a <=5
print(a, '<=', 5, '=', hasil)
hasil = b <= 5
print(b, '<=', 5, '=', hasil)
hasil = b <=4
print(b, '<=', 4, '=', hasil)

# 5. Sama dengan (==)
print('=====SAMA DENGAN (==)=====')

hasil = a ==5
print(a, '==', 5, '=', hasil)
hasil = b == 5
print(b, '==', 5, '=', hasil)
hasil = b ==4
print(b, '==', 4, '=', hasil)

# 6. Tidak sama dengan (!=)
print('=====TIDAK SAMA DENGAN (!=)')

hasil = a !=5
print(a, '!=', 5, '=', hasil)
hasil = b != 5
print(b, '!=', 5, '=', hasil)
hasil = b !=4
print(b, '!=', 4, '=', hasil)


# 'is' sebagai komparasi object identity
print('=====OBJECT IDENTITY (IS)=====')
x = 5 # ini adalah assignment membuat object 
y = 5
print('nilai x =', x, ',id =', hex(id(x)))
print('nilai y =', y, ',id =', hex(id(x)))
hasil = x is y
print('x is y =', hasil)


x = 5 # ini adalah assignment membuat object 
y = 6
print('nilai x =', x, ',id =', hex(id(x)))
print('nilai y =', y, ',id =', hex(id(x)))
hasil = x is y
print('x is y =', hasil)


# 'is not' sebagai komparasi object identity
print('=====OBJECT IDENTITY (IS NOT)=====')
x = 5 # ini adalah assignment membuat object 
y = 5
print('nilai x =', x, ',id =', hex(id(x)))
print('nilai y =', y, ',id =', hex(id(x)))
hasil = x is not y
print('x is y =', hasil)


x = 5 # ini adalah assignment membuat object 
y = 6
print('nilai x =', x, ',id =', hex(id(x)))
print('nilai y =', y, ',id =', hex(id(x)))
hasil = x is not y
print('x is y =', hasil)


