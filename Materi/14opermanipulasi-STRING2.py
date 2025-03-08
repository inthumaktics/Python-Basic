# OPERATOR DALAM BENTUK METHODS

## MENGUBAH CASE DARI STRING

#1. Merubah semua ke upper case

kata = "kocak!"
print("normal = " + kata)
kata = kata.upper()
print("upper = " + kata)

#2. Merunah semua ke lower case
kocak_banget = "ApAan siH AnJirrrRRR"
print("normal = " + kocak_banget )
kocak_banget = kocak_banget.lower()
print("lower = " + kocak_banget)

## PENGECEKAN DENGAN isX METHOD

#1. Pengecekan lower case 
contoh = "helo bang"
cek_lower = contoh.islower()
print(contoh + " is lower = " + str(cek_lower)) #hasilnya boolean

#2. Pengecekan upper case
cek_upper = contoh.isupper()
print(contoh + " is upper = " + str(cek_upper)) #hasilnya boolean

## beberapa contoh yang lain :
# isalpha() -->> mengecek semuanya huruf
# isalnum() -->> huruf dan angka
# isdecimal() -->> angka saja
# isspace() -->> spasi, tab, newline \n
# istitle() -->> semua kata dimulai dengan huruf besar

#3. Pengecekan judul/semua kata awal huruf besar
judul = "Queen Of Tears"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## PENGECEKAN KOMPONEN startswith() dan endswith()
cek_start = "Hasil Belajar".startswith("Hasil")
print("Start = " + str(cek_start))

cek_end = "Hasil Belajar".endswith("Belajar")
print("end = " + str(cek_end))

## PENGGABUNGAN KOMPONEN join() split()

#join()
pisah = ['Aku', 'Sayang', 'Mas Arya']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' iya '.join(pisah)
print(gabungan)

#split()
gabungan = "akuiyasayangiyamasarya"
print(gabungan.split('iya'))

## ALOKASI KARAKTER 

#rjust()
kanan = "kanan".rjust(15)
print("'"+kanan+"'")

#ljust()
kiri = "kiri".ljust(15)
print("'"+kiri+"'")

#center()
tengah = "tengah".center(20,"=")
print("-"+tengah+"-")

# kebalikannya -> strip()
tengah = tengah.strip("=") #menghilangkan tanda 
print("'"+tengah+"'")
                    

judul = "2. Memisahkan lalu Menggabungkan Nama-nama".center(10,"=")
print(judul)