listBuku = [
    {
        "Judul Buku": "Atomic Habits",
        "Pengarang": "James Clear",
        "Penerbit": "Avery",
        "Kategori": "Self-Help",
        "Tipe Buku": "Cetak",
        "Jumlah": 10
    },
    {
        "Judul Buku": "Laskar Pelangi",
        "Pengarang": "Andrea Hirata",
        "Penerbit": "Bentang Pustaka",
        "Kategori": "Fiksi",
        "Tipe Buku": "Cetak",
        "Jumlah": 10
    },
    {
        "Judul Buku": "Bumi",
        "Pengarang": "Tere Liye",
        "Penerbit": "Gramedia Pustaka Utama",
        "Kategori": "Fantasi",
        "Tipe Buku": "Ebook",
        "Jumlah": 1
    },
    {
        "Judul Buku": "Negeri 5 Menara",
        "Pengarang": "Ahmad Fuadi",
        "Penerbit": "Gramedia",
        "Kategori": "Motivasi",
        "Tipe Buku": "Ebook",
        "Jumlah": 1
    },
    {
        "Judul Buku": "Filosofi Teras",
        "Pengarang": "Henry Manampiring",
        "Penerbit": "Kompas",
        "Kategori": "Pengembangan Diri",
        "Tipe Buku": "Cetak",
        "Jumlah": 7
    },
    {
        "Judul Buku": "Rich Dad Poor Dad",
        "Pengarang": "Robert T. Kiyosaki",
        "Penerbit": "Plata Publishing",
        "Kategori": "Bisnis",
        "Tipe Buku": "Cetak",
        "Jumlah": 3
    },
    {
        "Judul Buku": "To Kill a Mockingbird",
        "Pengarang": "Harper Lee",
        "Penerbit": "J.B. Lippincott & Co.",
        "Kategori": "Klasik",
        "Tipe Buku": "Ebook",
        "Jumlah": 1
    }
]


listInfo = [
    {
        "Title": "Informasi General",
"Information": """Perpustakaan Purwadhika beroperasi dari Senin sampai Sabtu jam 08.00-22.00 WIB.
Tutup pada hari Minggu dan hari libur nasional.
Pengunjung hanya diperbolehkan membawa minuman dalam tumbler dan dilarang membawa makanan."""
    },
    {
        "Title": "Ketentuan dan Cara Pinjam Buku Cetak",
        "Information": """Buku yang hanya bisa dipinjam adalah buku cetak.
Buku hanya dapat dipinjam selama 6 hari.
Peminjam yang ingin mengembalikan buku cetak, bisa langsung mendatangi salah satu Book Station Perpustakaan Purwadhika."""
    },
    {
        "Title": "Denah Lokasi",
        "Information": """Lantai 1: Pusat Informasi, Book Station, Loker Penitipan Barang, Kantin, Toilet
Lantai 2: Koleksi Buku Anak, Koleksi Buku Fiksi, Ruang Anak, Mushollah, Toilet
Lantai 3: Koleksi Buku Non Fiksi, Ruang Diskusi, Ruang Audio Visual, PC Internet, Toilet."""
    }
]

