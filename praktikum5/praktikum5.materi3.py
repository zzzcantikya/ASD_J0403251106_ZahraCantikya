# ==========================================================
def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data): #jika index sudah sama dengan panjang data, artinya kita sudah melewati semua elemen dalam list
        return 0 #fungsi mengembalikan 0 sebagai nilai dasar untuk penjumlahan

    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1) #fungsi memanggil dirinya sendiri dengan index yang lebih besar (index + 1) untuk menjumlahkan elemen berikutnya dalam list

print(jumlah_list([2, 4, 6, 8])) # Output: 20

# pada contoh di atas memanggil fungsi jumlah_list dengan list [2, 4, 6, 8] dan index awal 0. 
# Lalu fungsi ini akan menjumlahkan elemen-elemen dalam list dengan memanggil dirinya sendiri secara rekursif,
# jika sudah mencapai index yang sama dengan panjang list, maka fungsi akan berhenti dan mengembalikan hasil penjumlahan saat unwinding kembali ke panggilan awal.