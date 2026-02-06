#===============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#===============================================

print("====Membuka file dalam satu string====")
with open ("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("tipe data :", type(isi_file))

print("====Membuka file perbaris====")
jumlah_baris = 0 #inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-",jumlah_baris)
        print("isinya :", baris)

#======================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Membaca Data dan Menyimpannya ke Struktur Data List
#======================================================================

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print ("NIM :", nim, "| Nama:", nama, "| Nilai:", nilai) #Menampilkan satuan data dalam bentuk kolom

#======================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca Data dan Menyimpannya dalam List
#======================================================================

data_list = [] #inisialisasi untuk menampung data

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip() 
        nim, nama, nilai = baris.split(",")
        data_list.append([nim,nama,int(nilai)])
print("====Menampilkan List====")
print(data_list)
print("contoh record ke 1", data_list[0])
print("contoh record ke 2", data_list[1])

print("Jumlah Record", len(data_list) )

#===========================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca Data dan Menyimpannya ke Struktur Data Dictionary
#===========================================================================
data_dict = {} #inisialisasi dictionary


with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip() 
        nim, nama, nilai = baris.split(",")
        #simpa data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)

        }
print ("====Menampilkan Data Dictionary====")
print(data_dict)