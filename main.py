# ============================================================
#   APLIKASI SHOWROOM MOBIL - Capstone Project Module 1
# ============================================================

import mysql.connector
import matplotlib.pyplot as plt

def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="292614wwraZ-",
        database="showroom_db"
    )

def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")

def garis(k="=", n=60):
    print(k * n)


# ============================================================
# 1. TAMPILKAN DATA MOBIL
# ============================================================

def tampilkan_data():
    while True:
        garis()
        print("  TAMPILKAN DATA")
        garis("-")
        print("  1. Table Cars")
        print("  2. Table Transactions")
        print("  0. Kembali")
        garis()
        p = input("  Pilihan: ").strip()

        if p == "0":
            break

        db = conn()
        cur = db.cursor()

        if p == "1":
            cur.execute("SELECT id_mobil, merk, Jenis_mobil, Harga_beli, Harga_jual FROM cars")
            rows = cur.fetchall()
            garis()
            print("  TABLE CARS")
            garis("-")
            print(f"  {'ID':<5} {'Merk':<22} {'Jenis':<10} {'Harga Beli':<22} {'Harga Jual'}")
            garis("-")
            for r in rows:
                print(f"  {r[0]:<5} {r[1]:<22} {r[2]:<10} {rupiah(r[3]):<22} {rupiah(r[4])}")
            garis()

        elif p == "2":
            cur.execute("SELECT id_dijual, merk, Harga_jual, di_bayar, pembeli FROM `transaction`")
            rows = cur.fetchall()
            garis()
            print("  TABLE TRANSACTIONS")
            garis("-")
            print(f"  {'ID':<5} {'Merk':<22} {'Harga Jual':<22} {'Di Bayar':<22} {'Pembeli'}")
            garis("-")
            for r in rows:
                print(f"  {r[0]:<5} {r[1]:<22} {rupiah(r[2]):<22} {rupiah(r[3]):<22} {r[4]}")
            garis()

        else:
            print("  [!] Pilihan tidak valid.")

        cur.close()
        db.close()


# ============================================================
# 2. TAMBAH MOBIL BARU (dengan password)
# ============================================================

def tambah_mobil():
    garis()
    print("  Masukkan Password (hint: tempat sekarang menimba ilmu)")
    garis("-")
    if input("  Password: ").strip() != "purwadhika":
        print("  [!] Password salah! Akses ditolak.")
        return
    print("  [OK] Akses diberikan.\n")

    db = conn()
    cur = db.cursor()

    cur.execute("SELECT MAX(id_mobil) FROM cars")
    id_baru = (cur.fetchone()[0] or 0) + 1
    print(f"  ID Otomatis : {id_baru}")

    merk = input("  Merk        : ").strip()
    if not merk:
        print("  [!] Merk tidak boleh kosong.")
        return

    print("  Jenis: [1] Bensin  [2] Listrik")
    jenis = {"1": "bensin", "2": "listrik"}.get(input("  Pilih: ").strip())
    if not jenis:
        print("  [!] Pilihan tidak valid.")
        return

    try:
        h_beli = float(input("  Harga Beli  : ").replace(".", "").replace(",", ""))
        h_jual = float(input("  Harga Jual  : ").replace(".", "").replace(",", ""))
    except ValueError:
        print("  [!] Harga harus angka.")
        return

    print(f"\n  {id_baru} | {merk} | {jenis} | {rupiah(h_beli)} | {rupiah(h_jual)}")
    if input("  Simpan? [y/n]: ").strip().lower() == "y":
        cur.execute("INSERT INTO cars VALUES (%s,%s,%s,%s,%s)", (id_baru, merk, jenis, h_beli, h_jual))
        db.commit()
        print(f"  [OK] '{merk}' berhasil ditambahkan!")
    else:
        print("  [!] Dibatalkan.")

    cur.close()
    db.close()


# ============================================================
# 3. HITUNG RATA-RATA HARGA JUAL
# ============================================================

def rata_rata_harga():
    db = conn()
    cur = db.cursor()
    cur.execute("SELECT AVG(Harga_jual), MIN(Harga_jual), MAX(Harga_jual) FROM cars")
    avg, mn, mx = cur.fetchone()
    garis()
    print("  RATA-RATA HARGA JUAL MOBIL")
    garis("-")
    print(f"  Rata-rata : {rupiah(avg)}")
    print(f"  Minimum   : {rupiah(mn)}")
    print(f"  Maksimum  : {rupiah(mx)}")
    garis()
    cur.close()
    db.close()


# ============================================================
# 4. VISUALISASI DATA
# ============================================================

def visualisasi():
    while True:
        print("\n  [1] Pie Chart Jenis  [2] Histogram Harga  [3] Bar Chart Top 10  [0] Kembali")
        p = input("  Pilihan: ").strip()
        if p == "0":
            break

        db = conn()
        cur = db.cursor()

        if p == "1":
            cur.execute("SELECT Jenis_mobil, COUNT(*) FROM cars GROUP BY Jenis_mobil")
            data = cur.fetchall()
            plt.pie([r[1] for r in data], labels=[r[0] for r in data], autopct="%1.1f%%", colors=["#4A90D9", "#E67E22"])
            plt.title("Proporsi Jenis Mobil")
            plt.show()

        elif p == "2":
            cur.execute("SELECT Harga_jual FROM cars")
            harga = [float(r[0]) / 1e6 for r in cur.fetchall()]
            plt.hist(harga, bins=8, color="#2ECC71", edgecolor="white")
            plt.title("Distribusi Harga Jual (Juta Rp)")
            plt.xlabel("Harga Jual (Juta)")
            plt.ylabel("Jumlah Mobil")
            plt.show()

        elif p == "3":
            cur.execute("SELECT merk, Harga_jual FROM cars ORDER BY Harga_jual DESC LIMIT 10")
            data = cur.fetchall()
            plt.barh([r[0] for r in data][::-1], [float(r[1]) / 1e6 for r in data][::-1], color="#9B59B6")
            plt.title("Top 10 Mobil Harga Jual Tertinggi")
            plt.xlabel("Harga Jual (Juta Rp)")
            plt.tight_layout()
            plt.show()

        cur.close()
        db.close()


# ============================================================
# MENU UTAMA
# ============================================================

def main():
    while True:
        garis()
        print("       APLIKASI SHOWROOM MOBIL")
        garis("-")
        print("  1. Tampilkan data mobil")
        print("  2. Tambah mobil baru")
        print("  3. Hitung rata-rata harga jual mobil")
        print("  4. Tampilkan visualisasi data")
        print("  5. Keluar dari program")
        garis()
        p = input("  Masukkan pilihan Anda (1-5): ").strip()

        if p == "1":   tampilkan_data()
        elif p == "2": tambah_mobil()
        elif p == "3": rata_rata_harga()
        elif p == "4": visualisasi()
        elif p == "5":
            print("  Sampai jumpa! 🚗")
            break
        else:
            print("  [!] Pilihan tidak valid. Masukkan angka 1-5.")

if __name__ == "__main__":
    main()