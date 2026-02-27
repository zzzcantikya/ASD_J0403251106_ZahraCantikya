# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    if n == 0: # Base case: jika n mencapai 0, print "Selesai" dan kembali
        print("Selesai")
        return
    
    print("Masuk:", n) # fase stacking (fungsi sedang memanggil dirinya sendiri)

    countdown(n - 1) # pemanggilan rekursif dengan n yang lebih kecil (n-1)

    print("Keluar:", n) # fase unwinding (kembali naik setelah selesai memanggil dirinya sendiri)

countdown(3)  
# Output: Masuk: 3
#         Masuk: 2    
#         Masuk: 1
#         Selesai
#         Keluar: 1
#         Keluar: 2
#         Keluar: 3

#  Alasan mengapa output 'keluar' muncul terbalik:
#  Output "Keluar" muncul terbalik karena setiap pemanggilan fungsi disimpan dalam struktur stack (tumpukan).
#  Fungsi akan terus menumpuk hingga mencapai base case. Setelah itu, fungsi akan selesai satu per satu mulai dari yang terakhir dipanggil.
#  Karena stack bekerja dengan prinsip LIFO (Last In, First Out), maka yang terakhir masuk akan keluar lebih dulu. 