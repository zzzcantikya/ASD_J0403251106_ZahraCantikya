# Nama  : Zahra Cantikya Paragasthya
# NIM   : j0403251106
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ========================================================== 
import heapq

graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'D': 5},
  'C': {'D': 1},
  'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B?
# jarak terpendek dari A ke B adalah 4, karena langsung dari A ke B dengan bobot 4
# 2. Berapa jarak terpendek dari A ke C?
# jarak terpendek dari A ke C adalah 2, karena langsung dari A ke C dengan bobot 2
# 3. Berapa jarak terpendek dari A ke D? 
# jarak terpendek dari A ke D adalah 3, karena melalui A -> C -> D dengan bobot 2 + 1 = 3
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# Karena jalur A -> C -> D memiliki total bobot yang lebih kecil (2 + 1 = 3) dibandingkan jalur A -> B -> D (4 + 5 = 9)
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# priority_queue digunakan untuk menyimpan node-node yang perlu dikunjungi, dengan urutan prioritas berdasarkan jarak 
# terpendek dari node awal.
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 
# Dijkstra mengasumsikan bahwa sekali sebuah node diproses dengan jarak terpendek, nilai tersebut sudah final dan tidak 
# akan berubah. Bobot negatif melanggar asumsi ini, ada kemungkinan ditemukan jalur yang lebih pendek setelah node sudah 
# "dikunci", sehingga hasil menjadi salah. Untuk bobot negatif, gunakan algoritma Bellman-Ford.