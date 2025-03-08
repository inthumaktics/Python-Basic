### PENGENALAN STRING
data = "ini adalah string"
print(data)
print(type(data))

#1. CARA MEMBUAT STRING

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."

'''
data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, dimana saya?"')
print("'Halo, kerjakan tugasmu bang!'")
print("Ini adalah hari jum'at")

#2. MENGGUNAKAN TANDA \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\t it?')

# backslash
print("C:\\user\\Erika") #benar pakai \\

# tab 
print("Erika\tArya, jadi berjauhan")
print("Arya \t\t\t Erika, semakin jauh")

# backspace
print("Arya \b Erika, jadi mendekat")

# newline
print("baris pertama.\nbaris kedua.") #LF -> Line Feed 
print("baris pertama.\rbaris kedua.") #CR -> Carriage Return
print("baris pertama.\r\nbaris kedua.") # -> Line Feed Carriage Return

#3. STRING LITERAL ATAU RAW

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# menggunakan literal string
print("""
Nama : Erika
Prodi : Sistem Informasi/B
Fakultas : Sains dan Teknologi Terapan
Website : www.inthumaktics.com/newProject
""")



