# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""): #
 
    if len(hasil) == n: # jika panjang hasil sudah sama dengan n, artinya sudah membentuk kombinasi yang lengkap, maka kita cetak hasilnya
        print(hasil)
        return
    
    kombinasi(n, hasil + "A") #fungsi memanggil dirinya sendiri dengan menambahkan 'A' ke hasil saat ini, agar bisa mencoba semua kemungkinan kombinasi dengan 'A' pada posisi tersebut.
    kombinasi(n, hasil + "B") #fungsi memanggil dirinya sendiri dengan menambahkan 'B' ke hasil saat ini, agar bisa mencoba semua kemungkinan kombinasi dengan 'B' pada posisi tersebut.

kombinasi(2) # output: AA, AB, BA, BB

# Bagaimana jumlah kombinasi yang dihasilkan?
# Pada contoh di atas, fungsi kombinasi dipanggil dengan n=2, yang berarti kita ingin menghasilkan
# semua kombinasi huruf 'A' dan 'B' dengan panjang 2. Kombinasi yang dihasilkan adalah: AA, AB, BA, BB.
# Jadi, total ada 4 kombinasi yang dihasilkan.