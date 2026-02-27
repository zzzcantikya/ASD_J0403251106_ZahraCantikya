# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n: #jika panjang hasil sudah sama dengan n, artinya sudah membentuk kombinasi biner yang lengkap, maka kita cetak hasilnya
        print(hasil)
        return
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") #fungsi memanggil dirinya sendiri dengan menambahkan '0' ke hasil saat ini, agar bisa mencoba semua kemungkinan kombinasi biner dengan '0' pada posisi tersebut.

    # Choose + Explore: tambah '1'
    biner(n, hasil + "1") #fungsi memanggil dirinya sendiri dengan menambahkan '1' ke hasil saat ini,

    biner(3)

#pada contoh di atas, fungsi biner dipanggil dengan n=3, yang berarti kita ingin menghasilkan semua kombinasi biner dengan panjang 3.