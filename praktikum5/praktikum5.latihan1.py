# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n): #fungsi untuk menghitung a pangkat n
 
    # Base case: jika n = 0, kembalikan 1 (karena a^0 = 1)
    if n == 0:
        return 1

    # Recursive case : a * pangkat(a, n - 1) (karena a^n = a * a^(n-1))
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

#contoh di atas memanggil fungsi pangkat dengan a=2 dan n=4, yang kemudian memanggil dirinya sendiri
#dengan n=3, n=2, n=1, dan berakhir n=0. Ketika mencapai n=0, fungsi mengembalikan 1,
#lalu kemudian hasilnya dikalikan kembali saat fungsi unwinding kembali ke panggilan awal, menghasilkan 16.