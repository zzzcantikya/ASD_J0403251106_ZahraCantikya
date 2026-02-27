# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    
    if len(hasil) == panjang: # jika panjang hasil sudah sama dengan panjang yang diinginkan, artinya sudah membentuk PIN yang lengkap, maka kita cetak hasilnya
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]: #fungsi melakukan iterasi untuk setiap angka dalam list ["0", "1", "2"], dan untuk setiap angka tersebut
        buat_pin(panjang, hasil + angka) #fungsi memanggil dirinya sendiri dengan menambahkan angka saat ini ke hasil, agar bisa mencoba semua kemungkinan kombinasi PIN dengan angka 0, 1, dan 2 pada posisi tersebut.

buat_pin(3) # output: semua kombinasi PIN dengan panjang 3 yang terdiri dari angka 0, 1, dan 2 (misalnya: 000, 001, 002, ..., 222)

# Bagaimana cara mencegah angka yang sama muncul berulang?
# Cara mencegah angka yang sama muncul berulang yaitu dengan menambahkan kondisi untuk memeriksa apakah angka yang akan ditambahkan ke hasil sudah ada dalam hasil saat ini atau belum.
# Jika sudah ada, maka kita bisa melewati penambahan angka tersebut dan melanjutkan ke angka berikutnya dalam iterasi.
# Dengan cara ini, kita hanya akan menghasilkan kombinasi PIN yang unik tanpa angka yang sama muncul berulang.