listAkun = [
    {
        "Full Name": "Naurotun Nadhifah",
        "Username": "dhifanana",
        "Password": "Password123",
        "Age": 27,
        "Domisili": "Pulo Gadung",
        "Favorite Genre": "Fiksi Ilmiah",
        "Registration Date": "20241120",
        "Role": "Admin"
    },
    {
        "Full Name": "Rose Blackpink",
        "Username": "rose_bp",
        "Password": "Password123",
        "Age": 28,
        "Domisili": "Menteng",
        "Favorite Genre": "Biografi",
        "Registration Date": "20230519",
        "Role": "Tamu"
    },
    {
        "Full Name": "Lisa Blackpink",
        "Username": "lisa_bp",
        "Password": "Password123",
        "Age": 28,
        "Domisili": "Menteng",
        "Favorite Genre": "Komik",
        "Registration Date": "20230519",
        "Role": "Tamu"
    },
    {
        "Full Name": "Jennie Blackpink",
        "Username": "jennie_bp",
        "Password": "Password123",
        "Age": 29,
        "Domisili": "Salemba",
        "Favorite Genre": "Fiksi Romansa",
        "Registration Date": "20230519",
        "Role": "Tamu"
    },
    {
        "Full Name": "Jisoo Blackpink",
        "Username": "jisoo_bp",
        "Password": "Password123",
        "Age": 30,
        "Domisili": "Kemang",
        "Favorite Genre": "Fiksi Sejarah",
        "Registration Date": "20230519",
        "Role": "Tamu"
    }
]


# =================================================================#
# =================================================================#


def lihat_menuUmum():
    print(f"""{"="*60}
  📚   HALO SELAMAT DATANG DI PERPUSTAKAAN PURWADHIKA   📚
{"="*60}
Main Menu
1. Masuk
2. Daftar Buku
3. Lihat Informasi
4. Tutup Aplikasi""")

    menuTerpilih = input("Masukkan angka menu yang ingin Anda tuju [1-4]: ")

    if not menuTerpilih.isdigit() or "." in menuTerpilih:
        print(
            "pilihan menu tidak valid, silakan masukkan angka menu yang ingin Anda tuju [1-4]")
    else:
        menuTerpilih = int(menuTerpilih)
        if menuTerpilih == 1:
            print("-"*60)
            lihat_masuk()
        elif menuTerpilih == 2:
            print("-"*60)
            lihat_bukuUmum()
        elif menuTerpilih == 3:
            print("-"*60)
            lihat_infoUmum()
        elif menuTerpilih == 4:
            print("TERIMA KASIH TELAH BERKUNJUNG. APLIKASI TERTUTUP")
            print("-"*60)
            exit()
        else:
            print("-"*60)
            print("pilihan menu tidak valid, silakan masukkan angka menu yang ingin Anda tuju [1-4]")
            lihat_menuUmum()


def lihat_masuk():
    username = input("Username: ").lower()
    password = input("Password: ")
    
    akunFound = [i for i in listAkun if i["Username"] == username]

    if not akunFound:
        print("Akun tidak terdaftar")
        print("-"*60)
        lihat_masuk()
    else:
        akun = akunFound[0]
        if (password != akun["Password"]):
            print("Password yang Anda masukkan salah")
            print("-"*60)
            lihat_masuk()
        elif(akun["Role"] == "Tamu"):
            print("Maaf aplikasi sebagai tamu dalam perbaikian. Silakan coba masuk lagi nanti")
            print("-"*60)
            lihat_masuk()
        elif(akun["Role"] == "Admin"):
            print("-"*60)
            lihat_menuAdmin()


def lihat_menuAdmin():
    print(f"""{"="*60}
📚🧑HALO ADMIN SELAMAT DATANG DI PERPUSTAKAAN PURWADHIKA🧑📚
{"="*60}
Main Menu
1. Buku
2. Informasi
3. Akun
4. Keluar
5. Tutup Aplikasi""")
    
    menuTerpilih = input("Masukkan angka menu yang ingin Anda tuju [1-5]: ")

    if not menuTerpilih.isdigit() or "." in menuTerpilih:
        print(
            "pilihan menu tidak valid, silakan masukkan angka menu yang ingin Anda tuju [1-5]")

    menuTerpilih = int(menuTerpilih)
    if menuTerpilih == 1:
        print("-"*60)
        lihat_menuBukuAdmin() 
    elif menuTerpilih == 2:
        print("-"*60)
        lihat_menuInfoAdmin() 
    elif menuTerpilih == 3:
        print("-"*60)
        lihat_menuAkunAdmin() 
    elif menuTerpilih == 4:
        print("-"*60)
        print("HALO ADMIN TERIMA KASIH TELAH BERKUNJUNG. SAMPAI JUMPA")
        lihat_menuUmum()
    elif menuTerpilih == 5:
        exit()
    else:
        print("-"*60)
        print("pilihan menu tidak valid, silakan masukkan angka menu yang ingin Anda tuju [1-5]")
        lihat_menuAdmin()
            

