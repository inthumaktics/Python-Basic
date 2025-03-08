#OPERASI DAN MANIPULASI STRING

# 1. Menyambung String (Concatenate)
nama_pertama = "Erika"
nama_tengah = "A"
nama_akhir = "Feb"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung Panjang String 
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk String
# mengecek apakah ada komponen char atau string di dalam string

a = "a"
status = a in nama_lengkap
print(a + " ada di " + nama_lengkap + " = " + str(status))

A = "A"
status = A in nama_lengkap
print(A + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*20)
print(25*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] " + nama_lengkap[0:4])
print("index ke-[3:7] :" + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2])

# item paling kecil 
print("paling kecil :" + min(nama_lengkap))
# item paling besar
print("paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 97
print("char untuk ASCII 97 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "saya suka belajar dan itu sangat menyenangkan"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))