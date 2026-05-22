# Nama  : Zahra Cantikya Paragasthya
# NIM   : j0403251106
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

import heapq

# Representasi graph berbobot menggunakan dictionary
# Bobot merepresentasikan jarak antar kota
graph = {
    'Bogor'  : {'Jakarta': 5, 'Depok': 2},
    'Depok'  : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga, kecuali node awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue menyimpan (jarak, node), node terkecil diproses duluan
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dan perbarui jarak jika ditemukan yang lebih kecil
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Penentuan node awal
start_node = 'Bogor'
hasil = dijkstra(graph, start_node)

# Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")


# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor.
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Node yang memiliki jarak paling kecil dari Bogor adalah Depok, dengan jarak 2.
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# node yang memiliki jarak paling besar dari Bogor adalah Bandung, dengan jarak 8.
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Dimulai dari Bogor (jarak 0). Priority queue memproses Depok (2) lebih dahulu
# karena bobotnya terkecil. Dari Depok ditemukan Jakarta = 2+2 = 4, lebih kecil
# dari jalur langsung Bogor->Jakarta = 5, sehingga jarak Jakarta diperbarui ke 4.
# Dari Depok juga ditemukan Bandung = 2+6 = 8. Dari Jakarta ditemukan Bandung = 4+7 = 11,
# namun 8 lebih kecil sehingga jarak Bandung tetap 8.
# Proses selesai saat priority queue kosong dan semua jarak sudah final.