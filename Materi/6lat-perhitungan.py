#LATIHAN KONVERSI SATUAN TEMPERATUR

#A. PROGRAM KONVERSI CELCIUS KE SATUAN LAIN
print('\nPROGRAM KONVERSI TEMPERATUR\n')

print('======CELCIUS======')
celcius = float(input('Masukkan suhu dalam celcius :'))
print('Suhu adalah :', celcius, '°C')

#1. REAMUR
reamur = (4/5) * celcius
print('Suhu dalam reamur adalah :', reamur, '°R')

#2. FAHRENHEIT
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam fahrenheit adalah :', fahrenheit, '°F')

#3. KELVIN
kelvin = celcius + 273
print('Suhu dalam kelvin adalah :', kelvin, '°K')

#B. PROGRAM KONVERSI REAMUR KE SATUAN LAIN
print('======REAMUR======')

reamur = float(input('Masukkan suhu dalam reamur :'))
print('Suhu dalam reamur adalah :', reamur, '°R')

#1. CELCIUS
celcius = (5/4) * reamur
print('Suhu dalam celcius adalah :', celcius, '°C')

#2. FAHRENHEIT
fahrenheit = ((5/9) * reamur) + 32
print('Suhu dalam fahrenheit adalah :', fahrenheit, '°F')

#3. KELVIN 
kelvin = ((5/4) * reamur) + 273
print('Suhu dalam kelvin adalah :', kelvin, '°K')

#C. PROGRAM KONVERSI FAHRENHEIT KE SATUAN LAIN
print('======FAHRENHEIT======')

fahrenheit = float(input('Masukkan suhu dalam fahrenheit :'))
print('Suhu dalam fahrenheit adalah :', fahrenheit, '°F')

#1. CELCIUS
celcius = (5/9) * (fahrenheit - 32)
print('Suhu dalam celcius adalah :', celcius, '°C')

#2. REAMUR
reamur = (4/9) * (fahrenheit - 32)
print('Suhu dalam reamur adalah :', reamur, '°R')

#3. KELVIN
kelvin = (fahrenheit - 32) * (5/9) + 273
print('Suhu dalam kelvin adalah :', kelvin, '°K')


#D. PROGRAM KONVERSI KELVIN KE SARUAN LAIN
print('======KELVIN======')

kelvin = float(input('Masukkan suhu dalam kelvin :'))
print('Suhu dalam kelvin adalah :', kelvin, '°K')

#1. CELCIUS
celcius = kelvin - 273
print('Suhu dalam kelvin adalah :', kelvin, '°K')

#2. REAMUR
reamur = (4/5) * (kelvin - 273)
print('Suhu dalam reamur adalah :', reamur, '°R')

#3. FAHRENHEIT
fahrenheit = (kelvin - 273) * (9/5) + 32
print('Suhu dalam fahrenheit adalah :', fahrenheit, '°F')