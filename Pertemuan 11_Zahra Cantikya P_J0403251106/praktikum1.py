#=========================================
# Praktikum 1 - Membuat adjacency matrix 
# Nama : Zahra Cantikya Paragasthya
# Nim : J0403251106
# Kelas : A2
#=========================================


def createGraph(V, edges):
    # Buat matrix V×V berisi semua 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Loop setiap edge yang ada
    for it in edges:
        u = it[0]  # node asal
        v = it[1]  # node tujuan
        mat[u][v] = 1  # tandai ada edge dari u ke v
        mat[v][u] = 1  # tandai sebaliknya (undirected)
    return mat  # kembalikan matrix yang sudah terisi

if __name__ == "__main__":
    V = 4  # jumlah node
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]  # daftar edge
    mat = createGraph(V, edges)  # buat graph

    print("Adjacency Matrix Representation:")
    for i in range(V):       # loop baris
        for j in range(V):   # loop kolom
            print(mat[i][j], end=" ")  # cetak nilai tiap sel
        print()  # pindah baris