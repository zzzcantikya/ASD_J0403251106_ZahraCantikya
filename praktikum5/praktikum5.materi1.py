# ==========================================================
# Contoh Rekursi 1: Faktorial
# ==========================================================
def faktorial(n):
    # Base case: berhenti ketika n = 0
    if n == 0: 
        return 1 #fungsi mengembalikan nilai 1
    
    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1) #fungsi memanggil dirinya sendiri dengan n-1

print(faktorial(5)) # Output: 120

#contoh di atas memanggil fungsi faktorial dengan n=5, yang kemudian memanggil dirinya sendiri
#dengan n=4, n=3, n=2, n=1, dan berakhir n=0. Ketika mencapai n=0, fungsi mengembalikan 1,
#lalu kemudian hasilnya dikalikan kembali saat fungsi unwinding kembali ke panggilan awal.