#FORMAT STRING

## Contoh generic

# String
nama = "Erika"
format_str = f"hello {nama}"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 200.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# Bilangan bulat dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# Menampilkan leading zero
angka = 300.76890
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# Menampilkan tanda + atau minus -
angka_minus = -20
angka_plus = +20
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Memformat persen 
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 15000
jumlah = 10
format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# Format angka lain (binary, octal, hexadecimal)

angka = 500
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