def lihat_menuInfoAdmin():
    print(f"""{"="*60}
Informasi
1. Lihat Daftar Informasi
2. Tambah Informasi
3. Ubah Informasi
4. Hapus Informasi
5. Kembali""")
    
    menuTerpilih = input("Masukkan angka aksi yang ingin Anda lakukan [1-5]: ")

    if not menuTerpilih.isdigit() or "." in menuTerpilih:
        print(
            "pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-5]")

    menuTerpilih = int(menuTerpilih)
    if menuTerpilih == 1:
        print("-"*60)
        lihat_infoAdmin(muncul_menuAdmin = True)
    elif menuTerpilih == 2:
        print("-"*60)
        tambah_info()
    elif menuTerpilih == 3:
        print("-"*60)
        ubah_info()
    elif menuTerpilih == 4:
        print("-"*60)
        hapus_info()
    elif menuTerpilih == 5:
        print("-"*60)
        lihat_menuAdmin()
    else:
        print("-"*60)
        print("pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-5]")
        lihat_menuInfoAdmin()
    

# =================================================================#
# =================================================================#


def lihat_infoUmum():
    for index, i in enumerate(listInfo):
        info1 = i["Title"].upper()
        info2 = i["Information"]
        print(f"{index+1}. {info1}")
        print(info2)
        print("-"*60)
    
    lihat_menuUmum()


def lihat_infoAdmin(muncul_menuAdmin = True):
    for index, i in enumerate(listInfo):
        info1 = i["Title"].upper()
        info2 = i["Information"]
        print(f"{index+1}. {info1}")
        print(info2)
        print("-"*60)
    
    if muncul_menuAdmin:
        lihat_menuInfoAdmin()


def tambah_info():
    title = input("Masukkan Judul: ").upper()
    info = input("Masukkan Informasi: ")
    
    infoBaru = {
        "Title": title,
        "Information": info
    }
    
    listInfo.append(infoBaru)
    print("-"*60)
    print(f"Selamat Anda berhasil menambahkan {title} ke dalam daftar informasi")
    lihat_menuInfoAdmin()


def ubah_info():
    lihat_infoAdmin(muncul_menuAdmin = False)

    daftarTerpilih = input(f"Masukkan angka daftar yang ingin Anda ubah: ")
    
    if not daftarTerpilih.isdigit() or "." in daftarTerpilih:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda ubah")
        print("-"*60)
        ubah_info()
        return
    
    daftarTerpilih = int(daftarTerpilih) - 1
    if daftarTerpilih >= len(listInfo) or daftarTerpilih < 0:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda ubah")
        print("-"*60)
        ubah_info()
        return
    
    title = input("Masukkan Judul Baru: ").upper()
    info = input("Masukkan Informasi Baru: ")
            
    listInfo[daftarTerpilih]["Title"] = title
    listInfo[daftarTerpilih]["Information"] = info
    
    print("-"*60)
    print(f"Selamat Anda berhasil mengubah informasi {title}")
    lihat_menuInfoAdmin()


