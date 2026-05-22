# Nama  : Zahra Cantikya Paragasthya
# NIM   : j0403251106
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B? 
# bobot langsung dari A ke B adalah 5
# 2. Berapa total bobot jalur A -> C -> B? 
# total bobot jalur A -> C -> B adalah 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# Jalur A -> C -> B (bobot 2) lebih kecil dibanding A -> B langsung (bobot 5)
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# Bellman-Ford merelaksasi semua edge sebanyak |V|-1 kali tanpa mengunci jarak, sehingga bobot negatif tetap bisa diproses dengan benar
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# Relaksasi edge yaitu memeriksa apakah dist[u] + w < dist[v], jika ya maka dist[v] diperbarui
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 
# Dijkstra langsung mengunci jarak node begitu diproses, artinya diasumsikan tidak ada jalur yang lebih pendek setelahnya. Asumsi ini
# hanya valid jika semua bobot positif. Jika ada bobot negatif, bisa saja jalur yang "dikunci" ternyata masih bisa dipersingkat, 
# sehingga hasil akhirnya salah.