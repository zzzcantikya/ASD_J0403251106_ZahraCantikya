# Nama  : Zahra Cantikya Paragasthya
# NIM   : J0403251106
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Tugas Mandiri: MST Jaringan Jalan Antar Kota
# Kasus 1 - Menggunakan Algoritma Kruskal + Union-Find
# ==========================================================

# Representasi weighted graph: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor',  'Jakarta'),
    (2, 'Bogor',  'Depok'),
    (3, 'Depok',  'Jakarta'),
    (6, 'Jakarta','Bandung'),
    (4, 'Depok',  'Bandung')
]

# --- Union-Find ---
parent = {}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return False
    parent[root_v] = root_u
    return True

# Inisialisasi parent
nodes = set()
for _, u, v in edges:
    nodes.add(u)
    nodes.add(v)
for node in nodes:
    parent[node] = node

# Urutkan berdasarkan bobot terkecil
edges.sort()

mst = []
total_bobot = 0

print("=" * 50)
print("  MST - Jaringan Jalan Antar Kota (Kruskal)")
print("=" * 50)
print("\nProses pemilihan jalan:")
print("-" * 50)

for bobot, u, v in edges:
    if union(u, v):
        mst.append((u, v, bobot))
        total_bobot += bobot
        print(f"✔ Dipilih : {u} -- {v}  (jarak={bobot} km)")
    else:
        print(f"✘ Dilewati: {u} -- {v}  (jarak={bobot} km) → cycle")

print("-" * 50)
print("\nMinimum Spanning Tree (Rute Jalan Optimal):")
for edge in mst:
    print(f"  {edge[0]} <--> {edge[1]}  [{edge[2]} km]")
print(f"\nTotal jarak minimum = {total_bobot} km")
print("=" * 50)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 1: Jaringan Jalan Antar Kota (Bogor, Depok, Jakarta, Bandung).
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal dengan struktur data Union-Find (deteksi cycle akurat).
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Bogor - Depok (2), Depok - Jakarta (3), Depok - Bandung (4)
#    Total 3 edge untuk 4 kota (N-1 = 3).
#
# 4. Berapa total bobot MST?
#    Total = 2 + 3 + 4 = 9 km
#
# 5. Mengapa edge tertentu tidak dipilih?
#    - Bogor-Jakarta (5): Bogor & Jakarta sudah terhubung via Bogor->Depok->Jakarta,
#      memilihnya akan membentuk cycle.
#    - Jakarta-Bandung (6): Jakarta & Bandung sudah terhubung via Jakarta->Depok->Bandung,
#      memilihnya juga membentuk cycle dan bobotnya paling besar.