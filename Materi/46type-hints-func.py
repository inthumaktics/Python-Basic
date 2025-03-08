'''Type Hints untuk Fungsi'''

# bentuk standar fungsi yang sudah dipelajari : 
'''
Studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Eren")
fungsi(True)
'''

# Penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''Fungsi dengan hints'''
    output = 10**argument
    return output

Hasil = sepuluh_pangkat(4)
print(Hasil)

def display(argument:string):
    print(argument)

display("Sung Jin-woo")