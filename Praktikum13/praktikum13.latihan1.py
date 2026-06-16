# Nama  : Zahra Cantikya Paragasthya
# NIM   : J0403251106
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree


# Daftar edge graph (sesuai gambar: A-B, A-C, A-D, B-D, C-D)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('B', 'D'),
    ('C', 'D')
]

# Contoh spanning tree yang valid (3 edge untuk 4 node, tanpa cycle)
spanning_tree = [
    ('A', 'B'),
    ('A', 'C'),
    ('C', 'D')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki semua edge termasuk yang membentuk cycle (A-D, B-D, C-D membentuk cycle).
#    Spanning tree hanya memilih edge secukupnya untuk menghubungkan semua node tanpa cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle berarti ada jalur berulang yang tidak efisien. Spanning tree
#    harus menghubungkan semua node dengan edge seminimal mungkin (tree = acyclic).
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk graph dengan N node, spanning tree selalu memiliki tepat N-1 edge.
#    Graph awal bisa memiliki lebih banyak edge karena membolehkan cycle.
#    Di sini: 4 node -> 3 edge pada spanning tree, graph asal punya 5 edge.