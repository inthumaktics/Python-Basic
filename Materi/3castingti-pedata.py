# CASTING TIPE DATA : merubah dari satu tipe ke tipe lain 
# Tipe data : int, float, str, bool

### INTEGER 
print('=====================INTEGER===========================')
data_int = 12;
print('data =', data_int, ',type =', type(data_int))

print('-------------------------------')

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print('data =', data_float, ', type =', type(data_float))
print('data =', data_str, ', type =', type(data_str))
print('data =', data_bool, ', type =', type(data_bool)) #akan false jika nilai int = 0

### FLOAT 
print('======================FLOAT=========================')
data_float = 15.5;
print('data =', data_float, ', type =', type(data_float))

print('-------------------------------')

data_int  = int(data_float) #akan dibulatkan ke bawah
data_str  = str(data_float)
data_bool = bool(data_float)
print('data =', data_int, ', type =', type(data_int))
print('data =', data_str, ', type =', type(data_str))
print('data =', data_bool, ', type =', type(data_bool)) #akan false jika nilai float = 0

### BOOLEAN
print('=====================BOOLEAN===============================')
data_bool = True;
print('data =', data_bool, ', type =', type(data_bool))

print('-------------------------------')

data_int   = int(data_bool)
data_float = float(data_bool)
data_str   = str(data_bool)
print('data =', data_int, ', type =', type(data_int))
print('data =', data_float, ', type =', type(data_float))
print('data =', data_str, ',type =', type(data_str))

### STRING
print('=====================STRING===============================')
data_str = '50';
print('data =', data_str, ', type =', type(data_str))

print('-------------------------------')

data_int   = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool  = bool(data_str) #false jika string kosong
print('data =', data_int, ',type =', type(data_int))
print('data =', data_float, ', type =', type(data_float))
print('data =', data_bool, ', type =', type(data_bool))


