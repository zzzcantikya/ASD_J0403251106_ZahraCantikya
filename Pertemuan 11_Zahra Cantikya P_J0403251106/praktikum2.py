#=========================================
# Praktikum 2 - Membuat adjacency list 
# Nama : Zahra Cantikya Paragasthya
# Nim : J0403251106
# Kelas : A2
#=========================================

def createGraph(V, edges):
    adj = {node: [] for node in V}  # buat dictionary kosong untuk tiap node

    # tambah setiap edge ke adjacency list
    for it in edges:
        u = it[0]  # node asal
        v = it[1]  # node tujuan
        adj[u].append(v)  # tambah v ke list u

        # karena Graph undirected
        adj[v].append(u)  # tambah u ke list v
    return adj

if __name__ == "__main__":
    V = ['A', 'B', 'C', 'D']  # node berupa huruf

    # daftar edge sesuai graph
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]

    adj = createGraph(V, edges)  # buat graph

    print("Adjacency List Representation:")
    for i in V:
        print(f"{i}:", end=" ")  # cetak nama node
        for j in adj[i]:
            print(j, end=" ")   # cetak node tetangganya
        print()