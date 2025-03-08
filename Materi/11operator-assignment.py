# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

##OPERATOR ARITMATIKA

a = 10 # adalah assignment
print('nilai a =', a)

# pertambahan
a += 1 #artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi', a)

# pengurangan
a -= 3 #artinya adalah a = a - 3
print('nilai a -= 3, nilai a menjadi', a)

#perkalian
a *= 2 #artinya adalah a = a * 2
print('nilai a *= 2, nilai a menjadi', a)

# pembagian
a /= 2 #artinya adalah a = a / 2
print ('nilai a /= 2, nilai a menjadi', a)

# modulus dan floor division
b = 15
print('\n nilai b =', b)

b %= 3
print ('nilai b %= 3, nilai b menjadi', b)

b //= 5
print ('nilai b //= 5, nilai b menjadi', b)

# pangkat atau eksponen
a = 5
print('\n nilai a =', a)
a **= 2
print('nilai a **= 2,  nilai a menjadi', a)

##OPERATOR BITWISE
# OR
c = True
print('nilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi ', c)
c = False
print('nilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi ', c)

# AND
c = True
print('nilai c =', c)
c &= False
print('nilai c &= False, nilai c menjadi ', c)
c = True
print('nilai c =', c)
c &= True
print('nilai c &= False, nilai c menjadi ', c)

# XOR
c = True
print('nilai c =', c)
c ^= False
print('nilai c ^= False, nilai c menjadi ', c)
c = True
print('nilai c =', c)
c ^= True
print('nilai c ^= False, nilai c menjadi ', c)

# geser-geser
d = 0b0100
print('nilai d =', format(d, '04b'))

d >>= 2
print('nilai d >>= 2, nilai menjadi', format(d, '04b'))

d <<= 1
print('nilai d <<= 1, nilai menjadi', format(d, '04b'))

