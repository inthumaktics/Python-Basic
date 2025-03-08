import datetime

mahasiswa1 = {
    'nama':'Eren Yeager',
    'nim':'24870001',
    'sks_lulus':145,
    'beasiswa':False,
    'lahir':datetime.datetime(2003,3,30)
}

mahasiswa2 = {
    'nama':'Hyuga Neji',
    'nim':'24870002',
    'sks_lulus':155,
    'beasiswa':True,
    'lahir':datetime.datetime(2003,7,3)

}

mahasiswa3 = {
    'nama':'Sung Jinwoo',
    'nim':'24870003',
    'sks_lulus':145,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,3,8)

}

mahasiswa4 = {
    'nama':'Uchiha Itachi',
    'nim':'24870004',
    'sks_lulus':150,
    'beasiswa':False,
    'lahir':datetime.datetime(2002,10,9)
}

mahasiswa5 = {
    'nama':'Ishigami Senku',
    'nim':'24870005',
    'sks_lulus':170,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,1,4)
}

data_mahasiswa = {
    'MHS001':mahasiswa1,
    'MHS002':mahasiswa2,
    'MHS003':mahasiswa3,
    'MHS004':mahasiswa4,
    'MHS005':mahasiswa5
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':^9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
