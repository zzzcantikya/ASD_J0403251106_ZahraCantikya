# Nama  : Zahra Cantikya Paragasthya
# NIM   : j0403251106
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 

# Sebuah kampus memiliki beberapa lokasi yang saling terhubung. Bobot pada graph merepresentasikan
# perkiraan waktu tempuh dalam menit. Mahasiswa diminta menjalankan program untuk mmengetahui waktu
# tempuh terpendek dari Gerbang Kampus ke lokasi lainnya.

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
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


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Kantin, dengan waktu tempuh 2 menit.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 7 menit, melalui jalur Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7).
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak selalu. Jalur langsung Gerbang -> Kantin -> Aula membutuhkan 9 menit,
# sedangkan Gerbang -> Kantin -> Lab -> Aula hanya 7 menit.
# Jalur dengan lebih banyak node bisa menghasilkan total bobot yang lebih kecil.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena semua bobot bernilai positif (waktu tempuh tidak mungkin negatif).
# Dijkstra selalu menghasilkan jarak terpendek yang tepat untuk kondisi ini.