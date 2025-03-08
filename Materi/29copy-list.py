## TEKNIK MENDUPLIKAT LIST 

x = ["hallo", "oke", "selesai"]
print(f" x = {x}")

y = x #pass by reference
print(f" y = {y}")

# mengubah data dari a

# ini akan mengubah kedua list
x[2] = "done!"
y.sort()
print(f" x = {x}")
print(f" y = {y}")

# addres dari kedua list
print(f" address x = {hex(id(x))}")
print(f" address y = {hex(id(y))}")

# Menduplikat list dengan copy
print("\n Membuat list z dengan x.copy()")

z = x.copy() # full duplikat
print(f" address x = {hex(id(x))}")
print(f" address y = {hex(id(y))}")
print(f" address z = {hex(id(z))}")

print(f" x = {x}")
print(f" y = {y}")
print(f" z = {z}")

print("\n Mengubah data 0")
z[0] = "apa ya?"
print(f" x = {x}")
print(f" y = {y}")
print(f" z = {z}")


print("\n Mengubah data 1")
z[1] = "How can I learned today?"
print(f" x = {x}")
print(f" y = {y}")
print(f" z = {z}")
