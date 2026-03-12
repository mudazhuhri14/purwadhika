============================================================
   README — APLIKASI SHOWROOM MOBIL
   Capstone Project Module 1
   Purwadhika Digital Technology School
============================================================

------------------------------------------------------------
INFORMASI PROYEK
------------------------------------------------------------
Nama Proyek       : Aplikasi Showroom Mobil
Bahasa            : Python 3
Database          : MySQL (showroom_db)
Library           : mysql.connector, matplotlib
Institusi         : Purwadhika Digital Technology School

------------------------------------------------------------
DESKRIPSI
------------------------------------------------------------
Aplikasi Showroom Mobil adalah program berbasis terminal (CLI)
yang terhubung langsung ke database MySQL. Aplikasi ini
memungkinkan pengguna untuk mengelola data kendaraan, melihat
data transaksi penjualan, serta menganalisis data melalui
visualisasi grafis.

------------------------------------------------------------
STRUKTUR DATABASE
------------------------------------------------------------
Database: showroom_db

Tabel 1 — cars
  - id_mobil      INT PRIMARY KEY       ID unik setiap mobil
  - merk          VARCHAR(100)          Nama merek mobil
  - Jenis_mobil   ENUM(listrik,bensin)  Jenis bahan bakar
  - Harga_beli    DECIMAL(15,2)         Harga pembelian
  - Harga_jual    DECIMAL(15,2)         Harga penjualan

Tabel 2 — transaction
  - id_dijual     INT PRIMARY KEY       ID transaksi (FK ke cars)
  - merk          VARCHAR(100)          Nama merek mobil
  - Harga_jual    DECIMAL(15,2)         Harga jual yang disepakati
  - di_bayar      DECIMAL(15,2)         Jumlah yang dibayarkan
  - pembeli       VARCHAR(100)          Nama pembeli

------------------------------------------------------------
FITUR APLIKASI
------------------------------------------------------------

1. TAMPILKAN DATA MOBIL
   Menampilkan data dari dua tabel MySQL:
   - Table Cars      : data seluruh mobil + harga beli & jual
   - Table Transaction : data transaksi penjualan + nama pembeli

   Query SQL:
   SELECT id_mobil, merk, Jenis_mobil, Harga_beli, Harga_jual
     FROM cars
   SELECT id_dijual, merk, Harga_jual, di_bayar, pembeli
     FROM `transaction`

2. TAMBAH MOBIL BARU
   Menambahkan data mobil baru ke tabel cars dengan proteksi
   password. Input: merek, jenis (bensin/listrik), harga beli,
   harga jual. ID di-generate otomatis.

   Query SQL:
   SELECT MAX(id_mobil) FROM cars
   INSERT INTO cars VALUES (%s, %s, %s, %s, %s)

3. HITUNG RATA-RATA HARGA JUAL
   Menampilkan statistik harga jual: rata-rata, minimum,
   dan maksimum dari seluruh data mobil.

   Query SQL:
   SELECT AVG(Harga_jual), MIN(Harga_jual), MAX(Harga_jual)
     FROM cars

4. VISUALISASI DATA
   Menampilkan tiga jenis grafik menggunakan matplotlib:
   - Pie Chart        : proporsi jenis mobil (categorical)
   - Histogram        : distribusi harga jual (numerical)
   - Bar Chart (H)    : Top 10 mobil harga jual tertinggi

   Query SQL:
   SELECT Jenis_mobil, COUNT(*) FROM cars GROUP BY Jenis_mobil
   SELECT Harga_jual FROM cars
   SELECT merk, Harga_jual FROM cars ORDER BY Harga_jual DESC LIMIT 10

------------------------------------------------------------
CARA MENJALANKAN
------------------------------------------------------------

Prasyarat:
  - Python 3.x sudah terinstall
  - MySQL Server sudah berjalan
  - Library mysql-connector-python dan matplotlib terinstall

Instalasi library:
  pip install mysql-connector-python matplotlib

Setup database:
  mysql -u root -p < showroom_db.sql

Jalankan program:
  python main.py

------------------------------------------------------------
STRUKTUR FILE
------------------------------------------------------------
  main.py          -> File utama program Python
  showroom_db.sql  -> Script pembuatan dan pengisian database
  README.txt       -> Dokumentasi proyek ini

------------------------------------------------------------
RINGKASAN QUERY SQL
------------------------------------------------------------
  No  Fungsi                        Jenis Query
  --  ----------------------------  -----------------------
  1   Tampilkan Table Cars          SELECT
  2   Tampilkan Table Transaction   SELECT
  3   Generate ID otomatis          SELECT MAX()
  4   Tambah mobil baru             INSERT INTO
  5   Statistik harga jual          SELECT AVG/MIN/MAX
  6   Pie chart jenis mobil         SELECT + GROUP BY
  7   Histogram harga jual          SELECT
  8   Bar chart top 10 mobil        SELECT + ORDER BY + LIMIT

============================================================
   Capstone Project Module 1 — Purwadhika Digital Technology School
============================================================