def hapus_info():    
    lihat_infoAdmin(muncul_menuAdmin = False)

    daftarTerpilih = input(f"Masukkan angka daftar yang ingin Anda hapus: ")
    
    if not daftarTerpilih.isdigit() or "." in daftarTerpilih:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        hapus_info()
        return
    
    daftarTerpilih = int(daftarTerpilih) - 1
    
    if daftarTerpilih >= len(listInfo) or daftarTerpilih < 0:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        print("-"*60)
        hapus_info()
        return
    
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus informasi dari daftar (Ya/Tidak)? ").lower()
    if konfirmasi == "ya":
        infoTerhapus = listInfo.pop(daftarTerpilih)
        print("-"*60)
        print(f"Selamat Anda berhasil menghapusnya dari daftar informasi")
        lihat_menuInfoAdmin()
    elif konfirmasi == "tidak":
        print("-"*60)
        lihat_infoAdmin()
    else:
        print("-"*60)
        print('Tidak menerima kata di luar "Ya" dan "Tidak"')
        print("-"*60)
        hapus_info()
 

# =================================================================#
# =================================================================#


def lihat_menuBukuAdmin():
    print(f"""{"="*60}
Buku
1. Lihat Daftar Buku
2. Tambah Buku
3. Ubah Buku
4. Hapus Buku
5. Kembali""")
    
    menuTerpilih = input("Masukkan angka aksi yang ingin Anda lakukan [1-5]: ")

    if not menuTerpilih.isdigit() or "." in menuTerpilih:
        print(
            "pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-5]")

    menuTerpilih = int(menuTerpilih)
    if menuTerpilih == 1:
        print("-"*60)
        lihat_bukuAdmin(muncul_menuAdmin = True)
    elif menuTerpilih == 2:
        print("-"*60)
        tambah_buku()
    elif menuTerpilih == 3:
        print("-"*60)
        ubah_buku()
    elif menuTerpilih == 4:
        print("-"*60)
        hapus_buku()
    elif menuTerpilih == 5:
        print("-"*60)
        lihat_menuAdmin()
    else:
        print("-"*60)
        print("pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-5]")
        lihat_menuBukuAdmin()    


def lihat_bukuUmum():
    for index, i in enumerate(listBuku):
        info1 = i["Judul Buku"].upper()
        info2 = i["Pengarang"]
        info3 = i["Penerbit"]
        info4 = i["Kategori"]
        info5 = i["Tipe Buku"]
        info6 = i["Jumlah"]
        print(f"{index+1}. {info1}")
        print(f"""Pengarang: {info2}
Penerbit: {info3}
Kategori: {info4}
Tipe Buku: {info5}
Jumlah: {info6}""")
        print("-"*60)
    
    lihat_menuUmum()


def lihat_bukuAdmin(muncul_menuAdmin = True):
    for index, i in enumerate(listBuku):
        info1 = i["Judul Buku"].upper()
        info2 = i["Pengarang"]
        info3 = i["Penerbit"]
        info4 = i["Kategori"]
        info5 = i["Tipe Buku"]
        info6 = i["Jumlah"]
        print(f"{index+1}. {info1}")
        print(f"""Pengarang: {info2}
Penerbit: {info3}
Kategori: {info4}
Tippe Buku: {info5}
Jumlah: {info6}""")
        print("-"*60)
    
    if muncul_menuAdmin:
        lihat_menuBukuAdmin()


def tambah_buku():
    judul = input("Masukkan Judul Buku: ").upper()
    pengarang = input("Masukkan Pengarang: ").title()
    penerbit = input("Masukkan Penerbit: ")
    kategori = input("Masukkan Kategori: ")
    tipe = input("Masukkan Tipe Buku (Cetak/Ebook): ").lower()
    jumlah = 0
    
    if tipe == "cetak":
        jumlah = input("Masukkan Jumlah: ")
    elif tipe == "ebook":
        jumlah += 1
    else:
        print('Tidak menerima kata di luar "Cetak" dan "Ebook". Form ditolak')
        tambah_buku()
        return
        
    bukuBaru = {
        "Judul Buku": judul,
        "Pengarang": pengarang,
        "Penerbit": penerbit,
        "Kategori": kategori,
        "Tipe Buku": tipe,
        "Jumlah": jumlah
    }
    
    listBuku.append(bukuBaru)
    print("-"*60)
    print(f"Selamat Anda berhasil menambahkan {judul} ke dalam daftar buku")
    lihat_menuBukuAdmin()


