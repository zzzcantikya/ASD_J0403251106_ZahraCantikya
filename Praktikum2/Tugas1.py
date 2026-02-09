# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :Zahra Cantikya Paragasthya
# NIM  :J0403251106
# Kelas:
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    stok_dict = {}  # dictionary untuk menyimpan data stok

    try:
        # membuka file dan membaca seluruh isinya
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()  # menghapus karakter newline
                kode, nama, stok = baris.split(",")
                stok_dict[kode] = {
                    "nama": nama,
                    "stok": int(stok)  
                }
    except FileNotFoundError:
        # jika file belum tersedia, data dianggap kosong
        pass

    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke dalam file teks.
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    if not stok_dict:
        print("Stok barang masih kosong.")
        return

    print("\n============== Daftar Barang Kantin ==============")
    print("{:<10} | {:<22} | {:<5}".format("Kode", "Nama Barang", "Stok"))
    print("-" * 45)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print("{:<10} | {:<22} | {:<5}".format(kode, nama, stok))

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambahkan barang baru ke dalam data stok.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    # validasi agar kode tidak duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return

    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print(f"Barang {nama} berhasil ditambahkan dengan stok {stok_awal}")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang dengan menambah atau mengurangi.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka")
        return

    nama_barang = stok_dict[kode]["nama"]

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print(f"Stok {nama_barang} berhasil diubah menjadi {stok_dict[kode]['stok']}")

    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh bernilai negatif")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print(f"Stok {nama_barang} berhasil diubah menjadi {stok_dict[kode]['stok']}")

    else:
        print("Pilihan tidak valid")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # membaca data stok dari file saat program dijalankan
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# menjalankan program utama
if __name__ == "__main__":
    main()
