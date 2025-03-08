# a = 20, a adalah variabel dengan nilai 20

# TIPE DATA
#1.  INTEGER : Angka satuan yang tidak ada komanya
data_integer = 15
print('data :', data_integer)
print('bertipe :', type(data_integer))

#2. FLOAT : Angka dengan koma
data_float = 20.5
print('data :', data_float)
print('bertipe :', type(data_float))

#3. STRING : Kumpulan karakter 
data_string = 'Erika sedang belajar python'
print('data :',data_string)
print('bertipe :', type(data_string))

#4. BOOLEAN : Binner True or False
data_bool = True
print('data :', data_bool)
print('bertipe :', type(data_bool))

# TIPE DATA KHUSUS
#1. COMPLEX : Bilangan Kompleks
data_complex = complex(10,8)
print('data :', data_complex)
print('bertipe :', type(data_complex))

#2. Tipe Data Dari Bahasa C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(45.2)
print('data :', data_c_double)
print('bertipe :', type(data_c_double))