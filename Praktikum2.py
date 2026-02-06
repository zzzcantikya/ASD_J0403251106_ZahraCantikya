#===============================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 1 : Membuat fungsi Load Data dari File
#===============================================================

#variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file :
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",")
            data_dict[nim]={"nama": nama, "nilai" : int(nilai)}
        return data_dict
    
#buka_data = baca_data(nama_file) #memanggil fungsi load data
print("jumlah data terbaca",baca_data)

#===============================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 2 : Membuat fungsi Menampilkan Data
#===============================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n==============Daftar Mahasiswa==============")
    print("{: <10} | {: <20} | {: <5}".format("NIM", "Nama", "nilai"))
    print("-" * 40)  #membuat garis

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <20} | {nilai: <5}")
        
#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 3 : Membuat fungsi Mencari Data
#=================================================================

#membuat  fungsi pencarian data
def cari_data(data_dict):
    nim_cari = input("Masukkan NIM Mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("========== Data Mahasiswa Ditemukan ==========")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi cari data
#cari_data(buka_data)

#====================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 4 : Membuat fungsi Update Data
#====================================================================

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim/ data mahasiswa yang ingin diupdate
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = input("Masukkan nilai baru 0-100 : ").strip()
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0-100. Update dibatalkan")
       
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru  

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi update data
#ubah_data(buka_data)

#====================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 5 : Membuat fungsi Menyimpan Data pada File
#====================================================================

#membuat fungsi simpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in data_dict:
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file, buka_data) #memanggil fungsi simpan data
print("Data berhasil disimpan ke file: ", nama_file)

#====================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 6 : Membuat menu interaktif
#====================================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fs.1 fungsi load data

    while True:
        print("\n===== Menu Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #fs 2 menampilkan data
        elif pilihan == "2":
            cari_data(buka_data) #memanggil fs.3 mencari data
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data) #memanggil fs.4 menyimpan data
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()  