from prettytable import PrettyTable
#Program Jasa Wedding, Mneyediakan jasa pernikahan dengan paket wedding yang tersedia
print('-----------------------------PROGRAM INDAH---------------------------------')
print('                  🤵Selamat Datang di Kirei Wedding👰                        ')
print('===========================================================================')
print('Silahkan Login Terlebih Dahulu')
#Login admin or pelanggan
def login():
    while True:
        print('\n==========LOGIN==========')
        print('1. Admin')
        print('2. Pelanggan')
        print('=========================')
        pilihan = input('Masukkan Pilihan Anda: ')
        if pilihan == '1':
            while True:
                username = input('\nMasukkan Username Admin: ')
                password = input('Masukkan Password: ')
                if username == 'KIREI' and password == 'kirei246':
                    print(f'\n❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ Selamat Datang Admin {username} ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀ ❀')
                    mode_admin()
                    return
                else:
                    print('Silahkan Masukkan Username dan Password Admin dengan Benar')
        elif pilihan == '2':
            pelanggan = input('\nMasukkan Nama Anda: ')
            print(f'\n----------Selamat Datang {pelanggan}----------')
            mode_pelanggan()
            break
        else:
            print('Maaf pilihan tidak tersedia')

#TABEL PAKET WEDDING
table = PrettyTable()
#Baris ini menentukan nama-nama kolom untuk tabel (field names)
table.field_names = ['Nomor', 'Nama Paket', 'Harga', 'Include'] #
def paket(nomor, nama, harga, include): #Mendefinisikan fungsi bernama paket
    table.add_row([nomor, nama, harga, include]) #Didalam fungsi paket, baris ini menambahkan sebuah baris baru ke dalam tabel

#Isi data paket
paket('1', 'Gedung Economy', '45000000', 'Gedung 2 jam SBY-SDA, Dekorasi Gedung, Rias & Busana, Catering 250 pax, Foto&Video, MC 1 Kali,Electone + Penyanyi')
paket('2', 'Gedung Glamour', '80000000', 'Gedung 3 Jam SBY-SDA, Dekorasi Gedung, Rias&Busana, Catering 500 pax, Foto&Video, MC 2 Kali, Band+Biola')
paket('3', 'Rumah Hemat', '25000000', 'Terop+Sound System, Dekorasi Pelaminan 4-6 m, Rias&Busana, Catering 250 pax, Foto&Video, MC 1 Kali')
paket('4', 'Rumah Mewah', '65000000', 'Terop Arabian+Sound System, Dekorasi Pelaminan 6-8 m, Rias&Busana, Catering 500 pax, Foto&Video, MC 3 Kali, Electone+Band+Penyanyi')

#Admin menambahkan paket wedding
def tambah_paket():
    while True:
        print('\n==========TAMBAH PAKET==========')
        nomor = input('Masukkan Nomor Paket: ')
        nama = input('Masukkan Nama Paket: ')
        harga = input('Masukkan Harga Paket: ')
        include = input('Masukkan Include Paket: ')
        paket(nomor, nama, harga, include) #memasukkan yang telah diinput ke dalam tabel
        print('=====================================')
        print(f'Paket {nama} Berhasil Ditambahkan ')
        print('-------------------------------------')
        pilihan = input('Apakah Ingin Menambah Paket Lagi (YA/TIDAK): ') #Perulangan pilihan
        if pilihan == 'TIDAK':
            break #berhenti perulangan

#Admin melihat paket wedding
def lihat_paket():
    print('                                                           ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮ PAKET WEDDING ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮ ✮')
    print(table) #Menampilkan tabel

#Admin memperbarui paket wedding
def perbarui_paket():
    lihat_paket()
    print('\n==========Perbarui Paket==========')
    while True:
        nomor = input('Masukkan Nomor Paket Yang Ingin Diperbarui: ')
        for row in table._rows: #Perulangan untuk setiap baris dalam tabel
            if row[0] == nomor: #Apakah setiap baris sama dengan input nomor
                pilihan = input('Masukkan Paket Yang Ingin Diperbarui (Nama/Harga/Include): ')
                pembaruan = input(f'Masukkan Pembaruan Paket Pada {pilihan}: ')
                if pilihan == 'Nama':
                    row[1] = pembaruan #Memperbarui data dalam baris
                    print('-------------------------------------')
                    print(f'Paket Wedding Nomor {nomor} Berhasil Diperbarui')
                    return
                elif pilihan == 'Harga':
                    row[2] = pembaruan
                    print('-------------------------------------')
                    print(f'Paket Wedding Nomor {nomor} Berhasil Diperbarui')
                    return
                elif pilihan == 'Include':
                    row[3] = pembaruan
                    print('-------------------------------------')
                    print(f'Paket Wedding Nomor {nomor} Berhasil Diperbarui')
                    return
                else:
                    print('-------------------------------------')
                    print('Pilihan Tidak Valid')
                    break
        else:
            print(f'Pilihan Paket Dengan Nomor {nomor} Tidak Ditemukan')
            print('-------------------------------------')

