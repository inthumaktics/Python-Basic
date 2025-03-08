#OPERASI LOGIKA ATAU BOOLEAN
# not, or, and, xor

# NOT
print('=====NOT=====')
a = False
c = not a
print('data a =', a)
print('-----NOT-----')
print('data c =', c)

# OR (Jika salah satu True, maka hasilnya adalah True)
print('=====OR=====')
a = False
b = False 
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)

a = True
b = False
c = a or b
print(a, 'OR', b, ' =', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '  =', c)


# AND (Jika dua buah nilai True, maka hasilnya True)
print('=====AND=====')
a = False
b = False 
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)

a = True
b = False
c = a and b
print(a, 'AND', b, ' =', c)

a = True
b = True
c = a and b
print(a, 'AND', b, ' =', c)

# XOR (Akan True jika salah satu True, sisanya False)
print('=====XOR=====')
a = False
b = False 
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, ' =', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
