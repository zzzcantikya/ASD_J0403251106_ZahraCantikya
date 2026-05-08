#=========================================
# Praktikum 3 - Konversi Matrix ke List
# Nama : Zahra Cantikya Paragasthya
# Nim : J0403251106
# Kelas : A2
#=========================================

def matrixToList(matrix):
    V = len(matrix)  # jumlah node dari ukuran matrix
    adj = {i: [] for i in range(V)}  # buat dictionary kosong

    # loop setiap sel matrix
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == 1:  # kalau ada edge maka,
                adj[i].append(j)   # tambah ke adjacency list
    return adj

if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    adj = matrixToList(matrix)  # konversi matrix ke list

    print("Adjacency List Representation:")
    for i in adj:
        print(f"{i}:", end=" ")   # cetak nama node
        for j in adj[i]:
            print(j, end=" ")     # cetak node tetangganya
        print()