def ubah_buku():
    lihat_bukuAdmin(muncul_menuAdmin = False)

    daftarTerpilih = input(f"Masukkan angka daftar yang ingin Anda ubah: ")
    
    if not daftarTerpilih.isdigit() or "." in daftarTerpilih:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda ubah")
        print("-"*60)
        ubah_buku()
        return
    
    daftarTerpilih = int(daftarTerpilih) - 1
    if daftarTerpilih >= len(listBuku) or daftarTerpilih < 0:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda ubah")
        print("-"*60)
        ubah_buku()
        return
    
    judul = input("Masukkan Judul Baru: ").upper()
    pengarang = input("Masukkan Pengarang Baru: ").title()
    penerbit = input("Masukkan Penerbit Baru: ")
    kategori = input("Masukkan Kategori Baru: ")
    tipe = input("Masukkan Tipe Buku (Cetak/Ebook): ")
    jumlah = 0
    
    if tipe == "cetak":
        print("-"*60)
        jumlah = input("Masukkan Jumlah Baru: ")
    elif tipe == "ebook":
        jumlah += 1
    else:
        print('Tidak menerima kata di luar "Cetak" dan "Ebook". Form ditolak')
        print(jumlah)
        return
        
    listBuku[daftarTerpilih]["Judul Buku"] = judul
    listBuku[daftarTerpilih]["Pengarang"] = pengarang
    listBuku[daftarTerpilih]["Penerbit"] = penerbit
    listBuku[daftarTerpilih]["Kategori"] = kategori
    listBuku[daftarTerpilih]["Tipe Buku"] = tipe
    listBuku[daftarTerpilih]["Jumlah"] = jumlah

    
    print("-"*60)
    print(f"Selamat Anda berhasil mengubah informasi {judul}")
    lihat_menuBukuAdmin()


def hapus_buku():    
    lihat_bukuAdmin(muncul_menuAdmin = False)

    daftarTerpilih = input(f"Masukkan angka daftar yang ingin Anda hapus: ")
    
    if not daftarTerpilih.isdigit() or "." in daftarTerpilih:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        hapus_buku()
        return
    
    daftarTerpilih = int(daftarTerpilih) - 1
    
    if daftarTerpilih >= len(listBuku) or daftarTerpilih < 0:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        print("-"*60)
        hapus_buku()
        return
    
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus buku dari daftar (Ya/Tidak)? ").lower()
    if konfirmasi == "ya":
        infoTerhapus = listBuku.pop(daftarTerpilih)
        print("-"*60)
        print(f"Selamat Anda berhasil menghapusnya dari daftar buku")
        lihat_menuBukuAdmin()
    elif konfirmasi == "tidak":
        print("-"*60)
        lihat_bukuAdmin()
    else:
        print("-"*60)
        print('Tidak menerima kata di luar "Ya" dan "Tidak"')
        print("-"*60)
        hapus_buku()
  

# =================================================================#
# =================================================================#


def lihat_menuAkunAdmin():
    print(f"""{"="*60}
Akun
1. Lihat Daftar Akun
2. Tambah Akun
3. Hapus Akun
4. Kembali""")
    
    menuTerpilih = input("Masukkan angka aksi yang ingin Anda lakukan [1-4]: ")

    if not menuTerpilih.isdigit() or "." in menuTerpilih:
        print(
            "pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-4]")

    menuTerpilih = int(menuTerpilih)
    if menuTerpilih == 1:
        print("-"*60)
        lihat_akunAdmin(muncul_menuAdmin = True)
    elif menuTerpilih == 2:
        print("-"*60)
        tambah_akun()
    elif menuTerpilih == 3:
        print("-"*60)
        hapus_akun()
    elif menuTerpilih == 4:
        print("-"*60)
        lihat_menuAdmin()
    else:
        print("-"*60)
        print("pilihan menu tidak valid, silakan masukkan angka aksi yang ingin Anda lakukan [1-4]")  
        lihat_menuAkunAdmin()  


