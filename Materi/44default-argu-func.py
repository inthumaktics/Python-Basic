'''DEFAULT ARGUMENT'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

### CONTOH 1
def greeting(nama = 'Are u okay?'):
    '''Fungsi dengan default argument'''
    print(f"hey {nama}")

greeting("halo")
greeting()

###CONTOH 2
def menyapa(nama, pesan = 'How are you?'):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"Ini adalah pesan dari {nama}, {pesan}")

menyapa("Eren", "TATAKAE!!!")
menyapa("Neji")

###CONTOH 3
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)

###CONTOH 4
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input4 = 15))