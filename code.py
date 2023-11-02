# Algoritma
# inisialisasi variabel berupa daftar list untuk setiap toping, crust dan size
toping = ["Frankfurter BBQ", "Meat Monsta", "Super Supreme", "Super Supreme Chiken"]
crust = ["Pan", "Stuffed Crust Sausage", "Stuffed Crust Cheese", "Cheesy Bites", "Crown Crust"]
size = ["Personal", "Regular", "Large"]

# Akan menampilkan tampilan awal dan konfirmasi pesanan
print('''
=======================================================
            SELAMAT DATANG DI LAYANAN KAMI
        ======================================
        PEMESANAN PIZZA BY : KELOMPOK 12 MI23F  
=======================================================
Apakah Anda ingin memesan pizza? (y/n)
''')
konfirmasi = input('(y/n) : ').lower()

# jika buyyer mengonfirmasi 'y', maka program akan melanjutkan 
if konfirmasi == "y":

# Akan menaampilkan daftar menu toping    
    print("""
==============================================
      Berikut merupakan daftar menu kami :
==============================================
          """)
    for i, daftar_menu in enumerate(toping):
        print (i+1, daftar_menu)
    pilihan_toping = int(input('Masukkan Pilihan anda (1-4) : '))
   
# Akan menampilkan daftar pilihan crust
    print("""
===============================================
  Berikut merupakan daftar Crust Pizza kami :
===============================================
          """)
    for i, daftar_crust in enumerate(crust):
        print(i+1, daftar_crust)
    pilihan_crust = int(input('Masukkan Crust pizza pilihan anda (1-5) : '))

# Akan menampilkan daftar size
    print("""
==============================================
  Berikut merupakan daftar Size Pizza kami :
==============================================
          """)
    for i, daftar_size in enumerate(size):
        print(i+1, daftar_size)
    pilihan_size = int(input('Masukkan Size pizza pilihan anda (1-3) : '))


# Akan menampilkan penawaran keju
    print('==============================================')
    keju_conf = input('Apakah Anda ingin menambah keju: (y/n) : ')
    if keju_conf == "y":
        keju = True
    else:
        keju = False      

# program berhenti ketika input selain "y"
else:
    print('''
==============================================
  Terimakasih telah menggunakan layanan kami
==============================================
          ''')

# program mulai melakukan pengecekan dan menghitung harga
harga = 0

# memberikan harga dasar berdasarkan ukuran pizza
if pilihan_crust == 1: # harga jika harga jika crust no 4
    harga += 43637 # tambahan harga jika ukuran personal
    if pilihan_size == 1:
        harga += 0
    elif pilihan_size == 2:
        harga += 57273 # tambahan harga jika ukuran regular
    else:
        harga += 89091 # tambahan harga jika ukuran large

elif pilihan_crust == 2: # harga jika harga jika crust no 2
    harga += 55455 #harga jika ukuran personal
    if pilihan_size == 1:
        harga += 0
    elif pilihan_size == 2:
        harga += 65455 # tambahan harga jika ukuran regular
    else:
        harga += 104545 # tambahan harga jika ukuran large

elif pilihan_crust == 3: # harga jika harga jika crust no 3
    harga += 52728 #harga jika ukuran personal
    if pilihan_size == 1:
        harga += 0
    elif pilihan_size == 2:
        harga += 64545 # tambahan harga jika ukuran regular
    else:
        harga += 102727# tambahan harga jika ukuran large

elif pilihan_crust == 4: # harga jika crust no 4
    harga += 57273 #harga jika ukuran personal
    if pilihan_size == 1:
        harga += 0
    elif pilihan_size == 2:
        harga += 66364 # tambahan harga jika ukuran regular
    else:
        harga += 107273 # tambahan harga jika ukuran large

else: #harga jika crust no 5
    harga -+ 57273 #harga jika ukuran personal
    if pilihan_size == 1:
        harga += 0
    elif pilihan_size == 2:
        harga += 66364 # tambahan harga jika ukuran regular
    else:
        harga += 102727 # tambahan harga jika ukuran large

# untuk menghitung tambahan pizza
if keju == True:
    tambahan_keju = 'Tambah Keju'
    if pilihan_size == 1:
        harga += 13636 # harga tambahan keju jika size personal
    elif pilihan_size == 2:
        harga += 16364 # harga tambahan keju jika size regular
    else:
        harga += 19091 # harga tambahan keju jika size large

else:
    tambahan_keju = 'Tanpa Tambahan Keju'

total = ("{:,}".format(harga))
# Akan menampilkan total dan ucapan terimakasih 
print(f'''
================================================
     BERIKUT MERUPAKAN STRUK TAGIHAN ANDA
================================================
Pesanan : {toping[(pilihan_toping)-1]}
Crust   : {crust[(pilihan_crust)-1]}
Size    : {size[(pilihan_size)-1}
Keju    : {tambahan_keju}
================================================
Total tagihan anda adalah : Rp. {total}
================================================
         TERIMA KASIH TELAH BERKUNJUNG 
                    DAN
         SELAMAT MENIKMATI PIZZA ANDA
================================================
''')
