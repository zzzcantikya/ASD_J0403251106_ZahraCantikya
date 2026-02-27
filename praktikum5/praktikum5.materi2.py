# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================
def hitung(n):
    # Base case berhenti ketika n = 0
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n) # fase stacking (fungsi sedang memanggil dirinya sendiri)
    hitung(n - 1) # pemanggilan rekursif dengan n yang lebuh kecil (n-1)
    print("Keluar:", n) # fase unwinding (kembali naik setelah selesai memanggil dirinya sendiri)

hitung(3)

#pada case di atas, fungsi yang pertama kali dipanggil adalah hitung(3).
#  Fungsi ini akan memanggil dirinya sendiri dengan n=2, lalu n=1, dan akhirnya n=0.
#  Ketika mencapai n=0, fungsi mencetak "Selesai" dan mulai kembali ke panggilan sebelumnya (unwinding), mencetak "Keluar: 1", "Keluar: 2", dan "Keluar: 3" secara berurutan.