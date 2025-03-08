#LATIHAN LOGIKA DAN KOMPARASI 
# Membuat gabungan area rentang dari angka

### ++++++++++3----------10++++++++++
inputUser = float(input('Masukkan angka yang bernilai\n kurang dari 3 \n atau \n lebih besar dari 10 :'))

# +++++++++3-----------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 =', isKurangDari)

#----------10++++++++++
isLebihDari = (inputUser > 10)
print('Lebih dari 10 =', isLebihDari)

##++++++++++3-----------10++++++++++
isCorrect = isKurangDari or isLebihDari
print('Angka anda adalah :', isCorrect)

###---------3++++++++++10---------
inputUser = float(input('Masukkan angka yang bernilai \n lebih besar dari 3 \n dan \n kurang dari 10 : '))

#---------3++++++++++
# Memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print('Lebih dari 3 =', isLebihDari)

#+++++++++10-----------
isKurangDari = (inputUser < 10)
print('Kurang dari =', isKurangDari)

##---------3+++++++++10---------
isCorrect = isLebihDari and isKurangDari
print('Angka anda adalah :', isCorrect)

