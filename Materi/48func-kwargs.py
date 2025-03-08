'''*kwargs'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Naruto", 180, 75)

def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f" {nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama = "Gojo", tinggi = 185, berat = 78)

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args :
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args :
            output *= angka 
    else:
        print("Tidak ada opersi")

    return output

hasil = math(5, 5, 5, 5, option = "tambah")
print(f"hasil jumlah {hasil}")

hasil = math(5, 5, 5, 5, option = "kali")
print(f"hasil kali {hasil}")