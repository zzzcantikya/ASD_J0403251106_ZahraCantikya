# Nama  : Zahra Cantikya Paragasthya
# NIM   : J0403251106
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Studi Kasus: Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

# Representasi weighted graph sebagai daftar edge (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# --- Union-Find untuk deteksi cycle yang lebih akurat ---
parent = {}

def find(node):
    """Mencari root/representatif dari suatu node."""
    if parent[node] != node:
        parent[node] = find(parent[node])  # path compression
    return parent[node]

def union(u, v):
    """Menggabungkan dua kelompok node."""
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return False  # Sudah terhubung, akan membentuk cycle
    parent[root_v] = root_u
    return True

# Inisialisasi parent untuk setiap node
nodes = set()
for _, u, v in edges:
    nodes.add(u)
    nodes.add(v)
for node in nodes:
    parent[node] = node

# Urutkan edge berdasarkan biaya (bobot) terkecil
edges.sort()

mst = []
total_biaya = 0

print("Proses pemilihan kabel (Algoritma Kruskal):")
print("-" * 45)

for biaya, u, v in edges:
    if union(u, v):
        mst.append((u, v, biaya))
        total_biaya += biaya
        print(f"✔ Dipilih : {u} - {v} (biaya={biaya})")
    else:
        print(f"✘ Dilewati: {u} - {v} (biaya={biaya}) → membentuk cycle")

print("-" * 45)
print("\nJaringan Kabel Minimum (MST):")
for edge in mst:
    print(f"  {edge[0]} <--> {edge[1]}, biaya = {edge[2]}")
print(f"\nTotal biaya minimum = {total_biaya}")

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal dengan Union-Find untuk deteksi cycle.
#
# 2. Edge mana saja yang dipilih?
#    GedungC - GedungD (1), GedungA - GedungC (2), GedungB - GedungD (3)
#
# 3. Berapa total biaya minimum?
#    Total biaya = 1 + 2 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST menjamin semua gedung terhubung dengan total panjang/biaya kabel
#    seminimal mungkin tanpa jalur berulang (redundant). Sangat efisien
#    untuk perencanaan infrastruktur jaringan.