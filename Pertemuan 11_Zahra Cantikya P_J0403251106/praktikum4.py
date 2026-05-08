#===============================================================================
# Praktikum 4 - Studi kasus dunia nyata : Peta Kota Sekitar Cianjur, Jawa Barat
# Nama : Zahra Cantikya Paragasthya
# Nim : J0403251106
# Kelas : A2
#===============================================================================

# ADJACENCY LIST
graph = {
    "Cianjur":        ["Bandung", "Sukabumi", "Bogor"],
    "Bandung":        ["Cianjur", "Sukabumi"],
    "Sukabumi":       ["Cianjur", "Bandung", "Bogor"],
    "Bogor":          ["Cianjur", "Sukabumi", "Pelabuhan Ratu"],
    "Pelabuhan Ratu": ["Bogor"]
}

# ADJACENCY MATRIX 
# Urutan: Cianjur=0, Bandung=1, Sukabumi=2, Bogor=3, Pelabuhan Ratu=4
nodes = ["Cianjur", "Bandung", "Sukabumi", "Bogor", "Pelabuhan Ratu"]

matrix = [
#    Cjr  Bdg  Skb  Bgr  Plb
    [ 0,   1,   1,   1,   0 ],  # Cianjur
    [ 1,   0,   1,   0,   0 ],  # Bandung
    [ 1,   1,   0,   1,   0 ],  # Sukabumi
    [ 1,   0,   1,   0,   1 ],  # Bogor
    [ 0,   0,   0,   1,   0 ],  # Pelabuhan Ratu
]

# TAMPILKAN ADJACENCY LIST
print("=" * 50)
print("    ADJACENCY LIST - PETA SEKITAR CIANJUR")
print("=" * 50)
for kota, tetangga in graph.items():
    print(f"{kota:16}: {' --- '.join(tetangga)}")

# TAMPILKAN ADJACENCY MATRIX
print("\n" + "=" * 50)
print("    ADJACENCY MATRIX - PETA SEKITAR CIANJUR")
print("=" * 50)

# header kolom
print(f"{'':16}", end="")
for n in nodes:
    print(f"{n[:3]:>6}", end="")
print()

# isi matrix
for i, row in enumerate(matrix):
    print(f"{nodes[i]:16}", end="")
    for val in row:
        print(f"{val:>6}", end="")
    print()

# TAMPILKAN NODE DAN EDGE 
print("\n" + "=" * 50)
print("    NODE DAN EDGE")
print("=" * 50)
print(f"Jumlah Node : {len(nodes)}")
print(f"Nama Node   : {', '.join(nodes)}")

print("\nDaftar Edge (Hubungan Antar Kota):")
edges_printed = set()
for kota, tetangga in graph.items():
    for t in tetangga:
        edge = tuple(sorted([kota, t]))
        if edge not in edges_printed:
            print(f"  {kota} --- {t}")
            edges_printed.add(edge)

print(f"\nJumlah Edge : {len(edges_printed)}")