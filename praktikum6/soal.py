# Data skor tes potensi akademik para pelamar
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Fungsi Merge Sort untuk mengurutkan data secara descending
def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        # Membagi list menjadi dua bagian
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        # Menggabungkan kembali dua bagian list dengan urutan dari terbesar ke terkecil
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                data[k] = lefthalf[i]
                i += 1
            else:
                data[k] = righthalf[j]
                j += 1
            k += 1

        # Memasukkan sisa elemen dari lefthalf jika masih ada
        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i += 1
            k += 1

        # Memasukkan sisa elemen dari righthalf jika masih ada
        while j < len(righthalf):
            data[k] = righthalf[j]
            j += 1
            k += 1


# Mengurutkan data nilai pelamar
mergeSort(data)

# Menampilkan skor dari yang tertinggi ke terendah
print("Skor setelah diurutkan (tertinggi ke terendah):")
print(data)

# Menampilkan lima kandidat dengan nilai tertinggi
print("\nLima kandidat dengan nilai tertinggi:")
for i in range(5):
    print(data[i])