def lihat_akunAdmin(muncul_menuAdmin = True):
    for index, i in enumerate(listAkun):
        info1 = i["Full Name"].title()
        info2 = i["Username"].lower()
        info4 = i["Age"]
        info5 = i["Domisili"]
        info6 = i["Favorite Genre"]
        info7 = i["Registration Date"]
        info8 = i["Role"]
        
        print(f"{index+1}. {info1}")
        print(f"""Username: {info2}
Age: {info4}
Domisili: {info5}
Favorite Genre: {info6}
Registration Date: {info7}
Role: {info8}""")
        print("-"*60)
    
    if muncul_menuAdmin:
        lihat_menuAkunAdmin()


def tambah_akun():
    fullname = input("Full Name: ").title()
    username = input("Username: ").lower()
    password = input("Password: ")
    age = input("Age: ")
    domisili = input("Domisili: ").lower()
    favGenre = input("Favorite Genre: ").lower()
    regDate = input("Registration Date (yyyymmdd): ")
    
    akunFound = [i for i in listAkun if i["Username"] == username]

    if akunFound:
        print("Username sudah digunakan. Form ditolak silakan coba lagi")
        tambah_akun()
    elif not age.isdigit() or "." in age:
        print("Age hanya menerima angka bulat. Form ditolak silakan coba lagi")
        tambah_akun()
    elif not regDate.isdigit() or "." in regDate or "-" in regDate or len(regDate) != 8:
        print("Registration date hanya menerima format yyyymmdd. Form ditolak silakan coba lagi")
        tambah_akun()
        return
      
    cek1 = int(regDate[0 : 4])
    cek2 = int(regDate[4 : 6])
    cek3 = int(regDate[6 : 8])
    
    if cek1 != 2025 or cek2 != 6 or cek3 != 11:
        print("Registration date hanya bisa diisi tanggal hari ini. Form ditolak silakan coba lagi")
        tambah_akun()
        return
    
    akunBaru = {
        "Full Name": fullname,
        "Username": username,
        "Password": password,
        "Age": age,
        "Domisili": domisili,
        "Favorite Genre": favGenre,
        "Registration Date": regDate,
        "Role": "Tamu"
    }
    
    listAkun.append(akunBaru)
    print("-"*60)
    print(f"Selamat akun {fullname} berhasil ditambahkan sebagai tamu Perpustakaan Purwadhika")
    lihat_menuAkunAdmin()


def hapus_akun():    
    lihat_akunAdmin(muncul_menuAdmin = False)

    daftarTerpilih = input(f"Masukkan angka daftar yang ingin Anda hapus: ")
    
    if not daftarTerpilih.isdigit() or "." in daftarTerpilih:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        hapus_akun()
        return
    
    daftarTerpilih = int(daftarTerpilih) - 1
    
    if daftarTerpilih >= len(listAkun) or daftarTerpilih < 0:
        print("pilihan daftar tidak valid, silakan masukkan angka daftar yang ingin Anda hapus")
        print("-"*60)
        hapus_akun()
        return
    
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus akun dari daftar (Ya/Tidak)? ").lower()
    if konfirmasi == "ya":
        infoTerhapus = listAkun.pop(daftarTerpilih)
        print("-"*60)
        print(f"Selamat Anda berhasil menghapusnya dari daftar akun")
        lihat_menuAkunAdmin()
    elif konfirmasi == "tidak":
        print("-"*60)
        lihat_akunAdmin()
    else:
        print("-"*60)
        print('Tidak menerima kata di luar "Ya" dan "Tidak"')
        print("-"*60)
        hapus_akun()


lihat_menuUmum()
