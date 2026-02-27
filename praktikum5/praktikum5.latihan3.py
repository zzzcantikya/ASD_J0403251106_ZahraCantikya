# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0): 

    # Base case : jika index sudah mencapai elemen terakhir, kembalikan elemen tersebut sebagai maksimum
    if index == len(data) - 1:
        return data[index]

    # Recursive case : cari maksimum dari sisa list
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa: # jika elemen saat ini lebih besar dari maksimum sisa, kembalikan elemen saat ini
        return data[index] 
    else:
        return maks_sisa # jika maksimum sisa lebih besar atau sama dengan elemen saat ini, kembalikan maksimum sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka)) # Output: Nilai maksimum: 9

# pada contoh di atas, fungsi cari_maks dipanggil dengan list angka dan index awal 0.
# fungsi ini akan membandingkan elemen saat ini dengan hasil maksimum dari sisa list yang dihitung secara rekursif.
# Base case terjadi ketika index mencapai elemen terakhir, di mana fungsi mengembalikan nilai elemen tersebut sebagai maksimum. 
# Recursive case terjadi ketika fungsi memanggil dirinya sendiri dengan index yang lebih besar untuk mencari maksimum dari sisa list, 
# lalu membandingkannya dengan elemen saat ini untuk menentukan nilai maksimum yang akan dikembalikan.
