# Nama  : Zahra Cantikya Paragasthya
# NIM   : J0403251106
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node 'A' digunakan sebagai titik awal.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge (A, C) dengan bobot 2 dipilih pertama karena dari A,
#    edge ke C (bobot 2) lebih kecil dari ke B (4) dan D (5).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan priority queue (min-heap). Setiap kali node baru
#    dikunjungi, semua edge ke tetangganya yang belum dikunjungi
#    dimasukkan ke heap. Edge dengan bobot terkecil selalu dipilih duluan.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 2 + 1 + 3 = 6
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Prim: mulai dari 1 node, kembangkan MST bertahap ke node terdekat.
#    - Kruskal: urutkan semua edge, pilih edge terkecil yg tidak membentuk cycle.
#    - Prim cocok untuk graph padat, Kruskal cocok untuk graph jarang/sparse.