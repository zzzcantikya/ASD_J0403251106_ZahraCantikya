# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================
def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1) #fungsi memanggil dirinya sendiri dengan menambahkan '0' ke hasil saat ini dengan tanpa mengubah jumlah_1 
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) #fungsi memanggil dirinya sendiri dengan menambahkan '1' ke hasil saat ini, dan juga menambahkan 1 ke jumlah_1 

biner_batas(4, 2)
#pada contoh di atas, fungsi biner_batas dipanggil dengan n=4 dan batas=2, yang artinya kita ingin menghasilkan semua kombinasi biner dengan panjang 4, tetapi hanya boleh memiliki maksimal 2 '1'.