#Admin menghapus paket wedding
def hapus_paket():
    lihat_paket()
    print('\n===============HAPUS PAKET==============')
    while True:
        nomor = input('Masukkan Nomor Paket Yang Ingin Dihapus: ')
        for row in table._rows: #Perulangan untuk setiap baris dalam tabel
            if row[0] == nomor: #Apakah setiap baris sama dengan input nomor
                table._rows.remove(row) #menghapus inputan nomor dalam baris tabel
                print('=========================================')
                print(f'Paket Nomor {nomor} Berhasil Dihapus Dalam Table')
                break
        else:
            print(f'Pilihan Paket Dengan Nomor {nomor} Tidak Ditemukan')
        print('----------------------------------------')
        pilihan = input('Apakah Ingin Menghapus Paket Lagi? (YA/TIDAK): ')
        if pilihan == 'TIDAK':
            break

def mode_admin():
    while True:
        print('\n==========Menu Admin==========') 
        print('1. Tambah Paket')
        print('2. Lihat Paket')
        print('3. Perbarui Paket')
        print('4. Hapus Paket')
        print('5. Keluar Program')
        print('--------------------------------')
        pilihan = input('Silahkan Pilih Menu: ')
        if pilihan == '1':
            lihat_paket()
            tambah_paket()
        elif pilihan == '2':
            lihat_paket()
            print('Paket Wedding Yang Tersedia')
        elif pilihan == '3':
            perbarui_paket()
        elif pilihan == '4':
            hapus_paket()
        elif pilihan == '5':
            print('Terima Kasih Telah Menggunakan Program Ini')
            return
        else:
            print('Pilihan Tidak Tersedia. Silahkan Pilih Kembali')

def mode_pelanggan():
    lihat_paket()
    while True:
        print('\n=========================================================')
        print('Order Paket Wedding DP 50% / Full Pembayaran')
        pilihan_order = input('Apakah anda ingin order paket wedding? (YA/TIDAK): ')
        if pilihan_order == 'YA':
            pilih_nomor = input('\nSilahkan Pilih Nomor Paket Yang Ingin Anda Order: ') #Pelanggan memilih nomor paket yang ada dalam tabel
            tanggal = input('Kapan Tanggal Pelaksanaan Acara Wedding?: ')
            for row in table.rows: #Perulangan untuk setiap baris dalam tabel
                if row[0] == pilih_nomor: #Apakah setiap baris sama dengan input nomor
                    nama = row[1] #(indeks ke-1) elemen kedua dalam baris dan dimasukkan ke variabel nama
                    harga = float(row[2]) #(indeks ke-2) elemen ketiga dalam baris diambil dan diubah ke tipe data float
                    pilih_pembayaran = input('Pilih Pembayaran (DP / FULL): ')
                    if pilih_pembayaran == 'DP':
                        dp = harga * 0.5 #Menghitung dp 50%
                        sisa_dp = harga - dp #Sisa dari dp
                        print('-----------------------------------------------------')
                        print(f'Jumlah DP : Rp. {dp}')
                        print(f'Jumlah DP 50% yang Harus Dibayar: Rp. {dp}')
                        print(f'Sisa yang Harus Dibayar: Rp. {sisa_dp} ')
                        print('-----------------------------------------------------')
                        konfirmasi = input(f'Konfirmasi Orderan Paket {nama} Anda dengan DP 50%? (YA/TIDAK): ')
                        if konfirmasi == 'YA':
                            print(f'Orderan Paket {nama} Berhasil dengan DP 50% dan Tanggal Pelaksanaan {tanggal} ')
                            print('-----------------------------------------------------')
                            print(f'\nTerima Kasih Telah Order Paket Wedding')
                            return
                        else:
                            print(f'Orderan Paket {nama} Anda Dibatalkan')
                            return
                    elif pilih_pembayaran == 'FULL':
                        print('-----------------------------------------------------')
                        konfirmasi = input(f'Konfirmasi Orderan Paket {nama} Anda dengan Full Pembayaran Rp. {harga}? (YA/TIDAK): ')
                        if konfirmasi == 'YA':
                            print(f'Orderan Paket {nama} Berhasil dengan Harga Rp. {harga} dan Tanggal Pelaksanaan {tanggal}')
                            print('-----------------------------------------------------')
                            print(f'Terima Kasih Telah Order Paket Wedding')
                            return
                        else:
                            print(f'Orderan Paket {nama} Anda Dibatalkan')
                            return
                    else:
                        print('Pilihan Pembayaran Tidak Benar. Silahkan Coba Lagi')
            else:
                print(f'Pilihan Paket Dengan Nomor {pilih_nomor} Tidak Ditemukan') 
        else:
            print('Terima Kasih Telah Mengunjungi Layanan Jasa Kirei Wedding')
            return

login()


