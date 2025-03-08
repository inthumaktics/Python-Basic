import os

'''FUNGSI DENGAN ARGUMENT (Input)'''

# Template 
    # def nama_fungsi(argument):
    # badan fungsi
os.system('cls')

def hello_world(nama):
    '''fungsi hello world menerima input dengan variabel nama'''
    print(f"Selamat datang ngoding{nama}")

hello_world('python')
hello_world('javascript')

# Program tambah 

def penambahan(angka1,angka2):
    '''Fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")


penambahan(10,10)
penambahan(100,1246758693)

# Program List

def greeting(List_nama):
    '''Fungsi say hi'''
    data_nama = List_nama.copy()
    for nama in data_nama:
        print(f"Selamat datang {nama}")

nama_undangan = ["Eren", "Mikasa", "Armin"]

greeting(nama_undangan)