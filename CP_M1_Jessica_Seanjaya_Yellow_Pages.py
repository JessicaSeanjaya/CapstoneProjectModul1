#Data
listkontak = [
    {
        'id': 'A0001',
        'nama' : 'Amanda',
        'telp' : '0211111111',
        'alamat' : 'Jl. Aceh No 1',
        'email' : 'amanda@gmail.com'
    },
    {
        'id': 'B0002',
        'nama' : 'Bunga',
        'telp' : '0212222222',
        'alamat' : 'Jl. Mawar No 9',
        'email' : 'bunga@gmail.com'
    },
    {
        'id':'C0003',
        'nama' : 'Cindy',
        'telp' : '0213333333',
        'alamat' : 'Jl. Kamboja No 23',
        'email' : 'cindy@yahoo.co.id'
    },
    {
        'id': 'D0004',
        'nama' : 'Dora',
        'telp' : '0214444444',
        'alamat' : 'Jl. Macan No 100',
        'email' : 'dora@yahoo.com'
    },
    {
        'id': 'E0005',
        'nama' : 'Edlyn',
        'telp' : '0215555555',
        'alamat' : 'Jl. Merauke No 99',
        'email' : 'edlyn@hotmail.com'
    }
]

#Main Menu
def mainmenu():
    while True:
        print('''
===========================================================================================================
||****************************************Welcome to Yellow Pages****************************************||
===========================================================================================================

List Menu: 
1. Menampilkan kontak
2. Menambah kontak
3. Mengupdate kontak
4. Menghapus kontak
5. Keluar program
''')
        menu = input ("Masukkan menu yang akan dijalankan : ")

        if menu == '1':
            menampilkankontak()
        elif menu == '2':
            menambahkontak()
        elif menu == '3':
            mengupdatekontak()
        elif menu == '4':
            menghapuskontak()
        elif menu == '5':
            keluarprogram()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            mainmenu()
            
#Back to Sub Menu
def kembali():
    while True:
        kembali= input ("\nKembali ke sub menu (Y/N):").upper()
        if kembali == "Y":
            break

#Show Data
def lihatkontak():
    print ('\nDaftar Kontak: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
    for i in range (len(listkontak)):
        print('{} \t | {} \t | {} \t | {} \t | {}'.format(listkontak [i]['id'], listkontak[i]['nama'], listkontak[i]['telp'], listkontak[i]['alamat'],listkontak[i]['email']))

#Read Data
def menampilkankontak():
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 1                                      |
|                             MENAMPILKAN KONTAK                                |
---------------------------------------------------------------------------------
1. Menampilkan semua list 
2. Menampilkan list berdasarkan ID
3. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            if len(listkontak)!=0:
                lihatkontak()
                kembali()
                menampilkankontak()
            else: 
                print ('\nData tidak tersedia')
                kembali()
                menampilkankontak()
        elif pilihan == '2':
            if len(listkontak)!=0:
                idcari = input("\nMasukkan id yang dicari: ").upper()
                for i in range(len(listkontak)):
                    if idcari == listkontak[i]['id']:
                        print ('\nDaftar Kontak: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
                        print ('{} \t | {} \t | {} \t | {} \t | {}'.format(listkontak[i]['id'], listkontak[i]['nama'], listkontak[i]['telp'], listkontak[i]['alamat'],listkontak[i]['email']))
                        kembali()
                        menampilkankontak()
                else:
                    print ('\nData tidak tersedia')
                    kembali()
                    menampilkankontak()
            else:
                print ('\nData tidak tersedia')
                kembali()
                menampilkankontak()
        elif pilihan == '3':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menampilkankontak()

#Create Data
def menambahkontak():
    lihatkontak()
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 2                                      |
|                              MENAMBAH KONTAK                                  |
---------------------------------------------------------------------------------
1. Menambahkan kontak
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idkontak = input ('\nMasukkan id kontak:').upper()
            for i in range(len(listkontak)):
                if idkontak == listkontak[i]['id']:
                    print ('\nData sudah tersedia')
                    kembali()
                    menambahkontak()
            else: 
                nama = input ('Masukkan nama kontak:').capitalize()
                telp = input ('Masukkan nomor telepon kontak:')
                alamat = input ('Masukkan alamat kontak:').title()
                email = input ('Masukkan email kontak:').lower()
                cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                if cek == 'Y':
                    listkontak.append(
                        {'id': idkontak,
                        'nama': nama, 
                        'telp': telp, 
                        'alamat': alamat, 
                        'email': email})
                    print ('\nData berhasil disimpan')
                    kembali()
                    menambahkontak()
                else:
                    print("\nData tidak tersimpan")
                    kembali()
                    menambahkontak()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menambahkontak()

#Update Data
def mengupdatekontak():
    lihatkontak()
    while True:
        print('''
--------------------------------------------------------------------------------
|                                   MENU 3                                     |
|                             MENGUPDATE KONTAK                                |
--------------------------------------------------------------------------------
1. Mengubah informasi kontak
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idupdate = input('\nMasukkan id kontak yang ingin diupdate:').upper()
            for i in range(len(listkontak)):
                if idupdate == listkontak[i]['id']:
                    print ('\nDaftar Kontak: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
                    print ('{} \t | {} \t | {} \t | {} \t | {}'.format(listkontak[i]['id'], listkontak[i]['nama'], listkontak[i]['telp'], listkontak[i]['alamat'],listkontak[i]['email']))
                    lanjutupdate = input ("\nApakah data ini ingin diupdate (Y/N):").upper()
                    if lanjutupdate =='Y':
                        bagianupdate = input('\nMasukkan bagian yang ingin diupdate (nama/telp/alamat/email):')
                        if bagianupdate == 'nama':
                            namaupdate = input('\nMasukkan nama kontak terbaru:').capitalize()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listkontak[i][bagianupdate] = namaupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatekontak()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatekontak()
                        elif bagianupdate == 'telp':
                            telpupdate = input('\nMasukkan nomor telp kontak terbaru:')
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listkontak[i][bagianupdate] = telpupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatekontak()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatekontak()
                        elif bagianupdate == 'alamat':
                            alamatupdate = input ('\nMasukkan alamat kontak terbaru:').title()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listkontak[i][bagianupdate] = alamatupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatekontak()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatekontak()
                        elif bagianupdate == 'email':
                            emailupdate = input('Masukkan email terbaru:').lower()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listkontak[i][bagianupdate] = emailupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatekontak()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatekontak()
                        else:
                            kembali()
                            mengupdatekontak()
                    else:
                        kembali()
                        mengupdatekontak()
            else:
                print ('\nData tidak tersedia')
                kembali()
                mengupdatekontak()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            mengupdatekontak()

#Delete Data
def menghapuskontak():
    lihatkontak()
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 4                                      |
|                              MENGHAPUS KONTAK                                 |
---------------------------------------------------------------------------------
1. Menghapus kontak
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idhapus = input ('\nMasukkan id kontak yang ingin dihapus:').upper()
            for i in range(len(listkontak)):
                if idhapus == listkontak[i]['id']:
                    cek = input ("\nApakah anda yakin akan menghapus data (Y/N):").upper()
                    if cek =='Y':
                        del listkontak[i]
                        print ("\nKontak berhasil dihapus")
                        kembali()
                        menghapuskontak()
                    else:
                        print ("\nKontak tidak dihapus")
                        kembali()
                        menghapuskontak()
            else:
                print ("\nKontak tidak tersedia")
                kembali()
                menghapuskontak()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menghapuskontak()

#Exit Program
def keluarprogram():
    print('\nSampai jumpa lagi !')
    exit()

mainmenu()