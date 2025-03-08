# WIHT AND MULTILINE

# DATA :

data_nama = "Santai dulu"
data_umur = 20
data_tinggi = 173.0
data_nomor_sepatu = 45

# STRING STANDARD :
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"String Standard"+"="*5)
print(data_string)

# STRING MULTILINE (enter, newline \n) : 
data_string = f"nama = {data_nama}, \numur = {data_umur},\ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"String Multiline newline"+"="*5)
print(data_string)

# STRING MULTILINE (kutip triplets) :
data_string = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"String Multiline 3 kutip"+"="*5)
print(data_string)

# Mengatur lebar :
data_nama = "Fakmennn"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"Mengatur Lebar"+5*"=")
print(data_string)